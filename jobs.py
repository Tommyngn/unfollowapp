from apscheduler.schedulers.blocking import BlockingScheduler
from instafollowers import  unfollowbot
import csv
from datetime import datetime

names=[]
# sched=BlockingScheduler(daemon=True)

# @sched.scheduled_job('interval', minutes=5, args=['noahthemac'],next_run_time=datetime.now())
def timed_job(name):
    print('This job is run every three minutes.')
    global names
    names.append('hiii')
    print(names)
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

# sched.start()