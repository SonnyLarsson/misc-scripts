@ECHO off
set "UNREAL_PROJECT_PATH=C:\Users\[user]\OneDrive\Documents\Gitlab\[project folder]\[project].uproject"
:start
cls
ECHO choose unreal version
ECHO.
ECHO 1. v4.26
ECHO 2. v4.27
ECHO 3. Built from source
set choice=
set /p choice=Enter the number of your selection: 
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto v4.26
if '%choice%'=='2' goto v4.27
if '%choice%'=='3' goto LOCAL
ECHO "%choice%" is not valid, try again
ECHO.
goto start
:v4.26
set "UNREAL_BUILDTOOL_PATH=C:\Program Files\Epic Games\UE_4.26\Engine\Binaries\DotNET\UnrealBuildTool.exe"
goto end
:LOCAL
set "UNREAL_BUILDTOOL_PATH=C:\GitHub\UnrealEngine\Engine\Binaries\DotNET\UnrealBuildTool.exe"
goto end
:v4.27
set "UNREAL_BUILDTOOL_PATH=C:\Program Files\Epic Games\UE_4.27\Engine\Binaries\DotNET\UnrealBuildTool.exe"
goto end
:end
call generate_unreal_files_vscode.bat