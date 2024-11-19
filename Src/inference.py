import joblib
import os

def model_fn(model_dir):
    # Load the model from the specified directory
    model = joblib.load(os.path.join(model_dir, 'model.joblib'))
    return model

def predict_fn(input_data, model):
    # Perform prediction
    prediction = model.predict(input_data)
    return prediction
