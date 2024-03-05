from dateutil import relativedelta
import datetime



def date_str_to_obj(person):
    #write code that takes a date string and returns a datetime object.
    format_string = "%Y-%m-%d"
    birthday_dt_obj = datetime.datetime.strptime(person['birthday'], format_string)
    return birthday_dt_obj

def calculate_age(person):
    birthday_dt = date_str_to_obj(person)
    today = datetime.date.today()
    difference = relativedelta.relativedelta(today, birthday_dt)
    return difference

def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days and in chronological order
    # 90 is passed in as a parameter from menus.py
    # Template:
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    
    birthday_list = []

    #paramaters are passed into the sort_birthday_list() that first creates an object for each person and appends
    #to birthday_list. Using sort() on birthday_list to chronologically order each person object by their birthday.
    def sort_birthday_list(person, turning_age, difference, birthday):
        birthday_list.append({
                    'name': person['name'], 
                    'turning_age': turning_age, 
                    'difference': difference,
                    'birthday': birthday
                  })
        birthday_list.sort(key=lambda item:item['birthday'])

    #Looping through the people_list that was passed into upcoming_birthday() function and converting
    #each string in person to a datetime object.
    #converting each datetime object to the current year in "birthday_this_year" and also to next year in 
    #"birthday_next_year". The if elif statement below checks if the difference between "birthday_this_year"
    #and "birthday_next_year is within 90 days or not". If the birth date is within 90 days, each person's parameters 
    #are passed into the sort_birthday_list().
    for person in people_list:
        
        birthday_dt = date_str_to_obj(person)
        now = datetime.datetime(year=2023, month=11, day=1)
        birthday_this_year = birthday_dt.replace(year=now.year)
        birthday_next_year = birthday_dt.replace(year=now.year+1)

        difference_this_year = birthday_this_year - now
        difference_next_year = birthday_next_year - now

        turning_age = relativedelta.relativedelta(now, birthday_dt).years +1

        
        if 0 < ((difference_this_year).days) <= days: 
            sort_birthday_list(person, turning_age, difference_this_year.days, birthday_this_year)
        elif 0 < ((difference_next_year).days) <= days:
            sort_birthday_list(person, turning_age, difference_next_year.days, birthday_next_year)
    
    #loops through each person in birthday_list that has been chronologially ordered by birthday and within 90 days
    #to print out person's name, the age they are turning, how many days until their birthday, and the month and day of birthday.
    for person in birthday_list:
        print(f"{person['name']} turns {person['turning_age']} in {person['difference']} days on {person['birthday'].strftime("%B %d")}")

    
#output
# ======== UPCOMING BIRTHDAYS ========
# Nova turns 24 in 27 days on November 28
# Declan turns 30 in 59 days on December 30
# Jane turns 40 in 90 days on January 30
# ====================================    

    
def pluralizeWord(singularWord, pluralWord, count):
        return pluralWord if count > 1 else singularWord


def display_age(person):
    # TODO: write code to display the age of person
    # Template:
    # PERSON is X years, X months, and X days old
    
    
    
    difference = calculate_age(person)
    
    def pluralizeWord(singularWord, pluralWord, count):
        return pluralWord if count > 1 else singularWord
    
    
    print(f"{person['name']} is {difference.years} "
          f"{pluralizeWord("year","years",difference.years)}, " 
          f"{difference.months} {pluralizeWord("month","months",difference.months)}, "
          f"and {difference.days} {pluralizeWord("day","days",difference.days)} old.")
    


def display_age_difference(people):
    # TODO: write the code to display the age difference between people
    # Template:
    # PERSON is older
    # PERSON and PERSON's age difference is: X years, X months, and X days
    
    
    person0 = date_str_to_obj(people[0])
    person1 = date_str_to_obj(people[1])

    if person0 < person1:
        print(f"{people[0]['name']} is older")
        difference = relativedelta.relativedelta(person1 ,person0)

    elif person0 > person1:
        print(f"{people[1]['name']} is older")
        difference = relativedelta.relativedelta(person0, person1)
        
    print(f"{people[0]['name']} and {people[1]['name']} age difference is "
          f"{difference.years} {pluralizeWord("year","years",difference.years)}, " 
          f"{difference.months} {pluralizeWord("month","months",difference.months)}, " 
          f"and {difference.days} {pluralizeWord("day","days",difference.days)} old.")

    
