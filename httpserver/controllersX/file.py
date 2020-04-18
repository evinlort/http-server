def write(query):
    query_list = filter(None, query.decode("utf-8").split('\r\n'))
    for q in query_list:
        print(q)
    return str()
