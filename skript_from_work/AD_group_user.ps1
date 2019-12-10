Import-Module activedirectory
get-adgroupmember "UAKHAA05RDP" | select name | Export-csv -path c:\temp\UAKHAA05RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAA17RDP" | select name | Export-csv -path c:\temp\UAKHAA17RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAT01RDP" | select Name | Export-csv -path c:\temp\UAKHAT01RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAT02RDP" | select Name | Export-csv -path c:\temp\UAKHAT02RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAD98RDP" | select Name | Export-csv -path c:\temp\UAKHAD98RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAD99RDP" | select Name | Export-csv -path c:\temp\UAKHAD99RDP-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAT01RDPSession" | select Name | Export-csv -path c:\temp\UAKHAT01RDPSession-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "UAKHAT02RDPSe" | select Name | Export-csv -path c:\temp\UAKHAT02RDPSe-2019.csv -Append -Encoding UTF8 -NoTypeInformation