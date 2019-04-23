import tornado.ioloop
import tornado.web
from application.routes import routing_table


def make_app():
    return tornado.web.Application(routing_table)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
