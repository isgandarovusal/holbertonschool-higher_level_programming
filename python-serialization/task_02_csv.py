#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader uses the first row (headers) as keys for the dictionaries
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
