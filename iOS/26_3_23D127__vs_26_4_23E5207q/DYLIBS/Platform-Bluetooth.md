## Platform-Bluetooth

> `/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`

```diff

-1139.82.1.0.0
-  __TEXT.__text: 0x4508
-  __TEXT.__auth_stubs: 0x430
+1147.100.12.0.0
+  __TEXT.__text: 0x4418
+  __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x2e3
   __TEXT.__oslogstring: 0x86d
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x118
   __TEXT.__objc_classname: 0xf7
   __TEXT.__objc_methname: 0x828
   __TEXT.__objc_methtype: 0x35d

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x6d0
   __AUTH.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E5896096-A4F3-3E28-9A59-D88949564417
-  Functions: 73
-  Symbols:   438
+  UUID: 03BDCEA3-2ABD-3060-AEC0-6D19A112FFF6
+  Functions: 74
+  Symbols:   435
   CStrings:  250
 
Symbols:
+ _OUTLINED_FUNCTION_2
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[_ACCBluetoothStatusComponent initWithUID:macAddr:name:forAccessoryUID:] : 228 -> 212
~ +[_ACCBluetoothStatusComponent createComponentFromDict:] : 240 -> 260
~ -[ACCPlatformBluetoothStatusAccessory initWithUID:] : 140 -> 132
~ -[ACCPlatformPluginBluetooth getAccessoryList] : 56 -> 64
~ -[ACCPlatformPluginBluetooth accessoryAttached:] : 708 -> 700
~ _logObjectForModule : 132 -> 116
~ __AttachToBTServer : 748 -> 716
~ -[ACCPlatformPluginBluetooth accessoryDetached:] : 880 -> 876
~ __BTGetAccessoryManager : 360 -> 336
~ __BTGetDevice : 980 -> 936
~ ___48-[ACCPlatformPluginBluetooth accessoryDetached:]_block_invoke : 500 -> 452
~ -[ACCPlatformPluginBluetooth pluginBTDevice:btAccessoryManager:btDevice:] : 696 -> 668
~ -[ACCPlatformPluginBluetooth unplugBTDevice:btAccessoryManager:btDevice:] : 672 -> 644
~ -[ACCPlatformPluginBluetooth startCheckingForUpdates:forAccessory:] : 792 -> 784
~ ___notifyComponentStatus : 424 -> 432
~ -[ACCPlatformPluginBluetooth stopCheckingForUpdates:forAccessory:] : 592 -> 580
~ -[ACCPlatformPluginBluetooth updateBTComponent:forAccessory:withEnabledState:] : 988 -> 1004
~ -[ACCPlatformPluginBluetooth iterateRegisteredComponentsForKnownAddresses:allOFF:] : 540 -> 564
~ -[ACCPlatformPluginBluetooth nameForMacAddress:] : 1256 -> 1184
~ -[ACCPlatformPluginBluetooth setBtEventQueue:] : 12 -> 64
~ -[ACCPlatformPluginBluetooth setAccessoryList:] : 12 -> 64
~ __sendBluetoothConnectionStatusNotification : 1208 -> 1260
~ __BTSessionCallback : 1436 -> 1336
~ __BTLocalDeviceCallback : 344 -> 328
~ __BTServiceCallback : 380 -> 372
~ __BTPostConnectionStatus : 168 -> 176
~ _OUTLINED_FUNCTION_0 : 24 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 24
+ _OUTLINED_FUNCTION_2
~ __sendBluetoothConnectionStatusNotification.cold.1 : 112 -> 56
~ _logObjectForModule.cold.1 : 144 -> 128

```
