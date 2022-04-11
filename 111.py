import xlrd


def func(fn):
    def wrapper(*args, **kwargs):
        print(1111)
        return fn(*args, **kwargs)
    return wrapper


@func  # test = func(test)
def test(num):
    print(num)


def log_with_param(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)


# sstr = "HD420600,HD420684,HD340500,HD420620,HD130100,HD450130,HD420630,HD340400,HX340126,HX360110,HX360111,HX340113,HD130300,HX410112,HX420135,HX430109,HD450150,HX650101,HD360120,HD420040,HX340128,HD340310,HD420590,HX360109,HD340320,HX450116,HX340204,HD420210,HD420350,HD420190,HX340202,HD521700,HX522206,HD620210,HD620280,HX522208,HD410120,HD420640,HD420370,HD420687,HD420686,HD420170,HD420110,HD610200,HD640100,HD640200,HD340500,HD410140,HX360114,HD610103,HD410150,HX421216,HX421302,HX340129,HD450160,HA420101,HA420134,HM420102,HM420145,HX520204,HX520419,HX522207,HX522305,HX522606,HX522709,HX420141,HX420145,HX420134,HD420020,HD420010,HD420146,HD340130,HX340801,HD340700,HD420695,HD420696,HD420697,HD420698,HD430140,HX425001,HD450115,HX410109,HX420123,HX430106,HD340610,HD425900,HD430120,HD340200,HD420030,HD420580,HD420148,HX360113,HD450140,HD130400,HX650101,HX410110,HX420140,HX430107,HD340340,HX340119,HD440100,HD420000,HD420610,HD420699,HD430100,HD360100,HD450100,HD610400,HX330401,HX420129,HD360140,HD340100,HD130200,HD130500,HD410200,HD420080,HD420650,HD360110,HX450111,HD420060,HD420560,HD360130,HX450113,HD520200,HD521400,HD610500,HD620140,HD521300,HD520600,HD410180,HD420470,HD420450,HD420694,HD420682,HD521200,HD520900,HD521800,HD520500,HD521900,HD420270,HD420460,HD420430,HD420230,HD420660,HD420410,HD420530,HD420683,HD410130,HD340800,HD420070,HD450120,HX450201,HX411308,HX420614,HX420514,HD640120"
# sstr = "HX421216,HX421302,HX340129,HD450160,HD430120,HD340200,HD420600,HD420684,HD340500,HD420620,HD130100,HD450130,HD420630,HD340400,HX340126,HX360110,HX650101,HD340100,HD340300,HD340330,HD340310,HD340320,HD340340,HD340610,HX340113,HX340119,HD340800,HX340128,HD440100,HD130200,HD130300,HD130500,HD410200,HX410109,HX410110,HX410112,HD420000,HD420030,HD420040,HD420060,HD420080,HD420070,HD420590,HD425900,HD420560,HD420610,HD420580,HD420650,HX420123,HD420699,HX420135,HX420140,HD420148,HA420101,HM420102,HA420134,HM420145,HF420145,HD430100,HX430106,HX430107,HX430109,HD360100,HD360110,HD360140,HD360120,HD360130,HX360109,HX360111,HX360113,HD450100,HD450110,HD450120,HD450140,HD450150,HX450111,HX450113,HD610400,HX330401,HX520204,HX520419,HX522207,HX522305,HX522606,HX522709,HX420141,HX420145,HX420134,HD420020,HD420010,HD420146,HD340130,HX450116,HX420129,HX340204,HD420210,HD420350,HD420190,HX340202,HD521700,HX522206,HX450201,HX411308,HX420614,HX420514,HX340801,HD340700,HD420695,HD420696,HD420697,HD420698,HD430140,HX425001,HD520200,HD521400,HD610500,HD620210,HD620280,HX522208,HD410120,HD420640,HD420370,HD420687,HD420686,HD420170,HD420110,HD610200,HD640100,HD640120,HD410140,HX360114,HD610103,HD640200,HD450115,HD620140,HD521300,HD520600,HD410180,HD420470,HD420450,HD420694,HD420682,HD521200,HD520900,HD521800,HD520500,HD521900,HD420270,HD420460,HD420430,HD420230,HD420660,HD420410,HD420530,HD420683,HD410150,HD130400,HD410130"
# ll = sstr.split(",")
#
# print(ll)
# print(len(ll))

