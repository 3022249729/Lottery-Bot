import requests
from bs4 import BeautifulSoup


def powerGetWinnerBackup():
    winBalls = []
    response = requests.get('https://www.powerball.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    whiteBalls = soup.find_all('div', class_='form-control col white-balls item-powerball')
    pBall = soup.find('div', class_='form-control col powerball item-powerball')
    for ball in whiteBalls:
        if (len(winBalls) != 5):
            winBalls.append(int(ball.text))
        else:
            break
    powerBall = int(pBall.text)
    return winBalls, powerBall
# backup getter from powerball.com


def powerGetWinner():
    powerInfo = {}
    winBalls = []
    response = requests.get('https://www.nylottery.org/powerball/results')
    soup = BeautifulSoup(response.content, 'html.parser')
    whiteBalls = soup.find_all('span', class_='resultBall ball')
    powerBall = soup.find('span', class_='resultBall powerball')
    date = soup.find_all('a', href=True)
    multiplier = soup.find('div', class_='power-play')
    # get html elements

    for d in date:
        if ('/powerball/results/' in str(d)):
            date = d.text
            break
    powerInfo['date'] = date
    # get newest date

    for ball in whiteBalls:
        if (len(winBalls) != 5):
            winBalls.append(int(ball.text))
        else:
            break
    powerInfo['whiteBalls'] = winBalls
    powerInfo['redBall'] = int(powerBall.text)
    # get newest winning balls and power ball

    powerInfo['multiplier'] = multiplier.text[-1]
    return powerInfo
    # get multiplier



