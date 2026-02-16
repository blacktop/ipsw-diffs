## deleted_helper

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted_helper`

```diff

-815.80.2.0.0
-  __TEXT.__text: 0x5a44
-  __TEXT.__auth_stubs: 0x660
+819.100.7.0.0
+  __TEXT.__text: 0x5a8c
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x5a0
   __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x14c
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__objc_methname: 0x401
-  __TEXT.__cstring: 0x76b
-  __TEXT.__oslogstring: 0xfc6
+  __TEXT.__cstring: 0x707
+  __TEXT.__oslogstring: 0xf2b
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methtype: 0x7a
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x340
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x4a0
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0xe0
+  __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x160
   __DATA.__objc_selrefs: 0x1b8
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABE18D1F-E425-30D2-B3BB-B5871D5EFCBA
-  Functions: 47
-  Symbols:   265
-  CStrings:  256
+  UUID: 73A07C35-ED89-35ED-A782-09BDB4F10C34
+  Functions: 46
+  Symbols:   258
+  CStrings:  247
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
- _OBJC_CLASS_$_NSConstantArray
- ___block_descriptor_32_e51_B24?0r*8^{?=BBqiIQQQ{timespec=qq}{timespec=qq}B}16l
- ___periodic_block_invoke
- __block_literal_global.172
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x9
- _os_variant_has_internal_diagnostics
Functions:
~ __main_block_invoke.67 : 2528 -> 2664
~ _purge_orphans : 824 -> 852
~ _iterate_orphans : 488 -> 504
~ ___purge_orphans_block_invoke : 304 -> 308
~ _fsPurgeable : 4104 -> 4176
~ -[CacheDeletePruner pruneContainerTmps] : 296 -> 308
~ ___39-[CacheDeletePruner pruneContainerTmps]_block_invoke : 644 -> 684
~ -[CacheDeletePruner pruneDir:bundleID:] : 732 -> 740
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke : 392 -> 408
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2 : 764 -> 784
~ _main : 504 -> 508
~ ___main_block_invoke : 420 -> 432
~ __main_block_invoke.47 : 508 -> 500
~ __main_block_invoke.48 : 208 -> 212
~ __main_block_invoke.53 : 944 -> 984
~ _fsPurge : 3116 -> 3204
~ _releaseReservedSpaceFromUpdateVolume : 492 -> 504
~ __main_block_invoke.81 : 824 -> 868
~ __main_block_invoke.90 : 768 -> 212
~ __main_block_invoke.93 : 104 -> 108
~ __main_block_invoke_2.96 : 104 -> 108
~ ___RegisterCacheDeleteOrphanDirHandlerService_block_invoke : 100 -> 104
~ ___RegisterCacheDeleteOrphanDirHandlerService_block_invoke_2 : 584 -> 612
~ ___RegisterCacheDeleteOrphanDirHandlerService_block_invoke_4 : 268 -> 272
~ __RegisterCacheDeleteOrphanDirHandlerService_block_invoke.109 : 312 -> 336
~ _getPurgeableInfoByDirKey : 880 -> 912
~ ___getPurgeableInfoByDirKey_block_invoke : 68 -> 72
~ _amountStillNeeded : 1028 -> 1064
CStrings:
+ "customerReleaseBuild IS SEED BUILD"
- "/var/mobile/Library/AutoBugCapture/"
- "/var/mobile/Library/Logs/AutoBugCapture/"
- "Customer build, clearing %@"
- "com.apple.cache_delete"
- "customerReleaseBuild IS INTERNAL BUILD"
- "customerReleaseBuild IS NOT INTERNAL BUILD"
- "customerReleaseBuild IS NOT SEED BUILD"
- "unable to get address of MGGetBoolAnswer"

```
