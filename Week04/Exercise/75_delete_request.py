import requests 

def deleteData(selectedId):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{selectedId}"
    response = requests.delete(api_url)
    return response.json()
print(deleteData(3))
