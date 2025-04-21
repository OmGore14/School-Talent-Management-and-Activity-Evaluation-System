import math
import csv
from collections import defaultdict


class Participant:
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str):
        self.name = name
        self.idi = idi
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__birth_day = birth_day
        self.__gender = gender
    def get_values(self):
        return (
            self.name,
            self.idi,
            self.__birth_year,
            self.__birth_month,
            self.__birth_day,
            self.__gender
        )
    def show_values(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.idi}")
        print(f"Birth Year: {self.__birth_year}")
        print(f"Birth Month: {self.__birth_month}")
        print(f"Birth Day: {self.__birth_day}")
        print(f"Gender: {self.__gender}")
        return None
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
    def calculate_age(self, curr_day: int, curr_month: int, curr_year: int) -> int:
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
        self.__age = self.calculate_age(1, 1, 2025) 
    def get_class_assigned(self):
        return self.__class_assigned
    def is_eligible(self) -> bool:
        return self.__eligible
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
class Teacher(Participant):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, 
                 subject: str, mentor_grade: int, mentor_class: str, judge: bool):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__subject = subject
        self.__mentor_grade = mentor_grade
        self.__mentor_class = mentor_class
        self.__judge = judge
    def get_values(self):
        return super().get_values() + (
            self.__subject,
            self.__mentor_grade,
            self.__mentor_class,
            self.__judge
        )
    def show_values(self):
        super().show_values()
        print(f"Subject: {self.__subject}")
        print(f"Mentor Grade: {self.__mentor_grade}")
        print(f"Mentor Class: {self.__mentor_class}")
        print(f"Judge: {self.__judge}")
        return None
    def set_values(self, data_attributes: dict):
        super().set_values(data_attributes)
        for key, value in data_attributes.items():
            if key == "subject":
                self.__subject = value
            elif key == "mentor_grade":
                self.__mentor_grade = value
            elif key == "mentor_class":
                self.__mentor_class = value
            elif key == "judge":
                self.__judge = value
        return None
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
    def get_class_assigned(self):
        return super().get_class_assigned()
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
class Activity:
    def __init__(self, activity_id: int, activity_name: str, activity_type: str,
                 max_participants: int, grade_level: int, is_active: bool,
                 participants: list, organizers: list):
        self.activity_id = activity_id  
        self.activity_name = activity_name  
        self.__activity_type = activity_type  
        self.__max_participants = max_participants 
        self.__grade_level = grade_level  
        self.__is_active = is_active  
        self.__participants = participants 
        self.__organizers = organizers
    def get_values(self):
        return (
            self.activity_id,
            self.activity_name,
            self.__activity_type,
            self.__max_participants,
            self.__grade_level,
            self.__is_active,
            self.__participants,
            self.__organizers
        )
    def show_values(self):
        print(f"Activity ID: {self.activity_id}")
        print(f"Activity Name: {self.activity_name}")
        print(f"Activity Type: {self.__activity_type}")
        print(f"Max Participants: {self.__max_participants}")
        print(f"Grade Level: {self.__grade_level}")
        print(f"Is Active: {self.__is_active}")
        print(f"Participants: {self.__participants}")
        print(f"Organizers: {self.__organizers}") 
        return None
    def set_values(self, data_attributes: dict):
        for key, value in data_attributes.items():
            if key == "activity_id":
                self.activity_id = value
            if key == "activity_name":
                self.activity_name = value
            if key == "max_participants":
                self.__max_participants = value
            elif key == "grade_level":
                self.__grade_level = value
            elif key == "is_active":
                self.__is_active = value
            elif key == "participants":
                self.__participants = value
            elif key == "organizers":
                self.__organizers = value
        return None
    def get_participants(self):
        return self.__participants
class SportsTournament(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int,
                 grade_level: int, is_active: bool, participants: list, organizers: list, game_type: str, duration_minutes: int):
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)
        self.__game_type = game_type  
        self.__duration_minutes = duration_minutes
    def show_values(self):
        super().show_values()
        print(f"Game Type: {self.__game_type}")
        print(f"Duration Minutes: {self.__duration_minutes}")
        return None
    def determine_winner(self):
        if not self.get_participants(): 
            return -1

        if self.__game_type == "Team":
            teams = {}
            for athlete in self.get_participants():
                if isinstance(athlete, Athlete) and athlete.is_eligible(): 
                    team = athlete.get_class_assigned()
                    if team not in teams:
                        teams[team] = []
                    teams[team].append(athlete.compute_scores())

            team_averages = {
                team: sum(scores) / len(scores)
                for team, scores in teams.items()
                if scores  
            }

            if not team_averages:  
                return -1
            winning_team = max(team_averages, key=team_averages.get)
            winning_athletes = [
                athlete for athlete in self.get_participants()
                if isinstance(athlete, Athlete) and
                athlete.is_eligible() and
                athlete.get_class_assigned() == winning_team
            ]
            return max(winning_athletes, key=lambda a: (a.compute_scores(), -a.idi), default=None)

        elif self.__game_type == "Individual":
            return max(
                (athlete for athlete in self.get_participants() if isinstance(athlete, Athlete) and athlete.is_eligible()),
                key=lambda a: (a.compute_scores(), -a.idi),
                default=-1
            )
        return -1
