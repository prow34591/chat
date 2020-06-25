def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	梓翔_word_count = 0
	梓翔_sticker_coint = 0
	梓翔_image_coun = 0
	緯_word_count = 0
	緯_sticker_coint = 0
	緯_image_coun = 0

	for line in lines:
		s = line.split(' ')
		tinm = s[0]
		name = s[1]
		if name == '梓翔(阿斌)':
			if s[2] == '貼圖':
				梓翔_sticker_coint += 1
			elif s[2] == '團片':
				梓翔_image_count = 0
			else:		
				for m in s[2:]:
					梓翔_word_count += len(m)
		elif name == '緯':
			if s[2] == '貼圖':
				緯_sticker_coint += 1
			elif s[2] == '團片':
				緯_image_count = 0
			else:
				for m in s[2:]:
					緯_word_count += len(m)

	print('梓翔說了', 梓翔_word_count, '個字')
	print('梓翔傳了', 梓翔_sticker_coint, '個貼圖')
	print('梓翔傳了', 梓翔_image_coun, '張圖片')

	print('緯說了', 梓翔_word_count, '個字')
	print('緯傳了', 梓翔_sticker_coint, '個貼圖')
	print('緯傳了', 梓翔_image_coun, '張圖片')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('5.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()