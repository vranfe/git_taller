@echo off
chcp 65001 > nul
title Sistema de Gestion de Inventario

REM Detectar comando java y javac
set "JAVAC_CMD=javac"
set "JAVA_CMD=java"

where javac >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if defined JAVA_HOME (
        set "JAVAC_CMD=%JAVA_HOME%\bin\javac.exe"
        set "JAVA_CMD=%JAVA_HOME%\bin\java.exe"
    ) else if exist "C:\Users\CIRA412\.p2\pool\plugins\org.eclipse.justj.openjdk.hotspot.jre.full.win32.x86_64_21.0.8.v20250724-1412\jre\bin\javac.exe" (
        set "JAVAC_CMD=C:\Users\CIRA412\.p2\pool\plugins\org.eclipse.justj.openjdk.hotspot.jre.full.win32.x86_64_21.0.8.v20250724-1412\jre\bin\javac.exe"
        set "JAVA_CMD=C:\Users\CIRA412\.p2\pool\plugins\org.eclipse.justj.openjdk.hotspot.jre.full.win32.x86_64_21.0.8.v20250724-1412\jre\bin\java.exe"
    )
)

echo ==========================================================
echo   SISTEMA DE GESTION DE INVENTARIO - PERSISTENCIA JDBC
echo ==========================================================

echo Compilando clases...
"%JAVAC_CMD%" -encoding UTF-8 -cp "lib/*" *.java

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] No se pudo compilar el proyecto. Verifique que Java JDK este instalado.
    pause
    exit /b %ERRORLEVEL%
)

echo Iniciando Menu Principal...
"%JAVA_CMD%" -cp ".;lib/*" MenuPrincipal
pause
