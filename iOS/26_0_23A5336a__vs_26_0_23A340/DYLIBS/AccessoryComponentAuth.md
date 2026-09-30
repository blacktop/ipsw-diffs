## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

 1124.2.1.0.0
-  __TEXT.__text: 0x118e4
+  __TEXT.__text: 0x11a6c
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x280
   __TEXT.__const: 0x8c80
   __TEXT.__cstring: 0x1360
-  __TEXT.__oslogstring: 0x1000
+  __TEXT.__oslogstring: 0x102e
   __TEXT.__unwind_info: 0x3f8
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x8dd
+  __TEXT.__objc_methname: 0x8ee
   __TEXT.__objc_methtype: 0x215
-  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_stubs: 0x980
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x1460
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x288
+  __DATA_CONST.__objc_selrefs: 0x290
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x948
   __AUTH_CONST.__cfstring: 0x1380

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96208CF2-F390-3E2B-A82D-875CFAD59C67
+  UUID: A7CE91EF-D0CC-373A-A9D9-B0CCDA4B1F73
   Functions: 401
-  Symbols:   1762
-  CStrings:  607
+  Symbols:   1766
+  CStrings:  609
 
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
