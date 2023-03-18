import json
import pymysql.cursors
import requests

# Connect to server

cnx = pymysql.connect(
  host="ap-south.connect.psdb.cloud",
  user="ztlsi70lnvxkck25qq2c",
  password="pscale_pw_qCBr6RoYBYKni5sIfBcribmFKLzRLN8rLe0FtBP0qLu",
  database='eatinghealthy',
  ssl={
        'ca': './cacert-2023-01-10.pem'
    }
)

URL = 'https://experimental.willow.vectara.io/v1/chat/completions'

headers = {
'Content-Type' :'application/json',
'customer-id':'3586459297',
'x-api-key': 'zqt_1cUGoc57wFV3fYyHTjRAF3vR4oDKz3_dmaSYQA'
}

cur = cnx.cursor()

def get_cursor ():
    cnx = pymysql.connect(
  host="ap-south.connect.psdb.cloud",
  user="ztlsi70lnvxkck25qq2c",
  password="pscale_pw_qCBr6RoYBYKni5sIfBcribmFKLzRLN8rLe0FtBP0qLu",
  database='eatinghealthy',
  ssl={
        'ca': './cacert-2023-01-10.pem'
    }
)
    return cnx.cursor()


def execute_Q (query):
    cur.execute(query)
    return cur.fetchall()

def get_user_allergy (userId):
    cur.execute(f'SELECT allergy FROM details WHERE userId = {userId}')
    return cur.fetchall()

def get_user_weight (userId):
    cur.execute(f'SELECT weight FROM details WHERE userId = {userId}')
    return cur.fetchall()

def get_user_height (userId):
    cur.execute(f'SELECT height FROM details WHERE userId = {userId}')
    return cur.fetchall()

def log_conversion (conversion , userId):
    cur.execute(f'SELECT conversion FROM conversation WHERE userId = {userId}')
    conversionHistory =  cur.fetchall()

    decodedLogs = json.loads(conversionHistory)

    updatedLogs = decodedLogs.update({'message': f'{conversion}'})

    cur.excute(f'UPDATE conversion SET conversation = {updatedLogs} WHERE userId = {userId}')
    

# type \ neutrinos 
def plan_my_meal (json_pref, userId):


    userAllergy = get_user_allergy(userId)
    userHeight = get_user_height(userId)
    userWeight = get_user_weight(userId)

    query = f'give me a weekly meal plan imppropate to my height is {userHeight}+ and weight is {userWeight} with {plan_my_meal} '
    
    print(query)

    if userAllergy != 'null' :
        query = query + f'and i have these allergys {userAllergy}'
    
    # log_conversion(query,userId)

    body = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": query
        }
    ]
}

    r = requests.post(URL,headers = headers ,json= body )
    return (r.json()['choices'][0]['message']['content'])

