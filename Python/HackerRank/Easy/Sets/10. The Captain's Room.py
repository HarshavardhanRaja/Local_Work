# https://www.hackerrank.com/challenges/py-the-captains-room/problem


# Concepts
"""
"""

# Tried this but time limit exceded.
"""
k = int(input())
room_list = list(map(int, input().split()))
unique_rooms = set(room_list)

for room in unique_rooms:
    if room_list.count(room) == 1:
        print(room)
        break
"""


# Tried this it worked but not efficient
k = int(input())
room_list = list(map(int, input().split()))
rooms = {}
for item in room_list:
    if item in rooms.keys():
        rooms[item] +=1
    else:
        rooms[item] = 1
        
for keys, values in rooms.items():
    if values == 1:
        print(keys)



# Efficient
"""
K = int(raw_input())

#Step 1
roomList = map(int,raw_input().split(' '))

#Step 2
roomSet = set(roomList) 

#Step 3
sumRoomSet = sum(roomSet) 
sumRoomList = sum(roomList) 

# Step 4
temp = sumRoomSet * K - sumRoomList 

# Step 5
answer = temp / (K - 1) 

# Step 6
print answer

"""