# sstr1 = "HX340129,HD450160,HX421302,HX421216,HX650101,HD430120,HD340200,HD420600,HD420684,HX340126,HX360110,HD340500,HD420620,HD130100,HD450130,HD420630,HD340400,HD340100,HD340300,HD340330,HD340310,HD340320,HD340340,HD340610,HX340113,HX340119,HD340800,HX340128,HD440100,HD130200,HD130300,HD130500,HD410200,HX410109,HX410110,HX410112,HD420000,HD420030,HD420040,HD420060,HD420080,HD420070,HD420590,HD425900,HD420560,HD420610,HD420580,HD420650,HX420123,HD420699,HX420135,HX420140,HD420148,HA420101,HM420102,HA420134,HM420145,HF420145,HD430100,HX430106,HX430107,HX430109,HD360100,HD360110,HD360140,HD360120,HD360130,HX360109,HX360111,HX360113,HD450100,HD450110,HD450120,HD450140,HD450150,HX450111,HX450113,HD610400,HX330401,HX520204,HX520419,HX522207,HX522305,HX522606,HX522709,HX420141,HX420145,HX420134,HD420020,HD420010,HD420146,HX420129,HX450116,HD340130,HX340204,HD420210,HD420350,HD420190,HX340202,HD521700,HX522206,HX450201,HX411308,HX420614,HX420514,HX340801,HD340700,HD420695,HD420696,HD420697,HD420698,HD430140,HX425001,HD520200,HD521400,HD610500,HD620210,HD620280,HX522208,HD410120,HD420640,HD420370,HD420687,HD420686,HD420170,HD420110,HD610200,HD640100,HD640120,HD410140,HX360114,HD610103,HD640200,HD450115,HD620140,HD521300,HD520600,HD410180,HD420470,HD420450,HD420694,HD420682,HD521200,HD520900,HD521800,HD520500,HD521900,HD420270,HD420460,HD420430,HD420230,HD420660,HD420410,HD420530,HD420683,HD410150,HD130400,HD410130"
# sstr1 = "HX421216,HX421302,HX340129,HD450160,HD430120,HD340200,HD420600,HD420684,HD340500,HD420620,HD130100,HD450130,HD420630,HD340400,HX340126,HX360110,HX650101,HD340100,HD340300,HD340330,HD340310,HD340320,HD340340,HD340610,HX340113,HX340119,HD340800,HX340128,HD440100,HD130200,HD130300,HD130500,HD410200,HX410109,HX410110,HX410112,HD420000,HD420030,HD420040,HD420060,HD420080,HD420070,HD420590,HD425900,HD420560,HD420610,HD420580,HD420650,HX420123,HD420699,HX420135,HX420140,HD420148,HA420101,HM420102,HA420134,HM420145,HF420145,HD430100,HX430106,HX430107,HX430109,HD360100,HD360110,HD360140,HD360120,HD360130,HX360109,HX360111,HX360113,HD450100,HD450110,HD450120,HD450140,HD450150,HX450111,HX450113,HD610400,HX330401,HX520204,HX520419,HX522207,HX522305,HX522606,HX522709,HX420141,HX420145,HX420134,HD420020,HD420010,HD420146,HD340130,HX450116,HX420129,HX340204,HD420210,HD420350,HD420190,HX340202,HD521700,HX522206,HX450201,HX411308,HX420614,HX420514,HX340801,HD340700,HD420695,HD420696,HD420697,HD420698,HD430140,HX425001,HD520200,HD521400,HD610500,HD620210,HD620280,HX522208,HD410120,HD420640,HD420370,HD420687,HD420686,HD420170,HD420110,HD610200,HD640100,HD640120,HD410140,HX360114,HD610103,HD640200,HD450115,HD620140,HD521300,HD520600,HD410180,HD420470,HD420450,HD420694,HD420682,HD521200,HD520900,HD521800,HD520500,HD521900,HD420270,HD420460,HD420430,HD420230,HD420660,HD420410,HD420530,HD420683,HD410150,HD130400,HD410130"
# ll1 = sstr1.split(",")

# print(ll1)
# print(len(ll1))
#
# for i in ll1:
#     if i not in ll:
#         print(i)
#
# aa = []
# for i in ll:
#     if i not in aa:
#         aa.append(i)
#     else:
#         print(i)


# work_book = xlrd.open_workbook(r"C:\Users\cpr264\Downloads\解除限价管控门店-0312.xlsx")
# #
# sheet1 = work_book.sheet_by_name("3月12日")
# cols = sheet1.col_values(1)[1::]
# print(cols)
# print(len(cols))
# #
#
# aa = ','.join(cols)
#
# print(aa)

# for i in cols:
#     if i not in ll:
#         print(i)

a = 200.345

print("%.2f" % a)
print(type(round(a, 2)))
print(format(a,'.2f'))

from decimal import Decimal

print(Decimal(a).quantize(Decimal("0.00")))