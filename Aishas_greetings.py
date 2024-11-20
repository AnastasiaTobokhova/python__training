from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, recipient):
    # Open the generic card template based on the card type
    template_file = open(f"{card_type}.txt", 'r')

    # Create and open a new card file for writing
    new_card_file = open(f"{sender_name}_generic.txt", 'w')

    try:
        # Write the custom card content
        new_card_file.write(f"Dear {recipient}\n")
        new_card_file.write(template_file.read())
        new_card_file.write(f"\nSincerely, {sender_name}")

        # Yield control back to the context block
        yield new_card_file
    finally:
        # Ensure both files are closed after use
        template_file.close()
        new_card_file.close()


# Assuming the generic function is defined as shown previously

# Use the with statement to generate the card
with generic('thankyou_card', 'Mwenda', 'Amanda') as card:
    print('Card Generated!')
# Open and read the generated card file
with open('Mwenda_generic.txt', 'r') as first_order:
    print(first_order.read())


class Personalized:
    def __init__(self, sender_name, receiver_name):
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        # Open a new file for writing with the format <sender_name>_personalized.txt
        self.file = open(f"{sender_name}_personalized.txt", 'w')

    def __enter__(self):
        # Write the receiver's name to the file
        self.file.write(f"Dear {self.receiver_name}\n")
        # Return the file object
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Write the closing line to the file
        self.file.write(f"\nSincerely, {self.sender_name}")
        # Close the file
        self.file.close()


# Assuming the Personalized class is defined as shown previously

# Use the with statement to generate the personalized card
with Personalized('John', 'Michael') as card:
    card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. "
               "I don’t say it often but I just wanted to let you know that you inspire me and I love you! "
               "All the best. Always.")

# Assuming the generic function and Personalized class are defined as shown previously

# Use nested with statements to generate both orders
with generic('happy_bday', 'Josiah', 'Remy') as generic_card, \
        Personalized('Josiah', 'Esther') as personalized_card:
    # Print confirmation for the generic card
    print('Generic Birthday Card Generated!')

    # Write the personalized message for Esther
    personalized_card.write(
        "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, "
        "you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. "
        "Cheers to 25!! You’re getting old!"
    )


# You are a part of Aisha’s Greetings - a card printing company that prints greeting cards with a hint of
# personalization! You want to help Aisha create a system that generates cards based on customers’ requests.
# You have been provided with two pre-filled card types:
# happy_bday.txt: a card with a birthday message
# thankyou_card.txt: a card file with a thank you message
# Click through the files on your right and see what’s in them!
