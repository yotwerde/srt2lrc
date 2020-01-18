filename = input('Give full path to .srt file (omit the .srt file extension): ')
srt = open(filename + '.srt', 'r')
lrc = open(filename + '.lrc', 'w')

lrc_lines = []
srt_lines = srt.readlines()
index = 1
while index < len(srt_lines):
    temp_time = srt_lines[index][3:12]
    temp_time = temp_time.replace(',', '.', 1)
    index += 1
    temp_lyric = srt_lines[index]
    temp_line = '[' + temp_time  + ']' + temp_lyric
    lrc_lines.append(temp_line)
    index += 3

for line in lrc_lines:
    lrc.write(line)

srt.close()
lrc.close()

input('The newly created .lrc file is located in the same directory as your .srt file\n\nHit Enter to quit...\n')
