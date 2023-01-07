# import colorgram
#
# colours = colorgram.extract('image.jpg', 10)
#
# rgb_list = []
#
# for item in colours:
#     colour_tuple = (item.rgb.r, item.rgb.g, item.rgb.b)
#     rgb_list.append(colour_tuple)
#
# print(rgb_list)
import random
import turtle
import colormap

colour_list = [(236, 236, 242), (240, 229, 236), (241, 231, 220), (224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61)]

turtle.speed("fastest")
turtle.hideturtle()

def draw_circle():
    rgb_colour = random.choice(colour_list)
    hex_colour = colormap.rgb2hex(rgb_colour[0], rgb_colour[1], rgb_colour[2])
    turtle.color(hex_colour, hex_colour)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


def draw_circleline():
    for x in range(0, 5):
        turtle.pendown()
        draw_circle()
        turtle.penup()
        turtle.forward(50)
    turtle.backward(250)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)


for x in range(0, 5):
    draw_circleline()

turtle.exitonclick()

