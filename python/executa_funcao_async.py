#!/usr/bin/env python
import multiprocessing
import datetime as dt
import os


def f(dado):
    try:
        print "executa...", dado
    except Exception as e:
        print e


pool = multiprocessing.Pool()
ini = dt.datetime.now()
for i in range(1000):
    pool.apply_async(f, args=(i, ))
pool.close()
pool.join()
fim = dt.datetime.now()
print "ini:", ini
print "fim:", fim
print "total tempo:", (fim-ini).seconds
