#!/usr/bin/python3


def find_avg_petrol():
    #file_handle = open("/home/sudouser/Desktop/temp.txt")
    avg = list()
    with open("/home/sudouser/Desktop/temp") as file_handle:
        for line in file_handle:
            last_3_digits = [int(i) for i in line.split()[-3:]]
            avg.append(sum(last_3_digits)//len(last_3_digits))
    with open("/home/sudouser/Desktop/temp1.txt","w+") as file_write:
        for l in avg:
            file_write.write(str(l)+"\n")


def main():
    find_avg_petrol()


if __name__ == '__main__':
    main()



