import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node customers_curated
customers_curated_node1690251327791 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_curated",
    transformation_ctx="customers_curated_node1690251327791",
)

# Script generated for node step_trainer_landing
step_trainer_landing_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stediproject-sichengshen/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="step_trainer_landing_node1",
)

# Script generated for node Join
Join_node1690251349178 = Join.apply(
    frame1=step_trainer_landing_node1,
    frame2=customers_curated_node1690251327791,
    keys1=["serialNumber"],
    keys2=["serialnumber"],
    transformation_ctx="Join_node1690251349178",
)

# Script generated for node Drop Fields
DropFields_node1690251367538 = DropFields.apply(
    frame=Join_node1690251349178,
    paths=[
        "customername",
        "email",
        "phone",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
        "sharewithresearchasofdate",
        "sharewithpublicasofdate",
        "sharewithfriendsasofdate",
    ],
    transformation_ctx="DropFields_node1690251367538",
)

# Script generated for node Accelerometer Trusted
StepTrainerTrusted_node1690274010832 = glueContext.getSink(path="s3://stediproject-sichengshen/step_trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="StepTrainerTrusted_node1690274010832")
StepTrainerTrusted_node1690274010832.setCatalogInfo(catalogDatabase="stedi",catalogTableName="step_trainer_trusted")
StepTrainerTrusted_node1690274010832.setFormat("json")
StepTrainerTrusted_node1690274010832.writeFrame(DropFields_node1690251367538)

job.commit()
