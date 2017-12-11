from threading import Thread
import time
from threading import Lock

Lk = Lock()			# 线程锁

def timer(name, delay, repeat):
	print(name+ ' Thread start\n')
	for i in range(repeat):
		time.sleep(delay)
		print(name + ' current time is ' + str(time.ctime(time.time())))
	print(name + ' Thread is completed.\n')

def Main():

	''' 多线程 '''
#	t1 = Thread(target=timer, args=('Timer1', 1, 5))
#	t2 = Thread(target=timer, args=('Timer2', 3, 5))
#	t1.start()
#	t2.start()
#	Lk.acquire()	# 上锁
#	t1.join()		# 加入主线程
#	t2.join()		# 加入主线程
#	Lk.release()	# 解锁
	
	''' 线程池 '''	
	threads = []
	for i in range(4):
		t = Thread(target=timer, args=('Timer'+str(i), 1+i, 5))
		threads.append(t)
		
	for thread in threads:
		thread.start()
		thread.join()		# 加入主线程 将会逐一执行，如果不加入主线程则会同时执行
		
	print('Main is finished.\n')
	
if __name__ == '__main__':
	Main()

	
