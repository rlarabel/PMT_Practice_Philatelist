class Group:
    def __init__(self, name, face_value, pub_year, commercial_value):
        self.__name = name
        self.__face_value = face_value
        self.__pub_year = pub_year
        self.__commercial_value = commercial_value

    def get_face_value(self):
        return self.__face_value

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_pub_year(self):
        return self.__pub_year

    def set_pub_year(self, pub_year):
        self.__pub_year = pub_year

    def set_face_value(self, face_val):
        self.__face_value = face_val

    def get_commercial_value(self):
        return self.__commercial_value


class GroupI(Group):
    def __init__(self, name, face_value, pub_year):
        commercial_value = face_value
        Group.__init__(self, name, face_value, pub_year, commercial_value)


class GroupII(Group):
    def __init__(self, name, face_value, pub_year):
        commercial_value = face_value * 2
        Group.__init__(self, name, face_value, pub_year, commercial_value)


class Philatelist:
    def __init__(self, name=''):
        self.__name = name
        self.__stamp_collection = []
        self.__total = 0

    def calculate_total_commercial_value(self):
        for stamp in self.__stamp_collection:
            self.__total += stamp.get_commercial_value()
        return self.__total

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_stamps(self):
        return self.__stamp_collection

    def add_stamp(self, stamp):
        self.__stamp_collection.append(stamp)
