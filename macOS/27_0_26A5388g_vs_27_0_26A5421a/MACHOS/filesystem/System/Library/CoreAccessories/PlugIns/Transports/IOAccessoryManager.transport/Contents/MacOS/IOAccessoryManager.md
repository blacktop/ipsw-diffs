## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/Contents/MacOS/IOAccessoryManager`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1210.0.0.501.1
-  __TEXT.__text: 0x46190
+1216.0.0.0.0
+  __TEXT.__text: 0x4640c
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_stubs: 0x4a80
-  __TEXT.__objc_methlist: 0x27d0
+  __TEXT.__objc_stubs: 0x4ae0
+  __TEXT.__objc_methlist: 0x27e8
   __TEXT.__const: 0x274
-  __TEXT.__cstring: 0x34bd
-  __TEXT.__oslogstring: 0xadf2
-  __TEXT.__objc_methname: 0x768f
+  __TEXT.__cstring: 0x34d9
+  __TEXT.__oslogstring: 0xae5a
+  __TEXT.__objc_methname: 0x76d1
   __TEXT.__objc_classname: 0x3dc
   __TEXT.__objc_methtype: 0xf28
   __TEXT.__gcc_except_tab: 0x77c
   __TEXT.__ustring: 0x146
   __TEXT.__unwind_info: 0xa20
-  __DATA_CONST.__const: 0x10f8
-  __DATA_CONST.__cfstring: 0x2da0
+  __DATA_CONST.__const: 0x1108
+  __DATA_CONST.__cfstring: 0x2dc0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x350
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4178
-  __DATA.__objc_selrefs: 0x1868
+  __DATA.__objc_selrefs: 0x1878
   __DATA.__objc_ivar: 0x3c0
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x6c4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 1343
-  Symbols:   2849
-  CStrings:  2592
+  Functions: 1345
+  Symbols:   2856
+  CStrings:  2596
 
Symbols:
+ -[ACCTransportIOAccessoryManager _invalidateAllAccessoryInfoFields]
+ -[ACCTransportIOAccessoryManager _unregisterBatteryNotifications]
+ GCC_except_table70
+ _ACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _kCFACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _objc_msgSend$_unregisterBatteryNotifications
+ _objc_msgSend$batteryIterator
+ _objc_msgSend$setBatteryIterator:
- GCC_except_table68
Functions:
~ _IOAccMgrNotifyEvent : 7888 -> 7728
~ -[ACCTransportIOAccessoryManager _registerForBatteryNotifications] : 344 -> 348
+ -[ACCTransportIOAccessoryManager _unregisterBatteryNotifications]
+ -[ACCTransportIOAccessoryManager _invalidateAllAccessoryInfoFields]
~ -[ACCTransportPluginIOAccessoryManager authStatusDidChange:forConnectionWithUUID:previousAuthStatus:authType:connectionIsAuthenticated:connectionWasAuthenticated:] : 1692 -> 1904
CStrings:
+ "BLEPairingAuthTimeoutValueS"
+ "Invalidating accessory info validity for manager %d to force inductiveDeviceType re-read"
+ "_invalidateAllAccessoryInfoFields"
+ "_unregisterBatteryNotifications"
+ "unregistering battery notifications for manager %d"
- "unregistering battery notifications"
```
