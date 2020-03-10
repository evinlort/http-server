def index(query):
    query = query.strip("/")
    fd = open(query, "r")
    return fd.read()