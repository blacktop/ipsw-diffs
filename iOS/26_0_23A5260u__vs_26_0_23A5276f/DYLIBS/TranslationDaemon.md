## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-336.4.0.0.0
-  __TEXT.__text: 0x18f344
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x199b0
-  __TEXT.__const: 0x440
-  __TEXT.__gcc_except_tab: 0x1b294
-  __TEXT.__cstring: 0x5a97
-  __TEXT.__oslogstring: 0xb25b
+341.0.0.0.0
+  __TEXT.__text: 0x1901b4
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x19a10
+  __TEXT.__const: 0x480
+  __TEXT.__gcc_except_tab: 0x1b220
+  __TEXT.__cstring: 0x5a8f
+  __TEXT.__oslogstring: 0xb547
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf400
+  __TEXT.__unwind_info: 0xf408
   __TEXT.__objc_classname: 0x470b
-  __TEXT.__objc_methname: 0x1ae5c
-  __TEXT.__objc_methtype: 0xdf5d
-  __TEXT.__objc_stubs: 0x12720
+  __TEXT.__objc_methname: 0x1af10
+  __TEXT.__objc_methtype: 0xdf6b
+  __TEXT.__objc_stubs: 0x127e0
   __DATA_CONST.__got: 0xc88
-  __DATA_CONST.__const: 0x40c0
+  __DATA_CONST.__const: 0x4028
   __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x66d0
+  __DATA_CONST.__objc_selrefs: 0x6718
   __DATA_CONST.__objc_superrefs: 0x10f8
   __DATA_CONST.__objc_arraydata: 0x150
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x9a0
-  __AUTH_CONST.__cfstring: 0x7580
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__cfstring: 0x75e0
   __AUTH_CONST.__objc_const: 0x2c170
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_doubleobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0xa2f8
   __DATA.__objc_ivar: 0x1154
   __DATA.__data: 0xa70
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F6FB5146-266C-3A67-B4C5-8F236B941EF0
-  Functions: 9891
-  Symbols:   33610
-  CStrings:  8938
+  UUID: 0804E71D-16A1-3126-A335-B82A9884C2D1
+  Functions: 9900
+  Symbols:   33637
+  CStrings:  8963
 
