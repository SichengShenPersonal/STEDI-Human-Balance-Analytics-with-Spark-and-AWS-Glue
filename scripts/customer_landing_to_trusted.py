import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Row Data
RowData_node1732121956151 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://stediproject-sichengshen/customer/landing/"], "recurse": True}, transformation_ctx="RowData_node1732121956151")

# Script generated for node Privacy Filter
PrivacyFilter_node1732123164098 = Filter.apply(frame=RowData_node1732121956151, f=lambda row: (not(row["shareWithResearchAsOfDate"] == 0)), transformation_ctx="PrivacyFilter_node1732123164098")

# Script generated for node Amazon S3
AmazonS3_node1732147505068 = glueContext.getSink(path="s3://stediproject-sichengshen/customer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1732147505068")
AmazonS3_node1732147505068.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_trusted")
AmazonS3_node1732147505068.setFormat("json")
AmazonS3_node1732147505068.writeFrame(PrivacyFilter_node1732123164098)
job.commit()
