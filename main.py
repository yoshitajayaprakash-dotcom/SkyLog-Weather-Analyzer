from weather_functions import (
    add_weather_reading,
    view_all_records,
    search_records_by_date,
    generate_sample_data
)
from data_analysis import (
    view_weather_statistics,
    detect_heatwave_days,
    detect_heavy_rainfall_days,
    export_data_to_csv
)

from visualisation import generate_weather_graphs
def display_menu():
    print("\n" + "=" * 45)
    print("                 SKYLOG")
    print("       WEATHER DATA LOGGER & ANALYZER")
    print("=" * 45)

    print("1. Add Weather Reading")
    print("2. View All Records")
    print("3. Search Records by Date")
    print("4. Generate Sample Weather Data")
    print("5. View Weather Statistics")
    print("6. Detect Heatwave Days")
    print("7. Detect Heavy Rainfall Days")
    print("8. Generate Weather Graphs")
    print("9. Export Data to CSV")
    print("10. Exit")

    print("=" * 45)


def main():

    while True:

        display_menu()

        try:
            choice = int(input("Enter your choice (1-10): "))

            if choice == 1:
                add_weather_reading()

            elif choice == 2:
                view_all_records()

            elif choice == 3:
                search_records_by_date()

            elif choice == 4:
                generate_sample_data()

            elif choice == 5:
                view_weather_statistics()

            elif choice == 6:
                detect_heatwave_days()

            elif choice == 7:
                detect_heavy_rainfall_days()

            elif choice == 8:
                generate_weather_graphs()

            elif choice == 9:
                export_data_to_csv()

            elif choice == 10:
                print("Thank you for using SkyLog!")
                break

            else:
                print("Invalid choice! Please enter 1-10.")

        except ValueError:
            print("Please enter a valid number.")


main()