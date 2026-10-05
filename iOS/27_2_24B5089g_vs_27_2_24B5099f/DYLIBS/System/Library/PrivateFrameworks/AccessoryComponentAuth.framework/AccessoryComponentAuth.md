## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

-1219.40.7.0.0
-  __TEXT.__text: 0x12a54
-  __TEXT.__objc_methlist: 0x568
+1219.40.10.502.1
+  __TEXT.__text: 0x12aa8
+  __TEXT.__objc_methlist: 0x5d0
   __TEXT.__const: 0xd730
   __TEXT.__cstring: 0x15c9
   __TEXT.__oslogstring: 0x12ca
   __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__unwind_info: 0x6a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4b8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0xe0
   __AUTH_CONST.__const: 0xc88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 497
-  Symbols:   1514
+  Functions: 506
+  Symbols:   1523
   CStrings:  353
 
Symbols:
+ -[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateLASWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService signRCAMChallenge:completionHandler:]
+ -[ACCHWComponentAuthService signVeridianChallenge:completionHandler:]
+ GCC_except_table79
- GCC_except_table72
```
