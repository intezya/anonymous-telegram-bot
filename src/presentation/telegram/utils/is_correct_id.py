async def is_correct_id[x](id_from_user, id_from_command: x) \
        -> ValueError | KeyError | bool | x:
    # Проверка ID на корректность (отсутствие букв):
    try:
        _id = int(id_from_command)
    except ValueError:
        return ValueError()  # Некорректная ссылка!

    # Проверка равенства ID:
    if _id == id_from_user:
        return False  # Нельзя отправить сообщение самому себе

    # Проверка существования в БД, возвращается KeyError если не существует
    # (Пока что используется try/except при отправке сообщения)
    # TODO: db interaction
    ...  # Такого пользователя не существует

    return _id
