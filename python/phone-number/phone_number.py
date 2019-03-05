import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = re.sub(r'^1', '', ''.join(re.findall(r"\d", phone_number)))
        matches = re.match(r"^([2-9]\d{2})([2-9]\d{2})(\d{4})$", self.number)

        if matches is None:
            raise ValueError("Invalid phone number!")

        self.area_code = matches.groups()[0]
        self.exchange_code = matches.groups()[1]
        self.subscriber_number = matches.groups()[2]

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"
