class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p1, p2, p3):

    val = (float(p2.y - p1.y) * (p3.x - p2.x)) - \
          (float(p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):


        return 1
    elif (val < 0):


        return 2
    else:

        return 0


with open('1.in') as f:
    w= int(f.readline())
    for line in f:
        x, y = [int(q) for q in line.split()]
        p1 = Point(x, y)
        x, y = [int(q) for q in f.readline().split()]
        p2 = Point(x, y)
        x, y = [int(q) for q in f.readline().split()]
        p3 = Point(x, y)
        print(p1.x , p1.y ,p2.x ,p2.y,p3.x,p3.y)
        o = orientation(p1, p2, p3)

        if (o == 0):
            print("Coliniare")
        elif (o == 1):
            print("viraj la dreapta")
        else:
            print("viraj la stanga")



