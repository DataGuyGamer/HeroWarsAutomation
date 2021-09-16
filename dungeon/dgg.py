import random

num = random.randrange(1, 2)

while 1==1:    
    num = random.randrange(1, 2)
    try:
        click("1631820008449.png")
        wait(1)
        click("1631820057573.png")
        wait(15)
    except FindFailed:
        wait(1)
    except Exception:
        wait(1)
    try:
        click("1631818885828.png")
        wait(num)
        click("1631818244820.png")
        wait(2)        
        click("1631818334194.png")
        wait(2)
        click("1631818547458.png") 
        click("1631818557366.png")
        wait(20)
        click("1631819668778.png")
    except FindFailed:
        try:
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