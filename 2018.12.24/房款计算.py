#!usr/bin/python3
#-*- coding:utf-8 -*-

# 思路
# 接受
    # price 单价
    # area 面积
    # ratio 按揭成数
    # time 按揭年数
    # yir 年利率
# 转换
    # ratio 按揭年数 7*0.1
    # time 按揭年数 20*12
    # yir 年利率 yir/100
    # mir 月利率 yir/12
# 计算
    # total_price 房款总额  price * area
    # down_payment 首期付款 down_payment * ( 1 - ratio )
    # loan 货款总额 total_price * ratio

    # ave_repay 月均还款
    # interest 总利息
    # total_repay 还款总额 loan + interest


if __name__ == "__main__":
    print("32456789")

