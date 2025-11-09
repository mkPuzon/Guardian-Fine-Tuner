'''ft_pipeline.py

Fine-tunes a model for content moderation and logs improvement metrics.

Oct 2025
'''
import os

from load_data import load_json_dataset

def tokenize_text(tokenizer, raw_text):
    text = raw_text["text"]
    # tokenize and truncate
    tokenizer.truncation_side = "left"
    tokenized_inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        max_length=512
    )
    return tokenized_inputs

def tokenize_dataset(train_set, test_set, val_set):
    tkn_train_set = tokenize_text(train_set)
    tkn_test_set = tokenize_text(test_set)
    tkn_val_set = tokenize_text(val_set)
    return tkn_train_set, tkn_test_set, tkn_val_set
    