Symbols:
+ +[MTSchemaMTInvocationEnded(LTTranslationAdditions) lt_initWithExists:localePair:qssSessionId:]
+ +[MTSchemaMTInvocationFailed(LTTranslationAdditions) lt_initWithWithError:localePair:qssSessionId:]
+ +[_LTDASRAssetService _assetTypesForDevice]
+ +[_LTDASRAssetService _availableAssets]
+ +[_LTDASRAssetService _catalog]
+ +[_LTDASRAssetService _requiredAssets]
+ +[_LTDASRAssetService _requiredSFConfigsForAssets:]
+ +[_LTDASRAssetService _selectedLTLocalesIdentifiers]
+ +[_LTDASRAssetService _subscribe:progress:completion:]
+ +[_LTDASRAssetService _subscribe:progress:completion:].cold.1
+ +[_LTDASRAssetService _subscribedSFConfigs]
+ +[_LTDASRAssetService _supportedGASRLocaleIdentifiers]
+ +[_LTDASRAssetService _supportedLTLocaleIdentifiers]
+ +[_LTDASRAssetService _supportsGASR]
+ +[_LTDASRAssetService _supportsNGASR]
+ +[_LTDASRAssetService _unsubscribe:completion:]
+ +[_LTDASRAssetService assetSpecifierForSFConfig:]
+ +[_LTDASRAssetService pathToSFAsset:]
+ +[_LTDASRAssetService queryAssetType:filter:error:]
+ +[_LTDAssetService _addSyntheticASREntriesToAssets:].cold.1
+ +[_LTDAssetService _addSyntheticASREntriesToAssets:].cold.2
+ +[_LTDAssetService _awaitDownloadOfTTSAssets]
+ +[_LTDLanguageAssetService _syncInstalledLocales]
+ +[_LTDSELFLoggingProduction endSuccessfullyWithExists:localePair:qssSessionId:mtId:sessionId:]
+ +[_LTDSELFLoggingProduction endWithError:localePair:qssSessionId:mtId:sessionId:]
+ +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:onDeviceOnly:]
+ +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:onDeviceOnly:].cold.1
+ +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:onDeviceOnly:].cold.2
+ +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:onDeviceOnly:].cold.3
+ -[_LTDASRAssetModel initWithAssetIdentifier:provider:]
+ -[_LTDASRAssetModel initWithAssetIdentifier:provider:].cold.1
+ -[_LTDAssetModel firstComponentAssetWithAssetSubtype:]
+ -[_LTDSELFLoggingManager invocationEndSuccessfullyWithInvocationId:qssSessionId:localePair:]
+ -[_LTDSELFLoggingManager invocationEndSuccessfullyWithInvocationId:qssSessionId:localePair:].cold.1
+ -[_LTDSELFLoggingManager invocationEndWithInvocationId:error:qssSessionId:localePair:]
+ -[_LTDSELFLoggingManager invocationEndWithInvocationId:error:qssSessionId:localePair:].cold.1
+ -[_LTHotfixManager _replaceHotfix:completion:].cold.5
+ -[_LTHotfixManager _versionedHotfixDirectoryNameFromBasePath:]
+ -[_LTHotfixManager _versionedHotfixDirectoryNameFromBasePath:].cold.1
+ _SFEntitledAssetTypeToString
+ __LTLocaleIdentifierMappedForASR
+ ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.26
+ ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.26.cold.1
+ ___35-[_LTDAssetModel localeIdentifiers]_block_invoke
+ ___39+[_LTDASRAssetService _availableAssets]_block_invoke
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.316
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.348
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.348.cold.1
+ ___47+[_LTDASRAssetService _unsubscribe:completion:]_block_invoke
+ ___47+[_LTDASRAssetService _unsubscribe:completion:]_block_invoke.cold.1
+ ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.67
+ ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.70
+ ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.70.cold.1
+ ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.70.cold.2
+ ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.70.cold.3
+ ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke
+ ___51+[_LTDASRAssetService queryAssetType:filter:error:]_block_invoke
+ ___52+[_LTDASRAssetService _supportedLTLocaleIdentifiers]_block_invoke
+ ___52+[_LTDAssetService _addSyntheticASREntriesToAssets:]_block_invoke
+ ___54+[_LTDASRAssetService _subscribe:progress:completion:]_block_invoke
+ ___54+[_LTDASRAssetService _subscribe:progress:completion:]_block_invoke_2
+ ___54+[_LTDASRAssetService _subscribe:progress:completion:]_block_invoke_2.cold.1
+ ___54-[_LTDAssetModel firstComponentAssetWithAssetSubtype:]_block_invoke
+ ___56+[_LTDASRAssetService queryAssetType:filter:completion:]_block_invoke
+ ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.340
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.374
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.36
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.37
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.38
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.39
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.30.cold.2
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.307
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.338
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.339
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.62
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.63
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.66
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67.cold.1
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.67.cold.2
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.333
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.318
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.315
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.315.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.91
+ ___83-[_LTOfflineTranslationEngine _translateParagraph:withContext:toLocale:completion:]_block_invoke_2.cold.1
+ ___85-[_LTOfflineTranslationEngine translateStreamingInput:context:stabilizer:completion:]_block_invoke_2.cold.2
+ ___block_descriptor_40_e8_32s_e24_B16?0"_LTDAssetModel"8ls32l8
+ ___block_descriptor_40_ea8_32bs_e42_v24?0"_LTTranslationResult"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40bs48bs_e42_v24?0"_LTTranslationResult"8"NSError"16ls40l8s32l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs_e18_v16?0"TTSAsset"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e28_v24?0"NSData"8"NSError"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48bs56w_e29_v24?0"NSArray"8"NSError"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s56l8s40l8s48l8
+ ___block_descriptor_81_ea8_32s40s48s56s64bs72w_e42_v24?0"_LTTranslationResult"8"NSError"16lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.205
+ ___block_literal_global.299
+ ___block_literal_global.304
+ ___block_literal_global.312
+ ___block_literal_global.319
+ ___block_literal_global.32
+ ___block_literal_global.329
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.344
+ ___block_literal_global.356
+ __availableAssets.onceToken
+ __availableAssets.shared
+ _kLTAssetTypeASR
+ _objc_msgSend$_availableAssets
+ _objc_msgSend$_awaitDownloadOfTTSAssets
+ _objc_msgSend$_requiredAssets
+ _objc_msgSend$_requiredSFConfigsForAssets:
+ _objc_msgSend$_selectedLTLocalesIdentifiers
+ _objc_msgSend$_subscribe:progress:completion:
+ _objc_msgSend$_subscribedSFConfigs
+ _objc_msgSend$_supportedGASRLocaleIdentifiers
+ _objc_msgSend$_supportedLTLocaleIdentifiers
+ _objc_msgSend$_supportsGASR
+ _objc_msgSend$_supportsNGASR
+ _objc_msgSend$_syncInstalledLocales
+ _objc_msgSend$_versionedHotfixDirectoryNameFromBasePath:
+ _objc_msgSend$assetSpecifierForSFConfig:
+ _objc_msgSend$bestAssetOfTypes:matching:
+ _objc_msgSend$combinedVoice
+ _objc_msgSend$componentFilter
+ _objc_msgSend$customVoice
+ _objc_msgSend$endSuccessfullyWithExists:localePair:qssSessionId:mtId:sessionId:
+ _objc_msgSend$endWithError:localePair:qssSessionId:mtId:sessionId:
+ _objc_msgSend$initWithAssetIdentifier:provider:
+ _objc_msgSend$initWithLanguage:assetType:
+ _objc_msgSend$invocationEndSuccessfullyWithInvocationId:qssSessionId:localePair:
+ _objc_msgSend$invocationEndWithInvocationId:error:qssSessionId:localePair:
+ _objc_msgSend$lt_initWithExists:localePair:qssSessionId:
+ _objc_msgSend$lt_initWithWithError:localePair:qssSessionId:
+ _objc_msgSend$pathToSFAsset:
+ _objc_msgSend$subscriptionsForClientIdentifier:
+ _objc_msgSend$ttsAssetForLocaleIdentifier:onDeviceOnly:
- +[MTSchemaMTInvocationEnded(LTTranslationAdditions) lt_initWithExists:qssSessionId:]
- +[MTSchemaMTInvocationFailed(LTTranslationAdditions) lt_initWithWithError:qssSessionId:]
- +[_LTDASRAssetService _assetTypesFoDevice]
- +[_LTDASRAssetService _downloadAsset:progress:completion:]
- +[_LTDASRAssetService _purgeAsset:completion:]
- +[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]
- +[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]
- +[_LTDASRAssetService _sfTaskHintForLTTaskHint:]
- +[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]
- +[_LTDASRAssetService _taskHintForLTAssetType:]
- +[_LTDASRAssetService asrAssetWithIdentifier:taskHint:]
- +[_LTDASRAssetService availableAssetsWithCompletion:]
- +[_LTDASRAssetService installedAssetsWithCompletion:]
- +[_LTDLanguageAssetService syncInstalledLocales]
- +[_LTDSELFLoggingProduction endSuccessfullyWithExists:qssSessionId:mtId:sessionId:]
- +[_LTDSELFLoggingProduction endWithError:qssSessionId:mtId:sessionId:]
- +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:]
- +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:].cold.1
- -[_LTDASRAssetModel initWithAssetIdentifier:].cold.1
- -[_LTDASRAssetModel setAssetPath:]
- -[_LTDASRAssetModel setProvider:]
- -[_LTDSELFLoggingManager invocationEndSuccessfullyWithInvocationId:qssSessionId:]
- -[_LTDSELFLoggingManager invocationEndSuccessfullyWithInvocationId:qssSessionId:].cold.1
- -[_LTDSELFLoggingManager invocationEndWithInvocationId:error:qssSessionId:]
- -[_LTDSELFLoggingManager invocationEndWithInvocationId:error:qssSessionId:].cold.1
- ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.20
- ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.20.cold.1
- ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.313
- ___46+[_LTDASRAssetService _purgeAsset:completion:]_block_invoke
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.345
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.345.cold.1
- ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.66
- ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.69
- ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.69.cold.1
- ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.69.cold.2
- ___47-[_LTHotfixManager _downloadHotfix:completion:]_block_invoke.69.cold.3
- ___48+[_LTDLanguageAssetService syncInstalledLocales]_block_invoke
- ___48+[_LTDLanguageAssetService syncInstalledLocales]_block_invoke_2
- ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke
- ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke_2
- ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke_3
- ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke
- ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke_2
- ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke_3
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.337
- ___58+[_LTDASRAssetService _downloadAsset:progress:completion:]_block_invoke
- ___58+[_LTDASRAssetService _downloadAsset:progress:completion:]_block_invoke_2
- ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.371
- ___60+[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]_block_invoke
- ___60+[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]_block_invoke_2
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.40
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.41
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.42
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.43
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34.cold.2
- ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.302
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.335
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.336
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.50
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.51
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.54
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55.cold.1
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55.cold.2
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.330
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.309
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.310
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.310.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93
- ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke
- ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke_2
- ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke_3
- ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke
- ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke_2
- ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke_3
- ___block_descriptor_40_ea8_32bs_e30_v16?0"_LTTranslationResult"8ls32l8
- ___block_descriptor_48_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e39_v24?0"_LTDASRAssetModel"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e28_"NSString"16?0"NSString"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e18_v16?0"TTSAsset"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e15_v16?0"NSSet"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40bs48bs_e30_v16?0"_LTTranslationResult"8ls40l8s32l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e27_v24?0"NSSet"8"NSError"16lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48bs56w_e29_v24?0"NSArray"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_81_ea8_32s40s48s56s64bs72w_e30_v16?0"_LTTranslationResult"8lw72l8s64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.202
- ___block_literal_global.29
- ___block_literal_global.301
- ___block_literal_global.309
- ___block_literal_global.316
- ___block_literal_global.322
- ___block_literal_global.323
- ___block_literal_global.340
- ___block_literal_global.341
- ___block_literal_global.342
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.38
- ___block_literal_global.50
- _objc_msgSend$_assetTypesFoDevice
- _objc_msgSend$_downloadAsset:progress:completion:
- _objc_msgSend$_purgeAsset:completion:
- _objc_msgSend$_sfInstalledLTIdentifiersForTaskHint:filter:completion:
- _objc_msgSend$_sfSupportedLTIdentifiersForTaskHint:filter:completion:
- _objc_msgSend$_sfTaskHintForLTTaskHint:
- _objc_msgSend$_supportedIdentifiersWithCommpletion:
- _objc_msgSend$_taskHintForLTAssetType:
- _objc_msgSend$asrAssetWithIdentifier:taskHint:
- _objc_msgSend$availableAssetsWithCompletion:
- _objc_msgSend$endSuccessfullyWithExists:qssSessionId:mtId:sessionId:
- _objc_msgSend$endWithError:qssSessionId:mtId:sessionId:
- _objc_msgSend$initWithLanguage:taskHint:
- _objc_msgSend$installedLanguagesForTaskHint:completion:
- _objc_msgSend$invocationEndSuccessfullyWithInvocationId:qssSessionId:
- _objc_msgSend$invocationEndWithInvocationId:error:qssSessionId:
- _objc_msgSend$isSupportedTaskHint:
- _objc_msgSend$lt_initWithExists:qssSessionId:
- _objc_msgSend$lt_initWithWithError:qssSessionId:
- _objc_msgSend$setAssetPath:
- _objc_msgSend$supportedIdentifiersForTask:completion:
- _objc_msgSend$supportedLanguagesForTaskHint:completion:
- _objc_msgSend$ttsAssetForLocaleIdentifier:
CStrings:
+ "ASR subscribe for %{public}@ failure: %@"
+ "ASR unsubscribe for %{public}@ failure: %@"
+ "ASR-%@_%@"
+ "ASRDataPackDefaultLIDThresholdVersion"
+ "Actually in subscribe for %@"
+ "Add missing subscription for %{public}@"
+ "At least one sentence encountered an error translating: %@"
+ "Failed to lookup child folders of Hotfix base path %{public}@"
+ "Failed to obtain asset specifier for ASR asset %{public}@"
+ "Failed to translate streaming input: %@"
+ "LTDHotfixManagerError"
+ "Models - sourceASR: %{BOOL}i (ignored), targetASR %{BOOL}i (ignored), mt: %{BOOL}i"
+ "Queried LID threshold version '%{public}@' for model version '%{public}@'; useFinalThresholds: %{BOOL}i; isFinalASR: %{BOOL}i; detected %{public}@, with score %f using discriminator threshold %{public}@%f and confidence offset %f (confident: %{BOOL}i)"
+ "Remove orphaned subscription for %@"
+ "Rolled back hotfix directory doesn't have a versioned subdirectory"
+ "Skipping invalid non-ASR asset %{public}@"
+ "Subscribe request with nil SFEntitledAssetConfig"
+ "Synthetic ASR continuing with failure %@"
+ "Synthetic ASR early return with failure %@"
+ "T@\"SFEntitledAssetConfig\",R,N,V_provider"
+ "TTS: Choosing: %@"
+ "TTS: bestAsset didn't find anything on-device, falling back to manual search"
+ "_assetTypesForDevice"
+ "_availableAssets"
+ "_awaitDownloadOfTTSAssets"
+ "_requiredAssets"
+ "_requiredSFConfigsForAssets:"
+ "_selectedLTLocalesIdentifiers"
+ "_subscribe:progress:completion:"
+ "_subscribedSFConfigs"
+ "_supportedGASRLocaleIdentifiers"
+ "_supportedLTLocaleIdentifiers"
+ "_supportsGASR"
+ "_supportsNGASR"
+ "_syncInstalledLocales"
+ "_versionedHotfixDirectoryNameFromBasePath:"
+ "asrCatalog"
+ "assetSpecifierForSFConfig:"
+ "bestAssetOfTypes:matching:"
+ "com.apple.speech.automaticspeechrecognition"
+ "combinedVoice"
+ "componentFilter"
+ "customVoice"
+ "endSuccessfullyWithExists:localePair:qssSessionId:mtId:sessionId:"
+ "endWithError:localePair:qssSessionId:mtId:sessionId:"
+ "firstComponentAssetWithAssetSubtype:"
+ "initWithAssetIdentifier:provider:"
+ "initWithLanguage:assetType:"
+ "invocationEndSuccessfullyWithInvocationId:qssSessionId:localePair:"
+ "invocationEndWithInvocationId:error:qssSessionId:localePair:"
+ "lt_initWithExists:localePair:qssSessionId:"
+ "lt_initWithWithError:localePair:qssSessionId:"
+ "pathToSFAsset:"
+ "subscriptionsForClientIdentifier:"
+ "ttsAssetForLocaleIdentifier:onDeviceOnly:"
+ "v52@0:8B16@\"_LTLocalePair\"20@\"SISchemaUUID\"28@\"SISchemaUUID\"36@\"SISchemaUUID\"44"
+ "v56@0:8@\"NSError\"16@\"_LTLocalePair\"24@\"SISchemaUUID\"32@\"SISchemaUUID\"40@\"SISchemaUUID\"48"
+ "v56@0:8@16@24@32@40@48"
+ "|TTS"
- "@28@0:8B16@20"
- "Add missing subscripton for %{public}@"
- "DisableSyncInstalledLocalesOnLaunch"
- "HotfixManager"
- "Queried LID threshold version '%{public}@'; useFinalThresholds: %{BOOL}i; isFinalASR: %{BOOL}i; detected %{public}@, with score %f using discriminator threshold %{public}@%f and confidence offset %f (confident: %{BOOL}i)"
- "Remove ophaned subscripton for %@"
- "T@\"SFEntitledAssetConfig\",&,N,V_provider"
- "UAF asset download failure due to network"
- "_assetTypesFoDevice"
- "_downloadAsset:progress:completion:"
- "_purgeAsset:completion:"
- "_sfInstalledLTIdentifiersForTaskHint:filter:completion:"
- "_sfSupportedLTIdentifiersForTaskHint:filter:completion:"
- "_sfTaskHintForLTTaskHint:"
- "_supportedIdentifiersWithCommpletion:"
- "_taskHintForLTAssetType:"
- "asrAssetWithIdentifier:taskHint:"
- "availableAssetsWithCompletion:"
- "endSuccessfullyWithExists:qssSessionId:mtId:sessionId:"
- "endWithError:qssSessionId:mtId:sessionId:"
- "initWithLanguage:taskHint:"
- "installedLanguagesForTaskHint:completion:"
- "invocationEndSuccessfullyWithInvocationId:qssSessionId:"
- "invocationEndWithInvocationId:error:qssSessionId:"
- "lt_initWithExists:qssSessionId:"
- "lt_initWithWithError:qssSessionId:"
- "q24@0:8q16"
- "setAssetPath:"
- "supportedLanguagesForTaskHint:completion:"
- "syncInstalledLocales"
- "ttsAssetForLocaleIdentifier:"
- "v16@?0@\"NSSet\"8"
- "v24@?0@\"NSSet\"8@\"NSError\"16"
- "v24@?0@\"_LTDASRAssetModel\"8@\"NSError\"16"
- "v44@0:8B16@\"SISchemaUUID\"20@\"SISchemaUUID\"28@\"SISchemaUUID\"36"
- "v44@0:8B16@20@28@36"
- "v48@0:8@\"NSError\"16@\"SISchemaUUID\"24@\"SISchemaUUID\"32@\"SISchemaUUID\"40"

```
