lngs = ["ru", "en"]
#####################  Регистрация  ##########################

start_cmd = ["Начать", "Start"]

reg = "Чтобы зарегестрироваться начть пользоваться ботом ввидите (Начать)\n" \
      "To register and start using the bot, enter (Start)"

reg_success = {"ru": "Вы успешно зарегестрированы!",
               "en": "You have successfully registered!"}

reg_already = {"ru": "Вы уже были зарегестрированы!",
               "en": "You have already been registered!"}

#####################  Дать Денег  ###########################

send_money = {"ru": "датьденег",
              "en": "sendmoney"}

send_money_success = {"ru": "Перевод успешно совершен!",
                      "en": "The transfer has been successfully completed!"}

send_money_miss = {"ru": f'Чтобы отпарвить деньги введи "!{send_money["ru"]} (Айди человека) (Сумму)"',
                   "en": f'To send money, enter "!{send_money["en"]} (VKID) (Amount)"'}

send_money_err = {"ru": "Неверная сумма или недостаточно денег, попробуйте еще раз.",
                  "en": "Incorrect amount or not enough money, try again."}

######################  Работы  ##############################

job = {"ru": "работа",
       "en": "job"}

job_stop = {"ru": "стоп",
            "en": "stop"}

job_working_info_balance = {"ru": "Ваш заработок",
                            "en": "Your earnings"}

job_working_info_lvl = {"ru": "Ваш лвл повысился на",
                        "en": "Your lvl has increased by"}

job_new_lvl = {"ru": "Ваш уровень повысился на ",
               "en": "Your level has increased by "}

job_working_time = {"ru": "Вы работали ",
                    "en": "You worked for "}

job_working_info_my_job = {"ru": "Ваша работа",
                           "en": "Your job"}

job_stop_working = {"ru": f"Чтобы закончить работать введите (!{job['ru']} {job_stop['ru']})",
                    "en": f"To stop working, enter (!{job['en']} {job_stop['en']})"}

job_info = {"ru": f"Чтобы начать работать введите (!{job['ru']} (Код работы))\n"
                  f"Чтобы получить список работ, код работ введите (!{job['ru']})",
            "en": f"To start working, enter (!{job['en']} (Job code))\n"
                  f"To get a list of works, list of work-codes, enter (!{job['en']})"}

job_miss = {"ru": "Вы уже работаете или Ваш уровень не достаточен для этой работы.",
            "en": "You are already working or your level is not sufficient for this job."}

job_success_start = {"ru": "Вы успешно начали работать!",
                     "en": "You have successfully started working!"}

job_success_stop = {"ru": "Вы успешно закончили работать!",
                    "en": "You have successfully finished working!"}

job_money = {"ru": "Заработок",
             "en": "Earnings"}

job_code = {"ru": "Код работы",
            "en": "Code of job"}

job_list = {"ru": "Список работ:",
            "en": "List of jobs:"}

#####################  Новое Имя  ############################

set_nick = {"ru": "новоеимя",
            "en": "rename"}

set_nick_success = {"ru": "Новое имя: ",
                    "en": "New name: "}

set_nick_miss = {"ru": f'Чтобы поменять имя введите "!{set_nick["ru"]} (Новое имя)"',
                 "en": f'To change the name, enter "!{set_nick["en"]} (New name)"'}

####################  Профиль  ###############################

my_profile = {"ru": "профиль",
              "en": "profile"}

my_profile_name_id = {"ru": "Айди",
                      "en": "Id"}

my_profile_name_myname = {"ru": "Мое имя",
                          "en": "My name"}

my_profile_name_balance = {"ru": "Баланс",
                           "en": "Balance"}

my_profile_name_modlvl = {"ru": "Уровень админки",
                          "en": "Mod level"}

my_profile_name_friends = {"ru": "Количество друзей",
                           "en": "Friend count"}

my_profile_friend_add = {"ru": "новыйдруг",
                         "en": "newfriend"}

my_profile_friend_err = {"ru": "Этот человек не зарегистрирован у нас в боте.",
                         "en": "This person is not registered in our bot."}

my_profile_friend_err_self = {"ru": "Вы не можете добавить в друзья самого себя '___'",
                              "en": "You can't add yourself as a friend '___'"}

my_profile_friend_success = {"ru": "Человек добавлен в список ваших друзей"
                                   ", ему нужно проделать ту же операцию"
                                   ", чтобы вы стали друзьями.",
                             "en": "The person has been added to your friends list"
                                   ", he needs to perform the same operation for you to become friends."}

