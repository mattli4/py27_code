from jd_price_crawler import Watcher
from jd_price_db import PriceDatabase
from jd_price_graph import PlotGraph

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
    plt = PlotGraph(dic, w.name)
    plt.gen_graph()
