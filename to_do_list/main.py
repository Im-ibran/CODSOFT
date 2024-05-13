import datetime

#get info and task by user
user_name = None
user_email = None
password = None
to_do_items = []

def get_user_details():

    global user_name, user_email, password, password_cnfrm
    if not user_name or not user_email or not password or not password_cnfrm:
        print("Hi i am a to-do-list app to store your daily tasks \nAs you are new user")
        password = input("Set your password: ")
        password_cnfrm = input("Confirm your password: ")
        if password == password_cnfrm:
            user_name = input("Helo sir what is your name : ")
            user_email = input("What's your email address : ")
        else:
            print("Passwords do not match. Please try again.")


def show_details():
    #showing user details plus date/time
    today = datetime.date.today()
    now = datetime.datetime.now()
    print(f"Today's date: {today.strftime('%Y-%m-%d')}")
    formatted_time = now.strftime("%H:%M:%S")
    print(f"Current time: {formatted_time} ")
    print("My current user is " + str(user_name) + " \nHis Email is: " + str(user_email))


def add_task():
#this part gets tasks from current user
    new_task = input("Enter a new task: ")
    to_do_items.append(new_task)
    print(f"{new_task} added to the to-do list!")


def list_tasks():
#this part prints tasks and that numb will show numbers in sequence and there
    if not to_do_items:
        print("There are no tasks in the list.")
    else:
        print("Current tasks:")
        show_details()  # Display current date/time before listing tasks
        for numb, task in enumerate(to_do_items, start=1): #enumerate iterates through the to do tasks list and returns an enumerate object
            print(f"{numb}. {task}")


def mark_task_done():
#this is so that current user can remore done tasks from list
    if not to_do_items:
        print("There are no tasks to mark as done.")
        return

    list_tasks()  # Display the list for reference
    try:
        task_number = int(input("Enter the number of the task to mark as done: "))
        task_to_remove = to_do_items[task_number - 1]  # Access the task based on user input
        to_do_items.remove(task_to_remove)
        print(f"{task_to_remove} marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")


def delete_user():
    #now here after selecting to erase user it will confirm erase and ask for pass if incorrect it will return to menu and cancel everything
    global user_name, user_email, password, to_do_items
    confirmation = input("Are you sure you want to delete your user information and tasks? (y/n): ")
    if confirmation.lower() == 'y':
        password_entered = input("Enter your password to confirm deletion: ")
        if password_entered == password:
            user_name = None
            user_email = None
            password = None
            to_do_items = []
            print("User details and tasks erased successfully.")
        else:
            print("Password was wrong. ERASE cancel")
    else:
        print("Erase cancel.")
def main():
#this is main program that will run in loop after setting current user
    while True:
        get_user_details()  # Get user details if not already provided
        print("\nTo-Do List App")
        print("1. Add a task in your to do list")
        print("2. Show all the tasks/user_info/date_time")
        print("3. Mark a task as done")
        print("4. Delete user information and tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Closing the App")
            break
        else:
            print("choice was invalid so Please try again.")


if __name__ == "__main__":
    main()
#It ensures that the code within the if block is only executed when the script is run directly

