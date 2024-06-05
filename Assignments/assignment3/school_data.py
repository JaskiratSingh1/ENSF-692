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

# School names in a list
school_names = ["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School", "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"]
# Corresponding school codes in a list
school_codes = ["1224", "1679", "9626", "9806", "9813", "9815", "9816", "9823", "9825", "9826", "9829", "9830", "9836", "9847", "9850", "9856", "9857", "9858", "9860", "9865"]
# List of all the years from given_data
enrollment_years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

# 3D array by stacking existing 2D arrays in the format (year, school, grade)
data_3D_array = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]).reshape((10,20,3))

# Dictionary to get school name value by given school code key
school_code_dict = {school_codes[i]: school_names[i] for i in range(len(school_codes))}

# Dictionary to get school code value by given school name key
school_name_dict = {school_names[i]: school_codes[i] for i in range(len(school_names))}

# You may add your own additional classes, functions, variables, etc.

# Class to manage and compute various statistics for a chosen school
class School:
    # Constructor to initialize publiic identifying characteristics
    def __init__(self):
        self.school_name = ""
        self.school_code = ""
        self.school_index = -1

    """
    Takes in a school name as a String, updates school details variables
    """
    def update_school_by_name(self, name):
        self.school_name = name
        self.school_code = school_name_dict[name]
        self.school_index = school_names.index(self.school_name)

    """
    Takes in a school code as a String, updates school details variables
    """
    def update_school_by_code(self, code):
        self.school_code = code
        self.school_name = school_code_dict[code]
        self.school_index = school_names.index(self.school_name)

    """
    Takes grade as String and returns the mean of enrollment numbers for that grade 
    as a String (converted from a floored int32)
    """
    def get_mean_enrollment(self, grade):
        enrollment_numbers = []
        # Loop through (i, school_index, grade)
        for i in range(10):
            # If statement to deal with nan values
            if not np.isnan(data_3D_array[i, self.school_index, grade]):
                enrollment_numbers.append(data_3D_array[i, self.school_index, grade])
        # Convert return type to int32 for print() function
        return str(np.mean(enrollment_numbers).astype(np.int32))

    """
    Calculates the lowest enrollment for the given school and returns the value 
    as a String (converted from a floored int32)
    """
    def get_lowest_enrollment(self):
        total_enrollment_numbers = []
        # Loop through (i, school_index, j)
        for i in range(10):
            for j in range(3):
                # If statement to deal with nan values
                if not np.isnan(data_3D_array[i, self.school_index, j]):
                    total_enrollment_numbers.append(data_3D_array[i, self.school_index, j])
        # Convert return type to int32 for print() function
        return str(np.min(total_enrollment_numbers).astype(np.int32))
    
    """
    Calculates the highest enrollment for the given school and returns the value 
    as a String (converted from a floored int32)
    """
    def get_highest_enrollment(self):
        total_enrollment_numbers = []
        # Loop through (i, school_index, j)
        for i in range(10):
            for j in range(3):
                # If statement to deal with nan values
                if not np.isnan(data_3D_array[i, self.school_index, j]):
                    total_enrollment_numbers.append(data_3D_array[i, self.school_index, j])
        # Convert return type to int32 for print() function
        return str(np.max(total_enrollment_numbers).astype(np.int32))
    
    """
    Calculate the total enrollments accross all grades in a year and print it for all 10 years
    """
    def print_total_enrollments(self):
        # Loop through (i, school_index, j)
        for i in range(10):
            enrollmentSum = []
            for j in range(3):
                # If statement to deal with nan values
                if not np.isnan(data_3D_array[i, self.school_index, j]):
                    enrollmentSum.append(data_3D_array[i, self.school_index, j])
            # Print enrollment information by the year
            print("Total enrollment for " + enrollment_years[i] + ": " + str(np.sum(enrollmentSum).astype(np.int32)))
        
    """
    Calculates the total enrollment over the 10 eyars and returns it
    as a String (converted from a floored int32)
    """
    def get_total_10_year_enrollment(self):
        total_10_year_enrollment = 0
        # Loop through 10 years and 3 grades for the current school
        for i in range(10):
            enrollmentSum = []
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data_3D_array[i, self.school_index, j]):
                    enrollmentSum.append(data_3D_array[i, self.school_index, j])
            total_10_year_enrollment += np.sum(enrollmentSum)

        return str(total_10_year_enrollment.astype(np.int32))
    
    """
    Calculates the mean of the total enrollment over the 10 eyars and returns it
    as a String (converted from a floored int32)
    """
    def get_mean_10_year_enrollment(self):
        yearly_enrollment = []
        # Loop through 10 years and 3 grades for the current school
        for i in range(10):
            sum_of_grades_enrollment = 0
            for j in range(3):
                #If statement to deal with nan values
                if not np.isnan(data_3D_array[i, self.school_index, j]):
                    sum_of_grades_enrollment += data_3D_array[i, self.school_index, j]
            yearly_enrollment.append(sum_of_grades_enrollment)
        # Return the mean of the 10 year enrollment
        return str(np.mean(yearly_enrollment).astype(np.int32))
    
    """
    Creates a sub array for all the schools, conducts a masking operation
    to obtain a list of data points larger than 500, and prints the median value
    """
    def print_large_enrollment_median(self):
        #Sub array view for schools
        enrollment_data = data_3D_array[:, self.school_index, :]
        #Masking operation
        large_enrollments = enrollment_data[enrollment_data > 500]

        #Check if there are any large enrollments, over 500
        if len(large_enrollments) == 0:
            print("No enrollments over 500.")
        else:
            print("For all enrollments over 500, the median value was: " + str(np.median(large_enrollments).astype(np.int32)))

