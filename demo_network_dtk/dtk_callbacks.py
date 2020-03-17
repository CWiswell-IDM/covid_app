from utils import DtkPerson

import dtk_generic_intrahost as dgi


def create_person_callback(self, mcw, age, gender):
    self.humans.append(DtkPerson(dgi.create((gender, age, mcw))))
