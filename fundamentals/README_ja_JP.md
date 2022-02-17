# Azure Machine Learning 基礎編 Live event

本ライブセッションでは、[Azure Machine Learning (AzureML)](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning) のコンポーネントの全体像や、[AzureML studio](https://docs.microsoft.com/azure/machine-learning/overview-what-is-machine-learning-studio) の Web ポータル機能を使ってクラウド上での AI を加速させる方法が理解をします。

コンテンツは [github repository](https://aka.ms/ftalive/azureml/fundamentals) で公開されています。


## アジェンダ
|     | トピック  | 機能 | 概要  
| :-- | :----- | :-----  | :-----
| 00. | イントロダクション  |     | プレゼンターやセッションの概要についてのイントロダクション
| 01. | [Azure portal](http://portal.azure.com/) 内部のリソース | | AzureML に含まれる各リソースの説明する
| 02. | [AzureML studio](https://ml.azure.com/) | 概要 | studio のインタフェースをガイドする
| 03. |  | コンピューティング (Compute) | 様々なコンピューティングについて言及する
| 04. |  | データストア (Datastores) | [サポートされているデータソース](https://docs.microsoft.com/azure/machine-learning/how-to-access-data#supported-data-storage-service-types) を探索し登録する
| 05. |  | データセット (Datasets) | データストアに格納されているデータをデータセットとして登録し、データから洞察を得る
| 06. | 自動機械学習 (AutoML) | ウィザード | 登録したデータセットを利用して自動機械学習を実行する
| 07. |  | 実行 (Run) | 自動機械学習の内部プロセスを確認する
| 08. |  | モデル (Models) | 学習済みのモデルの一覧を確認する
| 09. |  | モデルの理解| 学習済みモデルの精度や解釈性を確認する
| 10. | デプロイメント (Deployment) | ACI へのデプロイ | Azure Container Instance を用いたリアルタイム推論用エンドポイントをデプロイする
| 11. | | モデル登録| 格納されているアーティファクトを確認する
| 12. | | リアルタイム推論 | swagger.json を確認し、ACI のエンドポイントをテストする
| 13. | ノートブック (Notebooks) | フォルダ構造 | コードやノートブックが格納される場所を確認する
| 14. |  | ターミナル (Terminal) | ターミナルや git を操作する
| 15. |  | サンプル (Sample)| サンプルのノートブックを使い始めます
| 16. |  | インテリセンス (IntelliSense)| ノートブックでのコーディングの効率性を高める方法を示す
| 17. | AzureML SDK |  | Python を利用して AzureML Workspace を利用する
| 18. |  | メトリックのロギング | Azure ML SDK や MLflow を利用する
| 19. |  | スクリプトの実行 | リモートのクラスター環境でコードを実行する
| 20. |  | 環境 (Environments) | ソフトウェアの依存環境を定義する
| 21. |  | パイプライン (Pipeline) の作成 | パイプラインの中で複数のステップをオーケストレーションする
| 22. |  | パイプラインのエンドポイント (Endpoint) の利用 | パブリッシュされたエンドポイントを確認し REST API 経由で実行する
| 23. |  | 並列バッチ処理 (Parallel batch processing) | バッチ推論のパイプラインを作成し利用する

## サンプル

Azure ML のサンプルコード・ノートブックの一覧 : 

- [Fun with AzureML repo](https://github.com/rndazurescript/FunWithAzureML)
- [Many models solution accelerator](https://github.com/microsoft/solution-accelerator-many-models)
- [Official AzureML notebook samples](https://github.com/Azure/MachineLearningNotebooks/)
- [Community Driven AzureML notebook samples](https://github.com/Azure/azureml-examples)
- [MLOps starter](https://aka.ms/mlops)
