import requests
import re
from bs4 import BeautifulSoup



def megaGetWinner():
    megaInfo = {}
    winBalls = []
    response = requests.get('https://www.nylottery.org/mega-millions/results')
    soup = BeautifulSoup(response.content, 'html.parser')
    whiteBalls = soup.find_all('span', class_='resultBall ball')
    megaBall = soup.find('span', class_='resultBall mega-ball')
    date = soup.find_all('a', href = True)
    multiplier = soup.find('div', class_='megaplier')
    #get html elements

    for d in date:
        if('/mega-millions/results/' in str(d)):
            date = d.text
            break
    megaInfo['date'] = date
    #get newest date

    for ball in whiteBalls:
        if (len(winBalls) != 5):
            winBalls.append(int(ball.text))
        else:
            break
    megaInfo['whiteBalls'] = winBalls
    megaInfo['redBall'] = int(megaBall.text)
    #get newest winning balls and mega ball

    megaInfo['multiplier'] = multiplier.text[-1]
    return megaInfo
    #get multiplier



