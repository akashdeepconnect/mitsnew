from aws_cdk import core

from BuildServices.codepipelineService import CodePipelineService
from BuildServices.codebuildService import CodeBuildService

from Config.deployConfig import DeployConfig

class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        role_arn="arn:aws:iam::"+DeployConfig.account_id()+":role/"+DeployConfig.role_name()
        
        pipeline_role=CodePipelineService.get_role_from_arn(self, role_arn=role_arn)

        s3_bucket = CodePipelineService.create_s3_bucket_object(self, bucket_name=DeployConfig.s3_bucket())

        test_pipeline=CodePipelineService.create_pipeline(self, pipeline_id=DeployConfig.pipeline_id(), 
                                                            pipeline_name=DeployConfig.pipeline_name(), pipeline_role=pipeline_role, 
                                                            artifact_bucket=s3_bucket)
        
        github_source, artifact=CodePipelineService.create_source_stage(self, token="my-test-token", source_repo="cdk_codepipeline", 
                                                                branch="main", action_name="GitHub_Source", code_owner="VartikaMalik")

        codebuild_project = CodeBuildService.create_project(self, build_id="test-project", artifacts=artifact)
        
        github_action, output_artifacts= CodePipelineService.create_action_stage(self, artifact=artifact, project=codebuild_project, action_name="CodeBuild")
        
        test_pipeline.add_stage(
            stage_name="Source",
            actions=[github_source]
        )
        test_pipeline.add_stage(
            stage_name="Build",
            actions=[github_action]
        )