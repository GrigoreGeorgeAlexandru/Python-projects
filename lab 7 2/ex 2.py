import math
from operator import itemgetter


def Intersection(a,b):
    a1=a[0]
    b1=a[1]
    c1=-a[2]
    a2 = b[0]
    b2 = b[1]
    c2 = -b[2]
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        point=[]
        return point
    else:
        x=(b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        point=[x,y]
        return point

def isRectangle(p1,p2,p3,p4):

  cx=(p1[0]+p2[0]+p3[0]+p4[0])/4
  cy=(p1[1]+p2[1]+p3[1]+p4[1])/4

  dd1=math.sqrt(abs(cx-p1[0]))+math.sqrt(abs(cy-p1[1]))
  dd2=math.sqrt(abs(cx-p2[0]))+math.sqrt(abs(cy-p2[1]))
  dd3=math.sqrt(abs(cx-p3[0]))+math.sqrt(abs(cy-p3[1]))
  dd4=math.sqrt(abs(cx-p4[0]))+math.sqrt(abs(cy-p4[1]))
  return (dd1==dd2 and dd1==dd3 and dd1==dd4)

def solve(bl, tr, p) :
   if (p[0] > bl[0] and p[0] < tr[0] and p[1] > bl[1] and p[1] < tr[1]) :
      return True
   else :
      return False
def Area_of_a_Rectangle(width, height):

    Area = width * height
    return  Area

with open("input.in") as f:
    pp=[float(x) for x in f.readline().strip('\n').split(' ')]
    nr = int(f.readline())
    points = [[float(j) for j in next(f).strip('\n').split(' ')]for q in range(nr)]

intersections=[]
for l1 in points:
    for l2 in points:
        if l1!=l2:
            point=Intersection(l1,l2)
            if point!=[] and point not in intersections:
                intersections.append(point)


flag1=0
minarea=-1
minlist=[]
if len(intersections)>=4:
    for p1 in intersections:
        for p2 in intersections[intersections.index(p1)+1:]:
            for p3 in intersections[intersections.index(p2)+1:]:
                for p4 in intersections[intersections.index(p3)+1:]:
                    if p1!=p2!=p3!=p4:
                        if isRectangle(p1,p2,p3,p4)==1:
                           list=[p1,p2,p3,p4]
                           list=sorted(list,key=itemgetter(1))
                           list=sorted(list,key=itemgetter(0))
                           print(list)
                           if solve(list[0],list[3],pp)==True:
                               flag1=1
                               h = ((((list[1][0] - list[0][0]) ** 2) + ((list[1][1] - list[0][1]) ** 2)) ** 0.5)
                               w = ((((list[2][0] - list[0][0]) ** 2) + ((list[2][1] - list[0][1]) ** 2)) ** 0.5)
                               area=Area_of_a_Rectangle(h,w)
                               if minarea==-1 or minarea>area:
                                   minarea=area
                                   minlist=list

if flag1==1:

    print("(a) exista un dreptunghi cu proprietatea ceruta, (b) valoarea minima a ariilor dreptunghiurilor cu proprietatea ceruta este "+str(minarea))
    print(minlist)
else:
    print("(a) nu exista un dreptunghi cu proprietatea ceruta.")

