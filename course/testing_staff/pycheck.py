import os
import time


def pytest(code, inp, exp_out, TL):
    result = "OK"
    f = open("course/testing_staff/data.py", 'w')
    f.write(code)
    f.close()
    counter = 0
    Rtime = 0
    for i in inp:
        counter += 1
        f = open('course/testing_staff/input.txt', 'w')
        f.write(i)
        f.close()
        try:
            Stime = time.time()
            os.system(
                "python3 course/testing_staff/data.py <course/testing_staff/input.txt >course/testing_staff/output.txt")
            Rtime = time.time() - Stime
            f = open('course/testing_staff/output.txt', 'r')
            out = str(f.read())
            print(out)
            f.close()
            exp_out[counter - 1] += "\n"
            if out != exp_out[counter - 1]:
                result = "WA"
            if TL < Rtime:
                result = "TL"
            print(exp_out[counter - 1])
        except:
            result = "RE"
        if result != "OK":
            break
    print(result, counter)
    return result + " " + str(counter) + " " + str(Rtime)


def cpptest(code, inp, exp_out, TL):
    f = open("course/testing_staff/main.cpp", 'w')
    f.write(code)
    f.close()
    os.system('g++ course/testing_staff/main.cpp -o course/testing_staff/main.out -Wall -Werror')
    result = "OK"
    counter = 0
    Rtime = 0
    for i in inp:
        counter += 1
        f = open('course/testing_staff/input.txt', 'w')
        f.write(i)
        f.close()
        try:
            Stime = time.time()
            os.system(
                "./course/testing_staff/main.out <course/testing_staff/input.txt >course/testing_staff/output.txt")
            Rtime = time.time() - Stime
            f = open('course/testing_staff/output.txt', 'r')
            out = str(f.read())
            print(out)
            f.close()
            if out != exp_out[counter - 1]:
                result = "WA"
            if TL < Rtime:
                result = "TL"
            print(exp_out[counter - 1])
        except:
            result = "RE"
        if result != "OK":
            break
    print(result, counter)
    return result + " " + str(counter) + " " + str(Rtime)
