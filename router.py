import re
from order_tool import get_order
from retriever import retrieve_answer

def route(question):
    match = re.search(r"ORD\d+", question.upper())
    if match:
        order_id = match.group()
        return get_order(order_id)
    return retrieve_answer(question)