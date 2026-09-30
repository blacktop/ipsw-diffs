## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-343.3.0.0.0
-  __TEXT.__text: 0x191324
+345.0.0.0.0
+  __TEXT.__text: 0x1902d8
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x19a38
-  __TEXT.__const: 0x4b0
-  __TEXT.__gcc_except_tab: 0x1b24c
-  __TEXT.__cstring: 0x5aca
-  __TEXT.__oslogstring: 0xb958
+  __TEXT.__objc_methlist: 0x199b0
+  __TEXT.__const: 0x440
+  __TEXT.__gcc_except_tab: 0x1b2a4
+  __TEXT.__cstring: 0x5a73
+  __TEXT.__oslogstring: 0xb933
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf430
+  __TEXT.__unwind_info: 0xf3f0
   __TEXT.__objc_classname: 0x470b
-  __TEXT.__objc_methname: 0x1af88
+  __TEXT.__objc_methname: 0x1ae42
   __TEXT.__objc_methtype: 0xdf6b
-  __TEXT.__objc_stubs: 0x12840
-  __DATA_CONST.__got: 0xc90
-  __DATA_CONST.__const: 0x4050
+  __TEXT.__objc_stubs: 0x126e0
+  __DATA_CONST.__got: 0xc98
+  __DATA_CONST.__const: 0x3ec0
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6738
+  __DATA_CONST.__objc_selrefs: 0x66d0
   __DATA_CONST.__objc_superrefs: 0x10f8
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x7620
-  __AUTH_CONST.__objc_const: 0x2c170
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x7600
+  __AUTH_CONST.__objc_const: 0x2c150
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30

   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C614B290-660B-35BE-9027-C554D3D1F3D0
-  Functions: 9916
-  Symbols:   33683
-  CStrings:  8994
+  UUID: 7540FDFB-DAAF-35F5-9F45-3C5CC72AA76D
+  Functions: 9887
+  Symbols:   33602
+  CStrings:  8972
 
