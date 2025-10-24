# 大作业计划

## 基本环境配置
*参考文档：https://microsoft.github.io/autogen/stable/index.html*
虚拟环境基准：python 3.12\\
需求库：（pip install安装） \\
autogen-agentchat \\
autogen-ext\\
yfinance\\
matplotlib\\
pytz\\
numpy\\
pandas\\
python-dotenv\\
requests\\
bs4\\

## 大作业完成计划
多智能体任务：搜索指定范围内的股票价格，作折线图，并对搜索到的结果发表评论，最后把所有内容进行整合输出。\\
*参考文档：https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/examples/company-research.html* *(基本照抄了属于是)*

智能体配置：任务解析智能体、搜索智能体、制图智能体、评论智能体、整合输出智能体

结构：round-robin-team，按照上述顺序

模型：deepseek-r1，api用main.py中给的api-key

检索：麻烦负责检索开发的同学自己解决检索api和密钥了（x

输出记录：可以考虑在前端流式输出，也可以使用logging方法输出日志

## 开发任务分配 
Main.py编写，其他代码内容整合——1人
前端设计、logging设计——1人
前后端通信——1人
智能体策略编写——各1人（共5人）
测试脚本（5组）编写和测试运行——1人
测试运行并录制demo视频、整合PPT、word、展示——1人
**编写的代码、网页、demo视频都上传到github上**

## 汇报任务分配：
PPT：制作各自负责的部分，其中前端设计者需要同时负责领域综述
10分钟，每人做1-2页就可以了

Word写作分配同上
