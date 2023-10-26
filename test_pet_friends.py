from api import PetFriends
from sittings import valid_email, valid_password, invalid_email, invalid_password, null_email, null_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 400 и в тезультате не содержится слово key"""
    # 1 Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_null_user(email=null_email, password=null_password):
    """ Проверяем что запрос api ключа возвращает статус 400 и в тезультате не содержится слово key"""
    # 2 Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/Sphynx.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

      # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_valid_data(name='', animal_type='',
                                     age='', pet_photo='images/Sphynx.jpg'):
    """Проверяем что можно добавить питомца с без данных"""

      # 3 Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_max_valid_data(name='эuAAа6Йvxщv1tlIz2VlФэыssS7МVoc9jг.2ЛnuТbтгчвWcЛddеWТ3бвSжwwOmXТHRIecyтRО8nGqoXшДнjUyAдАMмQDvLLFЮ-5x8зAZ28SuЖJTT5iWjADQoбргHъWИсэgZf4PDU83бтp5Хk5ЪMZХfИЭAQpцYwТxiYZ0UжFЩ2pgHpGkзgrBCi.дOuZG6ПпЬуЖsRvИXНTukЪpcgrАРYЧХquC3.m_Т2уЩSьqgЧXЗЙвоTG2yOр1рdFмkц7aWgUanLHL', animal_type='эuAAа6Йvxщv1tlIz2VlФэыssS7МVoc9jг.2ЛnuТbтгчвWcЛddеWТ3бвSжwwOmXТHRIecyтRО8nGqoXшДнjUyAдАMмQDvLLFЮ-5x8зAZ28SuЖJTT5iWjADQoбргHъWИсэgZf4PDU83бтp5Хk5ЪMZХfИЭAQpцYwТxiYZ0UжFЩ2pgHpGkзgrBCi.дOuZG6ПпЬуЖsRvИXНTukЪpcgrАРYЧХquC3.m_Т2уЩSьqgЧXЗЙвоTG2yOр1рdFмkц7aWgUanLHL', age='эuAAа6Йvxщv1tlIz2VlФэыssS7МVoc9jг.2ЛnuТbтгчвWcЛddеWТ3бвSжwwOmXТHRIecyтRО8nGqoXшДнjUyAдАMмQDvLLFЮ-5x8зAZ28SuЖJTT5iWjADQoбргHъWИсэgZf4PDU83бтp5Хk5ЪMZХfИЭAQpцYwТxiYZ0UжFЩ2pgHpGkзgrBCi.дOuZG6ПпЬуЖsRvИXНTukЪpcgrАРYЧХquC3.m_Т2уЩSьqgЧXЗЙвоTG2yOр1рdFмkц7aWgUanLHL', pet_photo='images/Sphynx.jpg'):
    """Проверяем что можно добавить питомца с максимальными данных в name, animal_type, age"""

      # 4 Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name



def test_add_new_pet_with_invalid_data(name='44Барбоса', animal_type='111Двор',
                                     age='-1', pet_photo='images/Sphynx.jpg'):
    """Проверяем что можно добавить питомца с некорректными данными"""

      # 5 Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_invalid1_data(name='44Барбоса', age='-1', pet_photo='images/Sphynx.jpg'):
    """Проверяем что можно добавить питомца с неполными данными"""

     # 6 Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Автокот", "котька", "3", "images/Sphynx.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='АвтоКот', animal_type='Котенок', age=1):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet2_info(name='эuAAа6Йvxщv1tlIz2VlФэыssS7МVoc9jг.2ЛnuТbтгчвWcЛddеWТ3бвSжwwOmXТHRIecyтRО8nGqoXшДнjUyAдАMмQ'
                                              'DvLLFЮ-5x8зAZ28SuЖJTT5iWjADQoбргHъWИсэgZf4PDU83бтp5Хk5ЪMZХfИЭAQpцYwТxiYZ0UжFЩ2pgHpGkзgrBCi.дOuZG6ПпЬуЖsRvИXНTukЪpcgrАРYЧХquC3.m_Т2уЩSьqgЧXЗЙвоTG2yOр1рdFмkц7aWgUanLHL',
                                         animal_type='эuAAа6Йvxщv1tlIz2VlФэыssS7МVoc9jг.2ЛnuТbтгчвWcЛddеWТ3бвSжwwOmXТHRIecyтRО8nGqoXшДнjUyAдАMмQDvLLFЮ-5x8зAZ28SuЖJTT5iWjADQoбргHъWИсэgZf4PDU83бтp5Хk5ЪMZХfИЭAQpцYwТxi'
                                                     'YZ0UжFЩ2pgHpGkзgrBCi.дOuZG6ПпЬуЖsRvИXНTukЪpcgrАРYЧХquC3.m_Т2уЩSьqgЧXЗЙвоTG2yOр1рdFмkц7aWgUanLHL',
                                         age='10'):
    """Проверяем возможность обновления информации о питомце - максимальное колличество знаков в name, animal_type, age"""

    # 7 Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet3_info(name='44АвтоКот', animal_type='/"Котенок', age=-10):
    """Проверяем возможность обновления некорректной информацией о питомце"""

    # 8 Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_successful_update_self_pet1_info(name='44АвтоКот', age=1):
    """Проверяем возможность обновления информации о питомце"""

    # 9 Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")



def test_add_pet_with_valid_data(name='Новый', animal_type='Котирьевр',
                                     age='5'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    #pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_pet(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet(pet_photo="images/hvost.jpg"):
    """Проверяем возможность добавления фото питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
        assert status == 200
        assert result['pet_photo'] == pet_photo


def test_add_no_photo_of_pet(pet_photo=""):
    """10 Проверяем возможность добавления фото питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
        assert status == 200
        assert result['pet_photo'] == pet_photo



