def start():
  trans_no = input("Please enter a transaction number: ")
  first_alt = list(str(trans_no[-1::-2]))
  second_alt = list(str(trans_no[-2::-2]))
  
  total = sum([int(x) for x in first_alt]) * 3 + sum([int(x) for x in second_alt])
  
  check_digit = (total//10 + 1) * 10 - total
  if check_digit == 10:
    check_digit = 0
  
  #print(first_alt)
  #print(second_alt)
  
  #print(total)
  #print(check_digit)
  
  print("The check digit is " + str(check_digit))
  print("Your full transaction number is " + str(trans_no) + '-' + str(check_digit))

def check_digit_oneline():
  trans_no = input("Please enter a transaction number: ")
  
  # rewrite this line, asshole it's not readable!
  check_digit = ((sum([int(x) for x in list(str(trans_no[-1::-2]))]) * 3 + sum([int(x) for x in list(str(trans_no[-2::-2]))]))//10 + 1) * 10 - (sum([int(x) for x in list(str(trans_no[-1::-2]))]) * 3 + sum([int(x) for x in list(str(trans_no[-2::-2]))]))
  
  if check_digit == 10:
    check_digit = 0
  
  print("Your checkdigit is " + str(check_digit))

#start()
check_digit_oneline()
