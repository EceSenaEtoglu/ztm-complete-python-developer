import datetime

time1 = datetime.time(3,59,2)  # Create time obj
print(time1)
print(f"Hour: {time1.hour}")

# ---date---
print(datetime.date(2020,1,2))     # Create date obj

curr_date = datetime.date.today()  # Get current date
print(f"Year : {curr_date.year}")
print(f"Month : {curr_date.month}")
print(f"Day : {curr_date.day}")

# ---datetime---
datetime_obj = datetime.datetime(2020,8,11,2,1,3)  # Combines date and time objects
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())

print(datetime.datetime.now())  # Get current date and time


# ---timedelta---
curr_date = datetime.date.today()
diff = curr_date - datetime.date(curr_date.year+1,curr_date.month,curr_date.day)
print(diff)

# ---strftime---
date_str = datetime.date(2020,12,11).strftime("%A,%B %d, %Y")   # Monday, August 21, 2023
print(date_str)

# ---strptime---
datetime_obj = datetime.datetime.strptime("2020 June","%Y %B")
print(datetime_obj.month)