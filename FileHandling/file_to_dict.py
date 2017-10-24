#
#
# def file_to_dict():
#     file_handle = open("D:\\Ubuntu_BackUp\\untitled\\audio.conf")
#     dict_section = {}
#     cnt = 0
#     for line in file_handle:
#         cnt = 0
#         if not line.startswith('#') and line != '\n':
#             if line.startswith('['):
#                 section = line[1:line.rindex(']')]
#                 print(section)
#                 cnt = 1
#             else:
#                 var, sect = parse_inner_dict(file_handle)
#                 print("After function call")
#                 print(var)
#                 dict_section[section] = var
#                 section = sect[1:sect.rindex(']')]
#
#     file_handle.close()
#
#     return ''
#
#
# def parse_inner_dict(file_handle):
#     inner_dict = dict()
#     line = " "
#     while not '[' in line:
#         if '=' in line and not line.startswith('#'):
#             split_data = line.split('=')
#             if '#' in split_data[1]:
#                 split_split_data = split_data[1].split('#')
#                 inner_dict[split_data[0]] = split_split_data[0]
#             else:
#                 inner_dict[split_data[0]] = split_data[1]
#         line = file_handle.readline()
#     return inner_dict, line
#
# def main():
#     file_to_dict()
#
# if __name__ == '__main__':
#     main()


def file_to_dict():

    header = ''
    audio = {}
    audio_dict = {}

    file_handle = open("/home/sudouser/PycharmProjects/untitled/untitled/audio.conf")

    for line in file_handle:
        if not line:
            continue
        if line.startswith('['):
            print(line[1:-2])
            if header:
                audio[header] = audio_dict
                audio_dict = {}
                header = line [1:-2]
            else:
                header = line[1:-2]
        if line.startswith('#'):
            continue

        if '=' in line:
            key, value = line.split('=')
            audio_dict[key] = value.split()[0]

    audio[header] = audio_dict
    file_handle.close()
    print("Dictionary is {}".format(audio))


def main():
    file_to_dict()


if __name__ == '__main__':
    main()