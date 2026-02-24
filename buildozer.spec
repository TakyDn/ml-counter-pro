[app]

title = ML COUNTER PRO
package.name = mlcounterpro
package.domain = org.taky

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# ===== ANDROID CONFIG ESTÁVEL =====
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
