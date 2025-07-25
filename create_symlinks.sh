#!/bin/bash

# Script to create symbolic links for testing

echo "Creating symbolic links..."

# Create directories
mkdir -p config/v1.0.0 config/v2.0.0
mkdir -p build/2024-01-15-10-30-45 build/2024-01-16-14-20-30
mkdir -p dist/release-1.2.3 dist/release-1.2.4
mkdir -p bin lib src/shared

# Create some dummy files
echo "v1.0.0 config" > config/v1.0.0/config.json
echo "v2.0.0 config" > config/v2.0.0/config.json
echo "build output" > build/2024-01-15-10-30-45/build.log
echo "build output" > build/2024-01-16-14-20-30/build.log
echo "release files" > dist/release-1.2.3/app.exe
echo "release files" > dist/release-1.2.4/app.exe

# Create symlinks
ln -sf config/v1.0.0 config/current
ln -sf config/v2.0.0 config/latest
ln -sf build/2024-01-16-14-20-30 build/latest
ln -sf dist/release-1.2.4 dist/current

echo "Symlinks created successfully!"
echo "Current symlinks:"
ls -la config/current config/latest build/latest dist/current
