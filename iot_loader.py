import os

folders = [

    "data/telecom_iot_crm/crm",

    "data/telecom_iot_crm/revenue",

    "data/telecom_iot_crm/device"

]

for folder in folders:

    print(
        folder,
        "Exists:",
        os.path.exists(folder)
    )