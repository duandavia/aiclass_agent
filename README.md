# 大作业计划

## 使用方法（10.30update）

CLI启动：直接运行`CLI_main.py`，参照测试用例（e.g.：搜索港股昨天市值最高的科技类股票的名称，并进行分析）的语句输入指令开始运行。

前端启动：

*注意事项：`yfinance`库需要使用魔法上网访问，且不包含A股数据，搜索时建议聚焦港股美股进行分析*

## 基本环境配置
*参考文档：https://microsoft.github.io/autogen/stable/index.html*

虚拟环境基准：python 3.12

需求库：（pip install安装） 

`autogen-agentchat`

`autogen-ext`

`yfinance`

`matplotlib`

`pytz`

`numpy`

`pandas`

`python-dotenv`

`requests`

`bs4`

## 大作业完成计划
多智能体任务：搜索指定范围内的股票价格，作折线图，并对搜索到的结果发表评论，最后把所有内容进行整合输出。

*参考文档：https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/examples/company-research.html*

具体开发建议：

前端和数据接口：前端主要关注AI输出的`result`变量的显示和用户输入的`task`变量的显示；数据接口同学只关注这两个变量即可，其中`task`传到后端，`result`发到前端。

任务解析智能体：创建一个agent，开发一个配套的搜索函数作为tool封装，提示词参考：`f"使用所提供的tool检索信息，告诉我符合用户所描述的特征的股票名称，不需要其他信息和文字。"`

搜索智能体：创建一个agent，开发一个配套的搜索函数作为tool封装，提示词参考：`f"根据已知的股票名称，使用所提供的tool检索信息，告诉我这只股票在用户指令中指定的市场里的完整检索代码，不需要其他信息和文字。"`
*搜索函数需要麻烦各位自己解决搜索api及密钥*

制图智能体：创建一个agent，参考（可照抄）文档内容，开发一个配套的数据查询和制图函数，作为tool封装，提示词参考：`"进行数据分析。"`

评论智能体：创建一个agent，描述（description），提示词（system_message）可参考（照抄）文档中report_agent的描述。

输出智能体：创建一个agent，开发一个配套的输出函数作为tool封装，把制图智能体出的图和评论智能体输出的分析内容输出到文件中。

测试脚本和测试人员：注意我们使用的`yfinance`库不支持国内股市，如果可以的话建议编写测试指令时聚焦港股、美股等国外市场的股票。

智能体配置：任务解析智能体、搜索智能体、制图智能体、评论智能体、整合输出智能体

结构：round-robin-team，按照上述顺序

模型：deepseek-r1，api用needed_api中给的api-key

检索：麻烦负责检索开发的同学自己解决检索api和密钥了（x）

相应的api和密钥建议放到`needed_api.env`中。

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
PPT：制作各自负责的部分，其中前端设计者需要同时负责领域综述。
展示共10分钟，每人做1-2页就可以了

Word写作分配同上
