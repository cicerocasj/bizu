from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

import multiprocessing as mp
import time
def target(x):
   time.sleep(4)
   print("processing...")
   return "callback"
   global p
   p.close()
   p.terminate()
   p.join()


def result(callback):
	print 'finish', callback

def index(request):
	global p
	p = mp.Pool(processes=1)
	p.apply_async(target, ("arg", ),callback=result)
	print "start..."
	return HttpResponse("hello")


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
]

'''
start...
[06/May/2016 18:32:41] "GET / HTTP/1.1" 200 5
processing...
finish callback

'''
