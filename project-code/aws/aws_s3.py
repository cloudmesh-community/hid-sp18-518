# -*- coding: utf-8 -*-
import boto3
import botocore
import util


ACCESS_ID = util.getAWSAccessID()
SECRET_KEY = util.getAWSSecretKey()

def getS3():
    return boto3.client('s3',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)
def createBucket(bucketName):
    s3 = getS3()
    s3.create_bucket(Bucket=bucketName)
    
def deleteBucket(bucketName):
    s3 = getS3()
    s3.delete_bucket(Bucket=bucketName)
    
def getBuckets():
    s3 = getS3()
    return s3.list_buckets()

def downloadFile(bucketName, fileName, downloadPath):
    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)
    try:
        s3.meta.client.download_file(bucketName,fileName, downloadPath)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def downloadFileObj(bucketName, fileName):
    s3 = getS3()
    
    try:
        with open(fileName, 'wb') as fileObj:
            s3.download_fileobj(bucketName, fileName, fileObj)
        return fileObj
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise            

def uploadFile(bucketName, fileName, filePath):
    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)
    try:
        s3.meta.client.upload_file(filePath,bucketName,fileName)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

def uploadFileObj(bucketName, fileName, fileObj):
    s3 = getS3()
    try:
        #with open(fileObj, 'rb') as data:
        s3.upload_fileobj(fileObj, bucketName, fileName)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
 

def deleteFile(bucketName, fileName):
    s3 = getS3()
    s3.delete_object(Bucket=bucketName, Key=fileName)

def getFiles(bucketName):
    s3 = boto3.resource('s3',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)
    bucket = s3.Bucket(bucketName)
    return bucket.objects.all()



"""

response = getBuckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)

downloadFile("sush-bucket1","sample-app.png", "/home/sushant/e516/project/code/aws/sample-app.png") 

uploadFile("sush-bucket1","sample-app.png", "/home/sushant/e516/project/code/aws/sample-app.png")       

deleteFile("sush-bucket1","sample-app.png")

createBucket("sush-bucket2")

deleteBucket("sush-bucket2")

print getFiles("sush-bucket1")

for obj in getFiles("sush-bucket3"):
    print(obj.key)

"""
#print downloadFileObj("cloudmeshbkt", "sample-app.png")