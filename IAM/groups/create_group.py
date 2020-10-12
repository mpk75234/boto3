'''
bunny-slope boto3 example of create_group using boto3 Python SDK
'''
import boto3

iam = boto3.client('iam')

'''
create group "core"
'''
iam.create_group(GroupName='core')
