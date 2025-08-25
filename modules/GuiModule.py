def PrintLogo():
    print(r"""
___________.__                         _________                                         
\_   _____/|__|__  __ ____   _____    /   _____/ ____ _____    ____   ____   ____________ 
 |    __)  |  \  \/ // __ \ /     \   \_____  \_/ ___\\__  \  /    \ /    \_/ __ \_  __  |
 |     \   |  |\   /\  ___/|  Y Y  \  /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
 \___  /   |__| \_/  \___  >__|_|  / /_______  /\___  >____  /___|  /___|  /\___  >__|   
     \/                  \/      \/          \/     \/     \/     \/     \/     \/     
    """)

def PrintSuccess(id):
    print(f"[Success] Success! File saved at: \"results/{id}")

def PrintError(status):
    print(f"[Error] Error while connecting to server: \"{status}\"")

def PrintTooFewArguments():
    print("[Error] You need to specify the server id!")