import webbrowser
import socketserver
import threading
import time


#url = 'https://github.com/josedavidgm1995'
#webbrowser.open(url)

def worker(num):
    """thread worker function"""
    print ("Worker "+str(num))
    time.sleep(2)
    return

threads = []
for i in range(5):
    
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
    
    print("For: "+str(i) )
    

def sleeper():
    while True:
        # Get user input
        # The input() method its a block method.
        # the program will wait until the user set an input
        num = input('How long to wait: ')
 
        # Try to convert it to a float
        try:
            num = float(num)
        except ValueError:
            print('Please enter in a number.\n')
            continue
 
        # Run our time.sleep() command,
        # and show the before and after time
        print('Before: %s' % time.ctime())
        time.sleep(num)
        print('After: %s\n' % time.ctime())
        
try:
    sleeper()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()