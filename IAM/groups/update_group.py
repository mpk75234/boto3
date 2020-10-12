'''
bunny-slope example of update_group from boto3 Python SDK
'''
import boto3

'''
generate IAM client
'''
iam = boto3.client('iam')

iam.update_group(GroupName='core',NewGroupName='hardcore')
