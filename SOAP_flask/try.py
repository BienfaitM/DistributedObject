from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from spyne.service import ServiceBase
from spyne.service import *
from spyne.decorator import rpc


app = Flask(__name__)
# spyne = Spyne(app)

# class SomeSoapService(spyne.Service):
class SomeSoapService(ServiceBase):
    __service_url_path__ = '/soap/someservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    # @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    # def echo(str, cnt):
    #     for i in range(cnt):
    #         yield str
    @rpc(Integer(Unicode, Integer,_returns=Iterable(Unicode)))
    def echo(str,cnt):
        for i in range(cnt):
            yield str


if __name__ == '__main__':
    app.run(host = '127.0.0.1')