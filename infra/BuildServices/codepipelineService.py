from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    aws_codepipeline_actions as pipelineActions,
    aws_codepipeline as pipeline,
    aws_secretsmanager as secretsmanager,
    core
)

class CodePipelineService:

    def get_role_from_arn(self, role_arn):
        
        role=iam.Role.from_role_arn(self, id='role_id', role_arn=role_arn)
        return role
    
    def create_s3_bucket_object(self, bucket_name):

        s3_bucket=s3.Bucket.from_bucket_name(self, id='bucket_id', bucket_name=bucket_name)
        return s3_bucket

    def create_pipeline(self, pipeline_id, pipeline_name, artifact_bucket, pipeline_role):

        test_pipeline = pipeline.Pipeline(
            self,
            id=pipeline_id,
            pipeline_name=pipeline_name,
            artifact_bucket=artifact_bucket,
            role=pipeline_role
        )
        return test_pipeline

    def create_source_stage(self, token, code_owner, source_repo, branch, action_name):
        
        artifact= pipeline.Artifact()
        
        git_source = pipelineActions.GitHubSourceAction(
            oauth_token=core.SecretValue.secrets_manager(token),
            output=artifact,
            owner=code_owner,
            repo= source_repo,
            branch=branch,
            action_name=action_name
        )

        return git_source, artifact

    def create_action_stage(self, artifact, project, action_name):

        output_artifact=pipeline.Artifact()
        
        git_action= pipelineActions.CodeBuildAction(
            input=artifact,
            project=project,
            outputs=[output_artifact],
            action_name=action_name
        )

        return git_action, output_artifact

    