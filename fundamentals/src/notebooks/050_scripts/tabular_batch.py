from azureml.core import Model
import joblib
import os


def init():
    global model
    model_path = Model.get_model_path("pipeline_model")
    model_location = os.path.join(model_path, "model.joblib")
    print(f"Loading model from {model_location}")
    model = joblib.load(model_location)


def run(mini_batch):
    print(mini_batch.info())
    mini_batch["target"] = model.predict(mini_batch)
    return mini_batch[["id", "target"]].values.tolist()
