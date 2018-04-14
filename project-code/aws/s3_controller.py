import connexion
import six

from swagger_server.models.awss3 import AWSS3  # noqa: E501
from swagger_server import util

import aws_s3
import sys
import util


DOWNLOAD_DIR = util.getDownloadDir()

def create_bucket(bucketName):  # noqa: E501
    """create bucket

    create s3 bucket # noqa: E501

    :param bucketName: s3 bucket name
    :type bucketName: str

    :rtype: None
    """
    if bucketName == "":
        return "Please provide bucket name"
    
    try:
        response = aws_s3.createBucket(bucketName)
        return "Bucket Created Successfully-->" + bucketName
    except Exception, err:
        print Exception, err
        #print("VM create error:", sys.exc_info()[0])
        return "Bucket creation failed-->"+ str(err)
    

def delete_bucket(bucketName):  # noqa: E501
    """delete bucket

    delete s3 bucket # noqa: E501

    :param bucketName: s3 bucket name
    :type bucketName: str

    :rtype: None
    """
    if bucketName == "":
        return "Please provide bucket name"
    
    try:
        aws_s3.deleteBucket(bucketName)
        return "Bucket deleted successfully-->" + bucketName
    except Exception, err:
        print Exception, err
        return "Bucket deletion failed-->" + str(err)


def delete_file(bucketName, fileName):  # noqa: E501
    """delete file

     # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if bucketName == "" or fileName == "":
        return "Please provide bucket name and file name"
    
    try:
        aws_s3.deleteFile(bucketName,fileName)
        return "File deleted successfully --" + fileName
    except Exception, err:
        print Exception, err
        return "File deletion failed-->" + str(err)


def get_buckets():  # noqa: E501
    """get_buckets

    Returns list of buckets # noqa: E501


    :rtype: List[AWSS3]
    """
    
    buckets = []
    try:
        response = aws_s3.getBuckets()
        for bucket in response['Buckets']:
            awss3 = AWSS3( bucket_name=bucket["Name"], file_name=None)
            buckets.append(awss3)
        return buckets
    except Exception, err:
        print Exception, err
        #print("VM create error:", sys.exc_info()[0])
        return  str(err)
    
    
def get_files(bucketName):  # noqa: E501
    """list bucket files

    list bucket files # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str

    :rtype: List[AWSS3]
    """
    if bucketName == "":
        return "Please provide bucket name"
    
    
    files = []
    try:
        fileList = aws_s3.getFiles(bucketName)
        if fileList is None:
            return "No file present"
        
        for s3file in fileList:
            awss3 = AWSS3( bucket_name=None, file_name=s3file.key)
            files.append(awss3)
        return files
    except Exception, err:
        print Exception, err
        return str(err)
    

def upload_file(bucketName, fileName):  # noqa: E501
    """upload file

     # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    try:
        aws_s3.uploadFileObj(bucketName, fileName.filename, fileName)
        return 'File uploaded -- ' + fileName.filename
    except Exception, err:
        print Exception, err
        return str(err)
    
def download_file(bucketName, fileName):  # noqa: E501
    """download file

    download file to download directory # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if bucketName == "" or fileName == "":
        return "Please provide bucket name and file name"
    
    try:
        
        downloadPath = DOWNLOAD_DIR + "/" + fileName
        aws_s3.downloadFile(bucketName,fileName, downloadPath)
        return 'File downloaded to  -- ' + downloadPath
    except Exception, err:
        print Exception, err
        return str(err)

