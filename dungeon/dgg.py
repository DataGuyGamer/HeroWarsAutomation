import random

# https://github.com/DataGuyGamer/HeroWarsAutomation

num = random.randrange(1, 2)

#keep going through dungeons levels repeatedly
while 1==1:    
    num = random.randrange(1, 2)
    try:
        # click activate button... put screenshot for activate here
        click("1631820008449.png")
        wait(1)
        # click on collect to get the gold for each 10 level
        click("1631820057573.png")
        wait(15)
    except FindFailed:
        wait(1)
    except Exception:
        wait(1)
    try:
        # click on the battle icon
        click("1631818885828.png")
        wait(num)
        #click on attack icon
        click("1631818244820.png")
        wait(2)       
        # click on to-battle icon
        click("1631818334194.png")
        wait(2)
        # click on auto and speed up buttons
        click("1631818547458.png") 
        click("1631818557366.png")
        wait(20)
        #once mission is done click ok
        click("1631819668778.png")
    except FindFailed:
        try:
            # for some scenarios we may start from to-battle
            # add relevant screenshots here
            click("1631818334194.png")            
            wait(2)
            click("1631818547458.png")
            click("1631818557366.png")
            wait(20)
            click("1631819668778.png")
        except FindFailed:
            click("1631818547458.png")
            click("1631818557366.png") 
            wait(20)
            click("1631819668778.png")
    except SikuliException: 
        wait(2)
    except Exception:
        num = random.randrange(1, 2)
        wait(2)
