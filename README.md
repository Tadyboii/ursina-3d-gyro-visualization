# Ursina 3D Gyroscope Visualization

## Overview
This project is a 3D gyroscope visualization tool built using the Ursina game engine. It receives quaternion data via serial communication from an external device such as an Arduino or ESP32 with an MPU6050 sensor. The received quaternion values (qw, qx, qy, qz) are used to determine the object's orientation in 3D space, allowing real-time visualization of sensor movement.

## Features
- **Real-time 3D orientation visualization**
- **Serial communication support** for receiving quaternion data
- **Basic lighting shader** for improved visualization

## Requirements
### Hardware:
- Arduino/ESP32 with MPU6050 sensor
- USB connection to the computer

### Software:
- Python 3.7+
- Required Python libraries:
  - Ursina
  - PySerial
  - Math

Install dependencies using:
```sh
pip install ursina pyserial
```

## Usage
### 1. Define Constants
Before running the script, update the `constants.py` file with the appropriate values:
```python
SERIAL_PORT = "COM3"  # Replace with the actual serial port
BAUD_RATE = 115200     # Ensure it matches the baud rate of your microcontroller
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
```

### 2. Run the Visualization
After setting the correct serial port and baud rate, execute the script:
```sh
python main.py
```

### 3. Viewing the Output
Once the program is running, the 3D cube in the Ursina window will rotate based on the received quaternion data from the MPU6050 sensor.

##Demo
![InAction](https://github.com/Tadyboii/ursina-3d-gyro-visualization/blob/main/gyro.gif)

## Notes
- Ensure that your Arduino/ESP32 is correctly sending quaternion values over the serial connection. The serial should output quaternion values with this format:
```
{qw} {qx} {qy} {qz}
```
For example:
```
0.999878 0.003845 -0.003296 -0.012573 
```

## Contributing
Contributions are welcome! If you'd like to improve this project, feel free to submit a pull request or open an issue on GitHub.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

