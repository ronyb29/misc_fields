import unittest

from tests.test_models import Engine, fuel_carburation, fuel_injection, Transmission
from tests.test_utils import ModelTestCase


class TestFormatterStrategy(ModelTestCase):
    requires = [Engine]

    def test_strategy_serialization(self):
        Engine.create(id=1, fuel_up=fuel_carburation).save()
        carburated = Engine.get(id=1)
        assert isinstance(carburated, Engine)
        self.assertEqual(carburated.fuel_up(), 'carburation')

        Engine.create(id=2, fuel_up=fuel_injection).save()
        injected = Engine.get(id=2)
        assert isinstance(injected, Engine)
        self.assertEqual(injected.fuel_up(), 'injection')

    def test_enum_serialization(self):
        Engine.create(id=3, transmission=Transmission.manual).save()
        manual = Engine.get(id=3)
        assert isinstance(manual, Engine)
        self.assertEqual(manual.transmission, Transmission.manual)

    #TODO: test for non int enums

if __name__ == '__main__':
    unittest.main()
