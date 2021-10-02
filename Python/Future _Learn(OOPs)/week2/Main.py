from Room import Room
from character import Enemy

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
# kitchen.describe() # This is how you call the description of the room

dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dining_hall.get_details()

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

current_room = kitchen          

while True:		
    print("\n")         
    current_room.get_details()   

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
      
    command = input("> ")    
    current_room = current_room.move(command)  