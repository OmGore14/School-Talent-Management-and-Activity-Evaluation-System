
import math
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
class Student(Participant):
    # Defining the some new attributes and inheriting some.
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, 
                 grade_level: int, class_assigned: str, gpa: float, selected_activity: str, 
                 talent_score: float, athletic_score: float, leadership_score: float):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__grade_level = grade_level
        self.__class_assigned = class_assigned
        self.__gpa = gpa
        self.__selected_activity = selected_activity
        self.__talent_score = talent_score
        self.__athletic_score = athletic_score
        self.__leadership_score = leadership_score
        self.__eligible = self.__gpa >= 5.0
        self.__age = self.calculate_age(1, 1, 2025)  # Derived at object creation
    # Calculates eligibility based on average scores and GPA and updates eligible feature.
    def is_eligible(self) -> bool:
        return self.__eligible
    # Returns all inherited and new attributes as a tuple.
    def get_values(self):
        return super().get_values() + (
            self.__age,
            self.__grade_level,
            self.__class_assigned,
            self.__gpa,
            self.__selected_activity,
            self.__talent_score,
            self.__athletic_score,
            self.__leadership_score,
            self.__eligible 
        )
    # Prints all student details, including those from Participant.
    def show_values(self):
        super().show_values()
        print(f"Age: {self.__age}")
        print(f"Grade Level: {self.__grade_level}")
        print(f"Class Assigned: {self.__class_assigned}")
        print(f"GPA: {self.__gpa}")
        print(f"Selected Activity: {self.__selected_activity}")
        print(f"Talent Score: {self.__talent_score}")
        print(f"Athletic Score: {self.__athletic_score}")
        print(f"Leadership Score: {self.__leadership_score}")
        print(f"Eligible: {self.__eligible}")
        return None
    # Sets both inherited and new attributes.
    def set_values(self, data_attributes: dict):
        super().set_values(data_attributes)
        for key, value in data_attributes.items():
            if key == "grade_level":
                self.__grade_level = value
            elif key == "class_assigned":
                self.__class_assigned = value
            elif key == "gpa":
                self.__gpa = value
            elif key == "selected_activity":
                self.__selected_activity = value
            elif key == "talent_score":
                self.__talent_score = value
            elif key == "athletic_score":
                self.__athletic_score = value
            elif key == "leadership_score":
                self.__leadership_score = value
        self.__age = self.calculate_age(1, 1, 2025)
        self.__eligible = self.__gpa >= 5.0
        return None
    def get_age(self):
        return self.__age
    def get_talent_score(self):
        return self.__talent_score
    def set_eligible(self, value : bool):
        self.__eligible = value
    def get_gpa(self):
        return self.__gpa
    def get_athletic_score(self):
        return self.__athletic_score
    
class Artist(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, 
                 grade_level: int, class_assigned: str, gpa: float, selected_activity: str, 
                 talent_score: float, athletic_score: float, leadership_score: float, talent : str):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, grade_level, class_assigned, gpa, selected_activity, talent_score, athletic_score, leadership_score)
        self.__performance_level = self.get_talent_score()
        self.__talent = talent
    def get_values(self):
        return super().get_values() + (self.__performance_level, self.__talent)
    def show_values(self):
        super().show_values()
        print(f"Performance Level: {self.__performance_level}")
        print(f"Talent: {self.__talent}")
        return None
    def set_values(self, data_attributes):
        super().set_values(data_attributes)
        for key, value in data_attributes.items():
            if key == "performance_level":
                self.__performance_level = value
            if key == "talent":
                self.__talent = value
        self.__performance_level = self.get_talent_score()
        return None
    def is_eligible(self):
        if(self.get_gpa()>6 and self.get_age()>=16):
            self.set_eligible(True)
            return True
        else:
            self.set_eligible(False)
            return False
    def compute_scores(self):
        if(self.is_eligible()):
            return self.__performance_level
        else:
            return -1

class Athlete(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str,
                 grade_level: int, class_assigned: str, gpa: float, selected_activity: str,
                 talent_score: float, athletic_score: float, leadership_score: float, 
                 sports_category: str, fitness_score: float):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, 
                         grade_level, class_assigned, gpa, selected_activity, 
                         talent_score, athletic_score, leadership_score)
        self.__sports_category = sports_category
        self.__fitness_score = fitness_score
        self.__performance_level = self.get_athletic_score()

    def get_values(self):
        return super().get_values() + (self.__sports_category, self.__fitness_score, self.__performance_level)

    def show_values(self):
        super().show_values()
        print(f"Sports Category: {self.__sports_category}")
        print(f"Fitness Score: {self.__fitness_score}")
        print(f"Performance Level: {self.__performance_level}")
        return None

    def set_values(self, data_attributes):
        super().set_values(data_attributes)
        for key, value in data_attributes.items():
            if key == "sports_category":
                self.__sports_category = value
            elif key == "fitness_score":
                self.__fitness_score = value
        self.__performance_level = self.get_athletic_score()
        return None

    def is_eligible(self):
        if self.get_gpa() > 5.5 and self.get_age() >= 12:
            self.set_eligible(True)
            return True
        else:
            self.set_eligible(False)
            return False

    def compute_scores(self):
        if self.is_eligible():
            return self.__fitness_score * self.__performance_level
        else:
            return -1

class Scholar(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str,
                 grade_level: int, class_assigned: str, gpa: float, selected_activity: str,
                 talent_score: float, athletic_score: float, leadership_score: float,
                 subject_specialization: str, olympiad_scores: list):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, 
                         grade_level, class_assigned, gpa, selected_activity, 
                         talent_score, athletic_score, leadership_score)
        self.__subject_specialization = subject_specialization
        self.__olympiad_scores = olympiad_scores
        self.__performance_level = self.get_gpa()*10

    def get_values(self):
        return super().get_values() + (self.__subject_specialization, self.__olympiad_scores, self.__performance_level)

    def show_values(self):
        super().show_values()
        print(f"Subject Specialization: {self.__subject_specialization}")
        print(f"Olympiad Scores: {self.__olympiad_scores}")
        print(f"Performance Level: {self.__performance_level}")
        return None

    def set_values(self, data_attributes):
        super().set_values(data_attributes)
        for key, value in data_attributes.items():
            if key == "subject_specialization":
                self.__subject_specialization = value
            elif key == "olympiad_scores":
                self.__olympiad_scores = value
        self.__performance_level = self.get_gpa()*10
        return None

    def is_eligible(self):
        if ((self.get_gpa() > 8.0) and (self.get_age() >= 10) and 
            any(score > 80 for score in self.__olympiad_scores)):
            self.set_eligible(True)
            return True
        else:
            self.set_eligible(False)
            return False

    def compute_scores(self):
        if self.is_eligible():
            return sum(self.__olympiad_scores)*self.__performance_level
        else:
            return -1


