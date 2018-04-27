# Leveraging REST for cloud portability
  
## Pre-requisits

* You should have account with AWS, Azure and Google cloud
* Modify credentials.yml file under etc directory to include configuration information
* Replace TBD information in the file with appropriate credentail information
* Copy key file required by Google cloud under etc directory

## Instructions for docker installation

* Create and Start docker container using make command.
  
  * ```make docker-start```

* Test the service using following curl commands
  
  * ```make testaws```
  * ```make testazure```
  * ```make testgoogle```
  
* Stop the service using following commands
  
  * ```make docker-stop```

	
## Instructions for ubuntu without docker

* you should be running this program in python 2 environment.

* you should have default-jre installed.

* git clone the project.

* change the directory to project-code folder

* create the swagger server with following command
  
  * ```make service```

* run the swagger server with following command
  
  * ```make start```

* test the program using following command
  
  * ```make testaws```
  * ```make testazure```
  * ```make testgoogle```

* stop the service using following command
  
  * ```make stop```

* clean the server and client codes using following command
  
  * ```make clean```
