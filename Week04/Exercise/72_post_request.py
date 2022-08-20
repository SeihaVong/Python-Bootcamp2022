import requests

def insertData(id, title, completed):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": id, "title": title, "completed": completed}
    response = requests.post(api_url, json=todo)
    if (response.status_code == 201):
        print("data added")
        return response.json()
print(insertData(2, "Fix the bugs", False))