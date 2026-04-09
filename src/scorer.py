FREE_EMAIL_PROVIDERS = ["gmail", "yahoo", "outlook", "hotmail"]

def score_lead(lead):
    score = 0

    if lead.get("name"):
        score += 10
    if lead.get("email"):
        score += 30
    if lead.get("phone"):
        score += 20
    if lead.get("company"):
        score += 15
    if lead.get("email") and not any(provider in lead["email"].lower() for provider in FREE_EMAIL_PROVIDERS):
        score += 25

    return score

def is_good(lead):
    # Use the pre-computed score to avoid recalculating and risking inconsistencies
    return lead.get("score", 0) >= 40
