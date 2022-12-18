d1 = { 13:'D',3:'s',8:10,1:'3,14',24:'o',100:'o'}
d2 = {24:'i',48:'s',53:'c'}

class Task:
    def connect_dicts(dict1, dict2):
        connd = {}
        sumd1= 0; sumd2 = 0;
        for key in dict1:
            sumd1 = sumd1 + key
        for key in dict2:
            sumd2 = sumd2 + key
        if(sumd1 > sumd2):
            connd.update(dict2);
            connd.update(dict1)
        else:
            connd.update(dict1);
            connd.update(dict2)
        conndend = connd.copy()
        for key in connd:
            if(key<10):
               del conndend[key]
        sorted_connd = sorted(conndend.items(),key = lambda x: x[0])
        return dict(sorted_connd)
t = Task
print(t.connect_dicts(d1,d2))
print(t.connect_dicts({ 14: "a", 12: "b" }, { 11: "c", 15: "a" })) # =>{ "c": 11, "b": 12, "a": 15 }
print(t.connect_dicts({ 2: "a", 12: "b" }, { 11: "c", 5: "e" })) # =>{ "c": 11, "b": 12 }
