# 用if语句实现百分制转等级制
# 60分以下不合格，60-74为合格，75-89为良好，90分以上为优秀

def grade_conversation(score):
    if score < 60:
        return '不合格'
    elif score < 75:
        return '合格'
    elif score < 90:
        return '良好'
    else:
        return '优秀'

score = float(input())
print(grade_conversation(score))