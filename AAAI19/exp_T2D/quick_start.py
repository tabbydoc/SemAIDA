from evaluate_infer_col_gt import extract_classes_columns
from sample_lookup import lookup_new_samples
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'prediction_type',
    type=int,
    default=1,
    help='1 - predict colnet, 2 - predict lookup, 3 - predict assemble')
parser.add_argument(
    'evaluation-type',
    type=int,
    default=2,
    help='1 - evaluate strict, 2 - evaluate tolerant')




print('Step #1: extract column ground truth classes of columns of tables(T2Dv2)')

extract_classes_columns()

lookup_new_samples()