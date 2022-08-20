import requests

def patchData(selectedId, updatedTitle):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{selectedId}"
    todo = {"title": updatedTitle}
    response = requests.patch(api_url, json=todo)
    return response.json() 
print(patchData(3, "Have a kid"))