'''import subprocess

inputFile = "inter_output.csv"
trainingset = "trainingset.csv"

process = subprocess.Popen(['sampling.sh', inp
utFile, trainingset], stdout=subprocess.PIPE)
process.wait()

'''

import sys, re, string, random
import csv


f = csv.reader(open("final_trainingset.csv", "rb"))
f1 = csv.writer(open("sample_Csharp.csv", "wb"))
f2 = csv.writer(open("sample_Java.csv", "wb"))
f3 = csv.writer(open("sample_Php.csv", "wb"))
f4 = csv.writer(open("sample_Javascript.csv", "wb"))
f5 = csv.writer(open("sample_Android.csv", "wb"))
f6 = csv.writer(open("sample_Jquery.csv", "wb"))
f7 = csv.writer(open("sample_Iphone.csv", "wb"))
f8 = csv.writer(open("sample_cplusplus.csv", "wb"))
f9 = csv.writer(open("sample_aspdotnet.csv", "wb"))
f10 = csv.writer(open("sample_Python.csv", "wb"))
f11 = csv.writer(open("sample_dotnet.csv", "wb"))
f12 = csv.writer(open("sample_mysql.csv", "wb"))
f13 = csv.writer(open("sample_html.csv", "wb"))
f14 = csv.writer(open("sample_objecivec.csv", "wb"))
f15 = csv.writer(open("sample_sql.csv", "wb"))
f16 = csv.writer(open("sample_css.csv", "wb"))
f17 = csv.writer(open("sample_rubyrail.csv", "wb"))
f18 = csv.writer(open("sample_ios.csv", "wb"))
f19 = csv.writer(open("sample_c.csv", "wb"))
f20 = csv.writer(open("sample_ruby.csv", "wb"))
question_key1 = set()
question_key2 = set()
question_key3 = set()
question_key4 = set()
question_key5 = set()
question_key6 = set()
question_key7 = set()
question_key8 = set()
question_key9 = set()
question_key10 = set()
question_key11 = set()
question_key12 = set()
question_key13 = set()
question_key14 = set()
question_key15 = set()
question_key16 = set()
question_key17 = set()
question_key18 = set()
question_key19 = set()
question_key20 = set()
counter = [0] * 20

for l in f:


    truth_temp = 1
    if l[3] == 'c#':
        question_key1.add(l[0])
        f1.writerow(l + [truth_temp])
        counter[0] += 1

    elif l[3] == 'java':
        question_key2.add(l[0])
        f2.writerow(l + [truth_temp])
        counter[1] += 1

    elif l[3] == 'php':
        question_key3.add(l[0])
        f3.writerow(l + [truth_temp])
        counter[2] += 1

    elif l[3] == 'javascript':
        question_key4.add(l[0])
        f4.writerow(l + [truth_temp])
        counter[3] += 1

    elif l[3] == 'wpf':
        question_key5.add(l[0])
        f5.writerow(l + [truth_temp])
        counter[4] += 1

    elif l[3] == 'jquery':
        question_key6.add(l[0])
        f6.writerow(l + [truth_temp])
        counter[5] += 1

    elif l[3] == 'iphone':
        question_key7.add(l[0])
        f7.writerow(l + [truth_temp])
        counter[6] += 1

    elif l[3] == 'c++':
        question_key8.add(l[0])
        f8.writerow(l + [truth_temp])
        counter[7] += 1

    elif l[3] == 'asp.net':
        question_key9.add(l[0])
        f9.writerow(l + [truth_temp])
        counter[8] += 1

    elif l[3] == 'python':
        question_key10.add(l[0])
        f10.writerow(l + [truth_temp])
        counter[9] += 1

    elif l[3] == '.net':
        question_key11.add(l[0])
        f11.writerow(l + [truth_temp])
        counter[10] += 1

    elif l[3] == 'mysql':
        question_key12.add(l[0])
        f12.writerow(l + [truth_temp])
        counter[11] += 1

    elif l[3] == 'html':
        question_key13.add(l[0])
        f13.writerow(l + [truth_temp])
        counter[12] += 1

    elif l[3] == 'android':
        question_key14.add(l[0])
        f14.writerow(l + [truth_temp])
        counter[13] += 1

    elif l[3] == 'sql':
        question_key15.add(l[0])
        f15.writerow(l + [truth_temp])
        counter[14] += 1

    elif l[3] == 'css':
        question_key16.add(l[0])
        f16.writerow(l + [truth_temp])
        counter[15] += 1

    elif l[3] == 'ruby-on-rails':
        question_key17.add(l[0])
        f17.writerow(l + [truth_temp])
        counter[16] += 1

    elif l[3] == 'objective-c':
        question_key18.add(l[0])
        f18.writerow(l + [truth_temp])
        counter[17] += 1

    elif l[3] == 'c':
        question_key19.add(l[0])
        f19.writerow(l + [truth_temp])
        counter[18] += 1

    elif l[3] == 'asp.net-mvc':
        question_key20.add(l[0])
        f20.writerow(l + [truth_temp])
        counter[19] += 1

