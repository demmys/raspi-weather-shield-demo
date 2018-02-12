from flask import Flask, jsonify, render_template
from piweathershield import PiWeatherShield
import json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api')
def api():
  weatherShield = PiWeatherShield()
  htu21d = (weatherShield.htu21d.read_temperature(), weatherShield.htu21d.read_humidity())
  ms5637 = weatherShield.ms5637.read_temperature_and_pressure()
  tsys01 = weatherShield.tsys01.read_temperature()
  tsd305 = weatherShield.tsd305.read_temperature_and_object_temperature()
  return jsonify({
    'HTU21D': {
      'temperature': '%.1f' % htu21d[0],
      'humidity': '%.1f' % htu21d[1]
    },
    'MS5637': {
      'temperature': '%.1f' % ms5637[0],
      'pressure': '%.2f' % ms5637[1]
    },
    'TSYS01': {
      'temperature': '%.1f' % tsys01
    },
    'TSD305': {
      'temperature': '%.1f' % tsd305[0],
      'object_temperature': '%.1f' % tsd305[1]
    },
  })

if __name__ == '__main__':
  app.run()
