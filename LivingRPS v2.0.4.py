import psutil
import pygame
import pygame._sdl2 as sdl2
import datetime
import random
import math
import time
import sys
import os
import ctypes
import winreg
import locale
import tkinter as tk

# default resolution
W, H = 1600, 1200
W_OLD, H_OLD = W, H

# minimum resolution
MIN_W, MIN_H = 1320, 768

def check_resolution(min_width = 1344, min_height = 768, compensate=0):
    # 获取当前显示信息
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h
    
    # 实际需求尺寸（加上补偿）
    required_width = min_width
    required_height = min_height + compensate  # 补偿标题栏和任务栏
    
    if screen_width >= required_width and screen_height >= required_height:
        return True  # 分辨率足够，直接继续
    
    # 否则弹出对话框
    msg = f"Your screen resolution is {screen_width}x{screen_height}.\n" + \
        f"At least {required_width}x{required_height} is required.\n" + \
        f"Continue anyway?"
    # 使用messagebox
    buttons = ("Confirm", "Cancel")
    result = sdl2.messagebox(
        title = "Resolution Warning",
        message = msg,
        buttons = buttons,
        return_button = 0,         # 默认返回的按钮索引（0 = "确定"）
        escape_button = 1,
        warn = True
    )
    # 返回 True 如果点击确定，False 如果取消
    return result == 0 

# 获取当前进程
this_process = psutil.Process(os.getpid()) 

# clamp
def clamp(x: float, left: float = 0.0, right: float = 1.0) -> float: 
    return max(left, min(right, x))

# 有理数取模
def div_mod(p: int, q: int, mod: int = 998244353) -> int: 
    return p * pow(q, mod - 2, mod) % mod

# Resource helpers
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 图标
EMOJI_SIZE = 24
BIG_EMOJI_SIZE = 40

# rock, paper, scissors
icon_paper = pygame.image.load(resource_path('./paper.svg'))
icon_paper = pygame.transform.scale(icon_paper, (EMOJI_SIZE, EMOJI_SIZE))
icon_rock = pygame.image.load(resource_path('./rock.svg'))
icon_rock = pygame.transform.scale(icon_rock, (EMOJI_SIZE + 3, EMOJI_SIZE + 3))
icon_scissors = pygame.image.load(resource_path('./scissors.svg'))
icon_scissors = pygame.transform.scale(icon_scissors, (EMOJI_SIZE - 2, EMOJI_SIZE - 2))
icon_scissors = pygame.transform.rotate(icon_scissors, 180)

# maybe useful ↓↓↓
icon_laptop = pygame.image.load(resource_path('./laptop.svg'))
icon_laptop = pygame.transform.scale(icon_laptop, (EMOJI_SIZE, EMOJI_SIZE))
icon_heart = pygame.image.load(resource_path('./heart.svg'))
icon_heart = pygame.transform.scale(icon_heart, (EMOJI_SIZE, EMOJI_SIZE))
icon_timer = pygame.image.load(resource_path('./timer.svg'))
icon_timer = pygame.transform.scale(icon_timer, (EMOJI_SIZE, EMOJI_SIZE))
icon_bomb = pygame.image.load(resource_path('./bomb.svg'))
icon_bomb = pygame.transform.scale(icon_bomb, (EMOJI_SIZE + 10, EMOJI_SIZE + 10))
icon_warning = pygame.image.load(resource_path('./warning.svg'))
icon_warning = pygame.transform.scale(icon_warning, (EMOJI_SIZE, EMOJI_SIZE))
icon_systemclock = pygame.image.load(resource_path('./systemclock.svg'))
icon_systemclock = pygame.transform.scale(icon_systemclock, (EMOJI_SIZE - 6, EMOJI_SIZE - 6))
icon_box = pygame.image.load(resource_path('./box.svg'))
icon_box = pygame.transform.scale(icon_box, (EMOJI_SIZE, EMOJI_SIZE))
icon_heart = pygame.image.load(resource_path('./heart.svg'))
icon_heart = pygame.transform.scale(icon_heart, (EMOJI_SIZE + 4, EMOJI_SIZE + 4))
icon_timer = pygame.image.load(resource_path('./timer.svg'))
icon_timer = pygame.transform.scale(icon_timer, (EMOJI_SIZE + 1, EMOJI_SIZE + 1))
icon_laptop = pygame.image.load(resource_path('./laptop.svg'))
icon_laptop = pygame.transform.scale(icon_laptop, (EMOJI_SIZE, EMOJI_SIZE))
icon_memory = pygame.image.load(resource_path('./memory.svg'))
icon_memory = pygame.transform.scale(icon_memory, (EMOJI_SIZE - 1, EMOJI_SIZE - 1))
# maybe useful ↑↑↑

# ===============================================
# dark mode icons and light mode icons
# ===============================================

# heart
icon_heart_light = pygame.image.load(resource_path('./heart_light.svg'))
icon_heart_light = pygame.transform.scale(icon_heart_light, (EMOJI_SIZE + 1, EMOJI_SIZE + 1))
icon_heart_dark = pygame.image.load(resource_path('./heart_dark.svg'))
icon_heart_dark = pygame.transform.scale(icon_heart_dark, (EMOJI_SIZE + 1, EMOJI_SIZE + 1))

# memory
icon_memory_light = pygame.image.load(resource_path('./memory_light.svg'))
icon_memory_light = pygame.transform.scale(icon_memory_light, (EMOJI_SIZE - 2, EMOJI_SIZE - 2))
icon_memory_dark = pygame.image.load(resource_path('./memory_dark.svg'))
icon_memory_dark = pygame.transform.scale(icon_memory_dark, (EMOJI_SIZE - 2, EMOJI_SIZE - 2))

