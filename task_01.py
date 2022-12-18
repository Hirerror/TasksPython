class Task:

    def is_palindrome(string):
        flist = []
        forbdn = ("? ! : ; - () [] ... / , [ ] ( ) & * ` ")
        flist = forbdn.split(" ")
        fcount = forbdn.count(" ")

       
        string.encode("ascii",errors="replace")

        for f in range (0,fcount):
            string = string.replace(flist[f],"")

        string = string.lower() 

        concatstr = "".join(string.split())
        strcount = (concatstr.count(""))

        n = 0
        count = (strcount - 1) / 2
        i = strcount - 2

        if(strcount - 1 > 0):
            while int(count) != 0:
                   if concatstr[n] != concatstr[int(i)]:
                       bol = False
                       count = 0
                   else: n = n + 1; i = i - 1;count = count - 1; bol = True
            return bol
        else: print("Wrong")

print("This is a program for searching for palindromes without taking into account case and some characters.")
t = Task
print(t.is_palindrome("A man, a plan, a canal -- Panama"))
print(t.is_palindrome("Madam, I`m Adam!"))
print(t.is_palindrome("333"))
print(t.is_palindrome("123354"))