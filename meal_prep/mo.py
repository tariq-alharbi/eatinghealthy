import requests
from mealPlan import get_user_weight, get_user_height


URL = 'https://experimental.willow.vectara.io/v1/chat/completions'



headers = {
'Content-Type' :'application/json',
'customer-id':'3586459297',
'x-api-key': 'zqt_1cUGoc57wFV3fYyHTjRAF3vR4oDKz3_dmaSYQA'
}



def meal_prep (meal_ingredients, userId):

    height = get_user_height(userId)
    weight = get_user_weight(userId)

    body = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": f" make me a meal with this in ingredients "+ meal_ingredients + 'imppropate to my height is '+ str(height) +'+ and weight is '+ str(weight)
        }
    ]
}
    r = requests.post(URL,headers = headers ,json= body )
    return (r.json()['choices'][0]['message']['content'])



