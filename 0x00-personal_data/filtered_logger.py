#!/usr/bin/env python3
"""1 function: filter_datum"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 seperator: str) -> str:
    """
    Function to returns the log message obfuscated
    Args:
        fields - a list of strings representing all fields to obfuscate
        redaction - a string representing by what the field will be obfuscated
        message - a string representing the log line
        separator - a string representing by which character
                    is separating all fields in the log line (message)
    """

    count:int = -1
    split_msg: List[str] = message.split(seperator)
    for msg in split_msg:
        count += 1
        for field in fields:
            if field in msg:
                pattern: str = fr'{msg}'
                result: str = re.sub(pattern, redaction, msg)
                split_msg[count] = f'{field}={result}'

    obsfucated_msg: str = ';'.join(split_msg)
    return obsfucated_msg
