class Task:
    def count_words(ustr):
        x = ',-!@#$%^&*()=+/?.><:;"|'
        for i in x :
             ustr = ustr.replace(i,'')
        ustr = ustr.lower()
        ustr = ustr.split()
        wordlist = []
        countwl = []

        ldict = {}

        for w in ustr:

            if w not in wordlist:
                wordlist.append(w) 
                countwl.append(ustr.count(w))

            ldict = dict(zip(wordlist, countwl))
        return ldict
t = Task
print(t.count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(t.count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}

