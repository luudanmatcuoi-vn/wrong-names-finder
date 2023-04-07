import pyperclip, re

data = pyperclip.paste()

name = """
Fujibayashi, Ryou
Fujibayashi, Kyou
Furukawa, Nagisa
Ibuki, Fuuko
Ichinose, Kotomi
Okazaki, Tomoya
Sakagami, Tomoyo
Sunohara, Youhei
Furukawa, Akio
Furukawa, Sanae
Harada
Ibuki, Kouko
Ichinose, Kotaro
Ichinose, Mizue
Isogai
Kanako
Koumura, Toshio
Mitsui
Miyazawa, Yukine
Nishina, Rie
Okazaki, Naoyuki
Oogami
Sagara, Misae
Sakagami, Takafumi
Sugisaka
Sunohara, Mei
Yoshino, Yusuke
"""


# lọc bước đầu
name = name.lower()
name = name.replace(",","")
name = name.replace("\n"," ")
name = name.replace("-"," ")
name = name.split(" ")
name = [t for t in name if t !="" ]

# lọc bước đầu
dataraw = data
data = data.lower()

name = list(set(name))

for n in name: 
	lenn = len(n)
	pattern = "[^{name}][{name}]{{{a},{b}}}[^{name}]".format( name = n, a= str(lenn*2//3),  b = str(lenn*4//3) )
	res = re.findall(pattern, data)
	# Remove right word from result
	res = [t for t in res if n not in t ]

	result = [t[1:-1] for t in res]
	result = list(set(result))
	print("--------------------------")
	print(n)
	for t in result:
		temp = [g for g in res if t in g]
		print(t+"\t"+str(temp))

input()