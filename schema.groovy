graph = JanusGraphFactory.open('conf/gremlin-server/grap1.properties')
mgmt = graph.openManagement()

mgmt.makeVertexLabel('person').make()
mgmt.makeVertexLabel('call_info').make()
mgmt.makeEdgeLabel('MTO').make()
mgmt.makeEdgeLabel('MOC').make()

a_number = mgmt.makePropertyKey('a_number').dataType(String.class).cardinality(Cardinality.SINGLE).make()
tac = mgmt.makePropertyKey('tac').dataType(String.class).cardinality(Cardinality.SINGLE).make()
time = mgmt.makePropertyKey('time').dataType(String.class).cardinality(Cardinality.SINGLE).make()
duration = mgmt.makePropertyKey('duration').dataType(String.class).cardinality(Cardinality.SINGLE).make()

mgmt.buildIndex('vertexByA_number', Vertex.class).addKey(a_number).unique().buildCompositeIndex()
mgmt.buildIndex('a_numberAndDuration', Vertex.class).addKey(a_number).addKey(duration).buildMixedIndex("search")

graph.close()