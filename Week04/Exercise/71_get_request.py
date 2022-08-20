import requests

def getAllData():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    return response.json()
print(getAllData())


def getSingleData(id):
    api_url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = requests.get(api_url)
    return response.json()
print(getSingleData(1))