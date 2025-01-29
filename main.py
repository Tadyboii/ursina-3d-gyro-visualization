from ursina import *
from ursina.shaders import basic_lighting_shader
from math import atan2, asin, degrees
from constants import *
import serial

app = Ursina()
window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window.color = color.black
window.borderless = False
window.fullscreen = False
window.fps_counter.enabled = False
window.collider_counter.enabled = False
window.entity_counter.enabled = False

cube = Entity(model='cube', color=color.gray, scale=(2, 2, 2), shader=basic_lighting_shader)
left_eye = Entity(model='circle', color=color.black66, scale=(0.2, 0.2, 0.2), position=(0.25, 0.25, 0.52), parent=cube,
                  double_sided=True)
right_eye = Entity(model='circle', color=color.black66, scale=(0.2, 0.2, 0.2), position=(-0.25, 0.25, 0.52),
                   parent=cube, double_sided=True)

serial_read = serial.Serial(SERIAL_PORT, BAUD_RATE)

def update():
    line = serial_read.readline().decode().strip()
    data = line.split()
    if len(data) >= 4:
        qw = float(data[0])
        qx = float(data[1])
        qy = float(data[2])
        qz = float(data[3])
        yaw = -atan2(2.0 * (qw * qz + qx * qy), 1.0 - 2.0 * (qy * qy + qz * qz))
        pitch = asin(2.0 * (qw * qy - qz * qx))
        roll = atan2(2.0 * (qw * qx + qy * qz), 1.0 - 2.0 * (qx * qx + qy * qy))
        cube.rotation = Vec3(degrees(pitch), degrees(yaw), degrees(roll))
        print(f"qw: {qw} qx: {qx} qy: {qy} qz: {qz}")
app.run()
