This is for those of us who use vs code

Sometimes installing Unreal Engine won't give you a context-option to generate project files for VS Code, no matter what you do.
Sometimes you might want a different shortcut to generate files for a specific version, or to pick which version you want to generate files for, rather than going through the context menu.
Sometimes you might want a quick way to automate generating files for VS Code, on a server or similar.

Here's one solution for all of the above, using batch files.


===========


Scripts:

>>>config.bat - this file is used to map up your directory paths, and nothing else.
If all you need is a quick way to generate files for one specific version, you can set your paths in this file, and use generate_unreal_files_vscode.bat directly to generate files.
It should then be changed to something like:

set "unreal_path=C:\Program Files\Epic Games\UE_4.25\Engine\Binaries\DotNET\UnrealBuildTool.exe"
set "project_path=C:\Users\[user]\OneDrive\Documents\Gitlab\[project folder]\[project].uproject"

unreal_path is the location of the buildtool you want to use, in the install folder of whatever version of Unreal Engine you use.
Above, it's set to the default install folder of Unreal Engine for windows 10/11, in which case we usually want the buildtool in the DotNET folder.

project_path is the location of your .uproject-file, in the root folder of where you've put your local game files.

If you want to be able to generate project files for more than one version of Unreal Engine, you may leave config.bat untouched, and instead edit choose_unreal_version_to_generate.bat.



>>>choose_unreal_version_to_generate.bat - using this file gives you a quick and dirty way to pick between versions to generate project files for.

UNREAL_PROJECT_PATH is the location of your .uproject-file, in the root folder where you've put your local game files.

UNREAL_BUILDTOOL_PATH should be set to the Unreal Engine version you want to generate project files for.

*This file first sets UNREAL_PROJECT_PATH to your local project folder.
*Then we list which options are available to the user.
*After listing options, we prompt for input from the user.
*Input is mapped to conditional statements.
*If a condition is met, we jump to the appropriate place in the code, then we set UNREAL_BUILDTOOL_PATH, before calling generate_unreal_files_vscode.bat to generate project files.
*If no condition is met, we go back to the top, again prompting the user for input.



>>>generate_unreal_files_vscode.bat - this file does the actual work. It uses paths set in config.bat to generate project files. You generally shouldn't need to alter anything in this file.

-In case a new version of Unreal Engine suddenly expects different arguments for buildtool.exe, you may need to edit this file, though.
-If you want to use this file for automation, make sure to remove the "pause"-command at the end of the file.

"pause" is there to leave the window up so you can see the results, this is probably unnecessary in an automated context, and may even lock up your context, as it waits for user input.


===========


Usage:

Put config.bat and generate_unreal_files_vscode.bat in a folder of your choice, preferably somewhere where they won't be overwritten by someone else's changes.

If you have several versions of Unreal Engine you want to generate project files for, add choose_unreal_version_to_generate.bat to the folder.

Edit either config.bat (if only using one version of Unreal Engine) or choose_unreal_version_to_generate.bat (if using more than one version of Unreal Engine).

Manually start generation of project files by double-clicking either generate_unreal_files_vscode.bat or choose_unreal_version_to_generate.bat, as per information above.



It's possible to create a windows shortcut to either generate_unreal_files_vscode.bat or choose_unreal_version_to_generate.bat.
With an appropriately placed shortcut you may trigger project file generation from an icon on your taskbar, or in your start menu, for instance.

It is also possible to manually add a shortcut to one of the .bat-files in your context menu in windows, by using regedit.






