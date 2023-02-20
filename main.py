import time
import os
import sys

def open_resource(url):
    """Open the specified URL in the default web browser."""
    os.system(f'start {url}')

def track_time(duration):
    """Track the time spent on learning and pause for the specified duration."""
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= duration:
            break
        time.sleep(1)

def learn_c():
    """Main function to help learn C programming."""
    print("Welcome to your C programming learning session!")
    print("We will provide you with helpful resources and track your progress.")
    print("You will learn more effectively if you stay focused and take breaks when needed.")
    print("You have 1 week (7 days) to complete the learning session.")
    
    # Set the total duration of the learning session
    total_duration = 604800  # 1 week in seconds
    
    # Track the time spent on each task
    time_per_task = total_duration / 6
    
    # Set up progress tracker
    start_time = time.time()
    tasks_completed = 0
    time_remaining = total_duration
    
    # Loop through the tasks
    while tasks_completed < 6:
        # Open the resource for the current task
        if tasks_completed == 0:
            open_resource("https://www.learn-c.org/")
        elif tasks_completed == 1:
            open_resource("https://www.tutorialspoint.com/cprogramming/")
        elif tasks_completed == 2:
            open_resource("https://www.geeksforgeeks.org/c-programming-language/")
        elif tasks_completed == 3:
            open_resource("https://www.programiz.com/c-programming")
        elif tasks_completed == 4:
            open_resource("https://www.cplusplus.com/doc/tutorial/")
        elif tasks_completed == 5:
            open_resource("https://stackoverflow.com/questions/tagged/c")
        
        # Track the time spent on the current task
        time_left = time_per_task
        while time_left > 0:
            time_left = max(0, time_left - 1)
            time_elapsed = time.time() - start_time
            time_remaining = total_duration - time_elapsed
            percentage_complete = tasks_completed * 100 / 6
            print(f"Task {tasks_completed+1} in progress. {percentage_complete}% of the session complete. Time remaining: {int(time_remaining)} seconds.")
            
                    # Allow the user to pause or end the learning session
        if time_remaining > 0:
            choice = input("Enter 'p' to pause, 'e' to end, or any other key to continue: ")
            if choice.lower() == 'p':
                pause_duration = int(input("How many minutes would you like to pause for? "))
                track_time(pause_duration * 60)
            elif choice.lower() == 'e':
                print("Goodbye!")
                sys.exit()
        
        time.sleep(1)
    
    # Update the progress tracker
    tasks_completed += 1
    time_elapsed = time.time() - start_time
    time_remaining = total_duration - time_elapsed
    percentage_complete = tasks_completed * 100 / 6
    print(f"Task {tasks_completed} complete. {percentage_complete}% of the session complete. Time remaining: {int(time_remaining)} seconds.")
    
    # Display a motivational message every 10 minutes
    if tasks_completed < 6 and time_elapsed % 600 == 0:
        print("Keep up the good work!")
    
    # Offer a rest after every 2 tasks completed
    if tasks_completed % 2 == 0 and tasks_completed < 6:
        rest_duration = int(input("You've completed 2 tasks. How many minutes would you like to rest for? "))
        track_time(rest_duration * 60)

# Congratulate the user on completing the learning session
print("Congratulations on finishing the C programming learning session!")
print("You should now have a good foundation in C programming and be ready to tackle more advanced topics.")
print("Don't forget to practice what you've learned and continue to seek out new resources to expand your knowledge.")
if __name__ == '__main__':
    learn_c()
