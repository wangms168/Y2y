import pandas as pd


def km6421070101(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人佣金提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070102(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人业务拓展费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070103(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人其他提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070104(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人服务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070105(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人期权业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070106(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人IB业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070107(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人管理津贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070108(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人投顾业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070109(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人其他提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070110(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人开户奖'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070111(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人两融净息差提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070201(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人公募基金保有量提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070202(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人公募基金销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070203(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人基金分仓销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    out_ws.append(fl_list)


def km6421070301(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人公募基金销售手续费返还'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070302(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人公司理财产品销售提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[17] = 'gl01001' + ':销售产品类别'
    out_ws.append(fl_list)


def km6421070303(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人代理销售保险产品'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km6421070304(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '经纪人非公募产品销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km22411901(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '发放总部下拨奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km22211401(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '应付经纪人增值税'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22211402(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '应付经纪人城建税'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22211403(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '应付经纪人教育费附加'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22211407(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '应付经纪人地方教育费附加'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km222105(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '扣个人所得税'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = '06:人员类别'
    out_ws.append(fl_list)


def km224107(k, fl_list, amt, jbb, in_df, out_ws):
    s = in_df[k]  # 获取'224107'这一列pd.Serie这个对象
    for i, v in s.items():  # items是pd.Serie的每个项目，i是键(df的index)、v是值('224107'这列上的数据)
        if v and (not (pd.isnull(v))) and i != 'A1' and i != 'A2' and i != 'B' and i != 'D' and i != '合计' and i != '小计':
            i1 = i.split(':')[0]
            i2 = i.split(':')[1]
            # print('i1=', i1, 'i2=', i2, '  ', 'v=', v)
            fl_list[5] = '扣风险金'
            fl_list[6] = k
            fl_list[11] = str(round(v, 2))
            fl_list[12] = str(round(v, 2))
            fl_list[15] = i1 + ':人员档案'
            fl_list[16] = i2 + ':人员类别'
            out_ws.append(fl_list)


def km6601070201(k, fl_list, amt, jbb, in_df, out_ws):
    fl_list[5] = '扣房租'
    fl_list[6] = k
    fl_list[8] = str(-amt)
    fl_list[9] = str(-amt)
    fl_list[15] = jbb + ':部门'
    out_ws.append(fl_list)


def km1001(SInfo_df, fl_list, amt, jbb, in_df, out_ws):
    YYB_bm = fl_list[10]

    if SInfo_df['工资结算户'][YYB_bm] == "总部统一结算":
        kmbm = "114305"

        fl_list[5] = '发放经纪人委托费'
        fl_list[6] = kmbm
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        fl_list[15] = '1101:客商'
        out_ws.append(fl_list)

    elif SInfo_df['工资结算户'][YYB_bm] == "基本户":
        kmbm = SInfo_df['基本户-科目编码'][YYB_bm]
        yhzh = SInfo_df['基本户-银行账户编码'][YYB_bm] + ':银行账户'
        if pd.isna(SInfo_df)['基本户-科目编码'][YYB_bm]:  # pd.isna(SInfo_df)将各元素值转化为True或False
            kmbm = '1001'
            yhzh = ''

        fl_list[5] = '发放经纪人委托费'
        fl_list[6] = kmbm
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        fl_list[15] = yhzh
        out_ws.append(fl_list)

    elif SInfo_df['工资结算户'][YYB_bm] == "现金":
        fl_list[5] = '发放经纪人委托费'
        fl_list[6] = '1001'
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        out_ws.append(fl_list)


case = {
    "6421070101": km6421070101,  # 手续费及佣金支出\佣金提成
    "6421070102": km6421070102,  # 手续费及佣金支出\业务拓展费
    "6421070103": km6421070103,  # 手续费及佣金支出\其他经纪人提成
    "6421070104": km6421070104,  # 手续费及佣金支出\服务提成
    "6421070105": km6421070105,  # 手续费及佣金支出\期权业务提成
    "6421070106": km6421070106,  # 手续费及佣金支出\IB业务提成
    "6421070107": km6421070107,  # 手续费及佣金支出\管理津贴
    "6421070108": km6421070108,  # 手续费及佣金支出\投顾业务提成
    "6421070109": km6421070109,  # 手续费及佣金支出\其他
    "6421070110": km6421070110,  # 手续费及佣金支出\开户奖
    "6421070111": km6421070111,  # 手续费及佣金支出\两融净息差提成

    "6421070201": km6421070201,  # 手续费及佣金支出\公募基金保有量提成
    "6421070202": km6421070202,  # 手续费及佣金支出\公募基金销售奖励
    "6421070203": km6421070203,  # 手续费及佣金支出\基金分仓销售奖励

    "6421070301": km6421070301,  # 手续费及佣金支出\公募基金销售手续费返还
    "6421070302": km6421070302,  # 手续费及佣金支出\公司理财产品销售提成
    "6421070303": km6421070303,  # 手续费及佣金支出\代理销售保险产品
    "6421070304": km6421070304,  # 手续费及佣金支出\非公募产品销售奖励

    "22411901": km22411901,  # 总部下拨奖励挂账
    "22211401": km22211401,  # 应付经纪人增值税
    "22211402": km22211402,  # 应付经纪人城建税
    "22211403": km22211403,  # 应付经纪人教育费附加
    "22211407": km22211407,  # 应付经纪人地方教育费附加
    "222105": km222105,  # 应付个税

    "6601070201": km6601070201,  # 扣员工宿舍房租
    "224107": km224107,  # 应付风险金
}

kmdm = [*case]  # kmdm = list(case)


def switcher(dict, argument, fl_list, amt, jbb, in_df, out_ws):
    # Get the function from switcher dictionary
    func = dict.get(argument, lambda argument, fl_list, amt, jbb, in_df, out_ws: None)
    # Execute the function
    return func(argument, fl_list, amt, jbb, in_df, out_ws)
