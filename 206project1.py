#Julie Burke
#Expected score = 200
# worked with Olivia Gardella on basic concepts 
import os
import filecmp
import csv
from datetime import date
from datetime import datetime

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	filedata = []
	#Your code here:
	with open(file) as f:
		reader = csv.DictReader(f)
		for row in reader:
			filedata.append(row)
	return filedata


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorteddata = sorted(data, key = lambda x: x[col])
	return sorteddata[0]['First'] + ' ' + sorteddata[0]['Last']

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	classsize = {}
	for x in data:
		classsize[x['Class']] = classsize.get(x['Class'], 0) + 1
	return sorted(classsize.items(), key = lambda x: x[1], reverse = True)

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	daycounts = {}
	#Your code here:
	for x in a:
		day = x['DOB'].split('/')[1]
		daycounts[day] = daycounts.get(day, 0) + 1
	
	return int(sorted(daycounts.items(), key = lambda x: x[1], reverse = True)[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	ages = []
	today = date.today()
	for row in a:
		born= datetime.strptime(row['DOB'], "%m/%d/%Y")
		ages.append(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
	return round (sum(ages) / len (ages))


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	#Your code here:
	b = []
	for item in a:
		newdict = {"First": item["First"], "Last": item["Last"], "Email": item["Email"]}
		b.append(newdict)
	sorteddata = sorted(b, key = lambda x: x[col])
	keys = sorteddata[0].keys()
	with open(fileName,'w', newline="\n") as output_file:
		for person in sorteddata:
			output_file.write(person["First"] + "," + person["Last"] + "," + person["Email"] +"\n")

		#writer = csv.DictWriter(output_file, fieldnames = keys)
		#writer.writeheader()
		#writer.writerows(sorteddata)
	output_file.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

