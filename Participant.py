
# Importing Math Library.
import math
# Defining the Participant Class.
class Participant:
    # Initialising All Attributes(Private and Public).
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str):
        self.name = name
        self.idi = idi
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__birth_day = birth_day
        self.__gender = gender
    # Returns all attributes of the participant as a tuple securely.
    def get_values(self):
        return (
            self.name,
            self.idi,
            self.__birth_year,
            self.__birth_month,
            self.__birth_day,
            self.__gender
        )
    # Prints all participant details for easy human-readable display.
    def show_values(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.idi}")
        print(f"Birth Year: {self.__birth_year}")
        print(f"Birth Month: {self.__birth_month}")
        print(f"Birth Day: {self.__birth_day}")
        print(f"Gender: {self.__gender}")
        return None
    # Sets both inherited and new attributes.
    def set_values(self, data_attributes: dict):
        for key, value in data_attributes.items():
            if key == "name":
                self.name = value
            elif key == "idi":
                self.idi = value
            elif key == "birth_year":
                self.__birth_year = value
            elif key == "birth_month":
                self.__birth_month = value
            elif key == "birth_day":
                self.__birth_day = value
            elif key == "gender":
                self.__gender = value
        return None
    # Computes age using the current date. Returns the age in years. Performed using math.floor()
    def calculate_age(self, curr_day: int, curr_month: int, curr_year: int) -> int:
        # Checking Input Validity.
        if(curr_day==31 and curr_month in set(2,4,6,9,11)):
            return -1
        if(curr_month==2 and curr_day==30):
            return -1
        if(not(0<curr_day<32) or not (0<curr_month<13)):
            return -1
        age = curr_year - self.__birth_year
        if (curr_month, curr_day) < (self.__birth_month, self.__birth_day):
            age -= 1
            
        return math.floor(age)
    
