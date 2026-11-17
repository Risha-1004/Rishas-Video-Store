import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="videostore"
)

while True:
    print("\n=============================================")
    print("    RISHA'S VIDEO STORE     ")
    print("=============================================")
    print("1. Add New Movie Release")
    print("2. Edit Rental Price/Title")
    print("3. Archive/Remove Movie")
    print("4. Rental & Audience Insights")
    print("5. Generate Cinema Stats")
    print("6. Exit Application")
    print("=============================================")
    
    choice = input("Select an option (1-6): ")
    
    if choice == '1':
        print("\n--- Add New Movie ---")
        mid = int(input("Enter Movie ID: "))
        title = input("Enter Movie Title: ")
        director = input("Enter Director Name: ")
        print("Genres: [Drama] [Thriller] [Comedy] [Action] [Musical] [Romance]")
        genre = input("Enter Genre from above: ")
        price = int(input("Enter Rental Price (₹): "))
        
        cursor = conn.cursor()
        query = "INSERT INTO Movies (MovieID, Title, Director, Genre, RentalPrice, RentalCount) VALUES (%s, %s, %s, %s, %s, 0)"
        values = (mid, title, director, genre, price)
        
        cursor.execute(query, values)
        conn.commit()
        print("Movie successfully added to collection!")
        cursor.close()
        
    elif choice == '2':
        print("\n--- Edit Movie Details ---")
        mid = int(input("Enter the Movie ID to edit: "))
        
        print("What details do you want to edit?")
        print("A. Update Rental Price")
        print("B. Update Movie Title")
        editchoice = input("Select choice (A/B): ").upper()
        
        cursor = conn.cursor()
        if editchoice == 'A':
            newprice = int(input("Enter new Rental Price (₹): "))
            query = "UPDATE Movies SET RentalPrice = %s WHERE MovieID = %s"
            cursor.execute(query, (newprice, mid))
            conn.commit()
            print("Rental price updated successfully!")
            
        elif editchoice == 'B':
            newtitle = input("Enter new Movie Title: ")
            query = "UPDATE Movies SET Title = %s WHERE MovieID = %s"
            cursor.execute(query, (newtitle, mid))
            conn.commit()
            print("Movie title updated successfully!")
        else:
            print("Invalid Selection.")
        cursor.close()

    elif choice == '3':
        print("\n--- Archive Movie From System ---")
        mid = int(input("Enter the Movie ID to remove: "))
        
        cursor = conn.cursor()
        query = "DELETE FROM Movies WHERE MovieID = %s"
        cursor.execute(query, (mid,))
        conn.commit()
        
        print(f"Movie ID {mid} successfully archived from database!")
        cursor.close()

    elif choice == '4':
        query = "SELECT * FROM Movies"
        dfmovies = pd.read_sql(query, con=conn)
        
        print("\n=== Current Film Library (Pandas DataFrame) ===")
        print(dfmovies.to_string(index=False)) 
        
        print("\n=== Cinema Analytics Summary ===")
        print(f"Total Curated Titles:      {dfmovies['MovieID'].count()}")
        print(f"Average Rental Cost:       ₹{dfmovies['RentalPrice'].mean():.2f}")
        print(f"Premium Tier Rental Cost:  ₹{dfmovies['RentalPrice'].max()}")
        print(f"Total Screenings/Rentals:  {dfmovies['RentalCount'].sum()} streams")
        
        print("\n=== Total Rentals by Film Genre ===") 
        print(dfmovies.groupby('Genre')['RentalCount'].sum())
        
    elif choice == '5':
        dfmovies = pd.read_sql("SELECT * FROM Movies", con=conn)
        
        print("\n--- Cinema Visualizations ---")
        print("A. View Film Stream Performance (Horizontal Bar Chart)")
        print("B. View Audience Preference Share by Genre (Pie Chart)")
        subchoice = input("Select chart type (A/B): ").upper()
        
        if subchoice == 'A':
            plt.figure(figsize=(12, 8))
            plt.barh(dfmovies['Title'], dfmovies['RentalCount'], color='crimson', edgecolor='black')
            plt.title('Movie Lounge: Demand Distribution of Films', fontsize=14, fontweight='bold')
            plt.xlabel('Number of Times Streamed / Rented', fontsize=12)
            plt.ylabel('Movie Titles', fontsize=12)
            plt.tight_layout()
            plt.show() 
            
        elif subchoice == 'B':
            genredata = dfmovies.groupby('Genre')['RentalCount'].sum()
            
            plt.figure(figsize=(8, 8))
            plt.pie(genre_data, labels=genre_data.index, autopct='%1.1f%%', 
                    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#d5a6bd','#e6b8af','#c2c2f0'], startangle=140, 
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1})
            plt.title('Cinema Audience Genre Share Distribution', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid visual selection.")
            
    elif choice == '6':
        print("\nExiting Movie System.")
        conn.close()
        print("Thanks a lot for visiting!")
        break
        
    else:
        print("Invalid choice, please select 1-6.")
