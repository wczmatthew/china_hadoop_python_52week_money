"""
    作者：wcz
    功能：52周存钱挑战
    版本：v1.0
    日期：24/06/2018
"""


def main():
    """
        主函数
    """
    money_per_week = 10     # 每周存入的金额
    i = 1                   # 记录周数
    increase_money = 40     # 递增的金额
    total_week = 52         # 总周数
    saving = 0              # 账户累计

    while i <= total_week:
        saving += money_per_week

        print('第{}周，存入{}元，账户累计{}元'.format(i,money_per_week,saving))
        money_per_week += increase_money

        i += 1

    print('总金额：', saving)


if __name__ == '__main__':
    main()