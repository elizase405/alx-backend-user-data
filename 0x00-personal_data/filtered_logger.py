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

    for f in fields:
        message = re.sub(f'{f}=.*?{seperator}',
                         f'{f}={redaction}{seperator}', message)

    return message
