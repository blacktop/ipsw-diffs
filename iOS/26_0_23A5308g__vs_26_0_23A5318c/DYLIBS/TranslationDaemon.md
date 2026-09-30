## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-348.1.0.0.0
-  __TEXT.__text: 0x190d8c
+350.1.0.0.0
+  __TEXT.__text: 0x1931e0
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x199f0
+  __TEXT.__objc_methlist: 0x19bc0
   __TEXT.__const: 0x450
   __TEXT.__gcc_except_tab: 0x1b308
-  __TEXT.__cstring: 0x5a8a
-  __TEXT.__oslogstring: 0xbb83
+  __TEXT.__cstring: 0x5ac1
+  __TEXT.__oslogstring: 0xc0ac
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf410
-  __TEXT.__objc_classname: 0x470b
-  __TEXT.__objc_methname: 0x1aec9
-  __TEXT.__objc_methtype: 0xdf6b
-  __TEXT.__objc_stubs: 0x12760
+  __TEXT.__unwind_info: 0xf448
+  __TEXT.__objc_classname: 0x4749
+  __TEXT.__objc_methname: 0x1b146
+  __TEXT.__objc_methtype: 0xdfac
+  __TEXT.__objc_stubs: 0x128e0
   __DATA_CONST.__got: 0xc98
-  __DATA_CONST.__const: 0x3ee8
-  __DATA_CONST.__objc_classlist: 0x1188
+  __DATA_CONST.__const: 0x3f50
+  __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x66f8
-  __DATA_CONST.__objc_superrefs: 0x10f8
+  __DATA_CONST.__objc_selrefs: 0x6778
+  __DATA_CONST.__objc_superrefs: 0x1108
   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x7620
-  __AUTH_CONST.__objc_const: 0x2c150
+  __AUTH_CONST.__const: 0xa80
+  __AUTH_CONST.__cfstring: 0x7660
+  __AUTH_CONST.__objc_const: 0x2c470
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH.__objc_data: 0xa2f8
-  __DATA.__objc_ivar: 0x1154
+  __AUTH.__objc_data: 0xa398
+  __DATA.__objc_ivar: 0x117c
   __DATA.__data: 0xa68
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x1e8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08B6A923-8668-3892-94D5-00BCF1F934AD
-  Functions: 9898
-  Symbols:   33638
-  CStrings:  8989
+  UUID: F445A13F-BC34-3D95-BCEC-C3A5A750438D
+  Functions: 9945
+  Symbols:   33778
+  CStrings:  9042
 
