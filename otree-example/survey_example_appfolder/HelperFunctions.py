import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number



'''
we also want to implement some functions to help with the quota checking and 
to have an overwview (counting) who is taking part in our survey.

Generally when it comes to redirecting we distinguish between people who: 
1. took part in the whole survey (and get redirected as success to the provider)
2. people who get screened-out (meaning they did not fulfill a characteristic one agreed upon previously)
3. people who get redirected because the quota is already full

We encode those three different event in three different variables (booleans) to use for redirecting

'''
#screenout for everyone older than 40
def detect_screenout(self):
    if self.player.age_question > 40:
        self.player.screenout = 1

#screenout if quota is already full 
def detect_quota(self):
    #acces gender quotas dict
    gender_quotas = self.session.vars['gender_quotas']

    #store the selected gender 
    selected_gender = self.player.gender_question

    #if quota is full set boolean quota to 1
    if gender_quotas[selected_gender] >= 1:
        self.player.quota = 1  
    #if quota is not full increase the counter in the dict by the gender selected 
    else:
        gender_quotas[selected_gender] += 1
