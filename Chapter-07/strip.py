import re
string = input('String : ')
strip = input('Character to strip')

def restrip(string,strip):
    if strip != "":
        strip_regex = re.compile(strip)
        new_string = strip_regex.sub('', string)
        return new_string
    else:
        strip_regex = re.compile('^\s*|\s*$')
        new_string = strip_regex.sub('', string)
        return new_string

print(restrip(string,strip))