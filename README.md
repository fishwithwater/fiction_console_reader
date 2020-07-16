# Fiction Console Reader
## 简介
笔趣阁小说命令行阅读器
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
    "line_limit": 10
}
``` 
`fiction_index`为开始章节下标,`line_limit`为每页行数,`fiction_url`为小说目录页路径
4. 运行
`python app.py`
## 计划
- [x] 小说分页
- [x] 阅读器首页
- [ ] 目录查询、跳转
- [ ] 动态修改配置
- [ ] 一键伪装模式
