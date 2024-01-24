import tkinter as tk
from tkinter import ttk
from light import LightController
import json

class ColorControllerApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Light Controller")

    self.controller = LightController(40, 38, 37)
    self.controller.setup()

    # Initialize color variables
    self.red_var = tk.DoubleVar()
    self.green_var = tk.DoubleVar()
    self.blue_var = tk.DoubleVar()

    # Initialize configuration before turning off the lights
    self.last_config_before_off = {}

    # Set up the graphical interface
    self.setup_gui()

    # Load configuration on startup
    self.load_settings()

    # Restaura la configuración al cerrar la aplicación
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)

  def setup_gui(self):
    # Create the frame to contain everything
    main_frame = ttk.Frame(self.root)
    main_frame.pack(padx=10, pady=10)

    # Create the rectangle occupying the first column
    self.color_rectangle = tk.Label(main_frame, width=40, height=20, bg="#000000")
    self.color_rectangle.grid(row=0, column=0, padx=10, pady=10, rowspan=4)

    # Create sliders and labels in the second column
    sliders_frame = ttk.Frame(main_frame)
    sliders_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=4)
    self.sliders_frame = sliders_frame

    self.create_slider("Red", self.red_var, sliders_frame, row=0)
    self.create_slider("Green", self.green_var, sliders_frame, row=1)
    self.create_slider("Blue", self.blue_var, sliders_frame, row=2)

    # Label to display current slider values
    self.values_label = ttk.Label(sliders_frame, text="Slider Values")
    self.values_label.grid(row=3, column=0, columnspan=2, pady=5)

    # Button to turn lights off or on
    self.off_button = ttk.Button(sliders_frame, text="Turn Off", command=self.toggle_lights)
    self.off_button.grid(row=4, column=0, columnspan=2, pady=10)

  def create_slider(self, label_text, variable, parent_frame, row):
    label = ttk.Label(parent_frame, text=label_text)
    label.grid(column=0, row=row, pady=5)

    slider = ttk.Scale(parent_frame, from_=0, to=255, orient="horizontal", variable=variable, command=self.update_color)
    slider.grid(column=1, row=row, pady=5)

  def update_color(self, *args):
    # Get current slider values
    red = int(self.red_var.get())
    green = int(self.green_var.get())
    blue = int(self.blue_var.get())

    # Change color leds
    self.controller.set_color(red,blue,green)

    # Convert values from 0-255 to hexadecimal format and form the color
    color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    # Update the color of the rectangle
    self.color_rectangle.config(bg=color)

    # Update the label with current values
    self.values_label.config(text=f"Red: {red}   Green: {green}   Blue: {blue}")

    # Save the configuration to the file
    self.save_settings()

  def toggle_lights(self):
    if self.off_button["text"] == "Turn Off":
      # Save configuration before turning off the lights
      self.last_config_before_off = {
        "red": int(self.red_var.get()),
        "green": int(self.green_var.get()),
        "blue": int(self.blue_var.get())
      }

      # Turn off the lights (set sliders to 0)
      self.red_var.set(0)
      self.green_var.set(0)
      self.blue_var.set(0)

      # Change button text to "Turn On"
      self.off_button["text"] = "Turn On"

      # Disable sliders when lights are off
      self.set_sliders_state('disabled')

      # Update the color of the rectangle to black
      self.color_rectangle.config(bg="#000000")
      self.controller.set_color(0,0,0)
    else:
      # Restore the last configuration before turning off the lights
      if self.last_config_before_off:
        self.red_var.set(self.last_config_before_off["red"])
        self.green_var.set(self.last_config_before_off["green"])
        self.blue_var.set(self.last_config_before_off["blue"])

      # Change button text to "Turn Off"
      self.off_button["text"] = "Turn Off"

      # Enable sliders when lights are on
      self.set_sliders_state('normal')

      # Update the graphical interface and save the configuration
      self.update_color()

  def set_sliders_state(self, state):
      # Set the state of sliders and labels in sliders_frame
      for child in self.sliders_frame.winfo_children():
        if isinstance(child, ttk.Scale):
          child.configure(state=state)

  def load_settings(self):
    try:
      # Try to load configuration from the file
      with open("config.json", "r") as file:
        settings = json.load(file)

      # Apply the configuration to the sliders
      self.red_var.set(settings["red"])
      self.green_var.set(settings["green"])
      self.blue_var.set(settings["blue"])

      # Update the graphical interface
      self.update_color()

    except FileNotFoundError:
      print("The configuration file does not exist. Default values will be used.")

  def save_settings(self):
    # Save the configuration to the file
    settings = {
      "red": int(self.red_var.get()),
      "green": int(self.green_var.get()),
      "blue": int(self.blue_var.get())
    }

    with open("config.json", "w") as file:
      json.dump(settings, file, indent=4)

  def on_close(self):
    # Método que se llama al cerrar la aplicación
    print("Goodbye")
    self.controller.stop()
    self.root.destroy()

if __name__ == "__main__":
  try:
    root = tk.Tk()
    app = ColorControllerApp(root)
    root.mainloop()
  except KeyboardInterrupt:
    print('Close app')
