from string import ascii_letters
class Task:

    def multiply_numbers(inp = None):

        acnum = "1234567890"
        product = 1
        if isinstance(inp, (list)):
            x = ''
            for n in range(0,len(inp)):
                x += str(inp[n])
            inp = x

        if isinstance(inp, (float)):
            inp = str(inp)

        if isinstance(inp, (int,str)):
            if(len(inp.strip(ascii_letters)) == 0):
                return None
            else:
                for i in inp:
                    if len(i.strip(acnum)) == 0:
                        product *= int(i)

                return product
        else:
            return None

t = Task

print(t.multiply_numbers()) # => None
print(t.multiply_numbers('ss')) # => None
print(t.multiply_numbers('1234')) # => 24
print(t.multiply_numbers('sssdd34')) # => 12
print(t.multiply_numbers(2.3)) # => 6
print(t.multiply_numbers([5, 6, 4])) # => 120)