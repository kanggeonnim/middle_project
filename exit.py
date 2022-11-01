
# check if user wants another calculation
# break the while loop if answer is no/n

yes_list = ['yes', 'y']
no_list = ['no', 'n']

def isExit():
    next_calculation = (input("Let's do next calculation? (yes/no): ")).lower()
    while True:
        
        if next_calculation in yes_list:    # 계산을 더 하고 싶을 때
            return "yes"
        elif next_calculation in no_list:   # 더이상 계산을 하지 않을 때
            exit_answer = (input("Are you sure? (yes/no): ")).lower()   # 한번 더 물어봄

            while True: # yes 또는 no로만 대답을 받을 때 까지 질문함.

                if exit_answer in yes_list or exit_answer in no_list:
                    break
                else:   # 선택지에 없는 입력을 받았을 경우
                    exit_answer = (input("Quit the calculator? Please answer only (yes/no): ")).lower()

            if exit_answer in no_list: # 사실 속마음은 프로그램 종료를 원하지 않을 경우
                return "yes"
            elif exit_answer in yes_list: # 정말로 프로그램 종료를 원하는 경우
                return "no"

        else:   # 선택지에 없는 입력을 받았을 경우
            next_calculation = (input("Calculation again? Please answer only (yes/no): ")).lower()
