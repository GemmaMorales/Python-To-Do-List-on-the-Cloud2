import json, requests
todos = []

def get_todos():
    global todos
    return todos

def add_one_task(chore):
    chore = {}
    chore.update({
        "label": title,
        "done": False
    })
    todos.append(chore)
    pass

def print_list():
    if todos != []:
        print("\nYour To Do List consists of:")
        count = 1
        for chore in todos:
            print("Task #" + str(count) + ": " + str(chore["label"]) + " -completed: " 
            + str(chore["done"]))
            count += 1
        pass
    else:
        print("The current list is empty...")
    pass

    # r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/hammycakes') 
    # r = r.json()
    # print(r)

def delete_task(number_to_delete):
    for things in range(len(todos)):
        if (int(number_to_delete)-1) == (int(things)):
            print("Task is being deleted from the list...")
            del todos[int(things)]
    pass

def initialize_todos():
    global todos
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/hammycakes') 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/hammycakes', data = []) 
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()

    
def save_todos():
    temp = json.dumps(todos)
    r = requests.put(url = 'https://assets.breatheco.de/apis/fake/todos/user/hammycakes', headers = {"Content-Type":"application/json"}, data = temp)
    print(r.json())
    print(r)
    pass
    # if r.status_code == 200:
    #     print("You have saved to the todos.")
    

def load_todos():
    r = requests.get("https://assets.breatheco.de/apis/fake/todos/user/hammycakes")
    todos = r.json() #or response
    print(todos) #or response
    pass
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What is the number of the task you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")