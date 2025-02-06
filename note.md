User: 如何获取安卓应用的appPackage和appActivity
Kimi: 获取安卓应用的 `appPackage` 和 `appActivity` 是使用 Appium 进行自动化测试时的关键步骤。以下是几种常用的方法：

### 方法一：通过命令行获取
1. **连接设备并打开应用**：确保设备通过 USB 连接电脑，并开启开发者模式和 USB 调试[^9^]。
2. **运行命令获取信息**：
   - 打开命令行工具，输入以下命令：
     ```bash
     adb shell dumpsys window windows | findstr mCurrentFocus
     ```
   - 输出结果中，`mCurrentFocus` 后的字符串包含了 `appPackage` 和 `appActivity`[^9^][^18^]。例如：
     ```
     mCurrentFocus=Window{... u0 com.example.app/com.example.app.MainActivity}
     ```
     其中，`com.example.app` 是 `appPackage`，`com.example.app.MainActivity` 是 `appActivity`。

### 方法二：通过 `adb logcat` 获取
1. **打开应用**：在设备上打开目标应用[^10^][^18^]。
2. **运行命令并查看日志**：
   - 输入以下命令：
     ```bash
     adb logcat ActivityManager:I *:S
     ```
   - 对应用进行操作，日志中会显示类似以下内容：
     ```
     START u0 {act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.example.app/.MainActivity}
     ```
     其中，`com.example.app` 是 `appPackage`，`.MainActivity` 是 `appActivity`[^18^]。

### 方法三：通过 `aapt` 工具获取
1. **获取 APK 文件**：确保你有目标应用的 APK 文件[^10^][^13^]。
2. **运行命令**：
   - 在命令行中输入以下命令：
     ```bash
     aapt dump badging path/to/your/app.apk | findstr package
     ```
   - 输出结果中会显示类似以下内容：
     ```
     package: name='com.example.app' versionCode='1' versionName='1.0'
     launchable-activity: name='com.example.app.MainActivity'
     ```
     其中，`com.example.app` 是 `appPackage`，`com.example.app.MainActivity` 是 `appActivity`[^10^][^13^]。

### 方法四：通过 Appium Desktop 或 Inspector 获取
1. **使用 Appium Desktop**：
   - 打开 Appium Desktop，点击“Desired Capabilities”选项卡[^17^]。
   - 在“Android”选项卡中输入 APK 文件路径，点击“Start Session”。
   - Appium 会自动解析 APK 文件并显示 `appPackage` 和 `appActivity`[^17^]。

2. **使用 Appium Inspector**：
   - 启动 Appium Inspector，连接到设备并启动目标应用[^17^]。
   - 在 Inspector 窗口的“Capabilities”选项卡中查看 `appPackage` 和 `appActivity`[^17^]。

### 方法五：通过解压 APK 文件获取
1. **解压 APK 文件**：使用解压工具（如 7-Zip）解压 APK 文件[^16^]。
2. **查看 `AndroidManifest.xml` 文件**：
   - 打开解压后的 `AndroidManifest.xml` 文件，使用文本编辑器（如 Notepad++）查看内容[^16^]。
   - 搜索 `<manifest>` 标签获取 `appPackage`，搜索 `<activity>` 标签获取 `appActivity`[^16^]。

以上方法可以根据你的具体需求和环境选择使用，推荐优先尝试方法一和方法二，因为它们简单且高效。