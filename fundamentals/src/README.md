# Demo setup for the AzureML fundamentals Live event

## Resources deployment

Use the following links to deploy the required resources in your Azure subscription.

[![Deploy To Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.svg?sanitize=true)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Ffta-azure-machine-learning%2Fmain%2Ffundamentals%2Fsrc%2Fdeployment%2Fdemo-deploy.json)
[![Visualize](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/visualizebutton.svg?sanitize=true)](http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Ffta-azure-machine-learning%2Fmain%2Ffundamentals%2Fsrc%2Fdeployment%2Fdemo-deploy.json)

> **Note**: If you have deleted a KeyVault with the same name recently, you will need to use `recover` create mode. See here how [purge protection](https://docs.microsoft.com/azure/key-vault/general/soft-delete-overview#purge-protection) works.

> **Note**: If you see an error regarding the shutdown schedule of the compute instance, you will need to delete the existing compute instance to re-deploy the template.

## References

Various resources used while curating the demos:

- [Advanced ARM template for Compute Instance](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-computeinstance)
- [Setup scripts for Compute Instance](https://github.com/Azure/azureml-examples/tree/main/setup-ci)
