#!/usr/bin/env python3

from aws_cdk import core

from Stacks.application_stack import ApplicationStack
from Stacks.pipeline_stack import PipelineStack


app = core.App()
PipelineStack(app, "pipelineDeployment", env={'region': 'us-east-1'})
#ApplicationStack(app, "infra", env={'region': 'us-west-2'})

app.synth()
