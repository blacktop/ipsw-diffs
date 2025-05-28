## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

```diff

-3093.2.4.4.11
-  __TEXT.__text: 0x48500
+3093.23.0.0.0
+  __TEXT.__text: 0x485f8
   __TEXT.__auth_stubs: 0x1480
   __TEXT.__objc_methlist: 0x3100
   __TEXT.__const: 0x3f0
-  __TEXT.__cstring: 0x589a
-  __TEXT.__oslogstring: 0x1132
+  __TEXT.__cstring: 0x58dd
+  __TEXT.__oslogstring: 0x1174
   __TEXT.__gcc_except_tab: 0x8d8
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x2c3
   __TEXT.__unwind_info: 0x129c
   __TEXT.__objc_classname: 0x312
-  __TEXT.__objc_methname: 0x779f
+  __TEXT.__objc_methname: 0x77c9
   __TEXT.__objc_methtype: 0x12ff
   __TEXT.__objc_stubs: 0x5be0
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x1248
+  __DATA_CONST.__const: 0x1250
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2f18
   __DATA_CONST.__objc_selrefs: 0x2110
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__const: 0xba8
-  __AUTH_CONST.__cfstring: 0x4ca0
+  __AUTH_CONST.__cfstring: 0x4ce0
   __AUTH_CONST.__objc_const: 0xd38
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__objc_intobj: 0x1608
+  __AUTH_CONST.__objc_intobj: 0x1620
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xa50
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0x90
   __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x8c0
-  __DATA.__bss: 0x258
+  __DATA.__data: 0x8e0
+  __DATA.__bss: 0x238
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x2a0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1698
-  Symbols:   5473
-  CStrings:  2481
+  Functions: 1699
+  Symbols:   5477
+  CStrings:  2486
 
Symbols:
+ +[AXElement registerNotifications:withIdentifier:withHandler:].cold.4
+ ___35-[AXUIMLElement _currentMLElements]_block_invoke.305
+ ___62+[AXUIMLElement _queue_createMLElements:postDelegateCallback:]_block_invoke.322
+ ___block_literal_global.252
+ ___block_literal_global.257
+ ___block_literal_global.268
+ ___block_literal_global.289
+ ___block_literal_global.295
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.304
+ ___block_literal_global.307
+ ___block_literal_global.321
+ ___block_literal_global.326
+ ___block_literal_global.330
+ ___block_literal_global.333
+ ___block_literal_global.40
+ ___block_literal_global.512
+ ___block_literal_global.69
+ ___block_literal_global.91
+ _kAXAccessibilityTurnedOffNotification
+ _kAXXCAttributeScrollContentSize
- ___35-[AXUIMLElement _currentMLElements]_block_invoke.281
- ___62+[AXUIMLElement _queue_createMLElements:postDelegateCallback:]_block_invoke.298
- ___block_literal_global.228
- ___block_literal_global.233
- ___block_literal_global.244
- ___block_literal_global.265
- ___block_literal_global.271
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.280
- ___block_literal_global.283
- ___block_literal_global.297
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.323
- ___block_literal_global.509
- ___block_literal_global.68
- ___block_literal_global.90
CStrings:
+ "Must register for accessibility notifications on the main thread."
+ "T@\"NSString\",?,R,C"
+ "T^{__AXUIElement=},?,R,N"
+ "com.apple.accessibility.turned.off"
+ "kAXXCAttributeScrollContentSize"

```
