# LabPBR to MERS Converter
[中文] | [[EN]](README.md)  

将 LabPBR 材质格式转换为 MERS 格式的命令行工具。

## 功能

- 支持 LabPBR 到 MERS 格式的像素级转换
- 支持 PNG/TGA 输出格式
- 自动创建输出目录
- 批量处理支持（通过脚本调用）

## 构建

```bash
#安装依赖
pip install Pillow PyInstaller
#构建
python -m PyInstaller --onefile --name Lab2MERS --icon Lab2MERS.ico Lab2MERS.py
#构建结果在dist中
