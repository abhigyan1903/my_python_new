#program to find the fare of the bus using inheritance
class vehicle:
      def __init__(self, name, mileage, max_capacity):
           self.name=name
           self.mileage=mileage
           self.max_capacity=max_capacity

      def bus_fare(self):
         return self.max_capacity*100
class Bus(vehicle):

      def fare(self):
        amount = super().bus_fare()
        amount = amount+amount * 10 / 100
        return amount

bus_1 = Bus("tata", 32, 45)
print("cost of fare:", bus_1.bus_fare())