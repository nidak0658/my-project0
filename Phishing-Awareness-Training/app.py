import time

def display_slide(slide_number):
    """ Display the slide content based on slide number """
    slides = {
        1: "Slide 1: Introduction to Phishing Attacks\n"
           "- Definition of phishing attacks\n"
           "- Importance of awareness\n"
           "- Goals of the presentation",

        2: "Slide 2: Types of Phishing Attacks\n"
           "- Email Phishing:\n"
           "  - Fake emails mimicking legitimate sources\n"
           "  - Urgency and threats to compel action\n"
           "- Website Phishing:\n"
           "  - Fake websites resembling trusted sites\n"
           "  - Used to steal login credentials and personal information\n"
           "- Spear Phishing:\n"
           "  - Targeted attacks on specific individuals or organizations\n"
           "  - Research-based personalization for credibility",

        3: "Slide 3: Anatomy of a Phishing Email\n"
           "- Sender Information:\n"
           "  - Check sender's email address for inconsistencies\n"
           "- Subject Line:\n"
           "  - Urgent or threatening language\n"
           "  - Claims of account issues, rewards, or offers\n"
           "- Content:\n"
           "  - Poor grammar or spelling mistakes\n"
           "  - Requests for personal information or login credentials\n"
           "- Links and Attachments:\n"
           "  - Hover over links to reveal actual URLs\n"
           "  - Avoid downloading attachments from unknown sources",

        4: "Slide 4: Recognizing Phishing Websites\n"
           "- URL Inspection:\n"
           "  - Look for misspelled or unusual domain names\n"
           "  - Verify HTTPS encryption and security certificates\n"
           "- Design and Layout:\n"
           "  - Poor quality images, logos, or inconsistent branding\n"
           "  - Malicious pop-ups or redirects",

        5: "Slide 5: Social Engineering Tactics\n"
           "- Pretexting:\n"
           "  - Creating a fabricated scenario to elicit information\n"
           "  - Impersonation of authority figures or colleagues\n"
           "- Fear and Intimidation:\n"
           "  - Threats of consequences for inaction\n"
           "  - Urgent demands for immediate response",

        6: "Slide 6: Examples of Common Phishing Scenarios\n"
           "- Financial Institutions:\n"
           "  - Requests to verify account details\n"
           "  - False alerts of fraudulent activity\n"
           "- Online Retailers:\n"
           "  - Fake order confirmations or delivery notifications\n"
           "- Tech Support Scams:\n"
           "  - Calls or emails claiming technical issues and requesting remote access",

        7: "Slide 7: Red Flags and Warning Signs\n"
           "- Unsolicited Requests:\n"
           "  - Unexpected emails or messages asking for personal information\n"
           "- High-Risk Links:\n"
           "  - URLs that lead to suspicious or unfamiliar websites\n"
           "- Too Good to Be True Offers:\n"
           "  - Promises of large sums of money or prizes for little effort",

        8: "Slide 8: Best Practices to Avoid Phishing Attacks\n"
           "- Verify Sources:\n"
           "  - Contact the organization directly using official contact information\n"
           "- Hover Before Clicking:\n"
           "  - Check URLs by hovering over links before clicking\n"
           "- Enable Two-Factor Authentication (2FA):\n"
           "  - Adds an extra layer of security for account logins\n"
           "- Educational Training Programs:\n"
           "  - Regularly update employees and stakeholders on phishing tactics and prevention strategies",

        9: "Slide 9: Case Studies and Real-Life Examples\n"
           "- Phishing Incident Analysis:\n"
           "  - Review recent phishing attacks and their impacts\n"
           "- Success Stories:\n"
           "  - Organizations successfully thwarting phishing attempts through awareness and preparedness",

        10: "Slide 10: Conclusion and Recap\n"
            "- Summary of Key Points:\n"
            "  - Phishing attacks are pervasive and evolving\n"
            "  - Awareness and vigilance are crucial defenses\n"
            "- Takeaway Message:\n"
            "  - Stay informed, stay cautious, and report suspicious activities",

        11: "Slide 11: Q&A Session\n"
            "- Open Floor for Questions:\n"
            "  - Address participant queries and provide additional insights",

        12: "Slide 12: Resources and Further Reading\n"
            "- Additional Resources:\n"
            "  - Provide links to cybersecurity resources and training materials\n"
            "- Contact Information:\n"
            "  - Offer support for reporting suspicious activities or seeking further assistance"
    }

    if slide_number in slides:
        print(slides[slide_number])
    else:
        print("Slide not found.")

def display_presentation():
    """ Display the entire presentation """
    for slide_number in range(1, 13):
        display_slide(slide_number)
        time.sleep(5)  # Pause for 5 seconds before showing the next slide

def main():
    print("Welcome to the Phishing Awareness Training!")
    print("This training will educate you about recognizing and avoiding phishing attacks.\n")
    print("Press Enter to continue to the presentation...")
    input()

    display_presentation()

    print("\nThank you for completing the Phishing Awareness Training!")
    print("Remember to stay vigilant and report any suspicious activities.\n")

if __name__ == "__main__":
    main()
