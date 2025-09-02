def encode(strs: list[str]) -> str:
    final = ''
    number_of_strings_added = 0

    for string in strs:
        if number_of_strings_added < len(strs) - 1:
            final = final + string + '  '
        else:
            final = final + string

        number_of_strings_added += 1

    return final

def decode(s: str) -> list[str]:
    if s == '  ':
        return [""]
    else:
        return s.split('  ')

