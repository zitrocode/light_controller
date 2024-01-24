import RPi.GPIO as GPIO

class LightController:
  def __init__(self, red, blue, green):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    self.red_pin = int(red)
    self.blue_pin = int(blue)
    self.green_pin = int(green)

    self.red_pwm, self.blue_pwm, self.green_pwm = None, None, None
    self.red_value, self.blue_value, self.green_value = 0, 0, 0

  def setup(self):
    self.setup_gpio()
    self.setup_pwm()

  def setup_gpio(self):
    GPIO.setup(self.red_pin, GPIO.OUT)
    GPIO.setup(self.blue_pin, GPIO.OUT)
    GPIO.setup(self.green_pin, GPIO.OUT)

  def setup_pwm(self):
    self.red_pwm = self.create_pwm_instance(self.red_pin)
    self.blue_pwm = self.create_pwm_instance(self.blue_pin)
    self.green_pwm = self.create_pwm_instance(self.green_pin)

  def create_pwm_instance(self, pin):
    pwm_instance = GPIO.PWM(pin, 100)
    pwm_instance.start(self.get_value_for_pin(pin))
    return pwm_instance

  def get_value_for_pin(self, pin):
    if pin == self.red_pin:
      return self.red_value
    elif pin == self.blue_pin:
      return self.blue_value
    elif pin == self.green_pin:
      return self.green_value

  def set_color(self, red_value, blue_value, green_value):
    self.red_value = self.convert_to_pwm_value(red_value)
    self.blue_value = self.convert_to_pwm_value(blue_value)
    self.green_value = self.convert_to_pwm_value(green_value)

    self.loop()

  def reverse_numbers(self, value):
    return 255 - value

  def convert_to_pwm_value(self, value):
    invested = self.reverse_numbers(value)
    return (invested / 255) * 100

  def off_light(self):
    self.red_pwm.stop()
    self.blue_pwm.stop()
    self.green_pwm.stop()

  def loop(self):
    self.red_pwm.ChangeDutyCycle(self.red_value)
    self.blue_pwm.ChangeDutyCycle(self.blue_value)
    self.green_pwm.ChangeDutyCycle(self.green_value)

  def stop(self):
    self.off_light()
    GPIO.cleanup()