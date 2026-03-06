import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}   
df = pd.DataFrame(data) 
# Display the DataFrame
print(df)
# Accessing columns
print(df['Name']) # Output: 0      Alice
# Accessing rows
print(df.loc[0]) # Output: Name    Alice
# Filtering data
adults = df[df['Age'] >= 30]
print(adults) # Output:      Name  Age         City
# Output: 1    Bob   30  Los Angeles
# Output: 2 Charlie   35      Chicago   
