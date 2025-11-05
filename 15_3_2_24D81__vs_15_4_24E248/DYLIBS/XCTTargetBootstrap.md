## XCTTargetBootstrap

> `/System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/Versions/A/XCTTargetBootstrap`

```diff

-23196.3.0.0.0
-  __TEXT.__text: 0x222c
+23790.0.0.0.0
+  __TEXT.__text: 0x2310
   __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x154
+  __TEXT.__objc_methlist: 0x310
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__cstring: 0x337
   __TEXT.__oslogstring: 0x3c4
-  __TEXT.__unwind_info: 0x130
+  __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0x132
   __TEXT.__objc_methname: 0x8a6
   __TEXT.__objc_methtype: 0x285

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e8
+  __DATA_CONST.__objc_selrefs: 0x290
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0xaf8
+  __AUTH_CONST.__objc_const: 0x810
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x360
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C89BB62-965F-3047-9B04-766E2893B23F
-  Functions: 63
-  Symbols:   274
+  UUID: 6B0DD2E9-E246-39B6-BECD-8EE3EFB8040B
+  Functions: 69
+  Symbols:   280
   CStrings:  206
 
Symbols:
+ -[XCTTargetSession _on_queue_startListeningForClientConnections].cold.1
+ -[XCTTargetSession initWithDaemonConnection:registrationHandler:].cold.1
+ -[XCTTargetSession listener:shouldAcceptNewConnection:].cold.1
+ XCTConnectToDaemon.cold.1
+ XCTTBDefaultLog.cold.1
+ XCTTargetBootstrap.cold.1
+ __37-[XCTTargetSession _on_queue_connect]_block_invoke.276
+ __37-[XCTTargetSession _on_queue_connect]_block_invoke.277
+ __37-[XCTTargetSession _on_queue_connect]_block_invoke.277.cold.1
+ __51-[XCTTargetSession isInternallyEntitledConnection:]_block_invoke.302
+ __block_literal_global.280
+ __block_literal_global.301
- __37-[XCTTargetSession _on_queue_connect]_block_invoke.273
- __37-[XCTTargetSession _on_queue_connect]_block_invoke.274
- __37-[XCTTargetSession _on_queue_connect]_block_invoke.274.cold.1
- __51-[XCTTargetSession isInternallyEntitledConnection:]_block_invoke.299
- __block_literal_global.277
- __block_literal_global.298

```
