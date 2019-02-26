def sql_escape(req_body):
    # escape all suspicious chars (regarding SQLi)
    return req_body.replace("%27", "\\%27")\
        .replace("%00", "\\%00")\
        .replace("%08", "\\%08")\
        .replace("%09", "\\%09")\
        .replace("%0a", "\\%0a")\
        .replace("%0d", "\\%0d")\
        .replace("%1a", "\\%1a")\
        .replace("%22", "\\%22")\
        .replace("%25", "\\%25")\
        .replace("%5c", "\\%5c")\
        .replace("%5f", "\\%5f")
