## CacheDeleteDaily

> `/System/Library/CoreServices/CacheDeleteDaily`

```diff

-815.80.2.0.0
-  __TEXT.__text: 0x2e78
-  __TEXT.__auth_stubs: 0x550
+819.100.7.0.0
+  __TEXT.__text: 0x2f74
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x88

   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x7a
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__cfstring: 0xfe0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FC668EB-1F15-3D5C-BCFA-8ED38DDB7109
+  UUID: B682D305-5BBF-31BB-BDD6-D42C610B6E05
   Functions: 39
-  Symbols:   241
+  Symbols:   237
   CStrings:  385
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x9
Functions:
~ -[CacheDeletePruner pruneContainerTmps] : 296 -> 308
~ ___39-[CacheDeletePruner pruneContainerTmps]_block_invoke : 644 -> 684
~ -[CacheDeletePruner pruneDir:bundleID:] : 732 -> 740
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke : 392 -> 408
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2 : 764 -> 784
~ _main : 196 -> 204
~ ___main_block_invoke : 1064 -> 1096
~ _getLocalCloudDocsURLs : 588 -> 584
~ ___register_activity_block_invoke : 3252 -> 3308
~ __register_activity_block_invoke.31 : 328 -> 332
~ ___register_activity_block_invoke_2 : 460 -> 480
~ _updateUsage : 768 -> 760
~ ___populateUsage_block_invoke : 120 -> 132
~ _diskUsage : 560 -> 556
~ ___updateUsage_block_invoke : 24 -> 20
~ ___updateUsage_block_invoke_2 : 24 -> 20
~ _storageDailyStatsFilename : 492 -> 524
~ ___getLocalCloudDocsURLs_block_invoke : 444 -> 456
~ __getLocalCloudDocsURLs_block_invoke.441 : 96 -> 100

```
