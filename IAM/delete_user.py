import boto3
iam = boto3.client('iam')
'''
before:
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

BadIdeaBrad just ain't working out....
'''
iam.delete_user(UserName='BadIdeaBrad')
'''
y luego....
mike@mkdc752341u:~/Desktop/AWS/boto3/IAM$ python3 list_users.py
{'Users': [{'Path': '/', 'UserName': 'mike', 'UserId': 'AIDASLJ6LMJ7RJZ6TRACW'
, 'Arn': 'arn:aws:iam::161728914047:user/mike', 'CreateDate': datetime.datetim
e(2020, 10, 8, 21, 48, 54, tzinfo=tzutc())}], 'IsTruncated': False, 'ResponseM
etadata': {'RequestId': 'f51cc7df-42af-4092-9489-013f7f4a0167', 'HTTPStatusCod

e': 200, 'HTTPHeaders': {'x-amzn-requestid': 'f51cc7df-42af-4092-9489-013f7f4a
0167', 'content-type': 'text/xml', 'content-length': '545', 'date': 'Sat, 10 O
ct 2020 15:52:58 GMT'}, 'RetryAttempts': 0}}
mike <---control freak?
'''
