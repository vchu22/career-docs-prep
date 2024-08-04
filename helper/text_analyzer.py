from collections import Counter
import string
import json

class TextAnalyzer:
    def __init__(self) -> None:
        # self.skill_words = [
        #     "python", "java", "sql", "communication", "teamwork", 
        #     "problem-solving", "data science", "machine learning", "leadership"
        # ]
        with open('helper/data/skill_words.json', 'r') as file:
            self.skill_words = json.load(file)
        self.description = ""

    def find_most_common_skills(self, n : int):
        text = self.description.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        filtered_skills = [word for word in words if word in self.skill_words]
        skill_counts = Counter(filtered_skills)
        return skill_counts.most_common(n)