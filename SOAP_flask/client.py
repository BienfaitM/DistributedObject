# from suds.client import Client as SudsClient

# url = 'http://127.0.0.1:5000/soap/someservice?wsdl'
# client = SudsClient(url=url, cache=None)
# r = client.service.echo(str='hello world', cnt=3)
# print r
from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:5000/someservice/?WSDL', cache=NoCache())
r = client.service.echo(str='hello world', cnt=3)
print(r)
# print 'Student details:\n', my_client.service.student_details(101907)