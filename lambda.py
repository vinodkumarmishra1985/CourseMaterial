#dict inside the list
people =[
    {"name": "abc", "house":"NC"},
    {"name": "xyz", "house":"AZ"},
    {"name": "lmn", "house":"NJ"}
    ]

def f(person):
    return person["house"]

#people.sort(key=f)
people.sort(key=lambda person:person["name"]

print (people)
