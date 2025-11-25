import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
import os

load_dotenv()


database_url = os.getenv('DATABASE_URL')

def connection():
    return psycopg.connect(database_url, row_factory=dict_row)

# Sin dict_row: resultado = ('One Piece', 1100)
# Con dict_row: resultado = {'titulo': 'One Piece', 'capitulos': 1100}

