import csv
import os
from datetime import datetime

FILE_NAME = "data/weather_data.csv"


def add_weather_reading():

    print("\n========== ADD WEATHER READING ==========")

    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty!")
        return

    try:
        date = input("Enter date (YYYY-MM-DD): ")

        datetime.strptime(date, "%Y-%m-%d")

        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        rainfall = float(input("Enter rainfall (mm): "))

        if not -50 <= temperature <= 60:
            print("Invalid temperature!")
            return

        if not 0 <= humidity <= 100:
            print("Humidity must be between 0 and 100!")
            return

        if rainfall < 0:
            print("Rainfall cannot be negative!")
            return

        reading = {
            "date": date,
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall
        }

        os.makedirs("data", exist_ok=True)

        file_exists = os.path.exists(FILE_NAME)

        with open(FILE_NAME, "a", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=reading.keys()
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(reading)

        print("\nWeather reading saved successfully!")

    except ValueError:
        print("\nInvalid input! Please enter the correct values.")

    except OSError:
        print("\nUnable to save the weather record.")

def view_all_records():

    print("\n========== ALL WEATHER RECORDS ==========")

    try:
        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            records = list(reader)

            if not records:
                print("No weather records found.")
                return

            for record in records:
                print("\nDate:", record["date"])
                print("City:", record["city"])
                print("Temperature:", record["temperature"], "°C")
                print("Humidity:", record["humidity"], "%")
                print("Rainfall:", record["rainfall"], "mm")
                print("-" * 40)

    except FileNotFoundError:
        print("No weather data available yet.")

    except OSError:
        print("Unable to read weather records.")

def search_records_by_date():

    print("\n========== SEARCH WEATHER RECORDS ==========")

    search_date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(search_date, "%Y-%m-%d")

        with open(FILE_NAME, "r", newline="") as file:

            reader = csv.DictReader(file)

            found = False

            for record in reader:

                if record["date"] == search_date:

                    print("\nWeather Record Found!")
                    print("Date:", record["date"])
                    print("City:", record["city"])
                    print("Temperature:", record["temperature"], "°C")
                    print("Humidity:", record["humidity"], "%")
                    print("Rainfall:", record["rainfall"], "mm")

                    found = True

            if not found:
                print("No records found for this date.")

    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")

    except FileNotFoundError:
        print("No weather records available.")

    except OSError:
        print("Unable to read weather records.")

def generate_sample_data():
    print("\n========== GENERATE SAMPLE DATA ==========")

    sample_records = [
        ["2026-11-15", "Bengaluru", 27, 65, 2.5],
        ["2026-11-16", "Bengaluru", 30, 60, 0],
        ["2026-11-17", "Chennai", 36, 55, 5],
        ["2026-11-18", "Mumbai", 32, 70, 12],
        ["2026-11-19", "Delhi", 41, 40, 0],
        ["2026-11-20", "Bengaluru", 28, 65, 2.5]
    ]

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "date", "city", "temperature",
                "humidity", "rainfall"
            ])

        writer.writerows(sample_records)

    print("Sample weather data generated successfully!")
    print("6 sample records added.")