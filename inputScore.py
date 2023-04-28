init_turn = 0
program_active = True
student_list = {}
all_subject = ['Java', 'Python', 'SQL', 'C#']


def subject_highest():

    if len(student_list) != 0:
        print("以下為目前所有的科目")
        for subject in all_subject:
            print(subject)
        subject = input("請輸入欲查詢的科目名稱(注意大小寫):\n")
        if student_list != {}:
            score_list = []

            for _, item in student_list.items():
                score_list.append((item[subject]))

            max_score = max(score_list)
            count = score_list.count(max_score)

            print(f'這次有{count}人在{subject}中得到最高分{max_score}分，學生姓名為：')
            for name, value in student_list.items():
                if value[subject] == max_score:
                    print(name)
    else:
        print("目前沒有學生資料，請先新增學生資訊")


def average_highest():

    if len(student_list) != 0:
        average_dict = {}
        score_list = []

        for name, value in student_list.items():
            dict_name = name
            dict_num = (sum(list(value.values()))/4)
            average_dict.update({dict_name: dict_num})
            score_list.append(dict_num)

        max_score = max(score_list)
        count = score_list.count(max_score)

        print(f'這次有{count}人最高分平均{max_score}分，學生姓名為：')
        for name, value in average_dict.items():
            if value == max_score:
                print(name)
    else:
        print("目前沒有任何學生的資料，轉跳到主選單")


def sorted_score():

    if len(student_list) != 0:
        average_student_list = student_list.copy()

        for key, value in average_student_list.items():
            dict_num = (sum(list(value.values()))/4)
            average_student_list[key] = dict_num

        result = sorted(average_student_list.items(),
                        key=lambda x: x[1], reverse=True)

        print("由高至低排序的結果如下：")
        for key, value in result:
            print(f'{key}平均得到{value}分')
    else:
        print("目前沒有任何學生的資料，轉跳到主選單")


def add_student_input():
    while (True):
        name = input(f'請輸入學生的姓名：\n')
        if name.strip() == "" :
            print("姓名欄位不能為空，請重新輸入")
            continue
        if name in student_list:
            print("學生姓名已存在，請重新輸入姓名")
            continue
        else:

            student_list.update({name: {}})

            for subject in all_subject:

                while (True):

                    score = input(f"請輸入{name}學生的{subject}成績:\n")

                    

                    if score.isnumeric():

                        if int(score) < 0 or int(score) > 100:
                            print("請輸入0-100之間的合理的正整數")
                            continue

                        student_list[name].update({subject: int(score)})
                        break
            break


def delete_student():
    while (True):
        name = input("請輸入欲刪除學生之姓名")
        if name in student_list:
            while (True):
                confirm = input("確定要刪除嗎？(Y/N)\n")
                if confirm.lower() == "y":
                    del student_list[name]
                    print(f"已刪除{name}的資料")
                    break

                if confirm.lower() == "n":
                    print("取消刪除流程")
                    break
            repeat = input("請問要再次執行刪除流程嗎？(Y/N)\n")
            if repeat.lower() == 'y':
                continue
            else:
                break

        else:
            exit = input("學生資料不存在，欲返回選單？(Y/N)\n")
            if exit.lower() == "y":
                break
            elif exit.lower() == "n":
                continue


def search_student():

    if len(student_list) != 0:
        for key, _ in student_list.items():
            print(f"學生姓名：{key}")

        while (True):
            name = input("請問要查詢哪一位學生的資料呢？\n")

            if name in student_list:
                print(f"{name}學生的成績資料如下：")
                for key, value in student_list[name].items():
                    print(f'{key}：{value}分')
            else:
                print("該學生不存在")
            stop = input("是否還要繼續查詢呢？(Y/N)\n")
            if (stop.lower() == "y"):
                continue
            else:
                break
    else:
        print("目前沒有並沒有任何學生的相關資料")


while (init_turn < 6):

    name = input(f'請輸入學生{init_turn+1}號的姓名：\n')
    if name.strip() == "":
        print("姓名欄位不能為空，請輸入姓名")
        continue
    if name in student_list:
        print("學生姓名已存在，請重新輸入姓名")
        continue
    else:

        student_list.update({name: {}})

        for subject in all_subject:

            while (True):

                score = input(f"請輸入{name}學生的{subject}成績:\n")

                if score.isnumeric():
                    if int(score) < 0 or int(score) > 100:
                            print("請輸入0-100之間的合理的正整數")
                            continue

                    student_list[name].update({subject: int(score)})
                    break

        init_turn += 1


while (program_active):
    print("\n")
    print("請選擇要執行的功能(請輸入對應的數字)：\n")
    print("(1)找出指定科目的最高分")
    print("(2)找出得最高平均分的學生資料")
    print("(3)從高至低列出學生姓名與平均分數")
    print("(4)新增學生資料")
    print("(5)刪除學生資料")
    print("(6)查詢現有學生資料")
    print("(7)結束本程式")
    select = input("請輸入欲使用的功能")
    if select == "1":
        subject_highest()
    if select == "2":
        average_highest()
    if select == "3":
        sorted_score()
    if select == "4":
        add_student_input()
    if select == "5":
        delete_student()
    if select == "6":
        search_student()
    if select == "7":
        print("感謝使用，我們下次見")
        break
