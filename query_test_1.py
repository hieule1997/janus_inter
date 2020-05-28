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
from gremlin_python.structure.graph import  Graph
import glob2
import logging
import time
import pandas as pd
import datetime
import sys
logging.basicConfig(filename='./log/query_test_1.log',
                    format='[%(asctime)s] [%(levelname)s] [PROCESS_ID %(process)d] :%(message)s',
                    level=logging.DEBUG)
def setup_graph():
    try:
        graph = Graph()
        connstring = "ws://10.84.86.123:8182/gremlin"
        logging.info('Trying To Login')
        g = graph.traversal().withRemote(DriverRemoteConnection(connstring, 'g2'))
        logging.info('Successfully Logged In')
    except Exception as e:  # Shouldn't really be so broad
        logging.error(e, exc_info=True)
        raise BadRequestError('Could not connect to Neptune')
    return g
    # get all preson
# def get_persons():
#     logging.info('Request Received: Persons')
#     g = setup_graph()
#     return [{**node.__dict__, **properties} for node in g.V().hasLabel('sim')[0:3]
#             for properties in g.V(node).valueMap()]

#     # get preson
# def get_person(person_id, g):
#     """
#     TODO - add more ways of finding a person than just the id.
#     :param person_id:
#     :param g:
#     :return:
#     """

#     person = g.V(person_id).toList()
#     logging.info("People found are: %s" % person)
#     # If not found
#     if not person:
#         return None
#     # Just in case there is more than one - shouldn't happen
#     if len(person) > 1:
#         raise ValueError('More than one person found for id: %s' % person_id)
#     return person[-1]
#     # add new preson
# def new_person():
#     logging.info('Request Received: Add New Person')
#     g = setup_graph()
#     try:
#         properties = {"id": "XYZ1234", "prop1": "Some", "prop2": "Value"}
#         # TODO - Validate the JSON
#         logging.info('Adding New Person to Graph')
#         # Get the ID from the JSON
#         person_id = properties.pop('id')
#         if not person_id:
#             raise BadRequestError('Missing "id" in body')
#         person = get_person(person_id=person_id, g=g)
#         if person:
#             raise BadRequestError('id "%s" already exists' % person_id)
#         # TODO - Validate there is a single unique ID
#         person = g.addV('person').property(T.id, person_id).next()
#         # Ideally I would roll this into a single call
#         logging.info("Received Properties: " + str(properties))
#         for prop_name, prop_value in properties.items():
#             g.V(person).property(prop_name, prop_value).next()
#     except(ValueError, AttributeError, TypeError) as e:
#         logging.error(e, exc_info=True)
#         raise BadRequestError('Could not insert person.  Error: ' + str(e))
#     logging.info("Successfully inserted person")
#     return {"id": person_id}

# def Schema():
#     graph = Graph()
#     mgmt = graph.openManagement()
#     mgmt.printSchema()
# v1 = g.addV('person').property('name','marko').property('name','marko').next()
# v2 = g.addV('person').property('name','stephen').next()
# print(g.V(Bindings.of('id',v1)).addE('knows').to(v2).property('weight',0.75).iterate())
# print( g.V().both().name.toList())

# herculesAge = g.V().has('name', 'stephen')
# print(herculesAge.name.toList())
## Drop all Node
# g.V().drop().iterate()
# def loop_data(g,dataset):
#     print("running ....")
#     for (index,data) in dataset.iterrows():
#         v1 = g.addV('sim').property('name',data["a_number"]).property('tac',data["tac"]).next()
#         v2 = g.addV('sim').property('name',data["b_number"]).next()
#         g.V(Bindings.of('id',v1)).addE('info').to(v2).property('service_type',data["service_type"]).property('b_prefix',data["b_prefix"]).property('start_time',data["start_time"]).property('duration',data["duration"]).iterate()
# def main():
#     datetime_parser = lambda c: pd.to_datetime(c, format='%Y%m%d%H%M%S', errors='coerce')
#     msc_headers = ['a_number', 'b_number', 'service_type', 'b_prefix', 'start_time', 'duration', 'tac']
#     start = datetime.datetime.now()
#     print(start)
#     # for filename, (version,) in glob2.iglob('./data/*', with_matches=True):
#     #     print(filename)
#     #     msc_df = pd.read_csv(filename, header=None, names=msc_headers, parse_dates=['start_time'], 
#     #                     date_parser=datetime_parser, low_memory=False)
#     #     loop_data(msc_df)
#     #     end = datetime.datetime.now()
#     #     print("Time run :" + filename + " " + str(end - start))
#     g = Remote_connect()
#     msc_df = pd.read_csv("./data/xaj", header=None, names=msc_headers, parse_dates=['start_time'], 
#                         date_parser=datetime_parser, low_memory=False)
#     loop_data(g,msc_df)
#     end = datetime.datetime.now()
#     print("Time run : " + str(end - start))
if __name__ == '__main__':
    try:
        # main()
        g = setup_graph()
        # print(g.V().valueMap().limit(10).toList())
        g.V().drop().iterate()
        # new_person()
        # node_sim = get_persons()
        # print(node_sim)
        print('DONE!')
        sys.exit(0)
    except Exception as e:
        print('Error: {}'.format(e))
    