from jd_price_crawler import Watcher
from jd_price_db import PriceDatabase


if __name__ == '__main__':
    w = Watcher()
    w.get_price()
    db = PriceDatabase(w)
    if db.watcher.first_read == str(True):
        db.create_table()
        w.modifiy_xml_firstread()
    db.insert()
    dic = db.query()
    print dic