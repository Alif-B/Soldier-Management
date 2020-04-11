from JTF2 import JTF2
from CSOR import CSOR
from database import db

if __name__ == "__main__":
    db.create_tables([JTF2, CSOR])