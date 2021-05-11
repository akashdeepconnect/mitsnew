import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


class DeployConfig:
    __vars = {
        "lambdaRoleName": "test-lambda-role",
        "accountID": "123456789012",
        "pipelineRoleName": "test-codepipeline-role",
        "pipelineId": "my-test-pipeline-dev",
        "pipelineName": "my-test-pipeline",
        "s3_bucket": "my-test-bucket",
        "environment": "L2",
        "custom_tags": {
            "app_owner": "test-owner",
            "app_veersion": "2.4.1"
        }
    }

    @staticmethod
    def init():
        LOGGER.info("Configuring app settings")

    @staticmethod
    def resource_tags():
        return DeployConfig.__vars['custom_tags']

    @staticmethod
    def s3_bucket() -> str:
        return DeployConfig.__vars['s3_bucket']

    @staticmethod
    def environment() -> str:
        return DeployConfig.__vars['environment']

    @staticmethod
    def lambda_role_name() -> str:
        return DeployConfig.__vars['lambdaRoleName']

    @staticmethod
    def role_name() -> str:
        return DeployConfig.__vars['pipelineRoleName']

    @staticmethod
    def pipeline_id() -> str:
        return DeployConfig.__vars['pipelineId']

    @staticmethod
    def pipeline_name() -> str:
        return DeployConfig.__vars['pipelineName']

    @staticmethod
    def account_id() -> str:
        return DeployConfig.__vars['accountID']    
