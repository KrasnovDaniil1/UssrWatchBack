user_test = [
    {
        "folder":"f1",
        "name":"test1",
        "email":"test1",
        "oauth_provider":"test1",
        "oauth_id":"test1",
        "rating": 10,
        "avito_url":"test1",
        "meshok_url":"test1"
    },
    {
        "folder":"f2",
        "name":"test2",
        "email":"test2",
        "oauth_provider":"test2",
        "oauth_id":"test2",
        "avito_url":"test2",
        "meshok_url":"test2",
        "rating": 15
    }
]

mechanism_test = [
    {
        "folder": "f1",
        "code": "2428H",
        "stones": 18,
        "release": 1900,
        "mechanism_type_id": 1,
        "factory_id": 1,
        "user_id": 1
    },
    {
        "folder": "f2",
        "code": "2209",
        "stones": 22,
        "release": 1950,
        "mechanism_type_id": 2,
        "factory_id": 2,
        "user_id": 1
    },
    {
        "folder": "f3",
        "code": "2209",
        "stones": 17,
        "release": 2000,
        "mechanism_type_id": 3,
        "factory_id": 3,
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

watch_test = [
    {
        "folder": "папка на картинку",
        "code": '1234',
        "description": "Крутые часы, в единственном экземпляре",
        "integrated_bracelet": True,
        "start_release": 1970,
        "end_release": 1975,
        "case_material_id": 1,
        "mechanism_id": 1,
        "factory_id": 1,
        "brand_id": 1,
        "user_id": 1,
        "alias": "нвч министерка"
    },
    {
        "folder": "test2",
        "code": '123456',
        "description": "tetsttes2",
        "integrated_bracelet": True,
        "start_release": 1950,
        "end_release": 1990,
        "case_material_id": 3,
        "mechanism_id": 2,
        "factory_id": 3,
        "brand_id": 3,
        "user_id": 2,
        "alias": "джинс амфибия",
        
    },
    {
        "folder": "test3",
        "start_release": 1800,
        "end_release": 1950,
        "case_material_id": 2,
        "mechanism_id": 1,
        "factory_id": 2,
        "brand_id": 2,
        "user_id": 1,
        "alias": "министерка амфибия"
    },

]

alias_test = [
    {
        "watch_id": 1,
        
    },
    {
        "watch_id": 3,
    },
    {
        "watch_id": 2,
        
    }
]

collection_test = [
    {
        "user_id": 1,
        "watch_id": 1
    },
    {
        "user_id": 1,
        "watch_id": 2
    },
    {
        "user_id": 2,
        "watch_id": 1
    }
]


blocked_test = [
    {
        "email": "block@block.block"
    }
]

draft_watch_test = [
    {
        "folder": "draft_test",
        "user_id": 1
    }
]

draft_alias_test = [
    {
        "key": "alias test",
        "watch_id": 1
    }
]

draft_mechanism_test = [
    {
        "folder": "draft_test",
        "user_id": 1
    }
]

draft_mechanism_function_test = [
    {
        "mechanism_id": 1,
        "function_id": 1
    },
    {
        "mechanism_id": 1,
        "function_id": 2
    },
]