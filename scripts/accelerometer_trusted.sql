CREATE EXTERNAL TABLE `accelerometer_trusted`(
  `user` string COMMENT 'from deserializer',
  `timestamp` bigint COMMENT 'from deserializer',
  `x` double COMMENT 'from deserializer',
  `y` double COMMENT 'from deserializer',
  `z` double COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stediproject-sichengshen/accelerometer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='Accelerometer Landing to Trusted',
  'CreatedByJobRun'='jr_ffd231c849691dd7ac3af7ccf6ad5207a8fd2ee6249ad026ec2346d23279f853',
  'classification'='json')
