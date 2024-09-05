#!/usr/bin/python3
"""1 function: filter_datum"""

import re


def filter_datum(fields, redaction, message, seperator):
    """
    Function to returns the log message obfuscated
    Args:
        fields - a list of strings representing all fields to obfuscate
        redaction - a string representing by what the field will be obfuscated
        message - a string representing the log line
        separator - a string representing by which character
                    is separating all fields in the log line (message)
    """

    count = -1
    split_msg = message.split(seperator)
    for msg in split_msg:
        count += 1
        for field in fields:
            if field in msg:
                pattern = fr'{msg}'
                result = re.sub(pattern, redaction, msg)
                split_msg[count] = f'{field}={result}'

    msg = ';'.join(split_msg)
    return msg
