
def getGrade(perc):
    if perc < 35:
        grade ="Fail"
    elif perc >= 35 and perc <= 50:
        grade = "Third div"
    elif perc >50 and perc<65:
        grade = 'Second div'
    else:
        grade = "First div"
    return grade
perc = input("Enter the percetage :")
print("Your garde is : ",getGrade(int(perc)))

def getCountry(city):
    if city == 'Delhi':
        country = 'India'
    elif city == 'London':
        country = 'United Kingdom'
    elif city == 'NewYork':
        country = "United States"
    else:
        country = 'Not Avavilable'
    return country
city = input("enter city name :")
print("your country is : ", getCountry(str(city)))

def findCommonElement(set1, set2):
    set3 = set1 & set2
    return set3
set1 = {1,2,3,4,5}
set2 = {1,4,5,8,9}
print(findCommonElement(set1,set2))


def convertStringToList(s):
    return list(s)
s = input("Enter a string : ")
print(convertStringToList(s))

