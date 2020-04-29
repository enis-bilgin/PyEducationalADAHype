from pprint import pprint


class UserIdGenerator:
    def __init__(self):
        self.initialid = 10000

    def getNewId(self):
        temp = self.initialid
        self.initialid += 1
        return temp


class SingleUser:
    def __init__(self, name, age, location, userid):
        self.name = str(name)
        self.age = int(age)
        self.location = str(location)
        self.userid = int(userid)

    def showUser(self):
        pprint("User: {0}, Age: {1}, Location: {2}, id: {3}".format(self.name, self.age, self.location, self.userid))


class UserDictionary(dict):

    def __init__(self, *args, **kwargs):
        super(UserDictionary, self).__init__(*args, **kwargs)

    def readUser(self, id):
        temp_user = self.__dict__.get(id)
        if temp_user is not None:
            temp_user.showUser()
        else:
            pprint("User does not Exist in Database")

    def updateOrAddUser(self, name, age, location, userid):
        self.__dict__[userid] = SingleUser(name, age, location, userid)
        return

    def deleteUser(self, userid):
        self.__dict__.__delitem__(userid)
        return

    def readAllUsers(self):
        for key, value in self.__dict__.items():
            value.showUser()

    def countUsers(self):
        pprint("Size of database: {0}".format(len(self.__dict__)))

    def deleteAllUsers(self):
        self.__dict__.clear()