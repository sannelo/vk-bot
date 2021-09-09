import asyncio
import datetime
import math
import os
import threading

from vkbottle import Keyboard, Text, KeyboardButtonColor, Callback, GroupTypes, GroupEventType
import json

from functions import get_profile, key_Board, read, xp_bar, cmd_send_money, stop_working, start_working, add_friend, \
    new_name
from msg_settings import *
from settings import *
from job_propertis import *

from threading import Thread
from typing import Optional

from langdetect import detect_langs

import pickle
import random
import time
import vkbottle
from vkbottle.bot import Bot, Message


def save(data, f_name='users'):
    with open(f'{f_name}.json', "w", encoding="utf-8") as file:
        file.write(json.dumps(data, sort_keys=True, indent=4))


def load(f_name='users'):
    if os.path.isfile(f'{f_name}.json'):
        print("Файл загружен!")
        with open(f'{f_name}.json', "r", encoding="utf-8") as file:
            tmp = json.load(file)
    else:
        print("Файл не найден!")
        tmp = {}
    return tmp


users = load()
api = vkbottle.API(token=token)


def register_user(_id, lng="ru"):
    if users.get(_id) is not None:
        return False
    users[_id] = {"id": _id,
                  "mod_lvl": 0,
                  "nick_name": f'nn_{random.randint(100000, 999999)}',
                  "balance": 0,
                  "lng": lng,
                  "my_lvl": 0,
                  "my_lvl_xp": 0.0,
                  "friends": [],
                  "where": 0,
                  "imWorking": False,
                  "job": None,
                  "time_js": None,
                  "bonuses": []
                  }
    return True


def saving():
    global _DEBUG
    while True:
        time.sleep(5)
        if _DEBUG:
            print("         DEBUG         ")
        else:
            save(users)


def backup():
    global _DEBUG
    while True:
        if _DEBUG:
            print("         DEBUG      BUp")
        else:
            ttime = datetime.datetime.today().strftime("%Y_%m_%d_%H-%M-%S")
            save(users, f"backup_{ttime}")
            os.rename(f"{os.getcwd()}\\backup_{ttime}.json", f"{os.getcwd()}\\backups\\backup_{ttime}.json")
        time.sleep(3600)


bot = Bot(token=token)

_DEBUG = False

start_time = 0.0

tk = Thread(target=saving)
tk.start()


# noinspection PyTypeChecker
@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def test_event(event: GroupTypes.MessageEvent):
    await bot.api.messages.send_message_event_answer(
        event_id=event.object.event_id,
        user_id=event.object.user_id,
        peer_id=event.object.peer_id,
        event_data=json.dumps({"type": "show_snackbar", "text": get_profile(event.object.user_id, "mini", users)}),
    )


@bot.on.message(payload_map={"menu_profile": str})
async def menu_profile(message: Message):
    global _DEBUG
    payload = message.get_payload_json()['menu_profile']

    my_id = str(message.from_id)
    lng = users[my_id]['lng']

    if payload == "get_profile":
        await message.answer(get_profile(my_id, local_users=users))
    if payload == "send_money":
        await message.answer(send_money_miss[lng])

    pass


@bot.on.message(payload_map={"menu": str})
async def menu_update(message: Message):
    global _DEBUG

    my_id = str(message.from_id)
    lng = users[my_id]['lng']
    payload = message.get_payload_json()['menu']

    if payload == "next":
        users[my_id]['where'] += 1
    if payload == "back":
        users[my_id]['where'] -= 1
    if payload == "update":
        users[my_id]['where'] = 0

    if users[my_id]['where'] == -1:
        users[my_id]['where'] = 4
    if users[my_id]['where'] == 5:
        users[my_id]['where'] = 0

    await message.answer(f"Menu ", keyboard=key_Board(lng,
                                                      users[my_id]['where'],
                                                      my_id))
    pass


@bot.on.message(text=menu)
async def start_msg(message: Message):
    my_id = message.from_id
    lng = users[my_id]['lng']

    menu_number = users[my_id]['where']

    await message.answer("Keyboard", keyboard=key_Board(lng, menu_number, my_id))


