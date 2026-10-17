# our graph example {0:[1,2],1:[0,3],2:[0,4],3:[1],4:[2]}


def DFS_ALGORITHM(graph:dict,goal,node=0,expanded_list = None):
    if expanded_list is None:
        expanded_list = []

    expanded_list.append(node)
    if node == goal:
        return expanded_list
    
       

    for item in graph[node]:
        if item not in expanded_list:
            expanded_list.append(item)
            result = DFS_ALGORITHM(graph,goal,item,expanded_list)
            if result is not None:
                return result
    return None        