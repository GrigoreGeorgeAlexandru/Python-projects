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

def corection(equations,point):
    flag=0
    for eq in equations:
        if eq[0]*point[0]+eq[1]*point[1]+eq[2]>0:
            flag=1
            break
    if flag==0:
        return 1
    else:
        return 0


with open("input.in") as f:
    nr = int(f.readline())
    points = [[int(j) for j in next(f).strip('\n').split(' ')]for q in range(nr)]
print(points)
intersections=[]
for l1 in points:
    for l2 in points:
        if l1!=l2:
            point=Intersection(l1,l2)
            if point!=[] and point not in intersections:
                intersections.append(point)
print(intersections)
corpnt=[]
for point in intersections:
    if corection(points,point)==1:
        corpnt.append(point)
print(corpnt)

if len(corpnt)<2:
    print("intersectia este vida")
elif len(corpnt)<3:
    print("intersectia este nevida,nemarginita")
else:
    print("intersectia este nevida,marginita")
