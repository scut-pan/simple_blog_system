# Simple Blog System

一个基于 Flask 的轻量级博客系统，支持 Markdown 渲染和简洁的用户界面。

## 功能特性

- 📝 **文章管理**: 创建、编辑、删除和查看博客文章
- 🎨 **Markdown 支持**: 完整支持 Markdown 语法，包括代码高亮、表格等
- 🕒 **时区转换**: 自动将 UTC 时间转换为本地时间显示
- 💾 **SQLite 存储**: 使用轻量级 SQLite 数据库存储数据
- 📱 **响应式设计**: 适配各种设备屏幕尺寸
- 🚀 **轻量级**: 简洁高效，遵循 Python 设计哲学

## 技术栈

- **后端框架**: Flask 3.1.2+
- **数据库**: SQLite
- **Markdown 渲染**: Python-Markdown 3.10+
- **Python 版本**: 3.13+
- **包管理器**: uv

## 安装和运行

### 前置要求

- Python 3.13 或更高版本
- uv (Python 包管理器)

### 安装步骤

1. 克隆项目到本地：
   ```bash
   git clone <repository-url>
   cd simple_blog_system
   ```

2. 使用 uv 安装依赖：
   ```bash
   uv sync
   ```

3. 运行应用：
   ```bash
   uv run python main.py
   ```

4. 打开浏览器访问：
   ```
   http://127.0.0.1:5000
   ```

## 项目结构

```
simple_blog_system/
├── main.py                 # 应用入口点
├── pyproject.toml         # 项目配置和依赖
├── blog.db                # SQLite 数据库文件
├── src/                   # 源代码目录
│   ├── __init__.py
│   ├── app.py             # Flask 应用主程序
│   ├── database.py        # 数据库操作类
│   ├── models.py          # 数据模型定义
│   └── templates/         # HTML 模板文件
│       ├── base.html      # 基础模板
│       ├── index.html     # 首页模板
│       ├── post.html      # 文章详情模板
│       ├── create.html    # 创建文章模板
│       └── edit.html      # 编辑文章模板
├── docs/                  # 文档目录
├── .venv/                 # 虚拟环境
└── README.md              # 项目说明文档
```

## 使用说明

### 创建文章

1. 访问首页，点击 "新建文章" 按钮
2. 输入文章标题和内容（支持 Markdown 语法）
3. 点击 "发布" 按钮保存文章

### 编辑文章

1. 在文章详情页点击 "编辑" 按钮
2. 修改文章内容
3. 点击 "更新" 按钮保存修改

### Markdown 支持

本系统支持以下 Markdown 语法：

- **代码块**: 使用三个反引号包围代码
- **表格**: 使用标准 Markdown 表格语法
- **列表**: 支持有序和无序列表
- **链接和图片**: 标准 Markdown 语法
- **换行**: 自动将换行转换为 `<br>` 标签

## 开发说明

### 数据库

- 使用 SQLite 作为数据库
- 数据库文件自动创建在项目根目录 (`blog.db`)
- 首次运行时会自动创建必要的表结构

### 代码风格

项目严格遵循 Python 设计哲学（The Zen of Python）：
- 保持代码简洁明了
- 优先选择简单直接的实现方式
- 注重可读性和维护性

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 更新日志

### v0.1.0
- 初始版本发布
- 基础的博客文章功能
- Markdown 渲染支持
- 时区转换功能
- 响应式界面设计
