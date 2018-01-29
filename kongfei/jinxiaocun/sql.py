import unittest


class Jxc(object):
    def __init__(self,nationaldrugcode):
        self.nationaldrugcode=nationaldrugcode

    def sjkc(self):  #实际库存

        s=""
        for i in range(len(self.nationaldrugcode)):
            hiskc = "select sum(package_cnt)his实际库存,%s 药品本位码 from ce_inventory_account where to_char(account_date,'YYYY-MM-DD hh24:mi:ss')=(select max(to_char(account_date,'YYYY-MM-DD hh24:mi:ss')) from ce_inventory_account) and national_drug_code=%s;"%(self.nationaldrugcode[i],self.nationaldrugcode[i])


            s+=hiskc


        l=s.replace(';',' union ',len(self.nationaldrugcode)-1)

        print(l)


    def ljkc(self): #累计库存
        s=""
        for i in range(len(self.nationaldrugcode)):
            ljkc = "select t1.期初库存+t2.入库数量-t3.退药到医药公司数量 累计库存,%s 药品本位码 from (select actualamount 期初库存 from ce_invent_reg  where institutioncode=181160 and nationaldrugcode=%s and to_char(checktime,'YYYY-MM-DD hh24:mi:ss')=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),'YYYY-MM-DD hh24:mi:ss' ))t1,  (select sum(drugamount*packageproportion) 入库数量 from ce_inventory_in_181160 where nationaldrugcode=%s and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),'YYYY-MM-DD hh24:mi:ss' ))t2,  (select sum(cnt) 退药到医药公司数量 from ce_inventory_out_181160 where national_drug_code =%s and patient_type=0  and to_char(pay_date,'YYYY-MM-DD hh24:mi:ss')>=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),'YYYY-MM-DD hh24:mi:ss' ))t3;" %(self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i])
            s+=ljkc
        l = s.replace(';', ' union ', len(self.nationaldrugcode) - 1)
        print(l)

    def pcbfb(self): #偏差百分比
        s=""
        for i in range(len(self.nationaldrugcode)):

            # pcbfb = "select to_char(round（（t4.累计库存-t5.当期销售-t6.his实际库存)/t4.累计库存*100,2),'fm999990.99999'）||'%' 偏差百分比 from (select t1.期初库存+t2.入库数量-t3.退药到医药公司数量  累计库存 from (select actualamount 期初库存 from ce_invent_reg  where institutioncode=181160 and nationaldrugcode={0} and to_char(checktime,'YYYY-MM-DD hh24:mi:ss')=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),'YYYY-MM-DD hh24:mi:ss' ))t1,  (select sum(drugamount*packageproportion) 入库数量 from ce_inventory_in_181160 where nationaldrugcode={1} and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>='2017-04-24 9:10:25')t2,  (select sum(cnt) 退药到医药公司数量 from ce_inventory_out_181160 where national_drug_code ={2} and patient_type=0  and to_char(pay_date,'YYYY-MM-DD hh24:mi:ss')>='2017-04-24 9:10:25')t3)t4,(SELECT   sum(cnt)当期销售 from ce_inventory_out_181160 where national_drug_code={3} and patient_type!=0  and to_char(pay_date,'YYYY-MM-DD hh24:mi:ss')>='2017-04-24 9:10:25')t5,(select sum(package_cnt) his实际库存 from ce_inventory_account where to_char(account_date,'YYYY-MM-DD hh24:mi:ss')=(select max(to_char(account_date,'YYYY-MM-DD hh24:mi:ss')) from ce_inventory_account) and national_drug_code={4})t6;".format(self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i])

            pcbfb = "select to_char(round（（t4.累计库存-t5.当期销售-t6.his实际库存)/t4.累计库存*100,2),'fm999990.99999'）||'%s' 偏差百分比,%s 药品本位码 from (select t1.期初库存+t2.入库数量-t3.退药到医药公司数量  累计库存 from (select actualamount 期初库存 from ce_invent_reg  where institutioncode=181160 and nationaldrugcode=%s and to_char(checktime,\'YYYY-MM-DD hh24:mi:ss\')=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),\'YYYY-MM-DD hh24:mi:ss\' ))t1,  (select sum(drugamount*packageproportion) 入库数量 from ce_inventory_in_181160 where nationaldrugcode=%s and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>='2017-04-24 9:10:25')t2,  (select sum(cnt) 退药到医药公司数量 from ce_inventory_out_181160 where national_drug_code =%s and patient_type=0  and to_char(pay_date,\'YYYY-MM-DD hh24:mi:ss\')>='2017-04-24 9:10:25')t3)t4,(SELECT   sum(cnt)当期销售 from ce_inventory_out_181160 where national_drug_code=%s and patient_type!=0  and to_char(pay_date,'YYYY-MM-DD hh24:mi:ss')>='2017-04-24 9:10:25')t5,(select sum(package_cnt) his实际库存 from ce_inventory_account where to_char(account_date,'YYYY-MM-DD hh24:mi:ss')=(select max(to_char(account_date,'YYYY-MM-DD hh24:mi:ss')) from ce_inventory_account) and national_drug_code=%s)t6;" % ('%',self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i],self.nationaldrugcode[i])

            s += pcbfb
        l = s.replace(';', ' union ', len(self.nationaldrugcode) - 1)
        print(l)


if __name__ == '__main__':
    test= Jxc(['86902033000258','86903942000995','86900600001233','86902610000015'])
    # test.ljkc()
    test.pcbfb()


