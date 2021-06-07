


# Key:Value pairs
# in other languages also called as hash maps

Avenger = {'name':'Tony', 'Age':35, 'powers': ['Flight', 'Speed', 'Armor'], 'alias':'Ironman'}
print(Avenger)
print(Avenger['name'])
print(Avenger['Age'])
print(Avenger['powers'])


print(Avenger.get('name'))
print(Avenger.get('mobile'))


# update/add single key value pair
Avenger['mobile'] = 7542573052759
Avenger['Age'] = 29
print(Avenger)


# update/add multiple key value pair

Avenger.update({'name':'Thor', 'Age':2000, 'powers':['Lighting', 'Mijolner', 'god'], 'native': 'Asgard'})
print(Avenger)
del Avenger['alias']
mob = Avenger.pop('mobile')
print(Avenger)



# lenght, loop through keys
print(len(Avenger))
print(Avenger.keys())
print(Avenger.values())
print(Avenger.items())


for key in Avenger:
    print(key)

for key,value in Avenger.items():
    print(key,value)