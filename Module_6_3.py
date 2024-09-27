class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = dx
        self.x_distance = dx
        print(dx)


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dy = dy
        self.y_distance = dy
        print(dy)


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance, y_distance, sound)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self, x_distance, y_distance):
        return x_distance, y_distance

    def voise(self):
        return f'{self.sound}'


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

# p1.voice()
