## WatchConnectivity

> `/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity`

```diff

-221.0.0.0.0
-  __TEXT.__text: 0x29160
+222.0.0.0.0
+  __TEXT.__text: 0x29438
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x1f58
+  __TEXT.__objc_methlist: 0x1f80
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x340e
+  __TEXT.__cstring: 0x34d2
   __TEXT.__oslogstring: 0x23ae
   __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xaf0
   __TEXT.__objc_classname: 0x2c3
-  __TEXT.__objc_methname: 0x54f7
+  __TEXT.__objc_methname: 0x555c
   __TEXT.__objc_methtype: 0xaa8
-  __TEXT.__objc_stubs: 0x3b00
+  __TEXT.__objc_stubs: 0x3b40
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__const: 0x788
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_selrefs: 0x1268
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x10c0
-  __AUTH_CONST.__objc_const: 0x3d20
+  __AUTH_CONST.__objc_const: 0x3d30
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x1dc

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3064008-3FF4-3D01-89B1-52484085ABD1
-  Functions: 926
-  Symbols:   3195
-  CStrings:  1615
+  UUID: E9296FF2-09B9-363E-8E64-540E808C623B
+  Functions: 929
+  Symbols:   3204
+  CStrings:  1620
 
Symbols:
+ -[WCComplicationManager xpcManager:shouldWakeAppWithBundleID:completionHandler:]
+ -[WCPrivateXPCManager shouldWakeAppWithBundleID:completionHandler:]
+ ___27-[WCPrivateXPCManager init]_block_invoke.60
+ ___27-[WCPrivateXPCManager init]_block_invoke.60.cold.1
+ ___38-[WCPrivateXPCManager setupConnection]_block_invoke.68
+ ___80-[WCComplicationManager xpcManager:shouldWakeAppWithBundleID:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_literal_global.72
+ _objc_msgSend$shouldWakeAppWithBundleID:completionHandler:
+ _objc_msgSend$xpcManager:shouldWakeAppWithBundleID:completionHandler:
- ___27-[WCPrivateXPCManager init]_block_invoke.59
- ___27-[WCPrivateXPCManager init]_block_invoke.59.cold.1
- ___38-[WCPrivateXPCManager setupConnection]_block_invoke.67
- ___block_literal_global.71
CStrings:
+ "-[WCComplicationManager xpcManager:shouldWakeAppWithBundleID:completionHandler:]"
+ "-[WCComplicationManager xpcManager:shouldWakeAppWithBundleID:completionHandler:]_block_invoke"
+ "shouldWakeAppWithBundleID:completionHandler:"
+ "v20@?0B8@\"NSError\"12"
+ "xpcManager:shouldWakeAppWithBundleID:completionHandler:"

```
