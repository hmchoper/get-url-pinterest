from py3pin import Pinterest

pinterest = Pinterest.Pinterest(
    email="<your email>",
    password="<your password>",
    username="<your username>",
)

pinterest.login()

boards = pinterest.boards(username="miraridoctor")

boardIds = list(map(lambda board: board["id"], boards))

pinUrls = []


def getPinUrls(boardId):
    pins = pinterest.board_feed(board_id=boardId)
    for pin in pins:
        pinUrls.append(f'https://pinterest.com/pin/{pin["id"]}/')


for boardId in boardIds:
    getPinUrls(boardId)

print(pinUrls)
