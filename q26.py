"""
Write a program that reads a list of temperatures from a file called temps.txt, converts
those temperatures to Fahrenheit, and writes the results to a file called ftemps.txt.
"""

input_file = "temps.txt"
output_file = "ftemps.txt"
            
with open(input_file,'r') as infile:
    temp_fahrenheit =[]
    for temp in infile:
        if temp:
            temp_fahrenheit.append((float(temp)*9/5)+32)
            
with open(output_file,'w') as outfile:
    for temp1 in temp_fahrenheit:
        outfile.write(str(temp1)+"\n")
        
print(f"converted temperatures saved in {output_file}")