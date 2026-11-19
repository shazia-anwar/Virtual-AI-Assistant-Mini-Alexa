from datetime import datetime

def recommend_activity():
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "Good morning! Start your day with exercise or reading."
    
    elif 12 <= current_hour < 17:
        return "It is afternoon. Focus on learning or completing your tasks."
    
    elif 17 <= current_hour < 21:
        return "It is evening. You can go for a walk or enjoy a hobby."
    
    else:
        return "It is night. Relax and get some good sleep."


def perceptron_demo():
    print("\n--- Simple Perceptron Demo ---")
    
    input1 = 1
    input2 = 0
    
    weight1 = 0.5
    weight2 = 0.3
    bias = -0.2
    
    weighted_sum = (input1 * weight1) + (input2 * weight2) + bias
    
    if weighted_sum >= 0:
        output = 1
    else:
        output = 0
    
    print("Input 1:", input1)
    print("Input 2:", input2)
    print("Weight 1:", weight1)
    print("Weight 2:", weight2)
    print("Bias:", bias)
    print("Weighted Sum:", weighted_sum)
    print("Perceptron Output:", output)
