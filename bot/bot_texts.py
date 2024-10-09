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
    Все те, кто нарушает порядок в этой группе всякие там спамеры, нефоры и т.д. и т.п.
    будут отправяленны мной во временнОй изолятор, для переосмысления своих действий.
    С каждой ходкой, время пребвания там увеличивается экспоненциально с основанием 5
    и степенью n, где n - номер ходки. Всем мира и добра!
    """
    
    return intro


@prepare_text
def get_add_user() -> str:
    add_user = """
    Братья, давайте поприветствуем нового пользователя!
    """
    
    return add_user


@prepare_text
def get_leave_user() -> str:
    leave_user = """
    Крысы бегут первые с коробля...
    """
    
    return leave_user


@prepare_text
def get_kick_user() -> str:
    kick_user = """
    Этот вацок был нечистым, поэтому его исключили из группы
    """
    
    return kick_user
    