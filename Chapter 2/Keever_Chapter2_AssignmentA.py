# Creates the list of 30 common phrases in spam emails
def common_spam_words():
    words = [
        "Apply now",
        "Call now",
        "Click here",
        "For only",
        "Limited Time",
        "Offer expires",
        "Once in a lifetime",
        "Special promotion",
        "Risk free",
        "Certified",
        "Free",
        "Free offer",
        "Free membership",
        "Money Hack",
        "Deal",
        "Giving away",
        "No obligation",
        "100% off",
        "Opt in",
        "Click below",
        "Hurry",
        "Clearance",
        "Best rates",
        "Subscribe",
        "Affordable",
        "Solution",
        "Discount",
        "Join Millions",
        "Drastically reduced",
        "Guaranteed rates",
        "Buy now",
    ]

    with open('common_spam_phrases.txt', 'w') as file:
        for phrase in words:
            file.write(phrase + '\n')

# Defines the ask_user function which will read
def ask_user():
    with open('common_spam_phrases.txt', 'r') as file:
        words = [line.strip() for line in file]

    print('\nWelcome to Spam Rater! ')
    email_message = input('\nEnter the email message: ').strip()

    # Starts the spam score at zero
    spam_score = 0
    phrase_counts = {phrase: 0 for phrase in words}
    found_phrases = []

    # Adds a point to the spam score for every word that matches the list
    for phrase in words:
        count = email_message.lower().count(phrase.lower())
        if count > 0:
            spam_score += count
            phrase_counts[phrase] = count
            found_phrases.append(phrase)

# Creates the spam score criteria
    if spam_score >= 10:
        scam_likelihood = "HIGH"
    elif spam_score > 5:
        scam_likelihood = "Moderate"
    else:
        scam_likelihood = "low"

    # The spam score, likelihood rating and the words that ticked the system are displayed for the user
    print(f'\nThe spam score is: {spam_score}')
    print(f'The likelihood of this message being a scam is: {scam_likelihood}')
    print('Common spam phrases found in this message were:')
    for phrase in found_phrases:
        print(f'- {phrase} (Count: {phrase_counts[phrase]})')

# Call the functions to execute the script
common_spam_words()
ask_user()




