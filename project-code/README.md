# Leveraging REST for cloud portability
  
## Pre-requisits

* You should have an account with AWS, Azure and Google cloud
* Modify credentials.yml file under the etc directory to include configuration information
* Replace TBD information in the file with appropriate credential information
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

    
## Instructions for Ubuntu without docker

* you should be running this program in Python 2 environment.

* you should have default-jre installed.

* git clone the project.

* change directory to the project-code folder

* create the swagger server with the following command
  
  * ```make service```

* run swagger server with the following command
  
  * ```make start```

* test program using the following command
  
  * ```make testaws```
  * ```make testazure```
  * ```make testgoogle```

* stop service using the following command
  
  * ```make stop```

* clean server and client codes using the following command
  
  * ```make clean```
