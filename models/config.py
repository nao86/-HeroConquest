class SystemConfig:
  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'root',
      'host': 'localhost',
      'db_name': 'ヒロコンクエストデータベース'
  })

Config = SystemConfig