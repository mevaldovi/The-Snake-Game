import tkinter as tk  # providing classes for defining later
from PIL import Image, ImageTk
MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
GAME_SPEED = 1000  # MOVES PER SECOND


class Snake(tk.Canvas):  # creating Canvas widgets to display text, lines, & graphics
    def __init__(self):  # constructing a parent widget
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)
        self.load_assets()
        self.create_objects()
        self.score = 0

        def load_assets(self):
            # define our method to allow the app to load images
            try:
                self.snake_body_image = Image.open("./assets/snake.png")
                self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
                self.food_image = Image.open("./assets/food.png")
                self.food_image = ImageTk.PhotoImage(self.food_image)
            except IOError as error:
                print(error)  # js eqivalent of console.log(err)
                root.destroy()  # close window and stop application


def create_objects(self):
    self.create_text(
        45, 12, text="Score" {self.score}, tag="score", fill="#fff", font=("TkDefaultFont", 14)
    )
    for x_position, y_position in self.snake_positions:
        self.create_image(x_position, y_position,
                          image=self.snake_body, tag="snake")
        self.create_image(
            self.food_position[0], self.food_position[1], image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 693, outline="#525d69")

        def move_snake(
            self): head_x_position, head_y_position = self.snake_positions[0]
        new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        # reposition all elements of snake-body except last one

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

            def perform_actions(self):  # equivalent to setTimeout method in JS
                if self.check_collisions():
                    return

                self.move_snake()
                self.after(GAME_SPEED, self.perform_actions)

            def check_collisions(self):
                head_x_position, head_y_position = self.snake_position[0]

                return (
                    head_x_position in (0, 600)
                    or head_y_position in (20, 620)
                    or head_x_position, head_y_position in self.snake_positions[1:]
                )


# some-code-here
root = tk.Tk()
root.title("Snake")
root.resizable(False, False)  # tells window manager whether this is resizeable

board = Snake()
board.pack()  # organiz widgets in blocks before placing them in the parent widge

root.mainloop()  # calling the mainloop of tk
