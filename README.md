# CSV, JSON and TXT Reader and Writer Library

This library offers streamlined and efficient methods for reading and writing data to CSV, JSON and TXT files, enabling faster and more convenient data processing.

## Functions

### `write_to_csv(data, filename, labels='None')`

This function takes two lists and adds them to a CSV file line by line. If you choose to add labels, it will add data based on how many label rows there are.

Args:
- `data` (list): A multidimensional list of data for each line.
- `labels` (list): A list of labels for each row (optional).
- `filename` (str): The name of the file.

Returns:
- None

Raises:
- Exception: If the file name is not a .csv file.

### `write_to_txt(data, filename, labels='None', char_separator='None')`

This function takes two lists and adds them to a TXT file line by line. If you choose to add labels, it will add data based on how many label rows there are. If you choose to add a character separator instead of the default `,`, it will add that character in between elements.

Args:
- `data` (list): A multidimensional list of data for each line.
- `labels` (list): A list of labels for each row (optional).
- `filename` (str): The name of the file.
- `char_separator` (str): Character separator (optional).

Returns:
- None

Raises:
- Exception: If the file name is not a .txt file.

## write_to_json(data_list, file_name, labels)

Writes a multi-dimensional list to a JSON file using specified labels.

### Args:
- `data_list` (list): A multi-dimensional list to be written to the JSON file.
- `file_name` (str): The name of the JSON file to be created/overwritten.
- `labels` (list): A list of labels to be used for each list element in the JSON file.

### Raises:
- `Exception`: If `file_name` does not end with '.json'.

### Returns:
None.

---

## Example Usage

```python
from textscribe import scribe

# Example 1: Writing to a CSV file with labels
labels = ['Name', 'Age', 'City']
data = [['John', 25, 'New York'], ['Jane', 30, 'Los Angeles']]
filename = 'example.csv'
scribe.write_to_csv(data, filename, labels=labels)

# Example 2: Writing to a TXT file with labels and a custom separator
labels = ['Name', 'Age', 'City']
data = [['John', 25, 'New York'], ['Jane', 30, 'Los Angeles']]
filename = 'example.txt'
scribe.write_to_txt(data, filename, labels=labels, char_separator='/')

# Example 3: Writing to a JSON file with labels
data_list = [
    ["John", 30],
    ["Jane", 25],
    ["Bob", 40]
]
file_name = "data.json"
labels = ["name", "age"]
scribe.write_to_json(data_list, file_name, labels)
```
### `extract_data_by_label_csv(file_name, label)`

This function extracts data from a CSV file under a specified label.

- `file_name`: The name of the CSV file to read.
- `label`: The label to look for in the CSV file.

### `extract_data_by_label_txt(file_name, label, delimiter=',')`

This function extracts data from a TXT file under a specified label. You can also provide a custom delimiter to separate elements in the TXT file.

- `file_name`: The name of the TXT file to read.
- `label`: The label to look for in the TXT file.
- `delimiter`: The character used to separate elements in the TXT file (optional, default is ',').

## extract_data_by_label_csv

This function extracts data from a CSV file under a specified label.

def extract_data_by_label_csv(file_name, label):


### Args

- file_name (str): The name of the CSV file to read.
- label (str): The label to look for in the CSV file.

### Returns

- list: A list containing all the data under the given label.

### Raises

- ValueError: If the label is not found in the CSV file.
- Exception: If the file name is not a .csv file.

## extract_data_by_label_txt

This function extracts data from a TXT file under a specified label.

def extract_data_by_label_txt(file_name, label, delimiter=','):


### Args

- file_name (str): The name of the TXT file to read.
- label (str): The label to look for in the TXT file.
- delimiter (str): The character used to separate elements in the TXT file. Default is ','.

### Returns

- list: A list containing all the data under the given label.

### Raises

- ValueError: If the label is not found in the TXT file.
- Exception: If the file name is not a .txt file.

## get_json_values(file_name, label)

Searches a JSON file for all occurrences of a specified label, and returns a list of the corresponding values.

### Args:
- `file_name` (str): The name of the JSON file to search.
- `label` (str): The label to search for.

### Raises:
- `Exception`: If `file_name` does not end with '.json'.

### Returns:
A list of the values corresponding to the specified label.


## Example Usage

```python
# Import the necessary modules

from textscribe import scribe

# Example 1: Extracting data from a CSV file
file_name_csv = 'example.csv'
label_csv = 'age'
data_csv = scribe.extract_data_by_label_csv(file_name_csv, label_csv)
print(data_csv)

# Example 2: Extracting data from a TXT file with a custom delimiter
file_name_txt = 'example.txt'
label_txt = 'age'
delimiter_txt = '|'
data_txt = scribe.extract_data_by_label_txt(file_name_txt, label_txt, delimiter_txt)
print(data_txt)

# Example 3: Extracting data from a JSON file
file_name = "data.json"
label = "name"
name_values = get_json_values(file_name, label)
print(name_values)

```

## Github Repo

https://github.com/huntert1004/textscribe





