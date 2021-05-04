def get_file_ready(file):
    # read file and split chars in list
    f = list(file.read())
    # remove Punctuation marks and Empty lines
    for i in range(0, len(f)):
        if f[i] == "," or f[i] == ":" or f[i] == "-" or f[i] == '\n' or f[i] == "!" or f[i] == "@" or f[i] == "#" or f[
            i] == "$" or f[i] == "%" or f[i] == "^" or f[i] == "&" or f[i] == "*" or f[i] == "(" or f[i] == ")" or f[
            i] == "+" or f[i] == "=" or f[i] == "\\" or f[i] == "/" or f[i] == "_" or f[i] == ">" or f[i] == "<" or f[
            i] == "." or f[i] == "{" or f[i] == "}" or f[i] == "|" or f[i] == "\"" or f[i] == ";" or f[i] == "`" or f[
            i] == "”" or f[i] == "“" or f[i] == "€" or f[i] == "â" or f[i] == "œ" or f[i] == "\u200c" or f[
            i] == "\xa0" or f[i] == "?":
            f[i] = " "

    # remove Extra white spaces
    c = 1
    while c != 0:
        i = 0
        c = 0
        for j in f:
            if f[i] == " " and f[i - 1] == " ":
                f.pop(i)
                c = c + 1
            i = i + 1

    # fix ™
    # before fix ™s , after fix 's
    i = 0
    for j in f:
        if f[i] == "™":
            f[i] = "\'"
            f.pop((i - 1))
        i = i + 1

    # remove last space
    if f[len(f) - 1] == " ":
        f.pop(len(f) - 1)

    # Merge chars to string then make string in lowercase then split words in list
    f = "".join(f)
    f = f.lower()
    f = f.split(' ')
    return f


def common_words(list1, list2):
    # convert list to set
    set1 = set(list1)
    set2 = set(list2)
    # Returns Common words between set 1 and set 2
    return set1 & set2


# Open Files
file1 = open("HP Lovecraft’s Beyond the Wall of Sleep.txt", "r")
file2 = open("Jane Austin’s Pride and Prejudice.txt", "r")

# Clean Files
ListOfFile1 = get_file_ready(file1)
ListOfFile2 = get_file_ready(file2)

# find Common Words Between Files
CommonWords = common_words(ListOfFile1, ListOfFile2)
print("The Common Words Between The Two Books is: \n", CommonWords)

# Close Files
file1.close()
file2.close()

#to can use by cmd
#close=input("\nPress Enter to close The Program...")
