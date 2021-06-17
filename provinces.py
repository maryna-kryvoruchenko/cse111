import csv
from typing import Counter 

def main():
    data = read_lines("provinces.csv")
    data.pop(0)
    del data[-1]
    data = [item.replace("AB", "Alberta") for item in data]
    alberta_count = data.count("Alberta")
    print(data)
    print(f"Alberta occurs {alberta_count} times in the modified list.")

def read_lines(filename):
    data_list = []

    with open(filename, "rt") as data:
        for line in data:
            clean_line = line.strip()
            data_list.append(clean_line)
    
    return data_list
             

if __name__ == "__main__":
    main()