Symbols:
+ +[_LTDUAFBridge assetSubtypeForAssetSpecifier:]
+ -[_LTDLanguageAssetCache multicastObservers]
+ -[_LTDLanguageAssetCache multicastObservers].cold.1
+ -[_LTDLanguageAssetCache multicastObservers].cold.2
+ -[_LTDLanguageAssetCache multicastObservers].cold.3
+ -[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:].cold.1
+ -[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:].cold.1
+ __LTPreferencesIncludeHiddenCallTranslationLocales
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.313
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.30
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.34
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.33
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.33.cold.1
+ ___44-[_LTDLanguageAssetCache multicastObservers]_block_invoke
+ ___44-[_LTDLanguageAssetCache multicastObservers]_block_invoke_2
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.338
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.338.cold.1
+ ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.60
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.361
+ ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.53
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.296
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.335
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.336
+ ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.330
+ ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.9
+ ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.9.cold.1
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.24
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.27
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.27.cold.1
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_2.25
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.26
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.26.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.350
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.350.cold.1
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.306
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.307
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.308
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.314
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.309
+ ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.28
+ ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.28.cold.1
+ ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.47
+ ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.cold.1
+ ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.cold.2
+ ___83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.54
+ ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.58
+ ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.59
+ ___block_descriptor_105_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s64l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_32_e34_B16?0"<_LTDAssetModelProtocol>"8l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e15_v16?0?<v?B>8ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_81_e8_32s40s48s56s64r_e17_v16?0"NSError"8ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.296
+ ___block_literal_global.301
+ ___block_literal_global.305
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.316
+ ___block_literal_global.32
+ ___block_literal_global.320
+ ___block_literal_global.323
+ ___block_literal_global.338
+ ___block_literal_global.346
+ ___block_literal_global.45
+ ___block_literal_global.56
+ _kLTDebugIncludeHiddenCallTranslationLocales
+ _objc_msgSend$assetSubtypeForAssetSpecifier:
+ _objc_msgSend$multicastObservers
- +[_LTDAssetService _catalogRefreshInterval]
- +[_LTDAssetService _forceOneTimeCatalogRefresh]
- +[_LTDAssetService _isCatalogRefreshWaitExpired]
- +[_LTDAssetService _isCatalogRefreshWaitExpired].cold.1
- +[_LTDAssetService _isCatalogRefreshWaitExpired].cold.2
- +[_LTDAssetService _isObsoleteCatalogType:]
- +[_LTDAssetService _isObsoleteCatalogType:].cold.1
- +[_LTDAssetService _isObsoleteCatalogType:].cold.2
- +[_LTDAssetService _test_resetForceOneTimeCatalogRefresh]
- +[_LTDAssetService needsCatalogRefresh]
- +[_LTDAssetService refreshCatalogIfNeededWithCompletion:]
- +[_LTDAssetService setNeedsCatalogRefresh:]
- -[_LTDAssetModel compareDownloadPriority:]
- -[_LTDAssetModel downloadPriority]
- -[_LTDLanguageAssetCache _multicastObservers]
- -[_LTDLanguageAssetCache _multicastObservers].cold.1
- -[_LTOfflineAssetManager _refreshAllAssets:]
- -[_LTOfflineAssetManager refreshAllIfNeededWithCompletion:]
- __LTPreferencesLastOfflineAssetCatalogUpdate
- __LTPreferencesSetLastOfflineAssetCatalogUpdate
- ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.316
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.33
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.37
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.36
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.36.cold.1
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.3
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.3.cold.1
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.5
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.5.cold.1
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.cold.1
- ___45-[_LTDLanguageAssetCache _multicastObservers]_block_invoke
- ___45-[_LTDLanguageAssetCache _multicastObservers]_block_invoke_2
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.347
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.347.cold.1
- ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.61
- ___53+[_LTDAssetService queryAssetType:filter:completion:]_block_invoke_2
- ___53+[_LTDAssetService queryAssetType:filter:completion:]_block_invoke_3
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.339
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.cold.1
- ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.373
- ___59-[_LTOfflineAssetManager refreshAllIfNeededWithCompletion:]_block_invoke
- ___59-[_LTOfflineAssetManager refreshAllIfNeededWithCompletion:]_block_invoke_2
- ___59-[_LTOfflineAssetManager refreshAllIfNeededWithCompletion:]_block_invoke_3
- ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.54
- ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.305
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.338
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.339
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.333
- ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.16
- ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.16.cold.1
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.28
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.31
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.31.cold.1
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_2.29
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.30
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.30.cold.1
- ___67-[_LTTranslationServer configInfoForLocale:otherLocale:completion:]_block_invoke_2
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353.cold.1
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.312
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.316
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.313
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.313.cold.1
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_3
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_4
- ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.32
- ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.32.cold.1
- ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.51
- ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke_2
- ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke_2.cold.1
- ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke_2.cold.2
- ___83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke.47
- ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.39
- ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.39.cold.1
- ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.51
- ___90-[_LTOfflineTranslationEngine _translate:withContext:toLocale:paragraphResult:completion:]_block_invoke.52
- ___block_descriptor_104_e8_32s40s48s56bs64r72r_e5_v8?0ls32l8s56l8r64l8s40l8r72l8s48l8
- ___block_descriptor_104_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8r80l8s64l8
- ___block_descriptor_32_e41_B32?0"<_LTDAssetModelProtocol>"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_48_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_48_e8_32s40bs_e36_v24?0"_LTDAssetModel"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
- ___block_descriptor_73_e8_32s40s48bs56r_e15_v16?0?<v?B>8ls32l8s40l8s48l8r56l8
- ___block_descriptor_96_e8_32s40s48s56bs64r72r_e8_v16?0Q8ls32l8s56l8r64l8s40l8r72l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64r72r_e17_v16?0"NSError"8ls32l8s40l8r64l8s48l8r72l8s56l8
- ___block_literal_global.299
- ___block_literal_global.304
- ___block_literal_global.312
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.329
- ___block_literal_global.342
- ___block_literal_global.344
- ___block_literal_global.35
- ___block_literal_global.355
- ___block_literal_global.57
- __block_invoke.performingRefresh
- __hasForcedOneTimeCatalogRefresh
- _objc_msgSend$_catalogRefreshInterval
- _objc_msgSend$_forceOneTimeCatalogRefresh
- _objc_msgSend$_isCatalogRefreshWaitExpired
- _objc_msgSend$_isObsoleteCatalogType:
- _objc_msgSend$_multicastObservers
- _objc_msgSend$_refreshAllAssets:
- _objc_msgSend$downloadPriority
- _objc_msgSend$needsCatalogRefresh
- _objc_msgSend$processorCount
- _objc_msgSend$refreshAllIfNeededWithCompletion:
- _objc_msgSend$refreshCatalogIfNeededWithCompletion:
- _objc_msgSend$setNeedsCatalogRefresh:
- _objc_msgSend$timeIntervalSinceNow
CStrings:
+ "ASR failed to complete asset download %{public}@: %@"
+ "Download %{public}@ complete for %zd assets, running symlink validation"
+ "Download %{public}@ complete for %{public}@ but resolved an empty symlink asset list, skipping symlinking"
+ "Download %{public}@ completed item %zd / %zd: %{public}@"
+ "Download %{public}@ deferring symlink validation to cleanupScheduler: %{public}@"
+ "Download %{public}@ doesn't have a cleanupScheduler, directly doing work to validate symlinks"
+ "Download %{public}@ no missing assets detected"
+ "Download %{public}@ start for %zd assets"
+ "Download %{public}@ start item %zd / %zd: %{public}@"
+ "Download %{public}@ symlinks were modified"
+ "Download %{public}@ symlinks were not modified"
+ "Malformed parapragh did not split into sentences as expected: %{sensitive}@"
+ "Sending observer multicast"
+ "Skipping observer multicast due to no updates"
+ "Skipping observer multicast indeterminate update due to no updates"
+ "assetSubtypeForAssetSpecifier:"
+ "downloadAssets"
+ "multicastObservers"
- "Asset catalog updated failure %@"
- "Asset download completed for %{public}@ but resolved an empty symlink asset list, skipping symlinking"
- "B32@?0@\"<_LTDAssetModelProtocol>\"8Q16^B24"
- "Catalog need refresh since last poll not found"
- "Catalog needs refresh since last poll was %zd which exceeds %zd"
- "Catalog needs to refresh since the poll interval has elapsed"
- "Confirmed download %zd / %zd: %{public}@"
- "Confirmed download of %zd assets, running symlink validation"
- "Confirming download of %zd assets"
- "Deferring symlink validation to cleanupScheduler: %{public}@"
- "Detected MA catalog but default provider is UAF."
- "Detected obsolete catalog type: %{public}@"
- "Don't have a cleanupScheduler, directly doing work to validate symlinks"
- "Error reading config asset: %@"
- "Error refreshing config asset %@"
- "Failed to refresh catalog"
- "Failure updating all assets %@"
- "Finished refreshing config asset"
- "Finished updating all assets"
- "Refreshing config asset"
- "Symlinks were modified"
- "Symlinks were not modified"
- "Throttle concurrent downloads to %zd"
- "Update offline asset catalog"
- "_catalogRefreshInterval"
- "_forceOneTimeCatalogRefresh"
- "_isCatalogRefreshWaitExpired"
- "_isObsoleteCatalogType:"
- "_multicastObservers"
- "_refreshAllAssets:"
- "_test_resetForceOneTimeCatalogRefresh"
- "asset_services_uaf"
- "compareDownloadPriority:"
- "downloadPriority"
- "needsCatalogRefresh"
- "processorCount"
- "refreshAllIfNeededWithCompletion:"
- "refreshCatalogIfNeededWithCompletion:"
- "setNeedsCatalogRefresh:"
- "timeIntervalSinceNow"

```
