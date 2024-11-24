CREATE EXTERNAL TABLE `machine_learning_curated`(
  `serialnumber` string COMMENT 'from deserializer',
  `sensorreadingtime` bigint COMMENT 'from deserializer',
  `distancefromobject` int COMMENT 'from deserializer',
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
  's3://stediproject-sichengshen/step_trainer/curated/'
TBLPROPERTIES (
  'CreatedByJob'='Machine Learning Curated',
  'CreatedByJobRun'='jr_b1e5e5b33b221f41a45db313e1c39821e8e4f19b25031a89945ebfeeaf5a5101',
  'classification'='json')
