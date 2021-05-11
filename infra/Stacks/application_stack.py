from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_assets as s3_assets,
    aws_lambda as lambdas,
    aws_appsync as appsync,
    aws_cloudwatch as cloudwatch,
    aws_dynamodb as dynamodb,
    aws_kms as kms,
    aws_secretsmanager as secretsmanager,
    core
)

class ApplicationStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

