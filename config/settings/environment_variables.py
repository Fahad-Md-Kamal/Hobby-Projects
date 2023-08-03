from dotenv import dotenv_values

envs = dotenv_values()

SECRET_KEY = envs.get("SECRET_KEY")
DEBUG = bool(envs.get("DEBUG", 0))
ALLOWED_HOSTS = [envs.get("ALLOWED_HOSTS", "*")]
