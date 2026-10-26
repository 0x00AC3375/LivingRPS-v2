# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['LivingRPS v2.0.4.py'],
    pathex=[],
    binaries=[],
    datas=[('./logo.ico', '.'), ('./7seg.ttf', '.'), ('./seguiemj.ttf', '.'), ('./Sen-Regular.otf', '.'), ('./zh-cn.ttf', '.'), ('./clap.wav', '.'), ('./hi-hat.wav', '.'), ('./kick.wav', '.'), ('./snare.wav', '.'), ('./mining.ogg', '.'), ('./destruction_bomb.ogg', '.'), ('./destruction_mixer.ogg', '.'), ('./bomb.svg', '.'), ('./box.svg', '.'), ('./box_dark.svg', '.'), ('./box_light.svg', '.'), ('./clock_dark.svg', '.'), ('./clock_light.svg', '.'), ('./cymbal.wav', '.'), ('./heart.svg', '.'), ('./heart_dark.svg', '.'), ('./heart_light.svg', '.'), ('./laptop.svg', '.'), ('./memory.svg', '.'), ('./memory_dark.svg', '.'), ('./memory_light.svg', '.'), ('./paper.svg', '.'), ('./rock.svg', '.'), ('./scissors.svg', '.'), ('./resolution_dark.svg', '.'), ('./resolution_light.svg', '.'), ('./systemclock.svg', '.'), ('./timer.svg', '.'), ('./cpu_dark.svg', '.'), ('./cpu_light.svg', '.'), ('./warning_dark.svg', '.'), ('./warning_light.svg', '.'), ('./timer_dark.svg', '.'), ('./timer_light.svg', '.'), ('./volume_dark.svg', '.'), ('./volume_light.svg', '.'), ('./volume_mute_dark.svg', '.'), ('./volume_mute_light.svg', '.'), ('./volume_down_dark.svg', '.'), ('./volume_down_light.svg', '.'), ('./volume_big_dark.svg', '.'), ('./volume_big_light.svg', '.'), ('./fullscreen_dark.svg', '.'), ('./fullscreen_light.svg', '.'), ('./settings_dark.svg', '.'), ('./settings_light.svg', '.'), ('./information_dark.svg', '.'), ('./information_light.svg', '.'), ('./sound_dark.svg', '.'), ('./sound_light.svg', '.'), ('./warning.svg', '.'), ('./theme_light.svg', '.'), ('./theme_dark.svg', '.'), ('./language_light.svg', '.'), ('./language_dark.svg', '.'), ('./chart_light.svg', '.'), ('./chart_dark.svg', '.'), ('./easter_egg_light.svg', '.'), ('./easter_egg_dark.svg', '.'), ('./dashboard_light.svg', '.'), ('./dashboard_dark.svg', '.'), ('./slider_light.svg', '.'), ('./slider_dark.svg', '.'), ('./i18n.ja-jp.txt', '.'), ('./i18n.zh-cn.txt', '.'), ('./i18n.zh-tw.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='LivingRPS v2.0.4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.ico'],
)
