import os
import random
from twilio.rest import Client

messages = [
    "💧 Drink water. Your body is 60% water, not chai. Act accordingly.",
    "💧 Hydration alert! Even your phone needs charging. So do you — with water.",
    "💧 Your kidneys filed a complaint. Please drink water immediately.",
    "💧 Drink water or your skin will look like a raisin by Thursday. Your call.",
    "💧 Fun fact: crying doesn't count as hydration. Drink actual water.",
    "💧 Bhai/Behen, biryani gravy is NOT water. Please drink some.",
    "💧 This is your 2-hour water check. Yes, again. No excuses accepted.",
    "💧 Imagine your cells screaming 'PAANI DO!' in tiny voices. Help them.",
    "💧 Water > chai > everything else. Priorities sorted. Now drink.",
    "💧 Your future self with glowing skin says: DRINK WATER RIGHT NOW.",
    "💧 Plot twist: the headache you have? It's dehydration. Drink water, genius.",
]

def format_whatsapp_number(number):
    number = number.strip()
    if not number.startswith("whatsapp:"):
        number = "whatsapp:" + number
    if not number.startswith("whatsapp:+"):
        number = number.replace("whatsapp:", "whatsapp:+")
    return number

account_sid  = os.environ["TWILIO_ACCOUNT_SID"]
auth_token   = os.environ["TWILIO_AUTH_TOKEN"]
to_numbers   = os.environ["TO_WHATSAPP_NUMBER"].split(",")
from_number  = format_whatsapp_number(os.environ["FROM_WHATSAPP_NUMBER"])

client = Client(account_sid, auth_token)

for number in to_numbers:
    formatted = format_whatsapp_number(number)
    message = client.messages.create(
        body=random.choice(messages),
        from_=from_number,
        to=formatted
    )
    print(f"✅ Message sent to {formatted}! SID: {message.sid}")
