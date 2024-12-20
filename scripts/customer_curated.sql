CREATE EXTERNAL TABLE `customer_curated`(
  `customername` string COMMENT 'from deserializer',
  `email` string COMMENT 'from deserializer',
  `phone` string COMMENT 'from deserializer',
  `birthday` string COMMENT 'from deserializer',
  `serialnumber` string COMMENT 'from deserializer',
  `registrationdate` bigint COMMENT 'from deserializer',
  `lastupdatedate` bigint COMMENT 'from deserializer',
  `sharewithresearchasofdate` bigint COMMENT 'from deserializer',
  `sharewithpublicasofdate` bigint COMMENT 'from deserializer',
  `sharewithfriendsasofdate` bigint COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stediproject-sichengshen/customer/curated/'
TBLPROPERTIES (
  'CreatedByJob'='Custom Trusted to Curated',
  'CreatedByJobRun'='jr_0aa08deb6ddaad1e289cc7835787abbe0fa7ec0cf297a601848d74649b8ee3f7',
  'classification'='json')
