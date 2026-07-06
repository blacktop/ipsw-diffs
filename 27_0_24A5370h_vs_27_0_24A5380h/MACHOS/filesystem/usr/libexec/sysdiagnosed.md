## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-  __TEXT.__text: 0x60f60
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x9320
-  __TEXT.__objc_methlist: 0x3f1c
+  __TEXT.__text: 0x61128
+  __TEXT.__auth_stubs: 0x1700
+  __TEXT.__objc_stubs: 0x93c0
+  __TEXT.__objc_methlist: 0x3f54
   __TEXT.__const: 0x1cc
-  __TEXT.__cstring: 0x10bd5
+  __TEXT.__cstring: 0x10c36
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methtype: 0x17f5
-  __TEXT.__gcc_except_tab: 0xdac
-  __TEXT.__objc_methname: 0xa602
-  __TEXT.__oslogstring: 0x80fa
+  __TEXT.__objc_methtype: 0x1825
+  __TEXT.__gcc_except_tab: 0xda8
+  __TEXT.__objc_methname: 0xa737
+  __TEXT.__oslogstring: 0x8111
   __TEXT.__ustring: 0x4e8
   __TEXT.__unwind_info: 0x1190
-  __DATA_CONST.__const: 0x13e8
-  __DATA_CONST.__cfstring: 0x11540
+  __DATA_CONST.__const: 0x13c0
+  __DATA_CONST.__cfstring: 0x11600
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xe90
-  __DATA_CONST.__objc_arrayobj: 0x13f8
+  __DATA_CONST.__objc_arraydata: 0xeb0
+  __DATA_CONST.__objc_arrayobj: 0x1410
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__auth_got: 0xb78
-  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__auth_got: 0xb90
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA.__objc_const: 0x5388
-  __DATA.__objc_selrefs: 0x29c8
-  __DATA.__objc_ivar: 0x474
+  __DATA.__objc_const: 0x53b8
+  __DATA.__objc_selrefs: 0x29f0
+  __DATA.__objc_ivar: 0x478
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x3a0
   __DATA.__bss: 0x280

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1767
-  Symbols:   502
-  CStrings:  7498
+  Functions: 1773
+  Symbols:   505
+  CStrings:  7519
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _container_copy_sandbox_token
+ _sandbox_extension_consume
+ _sandbox_extension_release
CStrings:
+ "-O"
+ "/usr/local/bin/anetest"
+ "<TMPOUTPUTDIR>/ane.anetrace"
+ "@48@0:8@16@24@32@?40"
+ "@64@0:8@16@24@32@40@48@?56"
+ "ANETraceBuffer"
+ "Could not consume sandbox extension for identifier %@ : %m"
+ "T@?,C,N,V_completionHandler"
+ "_completionHandler"
+ "anetest_stdout.txt"
+ "completionHandler"
+ "getBackgroundPowerLogContainer"
+ "getSearchdiagnoseContainer"
+ "getSimplePathArrayContainer:withContainerName:andDestination:completionHandler:"
+ "getSimplePathArrayContainer:withContainerName:andDestination:withOffsets:sizes:completionHandler:"
+ "logs/ANE"
+ "setCompletionHandler:"
- "Received canceling, ending browsing"
- "countDisplays"

```
