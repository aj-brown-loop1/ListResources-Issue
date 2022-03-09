$hostname = '192.168.25.30'
$user = 'aj_api'
$pswd = 'SolGod369!!!'
$swis = Connect-Swis -Hostname $hostname -UserName $user -Password $pswd 

Get-SwisData $swis -Query 'SELECT TOP 1 NodeID, Caption FROM Orion.Nodes'
#Invoke-SwisVerb 'Orion.Nodes' 'GetScheduledListResourcesStatus' 

Invoke-SwisVerb $swis Orion.Nodes PollNow @("N:" + $VolNodeID)