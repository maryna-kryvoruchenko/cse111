import csv 

def main():
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    product_data = read_products("products.csv", PRODUCT_INDEX)
    request_data = process_request("request.csv")
    #intersection_set = product_data.intersection(request_data)
    product_data.intersection(request_data)
    for item in product_data.intersection(request_data):
        print(item)
    print(product_data)
    #print(intersection_set)

def read_products(filename, key_index):
    products = {}
    with open(filename, "rt") as products_list:
        reader = csv.reader(products_list)
        next(reader)
        
        for item in reader:
            key = item[key_index]
            products[key] = item

    return products

def process_request(filename):
    with open(filename, "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row in reader:
            print(row)



if __name__ == "__main__":
    main()
