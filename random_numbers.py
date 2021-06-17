import random as r

def main():
  """Creates a list and appends random numbers onto the list"""
  randnums = [16.2, 75.1, 52.3]
  print(f"randnums {randnums}")
  
  #Adds 1
  append_random_numbers(randnums)
  print(f"randnums {randnums}")

  #Adds 3
  append_random_numbers(randnums, 3)
  print(f"randnums {randnums}")

  randwords = []

  append_random_words(randwords,5)
  print(f"randwords {randwords}")

def append_random_numbers(numbers_list, quantity=1):
  for _ in range(quantity):
    random_num = r.uniform(0,100)
    rounded_num = round(random_num, 1)
    numbers_list.append(rounded_num)


def append_random_words(words_list, quantity=1):
  #
  
  for _ in range(quantity):
    words = ['peaches','pizza','pelmeni','join', 'love', 'smile', 'love', 'cloud', 'head', 'asparagus', 'banana', 'orange', 'γύρος', 'bacon', 'chocolate', 'mango', 'blueberry', ]
    word = r.choice(words)
    words_list.append(word)
    

if __name__ == "__main__":
  main()