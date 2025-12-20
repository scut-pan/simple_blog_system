import sqlite3
from datetime import datetime, timezone
from .models import Post


class Database:
    """数据库操作类，实现数据库的增删改查操作"""

    def __init__(self, db_path):
        """构造函数，初始化数据库连接"""
        # 获取数据库文件路径
        self.db_path = db_path
        # 创建数据库连接，允许在多线程中使用
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        # 创建游标对象
        self.cursor = self.conn.cursor()

    
    def create_table(self):
        """创建文章表"""
        sql = """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.cursor.execute(sql)
        # 增删改操作必须 commit 才能保存到数据库
        self.conn.commit()
    
    
    def create_post(self, title, content):
        """创建新文章(加入错误处理)"""
        try:
            # 使用 UTC 时间创建时间戳
            utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            sql = """
            INSERT INTO posts (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(sql, (title, content, utc_now, utc_now))
            self.conn.commit()
            # 获取插入数据的 ID
            last_id = self.cursor.lastrowid
            # 返回新创建文章的 ID
            return last_id
        except sqlite3.Error as e:
            print(f"数据库错误: {e}")
            # 回滚事务
            self.conn.rollback()
            return None
    

    def get_all_posts(self):
        """获取所有文章"""
        # 按创建时间倒序排序
        sql = """
        SELECT * FROM posts ORDER BY created_at DESC
        """
        self.cursor.execute(sql)
        # 获取所有结果，返回列表
        results = self.cursor.fetchall()
        # 转换为 Post 对象列表
        posts = []
        for row in results:
            post = Post(
                id=row[0],
                title=row[1],
                content=row[2],
                # 将字符串转换为带 UTC 时区的 datetime 对象
                created_at=datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
                updated_at=datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
            )
            posts.append(post)
        return posts
    
    
    def get_post_by_id(self, post_id):
        """根据ID获取文章"""
        sql = """
        SELECT * FROM posts WHERE id=?
        """
        self.cursor.execute(sql, (post_id,))
        # 获取一条结果，返回元组或 None
        result = self.cursor.fetchone()
        # 转换为 Post 对象
        if result:
            post = Post(
                id=result[0],
                title=result[1],
                content=result[2],
                # 将字符串转换为带 UTC 时区的 datetime 对象
                created_at=datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc),
                updated_at=datetime.strptime(result[4], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
            )
        else:
            post = None
        return post
    
    
    def update_post(self, post_id, title, content):
        """更新文章"""
        # 使用 UTC 时间更新时间戳
        utc_now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        sql = """
        UPDATE posts SET title=?, content=?, updated_at=? WHERE id=?
        """
        self.cursor.execute(sql, (title, content, utc_now, post_id))
        self.conn.commit()
        # 获取受影响的行数
        affected_rows = self.cursor.rowcount
        return affected_rows
        
    
    def delete_post(self, post_id):
        """删除文章"""
        sql = """
        DELETE FROM posts WHERE id=?
        """
        self.cursor.execute(sql, (post_id,))
        self.conn.commit()
        # 获取受影响的行数
        affected_rows = self.cursor.rowcount
        return affected_rows
    
    
    def close(self):
        """关闭数据库连接"""
        # 关闭游标（可选）
        self.cursor.close()
        # 关闭连接（必须）
        self.conn.close()
    
    
    
    