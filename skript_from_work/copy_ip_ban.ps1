$Date = (Get-Date -F yyyy-MM-dd_HH-mm)
$namefile = "$Date.txt"
#Rename-Item -Path "C:\temp\ip_ban\somefile.txt" -NewName "$namefile"
$Source = "\\uakhat01\c$\Admins\ip_ban.txt"
$Dest = "C:\temp\ip_ban\$namefile"
$Username = "adm2prokhorenk"
$Password = "Razr2B0tk2"
$WebClient = New-Object System.Net.WebClient
$WebClient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)
$WebClient.DownloadFile($Source, $Dest)

#$WebClient.UploadFile($Dest, $Source)
