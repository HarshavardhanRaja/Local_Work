class Room():

    # Creating a constructor and defining attributes
    """
    You are now going to add a constructor to your class.
    This is a special method to tell Python how to create an object of this class, 
    and it is always called __init__ with a double underscore on each side of ‘init’.
    """

    def __init__(self, room_name): # Here, ‘init’ stands for ‘initialise’, as a constructor initalises (that is, creates) an object.
        """
        Now you are going to add attributes for your room to the constructor. 
        The room should have a name — for example, it might be a kitchen, a bathroom, or a cellar.
        You are also going to store a description of the room to provide some atmosphere 
        — the cellar could be dark and dusty, for instance.
        """


        """
        To fully understand how this works, 
        you need to know how the ‘self’ parameter works in the constructor. 
        The self parameter automatically receives a reference to the object invoking the method. 
        By using self, a method can invoke the object and access the attributes and methods of that object. 
        In the previous constructor method, 
        the parameter self automatically receives a reference to a new Room object 
        while the parameter name receives kitchen. The line below creates the attribute
        """
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None




    """
    So that you are able to interact with the room object, you need to create some getters and setters. 
    These are methods that get and set the values of the object’s attributes.
    """
    """
    For every method within a class, you first need to specify the self parameter — the object itself 
    — followed by any data to pass in, 
    just as you did with the constructor
    """
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    # Here is a method to set the description of the room:
    def set_description(self, room_description):
        self.description = room_description

    # Here is a method to get the description of the room:
    def get_description(self):
        return self.description

    def describe(self):
        print( self.description )
    
    def set_name(self, room_name):
        self.name = room_name 

    def get_name(self):
        return self.name

    # Add link_room method here
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms : " + repr(self.linked_rooms))

    
    # Add get_details method here
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    # Add move method here
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


