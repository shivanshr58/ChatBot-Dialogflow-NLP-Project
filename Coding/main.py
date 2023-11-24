from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper 
import re
import generic_helper
app = FastAPI()
inprogress_orders={}
@app.post("/")
async def handle_request(request: Request):
    payload=await request.json()

    intent=payload['queryResult']['intent']['displayName']
    parameters=payload['queryResult']['parameters']
    output_contexts=payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

    intent_handler_dict = {
        'new.order': new_order,
        'order.add-context: ongoing-order': add_to_order,
        'order.remove-context: ongoing-order': remove_from_order,
        'order.complete-context: ongoing-order': complete_order,
        'track.order-context: ongoing-tracking': track_order,
        }
    return intent_handler_dict[intent](parameters, session_id)

def new_order(parameters: dict,session_id: str):
    if session_id in inprogress_orders:
        del inprogress_orders[session_id]
        fulfillment_text = "Your order has been cleared, please place a new order"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def track_order(parameters: dict,session_id: str):
    order_id = parameters['order_id']
    order_status = db_helper.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The order status for order id {int(order_id)} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id {int(order_id)}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def add_to_order(parameters: dict, session_id: str):
    food_list=parameters['food-item']
    quantity_list=parameters['number']
    floating_order=dict(zip(food_list,quantity_list))
    if session_id in inprogress_orders:
        inprogress_orders[session_id].update(floating_order)
    else:
        inprogress_orders[session_id]=floating_order
    order_string = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
    fulfillment_text = f'So far you have {order_string}, Do you need anything else ?'
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
        })

def remove_from_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text="Sorry I can't find your order.Please place your order again"
    else:
        removed_items = []
        unavailable_food_item = []
        for i in parameters['food-item']:
            if i not in inprogress_orders[session_id]:
                unavailable_food_item.append(i)
            else:
                del inprogress_orders[session_id][i]
                removed_items.append(i)
        if len(inprogress_orders[session_id]) ==0:
            new_order_string ="empty"
        else:
            new_order_string = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
        fulfillment_text = ''
        if len(removed_items)>0:
            fulfillment_text = f"Removed {','.join(removed_items)} from the order, now your order is {new_order_string}. "
        if len(unavailable_food_item)>0:
            fulfillment_text += f"These item(s) were not found in the order: {','.join(unavailable_food_item)} "
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
        })

def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text= "Sorry I can't find your order, please place your order again"
    else:
        order_id = db_helper.get_new_order_id()
        args = inprogress_orders[session_id].items()
        for food_item,quantity in args:
            db_helper.add_order_to_db(food_item,quantity,order_id)
        db_helper.add_order_track_to_db(order_id)
        total=db_helper.get_total(order_id)
        fulfillment_text = f"Order placed successfully! here is your order id {order_id}, and your total is {total}"
        del  inprogress_orders[session_id]
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text  
    })

