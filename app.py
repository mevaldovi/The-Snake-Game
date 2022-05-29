import tkinter as tk # providing classes for defining later
from PIL import Image, ImageTk

class Snake(tk.Canvas): # creating Canvas widgets to display text, lines, & graphics
    def __init__(self): # constructing a parent widget
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)

        self.load_assets()
        self.create_objects()

        def load_assets(self):
            # define our method to allow the app to load images
            try:
                self.snake_body_image = Image.open("./assets/snake.png")
                self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

                self.food_image = Image.open("./assets/food.png")
                self.food_image = ImageTk.PhotoImage(self.food_image)
            except IOError as error:
                    print(error) # js eqivalent of console.log(err)
                    # root.destroy() # close window and stop application

def create_objects(self):
    for x_position, y_position in self.snake_positions:
        self.create_image(x_position, y_position, image=self.snake_body, tag="snake")



# some-code-here
root = tk.Tk()
root.title("Snake")
root.resizable(False, False) #  tells window manager whether this is resizeable

board = Snake()
board.pack() # organiz widgets in blocks before placing them in the parent widge

root.mainloop() #calling the mainloop of tk

# wont let me install pillow what is going on??
