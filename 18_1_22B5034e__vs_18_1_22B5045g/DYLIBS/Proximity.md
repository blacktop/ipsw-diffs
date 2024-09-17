## Proximity

> `/System/Library/PrivateFrameworks/Proximity.framework/Proximity`

```diff

-458.0.8.0.0
-  __TEXT.__text: 0x2df58
-  __TEXT.__auth_stubs: 0x920
+458.0.10.0.0
+  __TEXT.__text: 0x2e218
+  __TEXT.__auth_stubs: 0x940
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1a24
-  __TEXT.__gcc_except_tab: 0x2d78
-  __TEXT.__cstring: 0x26a1
+  __TEXT.__gcc_except_tab: 0x2d84
+  __TEXT.__cstring: 0x26c0
   __TEXT.__const: 0x864
   __TEXT.__oslogstring: 0x103b
-  __TEXT.__unwind_info: 0x14c8
+  __TEXT.__unwind_info: 0x14d8
   __TEXT.__objc_classname: 0x516
-  __TEXT.__objc_methname: 0x4006
-  __TEXT.__objc_methtype: 0x1720
-  __TEXT.__objc_stubs: 0x2e00
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x738
+  __TEXT.__objc_methname: 0x403a
+  __TEXT.__objc_methtype: 0x1723
+  __TEXT.__objc_stubs: 0x2e40
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x788
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda8
+  __DATA_CONST.__objc_selrefs: 0xdb8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x708
-  __AUTH_CONST.__cfstring: 0x25c0
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__const: 0x728
+  __AUTH_CONST.__cfstring: 0x25e0
   __AUTH_CONST.__objc_const: 0x72a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xaa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1064
-  Symbols:   1406
-  CStrings:  1499
+  Functions: 1068
+  Symbols:   1413
+  CStrings:  1502
 
Symbols:
+ _dispatch_semaphore_create
+ _dispatch_semaphore_wait
+ _dispatch_semaphore_signal
+ _OBJC_CLASS_$_NSBundle
+ _PRGetChipInfoAsync
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "getPowerStatsWithTimeout:reply:"
+ "v28@0:8B16@?<v@?@\"PRChipInfo\">20"
+ "getChipInfoSync:reply:"
+ "sendHelloWithTimeout:reply:"
+ "com.apple.secureelementservice"
+ "bundleIdentifier"
+ "mainBundle"
- "sendHelloSync:reply:"
- "getChipInfo:"
- "getPowerStatsSync:reply:"
- "v24@0:8@?<v@?@\"PRChipInfo\">16"

```
