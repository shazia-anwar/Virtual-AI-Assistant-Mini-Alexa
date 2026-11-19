def get_user_name():
    """Ask the user for their name."""
    
    name = input("Assistant: Hi! I'm Mini Alexa. What's your name? ").strip()
    
    if not name:
        name = "Friend"
    
    return name


def build_greeting(name):
    """Create a personalized welcome message."""
    
    return f"Nice to meet you, {name}! I am Mini Alexa."
