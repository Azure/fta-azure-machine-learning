## :orange_circle: メトリック・ログの記録方法のガイドライン

Azure ML の実験 (Experiments) の各実行 (Runs) にメトリックやログの情報を紐づけて記録することができます。

### Azure ML Python SDK を利用する場合

Azure Machine Learning の Python SDK にメトリック・ログを記録する API があります。

```python
# ローカル実行の場合
from azureml.core import Workspace, Experiment

ws = Workspace.from_config()
exp = Experiment(workspace=ws, name="python-sdk-metrics-demo")
notebook_run = exp.start_logging()
s
notebook_run.log("accuracy", 0.95) #Scalar
notebook_run.log_list("accuracies", [0.6, 0.7, 0.87]) #List
notebook_run.log_row("Y over X", x=1, y=0.4) #Row
notebook_run.log_table("Y over X", {"x":[1, 2, 3], "y":[0.6, 0.7, 0.89]}) #Table

notebook_run.tag('DeploymentCandidate') #Tag
notebook_run.tag('type of model', 'classical ml') #Tag

notebook_run.complete()
```



### MLflow を利用する場合

Azure Machine Learning には MLflow Tracking (追跡 URI & ログ API) が内蔵されており、MLflow の API を用いたメトリック・ログの記録も可能です。

```python
# ローカル実行の場合
from azureml.core import Workspace
import mlflow
from mlflow.tracking import MlflowClient

ws = Workspace.from_config()
mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())

mlflow.create_experiment("mlflow-metrics-demo")
mlflow.set_experiment("mlflow-metrics-demo")
mlflow_run = mlflow.start_run()

mlflow.log_param(key="message", value="Hello from run!") #Parameter
mlflow.log_metric(key="accuracy", value=0.9) #Metric

mlflow.set_tag("DeploymentCandidate", "") #Tag
mlflow.set_tag("type of model", "classical ml") #Tag

mlflow.end_run()
```

また PyTorch, LightGBM などの主要なライブラリであれば自動でメトリック・ログを記録する機能 [Automatic Logging](https://www.mlflow.org/docs/latest/tracking.html#automatic-logging) も利用できます。

その他にも MLflow Project でのモデル学習 (Preview) や MLflow Model のデプロイ機能などの機能があります。詳細は [MLflow と Azure Machine LEarning](https://docs.microsoft.com/ja-jp/azure/machine-learning/concept-mlflow) を参照ください。




### 参考情報
- [Azure ML Python SDK - Run Class](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run.run?view=azure-ml-py#azureml-core-run-run-log)
- [メトリックおよびログ ファイルの記録および表示](https://docs.microsoft.com/ja-JP/azure/machine-learning/how-to-log-view-metrics)
- [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html)