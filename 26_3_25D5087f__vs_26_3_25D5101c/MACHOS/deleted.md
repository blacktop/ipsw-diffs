## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-815.60.2.0.0
-  __TEXT.__text: 0x492c0
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_stubs: 0x50a0
-  __TEXT.__objc_methlist: 0x2424
+815.80.2.0.0
+  __TEXT.__text: 0x4949c
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x50c0
+  __TEXT.__objc_methlist: 0x242c
   __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x1e20
-  __TEXT.__objc_methname: 0x597a
-  __TEXT.__cstring: 0x31e5
-  __TEXT.__oslogstring: 0x5ff7
+  __TEXT.__gcc_except_tab: 0x1f94
+  __TEXT.__objc_methname: 0x59a7
+  __TEXT.__cstring: 0x320d
+  __TEXT.__oslogstring: 0x614e
   __TEXT.__objc_classname: 0x387
-  __TEXT.__objc_methtype: 0xcd5
-  __TEXT.__unwind_info: 0xb50
-  __DATA_CONST.__auth_got: 0x700
+  __TEXT.__objc_methtype: 0xcef
+  __TEXT.__unwind_info: 0xb60
+  __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1aa8
-  __DATA_CONST.__cfstring: 0x2f80
+  __DATA_CONST.__const: 0x1ae8
+  __DATA_CONST.__cfstring: 0x3000
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x328
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x3708
-  __DATA.__objc_selrefs: 0x1818
+  __DATA.__objc_selrefs: 0x1820
   __DATA.__objc_ivar: 0x270
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x4e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 241A7232-14C0-3C31-8B27-4CA82AC68B07
-  Functions: 1021
-  Symbols:   2607
-  CStrings:  2686
+  UUID: C48C443E-CDAB-329E-ABED-96C52E75879D
+  Functions: 1022
+  Symbols:   2611
+  CStrings:  2701
 
Symbols:
+ -[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]
+ GCC_except_table262
+ GCC_except_table54
+ GCC_except_table58
+ __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.237
+ ___68-[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]_block_invoke
+ ___DADiskDisappearedCallback_block_invoke.1055
+ ___DADiskDisappearedCallback_block_invoke.1056
+ __block_literal_global.1005
+ __block_literal_global.1008
+ __block_literal_global.1025
+ __block_literal_global.1028
+ __block_literal_global.1031
+ __block_literal_global.1034
+ __block_literal_global.1041
+ __block_literal_global.1053
+ __block_literal_global.1069
+ __block_literal_global.999
+ __main_block_invoke.1023
+ __main_block_invoke.1039
+ __main_block_invoke.997
+ __main_block_invoke_2.1001
+ __main_block_invoke_2.1026
+ __main_block_invoke_2.1043
+ __main_block_invoke_3.1002
+ __main_block_invoke_3.1029
+ __main_block_invoke_4.1032
+ __main_block_invoke_5.1035
+ __siginfo_handler_block_invoke.1066
+ _objc_msgSend$sendCAEvent:key:value1:value2:value3:value4:
+ _xpc_activity_should_defer
- GCC_except_table53
- GCC_except_table57
- __47-[CacheDeleteAnalytics anonymizeAndFlush:name:]_block_invoke.225
- ___53-[CacheDeleteAnalytics sendCAEvent:key:value:value2:]_block_invoke
- ___DADiskDisappearedCallback_block_invoke.1051
- ___DADiskDisappearedCallback_block_invoke.1052
- __block_literal_global.1001
- __block_literal_global.1004
- __block_literal_global.1021
- __block_literal_global.1024
- __block_literal_global.1027
- __block_literal_global.1030
- __block_literal_global.1033
- __block_literal_global.1049
- __block_literal_global.1057
- __block_literal_global.995
- __main_block_invoke.1019
- __main_block_invoke.1035
- __main_block_invoke.993
- __main_block_invoke_2.1022
- __main_block_invoke_2.1039
- __main_block_invoke_2.997
- __main_block_invoke_3.1025
- __main_block_invoke_3.998
- __main_block_invoke_4.1028
- __main_block_invoke_5.1031
- __siginfo_handler_block_invoke.1058
Functions:
~ ___main_block_invoke_2 : 3720 -> 3872
~ -[CacheDeleteAnalytics sendCAEvent:key:value:value2:] : 352 -> 20
+ -[CacheDeleteAnalytics sendCAEvent:key:value1:value2:value3:value4:]
~ -[CacheDeleteAnalytics sendPurgeableAmountStats] : 1152 -> 1352
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
