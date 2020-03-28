## a warning system for DAI/USDT

### 框架依赖
- 运行环境
	- python 3.5.3 或以上版本

- 依赖python三方包
	- aiohttp>=3.2.1
	- aioamqp>=0.13.0
	- motor>=2.0.0 (可选)

- RabbitMQ服务器
    - 事件发布、订阅




- 运行
```text
python main.py config.json
```

- 设置
	- 设置好两个价格，超出此区间则发出提醒