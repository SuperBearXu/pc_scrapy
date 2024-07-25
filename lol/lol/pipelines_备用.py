# pipelines.py
from sqlalchemy.orm import sessionmaker
from modles import Article, Tag, db_connect, create_tables


class MySQLPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_tables(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save articles and tags in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        article = Article()
        article.title = item["title"]
        article.author = item["author"]

        # Add article to the session
        session.add(article)
        session.commit()

        for tag_name in item['tags']:
            tag = Tag()
            tag.tag = tag_name
            tag.article_id = article.id
            session.add(tag)

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
