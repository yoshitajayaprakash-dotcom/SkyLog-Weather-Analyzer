import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "data/weather_data.csv"


def generate_weather_graphs():
    print("\n========== WEATHER GRAPH GENERATION ==========")

    try:
        df = pd.read_csv(FILE_NAME)

        if df.empty:
            print("No weather records available.")
            return

        df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
        df["rainfall"] = pd.to_numeric(df["rainfall"], errors="coerce")

        os.makedirs("graphs", exist_ok=True)

        # Graph 1: Temperature by City
        plt.figure(figsize=(8, 5))
        plt.bar(df["city"], df["temperature"])
        plt.title("Temperature by City")
        plt.xlabel("City")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("graphs/temperature_graph.png")
        plt.close()

        # Graph 2: Rainfall by City
        plt.figure(figsize=(8, 5))
        plt.bar(df["city"], df["rainfall"])
        plt.title("Rainfall by City")
        plt.xlabel("City")
        plt.ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("graphs/rainfall_graph.png")
        plt.close()

        # Graph 3: Temperature Distribution
        plt.figure(figsize=(8, 5))
        plt.plot(df["date"], df["temperature"], marker="o")
        plt.title("Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("graphs/temperature_trend.png")
        plt.close()

        print("\nThree weather graphs generated successfully!")
        print("Check the graphs folder.")

    except FileNotFoundError:
        print("No weather data found. Add records first.")

    except Exception as e:
        print("Error generating graphs:", e)