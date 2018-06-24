"""
    作者：wcz
    功能：52周存钱挑战
    版本：v4.0
    日期：24/06/2018
    功能：设置每周存入的金额
"""
import math



def save_money_in_n_weeks(money_per_week, increase_money,total_week):
    """
        计算n周内的存款金额
    """
    money_list = []
    saving = 0
    for i in range(total_week):
        # saving += money_per_week
        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        money_per_week += increase_money

    return saving


def main():
    """
        主函数
    """
    money_per_week = float(input("请输入每周的存入金额"))
    increase_money = int(input("请输入每周的递增金额"))
    total_week = int(input("请输入总共的周数"))

    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)

    print('总金额：', saving)


if __name__ == '__main__':
    main()