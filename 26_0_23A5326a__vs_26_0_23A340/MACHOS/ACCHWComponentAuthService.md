## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-1124.0.6.0.0
-  __TEXT.__text: 0x11114
+1124.2.1.0.0
+  __TEXT.__text: 0x1129c
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x9a0
+  __TEXT.__objc_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x8c38
   __TEXT.__cstring: 0x1313
   __TEXT.__objc_classname: 0x9e
-  __TEXT.__objc_methname: 0xaa4
+  __TEXT.__objc_methname: 0xab5
   __TEXT.__objc_methtype: 0x2ee
-  __TEXT.__oslogstring: 0xf16
+  __TEXT.__oslogstring: 0xf44
   __TEXT.__unwind_info: 0x3e8
   __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0xd0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_selrefs: 0x368
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 86FD903A-FC24-3223-87B8-9AEE5A380AF0
+  UUID: 580F910E-E602-3C10-BDB6-5F4CA05338C3
   Functions: 394
-  Symbols:   2447
-  CStrings:  647
+  Symbols:   2450
+  CStrings:  649
 
Symbols:
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.23
+ _objc_msgSend$batteryCode
+ _objc_msgSend$getBytes:length:
Functions:
~ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:] : 9324 -> 9656
~ -[ACCHWComponentAuthService _verifyBatteryMatch:outputBatteryCode:] : 544 -> 604
CStrings:
+ "(moduleType=%d) cpSetBatteryCode failed: 0x%x"
+ "getBytes:length:"

```
