# model_deployment_demonstration

This repository was created for the second part of the assignment.

The steps that created the container including the nginx are described as follow:

1- Create a new file named 'Dockerfile'.
2- Create a new file named 'requirements.txt'.
3- Create a new directory named app, and create main.py.
4- Create a new file named 'nginx.conf'
5- Create a new Jupyter notebook, to POST request to the container endpoint and print out the response. 


To build the docker image, run the following command:

docker build -t model_deployment_demonstration .


The reason that I have chosen imdb model:

My main challenge was limitted space on my laptop that forced me to find a compact model that could be downloaded and containerized without requiring a significant amount of space.

In addition, the model can be considered as an useful example for further development in different applications.  

