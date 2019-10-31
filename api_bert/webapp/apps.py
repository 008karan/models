from django.apps import AppConfig
import html
#import pathlib
from pathlib import Path 
import os
import torch

from fast_bert.prediction import BertClassificationPredictor

class WebappConfig(AppConfig):
    name = 'webapp'
    pwd=os.getcwd()
    HOME = os.environ["HOME"]
    #MODEL_PATH = Path("required_files")
    #BERT_PRETRAINED_PATH = Path(pwd+"/webapp/required_files/bert_model/uncased_L-12_H-768_A-12")
    #LABEL_PATH = Path(pwd+"/webapp/labels/")
    #predictor = BertClassificationPredictor(model_path=pwd+"/webapp/required_files/emotion_try.bin", pretrained_path=BERT_PRETRAINED_PATH, label_path=LABEL_PATH, multi_label=True)  
    LABEL_PATH=Path(pwd+"/webapp/labels/")
    MODEL_PATH=Path(pwd+"/webapp/model_out_bert")
    predictor = BertClassificationPredictor(
				model_path=MODEL_PATH,
				label_path=LABEL_PATH, # location for labels.csv file
				multi_label=False,
				model_type='bert',
				do_lower_case=True)
