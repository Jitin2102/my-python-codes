##    DICTIONARY IN THE THE LIST 
person_1={
    'name':'Arjit Singh',
    'age':19,
    'city':'lucknow',
}
person_2={
    'name':'Kartikeya Singh',
    'age':20,
    'city':'mathura',
}
person_3={
    'name':'Arsh',
    'age':18.5,
    'city':'saharanpur'
}
people=[person_1,person_2,person_3]
for person in people:
    print(f"Name:{person['name']}")
    print(f"Age:{person['age']}")
    print(f"City:{person['city'].title()}")
    print()
    