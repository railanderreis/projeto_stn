from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3,
)

from data_platform import active_environment
from data_platform.data_lake.base import (
    BaseDataLakeBucket,
    DataLakeLayer
)


class DataLakeStack(core.Stack):
    def __init__(self, scope: core.Construct, **kwargs) -> None:
        self.deploy_env = active_environment
        super().__init__(scope, id=f'{self.deploy_env.value}-data-lake-stack', **kwargs)

        self.data_lake_raw_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.RAW
        )

        # Data Lake Processed
        self.data_lake_processed_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.PROCESSED
        )

        # Data Lake Curated
        self.data_lake_curated_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.CURATED
        )