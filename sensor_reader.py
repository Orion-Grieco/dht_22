import serial

arduino_port = ""
baud = 9600
fileName ="DHT22_data.csv"
samples = 10

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created File")

line = 0

while line <= samples:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print(float("NaN"))
