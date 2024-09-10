import time
from threading import Thread

def test1():
    time.sleep(5)
    print ("def test1")

def test2():
    time.sleep(5)
    print ("def test2")

tr1 = Thread(target=test1)
tr2 = Thread(target=test2)

tr1.start()
tr2.start()