import csv
import json
def write_to_json(data_list, file_name, labels):
    """
    Writes a multi-dimensional list to a JSON file using specified labels.
    :param data_list: a multi-dimensional list to be written to the JSON file
    :param file_name: the name of the JSON file to be created/overwritten
    :param labels: a list of labels to be used for each list element in the JSON file
    """
    if file_name.endswith('.csv'):
        json_data = []
        
        for data in data_list:
            
            formatted_dict = {}
            
            for i in range(len(labels)):
            
                formatted_dict[labels[i]] = data[i]
            
            json_data.append(formatted_dict)
        
        with open(file_name, 'w') as f:
            json.dump(json_data, f)
    else:
        raise Exception("File Name is not a .json file")


def get_json_values(file_name, label):
    """
    Searches a JSON file for all occurrences of a specified label, and returns a list of the corresponding values.
    :param file_name: the name of the JSON file to search
    :param label: the label to search for
    :return: a list of the values corresponding to the specified label
    """
    if file_name.endswith('.csv'):
    
        with open(file_name, 'r') as f:
            json_data = json.load(f)
        
        values = []
        
        for data_dict in json_data:
            
            if label in data_dict.keys():
                
                values.append(data_dict[label])
        
        return values
    else:
        raise Exception("File Name is not a .json file")

def extract_data_by_label_csv(file_name, label):
    if file_name.endswith('.csv'):
        data = []

        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)  # Get the header row

            if label not in headers:
                raise ValueError(f"Label '{label}' not found in the CSV file.")

            label_index = headers.index(label)

            for row in csv_reader:
                data.append(row[label_index])

        return data
    else:
        raise Exception("File Name is not a .csv file")

def extract_data_by_label_txt(file_name, label, delimiter=','):

    """
    Extracts data from a TXT file under a specified label.

    Args:
        file_name (str): The name of the TXT file to read.
        label (str): The label to look for in the TXT file.
        delimiter (str): The character used to separate elements in the TXT file. Default is ','.

    Returns:
        list: A list containing all the data under the given label.

    Raises:
        ValueError: If the label is not found in the TXT file.
    """
    if file_name.endswith('.txt'):
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
    else:
        raise Exception("File Name is not a .csv file")

def write_to_csv(data, filename,labels='None'):
    '''
    Takes two lists and adds them to CSV line by line.

    If you choose to add labels it will add data based on how many label rows there are.

    :param data: Multidementional list of data for each line.
    :type data: list

    :param labels: List of labels for each row.
    :type labels: list

    :param filename: Name of file.
    :type filename: string

    '''
    if filename.endswith('.csv'):
        if labels !='None':
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(labels)
                for row in data:
                    row_data = []
                    for i in range(len(labels)):
                        if i < len(row):
                            row_data.append(row[i])
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
                    print("Successfully added to CSV")
        else:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
            
                for row in data:
                    row_data = []
                    for i in range(len(data)):
                        if i < len(row):
                            row_data.append(row[i])
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
                    print("Successfully added to CSV")
    else:
        raise Exception("File Name is not a .csv file")

def write_to_txt(data, filename,labels='None',char_separator='None'):
    '''
    Takes two lists and adds them to CSV line by line.

    If you choose to add labels it will add data based on how many label rows there are.

    If you choose to add character seperater instead of the default , it will add that charater in between elements

    :param data: Multidementional list of data for each line.
    :type data: list

    :param labels: List of labels for each row.
    :type labels: list

    :param filename: Name of file.
    :type filename: string

    :param char_seperator: Charter Separator.
    :type char_seperator: string

    '''
    if filename.endswith('.txt'):
        if char_separator == 'None' or char_separator == ',':
            if labels != 'None':
                with open(filename, 'w') as f:
                    f.write(','.join(labels) + '\n')
                    for row in data:
                        f.write(','.join(str(x) for x in row) + '\n')
                        print("Successfully added to TXT")
            else:
                with open(filename, 'w') as f:
                    for row in data:
                        f.write(','.join(str(x) for x in row) + '\n')
                        print("Successfully added to TXT")
        else:
            if labels != 'None':
                with open(filename, 'w') as f:
                    f.write(','.join(labels) + '\n')
                    for row in data:
                        f.write(','.join(str(x) for x in row) + '\n')
                with open(filename, 'r') as f:
                    text = f.read()
                text = text.replace(',', char_separator)
                with open(filename, 'w') as f:
                    f.write(text)
                print("Successfully added to TXT")
            else:
                with open(filename, 'w') as f:
                    
                    for row in data:
                        f.write(','.join(str(x) for x in row) + '\n')
                with open(filename, 'r') as f:
                    text = f.read()
                text = text.replace(',', char_separator)
                with open(filename, 'w') as f:
                    f.write(text)
                print("Successfully added to TXT")
    else:
        raise Exception("File Name is not a .txt file")