# How to create a network access control list (NACL) in a VPC using boto3

## What is network access control list (NACL)?
### A network access control list (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.You can follow this [link](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) to know more.



-------------

### I have define the script to create the Network access control list[NACL]in the VPC. You just need to pass the region and VPC id at the run time and one more thing your aws credential (access and secret key) must be configure in your system then your resource will be create in the VPC. You need to follow the below commands.

**Files:** 

```
       create.py
```
## Apply the script using below commands:
1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command:

        python3 <create.py>


