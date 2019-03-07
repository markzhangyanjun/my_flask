from flask import Flask
from werkzeug.routing import BaseConverter

class Config(object):
    DEBUG = True


# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]

app = Flask(__name__)

app.config.from_object(Config)
app.url_map.converters['re'] = RegexConverter

@app.route("/")
def index():
    return "hello world"



if __name__ == '__main__':
    app.run()