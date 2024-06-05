# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
schoolNames = ["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School", "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"]
schoolCodes = ["1224", "1679", "9626", "9806", "9813", "9815", "9816", "9823", "9825", "9826", "9829", "9830", "9836", "9847", "9850", "9856", "9857", "9858", "9860", "9865"]

enrollmentYears = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

#(year, school, grade)
data3DArray = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]).reshape((10,20,3))

#Dictionary to get school name by given school code key
schoolCodeDict = {schoolCodes[i]: schoolNames[i] for i in range(len(schoolCodes))}

#Dictionary to get school code by given school name key
schoolNameDict = {schoolNames[i]: schoolCodes[i] for i in range(len(schoolNames))}

# You may add your own additional classes, functions, variables, etc.

class School:

    def __init__(self):
        self.schoolName = ""
        self.schoolCode = ""
        self.schoolIndex = -1

    def updateSchoolByName(self, name):
        self.schoolName = name
        self.schoolCode = schoolNameDict[name]
        self.schoolIndex = schoolNames.index(self.schoolName)

    def updateSchoolByCode(self, code):
        self.schoolCode = code
        self.schoolName = schoolCodeDict[code]
        self.schoolIndex = schoolNames.index(self.schoolName)

    def getMeanEnrollment(self, grade):
        enrollmentNumbers = []
        #loop through (i, schoolIndex, grade)
        for i in range(10):
            #If statement to deal with nan values
            if not np.isnan(data3DArray[i, self.schoolIndex, grade]):
                enrollmentNumbers.append(data3DArray[i, self.schoolIndex, grade])
        #Convert return type to int32 for print() function
        return str(np.mean(enrollmentNumbers).astype(np.int32))

    def getLowestEnrollment(self):
        totalEnrollmentNumbers = []
        #loop through (i, schoolIndex, j)
        for i in range(10):
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data3DArray[i, self.schoolIndex, j]):
                    totalEnrollmentNumbers.append(data3DArray[i, self.schoolIndex, j])
        #Convert return type to int32 for print() function
        return str(np.min(totalEnrollmentNumbers).astype(np.int32))
    
    def getHighestEnrollment(self):
        totalEnrollmentNumbers = []
        #loop through (i, schoolIndex, j)
        for i in range(10):
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data3DArray[i, self.schoolIndex, j]):
                    totalEnrollmentNumbers.append(data3DArray[i, self.schoolIndex, j])
        #Convert return type to int32 for print() function
        return str(np.max(totalEnrollmentNumbers).astype(np.int32))
    
    def printTotalEnrollments(self):
        for i in range(10):
            enrollmentSum = []
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data3DArray[i, self.schoolIndex, j]):
                    enrollmentSum.append(data3DArray[i, self.schoolIndex, j])
            print("Total enrollment for " + enrollmentYears[i] + ": " + str(np.sum(enrollmentSum).astype(np.int32)))
        
    def getTotal10YearEnrollment(self):
        total10YearEnrollment = 0

        for i in range(10):
            enrollmentSum = []
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data3DArray[i, self.schoolIndex, j]):
                    enrollmentSum.append(data3DArray[i, self.schoolIndex, j])
            total10YearEnrollment += np.sum(enrollmentSum)
        
        return str(total10YearEnrollment.astype(np.int32))
    
    def getMean10YearEnrollment(self):
        yearlyEnrollment = []

        for i in range(10):
            sumOfGradesEnrollment = 0
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data3DArray[i, self.schoolIndex, j]):
                    sumOfGradesEnrollment += data3DArray[i, self.schoolIndex, j]
            yearlyEnrollment.append(sumOfGradesEnrollment)
        return str(np.mean(yearlyEnrollment).astype(np.int32))
    
    def printLargeEnrollmentMedian(self):
        #Sub array view for schools
        school_data = data3DArray[:, self.schoolIndex, :]
        #Masking operation
        large_enrollments = school_data[school_data > 500]

        if len(large_enrollments) == 0:
            print("No enrollments over 500.")
        else:
            print("For all enrollments over 500, the median value was: " + str(np.median(large_enrollments).astype(np.int32)))
    

