# Symlink Examples

## Common Symlink Patterns

### 1. Version Management
```
config/
├── v1.0.0/
│   └── config.json
├── v2.0.0/
│   └── config.json
├── current -> v1.0.0/     # Current active version
└── latest -> v2.0.0/      # Latest available version
```

### 2. Build Artifacts
```
build/
├── 2024-01-15-10-30-45/
│   └── build.log
├── 2024-01-16-14-20-30/
│   └── build.log
└── latest -> 2024-01-16-14-20-30/  # Latest build
```

### 3. Release Management
```
dist/
├── release-1.2.3/
│   └── app.exe
├── release-1.2.4/
│   └── app.exe
└── current -> release-1.2.4/  # Current release
```

### 4. Development Tools
```
bin/
├── python -> /usr/bin/python3
├── node -> /usr/local/bin/node
└── git -> /usr/bin/git
```

### 5. Library Dependencies
```
lib/
├── libssl.so.1.1
├── libssl.so -> libssl.so.1.1
└── libssl.so.1 -> libssl.so.1.1
```

## Node.js npm Symlinks
```
node_modules/
├── .bin/
│   ├── eslint -> ../eslint/bin/eslint.js
│   └── prettier -> ../prettier/bin/prettier.js
├── eslint/
│   └── bin/
│       └── eslint.js
└── prettier/
    └── bin/
        └── prettier.js
```

## Python Virtual Environment
```
venv/
├── bin/
│   ├── python -> python3.9
│   ├── pip -> pip3
│   └── activate -> ../scripts/activate
└── scripts/
    └── activate
```
