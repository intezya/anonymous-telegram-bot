"""
Taken from
https://github.com/mahenzon/ri-sdk-python-wrapper/blob/master/ri_sdk_codegen/utils/case_converter.py
"""


def camel_case_to_snake_case(input_str: str) -> str:
    chars = []
    for c_idx, char in enumerate(input_str):
        if c_idx and char.isupper():
            nxt_idx = c_idx + 1
            flag = nxt_idx >= len(input_str) or input_str[nxt_idx].isupper()
            prev_char = input_str[c_idx - 1]
            if not prev_char.isupper() or not flag:
                chars.append('_')
        chars.append(char.lower())
    return ''.join(chars)
