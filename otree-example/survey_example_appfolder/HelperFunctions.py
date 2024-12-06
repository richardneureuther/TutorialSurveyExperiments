import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number

#screenout for everyone older than 40
def detect_screenout(self):
    if self.player.age_question > 40:
        self.player.screenout = 1

#screenout if quota is already full 
def detect_quota(self):
    
    if self.player.screenout == 0 and self.player.quota == 0:

        #acces gender quotas dict
        gender_quotas = self.session.vars['gender_quotas']
        #store the selected gender 
        selected_gender = self.player.gender_question 

        # Get the current completed count for the selected gender
        current_count = self.session.vars[f"completed_gender_{selected_gender}"]
        max_quota = gender_quotas[selected_gender]

        # Apply quota logic
        if current_count >= max_quota:
             self.player.quota = True  # Mark as screened out
        else:
            # Increment the quota counter for the selected gender
            self.session.vars[f"completed_gender_{selected_gender}"] += 1
            self.player.quota = False

    


            
      