print "half >>>>>>>>>>"
fn = csv.reader(open("final_trainingset.csv", "rb"))
firstline = 0
truth_temp = 0
cnt = 0
for l in fn:
    k = random.randint(1, 21)
    cnt += 1
    random_flag = 1
    while(random_flag == 1):
        if ((k == 1 or k == 21) and l[3] != 'c#' and counter[0] > 0):
            if (l[0] not in question_key1):
                f1.writerow(l + [truth_temp])
                random_flag = 0
                counter[0] -= 1
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 2 and l[3] != 'java' and counter[1] != 0):
            if (l[0] not in question_key2):
                f2.writerow(l + [truth_temp])
                random_flag = 0
                counter[1] -= 1
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 3 and l[3] != 'php'and counter[2] != 0):
            if (l[0] not in question_key3):
                f3.writerow(l + [truth_temp])
                random_flag = 0
                counter[2] -= 1
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 4 and l[3] != 'javascript' and counter[3] != 0):
            if (l[0] not in question_key4):
                f4.writerow(l + [truth_temp])
                random_flag = 0
                counter[3] -= 1
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 5 and l[3] != 'wpf' and counter[4] != 0):
            if (l[0] not in question_key5):
                f5.writerow(l + [truth_temp])
                counter[4] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 6 and l[3] != 'jquery' and counter[5] != 0):
            if (l[0] not in question_key6):
                f6.writerow(l + [truth_temp])
                counter[5] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 7 and l[3] != 'iphone' and counter[6] != 0):
            if (l[0] not in question_key7):
                f7.writerow(l + [truth_temp])
                counter[6] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 8 and l[3] != 'c++' and counter[7] != 0):
            if (l[0] not in question_key8):
                f8.writerow(l + [truth_temp])
                counter[7] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 9 and l[3] != 'asp.net' and counter[8] != 0):
            if (l[0] not in question_key9):
                f9.writerow(l + [truth_temp])
                counter[8] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 10 and l[3] != 'python' and counter[9] != 0):
            if (l[0] not in question_key10):
                f10.writerow(l + [truth_temp])
                counter[9] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 11 and l[3] != '.net' and counter[10] != 0):
            if (l[0] not in question_key11):
                f11.writerow(l + [truth_temp])
                counter[10] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 12 and l[3] != 'mysql' and counter[11] != 0):
            if (l[0] not in question_key12):
                f12.writerow(l + [truth_temp])
                counter[11] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 13 and l[3] != 'html' and counter[12] != 0):
            if (l[0] not in question_key13):
                f13.writerow(l + [truth_temp])
                counter[12] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 14 and l[3] != 'android' and counter[13] != 0):
            if (l[0] not in question_key14):
                f14.writerow(l + [truth_temp])
                counter[13] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 15 and l[3] != 'sql' and counter[14] != 0):
            if (l[0] not in question_key15):
                f15.writerow(l + [truth_temp])
                counter[14] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 16 and l[3] != 'css' and counter[15] != 0):
            if (l[0] not in question_key16):
                f16.writerow(l + [truth_temp])
                counter[15] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 17 and l[3] != 'ruby-on-rails' and counter[16] != 0):
            if (l[0] not in question_key17):
                f17.writerow(l + [truth_temp])
                counter[16] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 18 and l[3] != 'objective-c' and counter[17] != 0):
            if (l[0] not in question_key18):
                f18.writerow(l + [truth_temp])
                counter[17] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 19 and l[3] != 'c' and counter[18] != 0):
            if (l[0] not in question_key19):
                f19.writerow(l + [truth_temp])
                counter[18] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1

        elif (k == 20 and l[3] != 'asp.net-mvc' and counter[19] != 0):
            if (l[0] not in question_key20):
                f20.writerow(l + [truth_temp])
                counter[19] -= 1
                random_flag = 0
                cnt = 0
            else:
                k = random.randint(1, 21)
                cnt += 1
        elif (cnt > 100):
            random_flag = 0
            cnt = 0

        else:
            k = random.randint(1, 21)
            cnt += 1
    print counter
print "Done >>>>>>>>>"
print counter