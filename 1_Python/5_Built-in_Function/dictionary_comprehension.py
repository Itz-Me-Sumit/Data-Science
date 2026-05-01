# {key_expresion : value_expresion for item in iterable  if condition}

name = ["Sumit","Shivam","Shivang","Shiva"]
score = [10 , 32 , 13 , 32]

dic_comprehension = {name : score for name , score in zip(name,score)}
print(dic_comprehension)