Symbols:
+ +[_LTDASRAssetService _downloadAsset:options:progress:completion:]
+ +[_LTDASRAssetService _downloadAsset:options:progress:completion:].cold.1
+ +[_LTDASRAssetService _scheduleNextDownloadIfNeededWithCompletedDownloadEntry:]
+ +[_LTDASRAssetService pendingDownloadSchedulingAssetsNameToEntry]
+ +[_LTDASRAssetService pendingDownloadSchedulingAssetsNameToEntry].cold.1
+ +[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]
+ +[_LTDUAFAssetService _cancelDeferredUnsubscribeTimer]
+ +[_LTDUAFAssetService _deferredUnsubscribe]
+ +[_LTDUAFAssetService _downloadAsset:options:progress:completion:]
+ +[_LTDUAFAssetService _downloadAsset:options:progress:completion:].cold.1
+ +[_LTDUAFAssetService _ensureAssetDownloadCompletion:progress:]
+ +[_LTDUAFAssetService _registerOneTimeChangeHandler:]
+ +[_LTDUAFAssetService _scheduleNextDownloadIfNeededWithCompletedDownloadEntry:]
+ +[_LTDUAFAssetService _subscribeWithAssetSpecifiers:completion:]
+ +[_LTDUAFAssetService _subscribeWithAssetSpecifiers:completion:].cold.1
+ +[_LTDUAFAssetService _unsubscribeWithAssetSpecifiers:completion:]
+ +[_LTDUAFAssetService _updateDeferredUnsubscribeTimer]
+ +[_LTDUAFAssetService _updateDeferredUnsubscribeTimer].cold.1
+ +[_LTDUAFAssetService pendingDownloadSchedulingAssetsNameToEntry]
+ +[_LTDUAFAssetService pendingDownloadSchedulingAssetsNameToEntry].cold.1
+ -[_LTDASRAssetModelDownloadEntry .cxx_destruct]
+ -[_LTDASRAssetModelDownloadEntry asset]
+ -[_LTDASRAssetModelDownloadEntry completion]
+ -[_LTDASRAssetModelDownloadEntry duplicateEntries]
+ -[_LTDASRAssetModelDownloadEntry initWithAsset:options:progress:completion:]
+ -[_LTDASRAssetModelDownloadEntry options]
+ -[_LTDASRAssetModelDownloadEntry progress]
+ -[_LTDASRAssetModelDownloadEntry setAsset:]
+ -[_LTDASRAssetModelDownloadEntry setCompletion:]
+ -[_LTDASRAssetModelDownloadEntry setDuplicateEntries:]
+ -[_LTDASRAssetModelDownloadEntry setOptions:]
+ -[_LTDASRAssetModelDownloadEntry setProgress:]
+ -[_LTDAssetModelDownloadEntry .cxx_destruct]
+ -[_LTDAssetModelDownloadEntry asset]
+ -[_LTDAssetModelDownloadEntry completion]
+ -[_LTDAssetModelDownloadEntry duplicateEntries]
+ -[_LTDAssetModelDownloadEntry initWithAsset:options:progress:completion:]
+ -[_LTDAssetModelDownloadEntry options]
+ -[_LTDAssetModelDownloadEntry progress]
+ -[_LTDAssetModelDownloadEntry setAsset:]
+ -[_LTDAssetModelDownloadEntry setCompletion:]
+ -[_LTDAssetModelDownloadEntry setDuplicateEntries:]
+ -[_LTDAssetModelDownloadEntry setOptions:]
+ -[_LTDAssetModelDownloadEntry setProgress:]
+ _OBJC_CLASS_$__LTDASRAssetModelDownloadEntry
+ _OBJC_CLASS_$__LTDAssetModelDownloadEntry
+ _OBJC_IVAR_$__LTDASRAssetModelDownloadEntry._asset
+ _OBJC_IVAR_$__LTDASRAssetModelDownloadEntry._completion
+ _OBJC_IVAR_$__LTDASRAssetModelDownloadEntry._duplicateEntries
+ _OBJC_IVAR_$__LTDASRAssetModelDownloadEntry._options
+ _OBJC_IVAR_$__LTDASRAssetModelDownloadEntry._progress
+ _OBJC_IVAR_$__LTDAssetModelDownloadEntry._asset
+ _OBJC_IVAR_$__LTDAssetModelDownloadEntry._completion
+ _OBJC_IVAR_$__LTDAssetModelDownloadEntry._duplicateEntries
+ _OBJC_IVAR_$__LTDAssetModelDownloadEntry._options
+ _OBJC_IVAR_$__LTDAssetModelDownloadEntry._progress
+ _OBJC_METACLASS_$__LTDASRAssetModelDownloadEntry
+ _OBJC_METACLASS_$__LTDAssetModelDownloadEntry
+ __LTPreferencesOVADAudioBufferDuration
+ __LTPreferencesOVADPendingSwapTimeoutDuration
+ __OBJC_$_INSTANCE_METHODS__LTDASRAssetModelDownloadEntry
+ __OBJC_$_INSTANCE_METHODS__LTDAssetModelDownloadEntry
+ __OBJC_$_INSTANCE_VARIABLES__LTDASRAssetModelDownloadEntry
+ __OBJC_$_INSTANCE_VARIABLES__LTDAssetModelDownloadEntry
+ __OBJC_$_PROP_LIST__LTDASRAssetModelDownloadEntry
+ __OBJC_$_PROP_LIST__LTDAssetModelDownloadEntry
+ __OBJC_CLASS_RO_$__LTDASRAssetModelDownloadEntry
+ __OBJC_CLASS_RO_$__LTDAssetModelDownloadEntry
+ __OBJC_METACLASS_RO_$__LTDASRAssetModelDownloadEntry
+ __OBJC_METACLASS_RO_$__LTDAssetModelDownloadEntry
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.358
+ ___53+[_LTDUAFAssetService _registerOneTimeChangeHandler:]_block_invoke
+ ___54+[_LTDUAFAssetService _updateDeferredUnsubscribeTimer]_block_invoke
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.44
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.38.cold.2
+ ___64+[_LTDLanguageAssetService _syncInstalledLocalesWithCompletion:]_block_invoke_2.cold.1
+ ___65+[_LTDASRAssetService pendingDownloadSchedulingAssetsNameToEntry]_block_invoke
+ ___65+[_LTDUAFAssetService pendingDownloadSchedulingAssetsNameToEntry]_block_invoke
+ ___66+[_LTDASRAssetService _downloadAsset:options:progress:completion:]_block_invoke
+ ___66+[_LTDASRAssetService _downloadAsset:options:progress:completion:]_block_invoke_2
+ ___66+[_LTDASRAssetService _downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.35
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke.35.cold.1
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke_2
+ ___66+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:gateID:]_block_invoke_2.cold.1
+ ___66+[_LTDUAFAssetService _downloadAsset:options:progress:completion:]_block_invoke
+ ___66+[_LTDUAFAssetService _downloadAsset:options:progress:completion:]_block_invoke_2
+ ___66+[_LTDUAFAssetService _downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.397
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.397.cold.1
+ ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.398
+ ___block_descriptor_56_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40bs48bs56r_e5_v8?0lr56l8s40l8s32l8s48l8
+ ___block_descriptor_72_e8_32s40bs48bs56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
+ ___block_literal_global.211
+ ___block_literal_global.334
+ ___block_literal_global.336
+ ___block_literal_global.346
+ ___block_literal_global.361
+ ___block_literal_global.369
+ ___block_literal_global.372
+ ___block_literal_global.388
+ ___block_literal_global.42
+ ___block_literal_global.53
+ __downloadThrottlingLock
+ __syncInstalledLocalesWithRetry:gateID:.retryGate
+ _objc_msgSend$_cancelDeferredUnsubscribeTimer
+ _objc_msgSend$_deferredUnsubscribe
+ _objc_msgSend$_downloadAsset:options:progress:completion:
+ _objc_msgSend$_ensureAssetDownloadCompletion:progress:
+ _objc_msgSend$_registerOneTimeChangeHandler:
+ _objc_msgSend$_scheduleNextDownloadIfNeededWithCompletedDownloadEntry:
+ _objc_msgSend$_subscribeWithAssetSpecifiers:completion:
+ _objc_msgSend$_syncInstalledLocalesWithRetry:gateID:
+ _objc_msgSend$_unsubscribeWithAssetSpecifiers:completion:
+ _objc_msgSend$_updateDeferredUnsubscribeTimer
+ _objc_msgSend$asset
+ _objc_msgSend$duplicateEntries
+ _objc_msgSend$initWithAsset:options:progress:completion:
+ _objc_msgSend$pendingDownloadSchedulingAssetsNameToEntry
+ _objc_msgSend$setDuplicateEntries:
+ _pendingDownloadSchedulingAssetsNameToEntry._pendingDownloadSchedulingAssets
+ _pendingDownloadSchedulingAssetsNameToEntry.onceToken
- +[_LTDASRAssetService downloadAsset:options:progress:completion:].cold.1
- +[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]
- +[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:].cold.1
- +[_LTDUAFAssetService downloadAsset:options:progress:completion:].cold.1
- ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.316
- ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke
- ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke.36
- ___49+[_LTDLanguageAssetService _syncInstalledLocales]_block_invoke_2
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.48
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.39.cold.2
- ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke
- ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke_2
- ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.333
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.cold.1
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke_2
- ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353
- ___69+[_LTDUAFAssetService _registerForAsset:options:progress:completion:]_block_invoke.353.cold.1
- ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke
- ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke.35
- ___70+[_LTDLanguageAssetService _syncInstalledLocalesWithRetry:completion:]_block_invoke.35.cold.1
- ___block_descriptor_56_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
- ___block_descriptor_80_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
- ___block_literal_global.205
- ___block_literal_global.294
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.319
- ___block_literal_global.326
- ___block_literal_global.329
- ___block_literal_global.347
- ___block_literal_global.38
- ___block_literal_global.41
- ___block_literal_global.43
- ___block_literal_global.54
- __syncInstalledLocales.retryGate
- _objc_msgSend$_purgeUnusedAssetsWithCompletion:
- _objc_msgSend$_subscribe:completion:
- _objc_msgSend$_syncInstalledLocalesWithRetry:completion:
CStrings:
+ "@\"<_LTDAssetModelProtocol>\""
+ "@48@0:8@16Q24@?32@?40"
+ "ASR Asset download completed name %@, location %@"
+ "ASR Asset downloads completed all pending downloads"
+ "ASR Asset downloads downloads starting first download of %@"
+ "ASR Asset downloads finished download"
+ "ASR Asset downloads finished downloading assets %@ pending assets count %lu"
+ "ASR Asset downloads found existing same entry %@"
+ "ASR Asset downloads re-enqueue same assets %@"
+ "ASR Asset downloads successfully finished with deduped entries %@"
+ "ASR Asset downloads updating offlineStatus and calling completion on the duplicate entry assets %@"
+ "ASR Asset in the _catalog"
+ "B32@0:8@16@?24"
+ "Found missing subscriptions for %{public}@"
+ "MT assets purging timer fired"
+ "OVADAudioBufferDuration"
+ "OVADPendingSwapTimeoutDuration"
+ "Remove orphaned MT subscription for %@"
+ "Sync install set assets progress count: %zd"
+ "Sync retry attempt %zd:[%{public}@] begin"
+ "Sync retry attempt %zd:[%{public}@] in %zd secs for failure: %@"
+ "Sync retry attempt %zd:[%{public}@] succeeded"
+ "Sync retry attempt [%{public}@] retries exhausted"
+ "T@\"<_LTDAssetModelProtocol>\",&,N,V_asset"
+ "T@\"NSMutableArray\",&,N,V_duplicateEntries"
+ "T@?,C,N,V_progress"
+ "TQ,N,V_options"
+ "UAF Asset downloads downloads starting first download of %@"
+ "UAF Asset downloads finished download"
+ "UAF Asset downloads finished downloading assets %@ pending assets count %lu"
+ "UAF Asset downloads found existing same entry %@"
+ "UAF Asset downloads re-enqueue same assets %@"
+ "UAF Asset downloads successfully finished with deduped entries %@"
+ "UAF Asset downloads updating offlineStatus and calling completion on the duplicate entry assets %@"
+ "UAF Asset in the _catalog"
+ "UAF asset download completed but not found, scheduling update event observation for %@"
+ "UAF asset download completed but still not found after receiving update event for %@"
+ "UAF asset download completed name %@, location %@"
+ "UAF asset download fully completed: %@"
+ "UAF asset download one time update event"
+ "Updating MT assets purging timer"
+ "Updating subscription with %{public}@"
+ "_LTDASRAssetModelDownloadEntry"
+ "_LTDAssetModelDownloadEntry"
+ "_cancelDeferredUnsubscribeTimer"
+ "_deferredUnsubscribe"
+ "_downloadAsset:options:progress:completion:"
+ "_duplicateEntries"
+ "_ensureAssetDownloadCompletion:progress:"
+ "_options"
+ "_registerOneTimeChangeHandler:"
+ "_scheduleNextDownloadIfNeededWithCompletedDownloadEntry:"
+ "_subscribeWithAssetSpecifiers:completion:"
+ "_syncInstalledLocalesWithRetry:gateID:"
+ "_unsubscribeWithAssetSpecifiers:completion:"
+ "_updateDeferredUnsubscribeTimer"
+ "asset"
+ "duplicateEntries"
+ "initWithAsset:options:progress:completion:"
+ "pendingDownloadSchedulingAssetsNameToEntry"
+ "setAsset:"
+ "setDuplicateEntries:"
+ "setProgress:"
- "Add missing subscription for %{public}@"
- "Asset subscription %{public}@ failure %@"
- "Remove orphaned subscription for %@"
- "Sync install set assets progress: %@"
- "Sync installed begin"
- "Sync installed ended"
- "Sync retry attempt %zd begin"
- "Sync retry attempt %zd dispatch after %zd sec"
- "Sync retry attempt %zd ended"
- "Sync retry attempt %zd ended with failure: %@"
- "Sync retry exhausted attemps, no further attempts will be made for the active request"
- "_syncInstalledLocalesWithRetry:completion:"

```
