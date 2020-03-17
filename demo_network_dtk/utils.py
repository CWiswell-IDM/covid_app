
import json
from enum import Enum

import numpy as np

import dtk_generic_intrahost as dgi

class Gender(Enum):
    male = 1
    female = 0


class State(Enum):
    healthy = 0
    incubating = 1
    infected = 2
    dead = 3


class DtkPerson:
    """
    Represent a DTK person
    id: id in DTK
    """

    def __init__(self, person_id: int):
        self.id = person_id
        individual_info = json.loads(dgi.serialize(self.id))["individual"]
        self.gender = Gender(individual_info["m_gender"])
        self.age = individual_info["m_age"]
        self.mcw = individual_info["m_mc_weight"]
        self.state = State.healthy

    @property
    def formatted_age(self):
        """
        Returns a string representing the age
        """
        year = int(self.age / 365)
        months = int((self.age % 365) / 30)
        days = (self.age % 365) % 30
        return f"{year} years, {months} months, {int(days)} days"

    def __repr__(self):
        return f"<Individual {self.gender} #{self.id} - age: {self.age}>"


class DtkPersonNetwork(DtkPerson):
    def __init__(self, person_id, network_id):
        super().__init__(person_id)
        self.network_id = network_id

class Population(list):
    """
    Represents a population of individuals (DTKPerson)
    """

    def humans_older_than(self, age: int, state: State = None):
        """
        Returns a list of humans older than a given age.
        Optionally pass a state to also filter by state
        :param age: Minimum age (non inclusive)
        :param state: State
        :return: List of filtered individuals
        """
        if state:
            return list(filter(lambda human: human.age > age, self.get_humans_with_state(state)))
        return list(filter(lambda human: human.age > age, self))

    @property
    def men_count(self):
        """
        Count of males in the population
        """
        return sum(human.gender == Gender.male for human in self)

    @property
    def women_count(self):
        """
        Count of females in the population
        """
        return sum(human.gender == Gender.female for human in self)

    @property
    def mean_age(self):
        """
        Mean age of the population
        """
        return np.mean([human.age for human in self])

    @property
    def std_age(self):
        """
        Standard deviation of ages in the population
        """
        return np.std([human.age for human in self])

    def count_state(self, state: State):
        """
        How many individuals with the given state
        """
        return sum(human.state == state for human in self)

    def get_humans_with_state(self, state: State):
        """
        Get individuals with a given state
        """
        return list(filter(lambda human: human.state == state, self))