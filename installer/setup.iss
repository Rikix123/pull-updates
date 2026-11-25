[Setup]
AppId=PullBrowser.Windows.x64
AppName=Pull Browser
AppVersion=7.0.0
AppPublisher=Pull Browser
DefaultDirName={localappdata}\Programs\Pull Browser
DefaultGroupName=Pull Browser
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\Pull.WebView2.exe
WizardStyle=modern
Compression=lzma2/fast
SolidCompression=yes
OutputDir=dist
OutputBaseFilename=Pull-Browser-Setup-7.0.0
SetupIconFile=payload\pull.ico
CloseApplications=yes
RestartApplications=no
VersionInfoVersion=7.0.0.0

[Files]
Source: "payload\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Pull Browser"; Filename: "{app}\Pull.WebView2.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\Pull.WebView2.exe"; Description: "Open Pull Browser"; WorkingDir: "{app}"; Flags: nowait postinstall skipifsilent
