# 📊 signal-logger

Log your trading strategy signals to CSV or SQLite — easily and efficiently.

## ✅ Features
- Supports file or database logging
- Simple Python API
- Stores timestamp, symbol, signal type, strategy name, and extra info

## 🚀 Example
```python
from logger import SignalLogger
logger = SignalLogger(target="signals.db", mode="sqlite")
logger.log_signal(symbol="BTC/USDT", signal="long", strategy="ema_rsi", info="RSI=58.2")
