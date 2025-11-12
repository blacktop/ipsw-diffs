## CTParser

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`

```diff

-13123.3.0.0.0
-  __TEXT.__text: 0x5b58
-  __TEXT.__auth_stubs: 0x4b0
+13125.3.0.0.0
+  __TEXT.__text: 0x5a30
+  __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x515
-  __TEXT.__gcc_except_tab: 0x660
+  __TEXT.__gcc_except_tab: 0x66c
   __TEXT.__cstring: 0xe5
-  __TEXT.__oslogstring: 0x16f
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__oslogstring: 0x154
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x18
-  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x738
   __DATA.__data: 0x30
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 25D7054D-785A-3220-AF94-C3F56275D82F
-  Functions: 223
-  Symbols:   614
-  CStrings:  33
+  UUID: E1A22255-025D-3C84-919A-311A8CA36200
+  Functions: 221
+  Symbols:   608
+  CStrings:  32
 
Symbols:
+ GCC_except_table24
+ GCC_except_table34
+ GCC_except_table46
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table65
- GCC_except_table25
- GCC_except_table50
- GCC_except_table57
- GCC_except_table61
- GCC_except_table66
- GCC_except_table67
- __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
- __ZNK3xpc4dict15to_debug_stringEv
- __os_log_debug_impl
Functions:
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE : 744 -> 712
- __ZNK3xpc4dict15to_debug_stringEv
~ _OUTLINED_FUNCTION_0 : 16 -> 32
~ _OUTLINED_FUNCTION_1 : 32 -> 16
~ _OUTLINED_FUNCTION_3 : 12 -> 28
~ _OUTLINED_FUNCTION_5 : 28 -> 12
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.1 : 180 -> 124
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.2 : 124 -> 160
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.3 : 160 -> 56
- __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
CStrings:
- "#D Received XPC object: %s"

```
