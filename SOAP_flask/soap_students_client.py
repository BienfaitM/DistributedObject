from suds.client import Client
from suds.cache import NoCache

client = Client('http://127.0.0.1:5000/soap/someservice?wsdl', cache=None)
print (client)
print ('Student details:\n', my_client.service.student_details(99271))