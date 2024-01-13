import pandas as pd

def clean_dataset(dataset):
    # Remove duplicate rows
    dataset = dataset.drop_duplicates()

    # Fill in missing values with the mean of each column
    dataset = dataset.fillna(dataset.mean())

    # Correct obvious errors
    dataset['column_name'] = dataset['column_name'].replace('incorrect_value', 'correct_value')

    # Additional cleaning tasks can be performed here

    return dataset

# Read the dataset
data_name = input("Enter the name of your csv file: ")
dataset = pd.read_csv("data_name"+".csv")

# Clean the dataset
cleaned_dataset = clean_dataset(dataset)

# Save the cleaned dataset to a new file
cleaned_dataset.to_csv('cleaned_dataset.csv', index=False)
print('Dataset cleaning completed successfully!')
