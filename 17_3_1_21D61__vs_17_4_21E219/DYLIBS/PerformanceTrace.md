## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-162.3.0.0.0
-  __TEXT.__text: 0x3a9c
+176.0.0.0.0
+  __TEXT.__text: 0x3c2c
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x478
+  __TEXT.__objc_methlist: 0x490
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x615
+  __TEXT.__cstring: 0x62a
   __TEXT.__oslogstring: 0x1ad
   __TEXT.__unwind_info: 0x110
   __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0xffc
+  __TEXT.__objc_methname: 0x106e
   __TEXT.__objc_methtype: 0x309
-  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_stubs: 0xe00
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbe8
-  __DATA_CONST.__objc_selrefs: 0x408
-  __AUTH_CONST.__cfstring: 0x6a0
+  __DATA_CONST.__objc_const: 0xc18
+  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_const: 0x160
   __AUTH_CONST.__auth_got: 0x138
   __AUTH.__objc_data: 0x78
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x7c
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 115
-  Symbols:   502
-  CStrings:  344
+  Functions: 117
+  Symbols:   509
+  CStrings:  350
 
Symbols:
+ -[PTTraceConfig enableSwiftUITracing]
+ -[PTTraceConfig setEnableSwiftUITracing:]
+ _OBJC_IVAR_$_PTTraceConfig._enableSwiftUITracing
+ ___32-[PTTraceConfig _initConnection]_block_invoke.163
+ ___32-[PTTraceConfig _initConnection]_block_invoke.163.cold.1
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.78
+ _objc_msgSend$enableSwiftUITracing
+ _objc_msgSend$setEnableSwiftUITracing:
- ___32-[PTTraceConfig _initConnection]_block_invoke.160
- ___32-[PTTraceConfig _initConnection]_block_invoke.160.cold.1
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.77
CStrings:
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_enableSwiftUITracing"
+ "_enableSwiftUITracing"
+ "enableSwiftUITracing"
+ "setEnableSwiftUITracing:"

```
