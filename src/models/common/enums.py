from enum import Enum


class LabelType(str, Enum):
    RESPONSE_PRESENT = "response_present"
    NOT_NEEDED = "not_needed"
    NO_SALES = "no_sales"
    NEWSLETTER = "newsletter"
    AUTO_REPLY = "auto_reply"
