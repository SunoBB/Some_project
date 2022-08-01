import turtle
wn = turtle.Screen()          
wn.bgcolor("red")             
screen_width = 750;           
screen_height = 500;          
star_length = 200;            
 
wn.setup(width = screen_width, height = screen_height)
wn.title("Flag of Vietnam")
 
vin = turtle.Turtle()
vin.color("red")                # Set the color of the turtle to red
# Move the turtle to a predefined coordinate
vin.setx((screen_width - star_length)/2 - screen_width/2)
vin.sety(star_length/4)
vin.color("yellow")
vin.shape("blank")             
vin.pensize(3)                 
 
# Draw the flag
for counter in range(5):
    vin.forward(star_length)                 
    vin.right(144)
