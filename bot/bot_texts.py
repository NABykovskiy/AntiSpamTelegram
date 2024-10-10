import re

def prepare_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return re.sub(r'\s+', ' ', result).strip()
    return wrapper


@prepare_text
def get_intro() -> str:
    intro = """
    Ассаляму ва алейкум, братья! Я Мурик - новый смотрящий этой группы.
    В данной версии я буду вести некоторую статистику, и смотреть за вашим лексиконом.
    Всем мира и добра!
    """
    
    return intro


@prepare_text
def get_add_user() -> str:
    add_user = """
    Братья, давайте поприветствуем нового пользователя!
    """
    
    return add_user


@prepare_text
def get_end() -> str:
    leave_user = """
    Прощайте, братва! Не забывайте бродягу.
    """
    
    return leave_user


@prepare_text
def get_kick_user() -> str:
    kick_user = """
    Этот вацок был нечистым, поэтому его исключили из группы
    """
    
    return kick_user

@prepare_text
def get_profanity_warning() -> str:
    profanity_warinig = """
    Брат, наш язык итак прекрасен и соврешенен. По-братски, в следующий раз
    не матерись.
    """

    return profanity_warinig
    