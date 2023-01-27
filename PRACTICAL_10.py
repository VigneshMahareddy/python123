# Python program to count number of vowels,
#newlines and character in textfile
def counting(filename):
    txt_file = open(filename, "r")
    vowel = 0
    line = 0
    character = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    for alpha in txt_file.read():
        if alpha in vowels_list:
            vowel += 1   
        elif alpha not in vowels_list and alpha != "\n":
            character += 1             
        elif alpha == "\n":
            line += 1
    print("Number of vowels in ", filename, " = ", vowel)
    print("New Lines in ", filename, " = ", line)
    print("Number of characters in ", filename, " = ", character)
counting('Myfile.txt')
