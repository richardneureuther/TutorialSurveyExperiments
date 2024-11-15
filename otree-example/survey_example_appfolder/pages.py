from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player


class Welcome(Page):
    form_model = Player
   

class DemoPage0(Page):
    form_model = Player
    form_fields = ['age_question', 'name_question']

class DemoPage1(Page):
    form_model = Player
    form_fields = ['study_field_question']

class DemoPage2(Page):
    form_model = Player
    form_fields = ['satisfaction']

class DemoPage3(Page):
    form_model = Player
    form_fields = ["additional_comments"]


class EndPage(Page):
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage0,
                DemoPage1,  
                DemoPage2,  
                DemoPage3,        
                EndPage]