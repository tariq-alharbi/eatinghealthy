import json
import ssl
import pymysql.cursors
from mo import meal_prep

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
    body = json.loads(event["body"])
    id=body["id"]
    ingredients=body["ingredients"]
    print(id)
    print(ingredients)
    
    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "meal": meal_prep(ingredients,id),
            # "location": ip.text.replace("\n", "")
        }),
    }



