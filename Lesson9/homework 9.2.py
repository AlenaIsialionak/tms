#str1, str2, str3, str4 = input(), input(), input(), input()
str1, str2, str3, str4 = 'world', 'word', 'quiet', 'tired'
with open("my_file.txt", "w", encoding="utf-8") as file:
    new_line = [
        line.rstrip('\n') + '\n' for line in (str1, str2)
    ]
    file.writelines(new_line)
with open("my_file.txt", "a", encoding="utf-8") as file:
    new_line = [
        line.rstrip('\n') + '\n' for line in (str3, str4)
    ]
    file.writelines(new_line)


