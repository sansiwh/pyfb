import datetime

#根据字符串获取下一天
def str_date_add_one_day(date):
    d = datetime.datetime.strptime(date, '%Y-%m-%d')
    delta = datetime.timedelta(days=1)
    n_days = d + delta
    return n_days.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(str_date_add_one_day('2017-11-30'))