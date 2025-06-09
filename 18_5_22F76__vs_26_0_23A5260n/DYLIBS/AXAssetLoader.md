## AXAssetLoader

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x13060
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x1264
+3180.6.1.0.0
+  __TEXT.__text: 0x127c0
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x11cc
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x6bc
-  __TEXT.__cstring: 0xe71
-  __TEXT.__oslogstring: 0xf49
-  __TEXT.__dlopen_cstrs: 0x28e
-  __TEXT.__unwind_info: 0x6c8
+  __TEXT.__gcc_except_tab: 0x684
+  __TEXT.__cstring: 0xcf1
+  __TEXT.__oslogstring: 0xf75
+  __TEXT.__dlopen_cstrs: 0x23a
+  __TEXT.__unwind_info: 0x6a8
   __TEXT.__objc_classname: 0x2d5
-  __TEXT.__objc_methname: 0x2fb5
-  __TEXT.__objc_methtype: 0x5b5
-  __TEXT.__objc_stubs: 0x2500
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x888
+  __TEXT.__objc_methname: 0x2e9e
+  __TEXT.__objc_methtype: 0x581
+  __TEXT.__objc_stubs: 0x24a0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf0
+  __DATA_CONST.__objc_selrefs: 0xba8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x1a40
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__objc_const: 0x1a28
+  __AUTH_CONST.__objc_intobj: 0xa8
   __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x240
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F626A6F-3787-3369-9EC5-F29C0A2CE2B9
-  Functions: 507
-  Symbols:   1830
-  CStrings:  939
+  UUID: 9DF45E62-8E45-3200-995C-58D1EB56BBA7
+  Functions: 495
+  Symbols:   1789
+  CStrings:  905
 
Symbols:
+ -[AXComfortSoundsAssetPolicy shouldUseProductionServerForInternalBuilds]
+ GCC_except_table92
+ _ASSetAssetServerURLForAssetTypeSoft
+ _ASSetAssetServerURLForAssetTypeSoft.cold.1
+ ___122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke.298
+ ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.330
+ ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.331
+ ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.336
+ ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.336.cold.1
+ ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.340
+ ___69-[AXAssetController _replaceCachedAssetsWithAssets:error:completion:]_block_invoke.321
+ ___70-[AXAssetController downloadAssets:successStartBlock:completionBlock:]_block_invoke.315
+ ___block_literal_global.318
+ ___block_literal_global.333
- -[AXAssetController setProductionServerURL].cold.2
- -[AXAssetsService componentCacheChanged]
- -[AXAssetsService deleteCompactResourceIfNeededForIdentifier:]
- -[AXAssetsService downloadTTSResourceForVoiceId:]
- -[AXAssetsService informSiriVoiceSubscriptionsWithVoiceId:addition:]
- -[AXAssetsService restartTTSResourceMigration]
- -[AXAssetsService runFirstBootTasks:]
- -[AXAssetsService runFirstUnlockTasks]
- -[AXAssetsService updateTTSResourcesForActionType:]
- -[AXAudiogramIngestionAssetPolicy init]
- -[AXAudiogramIngestionAssetPolicy init].cold.1
- -[AXAudiogramIngestionAssetPolicy init].cold.2
- -[AXAudiogramIngestionAssetPolicy shouldUseProductionServerForInternalBuilds]
- ___122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke.295
- ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.327
- ___53-[AXAssetController _queue_refreshAssets:completion:]_block_invoke.328
- ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.333
- ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.333.cold.1
- ___66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.337
- ___69-[AXAssetController _replaceCachedAssetsWithAssets:error:completion:]_block_invoke.318
- ___70-[AXAssetController downloadAssets:successStartBlock:completionBlock:]_block_invoke.312
- ___NSDictionary0__struct
- ___block_literal_global.315
- ___block_literal_global.330
- ___getMASetServerUrlOverrideSymbolLoc_block_invoke
- __os_feature_enabled_impl
- _getMASetServerUrlOverrideSymbolLoc.ptr
- _objc_msgSend$invokeSimpleTaskById:arguments:
- _objc_msgSend$runFirstBootTasks:
- _objc_msgSend$runFirstUnlockTasks
CStrings:
+ "Clearing %@ server production URL overrides"
- "AXComponentChangeSimpleTask"
- "AXDeleteCompactResourceSimpleTask"
- "AXDownloadTTSResourceTask"
- "AXInformSiriVoiceSubscriptionsSimpleTask"
- "AXMigrateResourcesSimpleTask"
- "AXUpdateResourcesSimpleTask"
- "Accessibility"
- "AudiogramIngestionV2"
- "MASetServerUrlOverride"
- "com.apple.accessibility.AXAssetLoader"
- "componentCacheChanged"
- "deleteCompactResourceIfNeededForIdentifier:"
- "downloadTTSResourceForVoiceId:"
- "https://basejumper.apple.com/livability/Crystal"
- "informSiriVoiceSubscriptionsWithVoiceId:addition:"
- "invokeSimpleTaskById:arguments:"
- "kAXActionType"
- "kAXVoiceId"
- "kAXVoiceSubscriptionAddition"
- "restartTTSResourceMigration"
- "runFirstBootTasks:"
- "runFirstUnlockTasks"
- "updateTTSResourcesForActionType:"
- "v28@0:8@16B24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"

```
