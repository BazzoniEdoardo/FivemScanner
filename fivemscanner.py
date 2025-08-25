import sys

from modules.ConnectionModule import ServerConnection
from modules.GuiModule import *
from modules.ResultsModule import *


def main():
    PrintLogo()

    if len(sys.argv) < 2:
        PrintTooFewArguments()
        return

    serverId = sys.argv[1]

    connection = ServerConnection(serverId)

    connection.RequestServerInfo()

    CreateResult(connection.jsonData, serverId)

    PrintSuccess(serverId)

if __name__ == '__main__':
    main()
