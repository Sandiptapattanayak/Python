#return value with no argument

def get_current_year():
    import datetime
    current_year = datetime.datetime.now().year
    return current_year


year = get_current_year()
print("The current year is:", year)