# agent
icon_box_light = pygame.image.load(resource_path('./box_light.svg'))
icon_box_light = pygame.transform.scale(icon_box_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_box_dark = pygame.image.load(resource_path('./box_dark.svg'))
icon_box_dark = pygame.transform.scale(icon_box_dark, (EMOJI_SIZE, EMOJI_SIZE))

# timer (running)
icon_timer_light = pygame.image.load(resource_path('./timer_light.svg'))
icon_timer_light = pygame.transform.scale(icon_timer_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_timer_dark = pygame.image.load(resource_path('./timer_dark.svg'))
icon_timer_dark = pygame.transform.scale(icon_timer_dark, (EMOJI_SIZE, EMOJI_SIZE))

# clock
icon_systemclock_light = pygame.image.load(resource_path('./clock_light.svg'))
icon_systemclock_light = pygame.transform.scale(icon_systemclock_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_systemclock_dark = pygame.image.load(resource_path('./clock_dark.svg'))
icon_systemclock_dark = pygame.transform.scale(icon_systemclock_dark, (EMOJI_SIZE, EMOJI_SIZE))

# resolution
icon_resolution_light = pygame.image.load(resource_path('./resolution_light.svg'))
icon_resolution_light = pygame.transform.scale(icon_resolution_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_resolution_dark = pygame.image.load(resource_path('./resolution_dark.svg'))
icon_resolution_dark = pygame.transform.scale(icon_resolution_dark, (EMOJI_SIZE, EMOJI_SIZE))

# volume
icon_volume_dark = pygame.image.load(resource_path('./volume_dark.svg'))
icon_volume_dark = pygame.transform.scale(icon_volume_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_light = pygame.image.load(resource_path('./volume_light.svg'))
icon_volume_light = pygame.transform.scale(icon_volume_light, (EMOJI_SIZE, EMOJI_SIZE))

# warning
icon_warning_dark = pygame.image.load(resource_path('./warning_dark.svg'))
icon_warning_dark = pygame.transform.scale(icon_warning_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_warning_light = pygame.image.load(resource_path('./warning_light.svg'))
icon_warning_light = pygame.transform.scale(icon_warning_light, (EMOJI_SIZE, EMOJI_SIZE))

# cpu
icon_cpu_dark = pygame.image.load(resource_path('./cpu_dark.svg'))
icon_cpu_dark = pygame.transform.scale(icon_cpu_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_cpu_light = pygame.image.load(resource_path('./cpu_light.svg'))
icon_cpu_light = pygame.transform.scale(icon_cpu_light, (EMOJI_SIZE, EMOJI_SIZE))

# fullscreen
icon_fullscreen_light = pygame.image.load(resource_path('./fullscreen_light.svg'))
icon_fullscreen_light = pygame.transform.scale(icon_fullscreen_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_fullscreen_dark = pygame.image.load(resource_path('./fullscreen_dark.svg'))
icon_fullscreen_dark = pygame.transform.scale(icon_fullscreen_dark, (EMOJI_SIZE, EMOJI_SIZE))

# volume LV1-3
icon_volume_big_dark = pygame.image.load(resource_path('./volume_big_dark.svg'))
icon_volume_big_dark = pygame.transform.scale(icon_volume_big_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_big_light = pygame.image.load(resource_path('./volume_big_light.svg'))
icon_volume_big_light = pygame.transform.scale(icon_volume_big_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_small_dark = pygame.image.load(resource_path('./volume_down_dark.svg'))
icon_volume_small_dark = pygame.transform.scale(icon_volume_small_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_small_light = pygame.image.load(resource_path('./volume_down_light.svg'))
icon_volume_small_light = pygame.transform.scale(icon_volume_small_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_mute_dark = pygame.image.load(resource_path('./volume_mute_dark.svg'))
icon_volume_mute_dark = pygame.transform.scale(icon_volume_mute_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_volume_mute_light = pygame.image.load(resource_path('./volume_mute_light.svg'))
icon_volume_mute_light = pygame.transform.scale(icon_volume_mute_light, (EMOJI_SIZE, EMOJI_SIZE))

# settings (for panel title)
icon_settings_dark = pygame.image.load(resource_path('./settings_dark.svg'))
icon_settings_dark = pygame.transform.scale(icon_settings_dark, (BIG_EMOJI_SIZE - 4, BIG_EMOJI_SIZE - 4))
icon_settings_light = pygame.image.load(resource_path('./settings_light.svg'))
icon_settings_light = pygame.transform.scale(icon_settings_light, (BIG_EMOJI_SIZE - 4, BIG_EMOJI_SIZE - 4))

# information (for panel title)
icon_information_dark = pygame.image.load(resource_path('./information_dark.svg'))
icon_information_dark = pygame.transform.scale(icon_information_dark, (BIG_EMOJI_SIZE, BIG_EMOJI_SIZE))
icon_information_light = pygame.image.load(resource_path('./information_light.svg'))
icon_information_light = pygame.transform.scale(icon_information_light, (BIG_EMOJI_SIZE, BIG_EMOJI_SIZE))

# dashboard (for button)
icon_infobox_light = pygame.image.load(resource_path('./dashboard_light.svg'))
icon_infobox_light = pygame.transform.scale(icon_infobox_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_infobox_dark = pygame.image.load(resource_path('./dashboard_dark.svg'))
icon_infobox_dark = pygame.transform.scale(icon_infobox_dark, (EMOJI_SIZE, EMOJI_SIZE))

# sound (for panel title)
icon_sound_dark = pygame.image.load(resource_path('./sound_dark.svg'))
icon_sound_dark = pygame.transform.scale(icon_sound_dark, (BIG_EMOJI_SIZE - 4, BIG_EMOJI_SIZE - 4))
icon_sound_light = pygame.image.load(resource_path('./sound_light.svg'))
icon_sound_light = pygame.transform.scale(icon_sound_light, (BIG_EMOJI_SIZE - 4, BIG_EMOJI_SIZE - 4))

# easter egg (for button)
icon_easter_egg_light = pygame.image.load(resource_path('./easter_egg_light.svg'))
icon_easter_egg_light = pygame.transform.scale(icon_easter_egg_light, (EMOJI_SIZE, EMOJI_SIZE))
icon_easter_egg_dark = pygame.image.load(resource_path('./easter_egg_dark.svg'))
icon_easter_egg_dark = pygame.transform.scale(icon_easter_egg_dark, (EMOJI_SIZE, EMOJI_SIZE))

# language (for button)
icon_language_dark = pygame.image.load(resource_path('./language_dark.svg'))
icon_language_dark = pygame.transform.scale(icon_language_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_language_light = pygame.image.load(resource_path('./language_light.svg'))
icon_language_light = pygame.transform.scale(icon_language_light, (EMOJI_SIZE, EMOJI_SIZE))

# chart (for button)
icon_chart_dark = pygame.image.load(resource_path('./chart_dark.svg'))
icon_chart_dark = pygame.transform.scale(icon_chart_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_chart_light = pygame.image.load(resource_path('./chart_light.svg'))
icon_chart_light = pygame.transform.scale(icon_chart_light, (EMOJI_SIZE, EMOJI_SIZE))

# about (for button)
icon_about_dark = pygame.image.load(resource_path('./information_dark.svg'))
icon_about_dark = pygame.transform.scale(icon_about_dark, (EMOJI_SIZE + 4, EMOJI_SIZE + 4))
icon_about_light = pygame.image.load(resource_path('./information_light.svg'))
icon_about_light = pygame.transform.scale(icon_about_light, (EMOJI_SIZE + 4, EMOJI_SIZE + 4))

# setting (for button)
icon_slider_dark = pygame.image.load(resource_path('./slider_dark.svg'))
icon_slider_dark = pygame.transform.scale(icon_slider_dark, (EMOJI_SIZE + 2, EMOJI_SIZE + 2))
icon_slider_light = pygame.image.load(resource_path('./slider_light.svg'))
icon_slider_light = pygame.transform.scale(icon_slider_light, (EMOJI_SIZE + 2, EMOJI_SIZE + 2))

# parameter settings (for button)
icon_parameters_dark = pygame.image.load(resource_path('./settings_dark.svg'))
icon_parameters_dark = pygame.transform.scale(icon_settings_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_parameters_light = pygame.image.load(resource_path('./settings_light.svg'))
icon_parameters_light = pygame.transform.scale(icon_settings_light, (EMOJI_SIZE, EMOJI_SIZE))

# theme icon (moon = dark mode, sun = light mode)
icon_theme_dark = pygame.image.load(resource_path('./theme_dark.svg'))
icon_theme_dark = pygame.transform.scale(icon_theme_dark, (EMOJI_SIZE, EMOJI_SIZE))
icon_theme_light = pygame.image.load(resource_path('./theme_light.svg'))
icon_theme_light = pygame.transform.scale(icon_theme_light, (EMOJI_SIZE, EMOJI_SIZE))

# 监测程序是否活跃
class ActivityMonitor:
    def __init__(self, inactive_timeout = 5.0):
        self.last_activity_time = time.time()
        self.inactive_timeout = inactive_timeout
        self.active = True
    
    def reset_activity(self):
        """重置活动计时器"""
        self.last_activity_time = time.time()
        if not self.active:
            self.active = True
    
    def update(self):
        """检查是否进入非活跃状态"""
        if time.time() - self.last_activity_time > self.inactive_timeout:
            if self.active:
                self.active = False
    
    def handle_events(self, events):
        """处理事件，检测用户活动"""
        for event in events:
            if (event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYDOWN, pygame.KEYUP]):
                self.reset_activity()

monitor = ActivityMonitor(inactive_timeout = 5.0)

# 计时器
class Stopwatch:
    def __init__(self):
        self.reset()
    
    def start(self):
        """启动秒表"""
        if not self.running:
            self.running = True
            if self.start_time == 0:  # 第一次启动
                self.start_time = pygame.time.get_ticks()
            else:  # 从暂停恢复
                pause_duration = pygame.time.get_ticks() - self.pause_time
                self.start_time += pause_duration
    
    def pause(self):
        """暂停秒表"""
        if self.running:
            self.running = False
            self.pause_time = pygame.time.get_ticks()
    
    def stop(self):
        """停止秒表（同暂停）"""
        self.pause()
    
    def reset(self):
        """重置秒表"""
        self.running = False
        self.start_time = 0
        self.pause_time = 0
        self.elapsed_before_pause = 0
    
    # 将毫秒数格式化为 天数:小时:分钟:秒钟.毫秒
    def format_ticks(ticks):    
        milliseconds = ticks % 1000
        total_seconds = ticks // 1000
        seconds = total_seconds % 60
        total_minutes = total_seconds // 60
        minutes = total_minutes % 60
        total_hours = total_minutes // 60
        hours = total_hours % 24
        days = total_hours // 24
        return f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    
    def get_elapsed_time(self):
        """获取经过的时间（毫秒）"""
        if not self.running:
            if self.start_time == 0:  # 未启动过
                return 0
            else:  # 暂停状态
                return self.pause_time - self.start_time
        else:  # 运行中
            return pygame.time.get_ticks() - self.start_time
    
    def get_formatted_time(self):
        """获取格式化时间 00:00:00.000"""
        elapsed_ms = self.get_elapsed_time()
        return Stopwatch.format_ticks(elapsed_ms)

timer = Stopwatch()

def is_dark_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return value == 0
    except:
        return False

def enable_dark_title_bar(window):
    if pygame.get_init():  # 确保已经初始化
        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))

def disable_dark_title_bar(window):
    if pygame.get_init():  # 确保已经初始化
        hwnd = pygame.display.get_wm_info()["window"]
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, 19, ctypes.byref(ctypes.c_int(0)), ctypes.sizeof(ctypes.c_int))

# icon
def load_icon(icon = "./logo.ico"):
    try:
        icon_path = resource_path(icon)
        return pygame.image.load(icon_path)
    except:
        return None

# i18n
class I18n:
    def __init__(self, language = "zh-cn"):
        self.language = language
        self.texts = {}
        self.load_language(language = language)
    def load_language(self, language = "zh-cn") -> dict[str, str]:
        try:
            texts = {}
            language_path = resource_path(f"./i18n.{language}.txt")
            if os.path.exists(language_path):
                with open(language_path, "r", encoding = "utf-8") as f:
                    lines = f.readlines()
                    for ln in lines:
                        ln = ln.split("=")
                        # print(len(ln))
                        ln[1] = ln[1].strip()
                        if ln[1] != "":
                            texts[ln[0]] = ln[1] 
            self.texts = texts
        except Exception as e:
            print(e)
            pass

default_locale = locale.getlocale()
language_select = ["en-us", "zh-cn", "zh-tw", "ja-jp"] # coming soon
i18ns = {item: I18n(language = item) for item in language_select}

current_language = None
if default_locale[0] == 'Chinese (Simplified)_China':
    current_language = 1
elif default_locale[0] == 'Chinese (Traditional)_Taiwan':
    current_language = 2
elif default_locale[0] == 'Japanese_Japan':
    current_language = 3
else:
    current_language = 0

i18n = i18ns[language_select[current_language]]

# fonts
def load_font(font = "./Sen-Regular.otf", size = 20):
    font_path = resource_path(font)
    return pygame.font.Font(font_path, size = size)

# sound fx
pygame.mixer.init(channels = 256)
sound_kick   = pygame.mixer.Sound(resource_path("./kick.wav"))
sound_clap   = pygame.mixer.Sound(resource_path("./clap.wav"))
sound_hihat  = pygame.mixer.Sound(resource_path("./hi-hat.wav"))
sound_snare  = pygame.mixer.Sound(resource_path("./snare.wav"))
sound_cymbal = pygame.mixer.Sound(resource_path("./cymbal.wav"))
sound_explode = pygame.mixer.Sound(resource_path("./destruction_bomb.ogg"))
sound_bomb_deploy = pygame.mixer.Sound(resource_path("./mining.ogg"))
sound_agent_destruction = pygame.mixer.Sound(resource_path("./destruction_mixer.ogg"))

SOUNDS = {
    "kick":   sound_kick,
    "snare":  sound_snare,
    "hihat":  sound_hihat,
    "cowbell":   sound_clap,
    "cymbal": sound_cymbal,
}
sound_volumes = {
    "global": 0.03,
    "kick": 0.40,
    "snare": 0.45,
    "hihat": 0.25,
    "cymbal": 0.95,
    "cowbell": 0.35
}

sound_kick.set_volume(0.4 * sound_volumes["global"])
sound_clap.set_volume(0.35 * sound_volumes["global"])
sound_hihat.set_volume(0.25 * sound_volumes["global"])
sound_snare.set_volume(0.45 * sound_volumes["global"])
sound_cymbal.set_volume(0.95 * sound_volumes["global"])
sound_explode.set_volume(clamp(30 * sound_volumes["global"]))
sound_bomb_deploy.set_volume(clamp(30 * sound_volumes["global"]))
    
try:
    # Windows 10 Build 1607 及以上、Win11 全支持
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE v2
except:
    ctypes.windll.user32.SetProcessDPIAware()       # 老版本备用

# 只有 Windows 10 1903+ / Windows 11 支持
DWMWA_USE_IMMERSIVE_DARK_MODE = 20

# Init pygame
pygame.init()

# Check resolution
if not check_resolution(1344, 768, compensate = 0):
    pygame.quit()
    sys.exit()

pygame.mixer.set_num_channels(128)

# initialize screen
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption(os.path.basename(__file__)[:-3] + " by @0x00ac3375")
pygame.display.set_icon(load_icon())
if is_dark_mode():
    enable_dark_title_bar(pygame.display.get_surface())
else:
    disable_dark_title_bar(pygame.display.get_surface())

# --------- Default parameters (will be editable in Settings) -----------
NUM_AGENTS = 225
MAX_AGENTS = 1100
HEALING_PACKS = 35
RADIUS = 12
SPEED = 2
INITIAL_HEALTH = 12
HEAL_AMOUNT = 5
DAMAGE_WIN = -1
DAMAGE_LOSE = 2
DAMAGE_INNER = 0
OVERFLOW_DAMAGE_BASE = 1
OVERFLOW_MULTIPLIER = 1.00
PIECES = 8
MAX_PER_TYPE = 225
PROB_DECAY = 0.99
SPLIT_HEALTH_BASELINE = 20
CELL = 24
BOMB_INIT_TICKS = 60
EXPLODE_RADIUS = 225
EXPLODE_GROW_FRAMES = 3

# Hidden params
_SQ2R = 4 * pow(RADIUS, 2)

# Colors for fallback
LIGHT_BG  = (255,255,255)
LIGHT_FG  = (12,12,12)
DARK_BG   = (32,32,32)
DARK_FG   = (230,230,230)

# highlight color for buttons
hover_color_dark = (205, 205, 205)
hover_color_light = (64, 64, 64)
normal_color_dark = (175, 175, 175)
normal_color_light = (32, 32, 32)

# Types
TYPES = {
    "rock": {"emoji":  icon_rock, "color": (200, 50, 50)}, # "\U0001faa8"
    "paper": {"emoji": icon_paper, "color": (50, 200, 50)},
    "scissors": {"emoji": icon_scissors, "color": (50, 50, 200)}
}

ICONS = {
    'paper': icon_paper,
    'rock': icon_rock,
    'scissors': icon_scissors,
    'laptop': icon_laptop,
    'heart': icon_heart,
    'timer': icon_timer,
    'systemclock': icon_systemclock,
    'warning': icon_warning,
    'bomb': icon_bomb,
}

def beats(a, b):
    return (a=="rock" and b=="scissors") or (a=="scissors" and b=="paper") or (a=="paper" and b=="rock")

# ---------------- Entities ----------------

# Agent
class Agent:
    def __init__(self, x=None, y=None, health=None, type_ = None):
        self.x = x if x is not None else random.uniform(RADIUS, W - RADIUS)
        self.y = y if y is not None else random.uniform(RADIUS, H - RADIUS)
        angle = random.uniform(0, 2*math.pi)
        self.vx = math.cos(angle) * SPEED
        self.vy = math.sin(angle) * SPEED
        self.type = type_ if type_ is not None else random.choice(["rock","paper","scissors"])
        self.icon = ICONS[self.type]
        self.health = health if health is not None else INITIAL_HEALTH

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - RADIUS < 0:
            self.x = RADIUS; self.vx *= -1; sound_kick.play()
        elif self.x + RADIUS > W:
            self.x = W - RADIUS; self.vx *= -1; sound_kick.play()
        if self.y - RADIUS < 0:
            self.y = RADIUS; self.vy *= -1; sound_kick.play()
        elif self.y + RADIUS > H:
            self.y = H - RADIUS; self.vy *= -1; sound_kick.play()

    def draw(self, surf, health_font, fg_color):
        emoji_surface = self.icon
        emoji_rect = emoji_surface.get_rect(center=(int(self.x), int(self.y)))
        surf.blit(self.icon, emoji_rect)
        health_text = health_font.render(str(self.health), True, fg_color)
        health_rect = health_text.get_rect(center=(int(self.x), int(self.y)-20))
        if show_hp:
            surf.blit(health_text, health_rect)
    
    def should_split(self):
        # if len(agents) >= MAX_AGENTS: return False
        if self.health >= SPLIT_HEALTH_BASELINE * PIECES * 0.75:
            return True
        elif self.health > INITIAL_HEALTH:
            # 线性概率：health=21 → ~0%, health=59 → ~97%
            min_h = INITIAL_HEALTH + 1
            max_h = SPLIT_HEALTH_BASELINE * PIECES * 0.75 - 1
            if self.health <= min_h:
                return False
            p = (self.health - min_h) / (max_h - min_h)
            return random.random() < p * PROB_DECAY ** max(0, counts[self.type] - MAX_PER_TYPE)
        return False

# Packs
class HealingPack:
    def __init__(self):
        self.x = random.randint(10, W-10)
        self.y = random.randint(10, H-10)
    def draw(self, surf, color):
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), 4)

# Bombs
class Bomb(Agent):
    def __init__(self, x, y, ticks = BOMB_INIT_TICKS):
        self.x = x
        self.y = y
        # 覆盖不需要的字段
        self.type = "bomb"
        self.vx = 0                 # 初始静止
        self.vy = 0
        self.ticks = int(ticks)
        self.last_tick_time = pygame.time.get_ticks()
        self.exploding = False
        self.explode_start = 0
        self.radius = 0
        self.explode_frame = 0
        self.health = None
        self.type = "bomb"
        self.icon = ICONS[self.type]

    def update(self):
        if not self.exploding:
            now = pygame.time.get_ticks()
            if now - self.last_tick_time >= 1000:
                self.ticks -= 1
                self.last_tick_time = now
                # tick beep (optional) - more urgent with low ticks
                if self.ticks <= 5 and mode == "running":
                    if sound_snare:
                        sound_snare.play()
                if self.ticks <= 0:
                    self.exploding = True
                    self.explode_start = now
                    self.explode_frame = 0
                    # instant cymbal sound
                    if sound_cymbal and mode == "running":
                        sound_explode.play()
        else:
            # increase frame for growth
            self.explode_frame += 1
            if self.explode_frame > EXPLODE_GROW_FRAMES:
                # eligible for removal
                return True   # tell main loop to remove me
            return False
    
    def should_split(self):
        return False

    def draw(self, surf):
        # Draw bomb emoji, digital countdown and shaking if low
        if not self.exploding:
            # shaking
            ox, oy = 0, 0
            if self.ticks <= 10:
                # shake strength increases as ticks -> 0
                strength = (10 - self.ticks) / 10.0
                ox = int((random.random() - 0.5) * 12 * strength)
                oy = int((random.random() - 0.5) * 12 * strength)
            # draw bomb emoji centered, slight larger
            bomb_surf = bomb_font.render("\U0001f4a3", True, (255,255,255))
            rect = bomb_surf.get_rect(center=(int(self.x + ox), int(self.y + oy)))
            surf.blit(self.icon, rect)
            # seven-seg countdown overlay (center)
            timer_txt = str(max(0, self.ticks))
            seg = sevenseg_font.render(timer_txt, True, (255, 255, 255))
            seg_rect = seg.get_rect(center=(int(self.x + ox - 9), int(self.y + oy - 2)))
            surf.blit(seg, seg_rect)
        else:
            # explosion emoji for a few frames, then ring
            if self.explode_frame < EXPLODE_GROW_FRAMES:
                boom = explode_font.render("\U0001F4A5", True, (255,255,255))
                surf.blit(boom, boom.get_rect(center=(int(self.x), int(self.y))))

# ---------------- UI Components ----------------

# Button
class Button:
    def __init__(self, rect, text, font, colors, text_color):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.colors = colors  # (idle, hover, pressed)
        self.text_color = text_color
        self.pressed = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                return True
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        return False

    def draw(self, surf):
        mpos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mpos):
            color = self.colors[1] if not pygame.mouse.get_pressed()[0] else self.colors[2]
        else:
            color = self.colors[0]
        pygame.draw.rect(surf, color, self.rect, border_radius=10)
        txt = self.font.render(self.text, True, self.text_color)
        surf.blit(txt, txt.get_rect(center=self.rect.center))

# TextBox
class InputBox:
    def __init__(self, rect, text, font, theme):
        self.rect = pygame.Rect(rect)
        self.text = str(text)
        self.font = font
        self.active = False
        self.theme = theme

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
            else:
                ch = event.unicode
                # allow digits, dot, minus
                if ch.isdigit() or ch in ".-":
                    self.text += ch

    def draw(self, surf):
        bg = self.theme['input_active_bg'] if self.active else self.theme['input_bg']
        pygame.draw.rect(surf, bg, self.rect, border_radius=6)
        borderc = self.theme['accent'] if self.active else self.theme['panel_border']
        pygame.draw.rect(surf, borderc, self.rect, 2, border_radius=6)
        txt = self.font.render(self.text, True, self.theme['text'])
        surf.blit(txt, (self.rect.x+8, self.rect.y+4))

# Settings panel that adapts theme
class SettingsPanel:
    def __init__(self, screen, settings_dict, theme):
        self.screen = screen
        self.W, self.H = screen.get_size()
        self.settings_dict = dict(settings_dict)
        self.parameter_description = {field: i18n.texts.get("SettingsPanel." + field, field) for field in settings_keys}
        self.theme = theme
        self.title_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 34)
        self.label_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20)
        self.input_font = load_font(size = 20)
        self.panel_rect = pygame.Rect(self.W // 2 - 500, self.H // 2 - 390, 1000, 780)
        # Build inputs in order
        keys = list(self.settings_dict.keys())
        self.inputs = {}
        start_y = self.panel_rect.y + 65
        for i, k in enumerate(keys):
            self.inputs[k] = InputBox((self.panel_rect.x + 835, start_y + i * 36, 140, 30),
                                     str(self.settings_dict[k]), self.input_font, theme)
        # Buttons
        self.btn_apply = Button((self.panel_rect.x + 275, self.panel_rect.y + 715, 140, 44),
                                i18n.texts.get("SettingsPanel.ButtonApply", "Apply"), 
                                load_font(size = 20) if language_select[current_language] == "en-us" else load_font("./zh-cn.ttf", 20),
                                (theme['apply_idle'], theme['apply_hover'], theme['apply_pressed']),
                                theme['button_text'])
        self.btn_cancel = Button((self.panel_rect.x + 430, self.panel_rect.y + 715, 140, 44),
                                 i18n.texts.get("SettingsPanel.ButtonCancel", "Cancel"), 
                                 load_font(size = 20) if language_select[current_language] == "en-us" else load_font("./zh-cn.ttf", 20),
                                 (theme['cancel_idle'], theme['cancel_hover'], theme['cancel_pressed']),
                                 theme['button_text'])
        self.btn_reset = Button((self.panel_rect.x + 585, self.panel_rect.y + 715, 140, 44),
                                 i18n.texts.get("SettingsPanel.ButtonReset", "Reset"), 
                                 load_font(size = 20) if language_select[current_language] == "en-us" else load_font("./zh-cn.ttf", 20),
                                 (theme['reset_idle'], theme['reset_hover'], theme['reset_pressed']),
                                 theme['button_text'])
        
        # simple fade animation
        self.alpha = 0
        self.opening = True

    def handle_event(self, event):
        for inp in self.inputs.values():
            inp.handle_event(event)
        if self.btn_reset.handle_event(event):
            self.reset_params()
            timer.reset()
            return "reset"
        if self.btn_apply.handle_event(event):
            timer.reset()
            return "apply"
        if self.btn_cancel.handle_event(event):
            timer.start()
            return "cancel"
        return None

    def draw(self):
        # fade in alpha
        if self.opening and self.alpha < 180:
            self.alpha += 20
        overlay = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        overlay.fill((0,0,0,self.alpha))
        self.screen.blit(overlay, (0,0))
        # shadow
        shadow = pygame.Surface((self.panel_rect.w+12, self.panel_rect.h+12), pygame.SRCALPHA)
        shadow.fill((0,0,0,80))
        self.screen.blit(shadow, (self.panel_rect.x+6, self.panel_rect.y+6))
        # panel
        panel_surf = pygame.Surface((self.panel_rect.w, self.panel_rect.h), pygame.SRCALPHA)
        panel_surf.fill(self.theme['panel_bg'])
        pygame.draw.rect(panel_surf, self.theme['panel_border'], panel_surf.get_rect(), 3, border_radius=18)
        # blit panel
        self.screen.blit(panel_surf, self.panel_rect.topleft)
        # title
        title = self.title_font.render("     " + i18n.texts.get("SettingsPanel.Title", "Parameters"), True, self.theme['text'])
        self.screen.blit(title, (self.panel_rect.x+28, self.panel_rect.y+24))
        # icon
        self.screen.blit(icon_settings_dark if dark_mode else icon_settings_light, (self.panel_rect.x + 28, self.panel_rect.y + 24))
        # draw labels
        keys = list(self.settings_dict.keys())
        for i,k in enumerate(keys):
            y = self.panel_rect.y + 65 + i * 36
            label = self.label_font.render(self.parameter_description[k], True, self.theme['text'])
            self.screen.blit(label, (self.panel_rect.x+28, y+4))
            self.inputs[k].draw(self.screen)
        # draw buttons
        self.btn_apply.draw(self.screen)
        self.btn_cancel.draw(self.screen)
        self.btn_reset.draw(self.screen)

    def get_values(self):
        out = {}
        for k, inp in self.inputs.items():
            txt = inp.text.strip()
            # try to parse int/float fallback to original
            if txt == "":
                out[k] = self.settings_dict[k]
            else:
                if '.' in txt:
                    try:
                        out[k] = float(txt)
                        # if it is integral, cast to int for integer params
                        if out[k].is_integer():
                            out[k] = int(out[k])
                    except:
                        out[k] = self.settings_dict[k]
                else:
                    try:
                        out[k] = int(txt)
                    except:
                        out[k] = self.settings_dict[k]
        return out
    
    def reset_params(self):
        global  NUM_AGENTS, MAX_AGENTS, HEALING_PACKS, RADIUS, SPEED, INITIAL_HEALTH, HEAL_AMOUNT, \
                DAMAGE_WIN, DAMAGE_LOSE, DAMAGE_INNER, OVERFLOW_DAMAGE_BASE, OVERFLOW_MULTIPLIER, \
                PIECES, MAX_PER_TYPE, PROB_DECAY, SPLIT_HEALTH_BASELINE, CELL, BOMB_INIT_TICKS, EXPLODE_RADIUS, EXPLODE_GROW_FRAMES
        NUM_AGENTS = 225
        MAX_AGENTS = 1100
        HEALING_PACKS = 35
        RADIUS = 12
        SPEED = 2
        INITIAL_HEALTH = 12
        HEAL_AMOUNT = 5
        DAMAGE_WIN = -1
        DAMAGE_LOSE = 2
        DAMAGE_INNER = 0
        OVERFLOW_DAMAGE_BASE = 1
        OVERFLOW_MULTIPLIER = 1.00
        PIECES = 8
        MAX_PER_TYPE = 225
        PROB_DECAY = 0.99
        SPLIT_HEALTH_BASELINE = 20
        CELL = 24
        BOMB_INIT_TICKS = 60
        EXPLODE_RADIUS = 225
        EXPLODE_GROW_FRAMES = 3

# About panel
class AboutPanel:
    def __init__(self, screen, theme):

        # 初始化关于面板，接收屏幕和主题参数
        self.screen = screen  # 保存屏幕对象
        self.W, self.H = screen.get_size()  # 获取屏幕宽高
        self.theme = theme  # 保存主题配置

        self.title_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 32)
        self.text_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20)

        self.panel_rect = pygame.Rect(self.W//2 - 360, self.H//2 - 250, 720, 500)

        # 关闭按钮
        self.btn_close = Button(
            (self.panel_rect.x + 280, self.panel_rect.y + 430, 160, 44),
            i18n.texts.get("AboutPanel.ButtonClose", "Close"),
            load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20),
            (theme['cancel_idle'], theme['cancel_hover'], theme['cancel_pressed']),
            theme['button_text'])

        self.alpha = 0
        self.opening = True

    def handle_event(self, event):
        if self.btn_close.handle_event(event):
            return "close"
        return None

    def draw(self):
        # Fade-in
        if self.opening and self.alpha < 180:
            self.alpha += 20

        overlay = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        overlay.fill((0,0,0,self.alpha))
        self.screen.blit(overlay, (0,0))

        # shadow
        shadow = pygame.Surface((self.panel_rect.w+12, self.panel_rect.h+12), pygame.SRCALPHA)
        shadow.fill((0,0,0,80))
        self.screen.blit(shadow, (self.panel_rect.x+6, self.panel_rect.y+6))

        # panel
        panel_surface = pygame.Surface((self.panel_rect.w, self.panel_rect.h), pygame.SRCALPHA)
        panel_surface.fill(self.theme['panel_bg'])
        pygame.draw.rect(panel_surface, self.theme['panel_border'], panel_surface.get_rect(), 3, border_radius=18)
        self.screen.blit(panel_surface, self.panel_rect.topleft)

        # Title
        title = self.title_font.render("     " + i18n.texts.get("AboutPanel.Title", "About LivingRPS"), True, self.theme['text'])
        self.screen.blit(title, (self.panel_rect.x + 26, self.panel_rect.y + 24))

        # Icon
        self.screen.blit(icon_information_dark if dark_mode else icon_information_light,
            (self.panel_rect.x + 26, self.panel_rect.y + 24))

        # Body text（可自行编辑）
        lines = [
            os.path.basename(__file__)[:-3],
            i18n.texts.get("AboutPanel.Line1", "A dynamic Rock-Paper-Scissors ecology simulator for Windows 11."),
            i18n.texts.get("AboutPanel.Line2", "Features:"),
            i18n.texts.get("AboutPanel.Line3", " • Real-time emergent behavior"),
            i18n.texts.get("AboutPanel.Line4", " • Elastic collisions + RPS combat"),
            i18n.texts.get("AboutPanel.Line5", " • Healing Packs & Splitting"),
            i18n.texts.get("AboutPanel.Line6", " • Dynamic overflow population pressure"),
            i18n.texts.get("AboutPanel.Line7", " • Sound-reactive drum-machine mode"),
            i18n.texts.get("AboutPanel.Line8", "This application has been developed by 0x00ac3375."), 
            i18n.texts.get("AboutPanel.Line9", "Email: Jake3375@126.com  22281093@bjtu.edu.cn"),
        ]

        y = self.panel_rect.y + 90
        for line in lines:
            txt = self.text_font.render(line, True, self.theme['text'])
            self.screen.blit(txt, (self.panel_rect.x + 30, y))
            y += 30

        self.btn_close.draw(self.screen)

# Slider
class Slider:
    def __init__(self, rect, value, theme):
        self.rect = pygame.Rect(rect)
        self.value = value  # 0.0~1.0
        self.theme = theme
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                x = event.pos[0]
                t = (x - self.rect.x) / self.rect.w
                t = max(0, min(1, t))
                self.value = t

    def draw(self, surf):
        # 轨道
        pygame.draw.rect(surf, self.theme["input_bg"], (self.rect.x - 10, self.rect.y, self.rect.w + 20, self.rect.h), border_radius=6)
        # 滑块位置
        knob_x = self.rect.centerx + int((self.value - 0.5) * self.rect.w)
        pygame.draw.circle(surf, self.theme["accent"], (knob_x, self.rect.centery), 10)
        pygame.draw.rect(surf, self.theme["accent"], (knob_x - 10, self.rect.centery - 10, 20, 20),  border_radius=6)

# Sound Fx Settings Panel
class SoundSettingsPanel:
    def __init__(self, screen, theme, volume_dict):
        self.screen = screen
        self.theme = theme
        self.W, self.H = screen.get_size()

        self.panel_rect = pygame.Rect(self.W // 2 - 350, self.H // 2 - 270, 700, 540)

        self.title_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 32)
        self.label_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20)

        self.sliders = {
            "global":  Slider((self.panel_rect.x + 180, self.panel_rect.y + 110, 400, 22), volume_dict["global"], theme),
            "kick":    Slider((self.panel_rect.x + 180, self.panel_rect.y + 170, 400, 22), volume_dict["kick"], theme),
            "snare":   Slider((self.panel_rect.x + 180, self.panel_rect.y + 230, 400, 22), volume_dict["snare"], theme),
            "hihat":   Slider((self.panel_rect.x + 180, self.panel_rect.y + 290, 400, 22), volume_dict["hihat"], theme),
            "cymbal":  Slider((self.panel_rect.x + 180, self.panel_rect.y + 350, 400, 22), volume_dict["cymbal"], theme),
            "cowbell": Slider((self.panel_rect.x + 180, self.panel_rect.y + 410, 400, 22), volume_dict["cowbell"], theme),
        }

        self.btn_confirm = Button(
            (self.panel_rect.x + 260, self.panel_rect.y + 460, 180, 44),
            i18n.texts.get("SoundSettingsPanel.ButtonConfirm", "Confirm"), 
            load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20),
            (theme['apply_idle'], theme['apply_hover'], theme['apply_pressed']),
            theme['button_text']
        )

        self.alpha = 0
        self.opening = True

    def handle_event(self, event):
        for s in self.sliders.values():
            s.handle_event(event)
        if self.btn_confirm.handle_event(event):
            return "confirm"
        return None

    def draw(self):
        # Fade-in
        if self.opening and self.alpha < 180:
            self.alpha += 20

        overlay = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        overlay.fill((0,0,0,self.alpha))
        self.screen.blit(overlay, (0,0))

        # shadow
        shadow = pygame.Surface((self.panel_rect.w+12, self.panel_rect.h+12), pygame.SRCALPHA)
        shadow.fill((0,0,0,80))
        self.screen.blit(shadow, (self.panel_rect.x+6, self.panel_rect.y+6))

        # panel
        panel_surface = pygame.Surface((self.panel_rect.w, self.panel_rect.h), pygame.SRCALPHA)
        panel_surface.fill(self.theme['panel_bg'])
        pygame.draw.rect(panel_surface, self.theme['panel_border'], panel_surface.get_rect(), 3, border_radius=18)
        self.screen.blit(panel_surface, self.panel_rect.topleft)

        # --- 标题 ---
        title_surf = self.title_font.render("     " + i18n.texts.get("SoundSettingsPanel.Title", "Sound Fx Settings"), True, \
            (10,10,10) if not dark_mode else (230,230,230))
        self.screen.blit(title_surf, (self.panel_rect.x + 28, self.panel_rect.y + 24))

        # --- 图标 ---
        self.screen.blit(icon_sound_dark if dark_mode else icon_sound_light, (self.panel_rect.x + 28, self.panel_rect.y + 24))

        # --- 文本标签（左列） ---
        labels = [
            i18n.texts.get("SoundSettingsPanel.Global", "Global"),
            i18n.texts.get("SoundSettingsPanel.BassDrum","Bass Drum"),
            i18n.texts.get("SoundSettingsPanel.SnareDrum","Snare Drum"),
            i18n.texts.get("SoundSettingsPanel.Hihat","Hi-hat"),
            i18n.texts.get("SoundSettingsPanel.Cymbal","Cymbal"),
            i18n.texts.get("SoundSettingsPanel.Cowbell","Cowbell")
        ]

        start_y = self.panel_rect.y + 120
        for i, name in enumerate(labels):
            label_surf = self.label_font.render(name, True, (10,10,10) if not dark_mode else (230,230,230))
            label_rect = label_surf.get_rect(midleft=(self.panel_rect.x + 40, start_y + i * 60))
            self.screen.blit(label_surf, label_rect)

        # --- 绘制各 slider ---
        for key, slider in self.sliders.items():
            slider.draw(self.screen)

        # --- 百分比文字（右列） ---
        for i, key in enumerate(self.sliders.keys()):
            percent = int(self.sliders[key].value * 100)
            text = f"{percent}%"
            pct_surf = self.label_font.render(text, True, (10,10,10) if not dark_mode else (230,230,230))
            pct_rect = pct_surf.get_rect(midleft=(self.panel_rect.x + 620, start_y + i * 60))
            self.screen.blit(pct_surf, pct_rect)

        # --- Confirm 按钮 ---
        self.btn_confirm.draw(self.screen)

# ---------------- Theme definitions ----------------
LIGHT_THEME = {
    'panel_bg': (255,255,255,240),
    'panel_border': (200,200,200),
    'text': (10,10,10),
    'input_bg': (235,235,235),
    'input_active_bg': (255,255,255),
    'accent': (90,160,255),
    'apply_idle': (0,150,90),
    'apply_hover': (0,175,105),
    'apply_pressed': (0,120,75),
    'cancel_idle': (100,100,100),
    'cancel_hover': (130,130,130),
    'reset_idle': (156,18,21),
    'reset_hover': (176,48,44),
    'cancel_pressed': (80,80,80),
    'reset_pressed': (136,8,11),
    'button_text': (255,255,255)
}

DARK_THEME = {
    'panel_bg': (40,40,40,230),
    'panel_border': (90,90,90),
    'text': (230,230,230),
    'input_bg': (70,70,70),
    'input_active_bg': (90,90,90),
    'accent': (90,180,255),
    'apply_idle': (0,140,100),
    'apply_hover': (0,165,120),
    'apply_pressed': (0,110,85),
    'cancel_idle': (80,80,80),
    'cancel_hover': (110,110,110),
    'reset_idle': (156,18,21),
    'reset_hover': (176,48,44),
    'cancel_pressed': (60,60,60),
    'reset_pressed': (136,8,11),
    'button_text': (255,255,255)
}

# ---------- Simulation helpers ----------
def build_grid(agents):
    grid = {}
    for a in agents:
        cx = int(a.x // CELL)
        cy = int(a.y // CELL)
        grid.setdefault((cx,cy), []).append(a)
    return grid

# ---------- Initialize sim, including the operation of resetting everything ----------
def init_sim():
    global agents, healing_packs, counts, bombs, show_chart, chart_data, \
        hp_data, max_hp_data, avg_health, max_health, timer, show_hp, total_collusions
    agents = [Agent() for _ in range(NUM_AGENTS)]
    healing_packs = [HealingPack() for _ in range(HEALING_PACKS)]
    counts = {"rock":0,"paper":0,"scissors":0,"bomb":0}
    bombs = []
    show_chart = True  # 控制图表显示状态
    show_hp = True
    chart_data = {"rock": [], "paper": [], "scissors": []}  # 存储历史数据
    hp_data = []
    max_hp_data = []
    avg_health = 0
    total_collusions = 0
    max_health = max(a.health for a in agents)
    timer.reset()
    timer.start()

init_sim()

# ---------- Settings integration ----------
settings_keys = [
    "NUM_AGENTS","MAX_AGENTS","HEALING_PACKS","RADIUS","SPEED","INITIAL_HEALTH",
    "HEAL_AMOUNT","DAMAGE_WIN","DAMAGE_LOSE","DAMAGE_INNER","OVERFLOW_DAMAGE_BASE","OVERFLOW_MULTIPLIER",
    "PIECES","MAX_PER_TYPE","PROB_DECAY","SPLIT_HEALTH_BASELINE", "BOMB_INIT_TICKS", "EXPLODE_RADIUS"
]

settings_dict = {k: globals().get(k) for k in settings_keys}

# choose theme based on system
theme = DARK_THEME if is_dark_mode() else LIGHT_THEME

settings_panel = SettingsPanel(screen, settings_dict, theme)
about_panel = AboutPanel(screen, theme)
volume_panel = SoundSettingsPanel(screen, theme, sound_volumes)

# Settings button in bottom right
small_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", size = 20)

# Fonts
try:
    emoji_font = pygame.font.SysFont("Segoe UI Emoji", 24)
except:
    emoji_font = load_font("./seguiemj.ttf", 24)
    
hud_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", 20)
health_font = load_font("./Sen-Regular.otf", 18)  # 头顶生命值字体
sevenseg_font = load_font("./7seg.ttf", 21)
# draw bomb emoji centered, slight larger
try:
    bomb_font = pygame.font.SysFont("Segoe UI Emoji", 32)
    warning_font = pygame.font.SysFont("Segoe UI Emoji", 24)
    icon_font = pygame.font.SysFont("Segoe UI Emoji", 24)
    explode_font = pygame.font.SysFont("Segoe UI Emoji", EXPLODE_RADIUS)
except:
    bomb_font = load_font("./seguiemj.ttf", 32)
    warning_font = load_font("./seguiemj.ttf", 24)
    icon_font = load_font("./seguiemj.ttf", 24)
    explode_font = load_font("./seguiemj.ttf", EXPLODE_RADIUS)

# settings button
settings_button_rect = pygame.Rect(W - 260, H - 65, 240, 52)

# about button
about_button_rect = pygame.Rect(W - 260, H - 130, 240, 52)

# hud button
hud_button_rect = pygame.Rect(W - 780, H - 130, 240, 52)

# sounds settings button
sounds_button_rect = pygame.Rect(W - 520, H - 65, 240, 52)   

# chart settings button
chart_button_rect = pygame.Rect(W - 780, H - 65, 240, 52)

# theme settings button
theme_button_rect = pygame.Rect(W - 1040, H - 65, 240, 52)

# easter egg on/off button
easter_egg_rect = pygame.Rect(20, H - 130, 240, 52)

# hp value on/off button
hp_value_button_rect = pygame.Rect(W - 520, H - 130, 240, 52)

# language button
language_rect = pygame.Rect(20, H - 65, 240, 52)

# fullscreen button
fullscreen_button_rect = pygame.Rect(W - 1040, H - 130, 240, 52)

# chart
chart_rect = pygame.Rect(W - 420, 10, 400, 300)

# chart for easter egg.
easteregg_chart_rect = \
    pygame.Rect(W - 420, 650, 400, 300) if H >= 1100 else \
    pygame.Rect(20, H - 450, 400, 300)

# hp chart
hp_chart_rect = pygame.Rect(W - 420, 330, 400, 300)

mode = "running"  # running or settings

show_chart = True  # 控制图表显示状态
show_hud = True 
_fullscreen_ = False
_easter_egg_ = False
chart_data = {"rock": [], "paper": [], "scissors": []}  # 存储历史数据
hp_data = []
max_hp_data = []
divmod_data = []
avg_health = 0
total_collusions = 0
total_health = 0
max_health = max(a.health for a in agents)
MAX_CHART_POINTS = 200  # 图表最大数据点数

def draw_chart(surface, data, rect, theme):
    """绘制动态折线图"""
    if not data["rock"]:  # 没有数据时不绘制
        return
    
    # 绘制图表背景
    chart_bg = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    chart_bg.fill((40, 40, 40, 200) if theme == DARK_THEME else (255, 255, 255, 200))
    surface.blit(chart_bg, rect)
    pygame.draw.rect(surface, theme['panel_border'], rect, 2, border_radius=8)
    
    # 计算最大数量用于缩放
    all_data = data["rock"] + data["paper"] + data["scissors"]
    max_count = max(all_data) if all_data else 1
    max_count = max(max_count, 10)  # 确保最小值
    
    # 图表内边距
    padding = 40
    chart_width = rect.w - 2 * padding
    chart_height = rect.h - 2 * padding
    
    # 绘制坐标轴
    axis_color = theme['text']
    pygame.draw.line(surface, axis_color, 
                    (rect.x + padding, rect.y + rect.h - padding),
                    (rect.x + rect.w - padding, rect.y + rect.h - padding), 2)  # X轴
    pygame.draw.line(surface, axis_color,
                    (rect.x + padding, rect.y + padding),
                    (rect.x + padding, rect.y + rect.h - padding), 2)  # Y轴
    
    # 绘制刻度标签
    font = load_font(size = 14)

    # Y轴刻度
    for i in range(0, 6):
        y_pos = rect.y + padding + (chart_height * i // 5)
        value = int(max_count * (5 - i) // 5)
        label = font.render(str(value), True, theme['text'])
        surface.blit(label, (rect.x + 10, y_pos - 10))
    
    # 绘制三条折线
    colors = {
        "rock": (255, 100, 100),     # 红色
        "paper": (100, 255, 100),    # 绿色  
        "scissors": (100, 100, 255)  # 蓝色
    }
    
    for agent_type, color in colors.items():
        if len(data[agent_type]) > 1:
            points, OFFSET = [], 40
            for i, count in enumerate(data[agent_type][-chart_width:]):  # 只显示最近的数据
                
                x = rect.x + padding + ((3 * i // 2) % (chart_width))
                y = rect.y + rect.h - padding - (count / max_count) * chart_height
                points.append((x, y))
            
            if len(points) > 1:
                pygame.draw.lines(surface, color, False, points, 2)
    
    # 绘制图例
    legend_y = rect.y + rect.h - 30
    for i, (agent_type, color) in enumerate(colors.items()):
        current_count = data[agent_type][-1] if data[agent_type] else 0
        legend_text = f"{agent_type}: {current_count}"
        legend_surf = font.render(legend_text, True, color)
        surface.blit(legend_surf, (rect.x + 25 + 100 * i, legend_y))

def draw_hp_chart(surface, avghp_data: list, maxhp_data: list, rect, theme):
    """绘制动态折线图"""
    if not avghp_data:
        return

    # 绘制图表背景
    chart_bg = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    chart_bg.fill((40, 40, 40, 200) if theme == DARK_THEME else (255, 255, 255, 200))
    surface.blit(chart_bg, rect)
    pygame.draw.rect(surface, theme['panel_border'], rect, 2, border_radius=8)
    
    # 计算最大数量用于缩放
    data = avghp_data + maxhp_data
    max_count = max(data) if data else 1
    max_count = max(max_count, 10)  # 确保最小值
    
    # 图表内边距
    padding = 40
    chart_width = rect.w - 2 * padding
    chart_height = rect.h - 2 * padding
    
    # 绘制坐标轴
    axis_color = theme['text']
    pygame.draw.line(surface, axis_color, 
                    (rect.x + padding, rect.y + rect.h - padding),
                    (rect.x + rect.w - padding, rect.y + rect.h - padding), 2)  # X轴
    pygame.draw.line(surface, axis_color,
                    (rect.x + padding, rect.y + padding),
                    (rect.x + padding, rect.y + rect.h - padding), 2)  # Y轴
    
    # 绘制刻度标签
    font = load_font(size = 14)

    # Y轴刻度
    for i in range(0, 6):
        y_pos = rect.y + padding + (chart_height * i // 5)
        value = max_count * (5 - i) / 5
        label = font.render(f"{value:.1f}" if value < 100 else f"{value:.0f}", True, theme['text'])
        surface.blit(label, (rect.x + 9, y_pos - 10))
    
    # 绘制折线
    color_avg = (235, 185, 13)
    color_max = (255, 0, 255)
    
    points, OFFSET = [], 40
    for i, count in enumerate(avghp_data[-chart_width:]):  # 只显示最近的数据
                
        x = rect.x + padding + ((3 * i // 2) % (chart_width))
        y = rect.y + rect.h - padding - (count / max_count) * chart_height
        points.append((x, y))
            
        if len(points) > 1:
            pygame.draw.lines(surface, color_avg, False, points, 2)

    points, OFFSET = [], 40
    for i, count in enumerate(maxhp_data[-chart_width:]):  # 只显示最近的数据
                
        x = rect.x + padding + ((3 * i // 2) % (chart_width))
        y = rect.y + rect.h - padding - (count / max_count) * chart_height
        points.append((x, y))
            
        if len(points) > 1:
            pygame.draw.lines(surface, color_max, False, points, 2)
    
    # 绘制图例
    legend_y = rect.y + rect.h - 30
        
    legend_text_avg = f"Average health: {avg_health:.2f}"
    legend_surf = font.render(legend_text_avg, True, color_avg)
    surface.blit(legend_surf, (rect.x + 25, legend_y))
        
    legend_text_max = f"Max health: {max_health:.2f}"
    legend_surf = font.render(legend_text_max, True, color_max)
    surface.blit(legend_surf, (rect.x + 195, legend_y))

def draw_easteregg_chart(surface, divmod_data, rect, theme):
    if not divmod_data:
        return

    # 绘制图表背景
    chart_bg = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
    chart_bg.fill((40, 40, 40, 200) if theme == DARK_THEME else (255, 255, 255, 200))
    surface.blit(chart_bg, rect)
    pygame.draw.rect(surface, theme['panel_border'], rect, 2, border_radius=8)
    
    # 计算最大数量用于缩放
    data = divmod_data
    max_count = max(data) if data else 1
    max_count = max(max_count, 10)  # 确保最小值
    # for debug: max_count = 1000000000
    
    # 图表内边距
    padding = 40
    chart_width = rect.w - 2 * padding
    chart_height = rect.h - 2 * padding
    
    # 绘制坐标轴
    axis_color = theme['text']
    pygame.draw.line(surface, axis_color, 
                    (rect.x + padding, rect.y + rect.h - padding),
                    (rect.x + rect.w - padding, rect.y + rect.h - padding), 2)  # X轴
    pygame.draw.line(surface, axis_color,
                    (rect.x + padding, rect.y + padding),
                    (rect.x + padding, rect.y + rect.h - padding), 2)  # Y轴
    
    # 绘制刻度标签
    font = load_font(size = 14)

    # Y轴刻度
    for i in range(0, 6):
        y_pos = rect.y + padding + (chart_height * i // 5)
        value = max_count * (5 - i) / 5
        label = font.render(f"{value:.1f}" if value < 1e8 else \
            ("1.b" if value >= 995000000 else f"{value / 1e9:.2f}b"[1:]), True, theme['text'])
        surface.blit(label, (rect.x + 9, y_pos - 10))
    
    # 绘制折线
    color_avg = (0, 190, 255)
    
    points, OFFSET = [], 40
    for i, count in enumerate(divmod_data[-chart_width:]):  # 只显示最近的数据
                
        x = rect.x + padding + ((3 * i // 2) % (chart_width))
        y = rect.y + rect.h - padding - (count / max_count) * chart_height
        points.append((x, y))
            
        if len(points) > 1:
            pygame.draw.lines(surface, color_avg, False, points, 2)
    
    # 绘制图例
    legend_y = rect.y + rect.h - 30
        
    legend_text_avg = f"Average health -> {divmod_data[-1]:.0f} (mod 998244353)"
    legend_surf = font.render(legend_text_avg, True, color_avg)
    surface.blit(legend_surf, (rect.x + 25, legend_y))

    pass

# Main loop
running = True
timer.start()
dark_mode = is_dark_mode()
while running:
    # handle events
    events = pygame.event.get()
    monitor.update() if len(events) == 0 and mode == "running" else monitor.reset_activity()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # resizing windows is not allowed if the program is paused or in settings mode.
            if mode != "running":
                screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
            else:
                W, H = max(event.w, MIN_W), max(event.h, MIN_H)
                settings_button_rect = pygame.Rect(W - 260, H - 65, 240, 52)
                about_button_rect = pygame.Rect(W - 260, H - 130, 240, 52)
                hud_button_rect = pygame.Rect(W - 780, H - 130, 240, 52)
                sounds_button_rect = pygame.Rect(W - 520, H - 65, 240, 52)   
                chart_button_rect = pygame.Rect(W - 780, H - 65, 240, 52)
                theme_button_rect = pygame.Rect(W - 1040, H - 65, 240, 52)
                easter_egg_rect = pygame.Rect(20, H - 130, 240, 52)
                hp_value_button_rect = pygame.Rect(W - 520, H - 130, 240, 52)
                language_rect = pygame.Rect(20, H - 65, 240, 52)
                fullscreen_button_rect = pygame.Rect(W - 1040, H - 130, 240, 52)
                chart_rect = pygame.Rect(W - 420, 10, 400, 300)
                easteregg_chart_rect = \
                    pygame.Rect(W - 420, 650, 400, 300) if H >= 1100 else \
                    pygame.Rect(20, H - 450, 400, 300)
                hp_chart_rect = pygame.Rect(W - 420, 330, 400, 300)
                screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        if mode == "running":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    mx,my = pygame.mouse.get_pos()
                    bomb = Bomb(mx, my, ticks=BOMB_INIT_TICKS)
                    bombs.append(bomb)
                    agents.append(bomb)
                    sound_bomb_deploy.play()
                elif event.key == pygame.K_ESCAPE:
                    if _fullscreen_:
                        W, H = W_OLD, H_OLD
                        screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
                        settings_button_rect = pygame.Rect(W - 260, H - 65, 240, 52)
                        about_button_rect = pygame.Rect(W - 260, H - 130, 240, 52)
                        hud_button_rect = pygame.Rect(W - 780, H - 130, 240, 52)
                        sounds_button_rect = pygame.Rect(W - 520, H - 65, 240, 52)   
                        chart_button_rect = pygame.Rect(W - 780, H - 65, 240, 52)
                        theme_button_rect = pygame.Rect(W - 1040, H - 65, 240, 52)
                        easter_egg_rect = pygame.Rect(20, H - 130, 240, 52)
                        hp_value_button_rect = pygame.Rect(W - 520, H - 130, 240, 52)
                        language_rect = pygame.Rect(20, H - 65, 240, 52)
                        fullscreen_button_rect = pygame.Rect(W - 1040, H - 130, 240, 52)
                        chart_rect = pygame.Rect(W - 420, 10, 400, 300)
                        easteregg_chart_rect = \
                            pygame.Rect(W - 420, 650, 400, 300) if H >= 1100 else \
                            pygame.Rect(20, H - 450, 400, 300)
                        hp_chart_rect = pygame.Rect(W - 420, 330, 400, 300)
                        _fullscreen_ = not _fullscreen_
                    else: 
                        pass
            if event.type == pygame.MOUSEWHEEL:
                sound_volumes["global"] += clamp(event.y, -1, 1) * 0.01
                sound_volumes["global"] = clamp(sound_volumes["global"])
                sound_kick.set_volume(sound_volumes["kick"] * sound_volumes["global"])
                sound_clap.set_volume(sound_volumes["cowbell"] * sound_volumes["global"])
                sound_hihat.set_volume(sound_volumes["hihat"] * sound_volumes["global"])
                sound_snare.set_volume(sound_volumes["snare"] * sound_volumes["global"])
                sound_cymbal.set_volume(sound_volumes["cymbal"] * sound_volumes["global"])
                sound_explode.set_volume(clamp(30 * sound_volumes["global"]))
                sound_bomb_deploy.set_volume(clamp(30 * sound_volumes["global"]))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button != 4 and event.button != 5:
                if hud_button_rect.collidepoint(event.pos):
                    show_hud = not show_hud
                elif chart_button_rect.collidepoint(event.pos):
                    show_chart = not show_chart
                elif language_rect.collidepoint(event.pos):
                    current_language = (current_language + 1) % len(language_select)
                    i18n = i18ns[language_select[current_language]]
                    hud_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", 20)
                    small_font = load_font("./Sen-Regular.otf" if language_select[current_language] == "en-us" else "./zh-cn.ttf", 20)
                elif settings_button_rect.collidepoint(event.pos):
                    # open settings
                    # refresh panel theme (in case system changed)
                    theme = DARK_THEME if dark_mode else LIGHT_THEME
                    settings_panel = SettingsPanel(screen, settings_dict, theme)
                    mode = "settings"
                elif about_button_rect.collidepoint(event.pos):
                    theme = DARK_THEME if dark_mode else LIGHT_THEME
                    about_panel = AboutPanel(screen, theme)
                    mode = "about"
                elif sounds_button_rect.collidepoint(event.pos):
                    theme = DARK_THEME if dark_mode else LIGHT_THEME
                    volume_panel = SoundSettingsPanel(screen, theme, sound_volumes)
                    mode = "sounds"
                elif theme_button_rect.collidepoint(event.pos):
                    dark_mode = not dark_mode
                    (enable_dark_title_bar if dark_mode else disable_dark_title_bar)(pygame.display.get_surface())
                    theme = DARK_THEME if dark_mode else LIGHT_THEME
                elif hp_value_button_rect.collidepoint(event.pos):
                    show_hp = not show_hp
                elif easter_egg_rect.collidepoint(event.pos):
                    _easter_egg_ = not _easter_egg_
                elif fullscreen_button_rect.collidepoint(event.pos):
                    _fullscreen_ = not _fullscreen_
                    if _fullscreen_:
                        screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
                        W_OLD, H_OLD = W, H
                        W, H = screen_width, screen_height
                        os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
                        os.environ['SDL_VIDEO_CENTERED'] = '0'
                        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                        settings_button_rect = pygame.Rect(W - 260, H - 65, 240, 52)
                        about_button_rect = pygame.Rect(W - 260, H - 130, 240, 52)
                        hud_button_rect = pygame.Rect(W - 780, H - 130, 240, 52)
                        sounds_button_rect = pygame.Rect(W - 520, H - 65, 240, 52)   
                        chart_button_rect = pygame.Rect(W - 780, H - 65, 240, 52)
                        theme_button_rect = pygame.Rect(W - 1040, H - 65, 240, 52)
                        easter_egg_rect = pygame.Rect(20, H - 130, 215, 52)
                        hp_value_button_rect = pygame.Rect(W - 520, H - 130, 240, 52)
                        chart_rect = pygame.Rect(W - 420, 10, 400, 300)
                        hp_chart_rect = pygame.Rect(W - 420, 330, 400, 300)
                        easteregg_chart_rect = \
                            pygame.Rect(W - 420, 650, 400, 300) if H >= 1100 else \
                            pygame.Rect(20, H - 450, 400, 300)
                        language_rect = pygame.Rect(20, H - 65, 215, 52)
                        fullscreen_button_rect = pygame.Rect(W - 1040, H - 130, 240, 52)
                    else:
                        W, H = W_OLD, H_OLD
                        screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
                        settings_button_rect = pygame.Rect(W - 260, H - 65, 240, 52)
                        about_button_rect = pygame.Rect(W - 260, H - 130, 240, 52)
                        hud_button_rect = pygame.Rect(W - 780, H - 130, 240, 52)
                        sounds_button_rect = pygame.Rect(W - 520, H - 65, 240, 52)   
                        chart_button_rect = pygame.Rect(W - 780, H - 65, 240, 52)
                        theme_button_rect = pygame.Rect(W - 1040, H - 65, 240, 52)
                        easter_egg_rect = pygame.Rect(20, H - 130, 215, 52)
                        hp_value_button_rect = pygame.Rect(W - 520, H - 130, 240, 52)
                        chart_rect = pygame.Rect(W - 420, 10, 400, 300)
                        hp_chart_rect = pygame.Rect(W - 420, 330, 400, 300)
                        easteregg_chart_rect = \
                            pygame.Rect(W - 420, 650, 400, 300) if H >= 1100 else \
                            pygame.Rect(20, H - 450, 400, 300)
                        language_rect = pygame.Rect(20, H - 65, 215, 52)
                        fullscreen_button_rect = pygame.Rect(W - 1040, H - 130, 240, 52)
                else:
                    mx,my = event.pos
                    bomb = Bomb(mx, my, ticks=BOMB_INIT_TICKS)
                    bombs.append(bomb)
                    agents.append(bomb)
                    sound_bomb_deploy.play()

        elif mode == "settings":
            res = settings_panel.handle_event(event)
            if res == "apply":
                values = settings_panel.get_values()
                # apply values to globals
                NUM_AGENTS = int(values.get("NUM_AGENTS", NUM_AGENTS))
                MAX_AGENTS = int(values.get("MAX_AGENTS", MAX_AGENTS))
                HEALING_PACKS = int(values.get("HEALING_PACKS", HEALING_PACKS))
                RADIUS = int(values.get("RADIUS", RADIUS))
                SPEED = float(values.get("SPEED", SPEED))
                INITIAL_HEALTH = int(values.get("INITIAL_HEALTH", INITIAL_HEALTH))
                HEAL_AMOUNT = int(values.get("HEAL_AMOUNT", HEAL_AMOUNT))
                DAMAGE_WIN = int(values.get("DAMAGE_WIN", DAMAGE_WIN))
                DAMAGE_LOSE = int(values.get("DAMAGE_LOSE", DAMAGE_LOSE))
                DAMAGE_INNER = int(values.get("DAMAGE_INNER", DAMAGE_INNER))
                OVERFLOW_DAMAGE_BASE = int(values.get("OVERFLOW_DAMAGE_BASE", OVERFLOW_DAMAGE_BASE))
                OVERFLOW_MULTIPLIER = float(values.get("OVERFLOW_MULTIPLIER", OVERFLOW_MULTIPLIER))
                PIECES = int(values.get("PIECES", PIECES))
                MAX_PER_TYPE = int(values.get("MAX_PER_TYPE", MAX_PER_TYPE))
                PROB_DECAY = float(values.get("PROB_DECAY", PROB_DECAY))
                SPLIT_HEALTH_BASELINE = int(values.get("SPLIT_HEALTH_BASELINE", SPLIT_HEALTH_BASELINE))
                BOMB_INIT_TICKS = int(values.get("BOMB_INIT_TICKS", BOMB_INIT_TICKS))
                EXPLODE_RADIUS = int(values.get("EXPLODE_RADIUS", EXPLODE_RADIUS))
                # reinitialize sim
                init_sim()
                settings_dict = {k: globals().get(k) for k in settings_keys}
                settings_panel = SettingsPanel(screen, settings_dict, theme)
                mode = "running"
            elif res == "cancel":
                mode = "running"
            elif res == "reset":
                # reinitialize sim
                init_sim()
                settings_dict = {k: globals().get(k) for k in settings_keys}
                settings_panel = SettingsPanel(screen, settings_dict, theme)
                mode = "running"
        elif mode == "sounds":
            res = volume_panel.handle_event(event)
            if res == "confirm":
                # 将 slider 的值写回字典
                for key, slider in volume_panel.sliders.items():
                    sound_volumes[key] = slider.value
                # 应用到 pygame mixer（关键步骤）
                for snd_name, snd in SOUNDS.items():
                    snd.set_volume(sound_volumes["global"] * sound_volumes[snd_name])
                # 恢复 simulation
                mode = "running"
                timer.start()

    # Update / Draw
    BG_COLOR   = (32, 32, 32) if dark_mode else (255, 255, 255)
    FG_COLOR   = (255, 255, 255) if dark_mode else (0, 0, 0)     # 文字主色
    PACK_COLOR = (200, 200, 200) if dark_mode else (0, 0, 0)
    screen.fill(BG_COLOR)
    BG_COLOR = DARK_BG if dark_mode else LIGHT_BG
    TEXT_COLOR = DARK_FG if dark_mode else LIGHT_FG

    # Simulation update only in running mode
    if mode == "running":
        # 每 5 帧记录一次数据，避免过于密集
        if pygame.time.get_ticks() % 5 == 0:
            for agent_type in ["rock", "paper", "scissors"]:
                chart_data[agent_type].append(counts[agent_type])
                # 限制数据点数量
                if len(chart_data[agent_type]) > MAX_CHART_POINTS:
                    chart_data[agent_type].pop(0)
            hp_data.append(avg_health)
            max_hp_data.append(max_health)
            divmod_data.append(div_mod(total_health, len(agents) - len(bombs)) if max_health != 0 else 0)
            if len(hp_data) > MAX_CHART_POINTS:
                hp_data.pop(0)
            if len(max_hp_data) > MAX_CHART_POINTS:
                max_hp_data.pop(0)
            if len(divmod_data) > MAX_CHART_POINTS:
                divmod_data.pop(0)

        # 生成新的回血包（保持数量）
        while len(healing_packs) < HEALING_PACKS:
            healing_packs.append(HealingPack())

        # 移动 & 画出 agents
        # --- 先移动 ---
        for agent in agents:
            agent.move()

        # --- 构建空间分区 grid ---
        grid = {}
        for agent in agents:
            cx = int(agent.x // CELL)
            cy = int(agent.y // CELL)
            if (cx, cy) not in grid:
                grid[(cx, cy)] = []
            grid[(cx, cy)].append(agent)

        # --- 再绘制 ---
        for agent in agents:
            if agent.type != "bomb":
                agent.draw(screen, health_font, FG_COLOR)


        # 画出回血包
        pack_color = (14, 214, 46) if dark_mode else (0, 162, 232)
        for pack in healing_packs:
            pygame.draw.circle(screen, pack_color, (int(pack.x), int(pack.y)), 4)

        # 碰撞检测：Agent vs Agent（扣血）
        # --- 使用空间分区的碰撞检测 ---
        to_remove = set()
        neighbors = [
            (-1,-1), (0,-1), (1,-1),
            (-1, 0), (0, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]

        checked_pairs = set()  # 避免重复检测(A,B) 和 (B,A)

        for (cx, cy), cell_agents in grid.items():
            for agent in cell_agents:

                for dx, dy in neighbors:
                    key = (cx + dx, cy + dy)
                    if key not in grid:
                        continue

                    for other in grid[key]:

                        if agent is other:
                            continue

                        # 防止重复
                        pair = tuple(sorted((id(agent), id(other))))
                        if pair in checked_pairs:
                            continue
                        checked_pairs.add(pair)

                        dx2 = other.x - agent.x
                        dy2 = other.y - agent.y
                        dist2 = dx2 * dx2 + dy2 * dy2
                        if dist2 >= _SQ2R:
                            continue

                        dist = math.sqrt(dist2)
                        if dist <= 0:
                            continue

                        # --- 与你原来完全一致的碰撞反应 ---
                        nx, ny = dx2 / dist, dy2 / dist
                        dvx = other.vx - agent.vx
                        dvy = other.vy - agent.vy
                        impact = dvx * nx + dvy * ny

                        if impact < 0:
                            agent.vx += impact * nx
                            agent.vy += impact * ny
                            other.vx -= impact * nx
                            other.vy -= impact * ny
                            total_collusions += 1

                        # 推开避免重叠
                        overlap = 2 * RADIUS - dist
                        agent.x -= nx * overlap / 2
                        agent.y -= ny * overlap / 2
                        other.x += nx * overlap / 2
                        other.y += ny * overlap / 2

                        # --- 战斗（完全照搬你原来的代码） ---
                        if agent.type == "bomb" or other.type == "bomb":
                            # 炸弹只做物理碰撞，不参与 RPS 战斗
                            continue
                        if agent.type != other.type:
                            if beats(agent.type, other.type):
                                agent.health -= DAMAGE_WIN + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                    OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                                other.health -= DAMAGE_LOSE + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                    OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                            elif beats(other.type, agent.type):
                                other.health -= DAMAGE_WIN + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                    OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                                agent.health -= DAMAGE_LOSE + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                    OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                            sound_snare.play()
                        else:
                            agent.health -= DAMAGE_INNER + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                            other.health -= DAMAGE_INNER + int((len(agents) >= MAX_AGENTS) * OVERFLOW_DAMAGE_BASE * \
                                OVERFLOW_MULTIPLIER ** abs(len(agents) - MAX_AGENTS))
                            sound_hihat.play()

                        # 检查死亡
                        if agent.health <= 0:
                            # sound_agent_destruction.play()
                            to_remove.add(agent)
                        if other.health <= 0:
                            # sound_agent_destruction.play()
                            to_remove.add(other)



        # 移除死亡 agent
        agents = [a for a in agents if a not in to_remove]

        # 拾取回血包
        for agent in agents[:]:
            for pack in healing_packs[:]:
                dist = math.hypot(agent.x - pack.x, agent.y - pack.y)
                if dist < RADIUS + 4:
                    if agent.type != "bomb":
                        agent.health += HEAL_AMOUNT
                        healing_packs.remove(pack)
                        sound_clap.play()
                    # 检查是否分裂（拾取后立即判断）
                    if agent.should_split():
                        # 分裂！
                        angle_step = 2 * math.pi / PIECES
                        new_agents = []
                        for k in range(PIECES):
                            angle = k * angle_step
                            vx = math.cos(angle) * SPEED
                            vy = math.sin(angle) * SPEED
                            new_health = math.ceil(agent.health / PIECES)
                            new_agent = Agent(x = agent.x, y = agent.y, health = new_health, type_ = agent.type)
                            new_agent.vx, new_agent.vy = vx, vy
                            new_agents.append(new_agent)
                        agents.remove(agent)
                        agents.extend(new_agents)
                        break  # 拾取后立即分裂，不再继续检测其他包

        # 再次检查所有 agent 是否因战斗后血量满足分裂条件
        # （避免战斗后血量变化但未触发分裂）
        agents_to_split = []
        for agent in agents:
            if agent.should_split():
                sound_cymbal.play()
                agents_to_split.append(agent)

        for agent in agents_to_split:
            if agent not in agents:  # 可能已被移除
                continue
            angle_step = 2 * math.pi / PIECES
            new_agents = []
            for k in range(PIECES):
                angle = k * angle_step
                vx = math.cos(angle) * SPEED
                vy = math.sin(angle) * SPEED
                new_health = math.floor(agent.health / PIECES)
                new_agent = Agent(x=agent.x, y=agent.y, health=new_health, type_ = agent.type)
                new_agent.vx, new_agent.vy = vx, vy
                new_agent.type = agent.type
                new_agents.append(new_agent)
            agents.remove(agent)
            agents.extend(new_agents)

        # update bombs
        for b in bombs[:]:
            remove_flag = b.update()
            # if exploding, kill agents within current radius (each frame)
            if b.exploding:
                # kill agents whose center inside radius
                for a in agents[:]:
                    if (a.x - b.x)**2 + (a.y - b.y)**2 <= (EXPLODE_RADIUS)**2 and a.type != "bomb":
                        try:
                            agents.remove(a)
                        except ValueError:
                            pass
                # remove bomb after growth finished
                if remove_flag:
                    try:
                        bombs.remove(b)
                        agents.remove(b)
                    except ValueError:
                        pass

        # ----------------- Draw bombs (drawn regardless of mode, but not updated when paused) -----------------
        for b in bombs:
            b.draw(screen)

    # HUD 显示统计
    hud_surface = pygame.Surface((190, 130), pygame.SRCALPHA)
    hud_surface.fill((240, 240, 240, 150))
    counts = {"rock": 0, "paper": 0, "scissors": 0}
    total_health = 0
    for agent in agents:
        if agent.type != "bomb":
            counts[agent.type] += 1
            total_health += agent.health
    avg_health = total_health / max(len(agents) - len(bombs), 1) if agents else 0
    max_health = max(agent.health for agent in agents if agent.type != "bomb")

    # hud
    hud = pygame.Surface((855 if current_language == 0 else 735, 135), pygame.SRCALPHA)
    resolution_hud = pygame.Surface((440, 135), pygame.SRCALPHA)
    
    if show_hud:
        # hud
        hud.fill((64, 64, 64, 190) if dark_mode else (235, 235, 235, 190))
        lines = [i18n.texts.get("Hud1.Line1", "Total Agents: {:3} (Rock: {:3}   Scissors: {:3}   Paper: {:3}   Time Bomb: {})")
                    .format(len(agents) - len(bombs), counts['rock'], counts['scissors'], counts['paper'], len(bombs)),
                (i18n.texts.get("Hud1.Line2", "Average (Max) health: {:.2f} ({:.0f})")
                    .format(avg_health, max_health)) if not _easter_egg_ else \
                        (i18n.texts.get("Hud1.Line21", "Average (Max) health: {:.2f} ({:.0f}) = {:.0f}/{:.0f} -> {:.0f} (mod 998244353)")
                        .replace("<>", "=")\
                        .format(avg_health, max_health, total_health, len(agents) - len(bombs), \
                            div_mod(total_health, max(len(agents) - len(bombs), 1), 998244353))),
                # i18n.texts.get("Hud1.Collusion", 
                # "Total collusions: {} ({:.2f} per second)").format(total_collusions, total_collusions * 1000 / timer.get_elapsed_time()),
                i18n.texts.get("Hud1.Line3", "Time elapsed: {}")
                    .format(timer.get_formatted_time()), 
                i18n.texts.get("Hud1.Line4", "It is currently: {}")
                    .format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))]
        icons = [icon_box_dark, icon_heart_dark, icon_timer_dark, icon_systemclock_dark] \
            if dark_mode else [icon_box_light, icon_heart_light, icon_timer_light, icon_systemclock_light]
        icon_y = [11, 40, 72, 103]
        icon_x = [10, 9, 10, 10]
        for i, line in enumerate(lines):
            hud.blit(hud_font.render(line, True, TEXT_COLOR), (40, (8 if current_language == 0 else 10) + i * 31))
            hud.blit(icons[i], (icon_x[i], icon_y[i]))
        screen.blit(hud, (15, 10))

        # resolution, fps & CPU/Mem usage
        resolution_hud.fill((64, 64, 64, 190) if dark_mode else (235, 235, 235, 190))
        sys_info = [
            i18n.texts.get("Hud2.Line1", "Resolution (FPS): {}x{} ({:.2f})")
                .format(W, H, clock.get_fps()),
            i18n.texts.get("Hud2.Line2", "RAM: {:.2f} MB")
                .format(this_process.memory_info().rss / 1048576),
            i18n.texts.get("Hud2.Line3", "CPU Usage: {:.1f}%").format(this_process.cpu_percent() / psutil.cpu_count()),
            i18n.texts.get("Hud2.Line4", "Volume: {:.0f}%").format(sound_volumes["global"] * 100)]
        sys_info_icon = [
            icon_resolution_dark if not _fullscreen_ else icon_fullscreen_dark, 
            icon_memory_dark, 
            icon_cpu_dark, 
            icon_volume_big_dark if sound_volumes["global"] >= 0.005 else icon_volume_mute_dark
            ] if dark_mode else [
                icon_resolution_light if not _fullscreen_ else icon_fullscreen_light, 
                icon_memory_light, 
                icon_cpu_light, 
                icon_volume_big_light if sound_volumes["global"] >= 0.005 else icon_volume_mute_light
            ]
        for i, line in enumerate(sys_info):
            resolution_hud.blit(hud_font.render(line, True, TEXT_COLOR), (40, (8 if current_language == 0 else 9) + i * 31))
            resolution_hud.blit(sys_info_icon[i], (10, 9 + i * 31))
        screen.blit(resolution_hud, (15, 160))

    # low fps warning
    if clock.get_fps() <= 12 and H >= 820:
        low_fps_warning = pygame.Surface((440, 45), pygame.SRCALPHA)
        low_fps_warning.fill((64, 64, 64, 190) if dark_mode else (235, 235, 235, 190))
        low_fps_warning.blit(
            hud_font.render(i18n.texts.get("LowFpsWarning", "Low FPS may cause visual uncomfort."), True, TEXT_COLOR), (40, 10))
        low_fps_warning.blit(icon_warning_dark if dark_mode else icon_warning_light, (10, 10))
        screen.blit(low_fps_warning, (15, 310) if show_hud else (15, 10))

    # Draw buttons only when the program is active
    if monitor.active:

        # draw settings button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), settings_button_rect, border_radius=12)
        txt = small_font.render(i18n.texts.get("UI.ButtonParameters", "Parameters"), True, \
            (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center=(settings_button_rect.centerx + 15, settings_button_rect.centery)))
        screen.blit(icon_parameters_dark if dark_mode else icon_parameters_light, 
                    (settings_button_rect.x + 18, settings_button_rect.y + 12))

        # draw about button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), about_button_rect, border_radius=12)
        txt = small_font.render(i18n.texts.get("UI.About", "About"), True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center=(about_button_rect.centerx + 15, about_button_rect.centery)))
        screen.blit(icon_about_dark if dark_mode else icon_about_light, (about_button_rect.x + 17, about_button_rect.y + 11))

        # draw hud button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), hud_button_rect, border_radius=12)
        txt = small_font.render(
            i18n.texts.get("UI.Infobox", "Infobox:") + (i18n.texts.get("UI.On","ON") if show_hud else i18n.texts.get("UI.Off","OFF")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center=(hud_button_rect.centerx+15, hud_button_rect.centery)))
        screen.blit(icon_infobox_dark if dark_mode else icon_infobox_light, (hud_button_rect.x + 18, hud_button_rect.y + 12))

        # draw sound settings button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), sounds_button_rect, border_radius = 12)
        txt = small_font.render(i18n.texts.get("UI.SoundFxSettings", "Sound Fx Settings"), True, \
            (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center=(sounds_button_rect.centerx + 15, sounds_button_rect.centery)))
        screen.blit(icon_slider_dark if dark_mode else icon_slider_light, (sounds_button_rect.x + 18, sounds_button_rect.y + 12))

        # 在绘制部分添加图表按钮
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), chart_button_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.Chart","Chart: ") + \
                (i18n.texts.get("UI.On","ON") if show_chart else i18n.texts.get("UI.Off","OFF")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center=(chart_button_rect.centerx + 15, chart_button_rect.centery)))
        screen.blit(icon_chart_dark if dark_mode else icon_chart_light, (chart_button_rect.x + 18, chart_button_rect.y + 13))

        # 深浅主题按钮
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), theme_button_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.Theme", "Theme: ") + \
                (i18n.texts.get("UI.Light","Light") if not dark_mode else i18n.texts.get("UI.Dark","Dark")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center = (theme_button_rect.centerx+15, theme_button_rect.centery)))
        screen.blit(icon_theme_dark if dark_mode else icon_theme_light, (theme_button_rect.x + 17, theme_button_rect.y + 13))

        # language
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), language_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.Language", "Language: English"), True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center = (language_rect.centerx+15, language_rect.centery)))
        screen.blit(icon_language_dark if dark_mode else icon_language_light, (language_rect.x + 18, language_rect.y + 13))

        # hp value on/off button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60,60,60), hp_value_button_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.HpValue", "Hp Display: ") + \
                (i18n.texts.get("UI.On","ON") if show_hp else i18n.texts.get("UI.Off","OFF")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center = (hp_value_button_rect.centerx+15, hp_value_button_rect.centery)))
        screen.blit(icon_heart_dark if dark_mode else icon_heart_light, (hp_value_button_rect.x + 18, hp_value_button_rect.y + 13))

        # fullscreen button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60, 60, 60), fullscreen_button_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.FullScreen", "Full Screen: ") + \
                (i18n.texts.get("UI.FullScreenOn","ON") if _fullscreen_ else i18n.texts.get("UI.FullScreenOff","OFF")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center = (fullscreen_button_rect.centerx+15, fullscreen_button_rect.centery)))
        if _fullscreen_:
            screen.blit(icon_fullscreen_dark if dark_mode else icon_fullscreen_light, 
                        (fullscreen_button_rect.x + 16, fullscreen_button_rect.y + 13))
        else:
            screen.blit(icon_resolution_dark if dark_mode else icon_resolution_light,
                        (fullscreen_button_rect.x + 16, fullscreen_button_rect.y + 13))

        # easter egg button
        pygame.draw.rect(screen, (175,175,175,135) if not dark_mode else (60, 60, 60), easter_egg_rect, border_radius = 12)
        txt = small_font.render(
            i18n.texts.get("UI.EasterEgg", "Easter Egg: ") + \
                (i18n.texts.get("UI.EasterEggOn","ON") if _easter_egg_ else i18n.texts.get("UI.EasterEggOff","OFF")),
            True, (10,10,10) if not dark_mode else (230,230,230))
        screen.blit(txt, txt.get_rect(center = (easter_egg_rect.centerx+15, easter_egg_rect.centery)))
        screen.blit(icon_easter_egg_dark if dark_mode else icon_easter_egg_light, (easter_egg_rect.x + 16, easter_egg_rect.y + 13))

    # 绘制图表（如果开启）
    if show_chart:
        draw_chart(screen, chart_data, chart_rect, theme)
        draw_hp_chart(screen, hp_data, max_hp_data, hp_chart_rect, theme)
        if _easter_egg_:
            draw_easteregg_chart(screen, divmod_data, easteregg_chart_rect, theme)
    
    # if in settings mode, overlay panel
    if mode == "settings":
        timer.pause()
        settings_panel.draw()
    
    # if in about mode, overlay panel
    if mode == "about":
        timer.pause()
        res = about_panel.handle_event(event)
        if res == "close":
            mode = "running"
            timer.start()
        about_panel.draw()

    # if in sounds mode, overlay panel
    if mode == "sounds":
        timer.pause()
        res = volume_panel.handle_event(event)
        if res == "confirm":
            mode = "running"
            timer.start()
        volume_panel.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
