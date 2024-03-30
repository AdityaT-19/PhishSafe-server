from app.feat import FeatureExtraction
from pathlib import Path
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

from tensorflow.keras.models import load_model


import numpy as np

file_path = Path(__file__).resolve()
dir_path = file_path.parent
model_path = dir_path / "phishing-website-detector.h5"

model = load_model(model_path)

def predict(url):
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)
    y_pred = model.predict(x)
    return y_pred