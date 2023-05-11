import datetime
from cafe import Cafe
from errors import (
    VaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends, cafe):
    masks_to_buy, without_a_mask = 0, 0
    for person in friends:
        try:
            if cafe.visit_cafe(person):
                without_a_mask += 1
                if without_a_mask == len(friends):
                    print(f"Friends can go to {cafe.name}")
                    return f"Friends can go to {cafe.name}"

        except (VaccineError):
            print(f"All friends should be vaccinated")
            return f"All friends should be vaccinated"

        except (NotWearingMaskError):
            masks_to_buy += 1

    if masks_to_buy:
        print(f"Friends should buy {masks_to_buy} masks")
        return f"Friends should buy {masks_to_buy} masks"

friends = [
    {
        "name": "Alisa",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": 1
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": 0
    },
]
go_to_cafe(friends, Cafe("KFC")) # "Friends should buy 2 masks"
