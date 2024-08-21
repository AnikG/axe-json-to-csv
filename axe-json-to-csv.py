#!/usr/bin/env python
""" Convert axe DevTool result export JSON to CSV

This script reads a JSON file that was exported from the axe browser 
extension and converts it to a CSV file. The JSON is expected to have
the issues listed as an array of objects under a key called 'allIssues'.

The JSON file is the only argument required to run this script.

The script expects pandas to be installed. If it is not installed, you can install it using `pip install pandas`.

The output CSV file will be saved in the same directory as the input JSON file and will have the same name as the input JSON file, but with a .csv extension.

"""

import json
import pandas as pd

def read_json_file(json_file_name):
  """Read the JSON file and return the data as a dictionary"""
  with open(json_file, 'r') as f:
    data = json.load(f)
  return data

def flatten_array_of_objects(data, root_node_key):
  """Flatten an array of objects in a list of dictionaries"""
  flattened_data = pd.json_normalize(data[root_node_key])
  return flattened_data

def main(json_file_name):
  data = read_json_file(json_file_name)
  output_file_name = json_file_name.replace('.json', '.csv')

  flattened_data = flatten_array_of_objects(data, 'allIssues')

  flattened_data.to_csv(output_file_name, index=False)
  print(f"{len(data['allIssues'])} issues found and written to {output_file_name}")

if __name__ == "__main__":
  # read command line arguments
  import argparse
  parser = argparse.ArgumentParser(description='Convert axe DevTool result export JSON to CSV')
  parser.add_argument('json_file', type=str, help='The JSON file to convert - this would have been exported from the axe browser extension')
  args = parser.parse_args()
  json_file = args.json_file # expect argument like: './data/turo.com-2024-08-20.json'

  main(json_file)
