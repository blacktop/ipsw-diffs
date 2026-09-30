## CacheDeleteAppContainerCaches

> `/System/Library/CoreServices/CacheDeleteAppContainerCaches`

```diff

-815.80.2.0.0
-  __TEXT.__text: 0x4e58
-  __TEXT.__auth_stubs: 0x550
+819.100.7.0.0
+  __TEXT.__text: 0x50fc
+  __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__cstring: 0x5ce
   __TEXT.__oslogstring: 0x417
   __TEXT.__objc_methname: 0x61f
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methtype: 0xfa
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__auth_got: 0x2b8
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x4e8
   __DATA_CONST.__cfstring: 0x540

   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C7CE3C6-4D08-37A5-9A0D-C2AB34605E9E
+  UUID: 4093FB02-A322-3DB7-AB8F-B86167026CC4
   Functions: 72
-  Symbols:   320
+  Symbols:   313
   CStrings:  255
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x3
- _objc_retain_x9
Functions:
~ ___RegisterCacheDeleteAppFreezerService_block_invoke : 112 -> 116
~ _maybeReenableAppFreezer : 580 -> 596
~ ___RegisterCacheDeleteAppFreezerService_block_invoke_4 : 452 -> 460
~ __RegisterCacheDeleteAppFreezerService_block_invoke.19 : 112 -> 116
~ _isAppFreezerEnabled : 388 -> 400
~ __RegisterCacheDeleteAppFreezerService_block_invoke_2.24 : 440 -> 456
~ _setAppFreezeEnabled : 404 -> 412
~ -[CacheDeletePruner pruneContainerTmps] : 296 -> 308
~ ___39-[CacheDeletePruner pruneContainerTmps]_block_invoke : 644 -> 684
~ -[CacheDeletePruner pruneDir:bundleID:] : 732 -> 740
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke : 392 -> 408
~ ___39-[CacheDeletePruner pruneDir:bundleID:]_block_invoke_2 : 764 -> 784
~ -[CacheDeleteManagedAssets initWithInfo:atUrgency:] : 292 -> 312
~ -[CacheDeleteManagedAssets dateHasExpired:interval:] : 144 -> 148
~ -[CacheDeleteManagedAssets periodicShouldRemoveAsset:] : 180 -> 196
~ -[CacheDeleteManagedAssets sortAssets:] : 136 -> 140
~ ___39-[CacheDeleteManagedAssets sortAssets:]_block_invoke : 2432 -> 2552
~ -[CacheDeleteManagedAssets sizeEligibleAsset:] : 328 -> 336
~ ___46-[CacheDeleteManagedAssets sizeEligibleAsset:]_block_invoke : 284 -> 288
~ -[CacheDeleteManagedAssets assetsFromArray:forAmount:] : 460 -> 480
~ -[CacheDeleteManagedAssets purgeAssets:testObject:] : 444 -> 440
~ ___51-[CacheDeleteManagedAssets purgeAssets:testObject:]_block_invoke : 608 -> 620
~ ___51-[CacheDeleteManagedAssets purgeAssets:testObject:]_block_invoke_2 : 576 -> 580
~ __51-[CacheDeleteManagedAssets purgeAssets:testObject:]_block_invoke.10 : 248 -> 252
~ -[CacheDeleteManagedAssets periodic:] : 552 -> 556
~ ___37-[CacheDeleteManagedAssets periodic:]_block_invoke : 196 -> 212
~ ___37-[CacheDeleteManagedAssets periodic:]_block_invoke_2 : 336 -> 340
~ ___37-[CacheDeleteManagedAssets periodic:]_block_invoke_3 : 284 -> 288
~ -[CacheDeleteManagedAssets analytics] : 1364 -> 1440
~ ___37-[CacheDeleteManagedAssets analytics]_block_invoke : 336 -> 348
~ _RegisterCacheManagementAssetsService : 288 -> 292
~ ___RegisterCacheManagementAssetsService_block_invoke : 100 -> 104
~ ___RegisterCacheManagementAssetsService_block_invoke_2 : 212 -> 224
~ ___RegisterCacheManagementAssetsService_block_invoke_3 : 212 -> 216
~ ___RegisterCacheManagementAssetsService_block_invoke_4 : 2840 -> 3000

```
