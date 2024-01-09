# -*- coding:utf-8 -*
# @FileName:   接车制单新增页.py
# @Author:     刘峰
# @CreateTime: 2022/7/23 15:16

"""
    接车制单新增页，也叫接车制单详情页，可以新增和编辑
"""
from selenium.webdriver import Keys

from base.base_page import BasePage


class CustomerReceptionEditMainPage(BasePage):

    # 返回按钮
    goback_button = ("xpath", "//*[@id='section']/div[1]/div[1]/div/button")

    # 新建按钮
    new_button = ("xpath", "//span[text()='新建']")
    # 保存按钮
    save_button = ("xpath", "//span[text()='保存']")
    # 打印工单按钮
    print_order_button = ("xpath", "//span[text()='打印工单']")
    # 员工车校验按钮
    check_staff_car = ("xpath", "//span[text()='员工车校验']")
    # 商品车维修申请按钮
    apply_maintain_button = ("xpath", "//span[text()='商品车维修申请']")
    # 取消按钮
    cancle_order_button = ("xpath", "//*[@id='app']/div/div[1]/button[6]/span")
    # 派工按钮
    dispatching_button = ("xpath", "//span[text()='派工']")
    # 提交结算按钮
    commit_account_button = ("xpath", "//span[text()='提交结算']")
    # 结算按钮
    settle_account_button = ("xpath", "//span[text()='结算']")
    # 解锁出清材料
    unlock_clear_materials = ("xpath", "//span[text()='解锁出清材料']")

    # 工单号输入框
    work_num = ("xpath", "//label[@for='id.roNo']/../div/div/input")
    # 服务专员输入框
    service_people_input = ("xpath", "//label[@for='serviceAdvisor']/../div/div/div/input")
    # 厂家委托书号
    factory_entrust_number = ("xpath", "//label[@for='commission']/../div/div/input")
    # 行驶里程
    travel_distance = ("xpath", "//label[@for='inMileage']/../div/div/div/input")
    # 保修到期日期
    after_service_data = ("xpath", "//label[@for='wrtEndDate']/../div/div/input")
    # 车牌号搜索按钮
    license_select_button = ("xpath", "//label[@for='license']/../div/div/span/span/button")
    # 添加维修明细按钮
    add_maintain_detail = ("xpath", "//span[text()='添加维修明细']")

    """
        选择车主车辆窗口
    """
    # 车牌号输入框
    license_input = ("xpath", "//div[@id='searchFormView']/form/div/div[1]/div/div/div/input")
    # VIN输入框
    vin_input = ("xpath", "//*[@id='searchFormView']/form/div/div[2]/div/div/div/input")
    # 查询按钮
    search_button = ("xpath", "//div[@class='search-form-btn']/button[2]")
    # 确定按钮
    confirm_button = ("xpath", "//div[@class='vxe-grid--toolbar-wrapper']/div/div/button[2]")
    # 进入已开单提示
    today_have_order = ("class name", "el-message-box__message")
    # 确认
    confirm_button5 = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")

    """
        明细窗口
    """
    # 增加维修项目0B01002
    maintain_project = ("xpath", "//div[@title='0B01002']")
    # 确定按钮
    confirm_button2 = ("xpath", "//div[@id='pane-labour']/div/div[2]/div[1]/button/span")
    # 维修材料Tab页
    # 维修材料Tab
    maintain_materials = ("id", "tab-part")
    # 仓库输入框
    warehouse_input = ("xpath", "//div[@id='pane-part']/div/div[1]/div[1]/form/div/div[1]/div/div/div/div/input")
    # 配件输入框
    parts_input = ("xpath", "//div[@id='pane-part']/div/div[1]/div[1]/form/div/div[3]/div/div/div/input")
    # 查询按钮
    search_button2 = ("xpath", "//*[@id='pane-part']/div/div[1]/div[2]/button[3]/span")
    # 查询出的第一行数据
    first_data = ("xpath", "//*[@id='pane-part']/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]")
    # 确认按钮
    confirm_button3 = ("xpath", "//*[@id='pane-part']/div/form/div[2]/button[1]/span")
    # 返回按钮
    back_button = ("xpath", "//*[@id='pane-part']/div/form/div[2]/button[2]/span")


    # -----维修项目-----
    # 批量删除按钮
    project_batch_delete = ("xpath", "//*[@id='app']/div/div[4]/form/div[2]/div[1]/div[1]/button[1]/span")
    # 批量调整收费分区按钮
    project_batch_adjust = ("xpath", "//*[@id='app']/div/div[4]/form/div[2]/div[1]/div[1]/button[2]/span")
    # 勾选框（全选）
    project_checkbox = ("xpath", "//*[@id='app']/div/div[4]/form/div[2]/div[2]/div[2]/div[1]/table/thead/tr/th[1]/div[1]/span/span/span[2]")
    # 收费区分下拉框
    project_pay_divisive = ("xpath", "//*[@id='app']/div/div[4]/form/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/div/div/div/input")
    # 维修类型下拉框
    project_maintain_type = ("xpath", "//*[@id='app']/div/div[4]/form/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[5]/div/div/div/input")

    # -----维修材料------
    # 批量删除按钮
    materials_batch_delete = ("xpath", "//*[@id='app']/div/div[4]/form/div[5]/div[1]/div[1]/button[1]/span")
    # 批量调整收费分区按钮
    materials_batch_adjust = ("xpath", "//*[@id='app']/div/div[4]/form/div[5]/div[1]/div[1]/button[2]/span")
    # 勾选框（全选）
    materials_checkbox = ("xpath", "//*[@id='app']/div/div[4]/form/div[5]/div[2]/div[2]/div[1]/table/thead/tr/th[1]/div[1]/span/span/span[2]")
    # 维修区分下拉框
    materials_pay_divisive = ("xpath", "//*[@id='app']/div/div[4]/form/div[5]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/div/div/div/input")
    # 维修类型下拉框
    materials_maintain_type = ("xpath", "//*[@id='app']/div/div[4]/form/div[5]/div[2]/div[2]/div[2]/table/tbody/tr/td[5]/div/div/div/input")

    """
        批量调整收费区分窗口
    """
    # 收费区分下拉框
    charge_different_input = ("xpath", "//label[text()='收费区分']/../div/div/div/input")
    # 维修类型
    maintain_type_input = ("xpath", "/html/body/div[17]/div/div[2]/div[3]/div/form/div[2]/div/div/div/div/div/input")
    # 确定按钮
    confirm_adjust = ("xpath", "//div[@class='info']/div/div/button[1]/span[text()='确定']")

    # 保存成功提示文字
    save_success = ("xpath", "//p[@class='el-message__content']")

    # 保存后提示：提交行驶里程数一样
    road_haul = ("class name", "el-message-box__message")
    # 提示中的确定按钮
    confirm_button4 = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")

    # 保存后提示：填写保险到期日期的相关信息
    insurance_data = ("xpath", "//div[@class='el-message-box__message']/p")
    # 提示中的确定按钮
    confirm_button8 = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")

    # 提示：请填写机动车损失保险相关信息
    loss_insurance = ("xpath", "//div[@class='el-message-box__message']/p")
    # 提示：确定
    confirm_loss = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")

    # 提示：事故维修车相关维修类型未指定保险公司，是否继续保存？
    no_insurance_company = ("xpath", "//div[@class='el-message-box__message']/p")
    # 提示：确定
    confirm_company = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")

    # 提示：该客户超过6个月未做保养，请及时提醒！
    maintain_timeout = ("xpath", "//div[@class='el-message-box__message']/p")
    # 提示：确定
    confirm_maintain = ("xpath", "//div[@class='el-message-box__btns']/button/span")

    # 提示：车辆行驶里程低于上次行驶里程，需售后总监审核，是否提交售后总监审核？
    travel_mile = ("xpath", "//div[@class='el-message-box__message']/p")
    # 提示：取消
    cancle_travel = ("xpath", "//div[@class='el-message-box__btns']/button[1]/span")

    # 提示保存成功，工单信息是否同步至DMS?
    order_sync_DMS = ("xpath", "//div[@class='el-message-box__message']/p")
    # 确认按钮
    confirm_button9 = ("xpath", "//div[@class='el-message-box__btns']/button[2]/span")
    # 取消按钮
    cancle_button = ("xpath", "//div[@class='el-message-box__btns']/button[1]/span")

    """
        新增保险窗口
    """
    # 险种名称下拉框
    insurance_type_name = ("xpath", "//label[@for='insuranceTypeCode']/../div/div/div/input")
    # 保险公司下拉框
    insurance_company = ("xpath", "//label[@for='insurationCode' and text()='保险公司']/../div/div/div/input")
    # 保险开始时间
    insurance_start_data = ("xpath", "//label[@for='insuranceBeginDate']/../div/div/input")
    # 车损保额
    loss_money = ("xpath", "//label[@for='coverageAmount']/../div/div/div/input")
    # 确认按钮
    confirm_button7 = ("xpath", "//span[text()='确认']")

    """
        厂家维修类型窗口
    """
    # 厂家维修类型下拉框
    maintian_type_input = ("xpath", "//label[@for='factoryRepairType']/../div/div/div/input")
    # 保存按钮
    save_button2 = ("xpath", "//span[text()='保存']")

    """
        分项派工窗口
    """
    # 派工技师下拉框
    technician_input = ("xpath", "//label[@for='technician']/../div/div/div/input")
    assignLabourHour_input = ("xpath", "//label[@for='assignLabourHour']/../div/div/input")
    confirm_button6 = ("xpath", "//span[text()='确认']")

    # 打印界面：服务委托书
    service_attorney_book = ("xpath", "//*[@id='repair_order_standard']/div[3]/table/tr/td[2]/h2[2]")

    # 确定提交结算消息框：确定按钮
    confirm_commit = ("xpath", "//div[@class='el-message-box__btns']/button[2]")

    # 校验为员工车提示
    staff_car_success = ("xpath", "//p[@class='el-message__content']")

    # 工单提交结算成功提示语
    commit_order_success = ("xpath", "//p[@class='el-message__content']")

    # 提示解锁出清材料成功
    unlock_clear_success = ("xpath", "//p[@class='el-message__content']")

    """
        商品车维修申请窗口
    """
    # 销售部申报人输入框
    sale_declare_people = ("xpath", "//label[@for='signer']/../div/div/input")
    # 备注
    remark_input = ("xpath", "//label[@for='remark']/../div/div/textarea")
    # 申请按钮
    apply_button = ("xpath", "//span[text()='申请']")
    # 商品维修申请提示消息：确定按钮
    confirm_apply = ("xpath", "//div[@class='el-message-box__btns']/button[2]")
    # 申请成功提示
    apply_success = ("xpath", "//p[@class='el-message__content']")

    """
        右边优惠套餐栏
    """
    # 优惠券按钮
    discount_coupon_button = ("xpath", "//span[contains(text(), '优惠券')]")
    # 购买套餐按钮
    buy_set_meal = ("xpath", "//div[@class='operationButton']/div/div[5]/div/button")

    """
        购买套餐窗口
    """
    # 财务申请按钮
    finance_apply_button = ("xpath", "//span[text()='财务申请']")
    # 套餐类别
    set_meal_type = ("xpath", "//label[@for='mainTypeCode']/../div/div/div/input")
    # 二级类别
    second_level_type = ("xpath", "//label[@for='subTypeCode']/../div/div/div/input")
    # 项目代码搜索框
    project_code_select = ("xpath", "//label[@for='labourCode']/../div/div/span/span/button/i")
    # 销售人下拉框
    sale_people = ("xpath", "//label[@for='employeeNo']/../div/div/div/input")
    # 右上角关闭按钮
    close_button = ("xpath", "//span[text()='购买套餐']/../button/i")

    """
        选择保养套餐窗口
    """
    # 小保养
    little_maintain = ("xpath", "//li[contains(text(), '小保养')]")
    # 序号为1的套餐
    number_one = ("xpath", "//*[@class='vxe-body--row']")
    # 确定按钮
    confirm_set_meal = ("xpath", "//div[@class='vxe-grid--toolbar-wrapper']/div/div/button[1]/span")

    # 提示消息：申请成功，是否打印合同？
    apply_finance_success = ("xpath", "//div[@class='el-message-box__message']/p")
    # 取消按钮
    cancle_print = ("xpath", "//div[@class='el-message-box__btns']/button[1]")

    """
        查看优惠券窗口
    """
    # 未使用优惠券中序号1的优惠券
    discount_number_one = ("xpath", "//table[@class='vxe-table--body']/tbody/tr[1]/td[2]/div[text()='A保']")
    # 返回按钮
    back_discount_coupon = ("xpath", "//span[text()='返回']")


    # 新增接车制单，前置操作：跳转到新增接车制单页面
    def addAustomerReception(self, license, servicepeople, insurancetype, insurancecompany, project, isMaterial=False,
                             partsnumber='', vin='', maintaintype='', lossmoney=0):
        self.click(self.license_select_button)
        # 进入选择车主车辆窗口，选择车牌号
        self.input(self.license_input, license, True)
        if vin != '':
            self.input(self.vin_input, vin)
        self.click(self.search_button)
        self.clickByText(license)
        self.click(self.confirm_button)
        self.wait(3)

        try:
            text1 = self.webDriverWait(self.today_have_order).text
            if "此车今日已开单" in text1:
                self.click(self.confirm_button5)
        except:
            pass

        # 选择服务专员
        self.select(self.service_people_input, servicepeople)
        # 保修到期日期，此刻
        self.click(self.after_service_data, 0.5)
        elements = self.driver.find_elements("xpath", "//span[contains(text(), '此刻')]")
        for element in elements:
            if element.text == '此刻':
                element.click()
        self.wait(1)

        # 添加维修明细
        self.click(self.add_maintain_detail)
        self.click(self.maintain_project)
        self.click(self.confirm_button2)

        self.click(self.maintain_materials)
        self.wait(2)
        if isMaterial:
            # 选择维修材料
            self.input(self.parts_input, partsnumber)
            self.click(self.search_button2)
            self.click(self.first_data)
            # 确定返回
            self.click(self.confirm_button3)
            self.click(self.back_button)
            # 设置维修材料项目收费区分
            self.select(self.materials_pay_divisive, project)
            if maintaintype != '':
                self.select(self.materials_maintain_type, maintaintype)
        else:
            # 关闭窗口
            self.click(self.back_button)

        # 设置维修项目收费区分
        self.select(self.project_pay_divisive, project)
        if maintaintype != '':
            self.select(self.project_maintain_type, maintaintype)

        # 保存
        self.click(self.save_button, 0.5)

        try:
            text2 = self.webDriverWait(self.insurance_data).text
            if "请填写保险到期日期的相关信息" in text2:
                self.click(self.confirm_button8)

                # 新增保险页操作
                self.select(self.insurance_type_name, insurancetype)
                self.select(self.insurance_company, insurancecompany)
                # 选择日期，此刻
                self.click(self.insurance_start_data, 0.5)
                elements = self.driver.find_elements("xpath", "//span[contains(text(), '此刻')]")
                for element in elements:
                    if element.text == '此刻':
                        element.click()

                self.click(self.confirm_button7)
                self.wait(3)

                # 再次保存
                self.click(self.save_button, 0.5)
        except:
            pass

        try:
            text3 = self.getText(self.loss_insurance)
            if "请填写机动车损失保险相关信息" in text3:
                self.click(self.confirm_loss)

                self.select(self.insurance_company, insurancecompany)
                # 选择日期，此刻
                self.click(self.insurance_start_data, 0.5)
                elements = self.driver.find_elements("xpath", "//span[contains(text(), '此刻')]")
                for element in elements:
                    if element.text == '此刻':
                        element.click()

                self.input(self.loss_money, lossmoney)
                self.click(self.confirm_button7)
                self.wait(1)
                # 再次保存
                self.click(self.save_button, 0.5)
        except:
            pass

        try:
            text = self.getText(self.road_haul)
            if "本次行驶里程数和上次行驶里程数一样" in text:
                self.click(self.confirm_button4)
        except:
            pass

        try:
            text4 = self.webDriverWait(self.no_insurance_company).text
            if "事故维修车相关维修类型未指定保险公司" in text4:
                self.click(self.confirm_company)
        except:
            pass

        try:
            text5 = self.webDriverWait(self.maintain_timeout).text
            if "该客户超过6个月未做保养，请及时提醒" in text5:
                self.click(self.confirm_maintain)
        except:
            pass

        # try:
        #     text = self.webDriverWait(self.order_sync_DMS).text
        #     if "保存成功！工单信息是否同步至DMS?" in text:
        #         self.click(self.confirm_button9)
        #
        #     # 厂家维修类型
        #     self.select(self.maintian_type_input, maintiantype)
        #     self.click(self.save_button2)
        # except:
        #     pass

        self.wait(3)

    # 取消同步到DMS
    def cancleSyscDMS(self):
        text = self.webDriverWait(self.order_sync_DMS).text
        if "工单信息是否同步至DMS" in text:
            self.click(self.cancle_button)

    # 派工，前置条件：新增接车制单保存成功
    def dispatching(self, technician, hour):
        self.click(self.project_checkbox)
        self.click(self.dispatching_button)
        self.wait(1)

        # 分项派工
        self.input(self.technician_input, technician, wait=0.5)
        self.click("//ul/li[2]/span[text()='刘峰']")

        self.input(self.assignLabourHour_input, hour, True)
        self.click(self.confirm_button6)
        self.wait(2)

    # 编辑接车制单
    def editAustomerReception(self, factoryentrust, traveldistance):
        self.input(self.factory_entrust_number, factoryentrust)
        self.input(self.travel_distance, traveldistance, True)
        self.click(self.save_button)

        # try:
        #     text1 = self.webDriverWait(self.travel_mile).text
        #     if "车辆行驶里程低于上次行驶里程" in text1:
        #         self.click(self.cancle_travel)
        #         # 再次保存
        #         self.click(self.save_button)
        # except:
        #     pass
        #
        # try:
        #     text2 = self.webDriverWait(self.road_haul).text
        #     if "本次行驶里程数和上次行驶里程数一样" in text2:
        #         self.click(self.confirm_button4)
        # except:
        #     pass

        self.wait(3)

    # 打印工单，前置条件：进入到接车制单新增页面
    def printOrder(self):
        self.click(self.print_order_button)

    # 保存并提交结算，前置条件：进入编辑接车制单页面
    def saveAndCommit(self):
        self.click(self.save_button)
        try:
            text = self.webDriverWait(self.road_haul).text
            if "本次行驶里程数和上次行驶里程数一样" in text:
                self.click(self.confirm_button4)
                self.wait(3)
        except:
            pass
        self.cancleSyscDMS()

        self.click(self.commit_account_button)
        self.click(self.confirm_commit)
        self.wait(3)

    # 员工车校验
    def checkStaffCar(self, license):
        # 选择员工车
        self.click(self.license_select_button)
        # 进入选择车主车辆窗口，选择车牌号
        self.input(self.license_input, license, True)
        self.click(self.search_button)
        self.clickByText(license)
        self.click(self.confirm_button)
        self.wait(3)

        # 点击员工车校验
        self.click(self.check_staff_car)
        self.wait(1)

    # 提交结算，前置条件：接车制单的编辑界面
    def commitPay(self):
        self.click(self.commit_account_button)
        self.click(self.confirm_commit)
        self.wait(3)

    # 商品车维修申请，前置条件：接车制单新增页已保存商品车信息
    def applyForMaintain(self, saledeclarepeople, remark):
        self.click(self.apply_maintain_button)
        self.input(self.sale_declare_people, saledeclarepeople)
        self.input(self.remark_input, remark)
        self.click(self.apply_button)
        self.click(self.confirm_apply)
        self.wait(1)

    # 新增接车制单：添加多条维修项目和维修材料，前置条件：跳转到接车制单新增页面
    def addManyAustomerReception(self, license, servicepeople, partsnumber=''):
        self.click(self.license_select_button)
        # 进入选择车主车辆窗口，选择车牌号
        self.input(self.license_input, license, True)
        self.click(self.search_button)
        self.clickByText(license)
        self.click(self.confirm_button)
        self.wait(3)

        # 选择服务专员
        self.select(self.service_people_input, servicepeople)
        # 保修到期日期，此刻
        self.click(self.after_service_data)
        elements = self.driver.find_elements("xpath", "//span[contains(text(), '此刻')]")
        for element in elements:
            if element.text == '此刻':
                element.click()
        self.wait(1)

        # 添加维修明细
        self.click(self.add_maintain_detail)
        self.click(self.maintain_project)
        # 添加2条维修项目
        self.click(self.confirm_button2)
        self.click(self.confirm_button2)

        self.click(self.maintain_materials)
        # 选择维修材料
        self.click(self.first_data)
        self.click(self.confirm_button3)
        # 添加第2条维修材料
        self.input(self.parts_input, partsnumber)
        self.click(self.search_button2)
        self.click(self.first_data)
        self.click(self.confirm_button3)

        self.click(self.back_button)

    # 进行批量删除和批量调整收费分区操作，前置条件：已添加多条维修项目和维修材料
    def batchAdjustCharge(self, chargedifferent):
        # 维修项目批量调整
        self.click(self.project_checkbox)
        self.click(self.project_batch_adjust)
        self.select(self.charge_different_input, chargedifferent)
        self.click(self.confirm_adjust)
        # 维修项目批量删除
        self.click(self.project_batch_delete)
        self.wait(1)

        # 维修材料批量调整
        self.click(self.materials_checkbox)
        self.click(self.materials_batch_adjust)
        self.select(self.charge_different_input, chargedifferent)
        self.click(self.confirm_adjust)
        # 维修材料批量删除
        self.click(self.materials_batch_delete)

    # 购买套餐，前置条件：进入新增接车制单界面
    def buySetMeal(self, license, setmeal, secondlevel, salepeople):
        self.click(self.license_select_button)
        # 进入选择车主车辆窗口，选择车牌号
        self.input(self.license_input, license, True)
        self.click(self.search_button)
        self.clickByText(license)
        self.click(self.confirm_button)
        self.wait(3)

        # 页面右边购买套餐
        self.click(self.buy_set_meal)
        self.wait(3)
        # 购买套餐窗口
        self.select(self.set_meal_type, setmeal)
        self.select(self.second_level_type, secondlevel)
        self.click(self.project_code_select)
        self.wait(3)
        # 选择保养套餐
        self.click(self.number_one)
        self.click(self.confirm_set_meal)

        self.select(self.sale_people, salepeople)
        self.click(self.finance_apply_button)
        self.wait(1)

    # 通过添加优惠券，新增接车制单，前置条件：已进入新增接车制单
    def addOrderByDiscountCoupon(self, license, servicepeople, chargedifferent, warehouse, partsnumber, insurancetype, insurancecompany):
        self.click(self.license_select_button)
        # 进入选择车主车辆窗口，选择车牌号
        self.input(self.license_input, license, True)
        self.wait(1)
        self.click(self.search_button)
        self.clickByText(license)
        self.click(self.confirm_button)
        self.wait(3)

        try:
            text1 = self.webDriverWait(self.today_have_order).text
            if "此车今日已开单" in text1:
                self.click(self.confirm_button5)
        except:
            pass

        # 选择服务专员
        self.select(self.service_people_input, servicepeople)

        # 点击右边的优惠券按钮
        self.click(self.discount_coupon_button)
        self.wait(2)
        self.click(self.little_maintain)
        self.doubleClick(self.discount_number_one)
        self.wait(1)
        self.click(self.back_discount_coupon)

        # 添加维修明细
        self.click(self.add_maintain_detail)
        self.click(self.maintain_project)
        self.click(self.confirm_button2)
        self.click(self.maintain_materials)
        # 选择维修材料
        self.select(self.warehouse_input, warehouse)
        self.input(self.parts_input, partsnumber)
        self.click(self.search_button2)
        self.click(self.first_data)
        # 确定返回
        self.click(self.confirm_button3)
        self.click(self.back_button)

        # 维修项目批量调整
        self.click(self.project_checkbox)
        self.click(self.project_batch_adjust)
        self.select(self.charge_different_input, chargedifferent)
        self.click(self.confirm_adjust)

        # 维修材料批量调整
        self.click(self.materials_checkbox)
        self.click(self.materials_batch_adjust)
        self.select(self.charge_different_input, chargedifferent)
        self.click(self.confirm_adjust)

        # 保存
        self.click(self.save_button)

        try:
            text2 = self.webDriverWait(self.insurance_data).text
            if "请填写保险到期日期的相关信息" in text2:
                self.click(self.confirm_button8)

                # 新增保险页操作
                self.select(self.insurance_type_name, insurancetype)
                self.select(self.insurance_company, insurancecompany)
                # 选择日期，此刻
                self.click(self.insurance_start_data)
                elements = self.driver.find_elements("xpath", "//span[contains(text(), '此刻')]")
                for element in elements:
                    if element.text == '此刻':
                        element.click()

                self.click(self.confirm_button7)
                self.wait(3)

                # 再次保存
                self.click(self.save_button)
        except:
            pass

        try:
            text = self.webDriverWait(self.road_haul).text
            if "本次行驶里程数和上次行驶里程数一样" in text:
                self.click(self.confirm_button4)
        except:
            pass

        self.wait(3)
