import tkinter as tk
import math
from PIL import ImageTk, Image

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    # Call your functions here, such as draw_sky, draw_ground,
    draw_sky(canvas, 0, 0, 799, 250)
    draw_ground(canvas, 0, 250, 799, 599)
    draw_sun(canvas, 110, 30)
    draw_cloud(canvas, 150, 50, 300, 100, 250, 40, 350, 80, 250, 50, 450, 100)
    draw_road(canvas, 0, 280, 799, 420)
    draw_game(canvas, 100, 300, 160, 400, 160, 320, 210, 380, 210, 300, 270, 400, 270, 320, 350, 380)
    draw_game_lines(canvas, 100, 350, 160, 350, 210, 350, 270, 350, 310, 320, 310, 380)
    label_game(canvas, 330, 350, 290, 350, 240, 320, 240, 370, 180, 340, 140, 330, 140, 380)
    add_image(canvas)
    draw_house(canvas, 500, 150, 700, 250, 600, 30, 500, 150, 700, 150)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, x_1, y_1, x_2, y_2):
    canvas.create_rectangle(x_1, y_1, x_2, y_2, fill="#ccebff", width=0)

def draw_ground(canvas, x_1, y_1, x_2, y_2):
    canvas.create_rectangle(x_1, y_1, x_2, y_2, fill="#99ff66", width=0)

def draw_cloud(canvas, oval1_x1, oval1_y1, oval1_x2, oval1_y2, oval2_x1, oval2_y1, oval2_x2, oval2_y2, oval3_x1, oval3_y1, oval3_x2, oval3_y2):
    canvas.create_oval(oval1_x1, oval1_y1, oval1_x2, oval1_y2, fill="white", width=0)
    canvas.create_oval(oval2_x1, oval2_y1, oval2_x2, oval2_y2, fill="white", width=0)
    canvas.create_oval(oval3_x1, oval3_y1, oval3_x2, oval3_y2, fill="white", width=0)

def draw_sun(canvas, sun_left, sun_top):
    sun_width = 90
    sun_height = 70
    ray_length = 100
    ray_width = 3
    ray_count = 10

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height

    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="yellow", width=0)

    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i 
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill="yellow")

def draw_road(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#808080", width=0)

def draw_game(canvas, first_x1, first_y1, first_x2, first_y2, second_x1, second_y1, second_x2, second_y2, third_x1, third_y1, third_x2, third_y2, fourth_x1, fourth_y1, fourth_x2, fourth_y2):
    canvas.create_rectangle(first_x1, first_y1, first_x2, first_y2)
    canvas.create_rectangle(second_x1, second_y1, second_x2, second_y2)
    canvas.create_rectangle(third_x1, third_y1, third_x2, third_y2)
    canvas.create_rectangle(fourth_x1, fourth_y1, fourth_x2, fourth_y2)

def draw_game_lines(canvas, x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4):
    canvas.create_line(x1, x2, x3, x4)
    canvas.create_line(y1, y2, y3, y4)
    canvas.create_line(z1, z2, z3, z4)

def label_game(canvas, x1, x2, y1, y2, z1, z2, a1, a2, b1, b2, c1, c2, d1, d2):
    canvas.create_text(x1, x2, text="1")
    canvas.create_text(y1, y2, text="2")
    canvas.create_text(z1, z2, text="3")
    canvas.create_text(a1, a2, text="4")
    canvas.create_text(b1, b2, text="5")
    canvas.create_text(c1, c2, text="6")
    canvas.create_text(d1, d2, text="7")

def add_image(canvas):
    photo = Image.open('image.gif')
    canvas.image = ImageTk.PhotoImage(photo)
    canvas.create_image(100, 200, image = canvas.image)

def draw_house(canvas, x1, x2, x3, x4, y1, y2, y3, y4, y5, y6):
    canvas.create_rectangle(x1, x2, x3, x4, fill="#264d73", width=0)
    canvas.create_polygon(y1, y2, y3, y4, y5, y6, fill="#4dff4d", width=0)


# Call the main function so that
# this program will start executing.
main()