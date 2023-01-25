#! /bin/sh

# create time-series collection
mongosh <<EOF

use sensordb

db.createCollection( "sensors",{ timeseries:{timeField:"timestamp",metaField:"metadata",granularity:"hours"}})

EOF

#loads the data into the database

echo 'Loading data into database, please wait, it might take a while as there are more than 500k data records.'

python3 jsondata/mongo.py

# removes any unnecessary data components or dependencies

rm -rf jsondata

pip3 uninstall pymongo python-dateutil tqdm

apt-get remove -y python3 unzip python3-pip 

apt-get autoremove

echo "Script execution complete"
