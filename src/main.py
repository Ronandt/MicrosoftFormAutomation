from microsoft_form_filler import MicrosoftFormFiller
from url import Url
from datetime import date
from datetime import datetime
from datetime import time
from user import User
import rpa

user_profile = User("Test")
MicrosoftFormFiller(url = Url('Your form here')) \
.fill_input(user_profile.username) \
.fill_radio(1 + (time(12,0) < datetime.now().time() )) \
.fill_input(f"{date.today().strftime('%#m/%#e/%Y')}") \
.fill_input("9AM" if (time(12,0) > datetime.now().time() ) else "6PM")\
.submit_form()

