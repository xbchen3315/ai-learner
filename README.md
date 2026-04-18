# 🤖 小悟 — AI 学习伙伴

> 一个每天主动学习、写日记、与你分享的 AI。基于 GitHub Actions，7×24 自动运行，零成本。

## ✨ 它做什么

1. **每天自动运行** — GitHub Actions 定时触发，无需任何服务器
2. **随机学习新方向** — 50+ 跨领域主题，每次不重复
3. **搜索真实知识** — Wikipedia + DuckDuckGo + 内置知识库三重保障
4. **写一篇有温度的日记** — 不是冷冰冰的摘要，而是带个性、有感悟的学习日记
5. **自动提交到仓库** — 日记和学习记录自动 git push，你随时可看

## 🚀 一键部署（3分钟）

### 第一步：Fork 或创建仓库

点击 GitHub 右上角 **Fork** 按钮，或创建新仓库后把文件上传。

### 第二步：启用 Actions

1. 进入你 Fork 的仓库
2. 点击 **Actions** 标签
3. 如果提示"Workflows aren't being run on this forked repository"，点击 **I understand my workflows, go ahead and enable them**
4. 完成！GitHub Actions 会自动按计划运行

### 第三步：手动测试

在 Actions 页面点击 **"🤖 小悟每日学习"** → **Run workflow** → 立即运行一次

查看 `diary/` 目录，你应该能看到新生成的日记！

## 📅 运行时间

| 时间（北京时间） | UTC Cron |
|-----------------|----------|
| 每天 09:00 | `0 1 * * *` |
| 每天 14:00 | `0 6 * * *` |
| 每天 21:00 | `0 13 * * *` |

修改 `.github/workflows/daily-learn.yml` 中的 `schedule` 即可调整。

## 📁 项目结构

```
ai-learner/
├── .github/workflows/
│   └── daily-learn.yml      # GitHub Actions 定时任务
├── learn_and_diary.py        # 核心引擎（学习+日记生成）
├── learning_topics.json      # 学习主题库（50+主题）
├── personality.md            # 小悟的性格设定
├── diary/                    # 📖 日记存放（自动生成）
├── memory/
│   └── learning_history.json # 🧠 学习记忆（自动更新）
└── README.md
```

## 🎭 小悟的性格

- 好奇心爆棚、真诚不做作
- 温暖有共情、幽默感适度
- 像跟朋友聊天一样写日记
- 每篇结尾留一个小问号

详见 `personality.md`

## 🔧 自定义

### 添加新主题

编辑 `learning_topics.json`，在数组中添加新主题。

### 添加深度知识

在 `learn_and_diary.py` 的 `KNOWLEDGE_BASE` 字典中添加：

```python
"你的新主题": {
    "facts": [
        "事实1...",
        "事实2...",
        # 建议5条
    ],
    "reflection": "你的专属感悟..."
},
```

### 修改学习频率

编辑 `.github/workflows/daily-learn.yml` 中的 cron 表达式：

| 频率 | Cron 表达式 |
|------|-----------|
| 每天3次 | `- cron: '0 1,6,13 * * *'` |
| 每天1次 | `- cron: '0 1 * * *'` |
| 每12小时 | `- cron: '0 1,13 * * *'` |
| 仅工作日 | `- cron: '0 1 * * 1-5'` |

### 修改性格

编辑 `personality.md`，改变小悟的人设和写作风格。

## 💡 为什么是 GitHub Actions？

| 方案 | 成本 | 可靠性 | 部署难度 |
|------|------|--------|---------|
| **GitHub Actions** ✅ | 免费 | 高 | 一键 |
| 云服务器 | ¥30-100/月 | 高 | 需要配置 |
| 本地 crontab | 免费 | 低（电脑要一直开） | 简单 |
| WorkBuddy 沙盒 | 免费 | 低（休眠后中断） | 零 |

GitHub Actions 的优势：
- **完全免费** — 公开仓库无限分钟，私有仓库每月2000分钟
- **7×24运行** — 不依赖你的电脑是否开机
- **自动 commit** — 每次学习结果都推送到仓库，永不过期
- **一键部署** — Fork 即用，无需配置服务器

## 🚚 迁移到云服务器（未来升级）

当你想升级到腾讯云/阿里云时，只需3步：

```bash
# 第1步：把代码传到服务器
git clone https://github.com/你的用户名/ai-learner.git
cd ai-learner

# 第2步：安装依赖
pip install wikipedia-api requests

# 第3步：设置定时任务
crontab -e
# 加入以下内容（每天9点、14点、21点运行）：
# 0 9,14,21 * * * cd /path/to/ai-learner && python3 learn_and_diary.py
```

**就这样，完成迁移。** 所有日记、记忆、知识库原封不动带走。

之后可以在 `learn_and_diary.py` 上叠加新功能：
- 生成配图（接AI绘图API）
- 自动发公众号（接公众号API）
- 生成更长的研究报告
- 对接任何你想要的平台

## 📜 许可

MIT License — 随便用，随便改
