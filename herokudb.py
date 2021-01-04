import psycopg2 as pg
import csv

conn=pg.connect(host='ec2-18-232-232-96.compute-1.amazonaws.com',database='de519828rorgih',user='nhtbmdiomahfmr',port='5432',password='e7695b9bfebebe96f6c625e836a6abc58f1e30ca6a00c2cab39a8b3a22e85667')
curr=conn.cursor()

curr.execute('SELECT MAX(id) FROM public.unfollow_final;')

l=curr.fetchone()

if l[0] != None:
    print(l[0])
else:
    print('none')
