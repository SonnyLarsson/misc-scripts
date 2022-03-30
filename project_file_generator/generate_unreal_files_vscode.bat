@Echo Off
call config.bat
"%unreal_path%" -projectfiles -game -rocket -progress -engine -VSCode -TargetType=Editor -Progress -project=%project_path%
pause
