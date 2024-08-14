# text_file = open("week-8/test.txt", "x") # creating a new file
text_file = open("week-8/test.txt", "r")
file_content = text_file.read()
print(file_content)
text_file.close()

text_file = open("week-8/test.txt", "a")
text_file.write("\nGod is the greatest")
text_file.close()

print("=======================================")

text_file = open("week-8/test.txt", "r")
file_content = text_file.read()
print(file_content)
text_file.close()

text_file = open("week-8/test2.txt", "w")
text_file.write("Programming is fun")
text_file.close()

print("=======================================")

text_file = open("week-8/test.txt", "r")
file_content = text_file.read()
print(file_content)

text_file.close()