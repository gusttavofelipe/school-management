from decouple import config


NAME = config("NAME")
HOST = config("HOST")
PORT = config("PORT")
USER = config("USER")
PASSWORD = config("PASSWORD_DB")


ALLOWED_HOSTS = config("ALLOWED_HOSTS")
