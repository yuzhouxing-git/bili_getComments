# bili_getComments

一个轻量级的 Python 脚本，用于爬取 Bilibili 视频的评论数据，并保存为 CSV 文件。  
基于 `requests`、`re`、`csv`、`time` 和 `random` 库实现，以 MIT 协议开源。  
**仅限个人学习研究，严禁用于任何商业目的。**

## 功能特点

- 通过视频 BV 号获取一级评论（不含二级评论）
- 自动处理分页，支持大量评论抓取
- 随机延时，降低封禁风险
- 输出结构化 CSV 文件，包含：
  - 评论者昵称
  - 评论内容
  - 发布时间
  - 点赞数
- 代码简洁，易于修改和扩展

## 依赖环境

- Python 3.6+
- 以下 Python 库（可通过 pip 安装）：

```bash
pip install requests
```

> 注：`re`、`csv`、`time`、`random` 为 Python 内置库，无需额外安装。

## 快速开始

1. 克隆或下载本仓库。
2. 打开终端，进入脚本所在目录。
3. 修改 config.py 中的 `bvid`、`maxPage`、`cookies` 变量。
4. 运行脚本：

```bash
python main.py
```

5. 等待抓取完成，会在当前目录生成 `comments.csv` 文件。

## 使用说明

### 配置参数（在脚本顶部可调整）

| 参数名 | 说明 | 默认值 |
|--------|------|--------|
| `bvid` | 目标视频的 BV 号 | 需手动填写 |
| `maxPage` | 最大读取页数 | 10 |
| `cookies` | 请求头 Cookies | 需手动填写 |

（具体实现可参考 config.py 内的注释）

### 输出文件

- `comments.csv`：UTF-8 编码，Excel 可直接打开。

## 常见问题

**Q：提示 `requests` 未找到？**  
A：请执行 `pip install requests` 安装。

**Q：爬取过程中报错 `JSONDecodeError`？**  
A：可能是 B站接口返回了非 JSON 内容（如验证码页面），请检查延时是否过短，或尝试更换代理 IP。

**Q：如何获取视频的 BV 号？**  
A：在 B站视频页面的 URL 中，如 `https://www.bilibili.com/video/BVXXXXXXXXXX`，其中 `BVXXXXXXXXXX` 即为 BV 号。

**Q：能否爬取评论区中的图片或表情？**  
A：本脚本仅提取文本内容，如需图片链接可自行扩展解析逻辑。

## 注意事项

- B站 API 存在访问频率限制，请勿设置过短的延时，否则可能被临时封禁 IP。
- 本脚本仅用于合法合规的数据分析、个人学习等非商业用途。
- 请尊重用户隐私，不得将爬取数据用于恶意或侵犯他人权益的行为。
- 若 B站接口发生变化，需相应调整 `re` 正则或 URL 构造逻辑。

## 许可证

本项目采用 [MIT](https://opensource.org/licenses/MIT) 协议。  
你可以自由使用、修改、分发，但需保留原始版权声明。
```text
MIT License

Copyright (c) 2026 youzhouxing-git

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

如有建议或问题，欢迎提交 Issue 或 Pull Request。
