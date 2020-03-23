#. ../venv3_2/bin/activate
#. ../venv_pure/bin/activate
echo 'rabbitmq-server start'
nohup /usr/local/sbin/rabbitmq-server&
sleep 1

#nohup python quant/example/binance_triangle/main.py  ./quant/example/binance_triangle/config.json >> triangle  &
echo 'okex binance price difference'
nohup python quant/example/okex_binance_compare/main.py  quant/example/okex_binance_compare/config.json >> okex_binance_compare.log &
#nohup python quant/example/mongo_saver/main.py quant/example/mongo_saver/config.json>>kline_mongo.log&

#. ../venv3_2/bin/activate
sleep 1
nohup python Market/src/main.py Market/config_orderbooks.json>>Market/market.log&
#nohup python Market/src/main.py Market/config.json>>Market/kline.log&
#nohup ./bin/mongod --dbpath=./db2&
#nohup ../../database/mongodb-macos-x86_64-4.2.4/bin/mongod --dbpath= ../../database/mongodb-macos-x86_64-4.2.4/db2/&
