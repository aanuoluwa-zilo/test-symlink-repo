@echo off

REM Script to create symbolic links on Windows

echo Creating symbolic links...

REM Create directories
mkdir config\v1.0.0 config\v2.0.0
mkdir build\2024-01-15-10-30-45 build\2024-01-16-14-20-30
mkdir dist\release-1.2.3 dist\release-1.2.4
mkdir bin lib src\shared

REM Create some dummy files
echo v1.0.0 config > config\v1.0.0\config.json
echo v2.0.0 config > config\v2.0.0\config.json
echo build output > build\2024-01-15-10-30-45\build.log
echo build output > build\2024-01-16-14-20-30\build.log
echo release files > dist\release-1.2.3\app.exe
echo release files > dist\release-1.2.4\app.exe

REM Create symlinks (requires admin privileges)
mklink config\current config\v1.0.0
mklink config\latest config\v2.0.0
mklink build\latest build\2024-01-16-14-20-30
mklink dist\current dist\release-1.2.4

echo Symlinks created successfully!
echo Current symlinks:
dir config\current config\latest build\latest dist\current
