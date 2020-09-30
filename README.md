# DeviceManager

[![issues](https://img.shields.io/github/issues/chaya2z/DeviceManager)](https://github.com/chaya2z/DeviceManager/issues)
[![pull request](https://img.shields.io/github/issues-pr/chaya2z/DeviceManager)](https://github.com/chaya2z/DeviceManager/pulls)
[![License](https://img.shields.io/github/license/chaya2z/DeviceManager)](LICENSE)
![Python](https://img.shields.io/badge/Python-v3.8-blue)

Setting screen brightness application.

## Env

Python: version 3.8

## How to use

### 1. clone

Choose one method you like.

```shell script
# HTTPS
git clone https://github.com/chaya2z/DeviceManager.git

# SSH
git clone git@github.com:chaya2z/DeviceManager.git

# GitHub CLI
gh repo clone chaya2z/DeviceManager
```

### 2. Check your device

```shell script
ls /sys/class/backlight/
```

If return `intel_backlight` , skip 3.

### 3. Config path

Update `function/file_handling.py` .

```python
# line 9
# actual_brightness_pass = '/sys/class/backlight/intel_backlight/actual_brightness'
actual_brightness_pass = 'your backlight config file path'
```

```python
# line: 24
# brightness_pass = '/sys/class/backlight/intel_backlight/brightness'
brightness_pass = 'your backlight config file path'
```

### 4. Run

```
cd DeviceManager
sudo python3 script.py
```

## Option

Default scale-bar value: min 50, max 500. If you want to change them, please configure the following parts.

**warning:**
setting value of `from_` at 0, your screen is pitch-dark.

`gui_window.py`

```python
# gui_window.py
# line: 34 ~

        scale = tk.Scale(
            master=self.root,
            orient="horizontal",
            variable=GuiWindow.var,
            from_=50, # setting your like value of min brightness
            to=500, # setting your like value of max brightness
            length=500
        )
```

Confirm your device max brightness,

```shell script
cat /sys/class/backlight/intel_backlight/max_brightness
```

## License

This software is licensed under the MIT License.