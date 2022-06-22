from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random 
import json
from HelperFunctions import random_number

author = 'StartApp'
doc = ''

def seq_to_dict(s):
    '''for randomization'''
    r = {}
    l = len(s) - 1
    for i, j in enumerate(s):
        if i < l:
            r[j] = s[i + 1]
        else:
            r[j] = None
    return r


class Constants(BaseConstants):
    name_in_url = 'StartApp'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    import random

    session.wait_for_ids = 1
    session.arrived_ids = 2

##
    app_seq = subsession.config.get('app_sequence')

    for p in subsession.get_players():
        # we just determine it randomly here.
        # in your game, you should replace it with your desired logic.

        #randomizing
        first_app, second_app, *tail = app_seq
        random.shuffle(tail)
        new_app_seq = [first_app] + tail + [second_app]
        p.sequence_of_apps = json.dumps(new_app_seq)
        p.participant.vars['_updated_seq_apps'] = seq_to_dict(new_app_seq)

        



class Group(BaseGroup):
    g_gender = models.IntegerField(initial=0)
    

class Player(BasePlayer):
    #randomization
    sequence_of_apps = models.LongStringField()
    
    #Welcome - METADATA
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)

    #QuotaQuestions - Questions to check the quota
    age = models.IntegerField()
    gender = models.IntegerField()
    federalstate = models.IntegerField()
    #variables on the HelperFunctions.py
    screenout = models.BooleanField(initial=0) #todo global
    quota = models.BooleanField(initial=0) #todo global