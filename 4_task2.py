
initial_input = input('enter text to write to output.txt:')

with open ('output txt','w') as file:
    file.write(initial_input + '\n')

    append_input=input ('Enter additional text to append to output.txt:')

    with open('output.txt','a') as file:
        file.write(append_input +'\n')
        print("\n final content of out.txt:")
        with open('output.txt','r') as file:
            for line in file:
             print(line.strip ())
             




