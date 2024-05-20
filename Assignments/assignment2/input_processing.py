# input_processing.py
# JASKIRAT SINGH [JAZZ], ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.traffic_light_color = "green"
        self.pedestrian_is_detected = False
        self.vehicle_is_detected = False

    # Replace these comments with your function commenting
    def update_status(self, obstacle_type, new_value): # You may decide how to implement the arguments for this function
        if obstacle_type == "light":
            self.traffic_light_color = new_value
        elif obstacle_type == "pedestrian":
            if new_value == "yes":
                self.pedestrian_is_detected = True
            elif new_value == "no":
                self.pedestrian_is_detected = False
        elif obstacle_type == "vehicle":
            if new_value == "yes":
                self.pedestrian_is_detected = True
            elif new_value == "no":
                self.pedestrian_is_detected = False


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(self):
    #Print a message saying stop if there is a red light, pedestrian, or vehicle detected
    if self.pedestrian_is_detected or self.vehicle_is_detected or (self.traffic_light_color == "red"): 
        print("\nSTOP\n")
    #If the light is yellow then print a message saying caution
    elif self.traffic_light_color == "yellow":
        print("\nCAUTION\n")

    if self.pedestrian_is_detected:
        if self.vehicle_is_detected:
            print("Light =", self.traffic_light_color, ", Pedestrian = yes", ", Vehicle = yes\n")
        else:
            print("Light =", self.traffic_light_color, ", Pedestrian = yes", ", Vehicle = no\n")
    else:
        if self.vehicle_is_detected:
            print("Light =", self.traffic_light_color, ", Pedestrian = no", ", Vehicle = yes\n")
        else:
            print("Light =", self.traffic_light_color, ", Pedestrian = no", ", Vehicle = no\n")


        


# This function is used to validate the user input and returns True if the input is valid
# The function takes the user input and a set of allowable inputs
def validate_user_input(user_input):
    
    return False

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    # Creating new Sensor object
    car_sensor = Sensor()
    # Initializing user choice variable to 1 for the while loop
    user_vision_change_input = ""

    while user_vision_change_input != "0":
        # Ask the user for changes in vision input
        print("Are there changes detected in the vision input?")
        user_vision_change_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

        # If there is a light change
        if user_vision_change_input == "1":
            user_light_input = input("What change has been identified?: ")
            # Sanitize data with red green yellow
            car_sensor.update_status(obstacle_type = "light", new_value = user_light_input)

        elif user_vision_change_input == "2":
            user_pedestrian_input = input("What change has been identified?: ")
            # Sanitize data with true or false
            car_sensor.update_status("pedestrian", user_pedestrian_input)

        elif user_vision_change_input == "3":
            user_vehicle_input = input("What change has been identified?: ")
            # Sanitize data with true or false
            car_sensor.update_status("vehicle", user_vehicle_input)
        
        print_message(car_sensor)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()


