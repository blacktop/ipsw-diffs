## CTParser

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`

```diff

-12410.0.0.0.0
-  __TEXT.__text: 0x5860
-  __TEXT.__auth_stubs: 0x4a0
+12412.0.0.0.0
+  __TEXT.__text: 0x5988
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__const: 0x515
-  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__gcc_except_tab: 0x630
   __TEXT.__cstring: 0xe5
-  __TEXT.__oslogstring: 0x154
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__oslogstring: 0x16f
+  __TEXT.__unwind_info: 0x498
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x18
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x738
   __DATA.__data: 0x30
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 496B4920-5649-3119-ABC5-053533A095E0
-  Functions: 219
-  Symbols:   600
-  CStrings:  32
+  UUID: 36271141-E5FC-3397-A2BB-839D88A1F26D
+  Functions: 221
+  Symbols:   606
+  CStrings:  33
 
Symbols:
+ GCC_except_table16
+ GCC_except_table25
+ GCC_except_table41
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table61
+ GCC_except_table66
+ GCC_except_table67
+ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
+ __ZNK3xpc4dict15to_debug_stringEv
+ __os_log_debug_impl
- GCC_except_table34
- GCC_except_table46
- GCC_except_table54
- GCC_except_table62
- GCC_except_table65
Functions:
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE : 712 -> 744
+ __ZNK3xpc4dict15to_debug_stringEv
~ _OUTLINED_FUNCTION_0 : 32 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 32
~ _OUTLINED_FUNCTION_3 : 28 -> 12
~ _OUTLINED_FUNCTION_5 : 12 -> 28
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.1 : 124 -> 180
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.2 : 160 -> 124
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.3 : 56 -> 160
+ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
CStrings:
+ "#D Received XPC object: %s"

```