@bot.on.message(text=start_cmd)
async def start_msg(message: Message):
    lng = lngs[start_cmd.index(message.text)]

    if register_user(str(message.from_id), lng):
        await message.answer(reg_success[lng])
    else:
        await message.answer(reg_already[lng])


@bot.on.message(text="!<cmd> <cmd1> <cmd2>")
async def cmd_3(message: Message, cmd: Optional[str] = None,
                cmd1: Optional[str] = "1",
                cmd2: Optional[str] = "1"):
    await read(message.id, api)

    global _DEBUG, users

    my_id = str(message.from_id)
    lng = users[my_id]['lng']

    if users[my_id]['mod_lvl'] == 777:
        if cmd.lower() == "!money":
            try:
                users[int(cmd1)]['balance'] += int(cmd2)
            except:
                await message.answer(send_money_miss[lng])
        if cmd == "bar":
            await message.answer(xp_bar(int(cmd1), int(cmd2)))

    if cmd == set_nick[lng]:
        await new_name(message, local_users=users)

    if cmd.lower() == my_profile_friend_add[lng]:
        await message.answer(my_profile_friend_miss[lng])

    if cmd.lower() == send_money[lng]:
        try:
            if cmd_send_money(my_id, int(cmd1), int(cmd2), api):
                await message.answer(send_money_success[lng])
            else:
                await message.answer(send_money_err[lng])
        except:
            await message.answer(send_money_miss[lng])


@bot.on.message(text="!<cmd> <cmd1>")
async def cmd_2(message: Message,
                cmd: Optional[str] = "1",
                cmd1: Optional[str] = "1"):
    await read(message.id, api)

    global _DEBUG, users

    my_id = str(message.from_id)
    lng = users[my_id]['lng']

    if users[my_id]['mod_lvl'] == 777:
        if cmd.lower() == "info":
            await message.answer(get_profile(cmd1, local_users=users))

    if cmd.lower() == my_profile_friend_add[lng]:
        if cmd1 == str(message.from_id):
            await message.answer(my_profile_friend_err_self[lng])
            return
        if add_friend(my_id, str(cmd1), users):
            await message.answer(my_profile_friend_success[lng])
        else:
            await message.answer(my_profile_friend_err[lng])

    if cmd.lower() == job[lng]:
        if cmd1.lower() == job_stop[lng]:
            tmp_bool, tmp_money0, tmp_lvl0 = await stop_working(my_id, message, users)
            if tmp_bool:
                await message.answer(f"{job_success_stop[lng]}\n"
                                     f"{job_working_info_balance[lng]}: ${tmp_money0}$\n")
            else:
                await message.answer(job_info[lng])
            return

        if users[my_id]["imWorking"]:
            job_type = users[my_id]["job"]
            tmp_money = jobs[job_type]["money"] * math.floor(time.time() - users[my_id]["time_js"])

            tmp_msg = f"{job_miss[lng]}\n" \
                      f"{job_working_info_my_job[lng]}: {job_type}\n" \
                      f"{job_working_info_balance[lng]}: ${tmp_money}$\n" \
                      f"{job_stop_working[lng]}"

            await message.answer(tmp_msg)
            return

        try:
            jt = jobs[cmd1.lower()]
            jt = cmd1.lower()

            if start_working(my_id, jt, users):
                await message.answer(job_success_start[lng])
            else:
                await message.answer(job_miss[lng])
        except:
            await message.answer(job_info[lng])
        pass

    if cmd.lower() == my_profile[lng]:
        try:
            if my_id in users[str(cmd1)]['friends']:
                await message.answer(get_profile(cmd1, local_users=users))
            else:
                await message.answer(my_profile_err[lng])
        except:
            await message.answer(my_profile_miss[lng])

    if cmd.lower() == lng_command[lng]:
        if cmd1.lower() in lngs:
            users[my_id]['lng'] = cmd1.lower()
            await message.answer(lng_command_edited[users[my_id]['lng']])
        else:
            await message.answer(lng_command_miss[lng])

    if cmd.lower() == set_nick[lng]:  # СМЕНИТЬ ИМЯ ################
        await new_name(message, cmd1)

    if cmd.lower() == send_money[lng]:
        await message.answer(send_money_miss[lng])


