inputdata = input ('Enter comma separated data \n')
inputlist = list(inputdata)
for char in inputlist:
    inputlist.remove(',')
print(inputlist)