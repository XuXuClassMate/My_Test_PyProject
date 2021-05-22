from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义数据库基本配置
host = "stuq.ceshiren.com"
user = "hogwarts_python"
password = "hogwarts_python"
db = "hogwarts_python"
charset = "utf8mb4"

# 定义数据库基本对象
Base = declarative_base()


class User(Base):
    __tablename__ = 'seveniruby_user'  # 对应的表
    id = Column(Integer, primary_key=True)  # primary_key 是否主键
    username = Column(String)  # 对应字段的字段类型
    password = Column(String)
    email = Column(String)


def test_orm():
    engine = create_engine(
        # 数据库的连接方式 ：用户名+密码+端口
        f'mysql+pymysql://{user}:{password}@{host}/db'.format(
            host=host, db=db, user=user, password=password
        ), echo=True
    )
    # 绑定数据库，建立连接
    Session = sessionmaker(bind=engine)
    # 创建一个session的具体实例，以供后面调用
    session = Session()

    # 数据的插入操作
    u1 = User(
        username="seveniruby",
        password="password",
        email="seveniruby@ceshiren.com"
    )
    # 数据插入
    session.add(u1)
    # 递交到数据库
    session.commit()

    # 查询User对象 条件是user_name="seveniruby"的第一条数据
    u2 = session.query(User).filter_by(user_name="seveniruby").first()
    print(u2.username)
    assert u2.username == u1.username

