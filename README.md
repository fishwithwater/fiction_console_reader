# Fiction Console Reader
## 简介
笔趣阁小说命令行阅读器
##目前支持小说站
- http://www.xbiquge.la 编码utf-8
- https://www.guibuyu.org 编码gbk
## 快速使用
1. 下载代码
2. 安装依赖
`pip install -r requirements.txt`
3. 配置文件
```json
{
    "fiction_url": "/48/48246", 
    "fiction_index": 0, 
    "url_prefix": "http://www.xbiquge.la", 
    "line_limit": 10,
    "encoding": "utf-8"
}
``` 
`fiction_index`为开始章节下标,`line_limit`为每页行数,`fiction_url`为小说目录页路径
4. 运行
`python app.py`
## 计划
- [x] 小说分页
- [x] 阅读器首页
- [ ] 广告文字过滤
- [ ] 目录查询、跳转
- [ ] 动态修改配置
- [ ] 一键伪装模式
- [ ] 自定义快捷键
- [ ] 支持安装、发布到pypi
- [ ] 支持在线搜索小说阅读
- [ ] 支持缓存到本地阅读模式
