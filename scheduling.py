import time
import sched

#setting up a schedular
sc = sched.scheduler(time.time, time.sleep)

#function that will run according to our given time
def scdul_code():
    print('This string is running according to your schedule')


#function that will delay
def delay_function():

    #schedued to run given function after 5 secodns
    sc.enter(5,1,scdul_code)

    #run the scheduler job
    sc.run()

#calling function
delay_function()
