import os
import json

def CreateRawResultFile(jsonData, id):
    with open("results/" + id + "/RawData.json", "w", encoding="utf-8") as file:
        json.dump(jsonData, file, indent=4)

def CreatePlayerListFile(jsonData, id):
    with open("results/" + id + "/PlayerListData.json", "w", encoding="utf-8") as file:
        json.dump(jsonData, file, indent=4)

def CreateResourceListFile(jsonData, id):
    with open("results/" + id + "/ResourceListData.json", "w", encoding="utf-8") as file:
        json.dump(jsonData, file, indent=4)

def CreateServerInfoFile(jsonData, id):
    with open("results/" + id + "/ServerInfoData.json", "w", encoding="utf-8") as file:
        json.dump(jsonData, file, indent=4)

def CreateServerVars(jsonData, id):
    with open("results/" + id + "/VarsData.json", "w", encoding="utf-8") as file:
        json.dump(jsonData, file, indent=4)

def CreateResult(jsonData, id):
    CreateResultFolder(id)

    CreateRawResultFile(jsonData, id)
    CreatePlayerListFile(jsonData["Data"]["players"], id)
    CreateResourceListFile(jsonData["Data"]["resources"], id)
    CreateServerInfoFile(jsonData["Data"]["server"], id)
    CreateServerVars(jsonData["Data"]["vars"], id)

def CreateResultFolder(id):
    os.makedirs("results/" + id, exist_ok=True)