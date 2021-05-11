from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    aws_codebuild as codebuild,
    aws_secretsmanager as secretsmanager,
    core
)

class CodeBuildService:

    def create_project(self, build_id, artifacts):
       
        project = codebuild.PipelineProject(
            self,
            id=build_id,            
        )

        return project