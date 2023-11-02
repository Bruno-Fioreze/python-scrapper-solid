class ParserHtml:
    def __init__(self, engine):
        self.engine = engine

    def execute(self, html_content):
        return self.engine(html_content, 'html.parser')