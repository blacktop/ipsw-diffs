## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`

```diff

-1210.0.0.502.1
-  __TEXT.__text: 0x5d488
-  __TEXT.__objc_methlist: 0x2f7c
+1216.0.0.0.0
+  __TEXT.__text: 0x5d73c
+  __TEXT.__objc_methlist: 0x2f94
   __TEXT.__const: 0x368
-  __TEXT.__cstring: 0x5fde
-  __TEXT.__oslogstring: 0xbc54
+  __TEXT.__cstring: 0x5ffa
+  __TEXT.__oslogstring: 0xbcbc
   __TEXT.__gcc_except_tab: 0x8f4
   __TEXT.__ustring: 0x146
   __TEXT.__unwind_info: 0xec8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xef8
+  __DATA_CONST.__const: 0xf08
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f00
+  __DATA_CONST.__objc_selrefs: 0x1f10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x158
   __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x45a0
+  __AUTH_CONST.__cfstring: 0x45c0
   __AUTH_CONST.__objc_const: 0x4d10
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xc0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 1948
-  Symbols:   3608
-  CStrings:  1708
+  Functions: 1950
+  Symbols:   3615
+  CStrings:  1710
 
Symbols:
+ -[ACCTransportIOAccessoryManager _invalidateAllAccessoryInfoFields]
+ -[ACCTransportIOAccessoryManager _unregisterBatteryNotifications]
+ GCC_except_table64
+ _ACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _kCFACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _objc_msgSend$_unregisterBatteryNotifications
+ _objc_msgSend$batteryIterator
+ _objc_msgSend$setBatteryIterator:
- GCC_except_table62
Functions:
~ _IOAccMgrNotifyEvent : 7560 -> 7404
~ _OUTLINED_FUNCTION_20 : 12 -> 20
~ -[ACCTransportIOAccessoryManager _registerForBatteryNotifications] : 340 -> 344
+ -[ACCTransportIOAccessoryManager _unregisterBatteryNotifications]
+ -[ACCTransportIOAccessoryManager _invalidateAllAccessoryInfoFields]
~ -[ACCTransportPluginIOAccessoryManager authStatusDidChange:forConnectionWithUUID:previousAuthStatus:authType:connectionIsAuthenticated:connectionWasAuthenticated:] : 1644 -> 1852
~ _OUTLINED_FUNCTION_8 : 8 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 28
~ _OUTLINED_FUNCTION_10 : 16 -> 8
~ _OUTLINED_FUNCTION_11 : 28 -> 16
~ _OUTLINED_FUNCTION_21 : 20 -> 12
~ _LibSer_SEPControl_Deserialize : 160 -> 200
~ _LibSer_SEPControlResponse_Deserialize : 64 -> 88
CStrings:
+ "BLEPairingAuthTimeoutValueS"
+ "Invalidating accessory info validity for manager %d to force inductiveDeviceType re-read"
+ "unregistering battery notifications for manager %d"
- "unregistering battery notifications"
```
