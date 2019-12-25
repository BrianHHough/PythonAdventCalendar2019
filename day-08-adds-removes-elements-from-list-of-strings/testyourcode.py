#Encoding: UTF-8
import re

#Encode a text with base64
def base64Encode(text):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	bit_str=""	
	base64_str=""

	#Loop through all chars concatenate them as binary string
	for char in text:
		bin_char = bin(ord(char)).lstrip("0b")
		bin_char = (8-len(bin_char))*"0" + bin_char
		bit_str += bin_char

	#Add zero till text-length is divideable through 3
	while (((len(text)) % 3) != 0):
		bit_str += "00000000"	
		text += "0"
	
	#Split bit_str into 6bit long brackets
	brackets = re.findall('(\d{6})', bit_str)

	#Encode the brackets
	for bracket in brackets:
		if(bracket=="000000"):
			base64_str+="="
		else:
			base64_str+=alphabet[int(bracket,2)]
	return base64_str


    
def check_funcion(fun):
  participants_list, to_remove_list, to_add_list = ['A', 'B', 'C'], ['B'], ['A']
  results = []
  new_list = participants_list
  new_list2 = participants_list
  if len(to_remove_list)>0:
    new_list = [p for p in participants_list if p not in to_remove_list]
    new_list2 = [p for p in participants_list if p not in to_remove_list]
  if len(to_add_list)>0:
    for p in to_add_list:
      if p not in new_list:
        new_list.append(p)
        new_list2.append(p)
      else:
        new_list2 = list(map(lambda b: b.replace(p,p+"_1"), new_list))
        new_list2.append(p+'_2')
  new_list.sort()
  new_list2.sort()
  outp_func=fun(participants_list, to_remove_list, to_add_list)
  if type(outp_func)==list:
      results.append(new_list==outp_func or new_list2==outp_func)
  if len(results)>0 and all(results):
    print("Congrats, your code works! Now, submit it and see you tomorrow!")
  else:
    print("Try again, something is still not OK!")


def check_funcion22(fun):
  import re
  test_list = ['tr123rammer', '.@magda', 'm-agd-a', '_magda22_', 'magdaMAGDAmagda']
  results = []
  for name in test_list:
    outp_true=''
    if all(['_' not in name, '-' not in name, len(name)<=20,
    not name.startswith('.'), not name.endswith('.'), 
    (name.lower()==name or name.upper()==name), 
    len(re.findall('[@!#$%^&*?~:]', name))==0, not bool(re.search('\d', name))]):
      outp_true='Good'
    else:
      outp_true='Bad'
    outp_func=fun(name)
    if type(outp_func)==str:
      results.append(outp_func==outp_true)
  if len(results)>0 and all(results):
    print("Congrats, your code works! Now, submit it and see you tomorrow!")
  else:
    print("Try again, something is still not OK!")

#Decode a base64 chiffre
def base64Decode(chiffre):
	alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	bit_str=""
	text_str=""
	
	#Loop through every char
	for char in chiffre:
		#Ignore characters, which are not in the alphabet. Concatenate the binary representation of alphabet index of char 
		if char in alphabet:
			bin_char = bin(alphabet.index(char)).lstrip("0b")
			bin_char = (6-len(bin_char))*"0" + bin_char
			bit_str += bin_char
	
	#Make 8bit - 2byte brackets
	brackets = re.findall('(\d{8})', bit_str)

	#Decode char binary -> asciii
        for bracket in brackets:
                        text_str+=chr(int(bracket,2))

        return text_str