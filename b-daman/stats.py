f1=open("visor")
f2=open("back")
f3=open("body")
f4=open("core")
f5=open("foot")
f6=open("heel")
f7=open("larm")
f8=open("lshoulder")
f9=open("rarm")
f10=open("rshoulder")
g=open("results","w")
v1=[f.strip() for f in f1]
v2=[f.strip() for f in f2]
v3=[f.strip() for f in f3]
v4=[f.strip() for f in f4]
v5=[f.strip() for f in f5]
v6=[f.strip() for f in f6]
v7=[f.strip() for f in f7]
v8=[f.strip() for f in f8]
v9=[f.strip() for f in f9]
v10=[f.strip() for f in f10]
nr=1

for q in v1:
    weight=28
    parts=0
    visor = q.split()
    #print("visor "+str(visor)+str(weight)+" "+str(parts))
    if weight+int(visor[4])>102:
        break
    if parts+int(visor[5])>10:
        continue
    else:
        weight+=int(visor[4])
        parts+=int(visor[5])
        for w in v2:
            back = w.split()
            #print("back "+str(back)+str(weight)+ " "+str(parts))
            if weight + int(back[4] )> 102:
                break
            if parts + int(back[5] )> 10:
                continue
            else:
                weight += int(back[4])
                parts += int(back[5])
                for e in v3:
                    body = e.split()
                    #print("body "+str(body)+str(weight)+" "+str(parts))
                    if weight + int(body[4] )> 102:
                        break
                    if parts + int(body[5] )> 10:
                        continue
                    else:
                        weight += int(body[4])
                        parts += int(body[5])
                        for r in v4:
                            core = r.split()
                            #print("core "+str(core)+str(weight)+" "+str(parts))
                            if weight + int(core[4] )> 102:
                                break
                            if parts + int(core[5]) > 10:
                                continue
                            else:
                                weight += int(core[4])
                                parts += int(core[5])
                                for t in v5:
                                    foot = t.split()
                                    #print("foot "+str(foot)+str(weight)+" "+str(parts))
                                    if weight + int(foot[4]) > 102:
                                        break
                                    if parts + int(foot[5]) > 10:
                                        continue
                                    else:
                                        weight += int(foot[4])
                                        parts += int(foot[5])
                                        for y in v6:
                                            heel = y.split()
                                            #print("heel "+str(heel)+str(weight)+" "+str(parts))
                                            if weight + int(heel[4] )> 102:
                                                break
                                            if parts + int(heel[5]) > 10:
                                                continue
                                            else:
                                                weight += int(heel[4])
                                                parts += int(heel[5])
                                                for u in v7:
                                                    larm = u.split()
                                                    #print("larm "+ str(larm)+str(weight)+" "+str(parts))
                                                    if weight + int(larm[4] )> 102:
                                                        break
                                                    if parts + int(larm[5] )> 10:
                                                        continue
                                                    else:
                                                        weight += int(larm[4])*2
                                                        parts += int(larm[5])*2
                                                        for i in v8:
                                                            lshoulder = i.split()
                                                            #print("lshoulder "+str(lshoulder)+str(weight)+" "+str(parts))
                                                            if weight + int(lshoulder[4]) > 102:
                                                                break
                                                            if parts + int(lshoulder[5] )> 10:
                                                                continue
                                                            else:
                                                                weight += int(lshoulder[4])
                                                                parts += int(lshoulder[5])
                                                                for p in v10:
                                                                    rshoulder = p.split()
                                                                    #print("rshoulder "+str(rshoulder)+str(weight)+" "+str(parts))
                                                                    if weight +int( rshoulder[4]) > 102:
                                                                        break
                                                                    if parts +int( rshoulder[5]) > 10:
                                                                        continue
                                                                    else:
                                                                        weight += int(rshoulder[4])
                                                                        parts += int(rshoulder[5])
                                                                        rapidfire= int(visor[1])-4+int(back[1])+int(body[1])+int(core[1])+int(foot[1])+int(heel[1])+int(larm[1])*2+int(lshoulder[1])+int(rshoulder[1])
                                                                        power = int(visor[2])-5 + int(back[2]) + int(body[2]) + int(core[2]) + int(foot[2]) + int(heel[2]) + int(larm[2])*2 + int(lshoulder[2]) + int(rshoulder[2])
                                                                        accuracy = int(visor[3]) + int(back[3]) + int(body[3]) + int(core[3]) + int(
                                                                            foot[3]) + int(heel[3]) + int(larm[3])*2 + int(lshoulder[3]) + int(rshoulder[3])
                                                                        #print(str(weight) + " " + str(rapidfire//20+power//50))
                                                                        if (rapidfire//20+power//50)>=6:
                                                                            g.write(str(nr)+" "+str(rapidfire//20+power//50)+" "+str(rapidfire)+" "+str(power)+" "+str(accuracy)+" "+visor[0]+" "+back[0]+" "+body[0]+" "+core[0]+" "+foot[0]+" "+heel[0]+" "+larm[0]+" "+lshoulder[0]+" "+rshoulder[0]+"\n")
                                                                            nr+=1
                                                                        weight -= int(rshoulder[4])
                                                                        parts -= int(rshoulder[5])
                                                                weight -= int(lshoulder[4])
                                                                parts -= int(lshoulder[5])
                                                        weight -= int(larm[4]) * 2
                                                        parts -= int(larm[5]) * 2
                                                weight -= int(heel[4])
                                                parts -= int(heel[5])
                                        weight -= int(foot[4])
                                        parts -= int(foot[5])
                                weight -= int(core[4])
                                parts -= int(core[5])
                        weight -= int(body[4])
                        parts -= int(body[5])
                weight -= int(back[4])
                parts -= int(back[5])
        weight -= int(visor[4])
        parts -= int(visor[5])