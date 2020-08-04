"""Main module."""

from random import randint
from .PersonFactorySeeds import FemaleFirstNames, MaleFirstNames, LastNames, Streets, USLocations, Email

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

class random_customer():
    def CreateRandomCustomer(self):
        Person = {}
        print(randint(0,1))
        isMale = True if (randint(0,1)==1) else False
        print(isMale)
        if isMale:
            Person["FirstName"] = camelCase(MaleFirstNames.getMaleFirstName())
            Person["Gender"] = "M"
        else:
            Person["FirstName"] = camelCase(FemaleFirstNames.getFemaleFirstName())
            Person["Gender"] = "F"
        Person["LastName"] = camelCase(LastNames.getLastName())
        Person["AddressLine1"] = camelCase(Streets.getStreet())
        ZipCityState = USLocations.getUSZipCityState()
        Person["City"] = camelCase(ZipCityState.split(",")[1])
        Person["StateCode"] = ZipCityState.split(",")[2]
        # Person["StateName"] = getStateName(Person["StateCode"])
        Person["Zip"] = ZipCityState.split(",")[0]
        Person["PersonalEmail"] = Email.getEmailAddress(Person['FirstName'], Person['LastName'], True, 'Personal')

        return Person