class TalentShow(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int,
                 grade_level: int, is_active: bool, participants: list, organizers: list, talent_categories: list):
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)
        self.__talent_categories = talent_categories

    def show_values(self):
        super().show_values()
        print(f"Talent Categories: {self.__talent_categories}")
        return None

    def evaluate_talent(self):
        if not self.get_participants():
            return -1
        top_artist = max(
            (participant for participant in self.get_participants() if isinstance(participant, Artist)),
            key=lambda artist: (artist.compute_scores(), -artist.idi),
            default=-1
        )
        return top_artist
class AcademicCompetition(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int,
                 grade_level: int, is_active: bool, participants: list, organizers: list, subjects: list, max_marks: float):
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)
        self.__subjects = subjects
        self.__max_marks = max_marks

    def show_values(self):
        super().show_values()
        print(f"Subjects: {self.__subjects}")
        print(f"Max Marks: {self.__max_marks}")
        return None

    def determine_winner(self):
        if not self.get_participants():
            return -1
        top_scholar = max(
            (participant for participant in self.get_participants() if isinstance(participant, Scholar)),
            key=lambda scholar: scholar.compute_scores(),
            default=-1
        )
        return top_scholar


def load_participant_data(filepath: str) -> tuple[list[Student], list[Teacher]]:
    students = []
    teachers = []

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            idi = int(row["idi"])
            name = row["name"]
            birth_year = int(row["birth_year"])
            birth_month = int(row["birth_month"])
            birth_day = int(row["birth_day"])
            gender = row["gender"]

            subject = row["subject"].strip()
            if subject:  # Teacher case
                mentor_grade = int(row["mentor_grade"])
                mentor_class = row["mentor_class"]
                judge = row["judge"].strip().lower() == "true"
                teacher = Teacher(name, idi, birth_year, birth_month, birth_day, gender,
                                  subject, mentor_grade, mentor_class, judge)
                teachers.append(teacher)
            else:  # Student case
                grade_level = int(row["grade_level"])
                class_assigned = row["class_assigned"]
                gpa = float(row["gpa"])
                selected_activity = row["selected_activity"]
                talent_score = float(row["talent_score"])
                athletic_score = float(row["athletic_score"])
                leadership_score = float(row["leadership_score"])

                student = Student(name, idi, birth_year, birth_month, birth_day, gender,
                                  grade_level, class_assigned, gpa, selected_activity,
                                  talent_score, athletic_score, leadership_score,)
                students.append(student)

    return students, teachers
def specialised_students(filepath: str) -> tuple[list[Artist], list[Athlete], list[Scholar]]:

    artists = []
    athletes = []
    scholars = []

    classwise_data = {
        'Artist': defaultdict(list),
        'Athlete': defaultdict(list),
        'Scholar': defaultdict(list)
    }

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Skip row if any required field is empty
            required_fields = [
                "idi", "name", "birth_year", "birth_month", "birth_day", "gender",
                "grade_level", "class_assigned", "gpa", "selected_activity",
                "talent_score", "athletic_score", "leadership_score"
            ]
            if any(not row[field].strip() for field in required_fields):
                continue

            idi = int(row["idi"])
            name = row["name"]
            birth_year = int(row["birth_year"])
            birth_month = int(row["birth_month"])
            birth_day = int(row["birth_day"])
            gender = row["gender"]
            grade_level = int(row["grade_level"])
            class_assigned = row["class_assigned"]
            gpa = float(row["gpa"])
            selected_activity = row["selected_activity"]
            talent_score = float(row["talent_score"])
            athletic_score = float(row["athletic_score"])
            leadership_score = float(row["leadership_score"])

            if selected_activity == "Talent":
                if not row["talent"].strip():
                    continue
                talent = row["talent"]
                student = Artist(name, idi, birth_year, birth_month, birth_day, gender,
                                 grade_level, class_assigned, gpa, selected_activity,
                                 talent_score, athletic_score, leadership_score, talent)
                score = student.compute_scores()
                artists.append(student)
                classwise_data["Artist"][class_assigned].append((idi, name, grade_level, class_assigned, selected_activity, score))

            elif selected_activity == "Sports":
                if not row["fitness_score"].strip() or not row["sports_category"].strip():
                    continue
                fitness_score = float(row["fitness_score"])
                sports_category = row["sports_category"]
                student = Athlete(name, idi, birth_year, birth_month, birth_day, gender,
                                  grade_level, class_assigned, gpa, selected_activity,
                                  talent_score, athletic_score, leadership_score,
                                  sports_category, fitness_score)
                score = student.compute_scores()
                athletes.append(student)
                classwise_data["Athlete"][class_assigned].append((idi, name, grade_level, class_assigned, selected_activity, score))

            elif selected_activity == "Academic":
                if not row["subject_specialization"].strip():
                    continue
                subject_specialization = row["subject_specialization"]
                raw_scores = row["olympiad_scores"].replace("-", ",").strip("[] ")
                olympiad_scores = list(map(float, raw_scores.split(','))) if raw_scores else []
                student = Scholar(name, idi, birth_year, birth_month, birth_day, gender,
                                  grade_level, class_assigned, gpa, selected_activity,
                                  talent_score, athletic_score, leadership_score,
                                  subject_specialization, olympiad_scores)
                score = student.compute_scores()
                scholars.append(student)
                classwise_data["Scholar"][class_assigned].append((idi, name, grade_level, class_assigned, selected_activity, score))

    # Write per-class CSVs
    for category, data in classwise_data.items():
        for class_id, rows in data.items():
            filename = f"{class_id}-{category.lower()}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["participant_id", "name", "grade_level", "class_assigned", "selected_activity", "score"])
                writer.writerows(rows)

    return artists, athletes, scholars

