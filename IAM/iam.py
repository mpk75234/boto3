'''
IAM user generator with all bunny-slope CRUD functions
'''
import boto3
class IAM:
    def __init__(self,name):
        self.name = name
        self.iam = boto3.client('iam')
    def c(self):
        self.iam.create_user(UserName=self.name)
    def r(self):
        users = self.iam.list_users()
        print(users)
    def u(self,nuname):
        self.iam.update_user(NewUserName=nuname, UserName=self.name)
        self.r()
    def d(self):
        self.iam.delete_user(UserName=self.name)
        self.r()


if __name__ == '__main__':
    carlos = IAM('carlos')
    carlos.c()
    carlos.r()
