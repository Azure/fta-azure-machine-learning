# 実験にデータを持ち込む方法



## コンピューティングインスタンス (Compute Instance) にファイル形式のデータセット (File Dataset) をマウントする

> :warning: 読み込み専用です。書き込みはできません。

<br/>

登録済みのデータストア (Datastore) `workspaceblobstore` にある jpg の画像をファイル形式のデータセット (Dataset) として定義し、マウントします。

```python
datastore = Datastore.get(workspace, 'workspaceblobstore')
dataset = Dataset.File.from_files((datastore, 'animals/dog/year-*/*.jpg'))

with dataset.mount() as mount_context:
    # list top level mounted files and folders in the dataset
    os.listdir(mount_context.mount_point)

# You can also use the start and stop methods
mount_context = dataset.mount()
mount_context.start()  # this will mount the file streams
mount_context.stop()  # this will unmount the file streams
```


## 参考情報
- [FileDataset クラス](https://docs.microsoft.com/ja-jp/python/api/azureml-core/azureml.data.file_dataset.filedataset?view=azure-ml-py)