def classify_account(is_private, follows_anies) -> tuple[str, str]:
    # Force everything to string, strip spaces, lower case for absolute safety
    str_private = str(is_private).strip().lower()
    str_follows = str(follows_anies).strip().lower()

    if str_private in ['true', '1.0', '1']:
        return "PRIVATE", "account_private"

    if str_follows in ['true', '1.0', '1']:
        return "ANIES", "follows_anies"

    return "NEUTRAL", "not_following_anies"
