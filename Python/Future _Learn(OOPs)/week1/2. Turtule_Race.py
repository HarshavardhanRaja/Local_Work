# writing a program using objects, using Python’s turtle module to create a turtle race.


# step-1: 
# You need to ask Python to import the Turtle class, which is like a blueprint for making a turtle. 
# class names usually start with a capital so that they are easily distinguishable from variable names. (ex: Turtle)
from turtle import Turtle


# step-2:
# Create an instance of a Turtle object. 
tony = Turtle()



# step-4:
# Tell your Turtle object what it should look like. 
# Inside the object are attributes, which are pieces of data we can define. 
# The Turtle object has attributes for colour and shape.
# you can use the color and shape methods to customise those attributes.
tony.color('red')
tony.shape('turtle')




# step-5:
# instruct the turtle to stop drawing with penup(), 
# then to move to a location with goto(), 
# and finally to get ready to draw a line with pendown().
tony.penup()
tony.goto(-160, 100)
tony.pendown()



# step-6:
# Create three more instances of a Turtle object, each with a different name.
steve = Turtle()
nat = Turtle()
banner = Turtle()

# step-7:
#Tell one new turtle to goto(-160, 70), 
# one to goto(-160, 40), 
# one to goto(-160, 10).

steve.penup()
steve.goto(-160, 70)
steve.pendown()

nat.penup()
nat.goto(-160, 40)
nat.pendown()

banner.penup()
banner.goto(-160, 10)
banner.pendown()


# step-8:
# You now need to make the Turtle objects race. 
# Each turtle will move forward by a random number of pixels.
from random import randint

for movement in range(100):
    tony.forward(randint(1,5))
    nat.forward(randint(1,5))
    steve.forward(randint(1,5))
    banner.forward(randint(1,5))





