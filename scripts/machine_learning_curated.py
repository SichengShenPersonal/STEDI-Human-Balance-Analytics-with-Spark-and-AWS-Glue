import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Acc Trusted
AccTrusted_node1732466575639 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_trusted", transformation_ctx="AccTrusted_node1732466575639")

# Script generated for node Trainer Trusted
TrainerTrusted_node1732466542727 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_trusted", transformation_ctx="TrainerTrusted_node1732466542727")

# Script generated for node Join
TrainerTrusted_node1732466542727DF = TrainerTrusted_node1732466542727.toDF()
AccTrusted_node1732466575639DF = AccTrusted_node1732466575639.toDF()
Join_node1732466617470 = DynamicFrame.fromDF(TrainerTrusted_node1732466542727DF.join(AccTrusted_node1732466575639DF, (TrainerTrusted_node1732466542727DF['sensorreadingtime'] == AccTrusted_node1732466575639DF['timestamp']), "left"), glueContext, "Join_node1732466617470")

# Script generated for node Drop Fields
DropFields_node1732466868548 = DropFields.apply(frame=Join_node1732466617470, paths=["user"], transformation_ctx="DropFields_node1732466868548")

# Script generated for node ML Curated
MLCurated_node1732466881723 = glueContext.getSink(path="s3://stediproject-sichengshen/step_trainer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="MLCurated_node1732466881723")
MLCurated_node1732466881723.setCatalogInfo(catalogDatabase="stedi",catalogTableName="machine_learning_curated")
MLCurated_node1732466881723.setFormat("json")
MLCurated_node1732466881723.writeFrame(DropFields_node1732466868548)
job.commit()