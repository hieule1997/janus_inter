graph = JanusGraphFactory.open('conf/gremlin-server/grap1.properties')
g = graph.traversal()

new File('data/xaa').eachLine { line, count ->
  // Skip header
  if (count > 1){

    columns = line.split(',', -1)

    (a_number, b_number, service_type, b_prefix, start_time, duration, tac) = columns

    if (b_number.length() == 40){
        // node_a = g.V().has('person','a_number',a_number)
        // node_b = g.V().has('person','a_number',b_number)
        // println( node_a.hasNext(),node_b.hasNext())
        node_a =  g.V().has('person','a_number',a_number).fold().coalesce(unfold(),addV('person').property('a_number',a_number).property('tac',tac))
        node_b =  g.V().has('person','a_number',b_number).fold().coalesce(unfold(),addV('person').property('a_number',b_number).property('tac',""))
        print(node_a)
        print(node_b)
        if (service_type = "MTC"){
            g.V(node_a).addE('MTC').to(g.V(node_b))
            .property('time', start_time)
            .property('duration', duration)
            .next()
        }
        if (service_type = "MOC"){
            g.V(node_a).addE('MOC').to(g.V(node_b))
            .property('time', start_time)
            .property('duration', duration)
            .next()
        }
        
    }
    
  }
}

// new File('data/links.csv').eachLine { line, count ->
//   if (count > 1){
//     columns = it.split(',')
//     (source_entity,
//     target_entity,
//     attr1,
//     attr2) = columns

//     fromVertex = entityToId.get(source_entity)
//     toVertex = entityToId.get(target_entity)

//     g.V(fromVertex).addE('is_linked_to').to(g.V(toVertex))
//       .property('attr1', attr1)
//       .property('attr2', attr2)
//       .next()
//   }
// }

graph.tx().commit()
graph.close()



[GraphStep(vertex,[]), 
 HasStep([~label.eq(person), a_number.eq(a6987577763caef0fe21bcbb0fe1ba5c5890d5ce)]), 
 FoldStep, 
 CoalesceStep(
   [
     [UnfoldStep], 
     [AddVertexStep(
       {label=[person], tac=[86941003], a_number=[a6987577763caef0fe21bcbb0fe1ba5c5890d5ce]}
       )
     ]
   ]
 )
]
[GraphStep(vertex,[]),
  HasStep(
    [~label.eq(person), a_number.eq(c9c938049731cfc7af44f649129a2ebf43960ca5)]),
     FoldStep, 
     CoalesceStep([[Error in data/data.groovy at [36: }] - null