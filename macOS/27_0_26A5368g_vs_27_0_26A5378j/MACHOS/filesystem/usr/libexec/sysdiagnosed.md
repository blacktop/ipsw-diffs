## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-  __TEXT.__text: 0x5b888
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_stubs: 0x8320
-  __TEXT.__objc_methlist: 0x3874
+  __TEXT.__text: 0x5b984
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x83e0
+  __TEXT.__objc_methlist: 0x38ac
   __TEXT.__const: 0x1dc
-  __TEXT.__cstring: 0xe89e
-  __TEXT.__oslogstring: 0x72ce
+  __TEXT.__cstring: 0xe8c0
+  __TEXT.__oslogstring: 0x72e5
   __TEXT.__objc_classname: 0x322
-  __TEXT.__objc_methtype: 0xed5
-  __TEXT.__gcc_except_tab: 0xd5c
-  __TEXT.__objc_methname: 0x8e3f
-  __TEXT.__unwind_info: 0xff0
-  __DATA_CONST.__const: 0x1160
-  __DATA_CONST.__cfstring: 0x100a0
+  __TEXT.__objc_methtype: 0xf05
+  __TEXT.__gcc_except_tab: 0xd58
+  __TEXT.__objc_methname: 0x8f74
+  __TEXT.__unwind_info: 0xff8
+  __DATA_CONST.__const: 0x1130
+  __DATA_CONST.__cfstring: 0x100e0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x12d8
   __DATA_CONST.__objc_arrayobj: 0x1848
   __DATA_CONST.__objc_intobj: 0x228
-  __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA.__objc_const: 0x4b88
-  __DATA.__objc_selrefs: 0x2410
-  __DATA.__objc_ivar: 0x418
+  __DATA.__objc_const: 0x4bb8
+  __DATA.__objc_selrefs: 0x2438
+  __DATA.__objc_ivar: 0x41c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x278
   __DATA.__bss: 0x1f8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1617
-  Symbols:   438
-  CStrings:  6782
+  Functions: 1623
+  Symbols:   441
+  CStrings:  6795
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _container_copy_sandbox_token
+ _sandbox_extension_consume
+ _sandbox_extension_release
CStrings:
+ "@48@0:8@16@24@32@?40"
+ "@64@0:8@16@24@32@40@48@?56"
+ "BackgroundPowerlog"
+ "Could not consume sandbox extension for identifier %@ : %m"
+ "T@?,C,N,V_completionHandler"
+ "_completionHandler"
+ "completionHandler"
+ "getBackgroundPowerLogContainer"
+ "getSearchdiagnoseContainer"
+ "getSimplePathArrayContainer:withContainerName:andDestination:completionHandler:"
+ "getSimplePathArrayContainer:withContainerName:andDestination:withOffsets:sizes:completionHandler:"
+ "logs/powerlogs"
+ "setCompletionHandler:"
- "Received canceling, ending browsing"
- "countDisplays"

```
