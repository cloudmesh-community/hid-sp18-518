#swagger code gen path
SWAGGER_CODEGEN=java -jar swagger-codegen-cli.jar
SPEC_FILE=compute-storage.yml
DESTDIR=cloudmesh
CONFIG=$(DESTDIR)/config
DOWNLOADS = $(DESTDIR)/downloads

help: ## show this help
	@echo 'usage: make [target] ...'
	@echo 'Make file sequence - startdb, service, test, stop'
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY : init clean

init:
	mkdir $(DESTDIR)

service: clean init ## generate service and start the swagger server
	echo "Downloading Swagger Codegen"
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar 
	echo "Generating swagger code"
	$(SWAGGER_CODEGEN) generate \
		-i $(SPEC_FILE) \
		-l python-flask \
		-o $(DESTDIR) \
		-D supportPython2=true
	cp -r aws/*.* $(DESTDIR)/swagger_server/controllers/
	cp -r azure/*.* $(DESTDIR)/swagger_server/controllers/
	cp -r google/*.* $(DESTDIR)/swagger_server/controllers/
	if ! [ -d $(CONFIG) ]; then mkdir $(CONFIG); fi
	if ! [ -d $(DOWNLOADS) ]; then mkdir $(DOWNLOADS); fi
	cp etc/* $(CONFIG)
	pip install boto3
	pip install apache-libcloud
	pip install pycrypto
	echo "Installing Swagger server"
	cd $(DESTDIR) && pip install -r requirements.txt && python setup.py install 

start:
	echo "Starting Swagger Server"
	cd $(DESTDIR) && python -m swagger_server


testaws: ## Test AWS service
	echo "Create AWS EC2 VM -->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"vmId\": \"NA\",  \"name\": \"myVM\",  \"image\": \"ami-25615740\",  \"region\": \"us-east-2\",  \"size\": \"t2.micro\",  \"status\": \"NA\"}"
	echo "Get AWS VM List by region-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2
	echo "Get AWS VM by Name-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2
	echo "Start AWS EC2 VM-->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/start" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"	
	echo "Stop AWS EC2 VM-->"	
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/stop" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	echo "Terminate AWS EC2 VM-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/terminate" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	echo "Get AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/storage/aws/s3/bucket
	echo "Create AWS S3 Buckets-->"	
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"
	echo "Upload file to AWS S3 bucket"
	touch samplefile.txt
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/uploadFile" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "fileName=@samplefile.txt;type=text/markdown"
	echo "List files from AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt
	echo "Download file from AWS S3 bucket"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/downloadFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	echo "Delete file from AWS S3 Buckets-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/deleteFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	echo "Delete AWS S3 Buckets-->"		
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"

testazure: ## Test AZURE service
	#Azure compute
	echo "Create Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/createvm?name=AZ1&size=Standard_B1s&image_name=UbuntuServer&resource_group=libcloud&storage_account=libclouddiag209&network_intf=libcloud-vnet&blob_container=test123" -H  "accept: application/json"
	echo "List Azure VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/listvm" -H "accept: application/json"
	echo "Stop Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/stopvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	echo "Start Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/startvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	echo "Delete Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/deletevm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	#Azure storage
	echo "Create Azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVol?volname=newvol1&volsize=1&location=eastus&resource_group=libcloud&ex_account_type=Standard_LRS" -H  "accept: application/json"
	echo "create azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVolSnap?volname=newvol&snapname=newsnap&resource_group=libcloud&location=eastus" -H  "accept: application/json"
	echo "delete azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVolSnap?snapname=newsnap&resource_group=libcloud" -H  "accept: application/json"
	echo "delete azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVol?volname=newvol&resource_group=libcloud" -H  "accept: application/json"

testgoogle: ## Test Google service
	#Google Compute
	echo "Create Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/createvm?name=test123&size=g1-small&image_name=debian-8&location=us-east1-b" -H  "accept: application/json"
	echo "List Google VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/listvm" -H  "accept: application/json"
	echo "Stop Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/stopvm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	echo "Start Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/startvm?vmname=test123" -H  "accept: application/json"
	echo "Delete Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/deletevm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	#Google storage
	echo "Create Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVol?volname=newvol1&volsize=1&location=us-east1-b" -H  "accept: application/json"
	echo "create Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVolSnap?volname=newvol1&snapname=newvol1snap" -H  "accept: application/json"
	echo "delete Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVol?volname=newvol1" -H  "accept: application/json"
	echo "delete Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVolSnap?snapname=newvol1snap" -H  "accept: application/json"

stop: ## Stop swagger server
	echo "Stopping swagger serevr"
	ps -ef | grep 'swagger_server' | grep -v grep | awk '{print $$2}' | xargs kill

clean: ## Clean generated directories
	echo "Removing directories"
	rm -rf $(DESTDIR)
	
docker-start:
	# Add docker commands
	docker build -t cloudautomation .
	docker run -p 8080:8080 cloudautomation 


docker-stop:
	docker stop $$(docker ps -aq -f status=running)
	



