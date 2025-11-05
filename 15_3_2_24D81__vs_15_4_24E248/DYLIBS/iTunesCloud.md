## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Versions/A/iTunesCloud`

```diff

-4024.440.1.0.0
-  __TEXT.__text: 0x2d6108
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x14fd0
-  __TEXT.__const: 0x266c8
-  __TEXT.__gcc_except_tab: 0x31f4
-  __TEXT.__cstring: 0x165fa
-  __TEXT.__oslogstring: 0x1dde7
-  __TEXT.__ustring: 0x8e
+4024.540.1.0.0
+  __TEXT.__text: 0x2dd274
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x1731c
+  __TEXT.__const: 0x26598
   __TEXT.__dlopen_cstrs: 0x2ff
-  __TEXT.__unwind_info: 0x6380
+  __TEXT.__gcc_except_tab: 0x3290
+  __TEXT.__cstring: 0x167c1
+  __TEXT.__oslogstring: 0x1e2e2
+  __TEXT.__ustring: 0x8e
+  __TEXT.__unwind_info: 0x6238
   __TEXT.__eh_frame: 0x84
-  __TEXT.__objc_classname: 0x3a90
-  __TEXT.__objc_methname: 0x3340a
-  __TEXT.__objc_methtype: 0x7814
-  __TEXT.__objc_stubs: 0x1a3c0
-  __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__const: 0x2430
-  __DATA_CONST.__objc_classlist: 0xd50
+  __TEXT.__objc_classname: 0x3aa9
+  __TEXT.__objc_methname: 0x33940
+  __TEXT.__objc_methtype: 0x78c6
+  __TEXT.__objc_stubs: 0x1a740
+  __DATA_CONST.__got: 0xf50
+  __DATA_CONST.__const: 0x2480
+  __DATA_CONST.__objc_classlist: 0xd58
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9580
+  __DATA_CONST.__objc_selrefs: 0x9c70
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xb70
+  __DATA_CONST.__objc_superrefs: 0xb78
   __DATA_CONST.__objc_arraydata: 0x468
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH_CONST.__const: 0x1a5f0
-  __AUTH_CONST.__cfstring: 0x17c40
-  __AUTH_CONST.__objc_const: 0x32d48
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__const: 0x1b250
+  __AUTH_CONST.__cfstring: 0x17d40
+  __AUTH_CONST.__objc_const: 0x2f038
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x2580
-  __DATA.__objc_ivar: 0x227c
-  __DATA.__data: 0x2368
+  __AUTH.__objc_data: 0x25d0
+  __DATA.__objc_ivar: 0x22a0
+  __DATA.__data: 0x2398
+  __DATA.__bss: 0x588
   __DATA.__common: 0xa4c
-  __DATA.__bss: 0x578
   __DATA_DIRTY.__objc_data: 0x5fa0
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2E962FCA-3E93-3BF8-887A-CBBBCECD5888
-  Functions: 9825
-  Symbols:   21103
-  CStrings:  17154
+  UUID: 8BBA1D4E-305B-30F7-859A-758412EA8C30
+  Functions: 9646
+  Symbols:   21185
+  CStrings:  17241
 
Symbols:
+ +[ICBackgroundTaskScheduler sharedTaskScheduler]
+ +[ICUserIdentity autoupdatingDefaultMediaIdentity]
+ -[ICBackgroundTaskScheduler .cxx_destruct]
+ -[ICBackgroundTaskScheduler _init]
+ -[ICBackgroundTaskScheduler _loadSavedTaskInfo]
+ -[ICBackgroundTaskScheduler _postExpiredEvents]
+ -[ICBackgroundTaskScheduler _saveTaskInfo]
+ -[ICBackgroundTaskScheduler _scheduleNextTask]
+ -[ICBackgroundTaskScheduler cancelTask:]
+ -[ICBackgroundTaskScheduler hasScheduledTask:]
+ -[ICBackgroundTaskScheduler registerForTask:handler:]
+ -[ICBackgroundTaskScheduler scheduleRecurringTask:withInterval:afterDelay:withUserData:]
+ -[ICBackgroundTaskScheduler scheduleTask:afterDelay:withUserData:]
+ -[ICCloudClient importContainerArtworkForSagaID:artworkVariantType:completionHandler:]
+ -[ICDefaults sagaPushNotificationTimes]
+ -[ICDefaults setSagaPushNotificationTimes:]
+ -[ICHomeManager _postPropertiesChangedNotification]
+ -[ICLibraryAuthServiceClientTokenProvider _checkTokenPresetsForDSIDs:forceRefresh:]
+ -[ICLibraryAuthServiceClientTokenProvider _devicePresetErrorForConfiguration:WithSpecifiedDSIDs:]
+ -[ICLibraryAuthServiceClientTokenProvider _devicePresetForConfiguration:withDSIDs:]
+ -[ICLibraryAuthServiceClientTokenProvider _devicePresetNonDiscriminatoryFailForConfiguration:]
+ -[ICLibraryAuthServiceClientTokenProvider _devicePresetNonDiscriminatorySucceedForConfiguration:DSIDsToUse:]
+ -[ICMusicSubscriptionStatusMonitor _handleHomeManagerPropertiesDidChange:]
+ -[ICRequestContext _requestNotificationsEnabled]
+ -[ICRequestContext enableRequestNotifications]
+ -[ICRequestContext setTag:]
+ -[ICRequestContext tag]
+ -[ICURLRequest _requestWasEnqueuedAt:]
+ -[ICURLRequest _sanitizedURLString]
+ -[ICURLRequest _task:didCompleteWithError:at:]
+ -[ICURLRequest _task:didReceiveInitialResponse:at:]
+ -[ICURLRequest _task:didResumeAt:]
+ -[ICURLRequest observers]
+ -[ICURLRequest requestID]
+ -[ICURLRequest requestName]
+ -[ICURLRequest setRequestName:]
+ -[ICUserIdentityStoreACAccountBackend defaultMediaAccountDSIDWithError:]
+ -[ICUserIdentityStoreTestingBackend defaultMediaAccountDSIDWithError:]
+ GCC_except_table1082
+ GCC_except_table1109
+ GCC_except_table1244
+ GCC_except_table1320
+ GCC_except_table148
+ GCC_except_table1488
+ GCC_except_table1501
+ GCC_except_table1689
+ GCC_except_table1872
+ GCC_except_table1903
+ GCC_except_table1918
+ GCC_except_table1960
+ GCC_except_table2073
+ GCC_except_table2089
+ GCC_except_table2138
+ GCC_except_table2140
+ GCC_except_table2146
+ GCC_except_table2153
+ GCC_except_table2181
+ GCC_except_table2195
+ GCC_except_table2200
+ GCC_except_table2202
+ GCC_except_table2210
+ GCC_except_table2223
+ GCC_except_table2319
+ GCC_except_table2361
+ GCC_except_table2392
+ GCC_except_table2394
+ GCC_except_table2396
+ GCC_except_table2398
+ GCC_except_table2748
+ GCC_except_table2800
+ GCC_except_table2962
+ GCC_except_table2979
+ GCC_except_table2991
+ GCC_except_table3014
+ GCC_except_table37
+ GCC_except_table4084
+ GCC_except_table4088
+ GCC_except_table4090
+ GCC_except_table4092
+ GCC_except_table4096
+ GCC_except_table4103
+ GCC_except_table4107
+ GCC_except_table4122
+ GCC_except_table4126
+ GCC_except_table425
+ GCC_except_table4305
+ GCC_except_table432
+ GCC_except_table4358
+ GCC_except_table4362
+ GCC_except_table4365
+ GCC_except_table4370
+ GCC_except_table4434
+ GCC_except_table4476
+ GCC_except_table4480
+ GCC_except_table4482
+ GCC_except_table4549
+ GCC_except_table4624
+ GCC_except_table4784
+ GCC_except_table4852
+ GCC_except_table4933
+ GCC_except_table5097
+ GCC_except_table5339
+ GCC_except_table5434
+ GCC_except_table5481
+ GCC_except_table5505
+ GCC_except_table5546
+ GCC_except_table5547
+ GCC_except_table5622
+ GCC_except_table5640
+ GCC_except_table5918
+ GCC_except_table5925
+ GCC_except_table5933
+ GCC_except_table5944
+ GCC_except_table5946
+ GCC_except_table5947
+ GCC_except_table5948
+ GCC_except_table5949
+ GCC_except_table5954
+ GCC_except_table5959
+ GCC_except_table5964
+ GCC_except_table5975
+ GCC_except_table5991
+ GCC_except_table5993
+ GCC_except_table5999
+ GCC_except_table6008
+ GCC_except_table6017
+ GCC_except_table6050
+ GCC_except_table6086
+ GCC_except_table6093
+ GCC_except_table6094
+ GCC_except_table6154
+ GCC_except_table6157
+ GCC_except_table6198
+ GCC_except_table6203
+ GCC_except_table6209
+ GCC_except_table6212
+ GCC_except_table6215
+ GCC_except_table6218
+ GCC_except_table6221
+ GCC_except_table6224
+ GCC_except_table6227
+ GCC_except_table6230
+ GCC_except_table6233
+ GCC_except_table6236
+ GCC_except_table6239
+ GCC_except_table6340
+ GCC_except_table6353
+ GCC_except_table6552
+ GCC_except_table6559
+ GCC_except_table6731
+ GCC_except_table6735
+ GCC_except_table6737
+ GCC_except_table6760
+ GCC_except_table6806
+ GCC_except_table6988
+ GCC_except_table699
+ GCC_except_table7121
+ GCC_except_table713
+ GCC_except_table7262
+ GCC_except_table7275
+ GCC_except_table7298
+ GCC_except_table7311
+ GCC_except_table7355
+ GCC_except_table7356
+ GCC_except_table7357
+ GCC_except_table7358
+ GCC_except_table7400
+ GCC_except_table7418
+ GCC_except_table7470
+ GCC_except_table7473
+ GCC_except_table7484
+ GCC_except_table7534
+ GCC_except_table7553
+ GCC_except_table7586
+ GCC_except_table765
+ GCC_except_table7652
+ GCC_except_table8068
+ GCC_except_table8074
+ GCC_except_table8096
+ GCC_except_table8100
+ GCC_except_table8118
+ GCC_except_table8153
+ GCC_except_table8156
+ GCC_except_table8223
+ GCC_except_table8268
+ GCC_except_table8317
+ GCC_except_table8345
+ GCC_except_table8350
+ GCC_except_table8352
+ GCC_except_table8354
+ GCC_except_table8386
+ GCC_except_table8529
+ GCC_except_table8537
+ GCC_except_table8542
+ GCC_except_table8557
+ GCC_except_table8565
+ GCC_except_table8609
+ GCC_except_table8744
+ GCC_except_table8750
+ GCC_except_table8787
+ GCC_except_table879
+ GCC_except_table8790
+ GCC_except_table8797
+ GCC_except_table8800
+ GCC_except_table890
+ GCC_except_table9009
+ GCC_except_table9015
+ GCC_except_table9055
+ GCC_except_table9153
+ GCC_except_table9158
+ GCC_except_table984
+ GCC_except_table994
+ MSVFastHexStringFromBytes.hexCharacters.42062
+ MusicLibraryLibraryCore.frameworkLibrary.22250
+ MusicLibraryLibraryCore.frameworkLibrary.31789
+ OBJC_IVAR_$_ICBackgroundTaskScheduler._lock
+ OBJC_IVAR_$_ICBackgroundTaskScheduler._queue
+ OBJC_IVAR_$_ICBackgroundTaskScheduler._registered
+ OBJC_IVAR_$_ICBackgroundTaskScheduler._taskHandlers
+ OBJC_IVAR_$_ICBackgroundTaskScheduler._taskInfoDictionaries
+ OBJC_IVAR_$_ICContentKeySession._lock
+ OBJC_IVAR_$_ICRequestContext._requestNotificationsEnabled
+ OBJC_IVAR_$_ICRequestContext._tag
+ OBJC_IVAR_$_ICURLRequest._requestID
+ OBJC_IVAR_$_ICURLRequest._requestName
+ _ICArtworkInfoKeyArtworkDictionaryFullURL3x4
+ _ICHomeManagerPropertiesDidChangeNotification
+ _ICURLRequestDidStartNotification
+ _ICURLRequestTaskDidCompleteNotification
+ _ICURLRequestTaskDidReceiveResponseNotification
+ _ICURLRequestTaskDidResumeNotification
+ _MSV_XXH_XXH32_update.11790
+ _MSV_XXH_XXH32_update.17658
+ _MSV_XXH_XXH32_update.17798
+ _MSV_XXH_XXH32_update.20655
+ _MSV_XXH_XXH32_update.31725
+ _MSV_XXH_XXH32_update.42051
+ _MSV_XXH_XXH32_update.512
+ _MSV_XXH_XXH64_digest.17803
+ _MSV_XXH_XXH64_digest.31730
+ _MSV_XXH_XXH64_update.11791
+ _MSV_XXH_XXH64_update.17659
+ _MSV_XXH_XXH64_update.17799
+ _MSV_XXH_XXH64_update.20656
+ _MSV_XXH_XXH64_update.31726
+ _MSV_XXH_XXH64_update.42052
+ _MSV_XXH_XXH64_update.513
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_ICBackgroundTaskScheduler
+ _OBJC_METACLASS_$_ICBackgroundTaskScheduler
+ __108-[ICInAppMessageManager _updateShouldDownloadResources:onMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.489
+ __109-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponseNeedsReloadForRequestContext:completion:]_block_invoke.54
+ __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.664
+ __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.665
+ __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke_2.669
+ __116-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponseNeedsReloadForAllRequestContextsWithCompletion:]_block_invoke.51
+ __30-[ICURLBagProvider _loadCache]_block_invoke.139
+ __31-[ICURLSession _finishRequest:]_block_invoke.69
+ __31-[ICURLSession _finishRequest:]_block_invoke_2.70
+ __32-[ICURLSession _processRequest:]_block_invoke.65
+ __34-[ICURLBagProvider _loadMonoCache]_block_invoke.146
+ __35-[ICURLBagProvider invalidateCache]_block_invoke.66
+ __39-[ICURLSession _processPendingRequests]_block_invoke.62
+ __42-[ICCloudClient setPreferredVideoQuality:]_block_invoke.180
+ __42-[ICCloudClient uploadCloudItemProperties]_block_invoke.195
+ __45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.190
+ __46-[ICBackgroundTaskScheduler _scheduleNextTask]_block_invoke.39
+ __46-[ICBackgroundTaskScheduler _scheduleNextTask]_block_invoke.42
+ __46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.200
+ __46-[ICSecureKeyDeliveryRequestOperation execute]_block_invoke.28
+ __47-[ICBackgroundTaskScheduler _postExpiredEvents]_block_invoke.47
+ __48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.424
+ __48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.425
+ __52-[ICInAppMessageManager _performSyncRetryIfPending:]_block_invoke.481
+ __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.438
+ __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.442
+ __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.443
+ __52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.68
+ __52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.69
+ __52-[ICMusicSubscriptionStatusCache updateBaseCacheKey]_block_invoke.64
+ __53-[ICInAppMessageManager _addMessageEntry:completion:]_block_invoke.457
+ __53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.128
+ __56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.185
+ __57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.164
+ __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.449
+ __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.450
+ __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.454
+ __60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.212
+ __60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.153
+ __60-[ICInAppMessageManager listener:shouldAcceptNewConnection:]_block_invoke.541
+ __60-[ICLibraryAuthServiceClientTokenProvider _clientConnection]_block_invoke.183
+ __61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.141
+ __61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.157
+ __61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.173
+ __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.222
+ __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.223
+ __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.226
+ __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.227
+ __64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.175
+ __64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.145
+ __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.166
+ __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.167
+ __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.168
+ __65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.170
+ __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.649
+ __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.650
+ __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.660
+ __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke_2.654
+ __68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.171
+ __68-[ICMusicSubscriptionStatusCache _loadPersistedCacheWithCompletion:]_block_invoke.83
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.121
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.122
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.125
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.90
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.94
+ __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.126
+ __70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.143
+ __72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.126
+ __72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.134
+ __73-[ICMusicSubscriptionStatusCache _persistCachePostingGlobalNotification:]_block_invoke.88
+ __73-[ICURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.44
+ __75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.139
+ __75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.204
+ __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.241
+ __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.244
+ __77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.127
+ __78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.248
+ __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.624
+ __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.627
+ __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.631
+ __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.639
+ __79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.124
+ __80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.123
+ __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.478
+ __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.479
+ __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.480
+ __81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.206
+ __82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.149
+ __82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.117
+ __83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.147
+ __84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke.495
+ __84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke_2.496
+ __85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.125
+ __86-[ICCloudClient importContainerArtworkForSagaID:artworkVariantType:completionHandler:]_block_invoke.122
+ __87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.208
+ __88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.151
+ __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke.38
+ __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke.40
+ __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke_2.39
+ __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.54
+ __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.56
+ __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.59
+ __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.475
+ __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.476
+ __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.477
+ __91-[ICLibraryAuthServiceClientTokenProvider getTokenResultsForDSIDs:forceRefresh:completion:]_block_invoke.67
+ __91-[ICLibraryAuthServiceClientTokenProvider getTokenResultsForDSIDs:forceRefresh:completion:]_block_invoke.70
+ __92-[ICLibraryAuthServiceClientTokenProvider getTokenStatusForDSIDs:forcingRefresh:completion:]_block_invoke.87
+ __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.49
+ __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.52
+ __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.57
+ __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.58
+ __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.36
+ __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.37
+ __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.38
+ __94-[ICLibraryAuthServiceClientTokenProvider _refreshTokenForDSID:forExternalRequest:completion:]_block_invoke.97
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.503
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.507
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.508
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.513
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.517
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.518
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.519
+ __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.523
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.108
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.109
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.115
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.116
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.117
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke_2.112
+ __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke_2.114
+ __97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.217
+ __98-[ICLibraryAuthServiceClientTokenProvider getAllTokenStatusForAssistantForcingRefresh:completion:]_block_invoke.88
+ __98-[ICLibraryAuthServiceClientTokenProvider getAllTokenStatusForAssistantForcingRefresh:completion:]_block_invoke.89
+ __98-[ICMusicSubscriptionStatusCache getCachedSubscriptionStatusResponseForRequestContext:completion:]_block_invoke.37
+ __99-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponse:forRequestContext:completion:]_block_invoke.47
+ __Block_byref_object_copy_.10567
+ __Block_byref_object_copy_.10769
+ __Block_byref_object_copy_.10900
+ __Block_byref_object_copy_.1120
+ __Block_byref_object_copy_.12389
+ __Block_byref_object_copy_.13740
+ __Block_byref_object_copy_.14287
+ __Block_byref_object_copy_.14462
+ __Block_byref_object_copy_.14730
+ __Block_byref_object_copy_.15150
+ __Block_byref_object_copy_.16311
+ __Block_byref_object_copy_.16821
+ __Block_byref_object_copy_.17052
+ __Block_byref_object_copy_.17401
+ __Block_byref_object_copy_.18880
+ __Block_byref_object_copy_.19253
+ __Block_byref_object_copy_.19460
+ __Block_byref_object_copy_.20479
+ __Block_byref_object_copy_.21409
+ __Block_byref_object_copy_.22210
+ __Block_byref_object_copy_.22825
+ __Block_byref_object_copy_.22935
+ __Block_byref_object_copy_.25374
+ __Block_byref_object_copy_.2568
+ __Block_byref_object_copy_.25820
+ __Block_byref_object_copy_.26431
+ __Block_byref_object_copy_.26797
+ __Block_byref_object_copy_.26843
+ __Block_byref_object_copy_.27769
+ __Block_byref_object_copy_.28742
+ __Block_byref_object_copy_.29773
+ __Block_byref_object_copy_.30126
+ __Block_byref_object_copy_.31164
+ __Block_byref_object_copy_.32081
+ __Block_byref_object_copy_.32467
+ __Block_byref_object_copy_.32654
+ __Block_byref_object_copy_.32823
+ __Block_byref_object_copy_.330
+ __Block_byref_object_copy_.33569
+ __Block_byref_object_copy_.3514
+ __Block_byref_object_copy_.35707
+ __Block_byref_object_copy_.3587
+ __Block_byref_object_copy_.35945
+ __Block_byref_object_copy_.36081
+ __Block_byref_object_copy_.37020
+ __Block_byref_object_copy_.37195
+ __Block_byref_object_copy_.37901
+ __Block_byref_object_copy_.38171
+ __Block_byref_object_copy_.38764
+ __Block_byref_object_copy_.38945
+ __Block_byref_object_copy_.39249
+ __Block_byref_object_copy_.3939
+ __Block_byref_object_copy_.40100
+ __Block_byref_object_copy_.40698
+ __Block_byref_object_copy_.4294
+ __Block_byref_object_copy_.4422
+ __Block_byref_object_copy_.4456
+ __Block_byref_object_copy_.5349
+ __Block_byref_object_copy_.5507
+ __Block_byref_object_copy_.5590
+ __Block_byref_object_copy_.6331
+ __Block_byref_object_copy_.6778
+ __Block_byref_object_copy_.6894
+ __Block_byref_object_copy_.7348
+ __Block_byref_object_copy_.9584
+ __Block_byref_object_copy_.9694
+ __Block_byref_object_dispose_.10568
+ __Block_byref_object_dispose_.10770
+ __Block_byref_object_dispose_.10901
+ __Block_byref_object_dispose_.1121
+ __Block_byref_object_dispose_.12390
+ __Block_byref_object_dispose_.13741
+ __Block_byref_object_dispose_.14288
+ __Block_byref_object_dispose_.14463
+ __Block_byref_object_dispose_.14731
+ __Block_byref_object_dispose_.15151
+ __Block_byref_object_dispose_.16312
+ __Block_byref_object_dispose_.16822
+ __Block_byref_object_dispose_.17053
+ __Block_byref_object_dispose_.17402
+ __Block_byref_object_dispose_.18881
+ __Block_byref_object_dispose_.19254
+ __Block_byref_object_dispose_.19461
+ __Block_byref_object_dispose_.20480
+ __Block_byref_object_dispose_.21410
+ __Block_byref_object_dispose_.22211
+ __Block_byref_object_dispose_.22826
+ __Block_byref_object_dispose_.22936
+ __Block_byref_object_dispose_.25375
+ __Block_byref_object_dispose_.2569
+ __Block_byref_object_dispose_.25821
+ __Block_byref_object_dispose_.26432
+ __Block_byref_object_dispose_.26798
+ __Block_byref_object_dispose_.26844
+ __Block_byref_object_dispose_.27770
+ __Block_byref_object_dispose_.28743
+ __Block_byref_object_dispose_.29774
+ __Block_byref_object_dispose_.30127
+ __Block_byref_object_dispose_.31165
+ __Block_byref_object_dispose_.32082
+ __Block_byref_object_dispose_.32468
+ __Block_byref_object_dispose_.32655
+ __Block_byref_object_dispose_.32824
+ __Block_byref_object_dispose_.331
+ __Block_byref_object_dispose_.33570
+ __Block_byref_object_dispose_.3515
+ __Block_byref_object_dispose_.35708
+ __Block_byref_object_dispose_.3588
+ __Block_byref_object_dispose_.35946
+ __Block_byref_object_dispose_.36082
+ __Block_byref_object_dispose_.37021
+ __Block_byref_object_dispose_.37196
+ __Block_byref_object_dispose_.37902
+ __Block_byref_object_dispose_.38172
+ __Block_byref_object_dispose_.38765
+ __Block_byref_object_dispose_.38946
+ __Block_byref_object_dispose_.39250
+ __Block_byref_object_dispose_.3940
+ __Block_byref_object_dispose_.40101
+ __Block_byref_object_dispose_.40699
+ __Block_byref_object_dispose_.4295
+ __Block_byref_object_dispose_.4423
+ __Block_byref_object_dispose_.4457
+ __Block_byref_object_dispose_.5350
+ __Block_byref_object_dispose_.5508
+ __Block_byref_object_dispose_.5591
+ __Block_byref_object_dispose_.6332
+ __Block_byref_object_dispose_.6779
+ __Block_byref_object_dispose_.6895
+ __Block_byref_object_dispose_.7349
+ __Block_byref_object_dispose_.9585
+ __Block_byref_object_dispose_.9695
+ __ICCloudClientMigrateAllowMatchOnCellularToAllowAutoDownloadOnCellular_block_invoke.560
+ __MusicLibraryLibraryCore_block_invoke.22251
+ __MusicLibraryLibraryCore_block_invoke.31790
+ __OBJC_$_CLASS_METHODS_ICBackgroundTaskScheduler
+ __OBJC_$_CLASS_PROP_LIST_ICBackgroundTaskScheduler
+ __OBJC_$_INSTANCE_METHODS_ICBackgroundTaskScheduler
+ __OBJC_$_INSTANCE_VARIABLES_ICBackgroundTaskScheduler
+ __OBJC_CLASS_RO_$_ICBackgroundTaskScheduler
+ __OBJC_METACLASS_RO_$_ICBackgroundTaskScheduler
+ ___34-[ICURLRequest _task:didResumeAt:]_block_invoke
+ ___35-[ICURLRequest _sanitizedURLString]_block_invoke
+ ___46-[ICBackgroundTaskScheduler _scheduleNextTask]_block_invoke
+ ___46-[ICURLRequest _task:didCompleteWithError:at:]_block_invoke
+ ___47-[ICBackgroundTaskScheduler _postExpiredEvents]_block_invoke
+ ___48+[ICBackgroundTaskScheduler sharedTaskScheduler]_block_invoke
+ ___51-[ICHomeManager _postPropertiesChangedNotification]_block_invoke
+ ___51-[ICURLRequest _task:didReceiveInitialResponse:at:]_block_invoke
+ ___69-[ICMusicSubscriptionStatusMonitor _beginObservingSubscriptionStatus]_block_invoke_2
+ ___86-[ICCloudClient importContainerArtworkForSagaID:artworkVariantType:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32s_e22_v16?0"BGSystemTask"8l
+ ___block_descriptor_40_e8_32s_e35_v24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_48_e8_32s40bs_e55_v24?0"ICMusicSubscriptionStatusCacheKey"8"NSError"16l
+ ___block_descriptor_56_e8_32s40r48r_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_64_e8_32s40s48s56bs_e55_v24?0"ICMusicSubscriptionStatusCacheKey"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e27_v24?0"NSData"8"NSData"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e5_v8?0l
+ __block_literal_global.10100
+ __block_literal_global.11525
+ __block_literal_global.11964
+ __block_literal_global.12.15195
+ __block_literal_global.12.25163
+ __block_literal_global.12.26447
+ __block_literal_global.12528
+ __block_literal_global.13.39260
+ __block_literal_global.13159
+ __block_literal_global.13201
+ __block_literal_global.13775
+ __block_literal_global.14.26445
+ __block_literal_global.1465
+ __block_literal_global.14917
+ __block_literal_global.15211
+ __block_literal_global.167
+ __block_literal_global.16742
+ __block_literal_global.17454
+ __block_literal_global.17927
+ __block_literal_global.18.26443
+ __block_literal_global.18.35779
+ __block_literal_global.182
+ __block_literal_global.18307
+ __block_literal_global.184
+ __block_literal_global.187
+ __block_literal_global.18701
+ __block_literal_global.189
+ __block_literal_global.18934
+ __block_literal_global.19158
+ __block_literal_global.192
+ __block_literal_global.194
+ __block_literal_global.197
+ __block_literal_global.199
+ __block_literal_global.20.26441
+ __block_literal_global.202
+ __block_literal_global.20336
+ __block_literal_global.210
+ __block_literal_global.22.26436
+ __block_literal_global.22047
+ __block_literal_global.22274
+ __block_literal_global.223
+ __block_literal_global.225
+ __block_literal_global.227.41276
+ __block_literal_global.22729
+ __block_literal_global.22840
+ __block_literal_global.229
+ __block_literal_global.2309
+ __block_literal_global.231
+ __block_literal_global.2397
+ __block_literal_global.243.25362
+ __block_literal_global.24306
+ __block_literal_global.24432
+ __block_literal_global.25162
+ __block_literal_global.25358
+ __block_literal_global.25926
+ __block_literal_global.26097
+ __block_literal_global.26307
+ __block_literal_global.26453
+ __block_literal_global.2694
+ __block_literal_global.27809
+ __block_literal_global.28326
+ __block_literal_global.29142
+ __block_literal_global.29491
+ __block_literal_global.29790
+ __block_literal_global.29940
+ __block_literal_global.3.17934
+ __block_literal_global.30938
+ __block_literal_global.31444
+ __block_literal_global.31546
+ __block_literal_global.3188
+ __block_literal_global.31965
+ __block_literal_global.32547
+ __block_literal_global.329
+ __block_literal_global.33178
+ __block_literal_global.33608
+ __block_literal_global.34826
+ __block_literal_global.35344
+ __block_literal_global.35801
+ __block_literal_global.36961
+ __block_literal_global.3746
+ __block_literal_global.37915
+ __block_literal_global.38295
+ __block_literal_global.38392
+ __block_literal_global.39086
+ __block_literal_global.39270
+ __block_literal_global.3959
+ __block_literal_global.40214
+ __block_literal_global.40350
+ __block_literal_global.40504
+ __block_literal_global.40703
+ __block_literal_global.41275
+ __block_literal_global.41527
+ __block_literal_global.41882
+ __block_literal_global.4229
+ __block_literal_global.4474
+ __block_literal_global.453
+ __block_literal_global.4538
+ __block_literal_global.4656
+ __block_literal_global.55
+ __block_literal_global.5747
+ __block_literal_global.58.31593
+ __block_literal_global.6.26451
+ __block_literal_global.6222
+ __block_literal_global.69
+ __block_literal_global.6969
+ __block_literal_global.7066
+ __block_literal_global.73.22706
+ __block_literal_global.7367
+ __block_literal_global.7566
+ __block_literal_global.78
+ __block_literal_global.798
+ __block_literal_global.8.2389
+ __block_literal_global.8.26449
+ __block_literal_global.8288
+ __block_literal_global.8359
+ __block_literal_global.9288
+ __block_literal_global.96.29442
+ __getML3MusicLibraryClass_block_invoke.22249
+ _objc_msgSend$ICURLRequest:task:didCompleteWithError:at:
+ _objc_msgSend$ICURLRequest:task:didReceiveInitialResponse:at:
+ _objc_msgSend$ICURLRequest:task:didResumeAt:
+ _objc_msgSend$_checkTokenPresetsForDSIDs:forceRefresh:
+ _objc_msgSend$_devicePresetErrorForConfiguration:WithSpecifiedDSIDs:
+ _objc_msgSend$_devicePresetForConfiguration:withDSIDs:
+ _objc_msgSend$_devicePresetNonDiscriminatoryFailForConfiguration:
+ _objc_msgSend$_devicePresetNonDiscriminatorySucceedForConfiguration:DSIDsToUse:
+ _objc_msgSend$_handleHomeManagerPropertiesDidChange:
+ _objc_msgSend$_loadSavedTaskInfo
+ _objc_msgSend$_postExpiredEvents
+ _objc_msgSend$_postPropertiesChangedNotification
+ _objc_msgSend$_requestNotificationsEnabled
+ _objc_msgSend$_requestWasEnqueuedAt:
+ _objc_msgSend$_sanitizedURLString
+ _objc_msgSend$_saveTaskInfo
+ _objc_msgSend$_scheduleNextTask
+ _objc_msgSend$_task:didCompleteWithError:at:
+ _objc_msgSend$_task:didReceiveInitialResponse:at:
+ _objc_msgSend$_task:didResumeAt:
+ _objc_msgSend$cancelTask:
+ _objc_msgSend$cancelTaskRequestWithIdentifier:error:
+ _objc_msgSend$contentKeySpecifier
+ _objc_msgSend$defaultMediaAccountDSIDWithError:
+ _objc_msgSend$defaultMediaIdentity
+ _objc_msgSend$hasScheduledTask:
+ _objc_msgSend$importContainerArtworkForSagaID:artworkVariantType:configuration:completion:
+ _objc_msgSend$observers
+ _objc_msgSend$registerForTask:handler:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$requestName
+ _objc_msgSend$scheduleRecurringTask:withInterval:afterDelay:withUserData:
+ _objc_msgSend$scheduleTask:afterDelay:withUserData:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequestName:
+ _objc_msgSend$setScheduleAfter:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$sharedTaskScheduler
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$taskRequestForIdentifier:
+ _y1rKtVxYz7
+ audit_stringMusicLibrary.22266
+ audit_stringMusicLibrary.31793
+ getML3MusicLibraryClass.22247
+ getML3MusicLibraryClass.softClass.22248
+ sharedCache.sOnceToken.29939
+ sharedCache.sSharedCache.29941
+ sharedController.sOnceToken.35800
+ sharedController.sOnceToken.39269
+ sharedController.sSharedController.35802
+ sharedController.sSharedController.39271
+ sharedManager.sOnceToken.19157
+ sharedManager.sOnceToken.28325
+ sharedManager.sSharedManager.19159
+ sharedManager.sSharedManager.28327
+ sharedMonitor.sOnceToken.18306
+ sharedMonitor.sOnceToken.40213
+ sharedMonitor.sSharedMonitor.18308
+ sharedMonitor.sSharedMonitor.40215
+ sharedProvider.sOnceToken.40503
+ sharedProvider.sSharedProvider.40505
+ sharedTaskScheduler._scheduler
+ sharedTaskScheduler.onceToken
- +[ICURLSession _sanitizeURL:]
- -[ICLibraryAuthServiceClientTokenProvider _checkTokenPresetsForDSID:forceRefresh:]
- -[ICLibraryAuthServiceClientTokenProvider _devicePresetForConfiguration:withDSID:]
- -[ICURLRequest enableLoadURLMetricsWithRequestName:]
- -[ICURLRequest loadURLMetricsRequestName]
- -[ICURLRequest shouldReportLoadURLMetrics]
- -[ICURLSession _reportLoadURLMetricsWithSession:task:signatureName:request:error:]
- GCC_except_table1081
- GCC_except_table1108
- GCC_except_table1243
- GCC_except_table1319
- GCC_except_table1484
- GCC_except_table149
- GCC_except_table1497
- GCC_except_table1685
- GCC_except_table1867
- GCC_except_table1898
- GCC_except_table1913
- GCC_except_table1955
- GCC_except_table2068
- GCC_except_table2086
- GCC_except_table2135
- GCC_except_table2137
- GCC_except_table2143
- GCC_except_table2150
- GCC_except_table2178
- GCC_except_table2192
- GCC_except_table2197
- GCC_except_table2199
- GCC_except_table2204
- GCC_except_table2220
- GCC_except_table2316
- GCC_except_table2358
- GCC_except_table2389
- GCC_except_table2391
- GCC_except_table2393
- GCC_except_table2395
- GCC_except_table2744
- GCC_except_table2796
- GCC_except_table2960
- GCC_except_table2977
- GCC_except_table2987
- GCC_except_table2990
- GCC_except_table3012
- GCC_except_table38
- GCC_except_table4066
- GCC_except_table4074
- GCC_except_table4078
- GCC_except_table4080
- GCC_except_table4082
- GCC_except_table4093
- GCC_except_table4097
- GCC_except_table4112
- GCC_except_table4116
- GCC_except_table426
- GCC_except_table4294
- GCC_except_table433
- GCC_except_table4347
- GCC_except_table4351
- GCC_except_table4354
- GCC_except_table4359
- GCC_except_table4423
- GCC_except_table4465
- GCC_except_table4469
- GCC_except_table4471
- GCC_except_table4591
- GCC_except_table4749
- GCC_except_table4815
- GCC_except_table4896
- GCC_except_table5060
- GCC_except_table5302
- GCC_except_table5397
- GCC_except_table5444
- GCC_except_table5468
- GCC_except_table5509
- GCC_except_table5510
- GCC_except_table5585
- GCC_except_table5603
- GCC_except_table5881
- GCC_except_table5888
- GCC_except_table5896
- GCC_except_table5907
- GCC_except_table5909
- GCC_except_table5914
- GCC_except_table5919
- GCC_except_table5924
- GCC_except_table5935
- GCC_except_table5952
- GCC_except_table5960
- GCC_except_table5969
- GCC_except_table5978
- GCC_except_table6011
- GCC_except_table6047
- GCC_except_table6054
- GCC_except_table6055
- GCC_except_table6115
- GCC_except_table6118
- GCC_except_table6159
- GCC_except_table6164
- GCC_except_table6170
- GCC_except_table6173
- GCC_except_table6176
- GCC_except_table6179
- GCC_except_table6182
- GCC_except_table6185
- GCC_except_table6188
- GCC_except_table6191
- GCC_except_table6194
- GCC_except_table6197
- GCC_except_table6200
- GCC_except_table6301
- GCC_except_table6314
- GCC_except_table6511
- GCC_except_table6518
- GCC_except_table6690
- GCC_except_table6694
- GCC_except_table6696
- GCC_except_table6719
- GCC_except_table6765
- GCC_except_table6947
- GCC_except_table700
- GCC_except_table7080
- GCC_except_table714
- GCC_except_table7221
- GCC_except_table7234
- GCC_except_table7257
- GCC_except_table7270
- GCC_except_table7314
- GCC_except_table7315
- GCC_except_table7316
- GCC_except_table7317
- GCC_except_table7318
- GCC_except_table7377
- GCC_except_table7429
- GCC_except_table7432
- GCC_except_table7443
- GCC_except_table7452
- GCC_except_table7512
- GCC_except_table7545
- GCC_except_table7611
- GCC_except_table766
- GCC_except_table8027
- GCC_except_table8033
- GCC_except_table8056
- GCC_except_table8060
- GCC_except_table8073
- GCC_except_table8078
- GCC_except_table8116
- GCC_except_table8183
- GCC_except_table8228
- GCC_except_table8277
- GCC_except_table8303
- GCC_except_table8308
- GCC_except_table8310
- GCC_except_table8312
- GCC_except_table8344
- GCC_except_table8487
- GCC_except_table8495
- GCC_except_table8500
- GCC_except_table8515
- GCC_except_table8523
- GCC_except_table8567
- GCC_except_table8702
- GCC_except_table8706
- GCC_except_table8708
- GCC_except_table8745
- GCC_except_table8755
- GCC_except_table8758
- GCC_except_table880
- GCC_except_table891
- GCC_except_table8967
- GCC_except_table8973
- GCC_except_table9013
- GCC_except_table9111
- GCC_except_table9116
- GCC_except_table983
- GCC_except_table993
- MSVFastHexStringFromBytes.hexCharacters.41943
- MusicLibraryLibraryCore.frameworkLibrary.22147
- MusicLibraryLibraryCore.frameworkLibrary.31677
- OBJC_IVAR_$_ICURLRequest._loadURLMetricsRequestName
- _AnalyticsSendEventLazy
- _MSV_XXH_XXH32_update.11807
- _MSV_XXH_XXH32_update.17609
- _MSV_XXH_XXH32_update.20578
- _MSV_XXH_XXH32_update.31613
- _MSV_XXH_XXH32_update.41932
- _MSV_XXH_XXH32_update.519
- _MSV_XXH_XXH64_digest.17753
- _MSV_XXH_XXH64_digest.31618
- _MSV_XXH_XXH64_update.11808
- _MSV_XXH_XXH64_update.17610
- _MSV_XXH_XXH64_update.20579
- _MSV_XXH_XXH64_update.31614
- _MSV_XXH_XXH64_update.41933
- _MSV_XXH_XXH64_update.520
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_7_DAYS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- __108-[ICInAppMessageManager _updateShouldDownloadResources:onMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.486
- __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.669
- __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.670
- __110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke_2.674
- __116-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponseNeedsReloadForAllRequestContextsWithCompletion:]_block_invoke.52
- __30-[ICURLBagProvider _loadCache]_block_invoke.141
- __31-[ICURLSession _finishRequest:]_block_invoke.71
- __31-[ICURLSession _finishRequest:]_block_invoke_2.72
- __32-[ICURLSession _processRequest:]_block_invoke.67
- __34-[ICURLBagProvider _loadMonoCache]_block_invoke.148
- __35-[ICURLBagProvider invalidateCache]_block_invoke.68
- __39-[ICURLSession _processPendingRequests]_block_invoke.64
- __42-[ICCloudClient setPreferredVideoQuality:]_block_invoke.179
- __42-[ICCloudClient uploadCloudItemProperties]_block_invoke.194
- __45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.189
- __46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.199
- __46-[ICSecureKeyDeliveryRequestOperation execute]_block_invoke.25
- __48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.421
- __48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.422
- __52-[ICInAppMessageManager _performSyncRetryIfPending:]_block_invoke.478
- __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.434
- __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.435
- __52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.436
- __52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.66
- __52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.67
- __52-[ICMusicSubscriptionStatusCache updateBaseCacheKey]_block_invoke.62
- __53-[ICInAppMessageManager _addMessageEntry:completion:]_block_invoke.454
- __53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.130
- __53-[ICURLSession URLSession:task:didCompleteWithError:]_block_invoke.30
- __56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.184
- __57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.162
- __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.446
- __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.447
- __57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.448
- __60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.210
- __60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.151
- __60-[ICInAppMessageManager listener:shouldAcceptNewConnection:]_block_invoke.538
- __60-[ICLibraryAuthServiceClientTokenProvider _clientConnection]_block_invoke.180
- __61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.139
- __61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.156
- __61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.171
- __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.220
- __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.221
- __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.224
- __62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.225
- __64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.173
- __64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.143
- __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.163
- __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.164
- __64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.165
- __65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.169
- __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.654
- __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.655
- __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.665
- __66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke_2.659
- __68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.170
- __68-[ICMusicSubscriptionStatusCache _loadPersistedCacheWithCompletion:]_block_invoke.84
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.123
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.124
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.127
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.92
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.96
- __69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.128
- __70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.141
- __72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.125
- __72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.132
- __73-[ICMusicSubscriptionStatusCache _persistCachePostingGlobalNotification:]_block_invoke.89
- __73-[ICURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.46
- __75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.137
- __75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.202
- __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.239
- __75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.242
- __77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.126
- __78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.246
- __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.629
- __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.632
- __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.636
- __78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.644
- __79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.123
- __80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.122
- __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.475
- __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.476
- __80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.477
- __81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.204
- __82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.147
- __82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.114
- __83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.145
- __84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke.492
- __84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke_2.493
- __85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.124
- __87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.206
- __88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.149
- __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke.39
- __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke.41
- __88-[ICURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke_2.40
- __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.48
- __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.50
- __89-[ICLibraryAuthServiceClientTokenProvider getTokenResultForDSID:forceRefresh:completion:]_block_invoke.55
- __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.472
- __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.473
- __90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.474
- __91-[ICLibraryAuthServiceClientTokenProvider getTokenResultsForDSIDs:forceRefresh:completion:]_block_invoke.63
- __91-[ICLibraryAuthServiceClientTokenProvider getTokenResultsForDSIDs:forceRefresh:completion:]_block_invoke.66
- __92-[ICLibraryAuthServiceClientTokenProvider getTokenStatusForDSIDs:forcingRefresh:completion:]_block_invoke.83
- __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.53
- __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.54
- __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.60
- __92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.63
- __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.33
- __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.34
- __93-[ICLibraryAuthServiceClientTokenProvider getAllTokensForAssistantForcingRefresh:completion:]_block_invoke.35
- __94-[ICLibraryAuthServiceClientTokenProvider _refreshTokenForDSID:forExternalRequest:completion:]_block_invoke.94
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.500
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.504
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.505
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.509
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.510
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.511
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.516
- __96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.520
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.102
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.106
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.110
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.112
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke.114
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke_2.109
- __96-[ICLibraryAuthServiceClientTokenProvider _refreshTokensForDSIDs:forExternalRequest:completion:]_block_invoke_2.111
- __97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.216
- __98-[ICLibraryAuthServiceClientTokenProvider getAllTokenStatusForAssistantForcingRefresh:completion:]_block_invoke.85
- __98-[ICLibraryAuthServiceClientTokenProvider getAllTokenStatusForAssistantForcingRefresh:completion:]_block_invoke.86
- __99-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponse:forRequestContext:completion:]_block_invoke.48
- __Block_byref_object_copy_.10586
- __Block_byref_object_copy_.10790
- __Block_byref_object_copy_.10921
- __Block_byref_object_copy_.1122
- __Block_byref_object_copy_.12430
- __Block_byref_object_copy_.13797
- __Block_byref_object_copy_.14350
- __Block_byref_object_copy_.14524
- __Block_byref_object_copy_.14792
- __Block_byref_object_copy_.15209
- __Block_byref_object_copy_.16368
- __Block_byref_object_copy_.16884
- __Block_byref_object_copy_.17115
- __Block_byref_object_copy_.18821
- __Block_byref_object_copy_.19195
- __Block_byref_object_copy_.19403
- __Block_byref_object_copy_.20401
- __Block_byref_object_copy_.21305
- __Block_byref_object_copy_.22107
- __Block_byref_object_copy_.22718
- __Block_byref_object_copy_.22828
- __Block_byref_object_copy_.25258
- __Block_byref_object_copy_.2561
- __Block_byref_object_copy_.25703
- __Block_byref_object_copy_.26313
- __Block_byref_object_copy_.26679
- __Block_byref_object_copy_.26725
- __Block_byref_object_copy_.27652
- __Block_byref_object_copy_.28623
- __Block_byref_object_copy_.29655
- __Block_byref_object_copy_.30008
- __Block_byref_object_copy_.31046
- __Block_byref_object_copy_.31969
- __Block_byref_object_copy_.32355
- __Block_byref_object_copy_.32542
- __Block_byref_object_copy_.32711
- __Block_byref_object_copy_.329
- __Block_byref_object_copy_.33454
- __Block_byref_object_copy_.3513
- __Block_byref_object_copy_.35597
- __Block_byref_object_copy_.35835
- __Block_byref_object_copy_.3586
- __Block_byref_object_copy_.35971
- __Block_byref_object_copy_.36908
- __Block_byref_object_copy_.37083
- __Block_byref_object_copy_.37789
- __Block_byref_object_copy_.38061
- __Block_byref_object_copy_.38652
- __Block_byref_object_copy_.38833
- __Block_byref_object_copy_.39137
- __Block_byref_object_copy_.3941
- __Block_byref_object_copy_.39986
- __Block_byref_object_copy_.40588
- __Block_byref_object_copy_.4277
- __Block_byref_object_copy_.4402
- __Block_byref_object_copy_.4436
- __Block_byref_object_copy_.5327
- __Block_byref_object_copy_.5485
- __Block_byref_object_copy_.5570
- __Block_byref_object_copy_.6308
- __Block_byref_object_copy_.6756
- __Block_byref_object_copy_.6873
- __Block_byref_object_copy_.7327
- __Block_byref_object_copy_.9564
- __Block_byref_object_copy_.9673
- __Block_byref_object_dispose_.10587
- __Block_byref_object_dispose_.10791
- __Block_byref_object_dispose_.10922
- __Block_byref_object_dispose_.1123
- __Block_byref_object_dispose_.12431
- __Block_byref_object_dispose_.13798
- __Block_byref_object_dispose_.14351
- __Block_byref_object_dispose_.14525
- __Block_byref_object_dispose_.14793
- __Block_byref_object_dispose_.15210
- __Block_byref_object_dispose_.16369
- __Block_byref_object_dispose_.16885
- __Block_byref_object_dispose_.17116
- __Block_byref_object_dispose_.18822
- __Block_byref_object_dispose_.19196
- __Block_byref_object_dispose_.19404
- __Block_byref_object_dispose_.20402
- __Block_byref_object_dispose_.21306
- __Block_byref_object_dispose_.22108
- __Block_byref_object_dispose_.22719
- __Block_byref_object_dispose_.22829
- __Block_byref_object_dispose_.25259
- __Block_byref_object_dispose_.2562
- __Block_byref_object_dispose_.25704
- __Block_byref_object_dispose_.26314
- __Block_byref_object_dispose_.26680
- __Block_byref_object_dispose_.26726
- __Block_byref_object_dispose_.27653
- __Block_byref_object_dispose_.28624
- __Block_byref_object_dispose_.29656
- __Block_byref_object_dispose_.30009
- __Block_byref_object_dispose_.31047
- __Block_byref_object_dispose_.31970
- __Block_byref_object_dispose_.32356
- __Block_byref_object_dispose_.32543
- __Block_byref_object_dispose_.32712
- __Block_byref_object_dispose_.330
- __Block_byref_object_dispose_.33455
- __Block_byref_object_dispose_.3514
- __Block_byref_object_dispose_.35598
- __Block_byref_object_dispose_.35836
- __Block_byref_object_dispose_.3587
- __Block_byref_object_dispose_.35972
- __Block_byref_object_dispose_.36909
- __Block_byref_object_dispose_.37084
- __Block_byref_object_dispose_.37790
- __Block_byref_object_dispose_.38062
- __Block_byref_object_dispose_.38653
- __Block_byref_object_dispose_.38834
- __Block_byref_object_dispose_.39138
- __Block_byref_object_dispose_.3942
- __Block_byref_object_dispose_.39987
- __Block_byref_object_dispose_.40589
- __Block_byref_object_dispose_.4278
- __Block_byref_object_dispose_.4403
- __Block_byref_object_dispose_.4437
- __Block_byref_object_dispose_.5328
- __Block_byref_object_dispose_.5486
- __Block_byref_object_dispose_.5571
- __Block_byref_object_dispose_.6309
- __Block_byref_object_dispose_.6757
- __Block_byref_object_dispose_.6874
- __Block_byref_object_dispose_.7328
- __Block_byref_object_dispose_.9565
- __Block_byref_object_dispose_.9674
- __ICCloudClientMigrateAllowMatchOnCellularToAllowAutoDownloadOnCellular_block_invoke.557
- __MusicLibraryLibraryCore_block_invoke.22148
- __MusicLibraryLibraryCore_block_invoke.31678
- ___109-[ICMusicSubscriptionStatusCache setCachedSubscriptionStatusResponseNeedsReloadForRequestContext:completion:]_block_invoke_3
- ___29+[ICURLSession _sanitizeURL:]_block_invoke
- ___75-[ICMusicSubscriptionStatusCache _getCacheKeyForRequestContext:completion:]_block_invoke_3
- ___82-[ICURLSession _reportLoadURLMetricsWithSession:task:signatureName:request:error:]_block_invoke
- ___98-[ICMusicSubscriptionStatusCache getCachedSubscriptionStatusResponseForRequestContext:completion:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_48_e8_32s40bs_e43_v16?0"ICMusicSubscriptionStatusCacheKey"8l
- ___block_descriptor_64_e8_32s40s48s56bs_e43_v16?0"ICMusicSubscriptionStatusCacheKey"8l
- ___block_descriptor_72_e8_32s40s48s56s64s_e19_"NSDictionary"8?0l
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e27_v24?0"NSData"8"NSData"16l
- ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64b72r
- ___copy_helper_block_e8_32s40s48s56s64s72r
- ___destroy_helper_block_e8_32s40s48s56s64s72r
- __block_literal_global.10077
- __block_literal_global.10675
- __block_literal_global.11542
- __block_literal_global.11976
- __block_literal_global.12.15254
- __block_literal_global.12.25054
- __block_literal_global.12.26329
- __block_literal_global.12566
- __block_literal_global.13.39148
- __block_literal_global.13210
- __block_literal_global.13252
- __block_literal_global.13832
- __block_literal_global.14.26327
- __block_literal_global.1463
- __block_literal_global.15270
- __block_literal_global.16805
- __block_literal_global.169.9965
- __block_literal_global.17877
- __block_literal_global.18.26325
- __block_literal_global.18.35669
- __block_literal_global.181
- __block_literal_global.18257
- __block_literal_global.183
- __block_literal_global.186
- __block_literal_global.18651
- __block_literal_global.188
- __block_literal_global.18875
- __block_literal_global.19099
- __block_literal_global.191
- __block_literal_global.193
- __block_literal_global.196.28927
- __block_literal_global.198
- __block_literal_global.20.26323
- __block_literal_global.201
- __block_literal_global.20260
- __block_literal_global.209
- __block_literal_global.21944
- __block_literal_global.22.26318
- __block_literal_global.22171
- __block_literal_global.222
- __block_literal_global.224
- __block_literal_global.226
- __block_literal_global.22622
- __block_literal_global.22733
- __block_literal_global.228
- __block_literal_global.230
- __block_literal_global.2305
- __block_literal_global.2391
- __block_literal_global.241
- __block_literal_global.24197
- __block_literal_global.24323
- __block_literal_global.25053
- __block_literal_global.25243
- __block_literal_global.25809
- __block_literal_global.25980
- __block_literal_global.26189
- __block_literal_global.26335
- __block_literal_global.2691
- __block_literal_global.27692
- __block_literal_global.28207
- __block_literal_global.29025
- __block_literal_global.29373
- __block_literal_global.29672
- __block_literal_global.29822
- __block_literal_global.3.17884
- __block_literal_global.30820
- __block_literal_global.31336
- __block_literal_global.31437
- __block_literal_global.31853
- __block_literal_global.3186
- __block_literal_global.32435
- __block_literal_global.328
- __block_literal_global.33062
- __block_literal_global.33493
- __block_literal_global.34716
- __block_literal_global.35234
- __block_literal_global.35691
- __block_literal_global.36849
- __block_literal_global.3749
- __block_literal_global.37803
- __block_literal_global.38182
- __block_literal_global.38280
- __block_literal_global.38974
- __block_literal_global.39158
- __block_literal_global.3961
- __block_literal_global.40100
- __block_literal_global.40239
- __block_literal_global.40394
- __block_literal_global.40593
- __block_literal_global.41162
- __block_literal_global.41407
- __block_literal_global.41763
- __block_literal_global.4213
- __block_literal_global.4454
- __block_literal_global.450
- __block_literal_global.4519
- __block_literal_global.4638
- __block_literal_global.56
- __block_literal_global.57
- __block_literal_global.5721
- __block_literal_global.6.26333
- __block_literal_global.6195
- __block_literal_global.6948
- __block_literal_global.7045
- __block_literal_global.71
- __block_literal_global.71.5676
- __block_literal_global.7346
- __block_literal_global.7542
- __block_literal_global.76.29000
- __block_literal_global.8.2383
- __block_literal_global.8.26331
- __block_literal_global.801
- __block_literal_global.8265
- __block_literal_global.8336
- __block_literal_global.9269
- __block_literal_global.96.29324
- __getML3MusicLibraryClass_block_invoke.22146
- _fmod
- _malloc_type_malloc
- _objc_msgSend$_checkTokenPresetsForDSID:forceRefresh:
- _objc_msgSend$_devicePresetForConfiguration:withDSID:
- _objc_msgSend$_reportLoadURLMetricsWithSession:task:signatureName:request:error:
- _objc_msgSend$_sanitizeURL:
- _objc_msgSend$appleTimingApp
- _objc_msgSend$connectionType
- _objc_msgSend$enableLoadURLMetricsWithRequestName:
- _objc_msgSend$loadURLMetricsRequestName
- _objc_msgSend$requestBytesSent
- _objc_msgSend$responseBytesReceived
- _objc_msgSend$responseTime
- _objc_msgSend$secureConnectionStartTime
- _objc_msgSend$shouldReportLoadURLMetrics
- _xpc_activity_copy_criteria
- _xpc_activity_register
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
- audit_stringMusicLibrary.22163
- audit_stringMusicLibrary.31681
- getML3MusicLibraryClass.22144
- getML3MusicLibraryClass.softClass.22145
- sharedCache.sOnceToken.29821
- sharedCache.sSharedCache.29823
- sharedController.sOnceToken.35690
- sharedController.sOnceToken.39157
- sharedController.sSharedController.35692
- sharedController.sSharedController.39159
- sharedManager.sOnceToken.19098
- sharedManager.sOnceToken.28206
- sharedManager.sSharedManager.19100
- sharedManager.sSharedManager.28208
- sharedMonitor.sOnceToken.18256
- sharedMonitor.sOnceToken.40099
- sharedMonitor.sSharedMonitor.18258
- sharedMonitor.sSharedMonitor.40101
- sharedProvider.sOnceToken.40393
- sharedProvider.sSharedProvider.40395
CStrings:
+ "%{public}@ Cant get cached status because we failed to fetch cache key. err=%{public}@ error=%{public}@"
+ "%{public}@ Cant update cache because we failed to fetch cache key. err=%{public}@ error=%{public}@"
+ "%{public}@ Failed to cancel existing task. err=%{public}@"
+ "%{public}@ Failed to load account properties to form the cache key with. err=%{public}@"
+ "%{public}@ Failed to register with task scheduler"
+ "%{public}@ Failed to set refresh flag because we failed to fetch cache key. err=%{public}@ error=%{public}@"
+ "%{public}@ Failed to submit new task. err=%{public}@"
+ "%{public}@ Not performing bulk refresh because we couldn't find an active account or its not in good standing"
+ "%{public}@ Posting expired event '%{public}@"
+ "%{public}@ Posting expired events"
+ "%{public}@ Properties changed - posting notification"
+ "%{public}@ Registering handler for task '%{public}@'"
+ "%{public}@ Setting timer to perform periodic poll for %llds"
+ "%{public}@ Skipping posting event with no handler: '%{public}@'"
+ "%{public}@ Skipping scheduling task with no handler: '%{public}@'"
+ "%{public}@ Time for next event '%{public}@' has already passed - posting now"
+ "%{public}@ canceling task '%{public}@'"
+ "%{public}@ loaded persisted task info %{public}@"
+ "%{public}@ no more events to schedule"
+ "%{public}@ persisting event data %{public}@"
+ "%{public}@ scheduling next event '%{public}@' for %{public}@ (%llds from now)"
+ "%{public}@ scheduling recurring task '%{public}@' with interval %f and delay %f"
+ "%{public}@ scheduling task '%{public}@' with delay %f"
+ "Autoupdating Default Media Account: <%@>"
+ "Bag profile:%@ version:%@"
+ "Default Media Account: <%@>"
+ "ICBackgroundTaskScheduler"
+ "ICBackgroundTaskScheduler.m"
+ "ICDefaultsKeySagaPushNotificationTimes"
+ "ICURLRequest:task:didCompleteWithError:at:"
+ "ICURLRequest:task:didReceiveInitialResponse:at:"
+ "ICURLRequest:task:didResumeAt:"
+ "ICURLRequestDidStartNotification"
+ "ICURLRequestTaskDidCompleteNotification"
+ "ICURLRequestTaskDidReceiveResponseNotification"
+ "ICURLRequestTaskDidResumeNotification"
+ "MediaRedownload endpoint:%@"
+ "RadioGetTracks"
+ "SKD key:%@ persistent:%d"
+ "SKDCertificate"
+ "SKDNonce"
+ "Sending request to import container artwork for saga ID %llu and variant %ld..."
+ "SharedListeningSession id:create"
+ "SharedListeningSession id:join"
+ "StorePlatform personalized:0"
+ "StorePlatform personalized:1"
+ "SubPlaybackDispatch type:%ld lease-only:%d"
+ "SuzeLease endpoint:%@"
+ "T@\"ICBackgroundTaskScheduler\",R,N"
+ "T@\"NSString\",&,N,V_requestName"
+ "T@\"NSString\",R,C,N,V_requestID"
+ "T@,R,N,V_tag"
+ "_checkTokenPresetsForDSIDs:forceRefresh:"
+ "_devicePresetErrorForConfiguration:WithSpecifiedDSIDs:"
+ "_devicePresetForConfiguration:withDSIDs:"
+ "_devicePresetNonDiscriminatoryFailForConfiguration:"
+ "_devicePresetNonDiscriminatorySucceedForConfiguration:DSIDsToUse:"
+ "_handleHomeManagerPropertiesDidChange:"
+ "_loadSavedTaskInfo"
+ "_postExpiredEvents"
+ "_postPropertiesChangedNotification"
+ "_registered"
+ "_requestID"
+ "_requestName"
+ "_requestNotificationsEnabled"
+ "_requestWasEnqueuedAt:"
+ "_sanitizedURLString"
+ "_saveTaskInfo"
+ "_scheduleNextTask"
+ "_tag"
+ "_task:didCompleteWithError:at:"
+ "_task:didReceiveInitialResponse:at:"
+ "_task:didResumeAt:"
+ "_taskHandlers"
+ "_taskInfoDictionaries"
+ "autoupdatingDefaultMediaIdentity"
+ "cancelTask:"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.iTunesCloud.ICHomeManager.ICHomeManagerPropertiesDidChangeNotification"
+ "com.apple.itunescloud.ICBackgroundTaskScheduler.task_identifier"
+ "com.apple.itunescloud.ICInAppMessageManager.periodic_poll"
+ "com.apple.itunescloud.ICLibraryAuthServiceClientTokenProvider.refresh_timer"
+ "com.apple.mediaservices.ICBackgroundTaskScheduler.queue"
+ "contentKeySpecifier"
+ "defaultMediaAccountDSIDWithError:"
+ "enableRequestNotifications"
+ "full-url-3x4"
+ "hasScheduledTask:"
+ "importContainerArtworkForSagaID:artworkVariantType:completionHandler:"
+ "importContainerArtworkForSagaID:artworkVariantType:configuration:completion:"
+ "interval > 0"
+ "is_recurring"
+ "networkTaskID"
+ "observers"
+ "registerForTask:handler:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "requestID"
+ "requestName"
+ "requestURL"
+ "responseHeaders"
+ "sagaPushNotificationTimes"
+ "scheduleRecurringTask:withInterval:afterDelay:withUserData:"
+ "scheduleTask:afterDelay:withUserData:"
+ "scheduled_tasks"
+ "setRequestName:"
+ "setSagaPushNotificationTimes:"
+ "setScheduleAfter:"
+ "setTag:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "sharedTaskScheduler"
+ "submitTaskRequest:error:"
+ "tag"
+ "taskRequestForIdentifier:"
+ "userData"
+ "v16@?0@\"BGSystemTask\"8"
+ "v24@?0@\"ICMusicSubscriptionStatusCacheKey\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v40@0:8@16d24@32"
+ "v40@0:8Q16q24@?32"
+ "v48@0:8@16d24d32@40"
+ "v48@0:8Q16q24@\"ICConnectionConfiguration\"32@?<v@?@\"NSError\">40"
+ "v48@0:8Q16q24@32@?40"
+ "{DevicePresetTokenResult=@@B}24@0:8@16"
- "%{public}@ Fetching token result for DSID %{public}@. forceRefresh=%{BOOL}u"
- "%{public}@ Logging CoreAnalytics %{public}@ event: %@"
- "%{public}@ Not performing bulk refresh because privacy acknowledgement is required for the primary account"
- "%{public}@ Setting timer to perform periodic poll for %llds (+/- %llds)"
- "1.5"
- "@\"NSDictionary\"8@?0"
- "Bluetooth"
- "Cellular"
- "Ethernet"
- "Failed to turn AutoPlay %@, Feature not enabled"
- "Favoriting"
- "Other"
- "PotluckRadioAutoPlay"
- "UseAMSBagForMusic"
- "_checkTokenPresetsForDSID:forceRefresh:"
- "_devicePresetForConfiguration:withDSID:"
- "_loadURLMetricsRequestName"
- "_reportLoadURLMetricsWithSession:task:signatureName:request:error:"
- "_sanitizeURL:"
- "appVersion"
- "com.apple.amp.itunescloud.LoadURL"
- "com.apple.itunescloud.ICInAppMessageManager.periodic-poll-activity"
- "com.apple.itunescloud.library_auth_token_refresh_timer"
- "domainLookupTime"
- "enableLoadURLMetricsWithRequestName:"
- "loadURLMetricsRequestName"
- "mediaRedownload/%@"
- "radio/getTracks"
- "radioType"
- "requestSignature"
- "responseMessageSizeUncompressed"
- "sharedListening/create"
- "sharedListening/join"
- "shouldReportLoadURLMetrics"
- "skd/certificate"
- "skd/key?shared=%d&persistent=%d"
- "skd/nonce"
- "storePlatform/%@"
- "subPlaybackDispatch/%@"
- "suzeLease/%@"
- "token_refresh_dsid"
- "urlBag/%@/%@"
- "v16@?0@\"ICMusicSubscriptionStatusCacheKey\"8"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"

```
