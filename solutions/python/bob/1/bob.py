def response(hey_bob):
    # Remove leading and trailing whitespace
    hey_bob = hey_bob.strip()

    # Check for silence (empty or just whitespace)
    if hey_bob == "":
        return "Fine. Be that way!"

    # Check for yelling: has at least one letter and is all uppercase
    is_yelling = any(c.isalpha() for c in hey_bob) and hey_bob.upper() == hey_bob

    # Check for question
    is_question = hey_bob.endswith("?")

    # Yelled question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    # Yelling (but not question)
    elif is_yelling:
        return "Whoa, chill out!"
    # Question (but not yelling)
    elif is_question:
        return "Sure."
    # Anything else
    else:
        return "Whatever."