def main():
    # Prompt for user input for time in 24-hour format
    user_input = input("Enter a time in 24-hour format: ")
    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    # Convert the time to float value
    # 07:30 -> 7.5
    time = time.split(":")
    hour = int(time[0])
    minute = time[1]

    time = hour + int(minute) / 60
    return float(time)

if __name__ == "__main__":
    main()
