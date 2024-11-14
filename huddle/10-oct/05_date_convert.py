date = input("Enter date as DD-MM-YYYY: ")

split = date.split('-')

day = split[0]
month = split[1]
year = split[2]

print(year, month, day)