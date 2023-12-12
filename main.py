from splitwise import Splitwise
from flask import Flask, render_template
from tasks import fetch_data


app = Flask(__name__)
@app.route('/')
def index():
    user, top_4_friends, amount_top4, notifications = fetch_data()
    return render_template('index.html',amount=amount_top4,friends=top_4_friends,user=user,notifications=notifications)

if __name__ == '__main__':
    port = 5550
    app.run(debug=True)



