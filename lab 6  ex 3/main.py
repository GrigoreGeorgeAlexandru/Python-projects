from math import sqrt


def isInside(circle_x, circle_y, rad, x, y):
    if ((x - circle_x) * (x - circle_x) +
            (y - circle_y) * (y - circle_y) < rad * rad):
        print("inauntru")
    elif ((x - circle_x) * (x - circle_x) +
            (y - circle_y) * (y - circle_y) == rad * rad):
        print("pe latura" )
    else:
        print("inafara ")


def getCircle(x1, y1, x2, y2, x3, y3):
    x12 = x1 - x2
    x13 = x1 - x3

    y12 = y1 - y2
    y13 = y1 - y3

    y31 = y3 - y1
    y21 = y2 - y1

    x31 = x3 - x1
    x21 = x2 - x1


    sx13 = pow(x1, 2) - pow(x3, 2)


    sy13 = pow(y1, 2) - pow(y3, 2)

    sx21 = pow(x2, 2) - pow(x1, 2)
    sy21 = pow(y2, 2) - pow(y1, 2)

    f = (((sx13) * (x12) + (sy13) *
          (x12) + (sx21) * (x13) +
          (sy21) * (x13)) // (2 *
                              ((y31) * (x12) - (y21) * (x13))))

    g = (((sx13) * (y12) + (sy13) * (y12) +
          (sx21) * (y13) + (sy21) * (y13)) //
         (2 * ((x31) * (y12) - (x21) * (y13))))

    c = (-pow(x1, 2) - pow(y1, 2) -
         2 * g * x1 - 2 * f * y1)


    h = -g
    k = -f
    sqr_of_r = h * h + k * k - c


    r = round(sqrt(sqr_of_r), 5)

    return h, k, r

with open("6.in") as f:
    triunghi=[[int(j) for j in next(f).strip('\n').split(' ')] for t in range(3)]
    x,y,r=getCircle(triunghi[0][0],triunghi[0][1],triunghi[1][0],triunghi[1][1],triunghi[2][0],triunghi[2][1])
    print(x,y,r)
    nr = int(f.readline())
    for q in range(nr):
        points = [int(j) for j in next(f).strip('\n').split(' ')]
        isInside(x,y,r,points[0],points[1])