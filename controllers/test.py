
def ok(query):
    if "test" in query:
        if "ok" in query["test"]:
            return "<b>I am the router found answer</b>"
    fd = open("html/test.html", "r")
    text = fd.read()
    return text
