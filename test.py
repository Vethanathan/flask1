from ibm_botocore.client import Config
import ibm_boto3

cos = ibm_boto3.client("s3",
                      ibm_api_key_id="ipYVCUa76edOX_KWnbCo9fl3H5C5zR742y-gEM70BJAf",
                      ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/3e8473069ea8486cb7cefcc4946eebac:4031b620-3fe2-4fa1-9250-b42b3133f81d::",
                      config=Config(signature_version="oauth"),
                      endpoint_url="https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints")
# cos.upload_file("README.md", "vethanathan", "<target_file_name>")
cos.download_file("vethanathan", "main.5296d227.css", "\\templates")
