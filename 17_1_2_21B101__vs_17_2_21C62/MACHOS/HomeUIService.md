## HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

-825.2.8.1.1
-  __TEXT.__text: 0x5cb54
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0xdb40
+841.3.9.1.1
+  __TEXT.__text: 0x5cd50
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0xdb20
   __TEXT.__objc_methlist: 0x54c0
-  __TEXT.__objc_methname: 0x13d60
-  __TEXT.__cstring: 0x7289
-  __TEXT.__objc_classname: 0x1314
-  __TEXT.__objc_methtype: 0x3a3b
+  __TEXT.__objc_methname: 0x13d98
+  __TEXT.__cstring: 0x73dc
+  __TEXT.__objc_classname: 0x12f7
+  __TEXT.__objc_methtype: 0x3960
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x5c77
+  __TEXT.__oslogstring: 0x5cf0
   __TEXT.__gcc_except_tab: 0x858
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x1680
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x29f0
-  __DATA_CONST.__cfstring: 0x3800
+  __TEXT.__unwind_info: 0x16a0
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x2a58
+  __DATA_CONST.__cfstring: 0x3840
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x198
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xc48
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0xef40
-  __DATA.__objc_selrefs: 0x3e98
+  __DATA.__objc_const: 0xef48
+  __DATA.__objc_selrefs: 0x3ea8
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x890
+  __DATA.__objc_classrefs: 0x898
   __DATA.__objc_superrefs: 0x320
-  __DATA.__objc_ivar: 0x5f0
+  __DATA.__objc_ivar: 0x5fc
   __DATA.__objc_data: 0x22b0
-  __DATA.__data: 0x1320
+  __DATA.__data: 0x12c0
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/Home.framework/Home
   - /System/Library/PrivateFrameworks/HomeRecommendationEngine.framework/HomeRecommendationEngine
   - /System/Library/PrivateFrameworks/HomeUI.framework/HomeUI

   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
-  - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/NetAppsUtilitiesUI.framework/NetAppsUtilitiesUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6401EB6F-3257-3E50-8691-5958D0F0E256
-  Functions: 2264
-  Symbols:   475
-  CStrings:  5061
+  UUID: 3ECC6A90-9E2E-32B9-ACF9-245372202FE6
+  Functions: 2272
+  Symbols:   464
+  CStrings:  5074
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _OBJC_CLASS_$_CBController
+ _OBJC_CLASS_$_CWFInterface
- _BluetoothAvailabilityChangedNotification
- _BluetoothPowerChangedNotification
- _CFRelease
- _CFRunLoopGetCurrent
- _OBJC_CLASS_$_BluetoothManager
- _WiFiDeviceClientGetPower
- _WiFiDeviceClientRegisterPowerCallback
- _WiFiManagerClientCopyDevices
- _WiFiManagerClientCreate
- _WiFiManagerClientScheduleWithRunLoop
- _WiFiManagerClientSetPower
- _WiFiManagerClientUnscheduleFromRunLoop
- _kCFAllocatorDefault
- _kCFRunLoopDefaultMode
CStrings:
+ "\a"
+ "\"\x11"
+ "%s failed to get bluetooth powerState: %@"
+ "%s failed to set bluetooth powerState: %@"
+ "%s failed to set wifi powerState: %@"
+ "-[HSNetworkInterfaceManager _setBluetoothPowerState:]_block_invoke"
+ "-[HSNetworkInterfaceManager _setWiFiPowerState:]"
+ "-[HSNetworkInterfaceManager _updateBluetoothInterfaceStatusWithCompletion:]_block_invoke"
+ "/Library/Managed Preferences/mobile/com.apple.homed.plist"
+ "@\"CBController\""
+ "@\"CWFInterface\""
+ "@24@0:8B16B20"
+ "MatteriPhoneOnlyPairing"
+ "MatteriPhoneOnlyPairingEnabled"
+ "T@\"CBController\",&,N,V_bluetoothController"
+ "T@\"CWFInterface\",&,N,V_wifiInterface"
+ "T@\"UIViewController\",W,N,V_alertHostViewController"
+ "TQ,N,V_bluetoothInterfaceStatus"
+ "TQ,R,N,V_wiFiInterfaceStatus"
+ "_alertBaseLocalizationKeyForRequestBluetooth:Wifi:"
+ "_alertHostViewController"
+ "_alertLocalizedDescriptionForRequestBluetooth:Wifi:"
+ "_alertLocalizedTitleForRequestBluetooth:Wifi:"
+ "_bluetoothController"
+ "_bluetoothInterfaceStatus"
+ "_updateAlertForBluetooth:Wifi:"
+ "_updateBluetoothInterfaceStatusWithCompletion:"
+ "_wiFiInterfaceStatus"
+ "_wifiInterface"
+ "activate"
+ "alertHostViewController"
+ "bluetoothController"
+ "checkNetworkStatusAndShowAlertIfNeededForBluetooth:Wifi:"
+ "getPowerStateWithCompletion:"
+ "hasOptedToHH2"
+ "initWithAlertHostViewController:"
+ "powerOn"
+ "setAlertHostViewController:"
+ "setBluetoothController:"
+ "setBluetoothInterfaceStatus:"
+ "setPower:error:"
+ "setPowerState:completion:"
+ "setWifiInterface:"
+ "v24@?0q8@\"NSError\"16"
+ "wifiInterface"
- "@\"<HSNetworkInterfaceManagerDelegate>\""
- "@32@0:8Q16Q24"
- "HSNetworkInterfaceManagerDelegate"
- "T@\"<HSNetworkInterfaceManagerDelegate>\",W,N,V_delegate"
- "T^{__WiFiDeviceClient=},N,V_wiFiDevice"
- "T^{__WiFiManagerClient=},N,V_wiFiManager"
- "^{__WiFiDeviceClient=}"
- "^{__WiFiDeviceClient=}16@0:8"
- "^{__WiFiManagerClient=}"
- "^{__WiFiManagerClient=}16@0:8"
- "_alertBaseLocalizationKeyForBluetoothInterfaceStatus:wiFiInterfaceStatus:"
- "_alertLocalizedDescriptionForBluetoothInterfaceStatus:wiFiInterfaceStatus:"
- "_alertLocalizedTitleForBluetoothInterfaceStatus:wiFiInterfaceStatus:"
- "_handleBluetoothManagerStateChange:"
- "_registerForBluetoothNotifications"
- "_registerForWiFiNotifications"
- "_unregisterForBluetoothNotifications"
- "_unregisterForWiFiNotifications"
- "_updateBluetoothAndWiFiAlert"
- "_wiFiDevice"
- "_wiFiManager"
- "available"
- "enabled"
- "networkInterfaceManager:didUpdateBluetoothInterfaceStatus:"
- "networkInterfaceManager:didUpdateWiFiInterfaceStatus:"
- "setWiFiDevice:"
- "setWiFiManager:"
- "startObservingInterfaceChanges"
- "stopObservingInterfaceChanges"
- "v24@0:8^{__WiFiDeviceClient=}16"
- "v24@0:8^{__WiFiManagerClient=}16"
- "v32@0:8@\"HSNetworkInterfaceManager\"16Q24"
- "wiFiDevice"
- "wiFiManager"
- "\x81"

```
