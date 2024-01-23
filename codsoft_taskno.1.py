# HERE'S A WALKTHROUGH TO MY ENTIRE WORKFLOW :
# https://www.youtube.com/watch?v=OBU1-VIOwTQ&t=25s&ab_channel=DebjitMahato

import os

# okay so first create a class for the list
class ToDoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = [] # this list will be maintained inside the program
        self.load_from_file() # this function will load any previously saved progress

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    description, status = line.strip().split(',')
                    task = {
                        'description': description,
                        'status': status == 'True' # as True/False will be string, not boolean inside the file
                    } # I will create a task as a dictionary with two keys: description and status
                    self.tasks.append(task)
            print(f'Saved version loaded from {self.filename}')
        except FileNotFoundError:
            print('\nNo previously saved versions found. Starting an empty To Do List \n')

    def add_task(self, description):
        task = {
            'description': description,
            'status': False 
        }
        self.tasks.append(task)
        self.save_to_file() # maintaining and saving the progress in the text file
        print(f'task \'{description}\' added successfully to the To Do list\n')

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                line = f'{task['description']},{task['status']}\n'
                file.write(line)

    # now lets create the display function
    def display_tasks(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n~~:To Do List:~~")

        # the tasks should be categorized into pending and completed ones
        pending_tasks = [task for task in self.tasks if not task['status']]
        completed_tasks = [task for task in self.tasks if  task['status']]

        # we have to first check if the list is empty or not
        if not pending_tasks and not completed_tasks:
            print('\nNo tasks available currently!')

        else:
            print('\nPending tasks--')
            for i, task in enumerate(pending_tasks, 1): # as pending_tasks is an iterable, I'm adding a counter to it while printing for task indexing
                print(f'{i}. {task['description']} [TO-DO]')

            print('\nCompleted tasks--')
            for i, task in enumerate(completed_tasks, 1):
                print(f'{i}. {task['description']} [DONE]')
        print('-----------------------------------')


    def mark_as_done(self, task_index): # the task index will be given as input(1st indexed) and we will mark it as completed/done
        # as we can only mark pending tasks as done, first separate the uncompleted/pending tasks
        pending_tasks = [task for task in self.tasks if not task['status']]

        if 1 <= task_index <= len(pending_tasks):
            task = pending_tasks[task_index-1]
            task['status'] = True
            self.save_to_file()
            print(f'task {task['description']} marked as done')
        
        else:
            print('\nInvalid task index')

    def remove_task(self, task_type, task_index):
        if task_type == 1:
            pending_tasks = [task for task in self.tasks if not task['status']]
            if 1 <= task_index <= len(pending_tasks):
                task = pending_tasks[task_index-1]
                self.tasks.remove(task)
                print(f'\ntask {task["description"]} removed from list successfully')
            else:
                print('\nInvalid task index')
        elif task_type == 2:
            completed_tasks = [task for task in self.tasks if task['status']]
            if 1 <= task_index <= len(completed_tasks):
                task = completed_tasks[task_index-1]
                self.tasks.remove(task)
                print(f'\ntask {task["description"]} removed from list successfully')
            else:
                print('\nInvalid task index')
        else:
            print('\nInvalid choice')
        self.save_to_file()

    # I think the class is completed, now lets create the main function

def main():
    toDoList = ToDoList()

    while True:
        toDoList.display_tasks()
        print('\n1. Add new task \n2. Remove a task \n3. Mark task as done \n4. Quit')
        choice = input('please enter your choice (1/2/3/4): ')

        # this should look a lot cleaner
        if choice == '1':
            description = input('\nplease enter task description: ')
            toDoList.add_task(description)
        elif choice == '2':
            print('\nDo you wanna remove from: \n1. Pending tasks \n2. Completed tasks')
            task_type = int(input('choose the type: '))
            task_index = int(input('enter the task index to remove: '))
            toDoList.remove_task(task_type, task_index)
        elif choice == '3':
            task_index = int(input('\nenter the task index to mark it as done: '))
            toDoList.mark_as_done(task_index)
        elif choice == '4':
            print('Exiting the program. Goodbye!\n')
            break
        else:
            print('\nPlease enter a valid choice!')
    
if __name__ == "__main__":
    main()
