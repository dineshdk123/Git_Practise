def leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year}this is leap year")
    else:
        print(f"{year} this is not leap year")
leap_year(2100)


