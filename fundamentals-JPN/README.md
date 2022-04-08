# Azure Machine Learning 基礎編 Live event

本ライブセッションでは、[Azure Machine Learning (AzureML)](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning) の概要を説明し、[AzureML Studio](https://docs.microsoft.com/azure/machine-learning/overview-what-is-machine-learning-studio) の Web ポータル機能や [Azure ML Python SDK](https://docs.microsoft.com/ja-JP/python/api/overview/azure/ml/?view=azure-ml-py) を使って機械学習のプロセスを実行する様子をデモンストレーションを通じて解説します。

コンテンツは [github repository](https://aka.ms/ftalive/azureml/fundamentals) で公開されています。


## アジェンダ
|     | トピック  | 機能 | 概要  
| :-- | :----- | :-----  | :-----
| 00. | Introduction  |     | プレゼンターやセッションの概要について説明します。
| 01. | Azure ML 概要  |     | Azure Machine Learning のコンポーネントや特徴を説明します。
| 02. | Demo : Azure Machine Learning サービス作成 |[Azure Portal](http://portal.azure.com/) | AzureML に含まれる各リソースの説明する。
| 03. | Demo : Azure Machine Learning studio | [AzureML Studio](https://ml.azure.com/) | Studio のインタフェースをガイドする。<br/> - 手順 : [azureml_studio_walk_through.md](demonstration/azureml_studio_walk_through.md)
| 04. | Demo : Azure Machine Learning Python SDK | [AzureML Python SDK](https://docs.microsoft.com/ja-JP/python/api/overview/azure/ml/?view=azure-ml-py) | Python SDK を使った E2E の機械学習プロセスの実行方法をガイドする。<br/> - モデル学習 : [train-notebook.ipynb](src/notebooks/train-notebook.ipynb) <br/> - デプロイ: [deploy-notebook.ipynb](src/notebooks/deploy-notebook.ipynb)


## サンプル

Azure ML のサンプルコード・ノートブックの一覧 : 

- [Official AzureML notebook samples](https://github.com/Azure/MachineLearningNotebooks/)
- [Community Driven AzureML notebook samples](https://github.com/Azure/azureml-examples)
- [MLOps starter](https://aka.ms/mlops)