my_profile_friend_miss = {"ru": f"Чтобы добавить человека в друзья введите "
                                f"(!{my_profile_friend_add['ru']} (Айди человека))",
                          "en": f"To add a person as a friend, enter "
                                f"(!{my_profile_friend_add['en']} (The person's ID))"}

my_profile_miss = {"ru": f"Чтобы посмотреть свой профиль введите (!{my_profile['ru']})\n"
                         f"Чтобы посмотреть профиль ДРУГА введите (!{my_profile['ru']} (Айди ДРУГА))",
                   "en": f"To view your profile, enter (!{my_profile['en']})\n"
                         f"To view a FRIEND'S profile, enter (!{my_profile['en']} (FRIEND'S ID))"}

my_profile_err = {"ru": "Этого человека нет у вас в друзьях!",
                  "en": "This person is not your friend!"}

####################  Язык  ##################################

lng_command = {"ru": "язык",
               "en": "language"}

lng_command_list = {"ru": "языки",
                    "en": "languages"}

lng_command_list_out = {"ru": "Список языков:",
                        "en": "List of languages:"}

lng_command_miss = {"ru": f"Чтобы поменять язык введите (!{lng_command['ru']} (Язык))\n"
                          f"Чтобы получить список языков введите (!{lng_command_list['ru']})",
                    "en": f"To change the language, enter (!{lng_command['en']} (Language))\n"
                          f"To get a list of languages, enter (!{lng_command_list['en']})"}

lng_command_edited = {"ru": "Язык изменен на Русский.",
                      "en": "The language has been changed to English. (I'm using a translator, don't hit me.)"}

########################  Меню  ###############################

menu = ["меню", "menu"]

menu_using = {"ru": "Чтобы пользоваться ботом введите (меню)",
              "en": "To use the bot, enter (menu)"}

menu_num = {"ru": "Номер меню - ",
            "en": "Number menu - "}

menu_main = {"ru": "Главное меню",
             "en": "Main menu"}

menu_back = {"ru": "Назад",
             "en": "Back"}

menu_forth = {"ru": "Вперед",
              "en": "Forth"}

menu_update = {"ru": "обновить меню",
               "en": "Update menu"}

menu_name = [
    {"ru": "Профиль",
     "en": "Profile"},

    {"ru": "Работы",
     "en": "Jobs"},

    {"ru": "Друзяь",
     "en": "Friends"},

    {"ru": "Помощь",
     "en": "Help"},

    {"ru": "Об авторе",
     "en": "About author"}
]

menu_items = [
    # Первый раздел!
    [{"ru": "Профиль.",  # Первая кнопка, меню помощь. temp[0][*]
      "en": "Profile.",
      "action": {"menu_profile": "get_profile"}},

     {"ru": "Дать денег.",  # Вторая кнопка.
      "en": "Send money.",
      "action": {"menu_profile": "send_money"}},

     {"ru": "!" + set_nick["ru"],  # Третья кнопка.
      "en": "!" + set_nick["en"],
      "action": None},

     {"ru": "!" + my_profile["ru"],  # Четвертая кнопка.
      "en": "!" + my_profile["en"],
      "action": None},

     {"ru": "!" + set_nick["ru"],  # Пятая кнопка.
      "en": "!" + set_nick["en"],
      "action": None},

     {"ru": "!" + lng_command["ru"],  # Шестая кнопка.
      "en": "!" + lng_command["en"],
      "action": None},

     {"ru": "!" + my_profile["ru"],  # Скедьмая кнопка.
      "en": "!" + my_profile["en"],
      "action": None},

     {"ru": "!" + set_nick["ru"],  # Восьмая кнопка.
      "en": "!" + set_nick["en"],
      "action": None},

     {"ru": "!" + my_profile["ru"],  # Девятая кнопка.
      "en": "!" + my_profile["en"],
      "action": None},

     {"ru": "!" + my_profile["ru"],  # Десятая кнопка.
      "en": "!" + my_profile["en"],
      "action": None}
     ],

    # Второй раздел
    [{"ru": "тест",
      "en": "test",
      "action": None}],

    # Третий раздел
    [{"ru": "тест",
      "en": "test",
      "action": None}],

    # Четвертый разел
    [{"ru": "тест",
      "en": "test",
      "action": None}],

    # Пятый раздел
    [{"ru": "Ты боба",
      "en": "test",
      "action": None}]
]

###############################################################
