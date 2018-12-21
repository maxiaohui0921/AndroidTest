#-*-coding:utf-8-*-
#__author__='maxiaohui'
import logging  # 引入logging模块

def showLog(level,message):  #把所有log打印显示在屏幕上
    logging.basicConfig(level=logging.ERROR,format='%(asctime)s %(filename)s[line:%(lineno)d]  %(levelname)s:%(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
    # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
    if level=="info":    logging.info(message)
    if level == "debug":    logging.debug(message)
    if level == "warning":    logging.warning(message)
    if level == "error":    logging.error(message)
    if level == "critical":    logging.critical(message)

if __name__ == "__main__":  #当前脚本运行实例
    showLog("info","设备连接是断开的，请重新连接")