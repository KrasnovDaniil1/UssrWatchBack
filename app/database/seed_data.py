


# -------- Часы --------

factory_seed = [ # часовые заводы
    "1МЧЗ имени Кирова",
    "Петродворцовый часовой завод",
    "Чистопольский часовой завод",
    "2МЧЗ",
    "Пензенский часовой завод",
    "Минский часовой завод",
    "Угличский часовой завод",
    "Ульяновский часовой завод",
]

brand_seed = [ # названия брэнда часов
    "полёт",
    "слава",
    "ракета",
    "восток",
    "чайка",
    "заря",
    "луч",
    "победа",
    "зим",
    "звезда",
    
    
    "мир",
    "весна",
    "аврора",
    "океан",
    "штурманские",
    "сигнал",
    "командирские",
    "спутник",
    "волга",
    "волна",
    "вымпел",
    "дружба",
    "кама",
    "полюс",
    "колос",
    "космос",
    "люкс",
    "маяк",
    "нева",
    "сатурн",
    "свет",
    "старт",
    "столичные",
    "амфибия",
    
    
    "sekonda",
    "cornarvin",
    "exacta",
    "foreign",
    "serkisof",
    "orex",
    "mister anker",
    "fabuna",
    "sport",
    
    
    "poljot",
    "slava",
    "wostok",
    "raketa",
    "zarja",
    "chaika"
]

case_material_seed = [ # материалы корпуса часов
    "титан",
    "сталь",
    "дерево",
    "хром",
    "нейзильбер",
    "камень",
    "серебро",
    "нитрид",
    "алюминий",
    "пластик",
    
    "золото 583",
    "золото 585",
    "золото 750",
    
    "позолота Au",
    "позолота Au1",
    "позолота Au5",
    "позолота Au10",
    "позолота Au12.5",
    "позолота Au15",
    "позолота Au20",
    "позолота Au25",
    "позолота 22K",
    "позолота",
    
    # лимонная позолота, белая позолота, родиевая белая, желтая позолота,  без клейма, Au, Au1, Au5, Au10, Au12, Au12, Au12.5 Au15, Au20, Au25, +, <, M, Mю, 22K

]

gender_seed = [ # пол
    "мужские",
    "женские",
    "унисекс",
    "детские"
]

function_seed = [ # функции часов
    "автоподзавод",
    "ручной завод",
    "день недели",
    "дата",
    "стоп секунда",
    "хронограф", 
    "прецизионные", 
    "лунный календарь",
    "счетчик гейгера",
    "будильник",
    
    
    
]

mechanism_type_seed = [
    "механика",
    "кварц",
    "электро-магнитные",
]


admin_seed = [
    {
        "name": "admin",
        "password": "admin@admin.admin"
    }
]

user_test = [
    {
        "name":"test1",
        "email":"test1",
        "oauth_provider":"test1",
        "oauth_id":"test1",
        "avito_url":"test1",
        "meshok_url":"test1",
        "rating": 10
    },
    {
        "name":"test2",
        "email":"test2",
        "oauth_provider":"test2",
        "oauth_id":"test2",
        "avito_url":"test2",
        "meshok_url":"test2",
        "rating": 10
    }
]

mechanism_test = [
    {
        "stones": 18,
        "release": 1900,
        "mechanism_type_id": 1,
        "factory_id": 1,
        "user_id": 1
    },
    {
        "stones": 22,
        "release": 1950,
        "mechanism_type_id": 1,
        "factory_id": 2,
        "user_id": 1
    },
    {
        "stones": 17,
        "release": 2000,
        "mechanism_type_id": 1,
        "factory_id": 1,
        "user_id": 2
    },
]

mechanism_function_test = [
    {
        "mechanism_id": 1,
        "function_id": 1
    },
    {
        "mechanism_id": 1,
        "function_id": 2
    },
    {
        "mechanism_id": 2,
        "function_id": 3
    },
    {
        "mechanism_id": 3,
        "function_id": 4
    },
]

alias_test = [
    {
        "watch_id": 1,
        "key": "министерка"
    },
    {
        "watch_id": 1,
        "key": "джинс"
    },
    {
        "watch_id": 2,
        "key": "нвч"
    }
]


watch_test = [
    {
        "folder": "test1",
        "code": 1234,
        "integrated_bracelet": True,
        "start_release": 1900,
        "end_release": 1950,
        "gender_id": 1,
        "case_material_id": 1,
        "mechanism_id": 1,
        "factory_id": 1,
        "brand_id": 1,
        "user_id": 1
    },
    {
        "folder": "test3",
        "code": 1234,
        "start_release": 1800,
        "end_release": 1950,
        "gender_id": 1,
        "case_material_id": 1,
        "mechanism_id": 1,
        "factory_id": 1,
        "brand_id": 1,
        "user_id": 1
    },
    {
        "folder": "test2",
        "code": 123456,
        "integrated_bracelet": True,
        "start_release": 1950,
        "end_release": 1990,
        "gender_id": 2,
        "case_material_id": 3,
        "mechanism_id": 2,
        "factory_id": 2,
        "brand_id": 2,
        "user_id": 2
    },
]
