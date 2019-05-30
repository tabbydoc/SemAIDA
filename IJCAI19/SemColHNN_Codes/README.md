Requirement:
    python 2.7, scikit-learn-0.20.3, tensorflow 1.13.1, gensim, csv, json, sparql-client 2.6

Notice: Table set "Wikipedia" in codes and data is "Efthymiou" table set in the paper.
    
Considering the following train-test context generated T2D_IO/col_split.py: 
    
    --T2D_IO/train_cols.json (T2D-Tr, 70%) for training;
    --T2D_IO/test_cols_t2d.json (T2D-Te, 30%) for testing;
    --T2D_IO/test_cols_limaye.json for testing
    --T2D_IO/test_cols_wikipedia.json for testing

Step #1 generate samples (samples.py):
    
    --sample_file_name: train_cols.json/test_cols_{t2d,limaye,wikipedia}.json (Input)
    --out_dir_name: T2D_IO/train_samples, T2D_IO/test_samples_{t2d,limaye,wikipedia} (Corresponding Output)
    --this step can be ignored as the samples are already in T2D_IO/

Step #2 train and test (RNN.py/CNN.py/HNN.py):
    
    --test_name (T2D, Limaye, Wikipedia)
    --col_filters: e.g., 2,3 and 2,3,4
    --row_filters: e.g., 2,3
    --output_fc: output the FC layer output or not (will be used in Ensemble I)
    --output_score: output the score or not (will be used in Ensemble II)
    
Step #3 generate property vectors (prop2vec.py):

    --sample_type: train_samples, test_samples_{wikipedia,t2d,limaye} (Input)
    --output_type: train_prop2vecs, test_prop2vecs_{wikipedia,t2d,limaye} (Corresponding Output)
    --properties.json is generated by properties.py

Step #4 train and test with property vectors (Baseline.py)
    
    --test_name: T2D, Limaye, Wikipedia
    --use_property_vector: set it to 'yes'
    
Step #5 ensemble (Ensemble1.py/Ensemble2.py)
    
    --test_name: T2D, Limaye, Wikipedia
    --feature_name (--score_name): the FC output (score) of which NN model 
    --see more in the head of Ensemble1.py and Ensemble2.py
    
Note the data name "Wikipedia" here refers to "Efthymiou" in the paper.

Those parameters that are not specifically mentioned above, can be set to the default.

set --wv_model to the word2vec model directory (one trained by Wikipedia article dump in 2018 can be downloaded by https://urlzs.com/ujAXZ)