import sqlite3
import matplotlib.pyplot as plt

# Step 1: Create a database and population table
def create_database():
    """
    Creates a SQLite database with the name 'population_YI.db' (replace YI with your initials).
    Defines a table called 'population' with columns: city, year, and population.
    """
    db_name = "population_YI.db"  # Replace 'YI' with your initials
    conn = sqlite3.connect(db_name)  # Establish a connection to the database
    cursor = conn.cursor()
    
    # Create the 'population' table if it does not already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)
    conn.commit()
    conn.close()  # Close the connection to save resources
    return db_name

# Step 2: Insert initial data for 2023
def insert_initial_data(db_name):
    """
    Inserts initial population data for 10 cities in Florida for the year 2023.
    """
    # Sample data for 10 cities in Florida
    cities = [
        ('Miami', 2023, 470914),
        ('Orlando', 2023, 309154),
        ('Tampa', 2023, 407599),
        ('Jacksonville', 2023, 971319),
        ('Tallahassee', 2023, 199366),
        ('St. Petersburg', 2023, 258308),
        ('Hialeah', 2023, 235563),
        ('Fort Lauderdale', 2023, 182760),
        ('Cape Coral', 2023, 204510),
        ('Gainesville', 2023, 141085)
    ]
    conn = sqlite3.connect(db_name)  # Open connection to the database
    cursor = conn.cursor()
    
    # Insert the data into the table
    cursor.executemany("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", cities)
    conn.commit()
    conn.close()

# Step 3: Simulate population growth for 20 years
def simulate_population_growth(db_name):
    """
    Simulates population growth for the next 20 years at a 2% annual growth rate.
    Adds the simulated population data to the database.
    """
    growth_rate = 0.02  # 2% growth rate
    conn = sqlite3.connect(db_name)  # Open database connection
    cursor = conn.cursor()

    # Retrieve unique cities and their 2023 populations
    cursor.execute("SELECT DISTINCT city, population FROM population WHERE year = 2023")
    cities = cursor.fetchall()

    # Simulate population growth for each city
    for city, initial_population in cities:
        current_population = initial_population  # Start with the 2023 population
        for year in range(2024, 2044):  # Simulate for 20 years
            current_population = int(current_population * (1 + growth_rate))  # Apply 2% growth
            # Insert simulated data into the database
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                           (city, year, current_population))
    conn.commit()
    conn.close()

# Step 4: Visualize population growth
def plot_population_growth(db_name):
    """
    Prompts the user to choose a city and displays a graph of its population growth over 20 years.
    """
    conn = sqlite3.connect(db_name)  # Open database connection
    cursor = conn.cursor()

    # Retrieve a list of all cities from the database
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    # Print the available city options
    print("\nAvailable cities for visualization:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    # Allow user to select cities until they are done
    while True:
        choice = input("\nEnter the number of a city to view its population growth, or 'done' to exit: ")
        if choice.lower() == 'done':
            break  # Exit the loop if the user is done
        try:
            city_index = int(choice) - 1  # Convert user input to an index
            if 0 <= city_index < len(cities):  # Check if the input is valid
                selected_city = cities[city_index]  # Get the selected city
                # Retrieve population data for the selected city
                cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (selected_city,))
                data = cursor.fetchall()
                years, populations = zip(*data)  # Unpack data into separate lists

                # Plot the population data
                plt.figure(figsize=(10, 6))
                plt.plot(years, populations, marker='o', label=selected_city)
                plt.title(f"Population Growth of {selected_city} (2023-2043)")
                plt.xlabel("Year")
                plt.ylabel("Population")
                plt.grid(True)
                plt.legend()
                plt.show()  # Display the plot
            else:
                print("Invalid choice. Please select a valid number from the list.")
        except ValueError:
            print("Please enter a valid number or 'done' to exit.")

    conn.close()

# Main program
if __name__ == "__main__":
    # Create the database and table
    db_name = create_database()
    # Insert the initial 2023 population data
    insert_initial_data(db_name)
    # Simulate population growth for 20 years
    simulate_population_growth(db_name)
    # Visualize population growth based on user input
    plot_population_growth(db_name)
