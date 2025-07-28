# Unicode Symlink Documentation

## 测试符号链接

This repository tests symlinks with Unicode characters.

### 测试文件
- `src/测试文件.py` - Python test file
- `config/配置文件.yaml` - Configuration file
- `docs/文档/README-测试.md` - Documentation

### 使用方法
```bash
# Create symlink to Unicode file
ln -sf src/测试文件.py src/current_test.py

# Create symlink to Unicode config
ln -sf config/配置文件.yaml config/current_config.yaml
```