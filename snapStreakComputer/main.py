import pyautogui as pag

def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence=0.7)
        if position is None:
            print(f'{image} not found on screen')
            return None
        else:
            x = position[0] / 2
            y = position[1] / 2
            if image != "quit1.png":
                return x,y
            else:
                return x - 22, y - 22

    except OSError as e:
        print(f'there is no such file as {image}')
        raise Exception(e)

def click(image: str):
    position = get_position(image)
    pag.moveTo(position, duration=0.2)
    pag.click(position)

if __name__ == '__main__':

    # 1- open SNAPCHAT
    click("app.png")
    pag.sleep(15)

    # 2- click snap button twice
    try:
        click("snap2.png")
    except pag.ImageNotFoundException:
        try:
            click("snap1.png")
            pag.sleep(6)
            click("snap2.png")
        except pag.ImageNotFoundException:
            click("snap2.png")

    pag.sleep(0.15)

    # -- text --
    click("text.png")
    pag.write("this is a snap from my computer machine !")
    pag.sleep(0.2)

    # 3- click 'send to' button
    click("sendTo.png")
    pag.sleep(0.5)

    # 4- click 'shortcut' icon
    click("shortcut.png")
    pag.sleep(0.3)

    # 5- click on users
    try:
        while (True):
            click("block.png")
    except Exception:
        print("user")

    # 5- SEND
    #click("finalSend.png")

    # 6- close SNAPCHAT
    pag.moveTo(get_position("quit1.png"), duration=0.2)
    pag.click(get_position("quit1.png"))