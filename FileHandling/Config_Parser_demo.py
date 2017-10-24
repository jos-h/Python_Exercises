from configparser import ConfigParser


def main():
    file_to_dict_config()


def file_to_dict_config():
    parser = ConfigParser()
    parser.read("D:\\Ubuntu_BackUp\\untitled\\audio.conf")
    #print(parser.sections())

    for section_name in parser.sections():
        print('Section \t{}'.format(section_name))
        print('Options\t{}'.format(parser.options(section_name)))
        for name,value in parser.items(section_name):
            print("%s = %s" % (name,value))

    print(parser.options("General"))


if __name__ == '__main__':
    main()