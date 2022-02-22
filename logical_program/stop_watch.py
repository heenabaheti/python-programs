import time
# stopwatch program
"""took two point as startpoint and endpoint assign current time value into this """
time_start = input("Press Enter Key to start the time.")
startPoint = time.time()

time_end = input("Press Enter Key to end the time.")
endPoint = time.time()
total_time = endPoint - startPoint
# print(total_time)
print("Total time is : ", round(total_time, 2), "sec")
