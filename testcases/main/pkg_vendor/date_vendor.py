import random


class DataVendor(object):
    """
    登录测试数据
    """
    def __init__(self):
        pass

    # 供应商列表url
    url = "http://10.228.81.198:8080/"
    # 选择企业/非企业
    company = 0
    # 登录账户
    username = '金严虎测试'
    # 密码
    password = 'a1234567'
    # 供应商编码
    vendor_code = '12375'
    # 供应商简称
    vendor_short_code = '测试供应商12375'
    # 选择供应商状态:1启用，0禁用
    state = 1
    # 供应商列表地址
    vendor_url = 'http://10.228.81.198:8080/supplierManagement/supplierList'
    # 供应商录入页面url
    vendor_url1 = 'http://10.228.81.198:8080/supplierManagement/addSupplier'
    # 录入页面，供应商编码
    code = 12375
    # 录入页面，供应商名称
    name = '测试供应商12375'
    # 录入页面，供应商简称
    short_name = '测试供应商12375'
    # 录入页面，所属分类选择
    sort = 1
    # 录入页面，联系人1
    linkman = '测试'
    # 录入页面，手机1
    telephone = '17610225668'
    # 录入页面，地址1
    address = '测试地址'
