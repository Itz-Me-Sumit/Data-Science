# Concept: Diamond Problem + MRO(Method Resolution Order) + super()

class Device:
    def start(self):
        print("Device Starting")


class CameraDevice(Device):
    def start(self):
        print("Camera Ready")
        super().start()   # next class in MRO


class PhoneDevice(Device):
    def start(self):
        print("Phone Ready")
        super().start()   # next class in MRO


class SmartPhone(CameraDevice, PhoneDevice):
    def start(self):
        print("Smartphone Booting")
        super().start()   # MRO follow karega


sp = SmartPhone()
sp.start()

print("\nMRO Order:")
print(SmartPhone.mro())