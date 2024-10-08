from alembic.config import Config
from alembic import command
from sqlalchemy.exc import OperationalError


def run_migrations():
    """
    Функция для выполнения всех миграций, которые еще не были применены к базе данных
    """
    alembic_cfg = Config("alembic.ini")
    try:
        command.upgrade(alembic_cfg, "head")
    except OperationalError as e:
        print(f"Ошибка во время миграции: {e}")


if __name__ == "__main__":
    run_migrations()
