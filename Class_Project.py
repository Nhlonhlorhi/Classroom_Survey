class ClassroomSurvey:
    def __init__(self):
        self.questions = [
            "Do you like Python? (yes/no)",
            "Have you used Git before? (yes/no)",
            "Do you prefer working in a team? (yes/no)",
            "Would you like more coding projects? (yes/no)"
        ]
        self.responses = []  
    
    def collect_responses(self):
        print("\nPlease answer the following questions:\n")
        for question in self.questions:
            while True:
                answer = input(question + " ").strip().lower()
                if answer in ["yes", "no"]:
                    self.responses.append(answer)
                    break
                else:
                    print("Invalid response. Please answer 'yes' or 'no'.")

    def tally_responses(self):
        tally = {"yes": 0, "no": 0}
        for answer in self.responses:
            if answer in tally:
                tally[answer] += 1
        return tally
    def display_summary(self):
        tally = self.tally_responses()
        print("\nSurvey Summary:")
        print("\nSurvey Summary:")
        for answer, count in tally.items():
            print(f"{answer.capitalize()} - {count}")

survey = ClassroomSurvey()
survey.collect_responses()
survey.display_summary()
result = survey.tally_responses()
print(result)
