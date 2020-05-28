from gremlin_python import statics
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.traversal import WithOptions
import glob2
import logging
import time
import pandas as pd
import datetime
import sys
# logging.basicConfig(filename='./log/test_1.log',
#                     format='[%(asctime)s] [%(levelname)s] [THREAD_ID %(thread)d] [PROCESS_ID %(process)d] :%(message)s',
#                     level=logging.DEBUG)

def Remote_connect():
    return traversal().withRemote(DriverRemoteConnection('ws://10.84.86.123:8182/gremlin','g2'))

## Drop all Node
# g.V().drop().iterate()
def Drop_data(g):
    g.V().drop().iterate()

# Create Node 
def loop_data(g,dataset):
    print("running ....")
    for (index,data) in dataset.iterrows():
        # getorcreate node 
        v1 = g.V().has('sim','name',data["a_number"]).fold().coalesce(__.unfold(),__.addV('sim').property('name',data["a_number"]).property('tac',data["tac"])).next()
        v2 = g.V().has('sim','name',data["b_number"]).fold().coalesce(__.unfold(),__.addV('sim').property('name',data["b_number"])).next()
        # create egde
        g.V(v1).addE('info').to(v2).property('service_type',data["service_type"]).property('b_prefix',data["b_prefix"]).property('start_time',data["start_time"]).property('duration',data["duration"]).iterate()

def Schema(g):
    

def main():
    datetime_parser = lambda c: pd.to_datetime(c, format='%Y%m%d%H%M%S', errors='coerce')
    msc_headers = ['a_number', 'b_number', 'service_type', 'b_prefix', 'start_time', 'duration', 'tac']
    start = datetime.datetime.now()
    print(start)
    # for filename, (version,) in glob2.iglob('./data/*', with_matches=True):
    #     print(filename)
    #     msc_df = pd.read_csv(filename, header=None, names=msc_headers, parse_dates=['start_time'], 
    #                     date_parser=datetime_parser, low_memory=False)
    #     loop_data(msc_df)
    #     end = datetime.datetime.now()
    #     print("Time run :" + filename + " " + str(end - start))
    g = Remote_connect()
    msc_df = pd.read_csv("./data/xaa", header=None, names=msc_headers, parse_dates=['start_time'], 
                        date_parser=datetime_parser, low_memory=False)
    loop_data(g,msc_df)
    end = datetime.datetime.now()
    print("Time run : " + str(end - start))
if __name__ == '__main__':
    try:
        main()
        print('DONE!')
        sys.exit(0)
    except Exception as e:
        print('Error: {}'.format(e))