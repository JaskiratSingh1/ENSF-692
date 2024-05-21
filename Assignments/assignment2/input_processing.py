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

    # This method updates the status variables of the class with the user inputs
    def update_status(self, obstacle_type, new_value): # You may decide how to implement the arguments for this function
        # If there is a light change
        if obstacle_type == "light":
            self.traffic_light_color = new_value
        # If there is a pedestrian change
        elif obstacle_type == "pedestrian":
            if new_value == "yes":
                self.pedestrian_is_detected = True
            elif new_value == "no":
                self.pedestrian_is_detected = False
        # If there is a vehicle change
        elif obstacle_type == "vehicle":
            if new_value == "yes":
                self.vehicle_is_detected = True
            elif new_value == "no":
                self.vehicle_is_detected = False


# The sensor object should be passed to this function to print the action message and current status
def print_message(self):
    # Print a message saying stop if there is a red light, pedestrian, or vehicle detected
    if self.pedestrian_is_detected or self.vehicle_is_detected or (self.traffic_light_color == "red"): 
        print("\nSTOP")
    # If the light is yellow then print a message saying caution
    elif self.traffic_light_color == "yellow":
        print("\nCAUTION")
    # If there are no threats detected then print proceed
    elif self.pedestrian_is_detected == False or self.vehicle_is_detected == False or (self.traffic_light_color == "green"): 
        print("\nPROCEED")

    # Print update status depending on a pedestrian or vehicle being present
    if self.pedestrian_is_detected:
        if self.vehicle_is_detected:
            # Pedestrian and vehicle present
            print("\nLight =", self.traffic_light_color, ", Pedestrian = yes", ", Vehicle = yes\n")
        else:
            # Pedestrian but not vehicle present
            print("\nLight =", self.traffic_light_color, ", Pedestrian = yes", ", Vehicle = no\n")
    else:
        if self.vehicle_is_detected:
            # Vehicle but not pedestrian present
            print("\nLight =", self.traffic_light_color, ", Pedestrian = no", ", Vehicle = yes\n")
        else:
            # Neither vehicle nor pedestrian present
            print("\nLight =", self.traffic_light_color, ", Pedestrian = no", ", Vehicle = no\n")


# This function is used to validate the user input and returns a valid input
def get_user_input(obstacle_type):
    # Lists of allowable inputs based on obstacle detected
    light_inputs = ["green", "yellow", "red"]
    pedestrian_vehical_inputs = ["yes", "no"]
    user_choice_inputs = ["1", "2", "3", "0"]

    # For obstacle input
    if obstacle_type == "input": 
        print("Are there changes detected in the vision input?")
        user_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

        # Check if user input is valid
        if user_input in user_choice_inputs:
            return user_input
        # If user input is invalid print a message
        else:
            print("You must select either 1, 2, 3, or 0.\n")
            return
    # For light changes
    if obstacle_type == "light":
        user_input = input("What change has been identified?: ")

        # Check if user input is valid
        if user_input in light_inputs:
            return user_input
        # If user input is invalid print a message
        else:
            print("Invalid vision change.")
            return
    # For pedestrian or vehicle changes
    elif obstacle_type == "pedestrian" or obstacle_type == "vehicle":
        user_input = input("What change has been identified?: ")

        # Check if user input is valid
        if user_input in pedestrian_vehical_inputs:
            return user_input
        # If user input is invalid print a message
        else:
            print("Invalid vision change.")
            return
    
    # This should never be printed
    print("Invalid obstacle selection")
    return

# Main program function
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    # Creating new Sensor object
    car_sensor = Sensor()
    # Initializing user choice variable to 1 for the while loop
    user_vision_change_input = ""
    # Valid user vision change inputs
    user_inputs = ["1", "2", "3", "0"]

    # Run loop until user enters "0"
    while user_vision_change_input != "0":
        # Ask the user for changes in vision input
        user_vision_change_input = get_user_input("input")

        # If there is a light change
        if user_vision_change_input == "1":
            # Get sanitized input with either "red", "green", or "yellow"
            user_light_input = get_user_input("light")
            # Update object status variables
            car_sensor.update_status(obstacle_type = "light", new_value = user_light_input)

        elif user_vision_change_input == "2":
            # Get sanitized input with either "yes" or "no"
            user_pedestrian_input = get_user_input("pedestrian")
            # Update object status variables
            car_sensor.update_status("pedestrian", user_pedestrian_input)

        elif user_vision_change_input == "3":
            # Get sanitized input with either "yes" or "no"
            user_vehicle_input = get_user_input("vehicle")
            # Update object status variables
            car_sensor.update_status("vehicle", user_vehicle_input)
        
        # Print update message if user input is valid
        if user_vision_change_input in user_inputs:
            print_message(car_sensor)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()


