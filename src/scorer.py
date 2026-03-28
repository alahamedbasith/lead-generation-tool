def score_lead(lead):
    score = 0

    if lead["email"]:
        score += 40
    if lead["phone"]:
        score += 20
    if lead["company"]:
        score += 15
    if lead["email"] and "gmail" not in lead["email"]:
        score += 25

    return score

def is_good(lead):
    # Lowered to 40 so that any lead with just an email address still passes
    return score_lead(lead) >= 40