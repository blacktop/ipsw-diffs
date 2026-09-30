## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

```diff

-103.80.1.0.1
-  __TEXT.__text: 0x1175c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_stubs: 0x3c40
-  __TEXT.__objc_methlist: 0x1e30
-  __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x5f73
-  __TEXT.__oslogstring: 0x2598
-  __TEXT.__cstring: 0x1fac
-  __TEXT.__objc_classname: 0x437
-  __TEXT.__objc_methtype: 0x20de
-  __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0xc40
-  __DATA_CONST.__objc_classlist: 0xb0
+107.100.11.0.0
+  __TEXT.__text: 0x13cd4
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x4180
+  __TEXT.__objc_methlist: 0x2010
+  __TEXT.__cstring: 0x209e
+  __TEXT.__const: 0x48
+  __TEXT.__objc_methname: 0x64f9
+  __TEXT.__oslogstring: 0x273a
+  __TEXT.__objc_classname: 0x446
+  __TEXT.__objc_methtype: 0x20f1
+  __TEXT.__gcc_except_tab: 0x24
+  __TEXT.__unwind_info: 0x508
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__cfstring: 0xd00
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA.__objc_const: 0x3808
-  __DATA.__objc_selrefs: 0x1798
-  __DATA.__objc_ivar: 0x114
-  __DATA.__objc_data: 0x6e0
-  __DATA.__data: 0x978
-  __DATA.__bss: 0x78
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA.__objc_const: 0x3ae8
+  __DATA.__objc_selrefs: 0x1910
+  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_data: 0x730
+  __DATA.__data: 0x97c
+  __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI

   - /System/Library/PrivateFrameworks/SetupAssistantUI.framework/SetupAssistantUI
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
+  - /System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit
   - /System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AD6CE4F1-658B-3C7D-9201-7E93300812F4
-  Functions: 462
-  Symbols:   240
-  CStrings:  1672
+  UUID: A8A7FFF1-C538-38A3-A975-EC4581CC0734
+  Functions: 502
+  Symbols:   252
+  CStrings:  1773
 
Symbols:
+ _BSCopyDeviceTreeProperty
+ _CFDataGetBytes
+ _OBJC_CLASS_$_STStatusBarData
+ _OBJC_CLASS_$_STStatusBarDataBatteryEntry
+ _OBJC_CLASS_$_STStatusBarDataWifiEntry
+ _OBJC_CLASS_$_STUIStatusBar
+ _STStatusBarDataEntryMainBatteryKey
+ _STStatusBarDataEntryWifiKey
+ _UIDeviceBatteryLevelDidChangeNotification
+ _UIDeviceBatteryStateDidChangeNotification
+ _UIEdgeInsetsZero
+ _UIWindowLevelStatusBar
+ _WFInterfaceLinkQualityChangedNotification
+ _WFInterfaceNetworkChangedNotification
+ _kWFInterfaceLinkQualityKey
+ _kWFInterfaceNetworkKey
+ _kWFInterfacePreviousNetworkKey
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _OBJC_CLASS_$_AWAttentionAwarenessClient
- _OBJC_CLASS_$_AWAttentionAwarenessConfiguration
- _objc_claimAutoreleasedReturnValue
- _objc_copyWeak
- _objc_initWeak
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x8
CStrings:
+ "%ld%%"
+ "%{public}s: [DisplayManager] Auto-dim timer fired, dimming display"
+ "%{public}s: [DisplayManager] No assertion change needed (preventIdleSleep=%d, hasAssertion=%d, reasons=%@)"
+ "%{public}s: [StatusBar] Battery changed (capacity: %ld%% -> %ld%%, state: %d -> %d)"
+ "%{public}s: [StatusBar] Battery state changed, updating status bar"
+ "%{public}s: [StatusBar] Getting WiFi entry - isConnected: %{public}@, currentNetwork: %{public}@"
+ "%{public}s: [StatusBar] Initializing with WiFi manager: %{public}@"
+ "%{public}s: [StatusBar] Link quality changed - scaledRSSI: %.3f"
+ "%{public}s: [StatusBar] No changes - skipping UI update"
+ "%{public}s: [StatusBar] Performing initial status bar update"
+ "%{public}s: [StatusBar] Registered for WiFiKit notifications"
+ "%{public}s: [StatusBar] Starting monitoring"
+ "%{public}s: [StatusBar] Stopping monitoring"
+ "%{public}s: [StatusBar] Throttling link quality update - only %.1f seconds since last (minimum: 5.0 seconds)"
+ "%{public}s: [StatusBar] WiFi changed (bars: %ld -> %ld, connected: %{public}@ -> %{public}@)"
+ "%{public}s: [StatusBar] WiFi connected - SSID: %{public}@, scaledRSSI: %.3f, signalBars: %ld"
+ "%{public}s: [StatusBar] WiFi disconnected - showing 0 bars"
+ "%{public}s: [StatusBar] WiFi network connected or changed: %{public}@"
+ "%{public}s: [StatusBar] WiFi network disconnected (previous: %{public}@)"
+ "(none)"
+ "-[DisplayManager _autoDimTimerFired]"
+ "-[DisplayManager _initIdleSleep]"
+ "-[StatusBar batteryDidChange:]"
+ "-[StatusBar getBatteryEntry:]"
+ "-[StatusBar getWiFiEntry:]"
+ "-[StatusBar initWithWindowScene:mainWindow:wifiManager:]"
+ "-[StatusBar linkQualityChanged:]"
+ "-[StatusBar networkChanged:]"
+ "-[StatusBar startMonitoring]"
+ "-[StatusBar stopMonitoring]"
+ "-[StatusBar updateStatusBarData]"
+ "2"
+ "@\"STUIStatusBar\""
+ "@\"StatusBar\""
+ "@\"WFNetworkScanRecord\""
+ "@24@0:8^B16"
+ "IODeviceTree:/product"
+ "NO"
+ "StatusBar"
+ "T@\"NSMutableSet\",&,N,V_preventIdleSleepReasons"
+ "T@\"NSTimer\",&,N,V_autoDimTimer"
+ "T@\"STUIStatusBar\",&,N,V_statusBar"
+ "T@\"StatusBar\",&,N,V_statusBarView"
+ "T@\"UIWindow\",&,N,V_statusBarWindow"
+ "T@\"UIWindow\",W,N,V_mainWindow"
+ "T@\"WFNetworkListController\",W,N,V_wifiManager"
+ "T@\"WFNetworkScanRecord\",&,N,V_currentNetwork"
+ "TB,N,V_lastConnectionStatus"
+ "Td,N,V_lastLinkQualityUpdateTime"
+ "Tf,N,V_currentScaledRSSI"
+ "Tq,N,V_lastBatteryCapacity"
+ "Tq,N,V_lastBatteryState"
+ "Tq,N,V_lastSignalBars"
+ "YES"
+ "_autoDimTimer"
+ "_autoDimTimerFired"
+ "_currentNetwork"
+ "_currentScaledRSSI"
+ "_initIdleSleep"
+ "_lastBatteryCapacity"
+ "_lastBatteryState"
+ "_lastConnectionStatus"
+ "_lastLinkQualityUpdateTime"
+ "_lastSignalBars"
+ "_mainWindow"
+ "_preventIdleSleepReasons"
+ "_startAutoDimTimerIfNeeded"
+ "_statusBar"
+ "_statusBarView"
+ "_statusBarWindow"
+ "_stopAutoDimTimer"
+ "autoDimTimer"
+ "batteryDidChange:"
+ "batteryLevel"
+ "batteryState"
+ "constraintEqualToAnchor:constant:"
+ "currentNetwork"
+ "currentScaledRSSI"
+ "d24@0:8@16"
+ "dataByReplacingEntry:forKey:"
+ "date"
+ "dynamicIslandBottom:"
+ "entryWithCapacity:state:saverMode:prominentlyShowsDetailString:detailString:"
+ "entryWithType:status:lowDataMode:rawValue:displayValue:displayRawValue:"
+ "f"
+ "f16@0:8"
+ "getBatteryEntry:"
+ "getWiFiEntry:"
+ "initWithStyle:"
+ "initWithWindowScene:mainWindow:wifiManager:"
+ "island-notch-location"
+ "lastBatteryCapacity"
+ "lastBatteryState"
+ "lastConnectionStatus"
+ "lastLinkQualityUpdateTime"
+ "lastSignalBars"
+ "linkQualityChanged:"
+ "mainWindow"
+ "networkChanged:"
+ "nil"
+ "present"
+ "preventIdleSleepReasons"
+ "removeObserver:name:object:"
+ "resetAutoDimTimerAndUndim:"
+ "safeAreaInsets"
+ "scale"
+ "scaledRssi"
+ "screen"
+ "sendEvent:"
+ "setAutoDimTimer:"
+ "setBatteryMonitoringEnabled:"
+ "setCurrentNetwork:"
+ "setCurrentScaledRSSI:"
+ "setHidden:"
+ "setLastBatteryCapacity:"
+ "setLastBatteryState:"
+ "setLastConnectionStatus:"
+ "setLastLinkQualityUpdateTime:"
+ "setLastSignalBars:"
+ "setMainWindow:"
+ "setPreventIdleSleepReasons:"
+ "setStatusBar:"
+ "setStatusBarView:"
+ "setStatusBarWindow:"
+ "setTargetScreen:"
+ "setUserInteractionEnabled:"
+ "setWindowLevel:"
+ "setupStatusBarForWindowScene:"
+ "ssid"
+ "startMonitoring"
+ "statusBar"
+ "statusBarView"
+ "statusBarWindow"
+ "stopMonitoring"
+ "timeIntervalSince1970"
+ "traitCollection"
+ "updateStatusBarData"
+ "updateWithData:"
+ "userInterfaceStyle"
- "%{public}s: [DisplayManager] Adding idle timer disabled reason: %@"
- "%{public}s: [DisplayManager] Attempting to set idle timer disabled to %d"
- "%{public}s: [DisplayManager] Could not resume AttentionAwareness on undim: %@"
- "%{public}s: [DisplayManager] Could not suspend Attentionawareness on dim: %@"
- "%{public}s: [DisplayManager] Dimming for idle"
- "%{public}s: [DisplayManager] Ignoring request since idle timer disabled reason was not specified…"
- "%{public}s: [DisplayManager] Removing idle timer disabled reason: %@"
- "%{public}s: [DisplayManager] Reset idle for event %@"
- "%{public}s: [DisplayManager] Resetting idle timer and undim %d"
- "%{public}s: [DisplayManager] Setting a new attention awareness configuration with timeout: %f"
- "%{public}s: [DisplayManager] Unable to set configuration and reset attention lost timeout, error: %@"
- "%{public}s: [DisplayManager] What is TapToWakeGesture? Is it a thing on iOS?"
- "-[DisplayManager enableIdleSleep]"
- "-[DisplayManager init]_block_invoke"
- "-[DisplayManager resetIdleTimerAndUndim:]"
- "-[DisplayManager setIdleTimerDisabled:forReason:]"
- "@\"AWAttentionAwarenessClient\""
- "@24@0:8d16"
- "DRIdleTimer"
- "T@\"AWAttentionAwarenessClient\",&,N,V_attentionAwarenessClient"
- "T@\"NSMutableSet\",&,N,V_idleTimerDisabledReasons"
- "_additionalSafeAreaInsets"
- "_attentionAwarenessClient"
- "_idleTimerDisabledReasons"
- "attentionAwarenessClient"
- "configurationWithAttentionLostTimeout:"
- "containsObject:"
- "enableIdleSleep"
- "eventMask"
- "idleTimerDisabledReasons"
- "initWithCapacity:"
- "resetIdleTimerAndUndim:"
- "resumeWithError:"
- "setAttentionAwarenessClient:"
- "setAttentionLostTimeout:"
- "setConfiguration:shouldReset:"
- "setConfiguration:shouldReset:error:"
- "setEventHandlerWithQueue:block:"
- "setEventMask:"
- "setIdleTimerDisabled:forReason:"
- "setIdleTimerDisabledReasons:"
- "suspendWithError:"
- "v16@?0@\"AWAttentionEvent\"8"
- "{UIEdgeInsets=dddd}16@0:8"

```
