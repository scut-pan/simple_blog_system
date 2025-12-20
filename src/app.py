from flask import Flask, render_template,request, redirect, url_for
from .database import Database
from .models import Post
import markdown

# 创建 Flask 应用实例
app = Flask(__name__)
# 创建数据库对象，指定数据库文件路径
db = Database("blog.db")

# 初始化数据库
db.create_table()


# 定义 Markdown 渲染过滤器
@app.template_filter('markdown')
def render_markdown(text):
    """
    将 Markdown 文本转换为 HTML
    使用安全的基本配置，启用常用的 Markdown 功能
    """
    # 使用 markdown 库将文本转换为 HTML
    # 启用常用扩展：代码块、表格、换行等
    html = markdown.markdown(
        text,
        extensions=[
            'fenced_code',  # 支持围栏代码块 (```)
            'codehilite',   # 代码高亮
            'tables',       # 表格支持
            'nl2br',        # 换行转换为 <br>
            'toc',          # 目录生成
        ]
    )
    return html


@app.route("/")
def index():
    """首页，显示所有文章列表"""
    posts = db.get_all_posts()
    return render_template("index.html", posts=posts)


# 使用 <int:post_id> 接收整数类型的 URL 参数
@app.route("/post/<int:post_id>")
def view_post(post_id):
    """查看单篇文章的完整内容"""
    post = db.get_post_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return "文章未找到", 404
    

# GET 方法显示创建文章的表单，POST 方法处理表单提交
@app.route("/create", methods=["GET", "POST"])
def create_post():
    """创建新文章"""
    # 使用 request.method 判断请求类型
    if request.method == "POST":
        # 获取表单数据
        # 使用 request.form.get 方法获取表单字段，提供默认值避免 KeyError
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        
        # 验证表单数据
        if not title or not content:
            return "标题和内容不能为空", 400
        
        db.create_post(title, content)
        # 创建成功后重定向到首页
        return redirect(url_for("index"))
    return render_template("create.html")


# GET 方法显示编辑文章的表单，POST 方法处理表单提交
@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """编辑现有文章"""
    post = db.get_post_by_id(post_id)
    if not post:
        return "文章未找到", 404

    if request.method == "POST":
        # 获取表单数据
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        
        # 验证表单数据
        if not title or not content:
            return "标题和内容不能为空", 400
        
        db.update_post(post_id, title, content)
        # 更新成功后重定向到查看文章页面
        return redirect(url_for("view_post", post_id=post_id))
    
    return render_template("edit.html", post=post)
    

# 删除操作用 POST 方法处理，避免误删
@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    """删除文章"""
    db.delete_post(post_id)
    # 删除成功后重定向到首页
    return redirect(url_for("index"))


def run():
    """启动 Flask 应用"""
    app.run(
        # 开启调试模式，便于开发时自动重载和显示调试信息
        debug=True,
        host="0.0.0.0",
        port=5000
    )


if __name__ == "__main__":
    run()