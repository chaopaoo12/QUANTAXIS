#coding ：utf-8

"""
QUANTAXIS

Quantitative Financial Strategy Framework

by yutiansut

2017/4/5
"""
# 获取函数

from QUANTAXIS.QAFetch import (QA_fetch_get_stock_day,QA_fetch_get_trade_date,
                                QA_fetch_get_stock_indicator)
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_data

from QUANTAXIS.QASpider import (QA_spider_select_spider,QA_spider_start_spider,
                                QA_spider_end_spider)

# 任务中心
from QUANTAXIS.QATasks import (tasks,control)

# 存储函数
from QUANTAXIS.QASU.save_wind import ( QA_SU_save_stock_list, QA_SU_save_stock_day,
                                    QA_SU_save_stock_day_init, QA_SU_save_stock_day_init_simple, QA_SU_save_trade_date)

# 事件驱动
from QUANTAXIS.QASignal import (QA_signal_resend, QA_signal_send, QA_Signal_eventManager,
                                QA_Signal_events, QA_Signal_Sender, QA_Signal_Listener,QA_signal_usual_model)
# 市场函数

from QUANTAXIS.QAMarket import (QABid,QAMarket_core)

# 账户，组合，风控函数
from QUANTAXIS.QAARP import (QAAccount,QAPortfolio,QARisk)
from QUANTAXIS.QAARP.QAAccount import QA_Account
# 策略函数                                
from QUANTAXIS.QAStrategy.start_strategy import (QA_Strategy)
from QUANTAXIS.QAStrategy.strategy_signal import QA_Strategy_signal


#from QUANTAXIS.QAStrategy import (start_strategy,import_strategy,analysis_strategy,c)

# 工具函数
from QUANTAXIS.QAUtil import (QA_util_sql_mongo_setting,QA_util_cfg_initial,
                                QA_util_date_stamp, QA_util_time_stamp, QA_util_ms_stamp,
                                QA_util_log_debug, QA_util_log_expection, QA_util_log_info,
                                QA_start_initial,QA_Setting)
# 命令行与脚手架函数
import QUANTAXIS.QACmd
QA_util_log_info('Welcome to QUANTAXIS, the Version is 0.3.8-beta')

def QA_start_first_run(self):
    QA_SU_save_stock_day_init_simple()
    QA_util_log_info('first_run_quantaxis')
    pass
def QA_close(self):
    pass
def QA_help_fetch(self):
    QA_util_log_info('QA_fetch_get_stock_day,QA_fetch_get_trade_date,QA_fetch_get_stock_indicator')
def QA_help_su(self):
    QA_util_log_info('QA_SU_save_stock_list, QA_SU_save_stock_day,QA_SU_save_stock_day_init, QA_SU_save_trade_date')