from dataclasses import dataclass
from datetime import datetime

@dataclass
# 博客文章类
class Post:
    id: int                 # 文章ID（自增主键）
    title: str              # 文章标题（不能为空）
    content: str            # 文章内容
    created_at: datetime    # 创建时间（时间戳）
    updated_at: datetime    # 更新时间（时间戳）