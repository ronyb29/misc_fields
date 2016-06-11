import unittest

from peewee import *

database = SqliteDatabase(':memory:')


class ModelTestCase(unittest.TestCase):
    requires = None
    db = database

    def setUp(self):
        super(ModelTestCase, self).setUp()
        if self.requires:
            self.db.drop_tables(self.requires, True)
            self.db.create_tables(self.requires)

    def tearDown(self):
        super(ModelTestCase, self).tearDown()
        if self.requires:
            self.db.drop_tables(self.requires, True)
