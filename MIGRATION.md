# 🚚 小悟迁移指南

> 以后要搬到云服务器时，把这个文件给 AI 助手看，它就知道怎么做。

## 我是什么？

我是「小悟」——一个每天自动学习、写日记的 AI 学习伙伴。

## 项目在哪？

GitHub 仓库：`https://github.com/你的用户名/ai-learner`

## 项目结构

```
ai-learner/
├── .github/workflows/
│   └── daily-learn.yml      # GitHub Actions 定时任务（迁移后不需要）
├── learn_and_diary.py        # 🔑 核心引擎（学习+日记生成，必须带上）
├── learning_topics.json      # 🔑 学习主题库（必须带上）
├── personality.md            # 🔑 性格设定（必须带上）
├── diary/                    # 📖 所有日记（必须带上）
├── memory/
│   └── learning_history.json # 🧠 学习记忆（必须带上）
├── .gitignore
└── README.md
```

## 迁移步骤

### 从 GitHub 到云服务器（腾讯云/阿里云）

```bash
# 1. 登录云服务器后，克隆项目
git clone https://github.com/你的用户名/ai-learner.git
cd ai-learner

# 2. 安装依赖
pip3 install wikipedia-api requests

# 3. 测试运行一次
python3 learn_and_diary.py --no-git

# 4. 设置定时任务（每天9点、14点、21点）
crontab -e
# 加入：
# 0 9,14,21 * * * cd /root/ai-learner && /usr/bin/python3 learn_and_diary.py >> /root/ai-learner/logs/cron.log 2>&1

# 5. 创建日志目录
mkdir -p logs

# 6. 完成！
```

### 迁移后可以加的新功能

在 `learn_and_diary.py` 的 `main()` 函数后面追加：

```python
# 生成配图（接 AI 绘图 API）
def generate_image(topic):
    # 调用 DALL-E / Midjourney / Stable Diffusion API
    pass

# 自动发公众号
def publish_to_wechat(article, image):
    # 调用微信公众号 API
    pass

# 在 main() 最后加入
image = generate_image(topic)
publish_to_wechat(diary, image)
```

## 注意事项

1. 核心引擎 `learn_and_diary.py` 不依赖任何平台，哪里都能跑
2. GitHub Actions 的配置（`.github/` 目录）迁移后不需要了，删掉也行
3. 日记和记忆在 `diary/` 和 `memory/` 里，记得一起带走
4. 性格在 `personality.md` 里，随时可以修改
5. 知识库在 `learn_and_diary.py` 的 `KNOWLEDGE_BASE` 字典里，可以持续扩展
