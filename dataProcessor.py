from __future__ import print_function

import sys

from pyspark.sql import SQLContext 
from pyspark import SparkConf
from pyspark import SparkContext
from datetime import datetime
import uuid
import random
from pyspark.sql.types import * 
from pyspark_cassandra import CassandraSparkContext

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: station.py <file>", file=sys.stderr)
        exit(-1)

    conf = SparkConf().setAppName("Twitter Sentiment")
    sc = CassandraSparkContext(conf=conf) 
    sqlContext = SQLContext(sc)
    
    for i in xrange(1,len(sys.argv)):

       tweets = sqlContext.read.json(sys.argv[i])
       print('Filename = %s' % sys.argv[i],file=sys.stderr)
       tweets.printSchema()
       tweets.registerTempTable('tweets')

       temp = tweets.map(lambda row: {    'text': row.text,
                                          'name':row.name,
                                          'recordid': str(uuid.uuid1()),
                                          'longitude': str(row.location[0][0][1]) if row.location is not None else 0.00,
                                          'lattitude': str(row.location[0][0][0]) if row.location is not None else 0.00,
                                          'emotion': 'negative' if random.randrange(0,2) == 0 else 'positive' }).collect()
                                        #'state': row.STATE}).collect() 
                                        #'lat': row.LAT,
                                        #'lon': row.LON,
                                        #'elev': row.ELEV}).collect() 

       sc.parallelize(temp).saveToCassandra(keyspace='project', table='tweets')