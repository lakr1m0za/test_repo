Import-Module activedirectory
get-adgroupmember "name1" | select name | Export-csv -path c:\temp\name1-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name2" | select name | Export-csv -path c:\temp\name2-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name3" | select Name | Export-csv -path c:\temp\name3-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name4" | select Name | Export-csv -path c:\temp\name4-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name5" | select Name | Export-csv -path c:\temp\name5-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name6" | select Name | Export-csv -path c:\temp\name6-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name7" | select Name | Export-csv -path c:\temp\name7-2019.csv -Append -Encoding UTF8 -NoTypeInformation
get-adgroupmember "name8" | select Name | Export-csv -path c:\temp\name8-2019.csv -Append -Encoding UTF8 -NoTypeInformation
