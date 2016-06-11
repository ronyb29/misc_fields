from enum import Enum

from peewee import *

from misc_fields import StrategyField, EnumField

database = SqliteDatabase(':memory:')


class Transmission(Enum):
    automatic = 1
    manual = 2


def fuel_injection():
    return "injection"


def fuel_carburation():
    return "carburation"


class Engine(Model):
    id = PrimaryKeyField()
    fuel_up = StrategyField([fuel_carburation, fuel_injection], default_strategy=fuel_carburation, null=True)
    transmission = EnumField(Transmission, Transmission.automatic, null=True)


Engine.create_table(fail_silently=True)
