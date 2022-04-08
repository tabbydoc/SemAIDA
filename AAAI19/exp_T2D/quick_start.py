from predict_colnet import predict_colnet
from sample_general import read_cls_ents, query_gen_ents, write_gen_samples
from sample_particular import read_candidate_classes, read_ent_and_they_cls, generate_pos_sample, generate_neg_samples, \
    out_negative_samples
from evaluate_infer_col_gt import extract_classes_columns
from sample_lookup import read_table_cells, read_exist_ent_cls, lookup_ent_cls, write_ents_cls
from train_cnn import train_cnns
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--prediction_type',
    type=int,
    default=1,
    help='1 - predict colnet, 2 - predict lookup, 3 - predict assemble')
parser.add_argument(
    '--evaluation-type',
    type=int,
    default=2,
    help='1 - evaluate strict, 2 - evaluate tolerant')

FLAGS, unparsed = parser.parse_known_args()
if FLAGS.prediction_type not in {1, 2, 3}:
    print('Properties is wrong! Check the "prediction_type" property, it must be in [1,2,3]')

print('Step #1: extract column ground truth classes of columns of tables(T2Dv2)')

extract_classes_columns()

print('Step #2: generate samples for training')
print('----Lookup new Samples')
col_cells = read_table_cells()
cls_count, entities = read_exist_ent_cls()
cls_count, ent_cls = lookup_ent_cls(col_cells, entities, cls_count)
write_ents_cls(cls_count, ent_cls)

print('----Generate positive and negative samples')
cand_classes = read_candidate_classes()
ent_cls = read_ent_and_they_cls()
pos_samples = generate_pos_sample(cand_classes, ent_cls)
neg_samples = generate_neg_samples(pos_samples)
out_negative_samples(pos_samples, neg_samples)

print('----Generate general samples')
cls_ents = read_cls_ents()
cls_gen_ents = query_gen_ents(cls_ents)
write_gen_samples(cls_gen_ents)

print('Step #3 Train CNN-s')
train_cnns()

if 1 < FLAGS.prediction_type < 3:
    if FLAGS.prediction_type == 1:
        print('Step #4 Predict with ColNet')
        predict_colnet()
    if FLAGS.prediction_type == 2:
        print('Step #4 Predict with Look-up')
        pass
    if FLAGS.prediction_type == 3:
        print('Step #4 Predict by Colnet and Lookup')
        pass
