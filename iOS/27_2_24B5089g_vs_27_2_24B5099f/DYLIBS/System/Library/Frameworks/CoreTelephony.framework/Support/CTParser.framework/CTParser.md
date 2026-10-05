## CTParser

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`

```diff

-13496.3.0.0.0
-  __TEXT.__text: 0x57a8
+13498.0.0.0.0
+  __TEXT.__text: 0x56a0
   __TEXT.__const: 0x515
-  __TEXT.__gcc_except_tab: 0x5f8
+  __TEXT.__gcc_except_tab: 0x610
   __TEXT.__cstring: 0x397
-  __TEXT.__oslogstring: 0x166
-  __TEXT.__unwind_info: 0x560
+  __TEXT.__oslogstring: 0x14e
+  __TEXT.__unwind_info: 0x558
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x18
   __DATA_CONST.__weak_got: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 227
-  Symbols:   449
-  CStrings:  35
+  Functions: 225
+  Symbols:   448
+  CStrings:  34
 
Symbols:
+ GCC_except_table25
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table57
- GCC_except_table32
- GCC_except_table37
- GCC_except_table50
- GCC_except_table53
- GCC_except_table60
- __ZNK3xpc4dict15to_debug_stringEv
- __os_log_debug_impl
Functions:
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE : 780 -> 748
- __ZNK3xpc4dict15to_debug_stringEv
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_2 : 20 -> 12
~ _OUTLINED_FUNCTION_3 : 12 -> 16
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.1 : 124 -> 76
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.2 : 76 -> 104
~ __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.3 : 104 -> 52
- __ZN14CTParserClient15processResponseENSt3__110shared_ptrI19CTParserXPCResponseEE.cold.4
CStrings:
- "Received XPC object: %s"
```
