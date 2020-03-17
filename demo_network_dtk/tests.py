import unittest
unittest.__unittest

import dtk_nodedemog as dnd

import utils
import dtk_callbacks


class DtkCovidTests(unittest.TestCase):
    def setUp(self):
        self.population = None
        pass

    def tearDown(self):
        pass

    # region helpers
    def create_population(self):
        self.population = utils.Population()
        dnd.set_callback(dtk_callbacks.create_person_callback)
        dnd.populate_from_files()

    # endregion
    # region Population
    def test_init_population(self):
        self.assertIsNone(self.population)
        self.create_population()
        self.assertIsNotNone(self.population)

    # endregion