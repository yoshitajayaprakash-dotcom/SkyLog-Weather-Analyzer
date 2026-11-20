import pandas as pd
import numpy as np

FILE_NAME = "data/weather_data.csv"


def view_weather_statistics():
    print("\n========== WEATHER STATISTICS ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No weather records available.")
            return

        temperature = pd.to_numeric(df["temperature"], errors="coerce")
        humidity = pd.to_numeric(df["humidity"], errors="coerce")
        rainfall = pd.to_numeric(df["rainfall"], errors="coerce")

        print("\nTotal Records:", len(df))

        print("\nTemperature:")
        print("Average:", round(np.nanmean(temperature), 2), "°C")
        print("Highest:", round(np.nanmax(temperature), 2), "°C")
        print("Lowest:", round(np.nanmin(temperature), 2), "°C")

        print("\nHumidity:")
        print("Average:", round(np.nanmean(humidity), 2), "%")

        print("\nRainfall:")
        print("Average:", round(np.nanmean(rainfall), 2), "mm")
        print("Total:", round(np.nansum(rainfall), 2), "mm")

    except FileNotFoundError:
        print("No weather data found.")
    except Exception as e:
        print("Error:", e)


def detect_heatwave_days():
    print("\n========== HEATWAVE DETECTION ==========")

    try:
        df = pd.read_csv(FILE_NAME)
        df["temperature"] = pd.to_numeric(
            df["temperature"], errors="coerce"
        )

        hot_days = df[df["temperature"] >= 40]

        if hot_days.empty:
            print("No heatwave days detected.")
        else:
            print(hot_days[["date", "city", "temperature"]].to_string(index=False))

    except FileNotFoundError:
        print("No weather records available.")
    except Exception as e:
        print("Error:", e)


def detect_heavy_rainfall_days():
    print("\n========== HEAVY RAINFALL DETECTION ==========")

    try:
        df = pd.read_csv(FILE_NAME)
        df["rainfall"] = pd.to_numeric(
            df["rainfall"], errors="coerce"
        )

        rainy_days = df[df["rainfall"] >= 50]

        if rainy_days.empty:
            print("No heavy rainfall days detected.")
        else:
            print(rainy_days[["date", "city", "rainfall"]].to_string(index=False))

    except FileNotFoundError:
        print("No weather records available.")
    except Exception as e:
        print("Error:", e)

def export_data_to_csv():
    print("\n========== EXPORT WEATHER DATA ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No records available to export.")
            return

        export_file = "data/skylog_export.csv"
        df.to_csv(export_file, index=False)

        print("\nData exported successfully!")
        print("File saved at:", export_file)
        print("Total records exported:", len(df))

    except FileNotFoundError:
        print("No weather data available.")

    except Exception as e:
        print("Export failed:", e)