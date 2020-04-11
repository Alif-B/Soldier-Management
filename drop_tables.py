from database import db
from JTF2 import JTF2
from CSOR import CSOR

if __name__ == "__main__":
    db.drop_tables([JTF2, CSOR])
