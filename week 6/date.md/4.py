from datetime import datetime, time
def datefunc(dt2, dt1):
    timedelta=dt2-dt1
    return timedelta.days*24*3600+timedelta.seconds
dt1=datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
dt2=datetime.now()
print(datefunc(dt2, dt1))