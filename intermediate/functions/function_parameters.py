def check_weather(temp):
    if temp > 30:
        print("It's hot outside!")
    elif temp < 10:
        print("It's cold outside!")
    else:
        print("The weather is moderate.")
    
check_weather(35) # Output: It's hot outside!
check_weather(5)  # Output: It's cold outside!
check_weather(20) # Output: The weather is moderate.