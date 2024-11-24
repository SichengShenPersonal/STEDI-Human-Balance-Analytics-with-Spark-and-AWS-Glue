CREATE EXTERNAL TABLE `customer_trusted`(
  `serialnumber` string COMMENT 'from deserializer',
  `sharewithpublicasofdate` bigint COMMENT 'from deserializer',
  `birthday` string COMMENT 'from deserializer',
  `registrationdate` bigint COMMENT 'from deserializer',
  `sharewithresearchasofdate` bigint COMMENT 'from deserializer',
  `customername` string COMMENT 'from deserializer',
  `sharewithfriendsasofdate` bigint COMMENT 'from deserializer',
  `email` string COMMENT 'from deserializer',
  `lastupdatedate` bigint COMMENT 'from deserializer',
  `phone` string COMMENT 'from deserializer')
ROW FORMAT SERDE
  'org.openx.data.jsonserde.JsonSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://stediproject-sichengshen/customer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='Customer Landing to Trusted',
  'CreatedByJobRun'='jr_8b2fbfc81b894e6e71ad712a98b2eb9246491c998c5bfeceda4d28b359e3c284',
  'classification'='json')
