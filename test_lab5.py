import unittest
from Lab5 import ElectricalAppliance, Kettle, Laptop, TV, WashingMachine, Apartment, Fridge

class TestApartment(unittest.TestCase):

    def setUp(self):
        self.flat = Apartment()

        self.kettle = Kettle("Kettle", 2000, 0.3, 1.7)
        self.tv = TV("TV", 120, 0.8, 55)
        self.laptop = Laptop("Laptop", 65, 0.5, 16)
        self.washer = WashingMachine("Washer", 500, 0.7, 7)
        self.fridge = Fridge("Fridge", 300, 0.2, 220)

        self.flat.add_device(self.kettle)
        self.flat.add_device(self.tv)
        self.flat.add_device(self.laptop)
        self.flat.add_device(self.washer)
        self.flat.add_device(self.fridge)

    def test_add_device(self):
        self.assertEqual(len(self.flat.devices), 5)

    def test_add_invalid_device(self):
        with self.assertRaises(TypeError):
            self.flat.add_device("Not a device")

    def test_plug_device(self):
        self.flat.plug_device("Kettle")
        self.assertTrue(self.kettle.is_plugged)

    def test_plug_nonexistent_device(self):
        with self.assertRaises(ValueError):
            self.flat.plug_device("Unknown")

    def test_total_power(self):
        self.flat.plug_device("Kettle")
        self.flat.plug_device("TV")
        expected = 2000 + 120
        self.assertEqual(self.flat.total_power(), expected)

    def test_total_power_none_plugged(self):
        self.assertEqual(self.flat.total_power(), 0)

    def test_sort_by_power(self):
        self.flat.sort_by_power()
        powers = [d.power for d in self.flat.devices]
        self.assertEqual(powers, sorted(powers))

    def test_find_by_radiation(self):
        result = self.flat.find_by_radiation(0.3, 0.8)
        self.assertTrue(all(0.3 <= d.radiation <= 0.8 for d in result))

    def test_invalid_radiation_range(self):
        with self.assertRaises(ValueError):
            self.flat.find_by_radiation(1.0, 0.5)

if __name__ == "__main__":
    unittest.main()