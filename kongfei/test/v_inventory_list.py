CREATE OR REPLACE VIEW V_INVENTORY_LIST AS
SELECT t1."DISTRICTCODE",t1."DISTRICTID",t1."INSTITUTIONNAME",t1."INSTITUTIONCODE",t1."SYSDIRITEMID",t1."NATIONALDRUGCODE",t1."USAGEUNITAMOUNTPERPACKAGE",t1."GENERICNAME",t1."PACKAGEUNITREFNAME",t1."DRUGSPEC",t1."PRODUCTIONUNIT",
t1."ACTUALAMOUNT",t1."INPAMOUNT",t1."CHECKTIME",t1."OUTAMOUNT",t1."NOWAMOUNT",t1."USAGEUNITREFNAME", t2.PACKAGE_CNT, ROUND(((T1.NOWAMOUNT - t2.PACKAGE_CNT)/(t1.OUTAMOUNT + t2.PACKAGE_CNT)),4)*100 AS PERCENT_OFFSET, ABS(ROUND(((T1.NOWAMOUNT - t2.PACKAGE_CNT)/(t1.OUTAMOUNT + t2.PACKAGE_CNT)),4)*100) AS PERCENT_OFFSET_ABS, t2.ACCOUNT_DATE FROM
(select --tt."CE_INVENT_REG_ID",
tt."DISTRICTCODE",tt."DISTRICTID",tt."INSTITUTIONNAME",tt."INSTITUTIONCODE",
--tt."PHARMACYNAME",
--tt."PHARMACYID",
tt."SYSDIRITEMID",tt."NATIONALDRUGCODE",tt."USAGEUNITAMOUNTPERPACKAGE",tt."GENERICNAME",tt."PACKAGEUNITREFNAME",tt."DRUGSPEC",tt."PRODUCTIONUNIT",tt."ACTUALAMOUNT",tt."INPAMOUNT",tt."CHECKTIME",
sum(nvl(out.CNT,0)) as outamount,
(tt.actualamount + tt.inpamount - sum(nvl(out.CNT,0))) as nowamount,
tt.usageunitrefname
from
(Select  -- reg.ce_invent_reg_id,
reg.districtcode,reg.districtid, item.institutionname,item.institutioncode,
--reg.pharmacyname,reg.pharmacyid,
reg.sysdiritemid,reg.nationaldrugcode,
item.usageunitamountperpackage,item.genericname,item.packageunitrefname,item.drugspec,item.productionunit,item.usageunitrefname,
reg.actualamount,
sum(
   Case When item.packageunitrefname = item.usageunitrefname Then  nvl(inp.drugamount,0) Else
Case When  inp.packageunitrefname=item.packageunitrefname Then nvl(inp.drugamount,0)*nvl(item.usageunitamountperpackage,0) Else nvl(inp.drugamount,0) End End
)
as inpamount,
reg.checktime
From ce_inventorymonitor_items item,
   (SELECT a.* FROM (select Distinct row_number() over(PARTITION BY t.pharmacyid,t.nationaldrugcode,t.institutioncode ORDER BY t.checktime Desc) As rn,t.* from ce_invent_reg t where t.checktime is not Null And t.actualamount Is Not Null
      and t.isdeleted <> 1)a,
(select b.INSTITUTIONCODE, b.NATIONALDRUGCODE, max(b.CHECKTIME) as CHECKTIME from ce_invent_reg b GROUP BY b.INSTITUTIONCODE, b.NATIONALDRUGCODE) c
WHERE a.INSTITUTIONCODE = c.INSTITUTIONCODE
AND a.NATIONALDRUGCODE = c.NATIONALDRUGCODE AND a.CHECKTIME = c.CHECKTIME ORDER BY a.CHECKTIME ASC) reg
Left Join (SELECT i.* FROM ce_inventmondrug_inputs i, CE_INVENTORY_CONTROL c WHERE i.INSTITUTIONCODE=c.INSTITUTION_CODE AND i.PHARMACYHISID=c.DRUG_STORE_CODE AND c.IS_CHECK_IN = '1' ) inp
 On --inp.pharmacyhisid = reg.pharmacyid  and
 inp.nationaldrugcode = reg.nationaldrugcode and inp.inputtime > reg.checktime and inp.institutioncode = reg.institutioncode
Where   reg.rn = 1 and item.nationaldrugcode = reg.nationaldrugcode And item.institutioncode=reg.institutioncode
 and item.isdeleted <> 1
group by reg.ce_invent_reg_id,reg.districtcode,reg.districtid, item.institutionname,item.institutioncode,--reg.pharmacyname,reg.pharmacyid,
reg.sysdiritemid,reg.nationaldrugcode,
item.usageunitamountperpackage,item.genericname,item.packageunitrefname,item.drugspec,item.productionunit,item.usageunitrefname,reg.actualamount,reg.checktime
) tt
left join (SELECT o.* FROM CE_INVENTORY_OUT o, CE_INVENTORY_CONTROL c
WHERE  o.INSTITUTION_CODE=c.INSTITUTION_CODE
AND o.DRUG_STORE_CODE=c.DRUG_STORE_CODE AND ((c.IS_CHECK_OUT = '1' AND o.PATIENT_CODE IS NOT NULL)
OR  (c.IS_RETURN_BACK = '1' AND o.PATIENT_CODE IS NULL))) out
on out.NATIONAL_DRUG_CODE = tt.nationaldrugcode and out.INSTITUTION_CODE = tt.institutioncode  And out.PAY_DATE >  tt.checktime
group by --tt.ce_invent_reg_id,
tt.districtcode,tt.districtid, tt.institutionname,tt.institutioncode,--tt.pharmacyname,tt.pharmacyid,
tt.sysdiritemid,tt.nationaldrugcode,
tt.usageunitamountperpackage,tt.genericname,tt.packageunitrefname,tt.drugspec,tt.productionunit,tt.actualamount,tt.inpamount,tt.checktime,tt.usageunitrefname) t1,
(SELECT t.INSTITUTION_CODE, t.INSTITUTION_NAME, t.NATIONAL_DRUG_CODE, t.ITEM_HIS_NAME, t.ACCOUNT_DATE, sum(t.PACKAGE_CNT) AS PACKAGE_CNT
FROM (select a.* FROM CE_INVENTORY_ACCOUNT a )  t, CE_INVENTORY_CONTROL c WHERE t.INSTITUTION_CODE =c.INSTITUTION_CODE AND t.DRUG_STORE_CODE=c.DRUG_STORE_CODE AND c.IS_ACCOUNT = '1'
GROUP BY t.INSTITUTION_CODE, t.INSTITUTION_NAME, t.NATIONAL_DRUG_CODE, t.ITEM_HIS_NAME , t.ACCOUNT_DATE) t2
WHERE t1.INSTITUTIONCODE = t2.INSTITUTION_CODE AND T1.NATIONALDRUGCODE = T2.NATIONAL_DRUG_CODE
ORDER BY T2.ACCOUNT_DATE DESC;
