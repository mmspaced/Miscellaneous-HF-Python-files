# from datetime import datetime - alternative import but can cause
# ambiguity when two different modules have a function of the same name

import datetime, time, random

odd_minutes = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(5):
    right_this_minute = datetime.datetime.today().minute

    if right_this_minute in odd_minutes:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
        
    wait_time=random.randint(1, 60)
    time.sleep(wait_time)

