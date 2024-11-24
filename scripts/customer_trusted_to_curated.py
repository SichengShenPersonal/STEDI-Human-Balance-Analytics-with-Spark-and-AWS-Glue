import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Acc Landing
AccLanding_node1732143839721 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="AccLanding_node1732143839721")

# Script generated for node Customer Trusted
CustomerTrusted_node1732143795766 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_trusted", transformation_ctx="CustomerTrusted_node1732143795766")

# Script generated for node Join
Join_node1732143908905 = Join.apply(frame1=CustomerTrusted_node1732143795766, frame2=AccLanding_node1732143839721, keys1=["email"], keys2=["user"], transformation_ctx="Join_node1732143908905")

# Script generated for node SQL Query
SqlQuery216 = '''
select distinct customername, email, phone, birthday, 
serialnumber, registrationdate, lastupdatedate, 
sharewithresearchasofdate, sharewithpublicasofdate,
sharewithfriendsasofdate from J
'''
SQLQuery_node1732150041033 = sparkSqlQuery(glueContext, query = SqlQuery216, mapping = {"J":Join_node1732143908905}, transformation_ctx = "SQLQuery_node1732150041033")

# Script generated for node Customer Curated
CustomerCurated_node1732144015659 = glueContext.getSink(path="s3://stediproject-sichengshen/customer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="CustomerCurated_node1732144015659")
CustomerCurated_node1732144015659.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_curated")
CustomerCurated_node1732144015659.setFormat("json")
CustomerCurated_node1732144015659.writeFrame(SQLQuery_node1732150041033)
job.commit()