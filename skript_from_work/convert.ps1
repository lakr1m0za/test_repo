Get-ChildItem *.txt | % { Get-Content $_ | Out-File -Encoding UTF8 "$($_.basename)-utf8.txt" }
Remove-Item –path C:\temp\ip_ban\*.txt -exclude *-utf8.txt