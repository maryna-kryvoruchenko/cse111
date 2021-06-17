def main():
  print("This program is an implementation of the Rosenberg Self-Esteem Scale.\n" 
  "This program will show you ten statements that you could possibly\n"
  "apply to yourself. Please rate how much you agree with each of the\n"
  "statements by responding with one of these four letters:")

  print(
    "Answer Key:\n"
    "D = Strongly Disagree"
    "d = Disagree"
    "a = Agree"
    "A = Strongly Agree")

  #""""
  # pos_answers = -1
  # neg_answers = -1
  
  pos_q_one = calc_pos_stm(input("I feel that I am a person of worth, at least on an equal plane with others.\n Enter D, d, a, or A: "))
  
  pos_q_two = calc_pos_stm(input("I feel that I have a number of good qualities.\n Enter D, d, a, or A: "))
  
  neg_q_three = calc_neg_stm(input("All in all, I am inclined to feel that I am a failure.\n Enter D, d, a, or A: "))
  
  pos_q_four = calc_pos_stm(input("I am able to do things as well as most other people.\n Enter D, d, a, or A: "))

  neg_q_five = calc_neg_stm(input("I feel I do not have much to be proud of.\n Enter D, d, a, or A: "))
  
  pos_q_six = calc_pos_stm(input("I take a positive attitude toward myself.\n Enter D, d, a, or A: "))

  pos_q_seven = calc_pos_stm(input("On the whole, I am satisfied with myself.\n Enter D, d, a, or A: "))
  
  neg_q_eight = calc_neg_stm(input("I wish I could have more respect for myself.\n Enter D, d, a, or A: "))
  
  neg_q_nine = calc_neg_stm(input("I certainly feel useless at times.\n Enter D, d, a, or A: "))

  neg_q_ten = calc_neg_stm(input("At times I think I am no good at all.\n Enter D, d, a, or A: "))
  #"""
    
  pos_scores = pos_q_one + pos_q_two + pos_q_four + pos_q_six + pos_q_seven

  neg_scores = neg_q_three + neg_q_five + neg_q_eight + neg_q_nine + neg_q_ten

  total_score = pos_scores + neg_scores
  
  print(f"\nYour score is {total_score}")
  print("A score below 15 may indicate problematic low self-esteem.")

#"""
def calc_pos_stm(response):
  #This function calcs the answers for questions 1, 2, 4, 6, and 7 and returns the calculation
    score = -1
    if response == "A":
      score = 3
    elif response == "a":
      score = 2
    elif response == "d":
      score = 1
    elif response == "D":
      score = 0
    else:
      print("Please enter a valid answer.")
      
    return score
#"""     
#"""
def calc_neg_stm(response):
  #This function calcs the score for questions 3, 5, 8, 9 and 10  and returns the negative-statements score
  
  score = -1
  if response == "D":
    score = 3
  elif response == "d":
    score = 2
  elif response == "a":
    score = 1
  elif response == "A":
    score = 0
  else:
    print("Please enter a valid answer.")
    
  return score
#"""

main()