# iu_data_eng_batch
University project 

Clone the repository with :
git clone https://github.com/av-ll/iu_data_eng_batch/

change directory to the cloned repository :
cd iu_data_eng_batch

build the image:
docker build -t iu-data-eng docker

The image will start building

check if the image was built with :
docker images

You should see the image iu-data-eng there

Run the image as a container : 

docker run -p 27017:27017 --name iu-data-eng iu-data-eng

This might take a while as the 500000 records start getting loaded
into the database

Now the mongo database container is set up and you can start using it either 
through mongoshell (mongosh) or through a programming language locally (localhost).

