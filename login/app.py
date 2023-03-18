import json
import ssl
import pymysql.cursors

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

mydb = pymysql.connect(
  host="ap-south.connect.psdb.cloud",
  user="ztlsi70lnvxkck25qq2c",
  password="pscale_pw_qCBr6RoYBYKni5sIfBcribmFKLzRLN8rLe0FtBP0qLu",
  database='eatinghealthy',
  ssl={
        'ca': './cacert-2023-01-10.pem'
    }
)


def lambda_handler(event, context):
    username=event["queryStringParameters"]['username']
    password=event["queryStringParameters"]['password']
    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "login": login(username,password,mydb),
            # "location": ip.text.replace("\n", "")
        }),
    }

def login (username,password,db):
    with db.cursor() as cursor:
        # Read a single record
        sql ="select * from user where username =%s && password=%s"
        cursor.execute(sql, (username,password))
        result = cursor.fetchone()
        while result is not None:
            return(result[0])
            
        return 0

