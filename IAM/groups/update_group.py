'''
bunny-slope example of update_group from boto3 Python SDK
'''
import boto3

'''
generate IAM client
'''
iam = boto3.client('iam')

try:
    iam.update_group(GroupName='notepad_gurus',NewGroupName='hardcore')
except:
    print(f"NOT DERE....{e}")
