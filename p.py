import random
import time
from PIL import Image, ImageTk
import tkinter as tk

def display_dice(number, root):
    dice_images = [
        "dice1.png",
        "dice2.png",
        "dice3.png",
        "dice4.png",
        "dice5.png",
        "dice6.png",
    ]

    # Load the image corresponding to the dice face
    image_path = dice_images[number - 1]
    image = Image.open(image_path)

    # Convert Image to PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Display image in a Tkinter Label
    label = tk.Label(root, image=photo)
    label.photo = photo  # Reference to keep the image from being garbage collected
    label.pack()

    # Update the Tkinter window
    root.update_idletasks()

    # Pause for 1 second before displaying the next die
    time.sleep(1)

    # Destroy the label to remove the image
    label.destroy()

def roll_dice():
    num_dice = random.randint(1, 6)  # Choose a random number of dice (1 to 6)
    print(f"Rolling dice...")

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Rolling Dice")

    # Generate a single random number for all dice
    result = random.randint(1, 6)
    print("The number is:", result)

    for _ in range(num_dice):
        display_dice(result, root)

    # Close the Tkinter window after all dice are displayed
    root.destroy()

if __name__ == "__main__":
    roll_dice()
