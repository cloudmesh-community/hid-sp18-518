#/bin/sh
#Script name: benchmarking.sh
#Purpose: This script is written to run curl commands and
#collect duration results that can be used in benchmarking.
#
#Usage: benchmarking.sh <No. of iteration> <Cloud Name>
#	For ex. benchmarking.sh 5 AWS
#Reference: 
# https://www.linuxquestions.org/questions/linux-newbie-8/calculate-duration-in-seconds-in-bash-844392/

ITER=$1
CLOUD=$2


#for (i=0; i < $ITER; i++)
#for (i=0; i < 10; i++)
#do
#	echo $i 
#done

testaws(){

	#echo "Create AWS EC2 VM -->"
	START_TIME=`date +%s`
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"vmId\": \"NA\",  \"name\": \"myVM\",  \"image\": \"ami-25615740\",  \"region\": \"us-east-2\",  \"size\": \"t2.micro\",  \"status\": \"NA\"}"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Compute,Create VM," $duration


	START_TIME=`date +%s`
	#echo "Get AWS VM List by region-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Compute,List VM," $duration

	START_TIME=`date +%s`
	#echo "Get AWS VM by Name-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Compute,Get VM Details," $duration

        START_TIME=`date +%s`
        #echo "Stop AWS EC2 VM-->"      
        curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/stop" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
        END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
        echo "AWS,Compute,Stop VM," $duration


	START_TIME=`date +%s`
	#echo "Start AWS EC2 VM-->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/start" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"	
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Compute,Start VM," $duration

	START_TIME=`date +%s`
	#echo "Terminate AWS EC2 VM-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/terminate" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Compute,Delete VM," $duration

	START_TIME=`date +%s`	
	#echo "Get AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Get Vol/Bucket Details," $duration

	START_TIME=`date +%s`	
	#echo "Create AWS S3 Buckets-->"	
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Create Vol/Bucket," $duration

	START_TIME=`date +%s`
	#echo "Upload file to AWS S3 bucket"
	touch samplefile.txt
	curl -X POST "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/uploadFile" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "fileName=@samplefile.txt;type=text/markdown"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Upload File to S3," $duration

	START_TIME=`date +%s`
	#echo "List files from AWS S3 Buckets-->"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,List Vol/Bucket Details," $duration

	START_TIME=`date +%s`
	#echo "Download file from AWS S3 bucket"	
	curl -X GET "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/downloadFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Download File from S3," $duration

	START_TIME=`date +%s`
	#echo "Delete file from AWS S3 Buckets-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/cloudmeshbkt/deleteFile" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "fileName=samplefile.txt"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Delete S3 File," $duration

	START_TIME=`date +%s`
	#echo "Delete AWS S3 Buckets-->"		
	curl -X DELETE "http://localhost:8080/cloudmesh/storage/aws/s3/bucket" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "bucketName=cloudmeshbkt"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "AWS,Storage,Delete Vol/Bucket," $duration

}


testazure()
{
	#Azure compute
	START_TIME=`date +%s`
	#echo "Create Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/createvm?name=AZ1&size=Standard_B1s&image_name=UbuntuServer&resource_group=libcloud&storage_account=libclouddiag209&network_intf=libcloud-vnet&blob_container=test123" -H  "accept: application/json"
	#echo $duration
	END_TIME=`date +%s`
	duration=$(($END_TIME-$START_TIME))
	echo "Azure,Compute,Create VM,$duration"

	START_TIME=`date +%s`
	#echo "List Azure VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/listvm" -H "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Compute,List VM," $duration

	START_TIME=`date +%s`	
	#echo "Stop Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/stopvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Compute,Stop VM," $duration

	START_TIME=`date +%s`
	#echo "Start Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/startvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Compute,Start VM," $duration

	START_TIME=`date +%s`
	#echo "Delete Azure VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/azure/deletevm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Compute,Delete VM," $duration

	START_TIME=`date +%s`	
	#Azure storage
	#echo "Create Azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVol?volname=newvol1&volsize=1&location=eastus&resource_group=libcloud&ex_account_type=Standard_LRS" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Storage,Create Vol/Bucket," $duration

	START_TIME=`date +%s`
	#echo "create azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVolSnap?volname=newvol&snapname=newsnap&resource_group=libcloud&location=eastus" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Storage,Create Volume Snapshot," $duration

	START_TIME=`date +%s`
	#echo "delete azure volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVolSnap?snapname=newsnap&resource_group=libcloud" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Storage,Delete Volume Snapshot," $duration

	START_TIME=`date +%s`
	#echo "delete azure volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVol?volname=newvol&resource_group=libcloud" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Azure,Storage,Delete Vol/Bucket," $duration

}


testgoogle()
{
	
	#echo "Create Google VM"
	START_TIME=`date +%s`
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/createvm?name=test123&size=g1-small&image_name=debian-8&location=us-east1-b" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Compute,Create VM," $duration

	START_TIME=`date +%s`
	#echo "List Google VMs"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/listvm" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Compute,List VM," $duration

	START_TIME=`date +%s`
	#echo "Stop Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/stopvm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Compute,Stop VM," $duration

	START_TIME=`date +%s`
	#echo "Start Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/startvm?vmname=test123" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Compute,Start VM," $duration

	START_TIME=`date +%s`
	#echo "Delete Google VM"
	curl -X GET "http://localhost:8080/cloudmesh/compute/google/deletevm?vmname=test123&location=us-east1-b" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Compute,Delete VM," $duration
	
	#Google storage
	START_TIME=`date +%s`
	#echo "Create Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVol?volname=newvol1&volsize=1&location=us-east1-b" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Storage,Create Vol/Bucket," $duration
	
	START_TIME=`date +%s`
	#echo "create Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/createVolSnap?volname=newvol1&snapname=newvol1snap" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Storage,Create Volume Snapshot," $duration
	
	START_TIME=`date +%s`
	#echo "delete Google volume snap"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVol?volname=newvol1" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Storage,Delete Volume Snapshot," $duration
	
	START_TIME=`date +%s`	
	#echo "delete Google volume"
	curl -X GET "http://localhost:8080/cloudmesh/storage/google/deleteVolSnap?snapname=newvol1snap" -H  "accept: application/json"
	END_TIME=`date +%s`;duration=$(($END_TIME-$START_TIME))
	echo "Google,Storage,Delete Vol/Bucket," $duration
}


if [ $# -ne 2 ]
  then
        echo "Missing parameters. Usage example: benchmarking.sh 5 AWS"
        exit 1
fi


if [ "$CLOUD" != "AWS" ] && [ "$CLOUD" != "GOOGLE" ] && [ "$CLOUD" != "AZURE" ];
  then
       echo "Valid values for cloud are: AWS or GOOGLE or AZURE"
       exit 1
fi  

#echo $ITER
#echo $CLOUD

#testazure

echo "cloudname,opType,opName,duration"

for i in `seq 1 $ITER`
do
        if [ "$CLOUD" = "AWS" ]; then
                testaws
        elif [ "$CLOUD" = "AZURE" ]; then
                testazure
        elif [ "$CLOUD" = "GOOGLE" ]; then
                testgoogle
        fi
	sleep 120
done

