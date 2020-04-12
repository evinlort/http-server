from logger import log
from logic.db import DB
from logic.validate import Validate


def new(query):
    log.debug(query)
    dict_query = parse_query_to_dict(query)
    DB().put(Validate(dict_query).insert())
    return ""


def parse_query_to_dict(query):
    dict_query = dict()
    for pair in query.split("&"):
        paired_pair = pair.split("=")
        dict_query[paired_pair[0]] = paired_pair[1].replace("+", " ")
    return dict_query
