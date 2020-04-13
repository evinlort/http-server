import json

from logger import log
from logic.db import DB
from logic.validate import Validate


def new(query):
    log.debug(query)
    dict_query = parse_query_to_dict(query)
    return DB("product").put(Validate(dict_query).insert())


def get_units(query):
    log.debug(query)
    to_ret = list()
    for record in list(DB("units").all()):
        del record["_id"]
        to_ret.append(record["name"])
    log.debug(to_ret)
    return json.dumps(to_ret)


def parse_query_to_dict(query):
    dict_query = dict()
    for pair in query.split("&"):
        paired_pair = pair.split("=")
        dict_query[paired_pair[0]] = paired_pair[1].replace("+", " ")
    return dict_query
