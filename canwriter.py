from canard import can
from canard.hw import socketcan

dev = socketcan.SocketCanDev('vcan0')

frame = can.Frame(id=0x100)
frame.dlc = 8
frame.data=[1,2,3,4,5,6,7,8]

while True:
    dev.send(frame)
    
