def build_queries(profession, location=None):
    platforms = [
        "linkedin.com",
        "facebook.com",
        "instagram.com",
        "reddit.com"
    ]

    email_filter = '("@gmail.com" OR "@yahoo.com" OR "@outlook.com")'

    queries = []

    for p in platforms:
        if location:
            queries.append(f'site:{p} "{profession}" "{location}" {email_filter}')
        else:
            queries.append(f'site:{p} "{profession}" {email_filter}')

    return queries