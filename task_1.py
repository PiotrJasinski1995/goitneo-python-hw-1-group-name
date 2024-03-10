from datetime import datetime, timedelta
from collections import defaultdict


# Function for checking if day is on the weekend
def is_day_weekend(date):
    return True if date.weekday() == 5 or date.weekday() == 6 else False


# Function for calculating birthday celebrations on next weekend
def get_birthday_per_week(users):
    # List for dictionary keys, there is no need to put weekend days
    WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Offset for calculating start of the next weekd
    WEEK_MAX_OFFSET = 7

    # Dictionary with users
    users_dict = defaultdict(list)

    # Current date
    current_date = datetime.today().date()
    # current_date = datetime(2024, 12, 30).date()    # test for checking a date at the end of a year

    for user in users:
        name = user["name"]

        # Removing the time part
        celebration_day = user["birthday"].date()

        # Change celebbration date to actual year
        celebration_day = celebration_day.replace(year=current_date.year)

        # Calculate start of next week
        celebration_week_start_date = current_date + timedelta(days=WEEK_MAX_OFFSET - current_date.weekday())
        celebration_week_day_offset = (celebration_week_start_date - celebration_day).days

        # If celebration date is older than current, assign celebration for next year
        # Date year on weekends just before celebration date (in same year) cannot be incremented, because they are assigned to the next week
        if celebration_week_day_offset > 2:    
            celebration_day = celebration_day.replace(year=celebration_day.year + 1)
        
        celebration_day_offset = (celebration_day - celebration_week_start_date).days

        # If the day difference between celebration date and start of next week is more than 4 (4 == Friday), there is no point for further calculations
        if celebration_day_offset > 4:
            continue
        
        # If the day is on weekend, add proper offset to set it to next Monday
        if(is_day_weekend(celebration_day)):
            celebration_weekend_offset = WEEK_MAX_OFFSET - celebration_day.weekday()
            celebration_day = celebration_day + timedelta(days=celebration_weekend_offset)

        # At this point date should be within the next week, so there is no need for further conditions
        users_dict[WEEK_DAYS[celebration_day.weekday()]].append(name)
    
    # Print data
    if not users_dict:
        print('No celebration next week :(')
    else:
        print('Celebrations next week:\n')

        for day in WEEK_DAYS:
            if users_dict[day]:
                print(f'{day:<10}: {', '.join(users_dict[day])}')

    
############ TEST CALL ############
'''
users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 2),},
         {"name": "Bill a", "birthday": datetime(1955, 3, 3)},
         {"name": "Bill b", "birthday": datetime(1955, 3, 15)},
         {"name": "Bill c", "birthday": datetime(1955, 3, 16)},
         {"name": "Bill d", "birthday": datetime(1955, 3, 9)},
         {"name": "Bill e", "birthday": datetime(1955, 3, 10)},
         {"name": "Bill f", "birthday": datetime(1955, 3, 13)},
         {"name": "Bill f", "birthday": datetime(1955, 12, 30)}]

get_birthday_per_week(users)
'''
