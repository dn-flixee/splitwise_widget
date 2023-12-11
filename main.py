from splitwise import Splitwise
import pprint
import os
from flask import Flask, render_template
from config import set_environment_variables

set_environment_variables()

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
API_KEY = os.environ.get('API_KEY')

# sObj = Splitwise(CONSUMER_KEY,CONSUMER_SECRET,api_key=API_KEY)
# user = sObj.getCurrentUser()
# friend = sObj.getFriends()
# pprint.pprint(friend[1].first_name)
# print(user.picture.small)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name="flixee")

if __name__ == '__main__':
    app.run(debug=True)



