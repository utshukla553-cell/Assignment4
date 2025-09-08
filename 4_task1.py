try:
    with open('sample.txt','r') as file:
        for line in file:
         print(line.strip())
except FileNotFoundError:
          print("Enter:The file 'sample.txt' dose not exis")  
      
