import string
import random
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

email={}

def getEmailAddress(firstName, lastName, isPrimary=True, emailType='Personal'):
    email['isPrimary'] = isPrimary
    email['emailType'] = emailType
    email['emailAddress'] = (firstName+"."+lastName+"."+random_string(5)+"@yopmail.com").lower()
    return email

# print(getEmailAddress("Govind", "Soni"))