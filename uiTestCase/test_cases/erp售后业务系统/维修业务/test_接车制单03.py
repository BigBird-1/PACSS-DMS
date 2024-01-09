# -*- coding:utf-8 -*
# @FileName:   test_接车制单03.py
# @Author:     刘峰
# @CreateTime: 2022/8/2 16:48

"""
    接车制单测试用例组：
        14、购买套餐；    15、生成，使用优惠券；
"""

import allure

from page.erp售后业务系统.维修业务.接车制单详情页 import CustomerReceptionEditMainPage
from page.erp售后业务系统.维修业务.接车制单页 import CustomerReceptionPage
from page.erp售后业务系统.维修业务.结算页 import BalancePage
from page.erp财务系统.收银台.新收银台页 import NewCashierDeskPage
from page.erp配件系统.配件管理.配件出库管理.编辑维修领料页 import EditRepairOutPage
from page.erp配件系统.配件管理.配件出库管理.配件维修领料页 import RepairOutPage

@allure.feature("接车制单功能测试")
class TestCustomerReception03:

    @allure.title("接车制单初始化方法03")
    def test_begin(self, login):
        TestCustomerReception03.crp = CustomerReceptionPage(login)
        TestCustomerReception03.crep = CustomerReceptionEditMainPage(login)
        TestCustomerReception03.rop = RepairOutPage(login)
        TestCustomerReception03.erop = EditRepairOutPage(login)
        TestCustomerReception03.cdp = NewCashierDeskPage(login)
        TestCustomerReception03.bp = BalancePage(login)


    @allure.title("测试用例14：购买套餐；")
    def test_buySetMeal(self):

        with allure.step("步骤1：跳转到新增接车制单页面；"):
            self.crp.skipToAdd()

        with allure.step("步骤2：购买套餐；"):
            self.crep.buySetMeal(license='鄂CHZ85S', setmeal='惠保', secondlevel='A保', salepeople='超级管理员')

        with allure.step("步骤3：验证购买套餐申请是否成功；"):
            actual = self.crep.webDriverWait(self.crep.apply_finance_success).text
            expect = "申请成功"
            assert expect in actual

        with allure.step("后置处理：取消打印，关闭购买套餐窗口；"):
            self.crep.click(self.crep.cancle_print)
            self.crep.click(self.crep.close_button)
            self.crep.click(self.crep.goback_button)


    @allure.title("测试用例15：生成，使用优惠券；")
    def test_discountCoupon(self):

        with allure.step("步骤1：生成优惠券，到新收银台进行惠保收款；"):
            self.cdp.cashierDeskReceipt('鄂CHZ85S')
            self.crep.click(self.crep.goback_button)

        with allure.step("步骤2：使用优惠券，通过添加优惠券，新增接车制单；"):
            self.crp.skipToAdd()
            self.crep.addOrderByDiscountCoupon(license='鄂CHZ85S', servicepeople='超级管理员', chargedifferent='客户付费',
                                               warehouse="原厂库", partsnumber=".641010R500",
                                               insurancetype='机动车第三者责任保险', insurancecompany='中国平安保险（集团）股份有限公司')
            self.crep.cancleSyscDMS()
            self.crep.click(self.crep.goback_button)

            TestCustomerReception03.order_number = self.crp.getOrderNumber()

        with allure.step("步骤3：维修领料；"):
            self.rop.skipToMaintainPick(TestCustomerReception03.order_number)
            self.erop.editMaintainPick("周海波")
            self.crep.click(self.crep.goback_button)

        with allure.step("步骤4：提交结算，结算，使用惠保券；"):
            self.crp.skipToEdit(TestCustomerReception03.order_number)
            self.crep.editAustomerReception(2022080144316, 200)
            self.crep.commitPay()
            self.crep.click(self.crep.settle_account_button)
            self.crep.wait(1)
            self.bp.payBalance(suggest="维修建议输入", isusediscount=True)

        # with allure.step("步骤5：验证结算是否成功."):
        #     actual = self.bp.webDriverWait(self.bp.pay_success).text
        #     expect = "结算成功"
        #     assert expect in actual

        with allure.step("后置处理：取消同步到DMS，关闭结算页面，关闭接车制单编辑页面"):
            self.crep.cancleSyscDMS()
            self.crep.click(self.crep.goback_button)
            self.crep.click(self.crep.goback_button)