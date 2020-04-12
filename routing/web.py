from routing.route_tuple import *

routes = [
    Route("GET", "/", "test:ok"),
    Route("POST", "/", "insert:new"),
    Route("GET", "/test", "basic:test"),
    Route("post", "/send", "file:write"),
    Route("get", "/css", "css:index"),
    Route("get", "/js", "js:index")
]
