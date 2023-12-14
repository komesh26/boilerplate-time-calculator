import datetime
import re

def add_time(start, duration, day_of_week = ""):
    
    start_hour, start_minute, start_med = re.split(r":| ", start)
    du_hour , du_minute = duration.split(':')
    res_hour = int(start_hour) + int(du_hour)
    res_minute = int(start_minute) + int(du_minute)
    days = 0
    whatday=""
    res_med= start_med

    while res_minute >= 60:
        res_hour +=1
        res_minute-=60

    while res_hour >= 24:
        res_hour -= 24
        days +=1
    
    if int(start_hour) < 12 and res_hour >= 12:
        if start_med == "PM":
            res_med = "AM"
            days +=1
        elif start_med == "AM":
            res_med = "PM"
    
    if days == 1:
        whatday = " (next day)"
    elif days > 1:
        whatday= " (" + str(days) + " days later)"

    if res_hour > 12:
        res_hour -=12

    week = ["Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay", "Sunday"]

    if day_of_week != "":
        current_day_index = week.index(day_of_week)
        added_days = days
    
        if added_days >=7:
            added_days = added_days % 7
        new_day_index = current_day_index + added_days  

        if new_day_index >= len(week):
            new_day_index = new_day_index % 7  
    
    new_time =""
    if day_of_week == "":
        new_time = str(res_hour) + ":" + f"{int(res_minute):02d}" + " " + res_med + whatday 
    else:
        new_time = str(res_hour) + ":" + f"{int(res_minute):02d}" + " " + res_med + ", " + week[new_day_index] + whatday

    # time_clc = list()
    # # time_clc.append( f"{int(start_minute) + int(du_minute):02d}" )
    # time_clc.append( int(start_minute) + int(du_minute) )
    # time_clc.append( int(start_hour) + int(du_hour) )
    # time_clc.append(start_med)

    # if(time_clc[0] > 60):
    #     time_clc[1] = time_clc[1] + 1
    #     time_clc[0] = time_clc[0] - 60


    # if(time_clc[1] > 12):
    #     time_clc[1] = time_clc[1] - 12
    #     time_clc[2] = 'AM' if time_clc[2] == 'PM' else time_clc[2]
        

    # print(start_hour, start_minute, start_med, du_hour, du_minute, time_clc)

    return new_time