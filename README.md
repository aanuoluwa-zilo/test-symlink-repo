# Symbolic Links Repository

This repository demonstrates symbolic links and symlink structures commonly found in software projects.

## What are Symbolic Links?

Symbolic links (symlinks) are files that point to other files or directories. They act as shortcuts or references to the actual files.

## Repository Structure

This repository contains examples of common symlink patterns:

### 1. Configuration Symlinks
- `config/current` → `config/v1.0.0` (points to current config version)
- `config/latest` → `config/v2.0.0` (points to latest config version)

### 2. Build Output Symlinks
- `build/latest` → `build/2024-01-15-10-30-45` (points to latest build)
- `dist/current` → `dist/release-1.2.3` (points to current release)

### 3. Development Symlinks
- `src/shared` → `../shared-lib/src` (points to shared library)
- `node_modules/.bin/package` → `../package/bin/cli.js` (npm binary symlink)

### 4. System Symlinks
- `bin/python` → `/usr/bin/python3` (system Python symlink)
- `lib/libssl.so` → `libssl.so.1.1` (library version symlink)

## How to Create Symlinks

### On Unix/Linux/macOS:
```bash
# Create symlink to file
ln -s target_file link_name

# Create symlink to directory
ln -s target_directory link_name

# Examples:
ln -s config/v1.0.0 config/current
ln -s /usr/bin/python3 bin/python
```

### On Windows:
```cmd
# Create symlink to file
mklink link_name target_file

# Create symlink to directory
mklink /D link_name target_directory

# Examples:
mklink config\current config\v1.0.0
mklink bin\python C:\Python39\python.exe
```

## Common Use Cases

1. **Version Management**: Point to current/latest versions
2. **Build Artifacts**: Link to latest build outputs
3. **Shared Libraries**: Reference external dependencies
4. **Configuration**: Switch between config versions
5. **Development**: Link to development tools

## Testing Symlinks

Use the provided scripts to test symlink creation and validation.
