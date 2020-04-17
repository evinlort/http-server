
def test(query):
    return "Text by ROUTER"


def new(query):
    if isinstance(query, dict):
        if "test" in query:
            return query["test"].upper()
    if isinstance(query, bytes):
        with open("evgeny.pdf", "wb") as fd:
            fd.write(query)
            return "Saved"
    import time
    return f"Time is: {time.time()} and query was {query}"
