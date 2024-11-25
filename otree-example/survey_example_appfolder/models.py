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

author = 'Richard Neureuther'
doc = 'Test survey for the Tutorial'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
#The Variables are structured on the base of pages
    name_question = models.StringField(label="Please enter your name here:")

    age_question = models.IntegerField(label="Please enter your age here:", max= 120, min=1)
    
    study_field_question = models.StringField(label="Please enter your field of study here:")

    satisfaction = models.IntegerField(initial=-999, label="Please select the value that is most fitting:")

    additional_comments = models.StringField(label="Is there anything else you want to add?")

    windows_interface = models.IntegerField(initial=-999, label="Please select the value that is most fitting:")

    iOS_interface = models.IntegerField(initial=-999, label="Please select the value that is most fitting:")

    screen_height = models.IntegerField(initial=-999)
    screen_width = models.IntegerField(initial=-999)
                              