# Icy Pi

<a href='https://louwjlabuschagne.github.io/icypi/'><img src='./assets/mascot.jpg' width='100%'></a>

## Introduction
We are busy building an IoT solution that will monitor the temperature of freezers and send an alarm if the temperature of any one freezer goes below a given threshold.

To achieve this we use Icy Pi which is a Python package that aims to bring together 4 things, viz:
+ Being able to get readings from a `Sensor`. Consider <a href='https://www.adafruit.com/product/1782'>this</a> sensor that uses the <a href='https://i2c.info/'>I2C</a> protocol.
+ Being able to write the readings to Google Sheets
+ Being able to alarm to Gmail if a reading is below the set threshold
+ Being able to create a IcyPi client that can be kicked off by a cron job to do everything.

## Classes

### Sensor

```python
sensor = Sensor(config)
sensor.get_temp()
```

### GSpread   

```python
gspread = GSPread(config)
gspread.write_raw_log(code, message, value)
```

### Gmail   

```python
gmail = Gmail(config)
gmail.send_mail(to, msg)
```

### IcyPi   

```python
icypi = IcyPi(config)
icypi.check_all_freezers()
icypi.update_all_freezers()
```