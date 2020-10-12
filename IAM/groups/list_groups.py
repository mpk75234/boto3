'''
bunny-slope example of list_groups from Python boto3 SDK
'''
import boto3

'''
generate IAM client
'''
iam = boto3.client('iam')
groupz = iam.list_groups()
print(groupz)
