## audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

```diff

-20.43.1.0.0
-  __TEXT.__text: 0x1a3600
-  __TEXT.__auth_stubs: 0x2510
-  __TEXT.__objc_stubs: 0xcda0
-  __TEXT.__objc_methlist: 0x55e8
-  __TEXT.__const: 0x38b0
-  __TEXT.__gcc_except_tab: 0x3068
-  __TEXT.__cstring: 0x271f3
-  __TEXT.__objc_methname: 0x12ae4
+20.45.2.0.0
+  __TEXT.__text: 0x1a4520
+  __TEXT.__auth_stubs: 0x2520
+  __TEXT.__objc_stubs: 0xcea0
+  __TEXT.__objc_methlist: 0x5648
+  __TEXT.__const: 0x38d0
+  __TEXT.__gcc_except_tab: 0x30a0
+  __TEXT.__cstring: 0x27553
+  __TEXT.__objc_methname: 0x12c71
   __TEXT.__objc_classname: 0x5fb
-  __TEXT.__objc_methtype: 0x2224
+  __TEXT.__objc_methtype: 0x228b
   __TEXT.__oslogstring: 0x876a
   __TEXT.__constg_swiftt: 0x1584
   __TEXT.__swift5_typeref: 0x186e

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__info_plist: 0x53d
-  __TEXT.__unwind_info: 0x35a8
+  __TEXT.__unwind_info: 0x35d0
   __TEXT.__eh_frame: 0x1ea0
-  __DATA_CONST.__auth_got: 0x1298
+  __DATA_CONST.__auth_got: 0x12a0
   __DATA_CONST.__got: 0x8e0
-  __DATA_CONST.__auth_ptr: 0x6b8
+  __DATA_CONST.__auth_ptr: 0x6c8
   __DATA_CONST.__const: 0xa558
   __DATA_CONST.__cfstring: 0x6e80
   __DATA_CONST.__objc_classlist: 0x1b8

   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xf838
-  __DATA.__objc_selrefs: 0x40b0
-  __DATA.__objc_ivar: 0xb64
+  __DATA.__objc_const: 0xf8d8
+  __DATA.__objc_selrefs: 0x4108
+  __DATA.__objc_ivar: 0xb70
   __DATA.__objc_data: 0x1b50
   __DATA.__data: 0x2e28
   __DATA.__bss: 0x66c0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5524
-  Symbols:   1015
-  CStrings:  3991
+  Functions: 5535
+  Symbols:   1016
+  CStrings:  4004
 
Symbols:
+ _CUPrintFlags32
CStrings:
+ "-[AADeviceManagerDaemon smartRoutingStateUpdated:ForDeviceIdentifier:]_block_invoke"
+ "-[BTCloudServicesXPCConnection cloudServicesClientActivate:completion:]"
+ "-[BTCloudServicesXPCConnection cloudServicesClientActivate:completion:]_block_invoke"
+ "-[BTCloudServicesXPCConnection fetchAAProxCardsInfoForDeviceWithAddress:completion:]_block_invoke_2"
+ "-[BTSmartRoutingDaemon getSmartRoutingStateForDeviceAddress:]_block_invoke"
+ "-[BTSmartRoutingWxDevice _setTipiAndRoutedStateFlags:]"
+ "AADeviceManagerDaemon shared instance %!@(MISSING)"
+ "Head Gestures Notification: Invalidating existing notification first"
+ "Purging Audio Accessory Zone data"
+ "Setting tipiAndRoutedState for Wx %!@(MISSING) %!@(MISSING) -> %!@(MISSING)"
+ "Tell delegate to remove local cache for AudioAccessoryZone data"
+ "Unable to read sound profile record because device is in beforeFirstUnlock state"
+ "aaDeviceRecords call failed because device is in beforeFirstUnlock state"
+ "aaProxCardsRecords call failed because device is in beforeFirstUnlock state"
+ "getSmartRoutingStateForDeviceAddress %!@(MISSING)"
+ "getSmartRoutingStateForDeviceAddress error: No SR Wx device"
+ "smartRoutingStateUpdated: No Audio Accessory Device found"
- "Purging Audio Accessory data"
- "Unable to read sound profile record because in device is in beforeFirstUnlock state"
- "aaDeviceRecords call failed because in device is in beforeFirstUnlock state"
- "aaProxCardsRecords call failed because in device is in beforeFirstUnlock state"

```
