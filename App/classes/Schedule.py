import pandas as pd
from datetime import timedelta
from App.classes.Stations import splitStopIds

class Schedule:
    def __init__(self, date, line_id, full_schedule):
        self.date = date
        self.times = makeSchedule(full_schedule, line_id, date)

def makeSchedule(full_schedule, line_id, date):
    full_schedule = splitStopIds(full_schedule, 'stop_id') #don't do this here, unnecessary repetition
    line_schedule = full_schedule.groupby('line_id').get_group(line_id)
    line_schedule = scheduleTimeToDateTime(line_schedule, date)
    return line_schedule

def scheduleTimeToDateTime(schedule, date):
    arrival_times = schedule.arrival_time.tolist()
    
    arrival_hour = schedule.apply(lambda row: int(str(row['arrival_time'])[0:2]), axis=1)
    arrival_min = schedule.apply(lambda row: int(str(row['arrival_time'])[3:5]), axis=1)
    schedule.loc[:, 'arrival_hour'] = pd.Series(arrival_hour, index=schedule.index)
    schedule.loc[:, 'arrival_min'] = pd.Series(arrival_min, index=schedule.index)

    today = schedule[schedule['arrival_hour'] < 24]
    tomorrow = schedule[schedule['arrival_hour'] >= 24]

    dateTime_today = today.apply(lambda row: pd.to_datetime(date + ' ' + row['arrival_time']), axis=1)
    dateTime_tomorrow = tomorrow.apply(lambda row: pd.to_datetime(date + ' ' + hourMinusDay(row['arrival_hour']) + ':' + str(row['arrival_min']) + ':00') + timedelta(days=1), axis=1)
    today.loc[:, 'datetime'] = pd.Series(dateTime_today, index=today.index)
    tomorrow.loc[:, 'datetime'] = pd.Series(dateTime_tomorrow, index=tomorrow.index)
    
    schedule = pd.concat([today, tomorrow])
    return schedule

def hourMinusDay(hour):
    new_hour = int(hour) - 24
    return "{0:0=2d}".format(new_hour)
