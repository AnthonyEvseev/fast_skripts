from environs import Env

env = Env()
env.read_env()

HOST = env.str('HOST')
PORT = env.int('PORT')
DEST_DIR = env.str('DEST_DIR')
PATH = env.str('PATH')
