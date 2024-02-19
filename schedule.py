import json
from openai import AzureOpenAI

# 기본적인 날짜와 시간을 담은 dictionary
dictionary = {}
dictionary['month'] =['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
dictionary['date'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
dictionary['time'] = ['9시에서 12시','1시에서 3시','3시에서 6시']

# schedule.json 읽어오기
with open('schedule.json', 'r') as file:
    schedule = json.load(file)

# schedule.json에 새로운 일정 추가하기
def none_schedule(name:list = ['kim','lee','park'], month:str = 'mar'):
    none_list = []
    num = 0
    for i in dictionary['date']:
        for j in dictionary['time']:
            # name에 있는 사람들이 모두 none인 경우 none_list에 추가
            for k in name:
                if schedule[k][month][i][j] == 'none':
                    num += 1
            if num == len(name):
                none_list.append([i,j])
            num = 0
    return none_list

def schedule_add(none_list:list, info_path:str = './company_project_info.txt'):
    # [['7', '1시에서 3시'], ['17', '1시에서 3시']]
    answer = ''
    line = '8. 면접 가능 일자 \n\n'
    for i,j in none_list:
        answer += f'{i}일 {j}, '
    
    with open(info_path, 'a') as f:
        f.write(line)
        f.write(answer)


if __name__ == '__main__':
    ns = none_schedule(['kim','lee','park'], 'mar')
    schedule_add(ns)
    


