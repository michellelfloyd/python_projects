class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastesLike(self):
        raise NotImplementedException("Subclasses are responsible for creating this method")


class HotDog(Food):
    def tastesLike(self):
        print self.name, "is type", type(self), "has", self.calories, "calories and tastes like Extremely processed meat"


class Hamburger(Food):
    def tastesLike(self):
        print self.name, "is type", type(self), "has", self.calories, "calories and tastes like grilled goodness"


class ChickenPatty(Food):
    def tastesLike(self):
        print self.name, "is type", type(self), "has", self.calories, " calories and tastes like chicken"

dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Mickey Mouse shaped Chicken Tenders', 170))

for course in dinner:
    course.tastesLike()

