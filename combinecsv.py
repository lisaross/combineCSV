import csv
import glob
import os

def combine_csv_files(output_filename):
    csv_files = glob.glob('*.csv')

    # Initialize an empty list to store the data from each CSV file
    combined_data = []

    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # Read and discard the header in the individual file
            if not combined_data:  # If combined data is empty, it's the first file: We keep the header
                combined_data.append(header)
            combined_data.extend(row for row in reader)  # Add the rows from the current file to combined_data

    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(combined_data)

def main():
    output_filename = 'combined.csv'
    combine_csv_files(output_filename)

if __name__ == '__main__':
    main()
