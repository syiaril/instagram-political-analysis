def classify_account(is_private: bool, follows_anies: bool) -> tuple[str, str]:
    """
    Classifies the account based on its visibility and following status.
    Returns a tuple of (classification, classification_reason).
    """
    # In some pandas/CSV setups, bools might be strings or NaNs. Handling that just in case.
    if isinstance(is_private, str):
        is_private = is_private.lower() == 'true'
    if isinstance(follows_anies, str):
        follows_anies = follows_anies.lower() == 'true'
        
    if is_private == True or is_private == 1.0 or str(is_private).lower() == 'true':
        return "PRIVATE", "account_private"

    if follows_anies == True or follows_anies == 1.0 or str(follows_anies).lower() == 'true':
        return "ANIES", "follows_anies"

    return "NEUTRAL", "not_following_anies"
