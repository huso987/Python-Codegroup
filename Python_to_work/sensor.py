def sensor_data_fusion(sensor1_data, sensor2_data):
    averaged_data = {
        'temperature': (sensor1_data['temperature'] + sensor2_data['temperature']) / 2,
        'humidity': (sensor1_data['humidity'] + sensor2_data['humidity']) / 2
    }
    averaged_data_out = "Temperature: " + str(averaged_data['temperature']) + "  Humidity: "+str(averaged_data['humidity'])
    return averaged_data_out


sensor1 = {'temperature': 22.5, 'humidity': 45.0}
sensor2 = {'temperature': 23.5, 'humidity': 50.0}

result = sensor_data_fusion(sensor1, sensor2)
print(result)  
