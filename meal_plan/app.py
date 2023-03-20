import json
import ssl
import pymysql.cursors
from mealPlan import plan_my_meal

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

mydb = pymysql.connect(
  host="",
  user="",
  password="",
  database='',
  ssl={
        'ca': './'
    }
)


def lambda_handler(event, context):
    body = json.loads(event["body"])
    id=body["state"]
    pref=body["data"]
    print(id)
    print(pref)
    data=""

    for s in pref:
        data=data +" " + s
    
    
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "meal": plan_my_meal(data,int(id)),
            # "location": ip.text.replace("\n", "")
        }),
    }



