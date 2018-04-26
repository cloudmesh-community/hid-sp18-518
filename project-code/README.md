Instructions for docker installation

Create and Start docker container using make command. 

        make docker-start

    Test the service using following curl commands
        make test

    Stop the service using following commands
        make docker-stop

Instructions for ubuntu without docker

    you should be running this program in python 2 environment.

    you should have default-jre installed.

    you should have mongoDB installed.

    git clone the project.

    change the directory to swagger folder

    create the swagger server with following command
        make service

    run the swagger server with following command
        make start

    start mongodb with following command
        make startdb

    test the program using following command
        make test

    stop the service using following command
        make stop

    clean the server and client codes using following command
        make clean
