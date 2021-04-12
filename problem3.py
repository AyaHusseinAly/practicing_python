
def comparehalves(input_string):
   str_len = len(input_string)
   global front
   global back
   if (str_len % 2 != 0):
      front = input_string[0:int(str_len / 2)+1]
      back = input_string[(int(str_len / 2)) + 1:]
   else:
      front = input_string[0:int(str_len / 2)]
      back = input_string[int(str_len / 2):]



string_a = input("Enter First String: ")
string_b = input("Enter Second String: ")

comparehalves(string_a)
a_front=front
a_back=back
comparehalves(string_b)
b_front=front
b_back=back

print(a_front+b_front+a_back+b_back)
