import json
import pymysql.cursors

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



def execute_Q (queue):
    cur.execute(queue)
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
    cur.excute(f'SELECT conversion FROM conversion WHERE userId = {userId}')
    conversionHistory =  cur.fetchall()

    decodedLogs = json.loads(conversionHistory)

    updatedLogs = decodedLogs.update({'message': f'{conversion}'})

    cur.excute(f'UPDATE conversion SET conversion = {updatedLogs} WHERE userId = {userId}')
    

# type \ neutrinos 
def plan_my_meal (json_pref, userId):
    mealType = json_pref ['type']
    mealNeutrinos = json_pref['neutrinos']

    userAllergy = get_user_allergy(userId)
    userHeight = get_user_height(userId)
    userWeight = get_user_weight(userId)

    queue = f'give me a weekly meal plan imppropate to my height is {userHeight}+ and weight is {userWeight} with these neutrinos {mealNeutrinos} '
    
    if userAllergy != 'null' :
        queue +=  f'and i have these allergys {userAllergy}'
    
    log_conversion(queue)

    return execute_Q(cur, queue)






# # Close connection
# cnx.close()