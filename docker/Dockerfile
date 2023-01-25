
# Start with the official MongoDB image as the base image

FROM mongo:latest

# Copy the init.sh script into the folder that gets executed when running container

COPY init.sh /docker-entrypoint-initdb.d/

# Make the init.sh script executable

RUN chmod +x /docker-entrypoint-initdb.d/init.sh

# For persisting data

VOLUME [ "/data/db" ]

# Environmental variable to be able to be more maitainable later

ENV MONGO_PORT 27017

EXPOSE $MONGO_PORT

# Installing dependencies

RUN apt-get update && apt-get install -y python3 python3-pip unzip

# Copying host data and python script to image

COPY data.zip jsondata/

COPY mongo.py jsondata/

# Unzip data

RUN unzip jsondata/data.zip -d jsondata/

# Remove unnecessary zip file after extraction

RUN rm -rf jsondata/data.zip

# Install dependencies for mongo.py

RUN pip3 install pymongo python-dateutil tqdm

# Insert label for easier idenfication and metadata

LABEL maintainer="Joao Goncalves" \
      version="1.0" \
      description="Docker image for MongoDB that loads sensor data automatically"

