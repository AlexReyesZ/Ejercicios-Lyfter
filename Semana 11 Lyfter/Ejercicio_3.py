class Striker:
    def __init__(self, kick_power):
        self.kick_power=kick_power

    def punch(self):
        print('Landing a heavy cross!')

    def high_kick(self):
        print(f'Executing a head kick with {self.kick_power}kg of force')

class Grappler:
    def __init__(self, submission_skills):
        self.submission_skills=submission_skills

    def takedown(self):
        print('Doble leg takedown succesful')

    def submit(self):
        print(f'Applying a Raer naked choke (Skill level: {self.submission_skills})')


class MMAFighter(Striker,Grappler):
    def __init__(self,name, kick_power, submission_skills):
        Striker.__init__(self, kick_power)
        Grappler.__init__(self, submission_skills)
        self.name=name

    def show_stats(self):
        print(f"\n--- Fighter Profile: {self.name} ---")
        print(f"Kick Power: {self.kick_power}kg")
        print(f"Submission Level: {self.submission_skills}")


fighter = MMAFighter("Alex Reyes", 85, 99)
fighter.show_stats()

print("\n--- The Fight Starts ---")
fighter.punch()         # Viene de Striker
fighter.takedown()      # Viene de Grappler
fighter.high_kick()     # Viene de Striker
fighter.submit()        # Viene de Grappler