import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

# Adding 5 days
future = now + datetime.timedelta(days=5)
print("Date after 5 days:", future.date())
