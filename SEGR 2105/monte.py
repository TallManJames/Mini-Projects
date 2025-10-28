import random        #import for random variables
from time import process_time             #for process times
import math                  #for the real pi


def pi_estimate(runs):       #makes the different estimates easier
    inside_num = 0        #this is how many
    start_time = process_time()        #initial time before processing loop
    for i in range(runs):      #runs represents how many times I want this simulation to run to estimate pi
        temp_x = random.random()        #x value
        temp_y = random.random()        #y value
        if (temp_x**2 + temp_y**2) < 1:        # if (x^2 + y^2) is less than 1, then the dart landed inside that quartile of the circle
            inside_num += 1                  #landed in the circle
    end_time = process_time()           #final time after processing loop
    cpu_total_time = end_time - start_time            #difference of times
    if cpu_total_time >= 60:          #if total time is more than 60 seconds
        cpu_total_time = f"{int(cpu_total_time // 60)} minutes and {(cpu_total_time % 60):.8f} seconds"
    else:
        cpu_total_time = f"{cpu_total_time:.8f} seconds"        #if time is less than 60 seconds
    estimate = 4*(inside_num/runs)          # pi is around 4 times (darts inside / darts thrown)
    print(f"\nTime taken: {cpu_total_time}"        #total time to 8 decimal places
          f"\nApproximation of Pi: {estimate}"          #the estimation
          f"\nDifference: {math.pi - estimate}")        #math.pi is the real pi, this finds difference


print("Monte Carlo Finding Pi\n")
while True:
    userRuns = input("Enter how many darts: ")      #user inputs how many runs or "darts"
    try:
        userRuns = int(userRuns)           #tries to convert to integer
        if userRuns > 0:               #breaks statement IF the integer is greater than 0
            break
        else:
            print("Enter a value greater than 0")
    except ValueError:                     #this is incase there is a value error (ex: input is str)
        print("Enter a valid whole number")

pi_estimate(userRuns)            #runs the pi estimate with number of runs or "darts"