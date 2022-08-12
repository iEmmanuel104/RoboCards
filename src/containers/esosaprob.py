def texttags(text, words):
	replaced = []
	target = []
	for i in words.split(", "):
		target.extend(i.split()):
	for j in range(len(text.split())):
		if text[i] in target:
			print(i)
			text[i]=tags 
			replaced.extend(i)
	text = " ".join(text)


print(text)
print(replaced)
print(len(replaced))
print(len(" ".join(replaced).replace(" ","").replace(",","")))