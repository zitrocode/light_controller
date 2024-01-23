import RPi.GPIO as GPIO

# red: 40, blue: 38, green: 37

class LightController:
    def __init__(self, red, blue, green):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.red_value = 0
        self.blue_value = 0
        self.green_value = 0

        self.red_pin = int(red)
        self.blue_pin = int(blue)
        self.green_pin = int(green)

    def setup(self):
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)

        self.red_pwm = GPIO.PWM(self.red_pin, 100)
        self.blue_pwm = GPIO.PWM(self.blue_pin, 100)
        self.green_pwm = GPIO.PWM(self.green_pin, 100)

        self.red_pwm.start(self.red_value)
        self.blue_pwm.start(self.blue_value)
        self.green_pwm.start(self.green_value)


    def set_color(self, red, blue, green):
        self.red_value = self.changeNumber(255 - red)
        self.blue_value = self.changeNumber(255 - blue)
        self.green_value = self.changeNumber(255 - green)

        self.loop()

    def changeNumber(self, value):
        return (value / 255) * 100

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

