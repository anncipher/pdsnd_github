import time
import pandas as pd
import numpy as np

def load_data(city):
    # Load the data for the specified city
    data_file = f"{city.lower().replace(' ', '_')}.csv"
    df = pd.read_csv(data_file)
    
    return df

def get_user_filters():
    
     """
    # Get user input for month and day

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month = input("Enter the month (all, January, February, ..., June): ").title()
    day = input("Enter the day (all, Monday, Tuesday, ..., Sunday): ").title()

    return month, day

def filter_data(df, month, day):
    # Apply filters based on user input
    if month != 'All':
        df = df[df['Month'] == month]
        
    if day != 'All':
        df = df[df['Day of Week'] == day]
        
    return df

def print_statistics(df):
    # Print various statistics based on the filtered data
    print("\nStatistics:")
    
    """Displays statistics on the most frequent times of travel."""

    # Popular month
    popular_month = df['Month'].mode()[0]
    # Popular day
    popular_day = df['Day of Week'].mode()[0]
    # Popular hour
    df['Hour of Day'] = pd.to_datetime(df['Start Time']).dt.hour
    popular_hour = df['Hour of Day'].mode()[0]
    
    print('Most Common Month:', popular_month)
    print('Most Common Day of Week:', popular_day)
    print('Most Common Hour of Day:', popular_hour)

    """Displays statistics on the most popular stations and trip."""
    # Popular start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"\nMost Common Start Station in {city.title()}: {popular_start_station}")
    
    # Popular end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most Common End Station in {city.title()}: {popular_end_station}")
    
    """Displays statistics on the total and average trip duration."""
    # Popular trip
    # Create column "Trip" by concatenating 'Start Station' and 'End Station'
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print(f"Most Common Trip from Start to End in {city.title()}:', {popular_trip}")
    
    # Total trip duration
    total_trip_duration = df['Trip Duration'].sum()
    print(f"\nTotal Travel Time in {city.title()}: {total_trip_duration} seconds")
    
    # Average trip duration
    average_trip_duration = df['Trip Duration'].mean()
    print(f"Average Total Travel Time in {city.title()}: {average_trip_duration} seconds")
  
    """Displays statistics on bikeshare users. Statistics will be calculated using NumPy."""
    # Count each user type
    user_type_counts = df['User Type'].value_counts()
    print("\nUser Type Counts:")
    print(user_type_counts)
    
    if 'Gender' in df.columns:
        # Count each gender (available for NYC and Chicago)
        gender_counts = df['Gender'].value_counts()
        print("\nGender Counts:")
        print(gender_counts)
    else:
        print("\nGender information not available for this city.")
        
    if 'Birth Year' in df.columns:
        # Find the earliest, most recent, and most common year of birth (available for NYC and Chicago)
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        
        print("\nBirth Year Stats:")
        print(f"Earliest Birth Year: {earliest_birth_year}")
        print(f"Most Recent Birth Year: {most_recent_birth_year}")
        print(f"Most Common Birth Year: {most_common_birth_year}")
    else:
        print("\nBirth year information not available for this city.")
   
def display_raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # Ask user if they want to see 5 lines of raw data
    show_raw_data = input("Do you want to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
    
    # Display 5 lines of raw data if the user says yes
    if show_raw_data == 'yes':
        print("\nRaw Data:")
        print(df.head())
    elif show_raw_data == 'no':
        pass
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


def ask_show_raw_data():
    while True:
        user_input = input("Do you want to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()
    if user_input in ['yes', 'no']:
        return user_input
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
def ask_restart():
    # Ask user if they want to restart
    return input("Do you want to restart and analyze data for a different city, month, or day? Enter 'yes' or 'no': ").lower()

if __name__ == "__main__":
    restart = 'yes'
    while restart == 'yes':
        city = input("Enter the city(Chicago, New York City, or Washington):").lower()
        if city in ['chicago', 'new york city', 'washington']:
            df = load_data(city)
            
            # Assuming there is a 'Month' and 'Day of Week' column in the DtaFrame
            df['Month'] = pd.to_datetime(df['Start Time']).dt.strftime('%B')
            df['Day of Week'] = pd.to_datetime(df['Start Time']).dt.strftime('%A')
       
            month, day = get_user_filters()
            df_filtered = filter_data(df, month, day)
            
            print("\nFiltered Data:")
            print(df_filtered.head())
           
            print_statistics(df_filtered)
            # Display raw data based on user input
            display_raw_data(df_filtered)
   
display_rows_increments(df_filtered)
            """ Ask user if they want to see more raw data """
            
while ask_show_raw_data() =='yes':
            display_raw_data(df_filtered)
            # Ask user if they want to restart
            restart = ask_restart()
else:
    print("Thanks for using the Bikeshare Analysis tool. Have a great day!")

    print ("Goodbye!")