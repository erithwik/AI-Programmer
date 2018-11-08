def interpret(fileName):	
	file = open(fileName, "r")
	solve(file.read())
	file.close

def solve(code):
	def addOne():
		nonlocal data
		data[pointer] += 1
	def subOne():
		nonlocal data
		data[pointer] -= 1
	def moveRight():
		nonlocal pointer, data
		pointer += 1
		try:
			val = data[pointer]
		except:
			data.append(0)
	def moveLeft():
		nonlocal pointer
		pointer -= 1
		try:
			val = data[pointer]
		except:
			pointer += 1
	def printChar():
		print(chr(data[pointer]), end = "")
	def storeVal():
		nonlocal data
		val = input("What is the val?")
		data[pointer] = int(val)
	def startLoop():
		nonlocal data, pointer, i
		if data[pointer] == 0:
			braces = 1
			while braces > 0:
				i += 1
				if code[i] =='[':
					braces += 1
				elif code[i] == ']':
					braces -= 1
	def endLoop():
		nonlocal pointer, data, i
		braces = 1
		while braces > 0:
			i -= 1
			if code[i] == '[':
				braces -= 1
			elif code[i] == ']':
				braces += 1
		i -= 1

	i = 0
	data, pointer = [0], 0
	keyValDict = {">":moveRight, "<":moveLeft, "+":addOne, "-":subOne, ".":printChar, ",":storeVal, "[":startLoop, "]":endLoop}
	while i < len(code):
		keyValDict[code[i]]()
		i+=1

if __name__ == "__main__":
	interpret("bf.txt")