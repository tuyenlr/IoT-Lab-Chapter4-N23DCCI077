from sense_emu import SenseHat
import time

sense = SenseHat()

try:
   while True:
      temp = sense.get_temperature()
      hum = sense.get_humidity()
      press = sense.get_pressure()
      print(f'Temp: {temp:.1f} do C | Humidity: {hum:.1f}% | Pressure: {press>
      time.sleep(1)
except KeyboardInterrrupt:
     sense.clear()
     print('Dung doc cam bien.')
