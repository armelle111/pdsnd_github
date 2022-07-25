import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    add j =0
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago","new york city","washington"]
    months = ["january","february","march","april","may","june","all"]
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    i = 0
<<<<<<< HEAD
    j = 1
||||||| 51e30e7
=======
    j = 0
>>>>>>> refactoring
    while True:
        city = input("enter a name of city: ").lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)            
    while True:
        month = input("enter the month to filter, or all :").lower()
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)        
    while True:
        day = input("enter the day to filter, or all :").lower()
        if day in days:
            break          

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    print(df.head())
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Combine'] = df['Start Station']+df['End Station']
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
new york city
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    print(city,month,day)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df1 = df.groupby('month')['Trip Duration'].sum()
    #sorted_df = df1.sorted_values(by='month', ascending=True)
    print('by Month :\n', df['month'].mode()[0])
          

    # TO DO: display the most common day of week
    #df1 = df.groupby('day')['Trip Duration'].sum()
    
    print('by Day :\n', df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('Most Common Hour: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Common Start Station :\n', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Common End Station :\n', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Common Stat Station + End Station :\n', df['Combine'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\Sum travel time: ",df.groupby('month')['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("\nMean travel time: ",df.groupby('month')['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print(df.head())
    # TO DO: Display counts of user types
    #print("\nCount of USer Type ",df.count('User Types'))
    
    
    num_subscribers = df['User Type'].str.count('Subscriber').sum()
    num_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(num_subscribers)))
    print('\nNumber of customers are {}\n'.format(int(num_customers)))

    try:
        # TO DO: Display counts of gender
        num_male = df['Gender'].str.count('Male').sum()
        num_female = df['Gender'].str.count('Female').sum()
        print('\nNumber of Males are {}\n'.format(int(num_male)))
        print('\nNumber of Females are {}\n'.format(int(num_female)))
    except:
        print("Oops!  That was nogender  Try another city...")
        
    
    
    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        earlist_yb = df['Birth Year'].min()
        common_yb = df['Birth Year'].mode()[0]
        recent_yb = df['Birth Year'][1]
        print('\nEarlist Birth YEar {} , common {}, most recent {} \n'.format(earlist_yb,common_yb,recent_yb))
    except:
        print("Oops! there is no birth in the file ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart my Dear? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
