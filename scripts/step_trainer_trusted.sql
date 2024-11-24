CREATE EXTERNAL TABLE `step_trainer_trusted`(
  `serialnumber` string COMMENT 'from deserializer',
  `sensorreadingtime` bigint COMMENT 'from deserializer',
  `distancefromobject` int COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stediproject-sichengshen/step_trainer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='Step-Trainer Landing to Trusted',
  'CreatedByJobRun'='jr_df3cb18b9a2a264d90b95a018d5aa2be88f65d93b6e2af37da558dc221515382',
  'classification'='json')
