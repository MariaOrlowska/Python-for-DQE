import datetime


def publish_news():
    text = input("Enter News text: ").strip()
    city = input("Enter city: ").strip()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    record = f"News -------------------------\n{text}\n{city}, {date}\n\n"
    append_to_file(record)


def publish_private_ad():
    text = input("Enter Ad text: ").strip()
    exp_date_input = input("Enter expiration date (YYYY-MM-DD): ").strip()
    try:
        exp_date = datetime.datetime.strptime(exp_date_input, "%Y-%m-%d")
        days_left = (exp_date - datetime.datetime.now()).days
        record = f"Private Ad -------------------\n{text}\nExpires: {exp_date.date()}, {days_left} days left\n\n"
        append_to_file(record)
    except ValueError:
        print("Invalid date format. Try again.")


def publish_weather_report():
    city = input("Enter city: ").strip()
    temp = input("Enter temperature (°C): ").strip()
    try:
        temp = float(temp)
        tag = "🌞 Warm Day" if temp >= 15 else "❄️ Cold Day"
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        record = f"Weather Report --------------\nCity: {city}\nTemperature: {temp}°C\nDate: {date} | Tag: {tag}\n\n"
        append_to_file(record)
    except ValueError:
        print("Temperature must be a number.")


def append_to_file(content):
    with open("news_feed.txt", "a", encoding="utf-8") as f:
        f.write(content)
    print("Record published!\n")


def main():
    while True:
        print("Choose the type of record to publish:")
        print("1. News")
        print("2. Private Ad")
        print("3. Weather Report (unique)")
        print("4. Exit")
        choice = input("Enter choice number: ").strip()
        if choice == "1":
            publish_news()
        elif choice == "2":
            publish_private_ad()
        elif choice == "3":
            publish_weather_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
