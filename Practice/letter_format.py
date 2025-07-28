Recipient=input("Enter the recipient's name: ")
your_name=input("Enter your name: ")
reason= input("Enter the reason for writing: " )
letter="""

Dear {Recipient},

I hope this letter finds you well. I am writing to inform you about {reason}.

Thank you for your attention to this matter.

Sincerely,
{your_name}"""
print(letter.format(Recipient=Recipient, your_name=your_name, reason=reason))