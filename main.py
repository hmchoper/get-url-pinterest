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

# write to file
with open("pinUrls.csv", "w") as file:
    # write headers
    file.write("Pin URLs\n")
    for url in pinUrls:
        file.write(url + "\n")
print("File saved successfully")



print(pinUrls)
