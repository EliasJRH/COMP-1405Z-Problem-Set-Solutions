print('Course Grade Analysis')
file = open(input('Enter file name: '))
step = 1
temp_first, temp_last, temp_num, temp_grade = "","","", 0
highest_first, highest_last, highest_grade, highest_num, lowest_first, lowest_last, lowest_grade, lowest_num = "","", 0, "" ,"","", 0, ""
passed, didnt_pass, overall_avg, students = 0,0,0,0 
with file as file:
    for line in file:
        if step == 1:
            temp_first = line.strip()
        elif step == 2:
            temp_last = line.strip()
        elif step == 3:
            temp_num = line.strip()
        elif step == 4:
            temp_grade += int(line) * 0.25
        elif step == 5:
            temp_grade += int(line) * 0.25
        elif step == 6:
            step = 0
            temp_grade += int(line) * 0.5
            if int(line) >= 50 and temp_grade >= 50:
                passed += 1
            else:
                didnt_pass += 1
            overall_avg += temp_grade
            students += 1
            if students == 1:
                highest_first = temp_first
                highest_last = temp_last
                highest_num = temp_num
                highest_grade = temp_grade
                lowest_first = temp_first
                lowest_last = temp_last
                lowest_num = temp_num
                lowest_grade = temp_grade
            else:
                if temp_grade > highest_grade:
                    highest_first = temp_first
                    highest_last = temp_last
                    highest_num = temp_num
                    highest_grade = temp_grade
                elif temp_grade < lowest_grade:
                    lowest_first = temp_first
                    lowest_last = temp_last
                    lowest_num = temp_num
                    lowest_grade = temp_grade
            temp_grade = 0
        step += 1
print ('Number of Passes: ' + str(passed))
print ('Number of Fails: ' + str(didnt_pass))
print ('Average Final Grade: ' + str(overall_avg/students))
print ('Highest Grade: ' + highest_first + ' ' + highest_last + ' Student Number: ' + highest_num + ' - ' + str(highest_grade))
print ('Lowest Grade: ' + lowest_first + ' ' + lowest_last + ' Student Number: ' + lowest_num + ' - ' + str(lowest_grade))