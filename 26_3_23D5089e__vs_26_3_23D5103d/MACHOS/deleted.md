## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-815.60.2.0.0
-  __TEXT.__text: 0x42eb4
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x50a0
-  __TEXT.__objc_methlist: 0x24c4
+815.80.2.0.0
+  __TEXT.__text: 0x43074
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_stubs: 0x50c0
+  __TEXT.__objc_methlist: 0x24cc
   __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x1f64
-  __TEXT.__objc_methname: 0x5b4a
-  __TEXT.__cstring: 0x3362
-  __TEXT.__oslogstring: 0x61d7
+  __TEXT.__gcc_except_tab: 0x20d8
+  __TEXT.__objc_methname: 0x5b77
+  __TEXT.__cstring: 0x338a
+  __TEXT.__oslogstring: 0x632e
   __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methtype: 0xcb6
-  __TEXT.__unwind_info: 0xb30
-  __DATA_CONST.__auth_got: 0x760
+  __TEXT.__objc_methtype: 0xcd0
+  __TEXT.__unwind_info: 0xb38
+  __DATA_CONST.__auth_got: 0x768
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x18a0
-  __DATA_CONST.__cfstring: 0x30e0
+  __DATA_CONST.__const: 0x18e0
+  __DATA_CONST.__cfstring: 0x3160
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x3860
-  __DATA.__objc_selrefs: 0x1838
+  __DATA.__objc_selrefs: 0x1840
   __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B824AD57-0086-3C00-A7D9-F0CF2608AF4A
-  Functions: 953
-  Symbols:   2564
-  CStrings:  2707
+  UUID: F194D762-F7B3-3FA9-AEF0-48295DCC786C
+  Functions: 954
+  Symbols:   2568
+  CStrings:  2722
 
Symbols:
+ -[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]
+ GCC_except_table238
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table61
+ __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.234
+ ___68-[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]_block_invoke
+ __block_literal_global.1017
+ __block_literal_global.1027
+ __block_literal_global.1030
+ __block_literal_global.1034
+ __block_literal_global.1044
+ __block_literal_global.1048
+ __block_literal_global.1052
+ __main_block_invoke.1021
+ __main_block_invoke.1022
+ __main_block_invoke.1036
+ __main_block_invoke_2.1025
+ __main_block_invoke_2.1040
+ __main_block_invoke_3.1020
+ __main_block_invoke_3.1028
+ __siginfo_handler_block_invoke.1045
+ __siginfo_handler_block_invoke.1049
+ _objc_msgSend$sendCAEvent:key:value1:value2:value3:value4:
+ _xpc_activity_should_defer
- GCC_except_table53
- GCC_except_table57
- GCC_except_table60
- __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.222
- ___53-[CacheDeleteAnalytics sendCAEvent:key:value:value2:]_block_invoke
- __block_literal_global.1011
- __block_literal_global.1018
- __block_literal_global.1021
- __block_literal_global.1026
- __block_literal_global.1028
- __block_literal_global.1042
- __block_literal_global.1046
- __main_block_invoke.1009
- __main_block_invoke.1016
- __main_block_invoke.1030
- __main_block_invoke_2.1013
- __main_block_invoke_2.1034
- __main_block_invoke_3.1014
- __main_block_invoke_3.1022
- __siginfo_handler_block_invoke.1039
- __siginfo_handler_block_invoke.1043
Functions:
~ ___main_block_invoke_2 : 3328 -> 3516
~ -[CacheDeleteAnalytics sendCAEvent:key:value:value2:] : 308 -> 20
+ -[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]
~ -[CacheDeleteAnalytics sendPurgeableAmountStats] : 1020 -> 1172
CStrings:
+ "Daily Activity: Deferred before collecting any purgeable data, skipping stats posting"
+ "Daily Activity: Deferring during purgeable query (after %zu queries)"
+ "Daily Activity: Failed to defer before purgeable query"
+ "Daily Activity: Failed to defer during purgeable query"
+ "Daily Activity: Posting partial purgeable stats (%zu levels) before deferring"
+ "LEVEL1"
+ "LEVEL2"
+ "sendCAEvent:key:value1:value2:value3:value4:"
+ "v64@0:8@16@24@32@40@48@56"
+ "value_level1"
+ "value_level2"

```
