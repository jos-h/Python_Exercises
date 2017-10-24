audio = {}
audio_dic = {}
header = ""
fread = open("D:\\Ubuntu_BackUp\\untitled\\audio.conf", "r")
for line in fread:
    line = line.strip()
    if not line:
        continue
    if line[0] == "[":
        print(line[1:-1])
        if header:
            audio[header] = audio_dic
            audio_dic = {}
            header = line[1:-1]
        else:
            header = line[1:-1]
        continue
    elif line[0] == "#":
        continue

    key, value = line.split("=")
    audio_dic[key] = value.split()[0]
audio[header] = audio_dic
fread.close()
print(audio)