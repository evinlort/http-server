
def ok(query):
    if "test" in query:
        if "ok" in query["test"]:
            return "<b>I am the router found answer</b>"
    return "Hello, world!"
