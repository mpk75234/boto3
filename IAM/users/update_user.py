'''
always remember to import boto3 and create your client at start of
script:

import boto3

client = boto3.client('iam')
---------------------------------------------
using boto3.update_user on a very basic level if you don't like that..too bad who the hell are you anyhow Jeff Bezos?
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Client.update_user
'''
import boto3
iam = boto3.client('iam')
'''
before:
mike@mkdc752341u:~/Desktop/AWS/boto3/IAM$ python3 list_users.py
{'Users': [{'Path': '/', 'UserName': 'Dashnee', 'UserId': 'AIDASLJ6LMJ774WV2QZ
PD', 'Arn': 'arn:aws:iam::161728914047:user/Dashnee', 'CreateDate': datetime.d
atetime(2020, 10, 10, 15, 39, 58, tzinfo=tzutc())}, {'Path': '/', 'UserName':
'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW', 'Arn': 'arn:aws:iam::161728914047:u
ser/mike', 'CreateDate': datetime.datetime(2020, 10, 8, 21, 48, 54, tzinfo=tzu
tc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '16a59bb0-91e
1-4397-9c42-7ae99c693765', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requ

estid': '16a59bb0-91e1-4397-9c42-7ae99c693765', 'content-type': 'text/xml', 'c
ontent-length': '795', 'date': 'Sat, 10 Oct 2020 15:40:08 GMT'}, 'RetryAttempt
s': 0}}
Dashnee
'''
iam.update_user(NewUserName='BadIdeaBrad', UserName='Dashnee')
'''
after
mike@mkdc752341u:~/Desktop/AWS/boto3/IAM$ python3 list_users.py
{'Users': [{'Path': '/', 'UserName': 'BadIdeaBrad', 'UserId': 'AIDASLJ6LMJ774W
V2QZPD', 'Arn': 'arn:aws:iam::161728914047:user/BadIdeaBrad', 'CreateDate': da
tetime.datetime(2020, 10, 10, 15, 39, 58, tzinfo=tzutc())}, {'Path': '/', 'Use
rName': 'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW', 'Arn': 'arn:aws:iam::161728
914047:user/mike', 'CreateDate': datetime.datetime(2020, 10, 8, 21, 48, 54, tz
info=tzutc())}], 'IsTruncated': False, 'ResponseMetadata': {'RequestId': '5642
8887-439c-4647-b22a-c15aa3746843', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-a

mzn-requestid': '56428887-439c-4647-b22a-c15aa3746843', 'content-type': 'text/
xml', 'content-length': '803', 'date': 'Sat, 10 Oct 2020 15:49:37 GMT'}, 'Retr
yAttempts': 0}}
BadIdeaBrad
'''
