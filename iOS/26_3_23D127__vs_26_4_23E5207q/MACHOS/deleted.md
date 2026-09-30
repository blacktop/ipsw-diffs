## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-815.80.2.0.0
-  __TEXT.__text: 0x43074
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_stubs: 0x50c0
-  __TEXT.__objc_methlist: 0x24cc
+819.100.7.0.0
+  __TEXT.__text: 0x46bec
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_stubs: 0x5120
+  __TEXT.__objc_methlist: 0x24f4
   __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x20d8
-  __TEXT.__objc_methname: 0x5b77
-  __TEXT.__cstring: 0x338a
-  __TEXT.__oslogstring: 0x632e
+  __TEXT.__gcc_except_tab: 0x2090
+  __TEXT.__objc_methname: 0x5bc3
+  __TEXT.__cstring: 0x33c3
+  __TEXT.__oslogstring: 0x62f4
   __TEXT.__objc_classname: 0x392
   __TEXT.__objc_methtype: 0xcd0
-  __TEXT.__unwind_info: 0xb38
-  __DATA_CONST.__auth_got: 0x768
-  __DATA_CONST.__got: 0x218
+  __TEXT.__unwind_info: 0xc90
+  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__cfstring: 0x3160
+  __DATA_CONST.__cfstring: 0x31a0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3860
-  __DATA.__objc_selrefs: 0x1840
+  __DATA.__objc_const: 0x3868
+  __DATA.__objc_selrefs: 0x1860
   __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 183763E0-A301-3150-9775-A3599F75E864
-  Functions: 954
-  Symbols:   2568
-  CStrings:  2722
+  UUID: 02C736D4-7C5D-3DF6-BBB5-7EF346694A41
+  Functions: 956
+  Symbols:   2567
+  CStrings:  2730
 
Symbols:
+ -[AppContainerCaches cachesForInstalledApps]
+ -[CacheDelete queryAppContainers:replyBlock:]
+ GCC_except_table14
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table154
+ GCC_except_table22
+ GCC_except_table239
+ _OBJC_CLASS_$_NSNull
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.557
+ __34-[CacheDelete clientSetState:key:]_block_invoke.667
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.551
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.568
+ __block_literal_global.1022
+ __block_literal_global.1029
+ __block_literal_global.1035
+ __block_literal_global.1037
+ __block_literal_global.1039
+ __block_literal_global.1043
+ __block_literal_global.1049
+ __block_literal_global.1053
+ __block_literal_global.1057
+ __block_literal_global.979
+ __block_literal_global.983
+ __block_literal_global.987
+ __block_literal_global.990
+ __main_block_invoke.1020
+ __main_block_invoke.1026
+ __main_block_invoke.1027
+ __main_block_invoke.1041
+ __main_block_invoke.980
+ __main_block_invoke.988
+ __main_block_invoke_2.1024
+ __main_block_invoke_2.1030
+ __main_block_invoke_2.1045
+ __main_block_invoke_3.1025
+ __main_block_invoke_3.1033
+ __siginfo_handler_block_invoke.1050
+ __siginfo_handler_block_invoke.1054
+ _objc_msgSend$cachesForInstalledApps
+ _objc_msgSend$lastKnownTmpSize
+ _objc_msgSend$null
- GCC_except_table139
- GCC_except_table142
- GCC_except_table153
- GCC_except_table238
- __33-[CacheDelete clientCancelPurge:]_block_invoke.553
- __34-[CacheDelete clientSetState:key:]_block_invoke.663
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.547
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.564
- __block_literal_global.1017
- __block_literal_global.1024
- __block_literal_global.1027
- __block_literal_global.1030
- __block_literal_global.1034
- __block_literal_global.1038
- __block_literal_global.1044
- __block_literal_global.1048
- __block_literal_global.1052
- __block_literal_global.974
- __block_literal_global.978
- __block_literal_global.982
- __block_literal_global.985
- __main_block_invoke.1015
- __main_block_invoke.1021
- __main_block_invoke.1022
- __main_block_invoke.1036
- __main_block_invoke.975
- __main_block_invoke.983
- __main_block_invoke_2.1019
- __main_block_invoke_2.1025
- __main_block_invoke_2.1040
- __main_block_invoke_3.1020
- __main_block_invoke_3.1028
- __siginfo_handler_block_invoke.1045
- __siginfo_handler_block_invoke.1049
- _nan
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "CACHE_DELETE_LAST_USE_DATE"
+ "CACHE_DELETE_PLUGIN_PURGE_TMP"
+ "Tmp purge cleared %llu"
+ "cachesForInstalledApps"
+ "lastKnownTmpSize"
+ "null"
+ "queryAppContainers:replyBlock:"
- " APFSIOC_GET_FREE_QUEUE_INFO: free_queue_bytes:%lld free_queue_tier2_bytes: %lld"

```
