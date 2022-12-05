import serial

# This is for setting up serial connection between mcu connected via usb port and your python app
#COM Entered here should be the value of your com port, so needs to be selected accordingly
ser = serial.Serial('COM11', 9600)
while(1):
    # Read the incoming serial byte data from the Arduino
    data = ser.readline()

    # Convert the data from Serialzed Bytes to string type (removes b at the beginning symbolizing serial byte data)
    values=data.decode()
    
    #removes \r\n at the end
    values=values.strip()
    print(values)
