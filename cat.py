class MyFriend:
    def __init__(self, name):
        self.name = name

    def maykat(self):
        print(self.name + ": Мяу! Мяу!")

    def kusat(self):
        print(self.name + " кушает!")

my_friend = MyFriend("Мурзик_67")

my_friend.maykat()
my_friend.kusat()