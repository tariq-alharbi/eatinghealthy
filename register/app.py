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
cur=mydb.cursor()

def lambda_handler(event, context):
    body = json.loads(event["body"])
    username=body["username"]
    password=body["password"]
    height=body["height"]
    weight=body["weight"]
    allergy=body["allergy"]

    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "register": register(username,password,height,weight,allergy,mydb),
            # "location": ip.text.replace("\n", "")
        }),
    }

def register (username,password,height,weight,allergy,db):
    id=''
    print(weight)
    try:

        sql = "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"
        cur.execute(sql, (username, password))
        sql ="select * from user where username =%s"
        cur.execute(sql, (username))
        result = cur.fetchone()
        while result is not None:
                id=result[0]
                cur.execute(f"INSERT INTO `details` (`userId`, `height`,`weight`, `allergy`) VALUES ({id}, {height},{weight},'{allergy}')")

                return id
    except :
        return 0
    



    


    
            

