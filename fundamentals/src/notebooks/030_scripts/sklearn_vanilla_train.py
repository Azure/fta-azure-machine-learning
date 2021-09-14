import argparse
import os
import joblib
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLars
from sklearn import datasets

# This script can run locally using
# python train.py --alpha 0.9
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, dest="alpha", help="The alpha parameter")
args = parser.parse_args()

# Tracking with mlflow
mlflow.sklearn.autolog()
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

pipe = make_pipeline(StandardScaler(), LassoLars(alpha=args.alpha))
pipe.fit(X, y)

os.makedirs("./outputs", exist_ok=True)
joblib.dump(value=pipe, filename="./outputs/custom_serialization.pkl")

print(os.environ.get("MY_VAR", "MY_VAR is not set"))
