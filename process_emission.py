import json
import logging
import sys

import greengrasssdk

# Logging
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# SDK Client
client = greengrasssdk.client("iot-data")

# Counter
my_counter = 0
max_co2_0 = 0.0
max_co2_1 = 0.0
max_co2_2 = 0.0
max_co2_3 = 0.0
max_co2_4 = 0.0
def lambda_handler(event, context):
    global my_counter
    global max_co2_0
    global max_co2_1
    global max_co2_2
    global max_co2_3
    global max_co2_4

    co2 = event[2]

    if event[10] == "veh0":
        if float(co2) > float(max_co2_0):
            max_co2_0 = float(co2)
    if event[10] == "veh1":
        if float(co2) > float(max_co2_1):
            max_co2_1 = float(co2)
    if event[10] == "veh2":
        if float(co2) > float(max_co2_2):
            max_co2_2 = float(co2)
    if event[10] == "veh3":
        if float(co2) > float(max_co2_3):
            max_co2_3 = float(co2)
    if event[10] == "veh4":
        if float(co2) > float(max_co2_4):
            max_co2_4 = float(co2)


    #TODO3: Return the result
    client.publish(
        topic="maxco2/vehicle0",
        payload=json.dumps(
            {"vehicle0_max_co2": max_co2_0}
        ),
    )
    client.publish(
        topic="maxco2/vehicle1",
        payload=json.dumps(
            {"vehicle1_max_co2": max_co2_1}
        ),
    )
    client.publish(
        topic="maxco2/vehicle2",
        payload=json.dumps(
            {"vehicle2_max_co2": max_co2_2}
        ),
    )
    client.publish(
        topic="maxco2/vehicle3",
        payload=json.dumps(
            {"vehicle3_max_co2": max_co2_3}
        ),
    )
    client.publish(
        topic="maxco2/vehicle4",
        payload=json.dumps(
            {"vehicle4_max_co2": max_co2_4}
        ),
    )
    my_counter += 1

    return