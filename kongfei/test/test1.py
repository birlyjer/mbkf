# coding=utf-8
from resource.resource import *
from resource.logger import *
import cx_Oracle

db = dbcon('zh01')  # 建立连接
cr = db.cursor()  # 创建游标
# sql = 'select * from ce_inventorymonitor_items'
# cr.execute(sql)
# rs = cr.fetchall()

monitor_181220 = "select nationaldrugcode,genericname  from ce_inventorymonitor_items where institutioncode=181220"

cr.execute(monitor_181220)
monitor_181220_drugs = cr.fetchall()

drug_code = [x[0] for x in monitor_181220_drugs]
drug_name = [x[1] for x in monitor_181220_drugs]


# drug_code = [ '86902122000015']
# drug_code=['86904520000024', '86901013000042', '86902122000015', '86902033000258', '86900002000018', '86979489000088', '86903098000092', '86901187000060', '86979096001782', '86979096001805', '86902300000066', '86901187000084', '86903447000025', '86906632000053', '86900347000131', '86979263000013', '86900288001648', '86900044000014', '86900818002848', '86978997002713', '86978997002706', '86903973001237', '86978814000953', '86904647000327', '86900871000102', '86903922000694', '86901359000164', '86901359000188', '86978574000163', '86901427001017', '86904756000157', '86900941000094', '86900144004882', '86900371000275', '86979462000074', '86902181000339', '86978820000596', '86900599000521', '86900842000261', '86902529000205', '86901034000274', '86901470001590', '86901554000686', '86900177000134', '86901379000427', '86902068001053', '86905437000923', '86900228000069', '86978604000538', '86909198000017', '86901519000287', '86902959001155', '86901844000136', '86900227000053', '86900227000039', '86903546000032', '86900176000951', '86902777003355', '86902201000035', '86900964000200', '86900847000037', '86901359000355', '86901493000150', '86902120000277', '86902204001015', '86902959001513', '86905601000315', '86901693000059', '86900166001012', '86978403001156', '86978403001378', '86900600001233', '86900600001240', '86901359000102', '86901470000685', '86901034000113', '86978403000722', '86905490000106', '86978303000112', '86978814000984', '86900553000581', '86901844000242', '86902944000996', '86905801000382', '86904960000127', '86902770002300', '86907103000046', '86907103000022', '86978997002782', '86904747002030', '86904250000042', '86900290000158', '86900374000418', '86902547000010', '86902959000523', '86907103000015', '86978997002485', '86978997002218', '86978997002461', '86978997002096', '86900847000051', '86901503000194', '86978997002645', '86900014000211', '86978241000953', '86901359000416', '86900674000453', '86902959000714', '86902041000035', '86900961000067', '86902610000015', '86903722000016', '86902767000517', '86904073000236', '86900428000630', '86903942000995', '86978269000362', '86900785000373', '86902968001016', '86900202000511', '86905199000117', '86900100000095', '86900453000643', '86902181000384', '86902096000110', '86900407000101', '86904131000260', '86905698000441', '86905703000756', '86900818001360', '86900553000130', '86901729000282', '86902135000729', '86900120000037', '86904145001178', '86906632000022']


# 期初库存
def beginning_num(i):
    beginning_num = "select actualamount from ce_invent_reg  where institutioncode=181220 and nationaldrugcode=%s and to_char(checktime,'YYYY-MM-DD hh24:mi:ss')=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181220 and nationaldrugcode=%s),'YYYY-MM-DD hh24:mi:ss' ) " % \
                    (drug_code[i], drug_code[i])
    cr.execute(beginning_num)
    rs = cr.fetchall()

    beginning_num_int = int(rs[0][0])
    # print(drug_code[i],'的期初库存为:',beginning_num_int,'  ',end='')
    return beginning_num_int


# for i in range(len(drug_code)):
#     beginning_num(i)


