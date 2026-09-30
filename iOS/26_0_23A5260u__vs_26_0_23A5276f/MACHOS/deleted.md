## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-795.0.0.502.1
-  __TEXT.__text: 0x424b8
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x5060
+804.0.0.0.1
+  __TEXT.__text: 0x42a64
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x5080
   __TEXT.__objc_methlist: 0x24c4
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x1f88
-  __TEXT.__objc_methname: 0x5b64
-  __TEXT.__cstring: 0x32bf
-  __TEXT.__oslogstring: 0x5ffa
+  __TEXT.__objc_methname: 0x5b33
+  __TEXT.__cstring: 0x32f3
+  __TEXT.__oslogstring: 0x6116
   __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methtype: 0xccd
-  __TEXT.__unwind_info: 0xae8
-  __DATA_CONST.__auth_got: 0x758
+  __TEXT.__objc_methtype: 0xcb6
+  __TEXT.__unwind_info: 0xaf0
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x18a0
-  __DATA_CONST.__cfstring: 0x3040
+  __DATA_CONST.__cfstring: 0x3080
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x3860
-  __DATA.__objc_selrefs: 0x1828
+  __DATA.__objc_selrefs: 0x1830
   __DATA.__objc_ivar: 0x280
   __DATA.__objc_data: 0x960
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9C0A679-6DDB-3A52-845E-6277750EA037
+  UUID: E868DC91-F5C6-32F9-88FC-0F645D81DEB0
   Functions: 953
-  Symbols:   2559
-  CStrings:  2684
+  Symbols:   2563
+  CStrings:  2694
 
Symbols:
+ -[CacheDelete _clientSetState:key:asyncReserve:]
+ -[CacheDelete checkAndReserveSpace:]
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.547
+ __34-[CacheDelete clientSetState:key:]_block_invoke.657
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.541
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.510
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.511
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.512
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.558
+ ___48-[CacheDelete _clientSetState:key:asyncReserve:]_block_invoke
+ ___chkstk_darwin
+ __block_literal_global.1001
+ __block_literal_global.1008
+ __block_literal_global.1011
+ __block_literal_global.1018
+ __block_literal_global.1022
+ __block_literal_global.1028
+ __block_literal_global.1032
+ __block_literal_global.1036
+ __block_literal_global.50
+ __block_literal_global.968
+ __block_literal_global.972
+ __block_literal_global.976
+ __block_literal_global.979
+ __main_block_invoke.1005
+ __main_block_invoke.1006
+ __main_block_invoke.1020
+ __main_block_invoke.969
+ __main_block_invoke.977
+ __main_block_invoke.999
+ __main_block_invoke_2.1003
+ __main_block_invoke_2.1009
+ __main_block_invoke_2.1024
+ __main_block_invoke_3.1004
+ __main_block_invoke_3.1012
+ __siginfo_handler_block_invoke.1029
+ __siginfo_handler_block_invoke.1033
+ _memcmp
+ _objc_msgSend$_clientSetState:key:asyncReserve:
+ _objc_msgSend$checkAndReserveSpace:
+ _objc_msgSend$setLastUsedTime:
+ _objc_msgSend$unsignedLongValue
+ _statfs_ext
- -[CacheDelete _clientSetState:key:]
- -[CacheDelete checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:]
- __33-[CacheDelete clientCancelPurge:]_block_invoke.544
- __34-[CacheDelete clientSetState:key:]_block_invoke.651
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.538
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.505
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.506
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.507
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.555
- ___34-[CacheDelete clientSetState:key:]_block_invoke_2
- __block_literal_global.1006
- __block_literal_global.1009
- __block_literal_global.1012
- __block_literal_global.1020
- __block_literal_global.1026
- __block_literal_global.1030
- __block_literal_global.1034
- __block_literal_global.47
- __block_literal_global.966
- __block_literal_global.970
- __block_literal_global.974
- __block_literal_global.977
- __block_literal_global.999
- __main_block_invoke.1003
- __main_block_invoke.1004
- __main_block_invoke.1018
- __main_block_invoke.967
- __main_block_invoke.975
- __main_block_invoke.997
- __main_block_invoke_2.1001
- __main_block_invoke_2.1007
- __main_block_invoke_2.1022
- __main_block_invoke_3.1002
- __main_block_invoke_3.1010
- __siginfo_handler_block_invoke.1027
- __siginfo_handler_block_invoke.1031
- _objc_msgSend$_clientSetState:key:
- _objc_msgSend$checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:
- _objc_msgSend$setLastUsed:
Functions:
~ _enumerate_snapshots : 660 -> 1096
~ ___37-[CacheDelete purge:volume:callback:]_block_invoke_2 : 340 -> 344
~ -[CacheDelete checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:] -> -[CacheDelete checkAndReserveSpace:] : 2256 -> 2784
~ ___50-[CacheDelete CheckPurgeableAndUpdateReserveSpace]_block_invoke_2 : 720 -> 724
~ -[CacheDelete _clientSetState:key:] -> -[CacheDelete _clientSetState:key:asyncReserve:] : 1952 -> 1528
~ -[CacheDelete clientSetState:key:] -> ___48-[CacheDelete _clientSetState:key:asyncReserve:]_block_invoke : 2804 -> 644
~ ___34-[CacheDelete clientSetState:key:]_block_invoke -> -[CacheDelete clientSetState:key:] : 16 -> 1732
~ __34-[CacheDelete clientSetState:key:]_block_invoke.651 -> ___34-[CacheDelete clientSetState:key:]_block_invoke : 16 -> 1208
~ ___34-[CacheDelete clientSetState:key:]_block_invoke_2 -> __34-[CacheDelete clientSetState:key:]_block_invoke.657 : 16 -> 20
~ ___35-[CacheDelete pruneCacheableStates]_block_invoke_2 : 328 -> 332
~ ___89-[AppContainerCaches cachesForInstalledApps:bytesNeeded:volume:sortForUrgency:telemetry:]_block_invoke : 920 -> 1068
CStrings:
+ "%d _clientSetState: updating asynchronously"
+ "%d _clientSetState: updating synchronously "
+ "%d checkAndReserveSpace amountToReserve: %lld totalAPFSPurgeable:%lld "
+ "%d release space "
+ "CACHE_DELETE_RELEASE_AMOUNT"
+ "_clientSetState:key:asyncReserve:"
+ "checkAndReserveSpace:"
+ "com.apple.Safari.WebApp"
+ "enumerate_snapshots: (%s) skipping unsupported filesystem (%s)"
+ "enumerate_snapshots: (%s) statfs failed: %s"
+ "setLastUsedTime:"
+ "unsignedLongValue"
- "_clientSetState:key:"
- "checkAndReserveSpace:systemGrowthAmount:centralizedPurgeableFactor:pluginPurgeableFactor:maxReserveSpace:"
- "setLastUsed:"
- "v56@0:8@16@24@32@40@48"

```
