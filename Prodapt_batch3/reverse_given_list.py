aList = [100,200,300,400,500]
aList= aList[::-1]
print(aList)

#concatenate two lists index-wise

list1 = ["m","na","i","ke"]
list2 = ["y","me","s","lly"]
list3 = [ i+j for i ,j in zip(list1, list2)]
print(list3)

#output ["my","name","is","kelly"]

#remove empty strings from list of strings

list1=["Mike","","Emma","Kelly","","Brad"]
resList = list(filter(None, list1))
print(resList)