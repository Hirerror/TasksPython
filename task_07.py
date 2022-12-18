list = ["Cars", "For", "Potatoes", "racs", "four", "Scar", "Creams", "Scream"]
class Tasks:

    def combine_anagrams(word_list):

        str1 = ""
        for i in range(0,len(word_list)):
            str1 += word_list[i] + " "
        str1 = str1.lower()
        word_lisst = str1.split()
        finish_list = []
        temp_wl = word_lisst.copy()
        wd_count = word_lisst[0].count("")
        temp = [] 

        for w in word_lisst:

            for w2 in temp_wl:

                if(w.count("") == w2.count("")):

                    if(w == w2):
                        continue
                    if(len(w.strip(w2)) == 0):

                        if(wd_count != w.count("")):
                            temp = []
                        fn = len(finish_list)
                        if(fn == 0):
                            temp.append(w)
                            temp.append(w2)
                        for f in range(0,fn):
                            if(w not in finish_list[f]):
                                temp.append(w)
                            if(w2 not in finish_list[f]):
                                temp.append(w2)

                        if(w in word_lisst):
                            word_lisst.remove(w)
                            wd_count = w.count("")
                        if(w2 in word_lisst):
                            word_lisst.remove(w2)

                        if(temp not in finish_list):
                            finish_list += [temp]

        for i in range(0,len(word_lisst)):
            temp = [word_lisst[i]]
            finish_list.insert(0,temp)
        
        return finish_list

t = Tasks
print(t.combine_anagrams(list))
