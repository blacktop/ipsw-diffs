## DeviceDataResetXPCServiceWorker

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker`

```diff

-49.3.1.0.0
-  __TEXT.__text: 0x7778
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x1660
+54.0.0.0.0
+  __TEXT.__text: 0x78c8
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0x1064
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xfd7
+  __TEXT.__cstring: 0x1084
   __TEXT.__oslogstring: 0xf8d
   __TEXT.__objc_classname: 0x5f8
   __TEXT.__objc_methtype: 0x3bb
-  __TEXT.__objc_methname: 0x16e8
+  __TEXT.__objc_methname: 0x1758
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__cfstring: 0xcc0
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__cfstring: 0xe20
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x2a98
-  __DATA.__objc_selrefs: 0x6d0
+  __DATA.__objc_selrefs: 0x700
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BBA61979-06F1-32E8-8A70-E61A5A19EA2C
-  Functions: 316
-  Symbols:   298
-  CStrings:  722
+  UUID: 3E84B544-35AA-3E13-B6CD-AE5DCF7DA793
+  Functions: 319
+  Symbols:   302
+  CStrings:  750
 
Symbols:
+ _BiomeLibrary
+ _DDRDonateResetSignalComplete
+ _DDRDonateResetSignalStart
+ _OBJC_CLASS_$_BMDiscoverabilitySignals
CStrings:
+ "Discoverability"
+ "Signals"
+ "all-settings"
+ "brick-device"
+ "com.apple.devicedatareset.%@-reset-%@"
+ "complete"
+ "data-partition"
+ "initWithContentIdentifier:context:osBuild:userInfo:"
+ "network-settings"
+ "none"
+ "rapid-return-to-service"
+ "scene-understanding-data"
+ "sendEvent:"
+ "source"
+ "stringWithFormat:"
+ "unknown"

```
