from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from instafollowers import unfollowbot
from flask import Flask , render_template
from apscheduler.schedulers.background import BackgroundScheduler
import csv
import time
from datetime import datetime

app=Flask(__name__,template_folder='templatess')
sched=BackgroundScheduler(daemon=True)
namess=[]

def timed_job(name):
    print('This job is run every three minutes.')
    # global count
    global namess
    namess.append('hiii')
    print(namess,' yess')
    # names.clear()
    # count+=1
    # names.append(str(count))
    # bot = unfollowbot()
    # l = bot.getfollowerlist(name)
    # f = open('following_list_updated_new.csv', 'r')
    # g = list(csv.reader(f))
    # h=[]
    # for i in g:
    #     h.append(i[0])
    # for i in l:
    #     if str(i) not in h:
    #         names.append(i)
def refresh():
    print('refreshing page')
    path='/Users/tommynguyen/Desktop/chromedriver'
    drive = webdriver.Chrome(executable_path=path)
    drive.get('https://unfollow-app.herokuapp.com/')
    time.sleep(3)
    drive.refresh()


sched.add_job(timed_job,'interval', minutes=5, args=['noahthemac'], next_run_time=datetime.now())
sched.add_job(refresh, 'interval', minutes=20)
sched.start()

@app.route('/')
def home():

    return render_template('index.html',names=namess)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)