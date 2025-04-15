import datetime
import os


#Existing functions for interactive input
def append_to_file(content):
    with open("Task6_news_feed.txt", "a", encoding="utf-8") as f:
        f.write(content)
    print("Record published!\n")


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


# New functionality: Class to process records from a text file
class FileRecordProcessor:
    """
    Processes a text file containing one or many records.

    Expected input format (each record separated by a blank line):

    For News:
      Type: News
      Text: <news text>
      City: <city name>

    For Private Ad:
      Type: Private Ad
      Text: <ad text>
      Expiration: <YYYY-MM-DD>

    For Weather Report:
      Type: Weather Report
      City: <city name>
      Temperature: <°C>

    The processor applies case normalization and, if successful, removes the file.
    """

    def __init__(self, file_path="records_input.txt"):
        self.file_path = file_path

    def normalize_text(self, text):
        # Example normalization: convert to lowercase and strip extra spaces.
        return text.lower().strip()

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Split by double newlines (assuming records are separated by blank lines)
            record_blocks = [block for block in content.split("\n\n") if block.strip()]
            for block in record_blocks:
                # Split block lines and remove empty lines
                lines = [line.strip() for line in block.splitlines() if line.strip()]
                # Create a dictionary from the lines using the ':' delimiter
                record_data = {}
                for line in lines:
                    # Expecting "Key: Value" pairs
                    if ":" in line:
                        key, value = line.split(":", 1)
                        record_data[key.strip()] = self.normalize_text(value)

                record_type = record_data.get("Type", "")
                if record_type == "news":
                    self.process_news(record_data)
                elif record_type == "private ad":
                    self.process_private_ad(record_data)
                elif record_type == "weather report":
                    self.process_weather_report(record_data)
                else:
                    print("Unknown record type:", record_type)

            # If processing completes successfully, remove the file
            os.remove(self.file_path)
            print(f"File {self.file_path} processed and removed successfully.")
        except Exception as e:
            print(f"Error processing file: {e}")

    def process_news(self, data):
        text = data.get("Text", "No text provided")
        city = data.get("City", "Unknown")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        record = f"News -------------------------\n{text}\n{city.capitalize()}, {date}\n\n"
        append_to_file(record)

    def process_private_ad(self, data):
        text = data.get("Text", "No text provided")
        exp_date_input = data.get("Expiration", "")
        try:
            exp_date = datetime.datetime.strptime(exp_date_input, "%Y-%m-%d")
            days_left = (exp_date - datetime.datetime.now()).days
            record = f"Private Ad -------------------\n{text}\nExpires: {exp_date.date()}, {days_left} days left\n\n"
            append_to_file(record)
        except ValueError:
            print("Invalid expiration date in record:", exp_date_input)

    def process_weather_report(self, data):
        city = data.get("City", "Unknown")
        temp_input = data.get("Temperature", "")
        try:
            temp = float(temp_input)
            tag = "🌞 Warm Day" if temp >= 15 else "❄️ Cold Day"
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            record = f"Weather Report --------------\nCity: {city.capitalize()}\nTemperature: {temp}°C\nDate: {date} | Tag: {tag}\n\n"
            append_to_file(record)
        except ValueError:
            print("Invalid temperature value in record:", temp_input)


def main():
    while True:
        print("Choose the type of operation:")
        print("1. Publish News")
        print("2. Publish Private Ad")
        print("3. Publish Weather Report")
        print("4. Exit")
        print("5. Process Records from File")
        choice = input("Enter choice number: ").strip()
        if choice == "1":
            publish_news()
        elif choice == "2":
            publish_private_ad()
        elif choice == "3":
            publish_weather_report()
        elif choice == "5":
            file_path = input("Enter file path (or press Enter to use default 'records_input.txt'): ").strip()
            if not file_path:
                file_path = "records_input.txt"
            processor = FileRecordProcessor(file_path)
            processor.process_file()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

