from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

from survey_example_appfolder.HelperFunctions import detect_screenout, detect_quota

class Welcome(Page):
    form_model = Player
    form_fields = [ 'screen_height', 'screen_width']
   
   

class DemoPage0(Page):
    form_model = Player
    form_fields = ['age_question', 'name_question', "gender_question"]

    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1

#we want to detect all the screenouts and the quota reached right away
        detect_screenout(self)
        detect_quota(self)


class DemoPage1(Page):
    form_model = Player
    form_fields = ['study_field_question']

    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label),
                'screenout': safe_json(self.player.screenout),
                'quota': safe_json(self.player.quota)
                }

class DemoPage2(Page):
    form_model = Player
    form_fields = ['satisfaction']

class DemoPage3(Page):
    form_model = Player
    form_fields = ["additional_comments","time_additional_comments"]

class DemoPage4_group1(Page):
    def is_displayed(self):
        return self.player.group_assignment == 0
    form_model = Player
    form_fields = ["windows_interface"]


class DemoPage4_group2(Page):
    def is_displayed(self):
        return self.player.group_assignment == 1
    form_model = Player 
    form_fields = ["iOS_interface"]

class PopupQuestion(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout']

class EndPage(Page):

    def vars_for_template(self):
        '''this is another function by otree which allows you to "send" variables
        to html files if you need to access them from there'''
        return {"group_assignment": safe_json(self.player.group_assignment)}
    form_model = Player

class RedirectPage(Page):
    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label)}
    

    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,      
                EndPage,
                RedirectPage]


#other pages (commented out  for testing )
#               DemoPage0,
#                DemoPage1,
 #               DemoPage2,
  #              DemoPage3,
   #             DemoPage4_group1,
    #            DemoPage4_group2, 
     #           PopupQuestion, 