# 当期入库
def in_num(i):
    in_num = "SELECT sum(Case When bigact.packageunitrefname = bigact.usageunitrefname Then  nvl(inp.drugamount,0) Else Case When  inp.packageunitrefname=bigact.packageunitrefname Then nvl(inp.drugamount,0)*nvl(bigact.usageunitamountperpackage,0) Else nvl(inp.drugamount,0) End End) from ce_inventorymonitor_items bigact left JOIN ce_inventmondrug_inputs inp ON bigact.nationaldrugcode  = inp.nationaldrugcode  and inp.nationaldrugcode =%s and bigact.institutioncode='181220'"%drug_code[i]

    cr.execute(in_num)
    rs = cr.fetchall()
    if rs != [(None,)]:
        in_num_int = int(rs[0][0])
    else:
        in_num_int = 0
    # print(drug_code[i], '的当期入库为:',in_num_int,'  ',end='')
    return in_num_int









# 当期出库
def out_num(i):
    out_num = "SELECT   sum(cnt) from ce_inventory_out_181220 where national_drug_code=%s" % \
              drug_code[i]
    cr.execute(out_num)
    rs = cr.fetchall()
    if rs != [(None,)]:
        out_num_int = int(rs[0][0])
    else:
        out_num_int = 0
    # print(drug_code[i],'的当期出库库为:',out_num_int,'  ',end='')
    return out_num_int


# for i in range(len(drug_code)):
#     out_num(i)


# his实际库存
def actual_num(i):
    actual_num = "select sum(package_cnt)his实际库存最新 from ce_inventory_account_181220 where national_drug_code=%s and drug_store_name !='住院部药房' and account_date = (select max(account_date) from ce_inventory_account_181220 where national_drug_code=%s )" % \
                 (drug_code[i],drug_code[i])
    cr.execute(actual_num)
    rs = cr.fetchall()
    if rs != [(None,)]:
        actual_num_int = int(rs[0][0])
    else:
        actual_num_int = 0
    # print(drug_code[i], '的实际库存为:',actual_num_int)
    return actual_num_int


# # 偏差百分比
# def pcbfb(i):
#     pcbfb = (beginning_num(i) + in_num(i) - out_num(i) - actual_num(i)) / (beginning_num(i) + in_num(i))
#     return pcbfb

def pcbfb(i):
    if out_num(i) + actual_num(i)==0:
        pcbfb=1
    else:
        pcbfb = (beginning_num(i) + in_num(i) - out_num(i) - actual_num(i)) / (out_num(i) + actual_num(i))

    return pcbfb


# 销售金额
def sailes_sum(i):
    sailes_sum = "select sum(total_price)  from ce_inventory_out_181220 where national_drug_code=%s" % drug_code[i]
    cr.execute(sailes_sum)
    rs = cr.fetchall()
    if rs != [(None,)]:
        sailes_sum_float = int(rs[0][0])
    else:
        sailes_sum_float = 0
    return sailes_sum_float


# 购买金额
def purchase_sum(i):
    purchase_sum = "select sum(totalvalue) from ce_inventory_in_181220 where nationaldrugcode =%s" % drug_code[i]
    cr.execute(purchase_sum)
    rs = cr.fetchall()
    if rs != [(None,)]:
        purchase_sum_float = int(rs[0][0])
    else:
        purchase_sum_float = 0
    return purchase_sum_float

drug_dict={}
for i in range(len(drug_code)):
    #pcbfb=(beginning_num(i) + in_num(i) - out_num(i) - actual_num(i)) / (beginning_num(i) + in_num(i))
    pcl=beginning_num(i) + in_num(i) - out_num(i) - actual_num(i)#偏差量
    beginning_num(i), in_num(i), out_num(i), actual_num(i)
    print(drug_code[i], '的期初库存为：%d  当期入库为：%d  当期出库为：%d  实际库存为：%d  偏差百分比为：%.2f%%  偏差量为：%d  销售金额为：%.2f  购买金额为：%.2f' % (
    beginning_num(i), in_num(i), out_num(i), actual_num(i),pcbfb(i)*100,pcl,sailes_sum(i),purchase_sum(i)
    ))

    jxc_list_value=[beginning_num(i),in_num(i),out_num(i),actual_num(i),'%.2f%%'%(pcbfb(i)*100),pcl,sailes_sum(i),purchase_sum(i)]
    jxc_list_key=['期初库存','当期入库','当期出库','His实际库存','偏差百分比','偏差量','销售金额','购买金额']
    zh = zip(jxc_list_key,jxc_list_value)
    jxc_drug = dict((jxc_list_key,jxc_list_value) for jxc_list_key,jxc_list_value in zh)

    drug_dict[drug_code[i]]=jxc_drug

print(drug_dict)
