import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started"+time.ctime())
while(break_count < total_breaks):
     time.sleep(10)
     webbrowser.open("https://youtu.be/fyMhvkC3A84?list=PLzyYbaYKbahnDKc2MS0TEl7kGD2LIMr2F")
     break_count = break_count + 1