def getUserInput(message):
    while True:
        try:
            user_input = input(message)

            if user_input in schoolNames:
                return user_input
            elif user_input in schoolCodes:
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Invalid school name or code!\n")
        
def getTotalMeanByYear(year):
    enrollmentNumbers = []
    for i in range(20):
        for j in range(3):
            #If statement to deal with nan values
            if not np.isnan(data3DArray[year, i, j]):
                enrollmentNumbers.append(data3DArray[year, i, j])
    #Convert return type to int32 for print() function
    return str(np.mean(enrollmentNumbers).astype(np.int32))

def getTotalGraduatingClassSize(year):
    enrollmentNumbers = []
    for i in range(20):
        #If statement to deal with nan values
        if not np.isnan(data3DArray[year, i, 2]):
            enrollmentNumbers.append(data3DArray[year, i, 2])
    #Convert return type to int32 for print() function
    return str(np.sum(enrollmentNumbers).astype(np.int32))

def getHighestEnrollmentByGrade():
    #(year, school, grade)
    highestEnrollment = 0

    #Loop through all 10 years of data
    for i in range(10):
        #Loop through all 20 schools
        for j in range(20):
            ##Loop through all 3 grades
            for k in range(3):
                if not np.isnan(data3DArray[i, j, k]):
                    if data3DArray[i, j, k] > highestEnrollment:
                        highestEnrollment = data3DArray[i, j, k]
        
    return str(highestEnrollment.astype(np.int32))

def getLowestEnrollmentByGrade():
    #(year, school, grade)
    #Initialize to very high number that will never be true
    lowestEnrollment = 999999

    #Loop through all 10 years of data
    for i in range(10):
        #Loop through all 20 schools
        for j in range(20):
            ##Loop through all 3 grades
            for k in range(3):
                if not np.isnan(data3DArray[i, j, k]):
                    if data3DArray[i, j, k] < lowestEnrollment:
                        lowestEnrollment = data3DArray[i, j, k]
        
    return str(lowestEnrollment.astype(np.int32))
                

def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array:", data3DArray.shape)
    print("Dimensions of full data array", data3DArray.ndim)

    # Prompt for user input
    user_input = getUserInput("Please enter the high school name or school code: ")

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    #Create school object to keep track of chosen school
    chosenSchool = School()

    if user_input in schoolCodes:
        chosenSchool.updateSchoolByCode(user_input)
    else:
        chosenSchool.updateSchoolByName(user_input)

    #Printing school name and code
    print("School Name: " + chosenSchool.schoolName + ", School Code: " + chosenSchool.schoolCode)
    #Printing mean enrollment
    print("Mean enrollment for Grade 10:", chosenSchool.getMeanEnrollment(0))
    print("Mean enrollment for Grade 11:", chosenSchool.getMeanEnrollment(1))
    print("Mean enrollment for Grade 12:", chosenSchool.getMeanEnrollment(2))
    #Printing highest enrollment
    print("Highest enrollment for a single grade:", chosenSchool.getHighestEnrollment())
    #Printing lowest enrollment
    print("Lowest enrollment for a single grade:", chosenSchool.getLowestEnrollment())
    #Printing total enrollment for each year
    chosenSchool.printTotalEnrollments()
    #Printing total 10-year enrollment
    print("Total ten year enrollment: " + chosenSchool.getTotal10YearEnrollment())
    #Printing mean total 10-year enrollment
    print("Mean total enrollment over 10 years: " + chosenSchool.getMean10YearEnrollment())
    #Printing median of enrollments over 500
    chosenSchool.printLargeEnrollmentMedian()

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    #
    print("Mean enrollment in 2013: " + getTotalMeanByYear(enrollmentYears.index("2013")))
    print("Mean enrollment in 2022: " + getTotalMeanByYear(enrollmentYears.index("2022")))
    print("Total graduating class of 2022: " + getTotalGraduatingClassSize(enrollmentYears.index("2022")))
    print("Highest enrollment for a single grade: " + getHighestEnrollmentByGrade())
    print("Lowest enrollment for a single grade: " + getLowestEnrollmentByGrade())


if __name__ == '__main__':
    main()

