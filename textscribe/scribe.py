import csv
import json

def write_to_json(data_list, file_name, labels):
    """
    Writes a multi-dimensional list to a JSON file using specified labels.
    :param data_list: a multi-dimensional list to be written to the JSON file
    :param file_name: the name of the JSON file to be created/overwritten
    :param labels: a list of labels to be used for each list element in the JSON file
    """
    if not file_name.endswith('.json'):
        raise Exception("File Name is not a .json file")

    json_data = []
    for data in data_list:
        formatted_dict = {}
        for i in range(len(labels)):
            formatted_dict[labels[i]] = data[i]
        json_data.append(formatted_dict)

    with open(file_name, 'w') as f:
        json.dump(json_data, f)


def get_json_values(file_name, label):
    """
    Searches a JSON file for all occurrences of a specified label, and returns a list of the corresponding values.
    :param file_name: the name of the JSON file to search
    :param label: the label to search for
    :return: a list of the values corresponding to the specified label
    """
    if not file_name.endswith('.json'):
        raise Exception("File Name is not a .json file")

    with open(file_name, 'r') as f:
        json_data = json.load(f)

    values = []
    for data_dict in json_data:
        if label in data_dict.keys():
            values.append(data_dict[label])

    return values


def extract_data_by_label_csv(file_name, label):
    """
    Extracts data from a CSV file under a specified label.
    :param file_name: The name of the CSV file to read.
    :param label: The label to look for in the CSV file.
    :return: A list containing all the data under the given label.
    """
    if not file_name.endswith('.csv'):
        raise Exception("File Name is not a .csv file")

    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Get the header row

        if label not in headers:
            raise ValueError(f"Label '{label}' not found in the CSV file.")

        label_index = headers.index(label)
        data = [row[label_index] for row in csv_reader]

    return data


def extract_data_by_label_txt(file_name, label, delimiter=','):
    """
    Extracts data from a TXT file under a specified label.
    :param file_name: The name of the TXT file to read.
    :param label: The label to look for in the TXT file.
    :param delimiter: The character used to separate elements in the TXT file. Default is ','.
    :return: A list containing all the data under the given label.
    """
    if not file_name.endswith('.txt'):
        raise Exception("File Name is not a .txt file")

    data = []
    with open(file_name, mode='r') as txt_file:
        headers = txt_file.readline().strip().split(delimiter)

        if label not in headers:
            raise ValueError(f"Label '{label}' not found in the TXT file.")

        label_index = headers.index(label)
        for line in txt_file:
            row = line.strip().split(delimiter)
            data.append(row[label_index])

    return data




def write_to_csv(data, filename, labels=None):
    """
    Writes data to a CSV file. Each row of the data list is written as a separate row in the file.

    :param data: List of lists containing the data to write
    :param filename: Name of the CSV file to write to
    :param labels: Optional list of column labels to include in the CSV file
    """
    if not filename.endswith('.csv'):
        raise Exception("File Name is not a .csv file")

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        if labels is not None:
            writer.writerow(labels)

        for row in data:
            writer.writerow(row)

    print("Successfully added to CSV")

def write_to_txt(data, filename, labels=None, char_separator=','):
    """
    Writes data to a text file. Each row of the data list is written as a separate row in the file.

    :param data: List of lists containing the data to write
    :param filename: Name of the text file to write to
    :param labels: Optional list of column labels to include in the text file
    :param char_separator: Optional character separator to use between columns (default is ',')
    """
    if not filename.endswith('.txt'):
        raise Exception("File Name is not a .txt file")

    with open(filename, 'w') as f:
        if labels is not None:
            f.write(char_separator.join(labels) + '\n')

        for row in data:
            f.write(char_separator.join(str(x) for x in row) + '\n')

    print("Successfully added to TXT")
