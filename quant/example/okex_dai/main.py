# -*- coding:utf-8 -*-

"""
> Dai 价格提醒:
    1. 设置一个价格区间，到达的时候通过邮件或者语音提醒
    2. **；
 """
import sys
import os

from quant import const
from quant.utils import tools
from quant.utils import logger
from quant.config import config
from quant.market import Market
from quant.order import Order
from quant.market import Orderbook
from quant.utils import sendmail

class MyStrategy:

    def __init__(self):
        """ 初始化
        """
        self.sender =sendmail.SendEmail(config.email.get("host"), config.email.get("port"), \
            config.email.get("username"), config.email.get("password"), config.email.get("to"))
        self.low = 1.013
        self.high = 1.0315
        self.low_count = 0
        self.high_count = 0

        # 订阅行情
        Market(const.MARKET_TYPE_ORDERBOOK, "okex","DAI/USDT", self.on_event_orderbook_update)

    def say(self, s):
        os.system('say '+ s)

    async def on_event_orderbook_update(self, orderbook: Orderbook):
        """ 订单薄更新
        """
        ask1_price = float(orderbook.asks[0][0])  # 卖一价格
        bid1_price = float(orderbook.bids[0][0])  # 买一价格

        if ask1_price <= bid1_price:
            logger.info('data error', orderbook)
            return
        logger.info('prices: ', ask1_price, bid1_price) 
        if ask1_price > self.high and self.high_count % 100 == 0:
            self.low_count = 0
            self.high_count = self.high_count + 1
            logger.info(self.high, self.low, self.high_count, self.low_count)
            s = "Dai 已卖出" + orderbook.asks[0][0]
            await self.sender.send_c(s)
            self.say(s)

        if bid1_price < self.low and self.low_count % 100 == 0:
            self.high_count = 0
            self.low_count = self.low_count + 1 
            logger.info(self.high, self.low, self.high_count, self.low_count)
            s = "Dai 已买入" + orderbook.bids[0][0]
            await self.sender.send_c(s)
            self.say(s)

 
def main():
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = None

    from quant.quant import quant
    quant.initialize(config_file)
    MyStrategy()
    quant.start()


if __name__ == '__main__':
    main()
