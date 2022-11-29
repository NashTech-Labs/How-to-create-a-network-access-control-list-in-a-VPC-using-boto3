import logging
import boto3
from botocore.exceptions import ClientError
import time
REGION= input("Please, Enter the region name where you want to Delete this NACL:-\n=")

# logger config
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format=' %(message)s')

vpc = boto3.resource("ec2", region_name=REGION)


def create_nacl(vpc_id):
    try:
        response = vpc.create_network_acl(
            VpcId=vpc_id,
            TagSpecifications=[
                {'ResourceType':'network-acl',
                    'Tags': [{'Key': 'Name','Value': 'test-nacl'}]
                },
            ])

    except ClientError:
        logger_info.exception('Sorry, Not able to create the network ACL in given VPC')
        raise
    else:
        return response

if __name__ == '__main__':
    # Constants
    VPC_ID=input("Please, Enter the VPC ID to create NACL in it:- \n=")
    # VPC_ID = 'vpc-0e23aa401934e3988'
    for i in range(3):
        logger_info.info(f'Please wait ......  \n We are creating your NACL...\U0001F570')
        time.sleep(5)
    nacl = create_nacl(VPC_ID)
    logger_info.info(
        f'\nHurry, Your NACL has been created with this ID: {nacl.id} \U0001F44D ')
