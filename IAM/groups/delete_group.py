'''
buuny-slope example of delete_group from boto3 Python3 SDK
'''
import boto3

'''
generate client
'''
iam = boto3.client('iam')

iam.delete_group(GroupName='hardcore')
