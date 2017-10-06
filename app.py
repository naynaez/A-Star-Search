from graphics import *
from getdata import *
import A_star as aStarModule

WINDOW_WIDTH, WINDOW_HEIGHT = 921, 663

win = GraphWin("Welcome to Romania's shortest path finder (by EZY-AI)", WINDOW_WIDTH, WINDOW_HEIGHT)

def buttons():
    quit = Rectangle(Point(870, 605), Point(900, 635))   # Create exit button
    quit.setFill("yellow")
    text = Text(Point(885, 620), "Exit")
    quit.draw(win)
    text.draw(win)

    clear = Rectangle(Point(815, 605), Point(855, 635))   # Create clear button
    clear.setFill("yellow")
    text = Text(Point(835, 620), "Clear")
    clear.draw(win)
    text.draw(win)

    cityButton = []     # Create city button
    for i in range(20):
        cityButton.append(Rectangle(Point(citycoord[i][0],citycoord[i][1]), Point(citycoord[i][0] + 20,citycoord[i][1] + 20)))
        cityButton[i].setFill("red")
        cityButton[i].draw(win)

    return cityButton , quit , clear

def drawLine(resultList):
    m = range(len(resultList))
    for i in m:
        if i == len(resultList)-1:
            break
        else :
            #line = Line(pt, Point(150, 100))
            line = Line(Point(citycoord[resultList[i]][0]+10,citycoord[resultList[i]][1]+10)
                       ,Point(citycoord[resultList[i+1]][0]+10,citycoord[resultList[i+1]][1]+10))
            line.setOutline('yellow')
            line.setWidth(3)
            line.draw(win)
    return line
#def clearLine():


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def getCity(clickPoint,text,isExit,isClear):
    city = 20
    isSelected = True

    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.setText("")
        isClear = False
    elif inside(clickPoint, quit):
        isExit = True
    elif inside(clickPoint, clear):
        isClear = True
        text.setText('<< Clear >>')
    else:
        for i in range(20) :
            if inside(clickPoint, cityButton[i]):
                city = i
                break
        isClear = False
    if city >= 20 :
        city = 20
        isSelected = False

    text.setText(cityName[city])
    if(city <= 19):
        cityButton[city].setFill("yellow")

    return isSelected , isExit , city , isClear

startCityNum = 0                ## use in algorithm
destCityNum = 0
resultList = [0,1,2,3,4,5,6]


background = Image(Point(460,281), "map-label-bg.png")
background.draw(win)

cityButton , quit , clear = buttons()

startCityText = Text(Point(60,640), "None")
startCityText.setStyle('italic')
startCityText.draw(win)
destCityText = Text(Point(180,640), "None")
destCityText.setStyle('italic')
destCityText.draw(win)

resultText = Text(Point(600,640),'')
resultText.draw(win)
text = Text(Point(210, 610), "Start city         Destination city                      Result")
text.setStyle('bold')
text.draw(win)
tempText = Text(Point(0,0),"")

isStartSelected = False
isDestSelected = False
isExit = False
isClear = False
while not isExit :
    clickPoint = win.getMouse()
    _ , isExit , _ , isClear = getCity(clickPoint,tempText,isExit,isClear)
    if isClear:
            isStartSelected = False
            isDestSelected = False
            startCityText.setText('None')
            destCityText.setText('None')
            resultText.setText(' ')
            isClear = False
            for i in range(20):
                cityButton[i].setFill("red")
    elif not isStartSelected :
        isStartSelected , isExit , startCityNum , isClear = getCity(clickPoint,startCityText,isExit,isClear)
    elif not isDestSelected :
        isDestSelected , isExit , destCityNum , isClear = getCity(clickPoint,destCityText,isExit,isClear)
        resultText.setText("Click Anywhere")
    else :
        print ('>>>> Start algorithm <<<<')
        resultText.setText("Please wait ...")
        ############### Algorithm ##################
        resultList = aStarModule.A_starSearch(heuristic,startCityNum,destCityNum);
        ############################################
        resultText.setText('Path   ' + ','.join(str(p) for p in resultList ) + '   is the best way !!')
        #drawLine(resultList)
        print ('<<<< Finished >>>>')

win.close()
