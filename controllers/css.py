def index(query):
    query = query.strip("/")
    fd = open("css" + query, "r")
    return fd.read()
