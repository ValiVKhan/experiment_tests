#Imports
import time

#Variables
counter = 0
timer = float(10)
updatetime = 10

#Loop
while counter < 10:
    runfucntion()
    counter = counter + 1
    if ((time.time() - start_time)) > timer:
        print (counter)
        timer = timer + updatetime
