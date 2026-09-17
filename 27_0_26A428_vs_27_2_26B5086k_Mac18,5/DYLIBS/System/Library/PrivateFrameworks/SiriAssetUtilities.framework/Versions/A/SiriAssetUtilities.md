## SiriAssetUtilities

> `/System/Library/PrivateFrameworks/SiriAssetUtilities.framework/Versions/A/SiriAssetUtilities`

```diff

-3600.77.1.0.0
-  __TEXT.__text: 0x10204
-  __TEXT.__objc_methlist: 0xd28
+3605.11.1.0.0
+  __TEXT.__text: 0x1041c
+  __TEXT.__objc_methlist: 0xd30
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__cstring: 0x1b58
+  __TEXT.__cstring: 0x1bab
   __TEXT.__oslogstring: 0x231e
   __TEXT.__unwind_info: 0x610
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x710
-  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__cfstring: 0x5c0
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 366
-  Symbols:   951
-  CStrings:  312
+  Functions: 367
+  Symbols:   957
+  CStrings:  317
 
Symbols:
+ +[SAUCommonUtilities bundle]
+ _OBJC_CLASS_$_NSBundle
+ _UAFFaultCapture
+ _kUAFABCXPCFallback
+ _objc_msgSend$bundleForClass:
+ bundle.sSAUBundle
Functions:
+ +[SAUCommonUtilities bundle]
~ -[SAUXPCService operationWithConfig:completion:] : 492 -> 552
~ -[SAUXPCService lockLatestAtomicInstance:atomicInstance:completion:] : 456 -> 516
~ -[SAUXPCService subscriptions:subscriber:user:completion:] : 12 -> 264
~ -[SAUXPCService markAssetsExpired:completion:] : 420 -> 488
CStrings:
+ "lockLatestAtomicInstance"
+ "markAssetsExpired"
+ "operationWithConfig"
+ "proxy"
+ "subscriptions"
```
