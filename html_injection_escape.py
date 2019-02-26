import re


def html_escape(req_body):
    # Whitelist: <b>,</b>,<i>,</i>,<u> and </u>
    # possible malicious input
    suspicious = re.compile(r'(%3C([^b]|[^i]|[^u]){0,6}%3E)|(%3C%2F([^b]|[^i]|[^u]){0,6}%3E)')

    # Escape any tags that are not allowed (uses an external method)
    req_body = suspicious.sub(escape, req_body, re.IGNORECASE)

    # escape " just in case (escape it here since it is not included in the sql blacklist
    return req_body.replace("%34", "%26quot")



# An external method which escapes HTML tags
def escape(match):
    to_escape = match.group()
    return to_escape.replace("%3C", "%26lt").replace("%3E", "%26gt")