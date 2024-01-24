import argparse
import json

from light import LightController

class Controller:
  def __init__(self):
    self.controller = LightController(40, 38, 37)
    self.controller.setup()

    self.red = 255
    self.blue = 255
    self.green = 255

    self.load_settings()

  def set_color(self, red, blue, green):
    print(f"Color set to: Red={red}, Green={green}, Blue={blue}")
    self.save_settings(red, blue, green)
    
    self.controller.set_color(red, blue, green)

  def turn_on(self):
    self.controller.set_color(self.red, self.blue, self.green)
    print("Lights turned on")

  def turn_off(self):
    self.controller.set_color(0, 0, 0)
    print("Lights turned off")

  def load_settings(self):
    try:
      with open('config.json', 'r') as config:
        settings = json.load(config)
      
      self.red = int(settings.get('red', 0))
      self.blue = int(settings.get('blue', 0))
      self.green = int(settings.get('green', 0))

      self.controller.set_color(self.red, self.blue, self.green)
      print(f"Loaded configuration: Red={self.red}, Green={self.green}, Blue={self.blue}")
    except FileNotFoundError:
      print("The configuration file does not exist. Default values will be used.")

  def save_settings(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

    settings = {'red': red, 'blue': blue, 'green': green}
    with open('config.json', 'w') as config:
      json.dump(settings, config, indent=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Color Controller App")
    parser.add_argument("--set-color", nargs=3, type=int, metavar=("red", "green", "blue"),
                        help="Set the color of the lights")
    parser.add_argument("--on", action="store_true", help="Turn on the lights")
    parser.add_argument("--off", action="store_true", help="Turn off the lights")

    args = parser.parse_args()

    app = Controller()

    if args.set_color:
        app.set_color(*args.set_color)
    elif args.on:
        app.turn_on()
    elif args.off:
        app.turn_off()
    else:
        print("No valid command provided. Use --set-color, --on, or --off.")