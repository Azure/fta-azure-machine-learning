# FastTrack for Azure - Azure Machine Learning (AzureML) Live events

This repo contains the material used for the [FTA AzureML Live](https://aka.ms/ftaLive) events.

## Session QnA

We will start 1-2 minutes after the scheduled time to accommodate those still connecting.

The calls will not be recorded due to the wide audience and to encourage questions.

**Questions during the call?**: Feel free to type them in the chat window at any time. Note that questions you post will be public.

**Slideless session**: No PowerPoint, we promise! As we update [this repository](https://aka.ms/ftaLive/azureML) you will get the changes straight away.

Please give us your feedback through the [feedback form](https://aka.ms/ftaLive-feedback).

## Available sessions

- [AzureML fundamentals](./fundamentals/): In this session you will get an understanding of the overall [Azure Machine Learning (AzureML)](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning) components and how you can start using the [AzureML studio](https://docs.microsoft.com/azure/machine-learning/overview-what-is-machine-learning-studio) web portal to accelerate you AI journey in the cloud.

- [AzureML Enterprise Deployment](./enterprise-ml/): In this session you will learn how to design and implement [Azure Machine Learning (AzureML)](https://docs.microsoft.com/azure/machine-learning/overview-what-is-azure-machine-learning) using enterprise deployment features, so you can create a secure configuration that is compliant with your companies policies [Enterprise security and governance for AzureML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-enterprise-security).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
[Contributor License Agreement (CLA)](https://cla.opensource.microsoft.com) declaring that you have the right to, and actually do, grant us the rights to use your contribution.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### Linting you code contributions

Please make sure that your code and notebooks comply with flake8 and that the code blocks are formatted with [black](https://github.com/psf/black).

In your terminal install the prerequisites:

``` bash
pip install black[jupyter] flake8 flake8_nb
```

To format and verify your code:

``` bash
black .
flake8 .
flake8_nb .
```

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
