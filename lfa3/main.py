regex= open("input.in").readline().strip()
index1=regex.find("(")
index2=regex.find(")")
letters={x.strip() for x in regex[index1+1:index2].split(",")}
print(letters)