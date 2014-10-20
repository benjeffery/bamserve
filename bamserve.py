from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession
import arraybuffer
import numpy as np


class Component(ApplicationSession):
    """
   An application component providing procedures with different kinds of arguments.
   """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")

        def ping():
            return

        def add2(a, b):
            return a + b

        def stars(nick="somebody", stars=0):
            return u"{} starred {}x".format(nick, stars)

        def orders(product, limit=5):
            return [u"Product {}".format(i) for i in range(50)][:limit]

        def arglen(*args, **kwargs):
            return [len(args), len(kwargs)]

        def benny(length):
            return ''.join(arraybuffer.encode_array_set([
                ('test', np.random.randint(0,255,length)),
            ]))

        yield self.register(ping, u'com.arguments.ping')
        yield self.register(add2, u'com.arguments.add2')
        yield self.register(stars, u'com.arguments.stars')
        yield self.register(orders, u'com.arguments.orders')
        yield self.register(arglen, u'com.arguments.arglen')
        yield self.register(benny, u'com.arguments.benny')
        print("procedures registered")


if __name__ == '__main__':
    from autobahn.twisted.wamp import ApplicationRunner

    runner = ApplicationRunner("ws://127.0.0.1:8080/ws", "realm1")
    runner.run(Component)