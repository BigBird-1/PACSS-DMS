# -*- coding:utf-8 -*
# @FileName:   员工电子档案编辑页.py
# @Author:     刘峰
# @CreateTime: 2022/8/22 9:07

from base.base_page import BasePage

class PsnArchivesEditPage(BasePage):

    新增文件按钮 = "//button/span[text()='新增文件']"

    劳动合同集团 = "//span[text()='劳动合同（集团）']"
    劳动合同公司 = "//span[text()='劳动合同（公司）']"
    保密协议 = "//span[text()='保密协议']"
    安全生产经营承诺书2019 = "//span[text()='安全生产经营承诺书（2019）']"
    集团文件学习确认书 = "//span[text()='集团文件学习确认书']"
    新员工入职培训记录 = "//span[text()='新员工入职培训记录']"
    办公计算机使用承诺书 = "//span[text()='办公计算机使用承诺书']"

    """
        上传文件窗口
    """
    选择文件按钮 = "//span[text()='选择文件']/../../input"
    上传文件确定按钮 = "//div[contains(text(), '上传文件')]/../../div[2]/div/button[1]"

    # 在人员档案中上传相关文件，前置条件：跳转到员工电子档案编辑页
    def uploadFiles(self, file_path1, file_path2, file_path3, file_path4, file_path5, file_path6, file_path7):
        # 上传劳动合同（集团）
        self.click(self.劳动合同集团, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path1, wait=1.5)
        self.click(self.上传文件确定按钮, 1)
        # 上传劳动合同（公司）
        self.click(self.劳动合同公司, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path2, wait=1)
        self.click(self.上传文件确定按钮, 1)
        # 上传保密协议
        self.click(self.保密协议, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path3, wait=1)
        self.click(self.上传文件确定按钮, 1)
        # 上传安全生产经营承诺书（2019）
        self.click(self.安全生产经营承诺书2019, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path4, wait=1)
        self.click(self.上传文件确定按钮, 1)
        # 上传集团文件学习确认书
        self.click(self.集团文件学习确认书, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path5, wait=1)
        self.click(self.上传文件确定按钮, 1)
        # 上传新员工入职培训记录
        self.click(self.新员工入职培训记录, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path6, wait=1)
        self.click(self.上传文件确定按钮, 1)
        # 上传办公计算机使用承诺书
        self.click(self.办公计算机使用承诺书, 1)
        self.click(self.新增文件按钮)
        self.input(self.选择文件按钮, file_path7, wait=1)
        self.click(self.上传文件确定按钮, 1)
