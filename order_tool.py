import pandas as pd

orders = pd.read_csv("sample_data/orders.csv")

def get_order(order_id):
    res = orders[orders["order_id"] == order_id]
    if not res.empty:
        d = res.iloc[0].to_dict()
        output = ""
        for key, value in d.items():
            output+=f"{key}: {value}\n"
        return output
    else:
        return "Order not found."