from splitwise import Splitwise
import pprint
import os
from flask import Flask, render_template
from config import set_environment_variables
from tasks import fetch_data

# set_environment_variables()

# CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
# CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
# API_KEY = os.environ.get('API_KEY')

# sObj = Splitwise(CONSUMER_KEY,CONSUMER_SECRET,api_key=API_KEY)
# user = sObj.getCurrentUser()
# friends = sObj.getFriends()
# notifications = sObj.getNotifications()

# def total_amount(friend):
#     return sum(float(balance.getAmount()) for balance in friend.getBalances())

# # Sort friends based on the total amount
# sorted_friends = sorted(friends, key=total_amount, reverse=True)

# # Get the top 4 friends with the highest amounts
# top_4_friends = sorted_friends[:4]

# amount_top4 = []
# # Print amounts in all currencies for each friend
# for friend in top_4_friends:
#     total = ""
#     for i, balance in enumerate(friend.getBalances()):
#         amount = balance.getAmount()
#         currency_code = balance.getCurrencyCode()
#         total = total + f"{amount} {currency_code}"
#         if i < len(friend.getBalances()) - 1:
#             total = total +" + "
#     amount_top4.append(total)


app = Flask(__name__)
@app.route('/')
def index():
    user, top_4_friends, amount_top4, notifications = fetch_data()
    return render_template('index.html',amount=amount_top4,friends=top_4_friends,user=user,notifications=notifications)

if __name__ == '__main__':
    app.run(debug=True)



