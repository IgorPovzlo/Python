f = open('src_14.txt',  encoding='utf-8')
number_of_ratings = 0
sum_ratings = 0
f_gpa = open('src.txt', 'wt', encoding='utf-8')
while True:
    f_str = f.readline()
    if f_str != '':
        number_of_ratings += 1
        lst = f_str.split()
        x = 0
        for i in range(len(lst)):
            if i > 1:
                x += int(lst[i])
        average_ratings = round(x / (len(lst) - 2), 2)
        sum_ratings += average_ratings
        lst = lst[1] + " " + lst[0][:1] + "."
        name_average_ratings = '{:<15}    {:>} '.format(lst, average_ratings)
        f_gpa.write(name_average_ratings)
        f_gpa.write('\n')
        if average_ratings < 5:
            print(name_average_ratings)
    else:
        print('Cредний бал по классу -', round((sum_ratings / number_of_ratings), 2))
        break

f.close()
f_gpa.close()

