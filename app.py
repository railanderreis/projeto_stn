from athena.stack import AthenaStack
from aws_cdk import core

from bootcamp_data_platform_turma_3.data_lake.stack import DataLakeStack
from dms.stack import DmsStack
from glue_catalog.stack import GlueCatalogStack


from common_stack import CommonStack

app = core.App()

data_lake = DataLakeStack(app)
glue_catalog = GlueCatalogStack(app, data_lake_bucket=data_lake.data_lake_raw_bucket)
athena_stack = AthenaStack(app)
common_stack = CommonStack(app)


app.synth()