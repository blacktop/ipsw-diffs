## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-806.0.0.0.1
-  __TEXT.__text: 0x42b00
+810.0.0.0.0
+  __TEXT.__text: 0x42db8
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x5080
+  __TEXT.__objc_stubs: 0x50a0
   __TEXT.__objc_methlist: 0x24c4
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x1f64
-  __TEXT.__objc_methname: 0x5b33
-  __TEXT.__cstring: 0x3318
-  __TEXT.__oslogstring: 0x616e
+  __TEXT.__objc_methname: 0x5b4a
+  __TEXT.__cstring: 0x3362
+  __TEXT.__oslogstring: 0x618a
   __TEXT.__objc_classname: 0x392
   __TEXT.__objc_methtype: 0xcb6
   __TEXT.__unwind_info: 0xb30

   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x18a0
-  __DATA_CONST.__cfstring: 0x30a0
+  __DATA_CONST.__cfstring: 0x30e0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x3860
-  __DATA.__objc_selrefs: 0x1830
+  __DATA.__objc_selrefs: 0x1838
   __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E755B14C-6E8F-3ED4-85A2-CC33ACD9B3CF
+  UUID: BB497484-6E88-3A6C-B0F3-E63FD1EFB1DA
   Functions: 953
-  Symbols:   2563
-  CStrings:  2698
+  Symbols:   2564
+  CStrings:  2705
 
Symbols:
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.553
+ __34-[CacheDelete clientSetState:key:]_block_invoke.663
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.547
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.516
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.517
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.518
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.564
+ __block_literal_global.1018
+ __block_literal_global.1024
+ __block_literal_global.1026
+ __block_literal_global.1028
+ __block_literal_global.1032
+ __block_literal_global.1038
+ __block_literal_global.1042
+ __block_literal_global.1046
+ __block_literal_global.974
+ __block_literal_global.978
+ __block_literal_global.985
+ __main_block_invoke.1015
+ __main_block_invoke.1016
+ __main_block_invoke.1030
+ __main_block_invoke.975
+ __main_block_invoke.983
+ __main_block_invoke_2.1013
+ __main_block_invoke_2.1019
+ __main_block_invoke_2.1034
+ __main_block_invoke_3.1014
+ __main_block_invoke_3.1022
+ __siginfo_handler_block_invoke.1039
+ __siginfo_handler_block_invoke.1043
+ _objc_msgSend$numberWithUnsignedInt:
- __33-[CacheDelete clientCancelPurge:]_block_invoke.550
- __34-[CacheDelete clientSetState:key:]_block_invoke.660
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.544
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.511
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.512
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.513
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.561
- __block_literal_global.1004
- __block_literal_global.1014
- __block_literal_global.1017
- __block_literal_global.1019
- __block_literal_global.1025
- __block_literal_global.1031
- __block_literal_global.1035
- __block_literal_global.1039
- __block_literal_global.971
- __block_literal_global.975
- __block_literal_global.979
- __main_block_invoke.1002
- __main_block_invoke.1008
- __main_block_invoke.1023
- __main_block_invoke.972
- __main_block_invoke.980
- __main_block_invoke_2.1006
- __main_block_invoke_2.1012
- __main_block_invoke_2.1027
- __main_block_invoke_3.1007
- __main_block_invoke_3.1015
- __siginfo_handler_block_invoke.1032
- __siginfo_handler_block_invoke.1036
Functions:
~ -[CacheDelete checkAndReserveSpace:] : 2772 -> 3264
~ ___main_block_invoke_2 : 3124 -> 3328
CStrings:
+ "%d checkAndReserveSpace %d "
+ "CACHE_DELETE_SUR_"
+ "CACHE_DELETE_SUR_RESERVED_AMOUNT"
+ "CACHE_DELETE_SUR_STATE"
+ "numberWithUnsignedInt:"

```
