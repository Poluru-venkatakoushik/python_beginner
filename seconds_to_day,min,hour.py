sec=int(input("Enter no.of seconds : "))
hour=min=day=0
if(sec>=60):
    min=sec//60
    sec-=(min*60)
if(min>=60):
    hour=min//60
    min-=(hour*60)
if(hour>=24):
    day=hour//24
    hour-=(day*24)
print("{0:>5}day(s){1:>5}hour(s){2:>5}minute(s){3:>5}second(s)".format(day,hour,min,sec))