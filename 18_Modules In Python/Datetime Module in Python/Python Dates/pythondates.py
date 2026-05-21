import datetime
x=datetime.datetime.now()
month=x.strftime("%b")
print("Month in short form:",month)

print("-----")

month_full=x.strftime("%B")
print("Month in full form:",month_full)

print("-----")
month_num=x.strftime("%m")
print("Month in number form:",month_num)

print("-----")

year=x.strftime("%y")
print("Year in short form:",year)

print("-----")

year_full=x.strftime("%Y")
print("Year in full form:",year_full)

print("-----")
hour=x.strftime("%H")
print("Hour in 24-hour format:",hour)

print("-----")

hour_12=x.strftime("%I")
print("Hour in 12-hour format:",hour_12)

print("-----")

am_pm=x.strftime("%p")
print("AM/PM:",am_pm)

print("-----")

minute=x.strftime("%M")
print("Minute:",minute)

print("-----")

second=x.strftime("%S")
print("Second:",second)

print("-----")

microsecond=x.strftime("%f")
print("Microsecond:",microsecond)

print("-----")

day=x.strftime("%d")
print("Day of the month:",day)

print("-----")

weekday_short=x.strftime("%a")
print("Weekday in short form:",weekday_short)

print("-----")

weekday_full=x.strftime("%A")
print("Weekday in full form:",weekday_full)

print("-----")

day_of_year=x.strftime("%j")
print("Day of the year:",day_of_year)


print("-----")

week_number=x.strftime("%U")
print("Week number of the year:",week_number)

# print("-----")

# timezone=x.strftime("%Z")
# print("Timezone:",timezone)

print("-----")

date_time_combined=x.strftime("%c")
print("Combined date and time:",date_time_combined)

print("-----")

date_iso=x.strftime("%x")
print("Date in ISO format:",date_iso)

print("-----")
time_iso=x.strftime("%X")
print("Time in ISO format:",time_iso)




