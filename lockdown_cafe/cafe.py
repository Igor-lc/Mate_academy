import datetime
from errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        self.visitor = visitor

        if "vaccine" not in self.visitor:
            raise NotVaccinatedError("The visitor must have a vaccination key")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("The vaccine must not be expired")
        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("All visitors must wear masks")
        else:
            return f"Welcome to {self.name}"