"""
Takes in a print message as a String, asks the user for an input with the message.
Checks to see if user input is valid, throws a ValueError on invalid input and 
asks the user to try again
Returns the sanitized user input
"""
def get_user_input(message):
    # Run loop until user enters valid input
    while True:
        try:
            # Get user input
            user_input = input(message)
            # Check if user input is valid
            if user_input in school_names:
                return user_input
            elif user_input in school_codes:
                return user_input
            elif user_input == "0":
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Invalid school name or code!")

"""
Takes in a year as a String and calculates the mean of the enrollment numbers
in that given year and returns it as a String (converted from a floored int32)
"""
def get_total_mean_by_year(year):
    enrollment_numbers = []
    # Loop through all the schools and grades and given year
    for i in range(20):
        for j in range(3):
            #If statement to deal with nan values
            if not np.isnan(data_3D_array[year, i, j]):
                enrollment_numbers.append(data_3D_array[year, i, j])
    #Convert return type to int32 for print() function
    return str(np.mean(enrollment_numbers).astype(np.int32))

"""
Takes in a year as a String and calculates the size of the graduating class (grade 12)
in that given year and returns it as a String (converted from a floored int32)
"""
def get_total_graduating_class_size(year):
    enrollment_numbers = []
    # Loop through all schools at given year for Grade 12
    for i in range(20):
        #If statement to deal with nan values
        if not np.isnan(data_3D_array[year, i, 2]):
            enrollment_numbers.append(data_3D_array[year, i, 2])
    #Convert return type to int32 for print() function
    return str(np.sum(enrollment_numbers).astype(np.int32))

"""
Calculates the highest enrollment value and returns it as a 
String (converted from a floored int32)
"""
def get_highest_enrollment_by_grade():
    highest_enrollment = 0

    #(year, school, grade) data_3D_array formatting
    #Loop through all 10 years of data
    for i in range(10):
        #Loop through all 20 schools
        for j in range(20):
            ##Loop through all 3 grades
            for k in range(3):
                if not np.isnan(data_3D_array[i, j, k]):
                    if data_3D_array[i, j, k] > highest_enrollment:
                        highest_enrollment = data_3D_array[i, j, k]
        
    return str(highest_enrollment.astype(np.int32))

"""
Calculates the lowest enrollment value and returns it as a 
String (converted from a floored int32)
"""
def get_lowest_enrollment_by_grade():
    #(year, school, grade) data_3D_array formatting
    #Initialize to very high number that will never be true
    lowest_enrollment = 999999

    #Loop through all 10 years of data
    for i in range(10):
        #Loop through all 20 schools
        for j in range(20):
            ##Loop through all 3 grades
            for k in range(3):
                if not np.isnan(data_3D_array[i, j, k]):
                    if data_3D_array[i, j, k] < lowest_enrollment:
                        lowest_enrollment = data_3D_array[i, j, k]
        
    return str(lowest_enrollment.astype(np.int32))
                
"""
main() function for printing data, creating objects, and running the program loop
"""
def main():
    print("\nENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array:", data_3D_array.shape)
    print("Dimensions of full data array", data_3D_array.ndim)

    #Loop to keep requesting information until user enters 0
    while True:
        # Prompt for user input
        user_input = get_user_input("\nPlease enter the high school name or school code (0 to exit program): ")
        if user_input == "0":
            break
        # Print Stage 2 requirements here
        print("\n***Requested School Statistics***\n")

        # Create school object to keep track of chosen school
        chosen_school = School()

        # Update chosen_school object by school code or name
        if user_input in school_codes:
            chosen_school.update_school_by_code(user_input)
        else:
            chosen_school.update_school_by_name(user_input)

        # Printing school name and code
        print("School Name: " + chosen_school.school_name + ", School Code: " + chosen_school.school_code)
        # Printing mean enrollment
        print("Mean enrollment for Grade 10:", chosen_school.get_mean_enrollment(0))
        print("Mean enrollment for Grade 11:", chosen_school.get_mean_enrollment(1))
        print("Mean enrollment for Grade 12:", chosen_school.get_mean_enrollment(2))
        # Printing highest enrollment
        print("Highest enrollment for a single grade:", chosen_school.get_highest_enrollment())
        # Printing lowest enrollment
        print("Lowest enrollment for a single grade:", chosen_school.get_lowest_enrollment())
        # Printing total enrollment for each year
        chosen_school.print_total_enrollments()
        # Printing total 10-year enrollment
        print("Total ten year enrollment: " + chosen_school.get_total_10_year_enrollment())
        # Printing mean total 10-year enrollment
        print("Mean total enrollment over 10 years: " + chosen_school.get_mean_10_year_enrollment())
        # Printing median of enrollments over 500
        chosen_school.print_large_enrollment_median()

        # Print Stage 3 requirements here
        print("\n***General Statistics for All Schools***\n")

        # Print mean enrollments for given years
        print("Mean enrollment in 2013: " + get_total_mean_by_year(enrollment_years.index("2013")))
        print("Mean enrollment in 2022: " + get_total_mean_by_year(enrollment_years.index("2022")))
        # Print graduating class numbers
        print("Total graduating class of 2022: " + get_total_graduating_class_size(enrollment_years.index("2022")))
        # Print highest and lowest enrollment for a single grade
        print("Highest enrollment for a single grade: " + get_highest_enrollment_by_grade())
        print("Lowest enrollment for a single grade: " + get_lowest_enrollment_by_grade())

        # Print end of data disclaimer
        print("\n***End of data***")


if __name__ == '__main__':
    main()
