@echo off
chcp 65001 >nul 2>&1
title 小悟AI学习伙伴

echo ════════════════════════════════════════
echo   🤖 小悟的每日学习时间到！
echo ════════════════════════════════════════
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️ 没有检测到Python！
    echo.
    echo 请先安装Python：
    echo   1. 打开 https://www.python.org/downloads/
    echo   2. 点黄色按钮 Download Python
    echo   3. 安装时 **务必勾选 "Add Python to PATH"**
    echo   4. 安装完成后重新双击本文件
    echo.
    pause
    exit
)

REM 安装依赖
echo 🔧 正在检查依赖...
pip install wikipedia-api requests >nul 2>&1

REM 运行学习
echo.
echo 📖 小悟开始学习了...
echo.
cd /d "%~dp0"
python learn_and_diary.py

echo.
pause
