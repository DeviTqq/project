#Реализовать функцию, которая заменяет все окончания слов в предложении
#по соответствующему критерию, а так же в последнем слове
def replace_text(text: str, pattern: str, replacement: str) -> str:
	obj = text.split(' ')
	n = len(pattern)
	for i in range(len(obj)):
		if obj[i][-n:] == pattern:
			obj[i] = obj[i].replace(pattern, replacement)
	if pattern in obj[-1]:
		obj[-1] = obj[-1].replace(pattern,replacement)

	return ' '.join(obj)

replacement = '_'
text = 'awe bwet wea owew'
pattern = 'we'
print(replace_text(text, pattern, replacement))
