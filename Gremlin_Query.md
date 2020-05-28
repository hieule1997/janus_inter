
#### Remote connect   
Remote không tạo session  
Cú pháp
```
:remote connect tinkerpop.server conf/remote.yaml
```
**Lưu ý**
Khi sử dụng remote connect sẽ không thể sử dụng biến tự tạo trong console

Remote tạo session  
Cú pháp  
```
:remote connect tinkerpop.server conf/remote.yaml session
```
**Lưu ý**
Khi sử dụng trong session này có thể tạo biến tạm thời để sử dụng

#### Create graph
Cú pháp
```
graph = JanusGraphFactory.open('path/to/configuration.properties')
graph = JanusGraphFactory.open('conf/gremlin-server/grap1.properties')
g = graph.traversal()
```

#### Drop Graph
Cú pháp
```
JanusGraphFactory.drop(graph);
```

#### Show schema
Cú pháp
```
mgmt = graph.openManagement()
mgmt.printSchema()
```

get or create 
```
 g.V().has('person','name','bill').fold().coalesce(unfold(),addV('person').property('name','bill'))
```

#### Load file groovy
```
bin/gremlin.sh -e scripts/load_data.script 
```

NOTE 
****
Sử dụng indexes cho query  
JanusGraph chỉ phân biệt 2 loại chỉ mục biểu đồ : Composite and Mixed Indexes.

Composite indexes rất nhanh và hiệu quả nhưng chỉ giới hạn ở các tra cứu công bằng cho một tổ hợp các khóa thuộc tính được xác định trước đó. 

Mixed indexes có thể được sử dụng để tra cứu trên bất kỳ tổ hợp khóa được lập chỉ mục nào và hỗ trợ nhiều biến vị ngữ điều kiện ngoài tính bằng nhau tùy thuộc vào kho chỉ mục sao lưu


load plugin 
```
:plugin use tinkerpop.gephi
```

connect gephi
```
:remote connect tinkerpop.gephi
```
chang config gephi
```
:remote config host 0.0.0.0
:remote config port 8080
:remote config workspace workspace1
:remote config visualTraversal graph
```
create subgraph tinkergraph
```
g.E().hasLabel('knows').subgraph('subGraph').cap('subGraph')
```
JanusGraphFactory.getGraphNames()   
ConfiguredGraphFactory.getGraphNames()


Note :

Khi sử dụng load groovy  trình gremlin-server nó sẽ tự động mở 1 remote session, vì vậy các câu lệnh sẽ được sử dụng được trong session
