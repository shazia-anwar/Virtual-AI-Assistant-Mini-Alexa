from greetings import get_user_name, build_greeting
from datetime_utils import get_current_date, get_current_time
from calculator import calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import show_help


def main():
    
    print("=" * 45)
    print("       MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 45)
    
    user_name = get_user_name()
    
    print("Assistant:", build_greeting(user_name))
    print(f"Assistant: Welcome, {user_name}!")
    print("Assistant: Type 'help' to see my commands.")
    
    while True:
    
        command = input(f"\n{user_name}: ").strip().lower()
        
        if command in ["hello", "hi", "hey"]:
            print(f"Assistant: Hello, {user_name}! How can I help you?")
        
        elif command == "date":
            print("Assistant: Today's date is", get_current_date())
        
        elif command == "time":
            print("Assistant: Current time is", get_current_time())
        
        elif command == "calculate":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ").strip()
                num2 = float(input("Enter second number: "))
                
                result = calculate(num1, operator, num2)
                print("Assistant: Result:", result)
            
            except ValueError:
                print("Assistant: Please enter valid numbers.")
        
        elif command == "quote":
            print("Assistant:", get_random_quote())
        
        elif command == "joke":
            print("Assistant:", get_random_joke())
        
        elif command == "fact":
            print("Assistant:", get_random_fact())
        
        elif command == "game":
            play_guessing_game()
        
        elif command == "recommend":
            print("Assistant:", recommend_activity())
        
        elif command == "perceptron":
            perceptron_demo()
        
        elif command == "help":
            show_help()
        
        elif command in ["exit", "quit", "bye"]:
            print(f"Assistant: Goodbye, {user_name}! Have a great day.")
            break
        
        else:
            print("Assistant: Sorry, I didn't understand that command.")
            print("Assistant: Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
