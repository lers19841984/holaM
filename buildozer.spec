[app]
title = HolaMundoKivy
package.name = holamundo
package.domain = com.tuapp
source.dir = .
version = 1.0.0

requirements = 
    python==3.11.6,
    kivy==2.3.0,
    android==0.5

orientation = portrait
fullscreen = 0

# Android config
android.sdk = 34
android.ndk = 25.2.9519653
android.build_tools_version = 34.0.0
android.api = 34
android.minapi = 24
android.wakelock = 0
android.arch = arm64-v8a
android.accept_sdk_license = True

# Performance
p4a.branch = develop
p4a.optimizations = O3
p4a.enable_androidx = True

# Resources
icon.filename = icon.png
presplash.filename = icon.png
