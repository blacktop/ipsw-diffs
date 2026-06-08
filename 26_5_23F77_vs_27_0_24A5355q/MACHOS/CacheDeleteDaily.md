## CacheDeleteDaily

> `/System/Library/CoreServices/CacheDeleteDaily`

```diff

-819.120.2.0.0
-  __TEXT.__text: 0x2f74
-  __TEXT.__auth_stubs: 0x510
+901.0.0.0.1
+  __TEXT.__text: 0x2d9c
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x660
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__objc_methname: 0x4a8
-  __TEXT.__cstring: 0xe26
+  __TEXT.__cstring: 0xe28
   __TEXT.__oslogstring: 0x5a7
-  __TEXT.__objc_classname: 0x14
+  __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0x7a
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__cfstring: 0xfe0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x370
   __DATA_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0x160
   __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E72E7899-0A45-35FE-B3C3-DA1CC4F919A2
+  UUID: A792F2E6-086B-38D3-828F-169B32305EF1
   Functions: 39
-  Symbols:   237
+  Symbols:   239
   CStrings:  385
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
Functions:
~ -[CacheDeletePruner pruneContainerTmps] : 308 -> 296
~ ___39-[CacheDeletePruner pruneContainerTmps]_block_invoke : 684 -> 596
~ -[CacheDeletePruner pruneDir:bundleID:] : 740 -> 732
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2 : 784 -> 720
~ __39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2.17 : 220 -> 176
~ _main : 204 -> 196
~ ___main_block_invoke : 1096 -> 1044
~ _getLocalCloudDocsURLs : 584 -> 588
~ ___register_activity_block_invoke : 3308 -> 3248
~ __register_activity_block_invoke.31 : 332 -> 328
~ ___register_activity_block_invoke_2 : 480 -> 424
~ _updateUsage : 760 -> 772
~ ___populateUsage_block_invoke : 132 -> 120
~ _diskUsage : 556 -> 564
~ _storageDailyStatsFilename : 524 -> 448
~ ___getLocalCloudDocsURLs_block_invoke : 456 -> 448
~ __getLocalCloudDocsURLs_block_invoke.441 : 100 -> 96

```
