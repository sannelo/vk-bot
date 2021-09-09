import os
import json
import random
import string
import time
from threading import Thread

from PIL import Image
from claptcha import Claptcha
from flask import Flask, render_template, request
from pyngrok import ngrok


def randomString():
    return "".join((random.choice(string.ascii_uppercase) for _ in range(8)))


c = Claptcha(randomString, "fonts/Inkfree.ttf",
             resample=Image.BICUBIC, noise=0.3)

ng = None
app = Flask(__name__)
# ngrok.connect(5000, "http")
# print(ng.public_url)


def save(data, f_name='users'):
    with open(f'{f_name}.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(data, sort_keys=True, indent=4))


def load(f_name='users'):
    if os.path.isfile(f'{f_name}.json'):
        with open(f'{f_name}.json', "r", encoding="utf-8") as file:
            tmp = json.load(file)
    else:
        tmp = {}
    return tmp


capha_list = {}
hack_list = load("hacks")


@app.route('/')
def quiz_index():
    return 404


@app.route('/<user_id>')
def quiz_id(user_id):
    users = load()
    if users.get(str(user_id)) is not None:
        if user_id not in capha_list.keys():
            text, _ = c.write(f"static/{user_id}.png")
            capha_list[user_id] = text
        return render_template('index.html', content=f"static/{user_id}.png")
    else:
        return "User not found ERROR 404", 404


@app.route('/<user_id>/hack', methods=['POST'])
def quiz_answers(user_id):
    if request.form is None:
        return "Не верный запрос"

    if request.form['captcha'].lower() == capha_list[user_id].lower():
        my_id = request.form['user_id']
        if hack_list.get(my_id) is not None:
            if hack_list[my_id].get(user_id) is not None:
                hack_list[my_id][user_id] += random.randrange(100, 1000, random.randrange(13, 50, 2))
            else:
                hack_list[my_id] = {}
                hack_list[my_id][user_id] = random.randrange(100, 1000, random.randrange(13, 50, 2))
        else:
            hack_list[my_id] = {}
            hack_list[my_id][user_id] = random.randrange(100, 1000, random.randrange(13, 50, 2))

        del capha_list[user_id]
        os.remove(f"{os.getcwd()}\\static\\{user_id}.png")
        return render_template('password.html', tile="Решена успешно!",
                               link=f"2;{ng.public_url if ng is not None else 'http://192.168.0.107:5000'}/{user_id}")
    else:
        del capha_list[user_id]
        os.remove(f"{os.getcwd()}\\static\\{user_id}.png")
        return "Не верное значение!"


def saving():
    while True:
        time.sleep(5)
        save(hack_list, "hacks")


tk = Thread(target=saving)
tk.start()

app.debug = False
app.run(host='0.0.0.0')
print("Flask started")
