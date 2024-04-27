import os

import pandas as pd

from Persistence.DetailedYellowtailRecord import DetailedYellowtailRecord
from Persistence.YellowtailFileIO import YellowtailFileIO

# Configure Pandas display options for improved readability of output
pd.set_option('display.max_columns', None)  # Shows all columns
pd.set_option('display.max_rows', None)  # Shows all rows
pd.set_option('display.width', None)  # Utilizes maximum width of the console
pd.set_option('display.max_colwidth', None)  # Shows full content of each column


class YellowtailBusinessLogic:
    """
    This class handles the logic of all the program functionalities in this application. This class provides implementations
    for loading, saving, selecting, inserting, updating and deleting the CSV records.
    Written by: Yiting Yao.

    """
    updated_csv_file_path = "../Updated_YellowtailRecords_File.csv"

    def __init__(self):
        self.yellowtailfile_IO = YellowtailFileIO()
        # Initialize the list to an empty list to avoid 'NoneType' errors
        self.yellowtail_records_list = []
        try:
            self.load_yellowtail_records()
        except FileNotFoundError as e:
            print(f"An error occurred while loading records: {e}")  # Load original records

    def save_yellowtail_records(self):
        """
        Saves the YellowtailRecord(s) in the list to the appropriate csv file, based on their type.
        """
        simplified_records = [r for r in self.yellowtail_records_list if not isinstance(r, DetailedYellowtailRecord)]
        detailed_records = [r for r in self.yellowtail_records_list if isinstance(r, DetailedYellowtailRecord)]

        if simplified_records:
            self.yellowtailfile_IO.write_simplified_yellowtail_records(simplified_records)
        if detailed_records:
            self.yellowtailfile_IO.write_detailed_yellowtail_records(detailed_records)

    def load_yellowtail_records(self):
        """
        If updated records exist and are not empty, loads from the updated CSV file.
        Otherwise, loads from the original CSV file.
        """
        try:
            if os.path.exists(self.updated_csv_file_path) and os.path.getsize(self.updated_csv_file_path) > 0:
                # checks whether the file specified by the path exists and contains more than zero bytes (not empty)
                self.yellowtail_records_list = self.yellowtailfile_IO.read_updated_yellowtail_records()
            else:
                self.yellowtail_records_list = self.yellowtailfile_IO.read_original_yellowtail_records()
                # is an attribute of the instance that will hold the yellowtail fish records in memory. After loading
                # is performed, other parts of the program can then use self.yellowtail_records_list to access the
                # data and perform various operations like displaying records, updating records, or saving records.

            # If both calls return None, initialize the records list as empty, otherwise it will raise TypeError
            if self.yellowtail_records_list is None:
                self.yellowtail_records_list = []
        except FileNotFoundError:
            print("Error: The specified dataset file could not be found.")
            self.yellowtail_records_list = []  # Ensure the list is initialized

    def get_all_yellowtail_records(self):
        """
        This function retrieves the list of YellowtailRecord(s)
        :return: List of YellowtailRecord(s)
        """
        return self.yellowtail_records_list

    def get_single_specific_yellowtail_record(self, yellowtail_record_id):
        """
        This function retrieves a single specific YellowtailRecord from the list of records based on the id from user input.
        :param yellowtail_record_id: the YellowtailRecord ID to be specified by user.
        :return: the specified YellowtailRecord by ID
        """
        # Can name this anything, but it is a YellowtailRecord type object.
        yellowtail_record = self.yellowtail_records_list[yellowtail_record_id - 1]
        # Index starts at 1 for an array.
        # Self is always the business logic object which is calling yellowtail_records_list.
        return yellowtail_record

    def insert_yellowtail_record(self, yellowtail_record):
        """
        This function inserts a single YellowtailRecord to the record object list
        :param yellowtail_record: the YellowtailRecord to be added
        """
        self.yellowtail_records_list.append(yellowtail_record)
        # yellowtail_records_list is the array
        # CRUD uses the array object, loading and saves uses persist object

    def update_yellowtail_record(self, yellowtail_record, yellowtail_record_id):
        """
        This function updates a single specified YellowtailRecord in the record object list.
        :param yellowtail_record: the YellowtailRecord to update
        :param yellowtail_record_id: the YellowtailRecord ID specified by user input.
        """
        # Convert yellowtail_record_id to 0-based index
        index = yellowtail_record_id - 1
        if 0 <= index < len(self.yellowtail_records_list):
            self.yellowtail_records_list[index] = yellowtail_record
            # Optionally save and reload records here if needed
            self.save_yellowtail_records()
            self.load_yellowtail_records()
        else:
            print(f"Error: Invalid ID {yellowtail_record_id}. Please enter a valid ID.")

    def delete_yellowtail_record(self, yellowtail_record_id):
        """
        This function deletes a single specified YellowtailRecord in the record object list.
        :param yellowtail_record_id: the YellowtailRecord ID in specified by user input.
        """
        self.yellowtail_records_list.pop(yellowtail_record_id - 1)
        # pop is to remove in python

    def search_records(self):
        """
        This function searches existing records by month or year. It prompts the user for a year and a month,
        then checks for their existence in the DataFrame loaded from the updated CSV file.
        """
        df = pd.read_csv(self.updated_csv_file_path)  # Now correctly referencing the class variable
        year = input("Please enter the year to search for: ").strip()
        month = input("Please enter the month to search for: ").strip()

        # This checks if the year and month exist in the DataFrame.
        year_exists = year in df['year'].astype(str).unique()  # Update the column name if necessary
        month_exists = month in df['month'].astype(str).unique()  # Update the column name if necessary

        # Error handling and error messages for non-existent year or month in the records.
        if year and not year_exists:
            print(f"Sorry. The year you're looking for: year {year} does not exist in the records.")
            return
        if month and not month_exists:
            print(f"Sorry. The month you're looking for: month {month} does not exist in the records.")
            return

        # Creates a list to hold the query conditions. If the user has provided a year and/or month,
        # the conditions are appended to the query list.
        query = []
        if year:
            query.append(f"year == {year}")
        if month:
            query.append(f"month == {month}")

        # If the query list is not empty, the conditions are joined into a single string with an 'AND' operator (&)
        # and passed to df.query() to filter the DataFrame. The filtered DataFrame filtered_df is checked to see if
        # it's empty. If not, the search results are printed. If the query list is empty (no year or month provided),
        # it prints all records by default.

        if query:
            query_str = " & ".join(query)
            filtered_df = df.query(query_str)
            if filtered_df.empty:
                print("No records found matching the criteria specified.")
            else:
                print("Search results:")
                print(filtered_df)
        else:
            print("No search criteria provided. Displaying all records:")
            print(df)
