import sys

n=input()
if(n<2):
    print 'n<2 not allowed'
numbers=[]
for i in range(n):
    numbers.append(input())
result=[-1,-1]
maxBenefit=-sys.maxint -1
minimum=sys.maxint
min_index=0

for i in range(1,n):
	if(numbers[i-1]<minimum):
		minimum=numbers[i-1]
##		print numbers[i-1]
	benefit=numbers[i]-minimum
	if (benefit>maxBenefit):
		maxBenefit=benefit
		result[0]=min_index
		result[1]=i
print result[0]+1
print result[1]+1

