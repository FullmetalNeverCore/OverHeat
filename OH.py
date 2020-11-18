import wmi


def overheat():
    txtfile = open("tempe.txt", "w", encoding='utf-8')
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType==u'Temperature':
            print(sensor.Name)
            print(sensor.Value)
            text = txtfile.write(str(sensor.Value))

