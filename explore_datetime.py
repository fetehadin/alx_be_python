#ef display_current_datetime():

from datetime import timedelta, datetime

def display_current_datetime():
    current_date = datetime.now()
    return f"Current date and time:  {current_date.strftime('%Y-%m-%d %H:%M:%S')}"

def calculate_future_date():
    current_time = datetime.now()
    days = timedelta(int(input("Enter the number of days to add to the current date: ")))
    future_date = days + current_time    
    future_date = future_date
    return f"Future date: {future_date.strftime('%Y-%m-%d')}"

print(display_current_datetime())
print(calculate_future_date())


