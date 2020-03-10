def index(query):
    query = query.strip("/")
    fd = open("js/" + query, "r")
    return fd.read()
