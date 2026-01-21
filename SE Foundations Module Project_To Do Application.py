task = []                                                   ##Global list to store tasks##

def display_welcome_message():                                      ##Greetings to welcome users and displays menu##
    """Displays a welcome message to the user."""
    welcome = " Welcome to the To-Do Application! "
    
    formatted_welcome = welcome.strip().upper()
    print("=" * 50)
    print(formatted_welcome)
    print("=" * 50)
    
def display_menu():                                                        ##Here's the menu options##
    """Displays the menu options to the user."""
    menu= """
    Please choose an option:
    1. Add a task
    2. View tasks
    3. Remove a task
    4. Exit
    """
    print(menu)
    
def get_valid_menu_choice():                                                ##User Interaction in a While loop to keep asking until valid input##
    """Gets a valid menu choice from the user."""
    while True:
        try:
            choice = input("Enter your choice (1-4): ")                         ##User puts in their choice##
            
            choice_num = int(choice)                                      ##Converts input to integer##     
            if choice_num >= 1 and choice_num <= 4:                     ##Conditional validation using comparison and logical operators##
                return choice_num                                           ##Exit function if valid input##
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")   ##Alerts the user if they provide invalid input##
        
        except ValueError:                                            ##Exception handling for non-integer inputs##                                            
            print("Invalid input. Please enter a number between 1 and 4.")
        finally:                                             ##Finally block to execute code regardless of exceptions##                                 
            pass
        
        
def add_task():                                                             ##Adding tasks to the list##
    """Adds a task to the task list."""
    try:
        task = input("Enter the task you want to add: ")                 ##Guiding User to input the task##   
        
        task = task.strip()                                        ##Stripping any leading/trailing whitespace##                    
        
        if len(task) == 0:                                        ##Conditional: Validating non-empty input##                    
            print("Task cannot be empty. Please try again.")
            return                                                              ##Exits function if input is invalid##
        task.append(task)                                    ##Appends the task to the global list (end of list)##                
        print(f'Task "{task}" added successfully.')                     ##Confirmation message to the user##
        
    except Exception as e:                                            ##General exception handling##
        print(f"An error occurred while adding the task: {e}")
        
        
def view_tasks():
    """Diaplay all tasks with formatting."""                       
    if len(task) == 0:                              ##Checks if the task list is empty##
        print("No tasks available.")                ##Alerts user if no tasks are present##
    else:
        print("No tasks to view!")
        print("Your to-do list is empty.")
        return
    
    print("n" + "=" * 50)
    print("Your To-Do List:")
    print("=" * 50)
    
    for index, task in enumerate(task, start=1):               ##Enumerate function to display task number (Starting with 1) alongside task##
        print(f"{index}. {task}")                               ##Formatted output of tasks (index number + task description)##
        
    print("=" * 50)
    print(f"Total tasks: {len(task)}")                  ##Displays total number of tasks##
    
    
def delete_task():                                      
    """Deletes a task from the task list."""
    if len(task) == 0:                            ##Checks if the task list is empty....see if there's anything to delete##  
        print("No tasks available to delete.")
        return
    
    view_tasks()                          ##Displays current tasks before deletion.....allows user to see what's available##        
    
    try:
        task_num = int(input("Enter the task number to delete: "))
            
        task_index = int(task_num)
        
        if task_index < 1 or task_index > len(task):        ##Validates if the task number is within range##
            print("Invalid task number. Please try again.")             ##Alerts user if task number is invalid##
            return
        
        deleting_task = task[task_index - 1]
        del tasks[task_index - 1]
        
        print(f'Task "{deleting_task}" deleted successfully.')
        
        
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
    except IndexError:
        print("Task number does not exist!")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")
        
        
def main():
    display_welcome_message()
    
    running = True

    while running:                                ##Main loop to keep the application running until user decides to exit##  
        display_menu()
        choice = get_valid_menu_choice()                     ##Gets the user's menu choice##
        
        if choice == 1:                                  ##If-elif-else structure for menu options##
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            running = quit_application()
        else:
            print("Invalid choice. Please try again.")          ##Alerts user if choice is invalid##
    
            
        print()
        

def quit_application():
    """Quits the application."""
    goodbye = "Thank you for using the To-Do Application. Goodbye!"         ##User enters 4 and exists with a message##
    print("n" + "=" * 50)
    print(goodbye.center(50))
    print("=" * 50)
    return True