from distutils.log import error
import requests
import orionsdk
import urllib3
urllib3.disable_warnings()

swis = orionsdk.SwisClient('192.168.25.30', 'aj_api', 'SolGod369!!!',verify=False)
results = swis.query("SELECT TOP 3 NodeID, DisplayName FROM Orion.Nodes")
error = swis.invoke('Orion.Nodes','GetScheduledListResourcesStatus', 'DNS', 'Caption') #Nodeid doesnt work
#error = swis.invoke('Orion.Nodes','ListResources')
print(results['results'])
print(error)

#urls do not release any data
#https://192.168.25.30:17778/SolarWinds/InformationService/v3/Json/Invoke/Orion.Nodes/ImportListResources
#https://192.168.25.30:17778/SolarWinds/InformationService/v3/Json/Invoke/Orion.Nodes/ListResources
#https://192.168.25.30:17778/SolarWinds/InformationService/v3/Json/Invoke/Orion.Nodes/Resources