## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-238.0.0.0.0
+240.0.0.0.0
   __TEXT.__text: 0x11d8c
-  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0xc4c
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xc78
-  __TEXT.__cstring: 0xd39
+  __TEXT.__cstring: 0xd25
   __TEXT.__oslogstring: 0xce5
   __TEXT.__unwind_info: 0x660
   __TEXT.__objc_classname: 0x158

   __DATA_CONST.__objc_selrefs: 0x9a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x1318
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x168

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF5516E5-DA64-3E94-9D89-F1BD04DB8CEB
+  UUID: 1A2DBC43-FBB8-3618-A651-3C12E253836E
   Functions: 334
-  Symbols:   1303
-  CStrings:  831
+  Symbols:   1302
+  CStrings:  829
 
Symbols:
+ ___32-[PTTraceConfig _initConnection]_block_invoke.181
+ ___32-[PTTraceConfig _initConnection]_block_invoke.181.cold.1
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.417
- _NSLog
- ___32-[PTTraceConfig _initConnection]_block_invoke.184
- ___32-[PTTraceConfig _initConnection]_block_invoke.184.cold.1
- ___block_literal_global.186
- ___block_literal_global.188
- ___block_literal_global.420
CStrings:
- "traceRecordArgs: %@"

```
