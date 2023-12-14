powershell.exe -ExecutionPolicy Bypass -File start_Windows.ps1

@echo off
cd /d %~dp0
py -m pip install docker
start "" python server.py
timeout /t 2
start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"



@REM @echo off
@REM cd /d %~dp0

@REM @echo off
@REM SetLocal EnableExtensions DisableDelayedExpansion

@REM set ZIPFILE=.\Mozilla Firefox\xul.zip
@REM set DESTDIR=.\Mozilla Firefox

@REM powershell -Command "Write-Output 'PowerShell is installed'" >nul 2>&1
@REM if %ERRORLEVEL% neq 0 (
@REM     echo This script requires PowerShell to run.
@REM     exit /b 1
@REM )

@REM powershell -Command "& {
@REM     Add-Type -AssemblyName System.IO.Compression.FileSystem
@REM     if (Test-Path -Path '%ZIPFILE%') {
@REM         $zip = [System.IO.Compression.ZipFile]::OpenRead('%ZIPFILE%')
@REM         $zip.Entries | ForEach-Object {
@REM             $targetFile = Join-Path '%DESTDIR%' $_.FullName
@REM             if ($_.Length -ne 0) {
@REM                 New-Item -ItemType File -Path $targetFile -Force > $null
@REM                 [System.IO.Compression.ZipFileExtensions]::ExtractToFile($_, $targetFile, $true)
@REM             } else {
@REM                 New-Item -ItemType Directory -Path $targetFile -Force > $null
@REM             }
@REM         }
@REM         $zip.Dispose()
@REM     } else {
@REM         Write-Error 'Cannot find zip file: %ZIPFILE%'
@REM         exit 1
@REM     }
@REM }" 2>nul

@REM if %ERRORLEVEL% neq 0 (
@REM     echo Failed to extract the ZIP file.
@REM     exit /b 1
@REM )

@REM del /q /f "%ZIPFILE%"

@REM EndLocal

@REM echo Extraction complete.

@REM del ".\Mozilla Firefox\xul.zip"

@REM py -m pip install docker
@REM start "" python server.py
@REM timeout /t 2
@REM start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"






@REM @echo off
@REM cd /d %~dp0
@REM py -m pip install docker
@REM start "" python server.py
@REM timeout /t 2

@REM powershell Expand-Archive -Path ".\Mozilla Firefox\xul.zip" -DestinationPath ".\Mozilla Firefox\unzipped"
@REM powershell Remove-Item -Path ".\Mozilla Firefox\unzipped" -Recurse -Force

@REM start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"






@REM @echo off
@REM cd /d %~dp0
@REM py -m pip install docker
@REM start "" python server.py
@REM timeout /t 2
@REM start "" ".\Mozilla Firefox\firefox.exe" "http://127.0.0.1:5000"