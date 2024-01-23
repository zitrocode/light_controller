# Light Controller for Raspberry Pi

This project is an RGB light controller designed to work with an RGB LED strip and a Raspberry Pi. You can customize and control the colors of the LED strip by adjusting the red, green, and blue values through the GPIO pins of the Raspberry Pi.

**⚠ Important:** Only with Raspberry PI support

### 👷‍♂️ Requirements

- Raspberry Pi
- RGB LED strip
- Wiring connections
- Python 3.x installed on the Raspberry Pi

### ⚙ Pin Configuration

- Pin 40: Red
- Pin 37: Green
- Pin 38: Blue

Make sure to connect the LED strip correctly to the corresponding pins on the Raspberry Pi.

### 📦 Installation

1. Clone this repository on your Raspberry Pi:

```bash
git clone http://github.com/zitrocode/light_controller
```

2. Navigate to the project directory:

```bash
cd light_controller
```

### 🚀 Usage

1. Run the main script:

```bash
python ./main.py
```

**Note:** Ensure you have Tkinter installed on your Raspberry Pi to run the graphical interface.

### 🤝 Contributions

Contributions are welcome! If you encounter any issues or have improvements, please create an issue or a pull request.

### 📝 License

This project is licensed under the [MIT License](./LICENSE)
