# Presenter's notes for AzureML fundamentals

## Demo environment setup

- Deploy workspace using the instructions in [the src folder](./src/README.md)
- Create Win10 VM and connect to portal/AzureML
- 
- Navigate to **Author** | **Notebooks**. Run all notebooks located in the **fta-live** | **fundamentals** | **src** | **notebooks** folder in the **Files** tree.
- Configure and run a regression autoML experiment on top of the **diabetes-tabular** that got registered. You can create a new experiment named **diabetes-automl-experiment**. Target column is **target** and you can use the **cpu-cluster** cluster that is available. In the **View additional configuration settings** specify 0.5 in the **Exit criterion** | **Training job time (hours)**.
- Navigate to the AutoML run and name it **30minute_automl_run**.
- Select a trained model from the AutoML run (not the best one) and select the **Explain model** option to perform a model explanation.
- Deploy the selected model as an Azure Container Instance named **deploy-to-aci**.
- Navigate to **Assets** | **Datasets** | **pending-diabetes** and complete the **Generate profile** wizard.

## Before the live event

- Start your compute instance and execute the [before_event.py](./src/before_event.py) script in a terminal to scale up the **cpu-cluster**.
- Open following pages:
    - https://fasttrack.azure.com/live/category/Data
    - https://github.com/Azure/fta-azure-machine-learning/tree/main/enterprise-ml
    - https://docs.microsoft.com/en-us/azure/machine-learning/concept-azure-machine-learning-architecture
    - https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-resource-organization
    - https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace
    - 
- Open an Azure portal, navigate to the resource group and filter out the **container instances** to be able to show only the 5 AzureML deployed resources.
- Navigate to the **deploy-to-aci** endpoint:
  - Open the **Swagger URI**. Copy paste it in a [json formatter](https://www.jsonformatter.io/)
  - Copy the **REST endpoint** and paste it in the [reqbin sample](https://reqbin.com/etrbvco6). Select the **Content (27)** tab to have the sample request ready to send. If you want to try it, you can then remove one of the two records during the live event.
- Dismiss all notifications in the AzureML studio.

## During the live event

- From local pc - open Azure ML workspace to demonstrate how secure connectivity restricts access



## After the live event

- Execute the [after_event.py](./src/after_event.py) script in a terminal to delete deployed web services, scale down clusters and shut down you compute instance.
