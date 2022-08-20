import requests

def updateData(selectedId, updatedId, updatedTitle, updatedCompleted):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{selectedId}"
    todo = {"userId": updatedId, "title": updatedTitle, "completed": updatedCompleted}
    response = requests.put(api_url, json=todo)
    if (response.status_code == 204):
        print("data successfully updated")
        return response.json()
print(updateData(3,10, "Take a shower", False))

# update = put