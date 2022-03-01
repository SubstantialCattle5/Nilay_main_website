import json

data = dict()

keys = ('AMAZON_BOOK_PRICE_WEBSITE', 'COOKIE_CLICKER_BOT', 'Pomodoro_Timer', 'TURTLE_CROSSING', 'Flight Price Checker'
        , 'PASSWORD MANAGER')

values = ('A website which mails the user when a selected book is cheaper.',
          'A script created to automate the cookie clicker game.', 'Timer for people following the Pomodoro Technique',
          'This is a Mini-Game in Python based on OOPs and the Turtle module . The goal of this game is to help a turtle to cross the street.'
          ,
          'It is a program created to check the prices of flight for next 6 months from Mumbai to pre-determined locations.',
          'GUI application to store, search and create passwords for the user')

images = ('amazon_book.png', 'cookie.png', 'PomodoroTimer.png', 'turtle.png', 'mail.png', 'PasswordManager.png')
for key, value, image in zip(keys, values, images):
    data[key] = [ '../static/images/' + image, value]

with open('data.json' , 'w') as file :
        json.dump( data , file , indent = 4 )
