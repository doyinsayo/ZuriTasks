class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

        pass

    def change_name(self, new_name):

        self.new_name = new_name
        print("Name has been updated to" + " " + self.new_name)

    def change_age(self, new_age):
        self.new_age = new_age
        print("Age has been updated to" + " ", self.new_age)

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print("Track has been updated to" + " ", self.tracks)

    def get_score(self):
        print("the score is ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()