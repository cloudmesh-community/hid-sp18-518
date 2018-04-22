#/bin/sh
#Script name: benchmarking.sh
#Purpose: This script is written to run curl commands and
#collect duration results that can be used in benchmarking.
#
#Usage: benchmarking.sh <No. of iteration> <Cloud Name>
#	For ex. benchmarking.sh 5 AWS
#Reference: 
# https://stackoverflow.com/questions/8903239/


ITER=$1
CLOUD=$2


#for (i=0; i < $ITER; i++)
#for (i=0; i < 10; i++)
#do
#	echo $i 
#done

testaws(){

	echo "Create AWS EC2 VM -->"
	SECONDS=0
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"vmId\": \"NA\",  \"name\": \"myVM\",  \"image\": \"ami-25615740\",  \"region\": \"us-east-2\",  \"size\": \"t2.micro\",  \"status\": \"NA\"}"
	duration=$SECONDS
	echo "AWS,Compute,Create VM,"$duration


	SECONDS=0
	echo "Get AWS VM List by region-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2" -H  "accept: application/json"
	duration=$SECONDS
	echo "AWS,Compute,List VM,"$duration

	SECONDS=0
	echo "Get AWS VM by Name-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2" -H  "accept: application/json"
	duration=$SECONDS
	echo "AWS,Compute,Get VM Details,"$duration

	SECONDS=0
	echo "Start AWS EC2 VM-->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/start" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"	
	duration=$SECONDS
	echo "AWS,Compute,Start VM,"$duration

	SECONDS=0
	echo "Stop AWS EC2 VM-->"	
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/stop" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	duration=$SECONDS
	echo "AWS,Compute,Stop VM,"$duration

	SECONDS=0
	echo "Terminate AWS EC2 VM-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/terminate" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	duration=$SECONDS
	echo "AWS,Compute,Delete VM,"$duration

	SECONDS=0	
	echo "Get AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json"
	duration=$SECONDS
	echo "AWS,Storage,Get Vol/Bucket Details,"$duration

	SECONDS=0	
	echo "Create AWS S3 Buckets-->"	
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"
	duration=$SECONDS
	echo "AWS,Storage,Create Vol/Bucket,"$duration

	SECONDS=0
	echo "Upload file to AWS S3 bucket"
	touch samplefile.txt
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/uploadFile" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "fileName=@samplefile.txt;type=text/markdown"
	duration=$SECONDS
	echo "AWS,Storage,Upload File to S3," $duration

	SECONDS=0
	echo "List files from AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt" -H  "accept: application/json"
	duration=$SECONDS
	echo "AWS,Storage,List Vol/Bucket Details,"$duration

	SECONDS=0
	echo "Download file from AWS S3 bucket"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/downloadFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	duration=$SECONDS
	echo "AWS,Storage,Download File from S3,"$duration

	SECONDS=0
	echo "Delete file from AWS S3 Buckets-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/deleteFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	duration=$SECONDS
	echo "AWS,Storage,Delete S3 File,"$duration

	SECONDS=0
	echo "Delete AWS S3 Buckets-->"		
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"
	duration=$SECONDS
	echo "AWS,Storage,Delete Vol/Bucket,"$duration

}


testazure()
{
	#Azure compute
	SECONDS=0
	echo "Create Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/createvm?name=AZ1&size=Standard_B1s&image_name=UbuntuServer&resource_group=libcloud&storage_account=libclouddiag209&network_intf=libcloud-vnet&blob_container=test123" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Compute,Create VM,"$duration

	SECONDS=0
	echo "List Azure VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/listvm" -H "accept: application/json"
	duration=$SECONDS
	echo "Azure,Compute,List VM,"$duration

	SECONDS=0	
	echo "Stop Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/stopvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Compute,Stop VM,"$duration

	SECONDS=0
	echo "Start Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/startvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Compute,Start VM,"$duration

	SECONDS=0
	echo "Delete Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/deletevm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Compute,Delete VM,"$duration

	SECONDS=0	
	#Azure storage
	echo "Create Azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVol?volname=newvol1&volsize=1&location=eastus&resource_group=libcloud&ex_account_type=Standard_LRS" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Storage,Create Vol/Bucket,"$duration

	SECONDS=0
	echo "create azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVolSnap?volname=newvol&snapname=newsnap&resource_group=libcloud&location=eastus" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Storage,Create Volume Snapshot,"$duration

	SECONDS=0
	echo "delete azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVolSnap?snapname=newsnap&resource_group=libcloud" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Storage,Delete Volume Snapshot,"$duration

	SECONDS=0
	echo "delete azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVol?volname=newvol&resource_group=libcloud" -H  "accept: application/json"
	duration=$SECONDS
	echo "Azure,Storage,Delete Vol/Bucket,"$duration

}


testgoogle()
{
	
	echo "Create Google VM"
	SECONDS=0
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/createvm?name=test123&size=g1-small&image_name=debian-8&location=us-east1-b" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Compute,Create VM,"$duration

	SECONDS=0
	echo "List Google VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/listvm" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Compute,List VM,"$duration

	SECONDS=0
	echo "Stop Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/stopvm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Compute,Stop VM,"$duration

	SECONDS=0
	echo "Start Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/startvm?vmname=test123" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Compute,Start VM,"$duration

	SECONDS=0
	echo "Delete Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/deletevm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Compute,Delete VM,"$duration
	
	#Google storage
	SECONDS=0
	echo "Create Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVol?volname=newvol1&volsize=1&location=us-east1-b" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Storage,Create Vol/Bucket,"$duration
	
	SECONDS=0
	echo "create Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVolSnap?volname=newvol1&snapname=newvol1snap" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Storage,Create Volume Snapshot,"$duration
	
	SECONDS=0
	echo "delete Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVol?volname=newvol1" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Storage,Delete Volume Snapshot,"$duration
	
	SECONDS=0	
	echo "delete Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVolSnap?snapname=newvol1snap" -H  "accept: application/json"
	duration=$SECONDS
	echo "Google,Storage,Delete Vol/Bucket,"$duration
}


if [ $# -ne 2 ]
  then
        echo "Missing parameters. Usage example: benchmarking.sh 5 AWS"
        exit 1
fi

if [ "$CLOUD" == "AWS" ] || [ "$CLOUD" == "GOOGLE" ] || [ "$CLOUD" == "AZURE" ]
  then
       echo "Valid values for cloud are: AWS or GOOGLE or AZURE"
        exit 1
fi  

echo $ITER
echo $CLOUD

i=0
#testaws


