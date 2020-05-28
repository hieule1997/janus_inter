from gremlin_python.driver import client
client = client.Client('ws://10.15.14.209:8182/gremlin', 'g')

result_set = client.submit("[1,2,3,4]") 
future_results = result_set.all()  
results = future_results.result() 
assert results == [1, 2, 3, 4] 

future_result_set = client.submitAsync("[1,2,3,4]") 
result_set = future_result_set.result() 
result = result_set.one() 
assert results == [1, 2, 3, 4] 
assert result_set.done.done() 

client.close() 