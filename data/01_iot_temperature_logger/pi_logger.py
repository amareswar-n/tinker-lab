import serial,csv
from datetime import datetime
ser=serial.Serial('/dev/ttyUSB0',9600)
with open('log.csv','a',newline='') as f:
  writer=csv.writer(f)
  while True:
    line=ser.readline().decode().strip()
    if "," in line:
      t,h=line.split(",")
      writer.writerow([datetime.now(),t,h])