@bot.on.message(text="!<cmd>")
async def cmd_1(message: Message, cmd: Optional[str] = None):
    await read(message.id, api)

    global _DEBUG, users

    my_id = str(message.from_id)
    lng = users[my_id]['lng']

    if users[my_id]['mod_lvl'] == 777:
        if cmd.lower() == "stop":
            save(users)
            await message.answer("Saved\n"
                                 "Stopped")
            quit(-1)
        elif cmd.lower() == "debug":
            _DEBUG = not _DEBUG
            await message.answer(f"DEBUG STATUS IS: {_DEBUG}")
        elif cmd.lower() == "save":
            save(users)
        elif cmd.lower() == "load":
            users = load()

    if cmd.lower() == my_profile[lng]:
        await message.answer(get_profile(my_id, local_users=users))

    if cmd.lower() == my_profile_friend_add[lng]:
        await message.answer(my_profile_friend_miss[lng])

    if cmd.lower() == lng_command[lng]:
        await message.answer(lng_command_miss[lng])

    if cmd.lower() == lng_command_list[lng]:
        tmp_msg = lng_command_list_out[lng]
        i = 1
        for lng in lngs:
            tmp_msg += f"\n{i}. {lng}"
            i += 1
        await message.answer(tmp_msg)

    if cmd.lower() == job[lng]:

        if users[my_id]["imWorking"]:
            job_type = users[my_id]["job"]
            tmp_money = jobs[job_type]["money"] * math.floor(time.time() - users[my_id]["time_js"])
            tmp_lvl = jobs[job_type]["lvl_add"] * math.floor(time.time() - users[my_id]["time_js"])

            tmp_msg = f"{job_miss[lng]}\n" \
                      f"{job_working_info_my_job[lng]}: {job_type}\n" \
                      f"{job_working_info_balance[lng]}: ${tmp_money}$\n" \
                      f"{job_working_info_lvl[lng]}: {tmp_lvl}\n" \
                      f"{job_stop_working[lng]}"

            await message.answer(tmp_msg)
            return

        tmp_msg = job_info[lng]

        tmp_msg += "\n" + job_list[lng]
        i = 1
        for _job in jobs_name:
            tmp_msg += f"\n{i}. {_job[lng]}\n" \
                       f"{job_money[lng]} - {jobs[_job['action']]['money']}\n" \
                       f"{job_code[lng]} - {_job['action']}" \
                       f"\n"
            i += 1
        await message.answer(tmp_msg)

    if cmd.lower() == send_money[lng]:
        await message.answer(send_money_miss[lng])

    if cmd.lower() == set_nick[lng]:
        await new_name(message, None)


@bot.on.message()
async def msg(message: Message):
    if users.get(str(message.from_id)) is None:
        await message.answer(reg)
        return
    else:
        with open("bonuses.json", "r", encoding='utf-8') as read_file:
            data = json.load(read_file)

        tmp_bonuses = data["bonuses"]
        tmp_money = data["money"]

        if message.text.lower() in tmp_bonuses:
            if message.text.lower() not in users[str(message.from_id)]["bonuses"]:
                users[str(message.from_id)]["balance"] += tmp_money[tmp_bonuses.index(message.text.lower())]
                users[str(message.from_id)]["bonuses"].append(message.text.lower())
                await message.answer(f"Вам успешно начислен бонус в размере "
                                     f"${tmp_money[tmp_bonuses.index(message.text.lower())]}$")
            else:
                await message.answer("Ты уже получил этот бонус, не выпендривайся!")
            return

    lng = users[str(message.from_id)]['lng']

    await message.answer(menu_using[lng])


tk0 = Thread(target=backup)
tk0.start()


asyncio.run(bot.run_forever())
