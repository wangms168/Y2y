import pandas as pd


def km66011501(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = '22110101'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放工资'
    fl_list[6] = '22110101'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011501_D(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = '66011509'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = '22110105'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放工资'
    fl_list[6] = '22110105'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011501_L(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = '66011519'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '计提工资'
    fl_list[6] = '22110103'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放工资'
    fl_list[6] = '22110103'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011502(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提奖金'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '计提奖金'
    fl_list[6] = '22110102'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放奖金'
    fl_list[6] = '22110102'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011503(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提过节费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011504(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提交通补贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011505(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提伙食补贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011506(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提通讯补贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011507(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提辞退福利'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '计提辞退福利'
    fl_list[6] = '221109'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放辞退福利'
    fl_list[6] = '221109'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011510(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提劳保补贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011519(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提其他补贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km22110103(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提补贴小计'
    fl_list[6] = '22110103'
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放补贴小计'
    fl_list[6] = '22110103'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km66011601(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提医疗卫生'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011602(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提防暑降温'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011603(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提取暖费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011604(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提独生子女费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011605(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提文体宣传费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011606(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提探亲路费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011607(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提职工困难补助'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011608(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提丧葬抚恤救济费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011609(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提食堂费用'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km66011619(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提其他福利费'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km221102(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提福利小计'
    fl_list[6] = '221102'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None

    out_ws.append(fl_list)
    fl_list[5] = '【' + lb_2 + '】' + '发放福利小计'
    fl_list[6] = '221102'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km660115080101(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提佣金提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080102(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提服务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080103(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提期权业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080104(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提IB业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080105(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提管理津贴'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080106(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提投顾业务提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080107(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提两融净息差提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km660115080108(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提开户奖'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150802(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提基金保有量提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150803(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提基金销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150804(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提基金销售手续费返还'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150805(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提公司理财产品销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150806(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提代理销售保险产品'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150807(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提非公募产品销售奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601150819(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '计提其他提成'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[15] = jbb + ':部门'
    fl_list[16] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km22110104(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    #    if '22411901' in in_df.columns:
    #        print('有22411901')
    #        var = round(in_df['22411901']['合计'], 2)  # 总部下拨奖励合计金额
    #        amt = amt - var
    #    else:
    #        print('无22411901')

    fl_list[5] = '【' + lb_2 + '】' + '计提提成小计'
    fl_list[6] = '22110104'
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)

    fl_list[5] = '【' + lb_2 + '】' + '发放提成小计'
    fl_list[6] = '22110104'
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = lb_1 + ':人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


def km22411901(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '发放总部下拨奖励'
    fl_list[6] = k
    fl_list[8] = str(amt)
    fl_list[9] = str(amt)
    out_ws.append(fl_list)


def km22410401(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣个人养老'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22410402(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣个人失业'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22410403(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣个人医疗'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22410404(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣个人公积金'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km22410409(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣其他保险(企业年金)'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    out_ws.append(fl_list)


def km222105(k, fl_list, amt, lb, jbb, in_df, out_ws):
    lb_1 = lb.split(':')[0]
    lb_2 = lb.split(':')[1]

    fl_list[5] = '【' + lb_2 + '】' + '扣个人所得税'
    fl_list[6] = k
    fl_list[11] = str(amt)
    fl_list[12] = str(amt)
    fl_list[15] = lb_1 + ':人员类别'
    out_ws.append(fl_list)


def km6601070201(k, fl_list, amt, lb, jbb, in_df, out_ws):
    fl_list[5] = '扣房租'
    fl_list[6] = k
    fl_list[8] = str(-amt)
    fl_list[9] = str(-amt)
    fl_list[15] = jbb + ':部门'
    out_ws.append(fl_list)


def km224107(k, fl_list, amt, lb, jbb, in_df, out_ws):
    s = in_df[k]  # 获取'224107'这一列pd.Serie这个对象 
    # 对这个pd.Serie进行瘦身过滤下
    tc_list = ['A1小计', 'A2小计', 'A小计', 'B小计', 'D小计', 'L小计', '合计']
    s = s[~s.index.isin(tc_list)]          # 对这个pd.Serie过滤掉ti-list  ~是对True或Fault逻辑值取反
    # print("风险金",s)

    for i, v in s.items():  # items是pd.Serie的每个项目，i是键(df的index)、v是值('224107'这列上的数据)
        # if v and (not (pd.isnull(v))) and i != 'A1小计' and i != 'A2小计' and i != 'A小计' and i != 'B小计' and i != 'D小计' and i != 'L小计' and i != '合计':
        if v and (not (pd.isnull(v))):
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


def km1001(SInfo_df, fl_list, amt, jbb, in_df, out_ws):
    YYB_bm = fl_list[10]

    if SInfo_df['工资结算户'][YYB_bm] == "总部统一结算":
        kmbm = "114305"

        fl_list[5] = '发放员工工资'
        fl_list[6] = kmbm
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        fl_list[15] = '1101:客商'
        out_ws.append(fl_list)

    elif SInfo_df['工资结算户'][YYB_bm] == "基本户":
        kmbm = SInfo_df['基本户-科目编码'][YYB_bm]
        yhzh = SInfo_df['基本户-银行账户编码'][YYB_bm] + ':银行账户'

        if pd.isna(SInfo_df)['基本户-科目编码'][YYB_bm]:  # 若“科目编码”为空、则使用1001。 pd.isna(SInfo_df)将各元素值转化为True或False
            kmbm = '1001'
            yhzh = ''

        fl_list[5] = '发放员工工资'
        fl_list[6] = kmbm
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        fl_list[15] = yhzh
        out_ws.append(fl_list)

    elif SInfo_df['工资结算户'][YYB_bm] == "现金":
        fl_list[5] = '发放员工工资'
        fl_list[6] = '1001'
        fl_list[11] = str(amt)
        fl_list[12] = str(amt)
        out_ws.append(fl_list)

    var = round(in_df['66011501']['合计'], 2)  # 基本工资合计数
    if 'D小计' in in_df.index:
        var_D = round(in_df['66011501']['D小计'], 2)
        var -= var_D
    if 'L小计' in in_df.index:
        var_L = round(in_df['66011501']['L小计'], 2)
        var -= var_L

    fl_list[5] = '计提2%的工会经费'
    fl_list[6] = '660117'
    fl_list[8] = str(round(var * 0.02, 2))
    fl_list[9] = str(round(var * 0.02, 2))
    fl_list[11] = None
    fl_list[12] = None
    fl_list[15] = jbb + ':部门'
    fl_list[16] = '01:人员类别'
    out_ws.append(fl_list)

    fl_list[5] = '计提2%的工会经费'
    fl_list[6] = '221105'
    fl_list[8] = None
    fl_list[9] = None
    fl_list[11] = str(round(var * 0.02, 2))
    fl_list[12] = str(round(var * 0.02, 2))
    fl_list[15] = '01:人员类别'
    fl_list[16] = None
    out_ws.append(fl_list)


dict_AB = {
    "66011501": km66011501,  # 工资
    "66011502": km66011502,  # 奖金
    "66011503": km66011503,  # 过节费
    "66011504": km66011504,  # 交通补贴
    "66011505": km66011505,  # 伙食补贴
    "66011506": km66011506,  # 通讯补贴
    "66011510": km66011510,  # 劳保补贴
    "66011519": km66011519,  # 其他补贴
    "22110103": km22110103,  # 应付工资\其他  补贴小计
    "66011507": km66011507,  # 辞退福利

    "66011601": km66011601,  # 医疗卫生
    "66011602": km66011602,  # 防暑降温费
    "66011603": km66011603,  # 取暖费
    "66011604": km66011604,  # 独生子女费
    "66011605": km66011605,  # 文体宣传费
    "66011606": km66011606,  # 探亲路费
    "66011607": km66011607,  # 职工困难补助
    "66011608": km66011608,  # 丧葬抚恤救济费
    "66011609": km66011609,  # 食堂费用
    "66011619": km66011619,  # 其他福利
    "221102": km221102,      # 应付福利

    "660115080101": km660115080101,  # 佣金提成
    "660115080102": km660115080102,  # 服务提成
    "660115080103": km660115080103,  # 期权业务提成
    "660115080104": km660115080104,  # IB业务提成
    "660115080105": km660115080105,  # 管理津贴
    "660115080106": km660115080106,  # 投顾业务提成
    "660115080107": km660115080107,  # 两融净息差提成
    "660115080108": km660115080108,  # 开户奖
    "6601150802": km6601150802,  # 基金保有量提成
    "6601150803": km6601150803,  # 基金销售奖励
    "6601150804": km6601150804,  # 基金销售手续费返还
    "6601150805": km6601150805,  # 公司理财产品销售奖励
    "6601150806": km6601150806,  # 代理销售保险产品
    "6601150807": km6601150807,  # 非公募产品销售奖励
    "6601150819": km6601150819,  # 其他
    "22110104": km22110104,      # 应付提成支出
    "222105": km222105,          # 应付个税
}

dict_D = dict_AB.copy()
dict_D["66011501"] = km66011501_D  # D类人员
dict_L = dict_AB.copy()
dict_L["66011501"] = km66011501_L  # L类人员

dict = {
    "22411901": km22411901,  # 总部下拨奖励
    "22410401": km22410401,  # 应付个人养老
    "22410402": km22410402,  # 应付个人失业
    "22410403": km22410403,  # 应付个人医疗
    "22410404": km22410404,  # 应付个人公积金
    "22410409": km22410409,  # 应付企业年金(其他保险)
    "6601070201": km6601070201,  # 扣员工宿舍房租
    "224107": km224107,  # 应付风险金
}

kmdm = [*dict_AB] + [*dict]  # kmdm = list(dict_AB)


def switcher(dict, argument, fl_list, amt, lb, jbb, in_df, out_ws):
    # Get the function from switcher dictionary
    func = dict.get(argument, lambda argument, fl_list, amt, lb, jbb, in_df, out_ws: None)
    # Execute the function
    return func(argument, fl_list, amt, lb, jbb, in_df, out_ws)
