import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
# print("The program is running")
# # This is a test to see if it pushes to GitHub
# print("Welcome to the Python Calculator\n\nWhat would you like to do?")
# choice = input()

print("SCHEDULE YOUR DAY! You're bored in the house. Let's make your day fun!")
print("Write your times in this format: 00:00 AM or PM")

## ASK USER QUESTIONS
start_time = input("When do you start your day? ").upper()
end_time = input("When do you end your day? ").upper()

choices = [
    {"activity": "", "duration": 0},
    # Append new activities here
]

times = [
    {"start time": start_time},
    {"end time": end_time}
]

## ADD AT LEAST ONE ACTIVITY

first_choice = input("What do you want to do first? Type A, B, C, or D:\nA. Exercise\nB. Arts & crafts\nC. Video games\nD. Other\n").upper()
if first_choice == "A":
    choices[0]["activity"] = "Exercise"
elif first_choice == "B":  
    choices[0]["activity"] = "Arts & crafts"
elif first_choice == "C":
    choices[0]["activity"] = "Video games"
else:
    choices[0]["activity"] = input("What activity do you want to do first? ")

first_duration = input("How long do you want to do this activity? Put your duration in minutes. ")
choices[0]["duration"] = first_duration

## ADD MORE ACTIVITIES UNTIL THE USER IS DONE

# Add one activity
def addActivity():

    # Add a dictionary to the list
    choices.append(dict(activity = "", duration = 0))

    # Define the activity
    user_activity = input("Type what activity you want to do: ")
    choices[len(choices)-1]["activity"] = user_activity

    # Define the duration
    user_duration = input("How long do you want to do this activity? Put your duration in minutes. ")
    choices[len(choices)-1]["duration"] = user_duration

# Output the schedule​
def showSchedule():
    print("Start your day at " + times[0]["start time"])

    for i in range(0, len(choices)):
        print(choices[i]["activity"].capitalize() + " for " + str(choices[i]["duration"]) + " minutes")

    print("End your day at " + times[len(times)-1]["end time"])

# Ask the user to confirm that they are done
def confirmDone(): 
    print("Thank you for scheduling your day with us! ")
    user_done = input("Are you done with your schedule? Type Y to confirm and see your finished schedule, and N to add another activity: ").upper()
    
    while user_done == "N":
        addActivity()

        # Ask the user to confirm that they are done, again
        user_done = input("Are you done with your schedule? Type Y to confirm and see your finished schedule, and N to add another activity: ").upper()

    else:
        showSchedule()

# Add multiple activities by using the addActivity() function when necessary
def addMultActivities():

    # Ask the user if they want to add a second activity
    continue_schedule = input("Do you want to add another activity? Type Y or N: ").upper()

    while continue_schedule == "Y":
        addActivity()
        
        # Ask the user if they want to add more activities
        continue_schedule = input("Do you want to add another activity? Type Y or N: ").upper()

    else:
        confirmDone()

# Call the function!
addMultActivities()