import datetime
import math
import time
from typing import Optional

from vkbottle.bot import Message
from vkbottle import Keyboard, Text, KeyboardButtonColor, Callback, GroupTypes, GroupEventType

# import main
from job_propertis import *
from msg_settings import *


# noinspection DuplicatedCode
def time_format(_time):
    tmp_str = ""
    ttmp = datetime.datetime.fromtimestamp(_time).strftime(':%M:%S')
    dtmp = int(datetime.datetime.fromtimestamp(_time).strftime('%d'))
    htmp = int(datetime.datetime.fromtimestamp(_time).strftime('%H'))

    tmp_str += f"{(dtmp * 24) + htmp}"
    tmp_str += ttmp

    return tmp_str


async def read(msg_id, local_api):
    await local_api.request("messages.markAsRead", {'message_ids': msg_id, 'v': '5.21'})


# noinspection PyBroadException
async def get_name(_id, i=0, api=None):
    try:
        tmp = await api.request('users.get', {'user_ids': _id})
        if i == 0:
            return [tmp[0]['first_name'], tmp[0]['last_name']]
        elif i == 1:
            return tmp[0]['first_name'] + " " + tmp[0]['last_name']
    except:
        return False


def add_friend(id_my, id_friend, local_users):
    if local_users.get(str(id_friend)) is not None:
        if id_my in local_users[str(id_my)]["friends"]:
            return True
        local_users[str(id_my)]["friends"].append(id_friend)
        # main.users = local_users
        return True
    else:
        return False


def key_Board(lng, menu_number, _id) -> Optional[str]:
    key_board = Keyboard(one_time=False)
    key_board.add(Text(menu_name[menu_number][lng], {"menu": "update"}), color=KeyboardButtonColor.NEGATIVE)
    key_board.row()
    key_board.add(Callback(my_profile[lng].capitalize(), payload={"cmd": "callback"}))
    key_board.row()

    i = 1
    for button in menu_items[menu_number]:
        i += 1
        if i % 3 == 0 and i != 1:
            key_board.row()
        key_board.add(Text(button[lng], payload=button["action"]))

    key_board.row()
    key_board.add(Text(menu_back[lng], {"menu": "back"}), color=KeyboardButtonColor.POSITIVE)
    key_board.add(Text(menu_forth[lng], {"menu": "next"}), color=KeyboardButtonColor.POSITIVE)

    return key_board.get_json()


def xp_bar(my_count, max_count, empty="○", fill="●", ball=25):
    tmp_str = ""

    for i in range(ball):
        if i < round(ball * (my_count / max_count)):
            tmp_str += fill
        else:
            tmp_str += empty

    tmp_str += f" {round(100 * (my_count / max_count), 2)}%"
    return tmp_str


def cmd_send_money(my_id, to_id, money_count, local_users):  # Перевод денег#############
    if money_count <= 0 or local_users[my_id]['balance'] - money_count < 0:
        return False
    local_users[to_id]['balance'] += money_count
    local_users[my_id]['balance'] -= money_count
    return True


async def stop_working(_id, msg: Message, local_users):
    if not local_users[str(_id)]["imWorking"]:
        return False, None, None

    lng = local_users[_id]['lng']

    job_type = local_users[str(_id)]["job"]

    working_time = time.time() - local_users[str(_id)]["time_js"]

    money = jobs[job_type]["money"] * math.floor(working_time)

    my_xp = jobs[job_type]["lvl_add"] * math.floor(working_time)

    local_users[str(_id)]["balance"] += money

    local_users[str(_id)]["imWorking"] = False

    await new_lvl(_id, my_xp, msg, local_users)
    await msg.answer(f"{job_working_time[lng]} {time_format(working_time)}")

    return True, money, None


# noinspection PyBroadException
def get_profile(_id, profile_type="full", local_users=None):
    try:
        user = local_users[str(_id)]
        lng = user['lng']
    except:
        return "None :3"
    if profile_type == "full":
        return f"{my_profile_name_myname[lng]}: {user['nick_name']}\n" \
               f"{my_profile_name_balance[lng]}: ${user['balance']}\n" \
               f"{my_profile_name_id[lng]}: {user['id']}\n" \
               f"{my_profile_name_friends[lng]}: {len(user['friends'])}\n" \
               f"{my_profile_name_modlvl[lng]}: {user['mod_lvl']}"
    else:
        return f"{my_profile_name_myname[lng]}: {user['nick_name']}\n" \
               f"{my_profile_name_balance[lng]}: ${user['balance']}\n" \
               f"{my_profile_name_friends[lng]}: {len(user['friends'])}"


def start_working(_id, job_type, local_users):  # Добавить проверку на знания работы, обучение, усталость персонажа.

    if local_users[str(_id)]["imWorking"]:
        return False
    if jobs[job_type]["min_lvl"] < local_users[str(_id)]["my_lvl"]:
        local_users[str(_id)]["job"] = job_type
        local_users[str(_id)]["time_js"] = time.time()
        local_users[str(_id)]["imWorking"] = True
    else:
        return False
    return True


async def new_lvl(my_id, my_xp, msg: Message, local_users):
    lvl_now = local_users[my_id]["my_lvl"]
    xp_now = local_users[my_id]["my_lvl_xp"]
    lng = local_users[my_id]['lng']

    if my_xp + xp_now < ((lvl_now + 1) * 18):
        return

    tmp_lvl = 0

    local_users[my_id]["my_lvl"] += 1
    new_xp = xp_now + my_xp - ((lvl_now + 1) * 18)
    local_users[my_id]["my_lvl_xp"] = new_xp
    lvl_now = local_users[my_id]["my_lvl"]
    xp_now = local_users[my_id]["my_lvl_xp"]
    tmp_lvl += 1

    if xp_now > ((lvl_now + 1) * 18):
        while xp_now > ((lvl_now + 1) * 18):  # 37
            local_users[my_id]["my_lvl"] += 1  # 2
            new_xp = xp_now - ((lvl_now + 1) * 18)  # 37 - 18 = 19

            local_users[my_id]["my_lvl_xp"] = new_xp

            lvl_now = local_users[my_id]["my_lvl"]
            xp_now = local_users[my_id]["my_lvl_xp"]

            tmp_lvl += 1

    await msg.answer(f"{job_new_lvl[lng]} {tmp_lvl}\n"
                     f"{xp_bar(xp_now, round((lvl_now + 1) * 18))}")


async def new_name(message=None, cmd=None, local_users=None):
    my_id = str(message.from_id)
    lng = local_users[my_id]['lng']

    try:
        tmp_name = message.text.replace(message.text.split(" ")[0] + " ", "")

        if cmd is not None:
            local_users[my_id]["nick_name"] = cmd
            await message.answer(set_nick_success[lng] + local_users[my_id]['nick_name'])
        elif (tmp_name is not None) and (tmp_name != f"!{set_nick[lng]}"):
            local_users[my_id]["nick_name"] = tmp_name
            await message.answer(set_nick_success[lng] + local_users[my_id]["nick_name"])
        else:
            1 / 0
    except:
        await message.answer(set_nick_miss[lng])
