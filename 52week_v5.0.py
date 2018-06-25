"""
    作者：wcz
    功能：52周存钱挑战
    版本：v5.0
    日期：24/06/2018
    功能：根据第几周，输出存钱数
"""
import math
import datetime


def save_money_in_n_weeks(money_per_week, increase_money,total_week):
    """
        计算n周内的存款金额
    """
    money_list = []         # 记录每周存款数
    saved_money_list = []   # 每周账户累计
    saving = 0
    for i in range(total_week):
        # saving += money_per_week
        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        print('第{}周，存入{}元，账户累计{}元'.format(i+1, money_per_week, saving))
        money_per_week += increase_money

    return saved_money_list


def main():
    """
        主函数
    """
    money_per_week = float(input("请输入每周的存入金额"))
    increase_money = int(input("请输入每周的递增金额"))
    total_week = int(input("请输入总共的周数"))

    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    week_num = input_date.isocalendar()[1]

    # week_num = int(input('请输入第几周：'))

    print('第{}周的存款是{}元'.format(week_num, saved_money_list[week_num-1]))


if __name__ == '__main__':
    main()