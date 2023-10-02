def fibotete(lastResult, currentNumber, userInput, count):

   if count != userInput:
      count += 1
      result = lastResult + currentNumber
      print(f"f({count}) = {result}")
      fibotete(currentNumber,result,userInput,count)

fibotete(1,0,int(input()), 0)