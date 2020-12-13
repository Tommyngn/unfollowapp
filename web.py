from instafollowers import unfollowbot
from flask import Flask , render_template
from apscheduler.schedulers.background import BackgroundScheduler
import csv
import time
from datetime import datetime

app=Flask(__name__,template_folder='templatess')
# sched=BackgroundScheduler(daemon=True)
names=[]
count=0

# def timed_job(name):
#     print('This job is run every three minutes.')
#     global count
#     global names
#     names.clear()
#     count+=1
#     names.append(str(count))
#     bot = unfollowbot()
#     l = bot.getfollowerlist(name)
#     f = open('following_list_updated_new.csv', 'r')
#     g = list(csv.reader(f))
#     h=[]
#     for i in g:
#         h.append(i[0])
#     for i in l:
#         if str(i) not in h:
#             names.append(i)

# sched.add_job(timed_job,'interval', minutes=5, args=['noahthemac'], next_run_time=datetime.now() )

@app.route('/')
def home():
    return render_template('index.html',names=names)



if __name__ == '__main__':
    # sched.start()
    app.run(debug=True, use_reloader=False)