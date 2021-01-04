from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from instafollowers import unfollowbot
from flask import Flask , render_template
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2 as pg
import csv
import time
import os
from datetime import datetime

app=Flask(__name__,template_folder='templatess')
sched=BackgroundScheduler(daemon=True)
namess=[]

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--no-sandbox")
op.add_argument("--headless")
op.add_argument("--disable-dev-shm-usage")
op.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
drive = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
conn=pg.connect(host='ec2-18-232-232-96.compute-1.amazonaws.com',database='de519828rorgih',user='nhtbmdiomahfmr',port='5432',password='e7695b9bfebebe96f6c625e836a6abc58f1e30ca6a00c2cab39a8b3a22e85667')
curr=conn.cursor()

def timed_job(name):
    print('This job is run every three minutes.')
    bot=unfollowbot()
    list1=bot.getfollowerlist(name,drive)
    curr.execute('SELECT name FROM public.following_updated_new;')
    list2=curr.fetchall()
    list3=[]
    for pos1, i in enumerate(list2):
        list3.append(i[0])

    curr.execute('SELECT MAX(id) FROM public.unfollow_final')
    l=curr.fetchone()
    if l[0] != None:
        count=l[0]
        sql='INSERT INTO public.unfollow_final (id,name) VALUES (%s,%s);'
        for pos1, i in enumerate(list3):
            if str(i) not in list1:
                values=(count,i)
                curr.execute(sql,values)
                count+=1
    else:
        sql = 'INSERT INTO public.unfollow_final (id,name) VALUES (%s,%s);'
        for pos1, i in enumerate(list3):
            if str(i) not in list1:
                values = (pos1, i)
                curr.execute(sql, values)


def refresh():
    print('refreshing page')
    global drive
    drive.get('https://unfollow-app.herokuapp.com/')
    time.sleep(3)
    drive.refresh()

sched.add_job(timed_job,'interval', minutes=30, args=['tommyngn'], next_run_time=datetime.now())
sched.add_job(refresh, 'interval', minutes=3)
sched.start()

@app.route('/')
def home():
    global curr
    curr.execute('SELECT name FROM public.unfollow_final;')
    row=curr.fetchall()
    namee=[]
    for i in row:
        namee.append(i[0])

    return render_template('index.html',names=namee)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)