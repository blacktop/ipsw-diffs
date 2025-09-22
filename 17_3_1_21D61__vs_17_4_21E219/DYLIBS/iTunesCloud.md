## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4023.400.6.0.0
-  __TEXT.__text: 0x2876a8
-  __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x14a50
-  __TEXT.__const: 0x1654c
-  __TEXT.__gcc_except_tab: 0x25e0
-  __TEXT.__cstring: 0x16159
-  __TEXT.__oslogstring: 0x1ca71
+4023.510.1.0.0
+  __TEXT.__text: 0x2b1cb0
+  __TEXT.__auth_stubs: 0x1510
+  __TEXT.__objc_methlist: 0x14cd0
+  __TEXT.__const: 0x18ec4
+  __TEXT.__gcc_except_tab: 0x2658
+  __TEXT.__cstring: 0x16609
+  __TEXT.__oslogstring: 0x1d48b
   __TEXT.__ustring: 0x8e
-  __TEXT.__dlopen_cstrs: 0x3de
-  __TEXT.__unwind_info: 0x6224
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x39ac
-  __TEXT.__objc_methname: 0x319d0
-  __TEXT.__objc_methtype: 0x736a
-  __TEXT.__objc_stubs: 0x19f20
+  __TEXT.__dlopen_cstrs: 0x48a
+  __TEXT.__unwind_info: 0x6b20
+  __TEXT.__eh_frame: 0x2468
+  __TEXT.__objc_classname: 0x39f8
+  __TEXT.__objc_methname: 0x32384
+  __TEXT.__objc_methtype: 0x751e
+  __TEXT.__objc_stubs: 0x1a300
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x7e40
-  __DATA_CONST.__objc_classlist: 0xd20
+  __DATA_CONST.__const: 0x75f0
+  __DATA_CONST.__objc_classlist: 0xd30
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x298
+  __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x27438
-  __DATA_CONST.__objc_selrefs: 0x9348
+  __DATA_CONST.__objc_const: 0x27948
+  __DATA_CONST.__objc_selrefs: 0x94a8
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0xf40
+  __DATA_CONST.__objc_superrefs: 0xb60
   __DATA_CONST.__objc_arraydata: 0x5a8
-  __AUTH_CONST.__const: 0x10580
-  __AUTH_CONST.__cfstring: 0x17580
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH_CONST.__objc_const: 0xa380
+  __AUTH_CONST.__const: 0x12178
+  __AUTH_CONST.__cfstring: 0x17880
+  __AUTH_CONST.__objc_intobj: 0x450
+  __AUTH_CONST.__objc_const: 0xa4a0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x2a8
-  __AUTH_CONST.__auth_got: 0xa90
-  __AUTH.__objc_data: 0x4c40
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0xf28
-  __DATA.__objc_superrefs: 0xb50
-  __DATA.__objc_ivar: 0x2210
-  __DATA.__data: 0x24d0
-  __DATA.__common: 0xa8c
-  __DATA.__bss: 0x278
+  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH.__objc_data: 0x4ce0
+  __DATA.__objc_ivar: 0x2250
+  __DATA.__data: 0x24e8
+  __DATA.__bss: 0x2a0
+  __DATA.__common: 0xa98
   __DATA_DIRTY.__objc_data: 0x3700
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x400
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6A0DA99E-3366-3948-A603-165424721151
-  Functions: 9590
-  Symbols:   29981
-  CStrings:  16841
+  UUID: 10BA6625-A514-36FC-AE28-84EC31E984D2
+  Functions: 9711
+  Symbols:   30268
+  CStrings:  17011
 
Symbols:
+ +[ICMusicSubscriptionStatus dateFromMilliseconds:]
+ +[ICPlaybackPositionClient sharedService]
+ +[ICPlaybackPositionEntity keyValueStoreItemIdentifierForUniqueStoreID:itemTitle:albumName:itemArtistName:feedURL:feedGUID:]
+ +[ICPlaybackPositionEntity supportsSecureCoding]
+ +[ICPlaybackPositionEntity ubiquitousIdentifierWithItemTitle:albumName:itemArtistName:]
+ +[ICPlaybackPositionEntity ubiquitousIdentifierWithPodcastFeedURL:feedGUID:]
+ +[ICPlaybackPositionEntity ubiquitousIdentifierWithUniqueStoreID:]
+ +[ICPlaybackPositionEntity ubiquitousIdentifierWithiTunesUFeedURL:feedGUID:]
+ -[ICMusicSubscriptionStatus initialPurchaseTimestamp]
+ -[ICMusicSubscriptionStatus serviceBeginsTimestamp]
+ -[ICMutableMusicSubscriptionStatus setInitialPurchaseTimestamp:]
+ -[ICMutableMusicSubscriptionStatus setServiceBeginsTimestamp:]
+ -[ICMutablePlayActivityEvent setSharedActivityType:]
+ -[ICPlayActivityEvent sharedActivityType]
+ -[ICPlaybackPositionClient .cxx_destruct]
+ -[ICPlaybackPositionClient connection]
+ -[ICPlaybackPositionClient deletePlaybackPositionEntitiesFromLibraryWithIdentifier:]
+ -[ICPlaybackPositionClient deletePlaybackPositionEntities]
+ -[ICPlaybackPositionClient deletePlaybackPositionEntity:]
+ -[ICPlaybackPositionClient getLocalPlaybackPositionForEntityIdentifiers:completionBlock:]
+ -[ICPlaybackPositionClient getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:]
+ -[ICPlaybackPositionClient init]
+ -[ICPlaybackPositionClient persistPlaybackPositionEntity:isCheckpoint:completionBlock:]
+ -[ICPlaybackPositionClient pullPlaybackPositionEntity:completionBlock:]
+ -[ICPlaybackPositionClient pushPlaybackPositionEntity:completionBlock:]
+ -[ICPlaybackPositionClient synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:]
+ -[ICPlaybackPositionClient synchronizePlaybackPositions]
+ -[ICPlaybackPositionClient updateForeignDatabaseWithValuesFromPlaybackPositionEntity:]
+ -[ICPlaybackPositionEntity .cxx_destruct]
+ -[ICPlaybackPositionEntity bookmarkTime]
+ -[ICPlaybackPositionEntity bookmarkTimestamp]
+ -[ICPlaybackPositionEntity copyWithZone:]
+ -[ICPlaybackPositionEntity description]
+ -[ICPlaybackPositionEntity encodeWithCoder:]
+ -[ICPlaybackPositionEntity hasBeenPlayed]
+ -[ICPlaybackPositionEntity hash]
+ -[ICPlaybackPositionEntity initWithCoder:]
+ -[ICPlaybackPositionEntity initWithDomain:]
+ -[ICPlaybackPositionEntity initWithDomain:playbackPositionKey:persistentIdentifier:]
+ -[ICPlaybackPositionEntity isEqual:]
+ -[ICPlaybackPositionEntity itemPersistentIdentifier]
+ -[ICPlaybackPositionEntity libraryIdentifier]
+ -[ICPlaybackPositionEntity playbackPositionDomain]
+ -[ICPlaybackPositionEntity playbackPositionKey]
+ -[ICPlaybackPositionEntity setBookmarkTime:]
+ -[ICPlaybackPositionEntity setBookmarkTimestamp:]
+ -[ICPlaybackPositionEntity setHasBeenPlayed:]
+ -[ICPlaybackPositionEntity setItemPersistentIdentifier:]
+ -[ICPlaybackPositionEntity setLibraryIdentifier:]
+ -[ICPlaybackPositionEntity setPlaybackPositionKey:]
+ -[ICPlaybackPositionEntity setUserPlayCount:]
+ -[ICPlaybackPositionEntity userPlayCount]
+ -[ICURLRequest aggregatedPerformanceMetrics]
+ -[ICURLRequest setAggregatedPerformanceMetrics:]
+ -[ICURLResponse aggregatedPerformanceMetrics]
+ GCC_except_table2109
+ GCC_except_table2111
+ GCC_except_table2116
+ GCC_except_table2119
+ GCC_except_table2132
+ GCC_except_table5211
+ GCC_except_table5307
+ GCC_except_table5355
+ GCC_except_table5379
+ GCC_except_table5422
+ GCC_except_table5423
+ GCC_except_table5496
+ GCC_except_table5512
+ GCC_except_table5789
+ GCC_except_table5796
+ GCC_except_table5804
+ GCC_except_table5815
+ GCC_except_table5817
+ GCC_except_table5822
+ GCC_except_table5829
+ GCC_except_table5839
+ GCC_except_table5854
+ GCC_except_table5862
+ GCC_except_table5871
+ GCC_except_table5880
+ GCC_except_table5913
+ GCC_except_table5927
+ GCC_except_table5936
+ GCC_except_table5943
+ GCC_except_table5944
+ GCC_except_table6006
+ GCC_except_table6046
+ GCC_except_table6052
+ GCC_except_table6055
+ GCC_except_table6058
+ GCC_except_table6061
+ GCC_except_table6064
+ GCC_except_table6067
+ GCC_except_table6070
+ GCC_except_table6073
+ GCC_except_table6076
+ GCC_except_table6079
+ GCC_except_table6082
+ GCC_except_table6182
+ GCC_except_table6195
+ GCC_except_table6388
+ GCC_except_table6395
+ GCC_except_table6569
+ GCC_except_table6573
+ GCC_except_table6575
+ GCC_except_table6598
+ GCC_except_table6644
+ GCC_except_table6831
+ GCC_except_table6964
+ GCC_except_table7107
+ GCC_except_table7120
+ GCC_except_table7141
+ GCC_except_table7152
+ GCC_except_table7197
+ GCC_except_table7198
+ GCC_except_table7199
+ GCC_except_table7200
+ GCC_except_table7201
+ GCC_except_table7242
+ GCC_except_table7260
+ GCC_except_table7312
+ GCC_except_table7315
+ GCC_except_table7324
+ GCC_except_table7331
+ GCC_except_table7372
+ GCC_except_table7391
+ GCC_except_table7424
+ GCC_except_table7482
+ GCC_except_table7483
+ GCC_except_table7496
+ GCC_except_table7913
+ GCC_except_table7919
+ GCC_except_table7941
+ GCC_except_table7945
+ GCC_except_table7956
+ GCC_except_table7961
+ GCC_except_table7996
+ GCC_except_table7999
+ GCC_except_table8061
+ GCC_except_table8106
+ GCC_except_table8154
+ GCC_except_table8179
+ GCC_except_table8184
+ GCC_except_table8186
+ GCC_except_table8188
+ GCC_except_table8220
+ GCC_except_table8363
+ GCC_except_table8371
+ GCC_except_table8376
+ GCC_except_table8391
+ GCC_except_table8399
+ GCC_except_table8443
+ GCC_except_table8577
+ GCC_except_table8581
+ GCC_except_table8583
+ GCC_except_table8620
+ GCC_except_table8623
+ GCC_except_table8630
+ GCC_except_table8633
+ GCC_except_table8844
+ GCC_except_table8848
+ GCC_except_table8888
+ _CC_MD5_Init
+ _Ejwmn62s
+ _Hz73b
+ _ICPlaybackPositionEntityIdentifierForProperties
+ _ICPlaybackPositionServiceDomainDefault
+ _ICPlaybackPositionServiceDomainExtras
+ _ICURLBagKeyKVSRequestURLGet
+ _ICURLBagKeyKVSRequestURLGetAll
+ _ICURLBagKeyKVSRequestURLPut
+ _ICURLBagKeyKVSRequestURLPutAll
+ _ICURLBagKeyKVSRequestURLSync
+ _MSVFastHexStringFromBytes.hexCharacters.41185
+ _MusicLibraryLibrary
+ _MusicLibraryLibraryCore.frameworkLibrary.21906
+ _MusicLibraryLibraryCore.frameworkLibrary.31310
+ _NROcmM
+ _OBJC_CLASS_$_ICPlaybackPositionClient
+ _OBJC_CLASS_$_ICPlaybackPositionEntity
+ _OBJC_IVAR_$_ICMediaUserStateCenter._cloudClient
+ _OBJC_IVAR_$_ICMusicSubscriptionStatus._initialPurchaseTimestamp
+ _OBJC_IVAR_$_ICMusicSubscriptionStatus._serviceBeginsTimestamp
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._sharedActivityType
+ _OBJC_IVAR_$_ICPlayActivityEvent._sharedActivityType
+ _OBJC_IVAR_$_ICPlaybackPositionClient._connection
+ _OBJC_IVAR_$_ICPlaybackPositionClient._listenerEndpointProvider
+ _OBJC_IVAR_$_ICPlaybackPositionClient._serialQueue
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._bookmarkTime
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._bookmarkTimestamp
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._hasBeenPlayed
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._itemPersistentIdentifier
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._libraryIdentifier
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._playbackPositionDomain
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._playbackPositionKey
+ _OBJC_IVAR_$_ICPlaybackPositionEntity._userPlayCount
+ _OBJC_IVAR_$_ICURLRequest._aggregatedPerformanceMetrics
+ _OBJC_IVAR_$_ICURLResponse._aggregatedPerformanceMetrics
+ _OBJC_METACLASS_$_ICPlaybackPositionClient
+ _OBJC_METACLASS_$_ICPlaybackPositionEntity
+ _VLxCLgDpiF
+ _VONlh32NYbFTEnv
+ __MSV_XXH_XXH32_update.11645
+ __MSV_XXH_XXH32_update.17358
+ __MSV_XXH_XXH32_update.20327
+ __MSV_XXH_XXH32_update.31246
+ __MSV_XXH_XXH32_update.41174
+ __MSV_XXH_XXH64_digest.17501
+ __MSV_XXH_XXH64_digest.31251
+ __MSV_XXH_XXH64_update.11646
+ __MSV_XXH_XXH64_update.17359
+ __MSV_XXH_XXH64_update.20328
+ __MSV_XXH_XXH64_update.31247
+ __MSV_XXH_XXH64_update.41175
+ __OBJC_$_CLASS_METHODS_ICPlaybackPositionClient
+ __OBJC_$_CLASS_METHODS_ICPlaybackPositionEntity
+ __OBJC_$_CLASS_PROP_LIST_ICPlaybackPositionEntity
+ __OBJC_$_INSTANCE_METHODS_ICPlaybackPositionClient
+ __OBJC_$_INSTANCE_METHODS_ICPlaybackPositionEntity
+ __OBJC_$_INSTANCE_VARIABLES_ICPlaybackPositionClient
+ __OBJC_$_INSTANCE_VARIABLES_ICPlaybackPositionEntity
+ __OBJC_$_PROP_LIST_ICPlaybackPositionClient
+ __OBJC_$_PROP_LIST_ICPlaybackPositionEntity
+ __OBJC_$_PROP_LIST_ICStorePlatformResponse.134
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICPlaybackPositionService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICPlaybackPositionService
+ __OBJC_$_PROTOCOL_REFS_ICPlaybackPositionService
+ __OBJC_CLASS_PROTOCOLS_$_ICPlaybackPositionClient
+ __OBJC_CLASS_PROTOCOLS_$_ICPlaybackPositionEntity
+ __OBJC_CLASS_RO_$_ICPlaybackPositionClient
+ __OBJC_CLASS_RO_$_ICPlaybackPositionEntity
+ __OBJC_LABEL_PROTOCOL_$_ICPlaybackPositionService
+ __OBJC_METACLASS_RO_$_ICPlaybackPositionClient
+ __OBJC_METACLASS_RO_$_ICPlaybackPositionEntity
+ __OBJC_PROTOCOL_$_ICPlaybackPositionService
+ __OBJC_PROTOCOL_REFERENCE_$_ICPlaybackPositionService
+ ___104-[ICPlaybackPositionClient synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:]_block_invoke
+ ___108-[ICInAppMessageManager _updateShouldDownloadResources:onMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.412
+ ___110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.622
+ ___110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke_2.626
+ ___125-[ICPlaybackPositionClient getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:]_block_invoke
+ ___125-[ICPlaybackPositionClient getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:]_block_invoke.6
+ ___30-[ICURLBagProvider _loadCache]_block_invoke.132
+ ___31-[ICURLSession _finishRequest:]_block_invoke.64
+ ___31-[ICURLSession _finishRequest:]_block_invoke_2.65
+ ___32-[ICURLSession _processRequest:]_block_invoke.62
+ ___34-[ICURLBagProvider _loadMonoCache]_block_invoke.137
+ ___38-[ICMediaUserStateCenter _initLazily:]_block_invoke_2
+ ___38-[ICMediaUserStateCenter _initLazily:]_block_invoke_3
+ ___38-[ICPlaybackPositionClient connection]_block_invoke
+ ___38-[ICPlaybackPositionClient connection]_block_invoke.79
+ ___38-[ICPlaybackPositionClient connection]_block_invoke.80
+ ___39-[ICURLSession _processPendingRequests]_block_invoke.61
+ ___41+[ICPlaybackPositionClient sharedService]_block_invoke
+ ___41-[ICMediaUserStateCenter _onAsyncServer:]_block_invoke_2
+ ___45-[ICInAppMessageManager _xpcClientConnection]_block_invoke.362
+ ___48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.366
+ ___52-[ICInAppMessageManager _performSyncRetryIfPending:]_block_invoke.408
+ ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.375
+ ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.378
+ ___52-[ICMediaUserStateCenter _establishClientConnection]_block_invoke.92
+ ___53-[ICInAppMessageManager _addMessageEntry:completion:]_block_invoke.384
+ ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.124
+ ___55-[ICMediaUserStateCenter _getUserStatesForcingRefresh:]_block_invoke.96
+ ___57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.380
+ ___57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.383
+ ___57-[ICPlaybackPositionClient deletePlaybackPositionEntity:]_block_invoke
+ ___58-[ICMediaUserStateCenter refreshUserStatesWithCompletion:]_block_invoke.30
+ ___60-[ICInAppMessageManager listener:shouldAcceptNewConnection:]_block_invoke.451
+ ___60-[ICLibraryAuthServiceClientTokenProvider _clientConnection]_block_invoke.142
+ ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.182
+ ___63-[ICPlayActivityCenter _daemonPlayActivityControllerConnection]_block_invoke.67
+ ___65-[ICMediaUserStateCenter _applyServerStateUpdatedWithUserStates:]_block_invoke.104
+ ___66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.612
+ ___66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke_2.616
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.120
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.121
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.122
+ ___70-[ICDeveloperTokenDefaultProvider _fetchDeveloperTokenWithClientInfo:]_block_invoke.6
+ ___71-[ICCloudClientAvailabilityService _xpcConnectionWithListenerEndpoint:]_block_invoke.81
+ ___71-[ICPlaybackPositionClient pullPlaybackPositionEntity:completionBlock:]_block_invoke
+ ___71-[ICPlaybackPositionClient pullPlaybackPositionEntity:completionBlock:]_block_invoke.8
+ ___71-[ICPlaybackPositionClient pushPlaybackPositionEntity:completionBlock:]_block_invoke
+ ___71-[ICPlaybackPositionClient pushPlaybackPositionEntity:completionBlock:]_block_invoke.10
+ ___73-[ICCloudContentTasteRequestListener _setupContentTasteServiceConnection]_block_invoke.83
+ ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.192
+ ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.195
+ ___78-[ICExternalSharedListeningConnectionController _initializeConnectionIfNeeded]_block_invoke.198
+ ___78-[ICExternalSharedListeningConnectionController _initializeConnectionIfNeeded]_block_invoke.202
+ ___78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.199
+ ___78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.593
+ ___78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.597
+ ___79-[ICCloudServiceStatusMonitor requestAuthorizationForScopes:completionHandler:]_block_invoke.157
+ ___79-[ICCloudServiceStatusMonitor requestAuthorizationForScopes:completionHandler:]_block_invoke_2.161
+ ___80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.407
+ ___81-[ICCloudServiceStatusMonitor _validateAuthorizationExpiryWithCompletionHandler:]_block_invoke.175
+ ___81-[ICCloudServiceStatusMonitor _validateAuthorizationExpiryWithCompletionHandler:]_block_invoke.177
+ ___84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke.416
+ ___84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke_2.417
+ ___84-[ICPlaybackPositionClient deletePlaybackPositionEntitiesFromLibraryWithIdentifier:]_block_invoke
+ ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke.123
+ ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke.125
+ ___86-[ICPlaybackPositionClient updateForeignDatabaseWithValuesFromPlaybackPositionEntity:]_block_invoke
+ ___87-[ICPlaybackPositionClient persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke
+ ___87-[ICPlaybackPositionClient persistPlaybackPositionEntity:isCheckpoint:completionBlock:]_block_invoke.4
+ ___90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.404
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.422
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.427
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.433
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.435
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke_2.434
+ ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke_2.437
+ ___Block_byref_object_copy_.10335
+ ___Block_byref_object_copy_.10633
+ ___Block_byref_object_copy_.10761
+ ___Block_byref_object_copy_.1102
+ ___Block_byref_object_copy_.12285
+ ___Block_byref_object_copy_.13628
+ ___Block_byref_object_copy_.14172
+ ___Block_byref_object_copy_.14344
+ ___Block_byref_object_copy_.14609
+ ___Block_byref_object_copy_.15020
+ ___Block_byref_object_copy_.16155
+ ___Block_byref_object_copy_.16634
+ ___Block_byref_object_copy_.16861
+ ___Block_byref_object_copy_.18592
+ ___Block_byref_object_copy_.18958
+ ___Block_byref_object_copy_.19171
+ ___Block_byref_object_copy_.20155
+ ___Block_byref_object_copy_.21062
+ ___Block_byref_object_copy_.21868
+ ___Block_byref_object_copy_.22485
+ ___Block_byref_object_copy_.2256
+ ___Block_byref_object_copy_.22585
+ ___Block_byref_object_copy_.25002
+ ___Block_byref_object_copy_.2514
+ ___Block_byref_object_copy_.25433
+ ___Block_byref_object_copy_.25994
+ ___Block_byref_object_copy_.26347
+ ___Block_byref_object_copy_.26389
+ ___Block_byref_object_copy_.27309
+ ___Block_byref_object_copy_.28272
+ ___Block_byref_object_copy_.29299
+ ___Block_byref_object_copy_.29641
+ ___Block_byref_object_copy_.30676
+ ___Block_byref_object_copy_.31595
+ ___Block_byref_object_copy_.31980
+ ___Block_byref_object_copy_.3203
+ ___Block_byref_object_copy_.32158
+ ___Block_byref_object_copy_.32318
+ ___Block_byref_object_copy_.3270
+ ___Block_byref_object_copy_.33074
+ ___Block_byref_object_copy_.35127
+ ___Block_byref_object_copy_.35352
+ ___Block_byref_object_copy_.35486
+ ___Block_byref_object_copy_.3607
+ ___Block_byref_object_copy_.36349
+ ___Block_byref_object_copy_.36512
+ ___Block_byref_object_copy_.37200
+ ___Block_byref_object_copy_.37471
+ ___Block_byref_object_copy_.38058
+ ___Block_byref_object_copy_.38237
+ ___Block_byref_object_copy_.38543
+ ___Block_byref_object_copy_.39395
+ ___Block_byref_object_copy_.3965
+ ___Block_byref_object_copy_.4111
+ ___Block_byref_object_copy_.4144
+ ___Block_byref_object_copy_.5017
+ ___Block_byref_object_copy_.5176
+ ___Block_byref_object_copy_.5323
+ ___Block_byref_object_copy_.6064
+ ___Block_byref_object_copy_.6501
+ ___Block_byref_object_copy_.6614
+ ___Block_byref_object_copy_.7117
+ ___Block_byref_object_copy_.9418
+ ___Block_byref_object_copy_.9523
+ ___Block_byref_object_dispose_.10336
+ ___Block_byref_object_dispose_.10634
+ ___Block_byref_object_dispose_.10762
+ ___Block_byref_object_dispose_.1103
+ ___Block_byref_object_dispose_.12286
+ ___Block_byref_object_dispose_.13629
+ ___Block_byref_object_dispose_.14173
+ ___Block_byref_object_dispose_.14345
+ ___Block_byref_object_dispose_.14610
+ ___Block_byref_object_dispose_.15021
+ ___Block_byref_object_dispose_.16156
+ ___Block_byref_object_dispose_.16635
+ ___Block_byref_object_dispose_.16862
+ ___Block_byref_object_dispose_.18593
+ ___Block_byref_object_dispose_.18959
+ ___Block_byref_object_dispose_.19172
+ ___Block_byref_object_dispose_.20156
+ ___Block_byref_object_dispose_.21063
+ ___Block_byref_object_dispose_.21869
+ ___Block_byref_object_dispose_.22486
+ ___Block_byref_object_dispose_.2257
+ ___Block_byref_object_dispose_.22586
+ ___Block_byref_object_dispose_.25003
+ ___Block_byref_object_dispose_.2515
+ ___Block_byref_object_dispose_.25434
+ ___Block_byref_object_dispose_.25995
+ ___Block_byref_object_dispose_.26348
+ ___Block_byref_object_dispose_.26390
+ ___Block_byref_object_dispose_.27310
+ ___Block_byref_object_dispose_.28273
+ ___Block_byref_object_dispose_.29300
+ ___Block_byref_object_dispose_.29642
+ ___Block_byref_object_dispose_.30677
+ ___Block_byref_object_dispose_.31596
+ ___Block_byref_object_dispose_.31981
+ ___Block_byref_object_dispose_.3204
+ ___Block_byref_object_dispose_.32159
+ ___Block_byref_object_dispose_.32319
+ ___Block_byref_object_dispose_.3271
+ ___Block_byref_object_dispose_.33075
+ ___Block_byref_object_dispose_.35128
+ ___Block_byref_object_dispose_.35353
+ ___Block_byref_object_dispose_.35487
+ ___Block_byref_object_dispose_.3608
+ ___Block_byref_object_dispose_.36350
+ ___Block_byref_object_dispose_.36513
+ ___Block_byref_object_dispose_.37201
+ ___Block_byref_object_dispose_.37472
+ ___Block_byref_object_dispose_.38059
+ ___Block_byref_object_dispose_.38238
+ ___Block_byref_object_dispose_.38544
+ ___Block_byref_object_dispose_.39396
+ ___Block_byref_object_dispose_.3966
+ ___Block_byref_object_dispose_.4112
+ ___Block_byref_object_dispose_.4145
+ ___Block_byref_object_dispose_.5018
+ ___Block_byref_object_dispose_.5177
+ ___Block_byref_object_dispose_.5324
+ ___Block_byref_object_dispose_.6065
+ ___Block_byref_object_dispose_.6502
+ ___Block_byref_object_dispose_.6615
+ ___Block_byref_object_dispose_.7118
+ ___Block_byref_object_dispose_.9419
+ ___Block_byref_object_dispose_.9524
+ ___MusicLibraryLibraryCore_block_invoke.21907
+ ___MusicLibraryLibraryCore_block_invoke.31311
+ ___block_descriptor_40_e8_32bs_e49_v28?0B8"NSError"12"ICPlaybackPositionEntity"20ls32l8
+ ___block_descriptor_40_e8_32s_e60_v24?0"<ICMediaUserStateCenterServerProtocol>"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10.26002
+ ___block_literal_global.10426
+ ___block_literal_global.11379
+ ___block_literal_global.11819
+ ___block_literal_global.12.24794
+ ___block_literal_global.12.26000
+ ___block_literal_global.12391
+ ___block_literal_global.13.38552
+ ___block_literal_global.13034
+ ___block_literal_global.13076
+ ___block_literal_global.13661
+ ___block_literal_global.1437
+ ___block_literal_global.15059
+ ___block_literal_global.156
+ ___block_literal_global.16557
+ ___block_literal_global.169.28570
+ ___block_literal_global.174.10421
+ ___block_literal_global.17621
+ ___block_literal_global.18.35185
+ ___block_literal_global.180
+ ___block_literal_global.18030
+ ___block_literal_global.18424
+ ___block_literal_global.18644
+ ___block_literal_global.18859
+ ___block_literal_global.19.25887
+ ___block_literal_global.194
+ ___block_literal_global.20027
+ ___block_literal_global.21
+ ___block_literal_global.210
+ ___block_literal_global.21705
+ ___block_literal_global.21929
+ ___block_literal_global.22386
+ ___block_literal_global.2265
+ ___block_literal_global.2347
+ ___block_literal_global.23947
+ ___block_literal_global.24070
+ ___block_literal_global.24793
+ ___block_literal_global.24990
+ ___block_literal_global.25501
+ ___block_literal_global.25666
+ ___block_literal_global.25869
+ ___block_literal_global.26008
+ ___block_literal_global.2637
+ ___block_literal_global.27343
+ ___block_literal_global.27858
+ ___block_literal_global.28670
+ ___block_literal_global.2881
+ ___block_literal_global.29008
+ ___block_literal_global.29313
+ ___block_literal_global.29462
+ ___block_literal_global.3.15057
+ ___block_literal_global.3.17628
+ ___block_literal_global.30450
+ ___block_literal_global.31007
+ ___block_literal_global.31067
+ ___block_literal_global.31482
+ ___block_literal_global.32054
+ ___block_literal_global.32667
+ ___block_literal_global.33111
+ ___block_literal_global.3420
+ ___block_literal_global.34244
+ ___block_literal_global.34768
+ ___block_literal_global.35208
+ ___block_literal_global.361
+ ___block_literal_global.3626
+ ___block_literal_global.36290
+ ___block_literal_global.37213
+ ___block_literal_global.37577
+ ___block_literal_global.37673
+ ___block_literal_global.382
+ ___block_literal_global.38382
+ ___block_literal_global.38562
+ ___block_literal_global.3897
+ ___block_literal_global.39496
+ ___block_literal_global.39637
+ ___block_literal_global.39767
+ ___block_literal_global.40442
+ ___block_literal_global.40674
+ ___block_literal_global.41005
+ ___block_literal_global.4162
+ ___block_literal_global.4225
+ ___block_literal_global.4347
+ ___block_literal_global.47.31107
+ ___block_literal_global.52.31112
+ ___block_literal_global.53.37575
+ ___block_literal_global.5479
+ ___block_literal_global.566
+ ___block_literal_global.569
+ ___block_literal_global.5944
+ ___block_literal_global.6.26006
+ ___block_literal_global.66
+ ___block_literal_global.6688
+ ___block_literal_global.6784
+ ___block_literal_global.69.22363
+ ___block_literal_global.7001
+ ___block_literal_global.7164
+ ___block_literal_global.7397
+ ___block_literal_global.76.31132
+ ___block_literal_global.8.26004
+ ___block_literal_global.8114
+ ___block_literal_global.8193
+ ___block_literal_global.82
+ ___block_literal_global.85
+ ___block_literal_global.9127
+ ___block_literal_global.9918
+ ___getML3MusicLibraryClass_block_invoke.21905
+ ___getML3TrackPropertyAlbumSymbolLoc_block_invoke
+ ___getML3TrackPropertyArtistSymbolLoc_block_invoke
+ ___getML3TrackPropertyFeedURLSymbolLoc_block_invoke
+ ___getML3TrackPropertyPodcastExternalGUIDSymbolLoc_block_invoke
+ ___getML3TrackPropertyTitleSymbolLoc_block_invoke
+ __unnamed_array_storage.187
+ __unnamed_array_storage.188
+ __unnamed_array_storage.205
+ __unnamed_array_storage.211
+ __unnamed_array_storage.214
+ __unnamed_array_storage.215
+ __unnamed_array_storage.218
+ __unnamed_array_storage.233
+ __unnamed_array_storage.239
+ __unnamed_array_storage.240
+ __unnamed_array_storage.246
+ __unnamed_array_storage.249
+ __unnamed_array_storage.250
+ __unnamed_array_storage.253
+ __unnamed_array_storage.259
+ __unnamed_array_storage.260
+ __unnamed_array_storage.263
+ __unnamed_array_storage.273
+ __unnamed_array_storage.279
+ __unnamed_array_storage.280
+ __unnamed_array_storage.286
+ __unnamed_array_storage.289
+ __unnamed_array_storage.290
+ __unnamed_array_storage.296
+ __unnamed_array_storage.302
+ __unnamed_array_storage.303
+ __unnamed_array_storage.309
+ __unnamed_array_storage.30957
+ __unnamed_array_storage.31111
+ __unnamed_array_storage.312
+ __unnamed_array_storage.313
+ __unnamed_array_storage.316
+ __unnamed_array_storage.322
+ __unnamed_array_storage.328
+ __unnamed_array_storage.329
+ __unnamed_array_storage.332
+ __unnamed_array_storage.335
+ __unnamed_array_storage.336
+ __unnamed_array_storage.339
+ __unnamed_array_storage.347
+ __unnamed_array_storage.348
+ __unnamed_array_storage.40899
+ __unnamed_array_storage.96.40900
+ _audit_stringMusicLibrary.21922
+ _audit_stringMusicLibrary.31314
+ _getML3MusicLibraryClass.21903
+ _getML3MusicLibraryClass.softClass.21904
+ _getML3TrackPropertyAlbum
+ _getML3TrackPropertyAlbumSymbolLoc.ptr
+ _getML3TrackPropertyArtist
+ _getML3TrackPropertyArtistSymbolLoc.ptr
+ _getML3TrackPropertyFeedURL
+ _getML3TrackPropertyFeedURLSymbolLoc.ptr
+ _getML3TrackPropertyPodcastExternalGUID
+ _getML3TrackPropertyPodcastExternalGUIDSymbolLoc.ptr
+ _getML3TrackPropertyTitle
+ _getML3TrackPropertyTitleSymbolLoc.ptr
+ _objc_msgSend$aggregatedPerformanceMetrics
+ _objc_msgSend$autoupdatingSharedLibrary
+ _objc_msgSend$bookmarkTime
+ _objc_msgSend$bookmarkTimestamp
+ _objc_msgSend$dateFromMilliseconds:
+ _objc_msgSend$deletePlaybackPositionEntitiesFromLibraryWithIdentifier:
+ _objc_msgSend$deletePlaybackPositionEntity:
+ _objc_msgSend$getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:
+ _objc_msgSend$hasBeenPlayed
+ _objc_msgSend$initWithDomain:
+ _objc_msgSend$itemPersistentIdentifier
+ _objc_msgSend$keyValueStoreItemIdentifierForUniqueStoreID:itemTitle:albumName:itemArtistName:feedURL:feedGUID:
+ _objc_msgSend$libraryIdentifier
+ _objc_msgSend$libraryUID
+ _objc_msgSend$performBlockAfterServerSetup:
+ _objc_msgSend$persistPlaybackPositionEntity:isCheckpoint:completionBlock:
+ _objc_msgSend$playbackPositionDomain
+ _objc_msgSend$playbackPositionKey
+ _objc_msgSend$promiseWithTimeout:
+ _objc_msgSend$pullPlaybackPositionEntity:completionBlock:
+ _objc_msgSend$pushPlaybackPositionEntity:completionBlock:
+ _objc_msgSend$setAggregatedPerformanceMetrics:
+ _objc_msgSend$setBookmarkTime:
+ _objc_msgSend$setBookmarkTimestamp:
+ _objc_msgSend$setHasBeenPlayed:
+ _objc_msgSend$setItemPersistentIdentifier:
+ _objc_msgSend$setLibraryIdentifier:
+ _objc_msgSend$setPlaybackPositionKey:
+ _objc_msgSend$setUserPlayCount:
+ _objc_msgSend$sharedActivityType
+ _objc_msgSend$synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:
+ _objc_msgSend$updateForeignDatabaseWithValuesFromPlaybackPositionEntity:
+ _objc_msgSend$userPlayCount
+ _sharedCache.sOnceToken.29461
+ _sharedCache.sSharedCache.29463
+ _sharedController.sOnceToken.35207
+ _sharedController.sOnceToken.38561
+ _sharedController.sSharedController.35209
+ _sharedController.sSharedController.38563
+ _sharedManager.sOnceToken.18858
+ _sharedManager.sOnceToken.27857
+ _sharedManager.sSharedManager.18860
+ _sharedManager.sSharedManager.27859
+ _sharedMonitor.sOnceToken.18029
+ _sharedMonitor.sOnceToken.39495
+ _sharedMonitor.sSharedMonitor.18031
+ _sharedMonitor.sSharedMonitor.39497
+ _sharedProvider.sOnceToken.39766
+ _sharedProvider.sSharedProvider.39768
+ _sharedService.__sharedService
+ _sharedService.onceToken
+ _wmhYOjgJkR
- -[ICMediaUserStateCenter _getUserStatesCacheOnly]
- -[ICURLRequest performanceMetrics]
- -[ICURLRequest setPerformanceMetrics:]
- -[ICURLResponse setPerformanceMetrics:]
- GCC_except_table2108
- GCC_except_table2110
- GCC_except_table2113
- GCC_except_table2118
- GCC_except_table2121
- GCC_except_table2134
- GCC_except_table5209
- GCC_except_table5305
- GCC_except_table5384
- GCC_except_table5385
- GCC_except_table5458
- GCC_except_table5474
- GCC_except_table5751
- GCC_except_table5758
- GCC_except_table5766
- GCC_except_table5777
- GCC_except_table5779
- GCC_except_table5784
- GCC_except_table5791
- GCC_except_table5801
- GCC_except_table5816
- GCC_except_table5824
- GCC_except_table5833
- GCC_except_table5842
- GCC_except_table5875
- GCC_except_table5889
- GCC_except_table5898
- GCC_except_table5905
- GCC_except_table5906
- GCC_except_table5965
- GCC_except_table5968
- GCC_except_table6008
- GCC_except_table6014
- GCC_except_table6017
- GCC_except_table6020
- GCC_except_table6023
- GCC_except_table6026
- GCC_except_table6029
- GCC_except_table6032
- GCC_except_table6035
- GCC_except_table6038
- GCC_except_table6044
- GCC_except_table6144
- GCC_except_table6157
- GCC_except_table6350
- GCC_except_table6357
- GCC_except_table6531
- GCC_except_table6535
- GCC_except_table6537
- GCC_except_table6560
- GCC_except_table6606
- GCC_except_table6793
- GCC_except_table6926
- GCC_except_table7069
- GCC_except_table7082
- GCC_except_table7103
- GCC_except_table7114
- GCC_except_table7158
- GCC_except_table7176
- GCC_except_table7228
- GCC_except_table7231
- GCC_except_table7240
- GCC_except_table7247
- GCC_except_table7288
- GCC_except_table7307
- GCC_except_table7340
- GCC_except_table7398
- GCC_except_table7399
- GCC_except_table7412
- GCC_except_table7829
- GCC_except_table7835
- GCC_except_table7857
- GCC_except_table7861
- GCC_except_table7872
- GCC_except_table7877
- GCC_except_table7912
- GCC_except_table7915
- GCC_except_table7977
- GCC_except_table8022
- GCC_except_table8070
- GCC_except_table8095
- GCC_except_table8100
- GCC_except_table8102
- GCC_except_table8104
- GCC_except_table8136
- GCC_except_table8279
- GCC_except_table8287
- GCC_except_table8292
- GCC_except_table8307
- GCC_except_table8315
- GCC_except_table8359
- GCC_except_table8493
- GCC_except_table8497
- GCC_except_table8499
- GCC_except_table8536
- GCC_except_table8539
- GCC_except_table8546
- GCC_except_table8549
- GCC_except_table8760
- GCC_except_table8764
- GCC_except_table8804
- _MSVFastHexStringFromBytes.hexCharacters.40692
- _OBJC_IVAR_$_ICURLRequest._performanceMetrics
- _OBJC_IVAR_$_ICURLResponse._performanceMetrics
- __MSV_XXH_XXH32_update.11588
- __MSV_XXH_XXH32_update.17294
- __MSV_XXH_XXH32_update.20239
- __MSV_XXH_XXH32_update.40681
- __MSV_XXH_XXH64_digest.17416
- __MSV_XXH_XXH64_update.11589
- __MSV_XXH_XXH64_update.17295
- __MSV_XXH_XXH64_update.20240
- __MSV_XXH_XXH64_update.40682
- __OBJC_$_PROP_LIST_ICStorePlatformResponse.135
- ___108-[ICInAppMessageManager _updateShouldDownloadResources:onMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.411
- ___110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke.620
- ___110-[ICSharedListeningQueue insertTracklist:afterItemIdentifier:playNowWithPreferredStartIndexPath:completionEx:]_block_invoke_2.625
- ___30-[ICURLBagProvider _loadCache]_block_invoke.134
- ___31-[ICURLSession _finishRequest:]_block_invoke.63
- ___31-[ICURLSession _finishRequest:]_block_invoke_2.64
- ___32-[ICURLSession _processRequest:]_block_invoke.61
- ___34-[ICURLBagProvider _loadMonoCache]_block_invoke.139
- ___39-[ICURLSession _processPendingRequests]_block_invoke.60
- ___45-[ICInAppMessageManager _xpcClientConnection]_block_invoke.361
- ___48-[ICInAppMessageManager _schedulePeriodicUpdate]_block_invoke.364
- ___49-[ICMediaUserStateCenter _getUserStatesCacheOnly]_block_invoke
- ___49-[ICMediaUserStateCenter _getUserStatesCacheOnly]_block_invoke.93
- ___52-[ICInAppMessageManager _performSyncRetryIfPending:]_block_invoke.407
- ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.371
- ___52-[ICInAppMessageManager _performSyncWithCompletion:]_block_invoke.376
- ___52-[ICMediaUserStateCenter _establishClientConnection]_block_invoke.89
- ___53-[ICInAppMessageManager _addMessageEntry:completion:]_block_invoke.383
- ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.126
- ___55-[ICMediaUserStateCenter _getUserStatesForcingRefresh:]_block_invoke.95
- ___57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.379
- ___57-[ICInAppMessageManager _processSyncResponse:completion:]_block_invoke.382
- ___58-[ICMediaUserStateCenter refreshUserStatesWithCompletion:]_block_invoke.28
- ___60-[ICInAppMessageManager listener:shouldAcceptNewConnection:]_block_invoke.450
- ___60-[ICLibraryAuthServiceClientTokenProvider _clientConnection]_block_invoke.141
- ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.178
- ___63-[ICPlayActivityCenter _daemonPlayActivityControllerConnection]_block_invoke.66
- ___65-[ICMediaUserStateCenter _applyServerStateUpdatedWithUserStates:]_block_invoke.103
- ___66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke.610
- ___66-[ICSharedListeningQueue insertTracklist:atPosition:completionEx:]_block_invoke_2.615
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.122
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.123
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.124
- ___70-[ICDeveloperTokenDefaultProvider _fetchDeveloperTokenWithClientInfo:]_block_invoke_2
- ___71-[ICCloudClientAvailabilityService _xpcConnectionWithListenerEndpoint:]_block_invoke.78
- ___73-[ICCloudContentTasteRequestListener _setupContentTasteServiceConnection]_block_invoke.82
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.191
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.194
- ___78-[ICExternalSharedListeningConnectionController _initializeConnectionIfNeeded]_block_invoke.197
- ___78-[ICExternalSharedListeningConnectionController _initializeConnectionIfNeeded]_block_invoke.201
- ___78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.198
- ___78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.591
- ___78-[ICSharedListeningQueue replaceTracklist:preferredStartIndexPath:completion:]_block_invoke.596
- ___79-[ICCloudServiceStatusMonitor requestAuthorizationForScopes:completionHandler:]_block_invoke.156
- ___79-[ICCloudServiceStatusMonitor requestAuthorizationForScopes:completionHandler:]_block_invoke_2.160
- ___80-[ICInAppMessageManager _removeAllMessageEntriesForBundleIdentifier:completion:]_block_invoke.404
- ___81-[ICCloudServiceStatusMonitor _validateAuthorizationExpiryWithCompletionHandler:]_block_invoke.173
- ___81-[ICCloudServiceStatusMonitor _validateAuthorizationExpiryWithCompletionHandler:]_block_invoke.176
- ___84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke.415
- ___84-[ICInAppMessageManager _checkForMessageResourcesNeedingDownloadForcingIfNecessary:]_block_invoke_2.416
- ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke.121
- ___85-[ICCloudServiceStatusMonitor revokeMusicKitUserTokensForAccountDSID:withCompletion:]_block_invoke.124
- ___90-[ICInAppMessageManager _removeMessageEntryWithIdentifier:forBundleIdentifier:completion:]_block_invoke.401
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.421
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.425
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.428
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke.434
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke_2.433
- ___96-[ICInAppMessageManager _downloadResourcesForMessageWithIdentifier:bundleIdentifier:completion:]_block_invoke_2.436
- ___Block_byref_object_copy_.10293
- ___Block_byref_object_copy_.10580
- ___Block_byref_object_copy_.10708
- ___Block_byref_object_copy_.1103
- ___Block_byref_object_copy_.12236
- ___Block_byref_object_copy_.13583
- ___Block_byref_object_copy_.14125
- ___Block_byref_object_copy_.14298
- ___Block_byref_object_copy_.14563
- ___Block_byref_object_copy_.14970
- ___Block_byref_object_copy_.16099
- ___Block_byref_object_copy_.16578
- ___Block_byref_object_copy_.16805
- ___Block_byref_object_copy_.18501
- ___Block_byref_object_copy_.18866
- ___Block_byref_object_copy_.19076
- ___Block_byref_object_copy_.20068
- ___Block_byref_object_copy_.20966
- ___Block_byref_object_copy_.22233
- ___Block_byref_object_copy_.22334
- ___Block_byref_object_copy_.2254
- ___Block_byref_object_copy_.24742
- ___Block_byref_object_copy_.2507
- ___Block_byref_object_copy_.25171
- ___Block_byref_object_copy_.25732
- ___Block_byref_object_copy_.26087
- ___Block_byref_object_copy_.26129
- ___Block_byref_object_copy_.27050
- ___Block_byref_object_copy_.28010
- ___Block_byref_object_copy_.29039
- ___Block_byref_object_copy_.29381
- ___Block_byref_object_copy_.30417
- ___Block_byref_object_copy_.31144
- ___Block_byref_object_copy_.31525
- ___Block_byref_object_copy_.31702
- ___Block_byref_object_copy_.31862
- ___Block_byref_object_copy_.3189
- ___Block_byref_object_copy_.3256
- ___Block_byref_object_copy_.32622
- ___Block_byref_object_copy_.34654
- ___Block_byref_object_copy_.34879
- ___Block_byref_object_copy_.35013
- ___Block_byref_object_copy_.35874
- ___Block_byref_object_copy_.3597
- ___Block_byref_object_copy_.36037
- ___Block_byref_object_copy_.36723
- ___Block_byref_object_copy_.36993
- ___Block_byref_object_copy_.37584
- ___Block_byref_object_copy_.37763
- ___Block_byref_object_copy_.38068
- ___Block_byref_object_copy_.38914
- ___Block_byref_object_copy_.3954
- ___Block_byref_object_copy_.4093
- ___Block_byref_object_copy_.4126
- ___Block_byref_object_copy_.4992
- ___Block_byref_object_copy_.5150
- ___Block_byref_object_copy_.5280
- ___Block_byref_object_copy_.6029
- ___Block_byref_object_copy_.6462
- ___Block_byref_object_copy_.6574
- ___Block_byref_object_copy_.7077
- ___Block_byref_object_copy_.9382
- ___Block_byref_object_copy_.9487
- ___Block_byref_object_dispose_.10294
- ___Block_byref_object_dispose_.10581
- ___Block_byref_object_dispose_.10709
- ___Block_byref_object_dispose_.1104
- ___Block_byref_object_dispose_.12237
- ___Block_byref_object_dispose_.13584
- ___Block_byref_object_dispose_.14126
- ___Block_byref_object_dispose_.14299
- ___Block_byref_object_dispose_.14564
- ___Block_byref_object_dispose_.14971
- ___Block_byref_object_dispose_.16100
- ___Block_byref_object_dispose_.16579
- ___Block_byref_object_dispose_.16806
- ___Block_byref_object_dispose_.18502
- ___Block_byref_object_dispose_.18867
- ___Block_byref_object_dispose_.19077
- ___Block_byref_object_dispose_.20069
- ___Block_byref_object_dispose_.20967
- ___Block_byref_object_dispose_.22234
- ___Block_byref_object_dispose_.22335
- ___Block_byref_object_dispose_.2255
- ___Block_byref_object_dispose_.24743
- ___Block_byref_object_dispose_.2508
- ___Block_byref_object_dispose_.25172
- ___Block_byref_object_dispose_.25733
- ___Block_byref_object_dispose_.26088
- ___Block_byref_object_dispose_.26130
- ___Block_byref_object_dispose_.27051
- ___Block_byref_object_dispose_.28011
- ___Block_byref_object_dispose_.29040
- ___Block_byref_object_dispose_.29382
- ___Block_byref_object_dispose_.30418
- ___Block_byref_object_dispose_.31145
- ___Block_byref_object_dispose_.31526
- ___Block_byref_object_dispose_.31703
- ___Block_byref_object_dispose_.31863
- ___Block_byref_object_dispose_.3190
- ___Block_byref_object_dispose_.3257
- ___Block_byref_object_dispose_.32623
- ___Block_byref_object_dispose_.34655
- ___Block_byref_object_dispose_.34880
- ___Block_byref_object_dispose_.35014
- ___Block_byref_object_dispose_.35875
- ___Block_byref_object_dispose_.3598
- ___Block_byref_object_dispose_.36038
- ___Block_byref_object_dispose_.36724
- ___Block_byref_object_dispose_.36994
- ___Block_byref_object_dispose_.37585
- ___Block_byref_object_dispose_.37764
- ___Block_byref_object_dispose_.38069
- ___Block_byref_object_dispose_.38915
- ___Block_byref_object_dispose_.3955
- ___Block_byref_object_dispose_.4094
- ___Block_byref_object_dispose_.4127
- ___Block_byref_object_dispose_.4993
- ___Block_byref_object_dispose_.5151
- ___Block_byref_object_dispose_.5281
- ___Block_byref_object_dispose_.6030
- ___Block_byref_object_dispose_.6463
- ___Block_byref_object_dispose_.6575
- ___Block_byref_object_dispose_.7078
- ___Block_byref_object_dispose_.9383
- ___Block_byref_object_dispose_.9488
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_48_e8_32s40r_e60_v24?0"<ICMediaUserStateCenterServerProtocol>"8"NSError"16ls32l8r40l8
- ___block_literal_global.10.25742
- ___block_literal_global.10383
- ___block_literal_global.11325
- ___block_literal_global.11767
- ___block_literal_global.12.24536
- ___block_literal_global.12.25740
- ___block_literal_global.12346
- ___block_literal_global.12989
- ___block_literal_global.13.38077
- ___block_literal_global.13031
- ___block_literal_global.13614
- ___block_literal_global.1440
- ___block_literal_global.15009
- ___block_literal_global.157.5223
- ___block_literal_global.16502
- ___block_literal_global.168.28311
- ___block_literal_global.173
- ___block_literal_global.17535
- ___block_literal_global.179
- ___block_literal_global.17941
- ___block_literal_global.18.25738
- ___block_literal_global.18.34712
- ___block_literal_global.18333
- ___block_literal_global.18553
- ___block_literal_global.18767
- ___block_literal_global.19.25625
- ___block_literal_global.193
- ___block_literal_global.19935
- ___block_literal_global.204
- ___block_literal_global.21609
- ___block_literal_global.22135
- ___block_literal_global.2263
- ___block_literal_global.2341
- ___block_literal_global.23688
- ___block_literal_global.23812
- ___block_literal_global.24535
- ___block_literal_global.24729
- ___block_literal_global.25239
- ___block_literal_global.25404
- ___block_literal_global.25607
- ___block_literal_global.25748
- ___block_literal_global.2624
- ___block_literal_global.27084
- ___block_literal_global.27599
- ___block_literal_global.28410
- ___block_literal_global.2868
- ___block_literal_global.28750
- ___block_literal_global.29053
- ___block_literal_global.29203
- ___block_literal_global.3.15007
- ___block_literal_global.3.17542
- ___block_literal_global.30192
- ___block_literal_global.30745
- ___block_literal_global.30805
- ___block_literal_global.31031
- ___block_literal_global.31599
- ___block_literal_global.32216
- ___block_literal_global.32659
- ___block_literal_global.33775
- ___block_literal_global.3410
- ___block_literal_global.34297
- ___block_literal_global.34735
- ___block_literal_global.35815
- ___block_literal_global.360
- ___block_literal_global.3616
- ___block_literal_global.36736
- ___block_literal_global.37103
- ___block_literal_global.37200
- ___block_literal_global.37907
- ___block_literal_global.38087
- ___block_literal_global.381
- ___block_literal_global.3888
- ___block_literal_global.39025
- ___block_literal_global.39165
- ___block_literal_global.39295
- ___block_literal_global.39988
- ___block_literal_global.40178
- ___block_literal_global.40511
- ___block_literal_global.4144
- ___block_literal_global.4203
- ___block_literal_global.4323
- ___block_literal_global.47.30845
- ___block_literal_global.49
- ___block_literal_global.52.30850
- ___block_literal_global.5444
- ___block_literal_global.551
- ___block_literal_global.554
- ___block_literal_global.5909
- ___block_literal_global.6.25746
- ___block_literal_global.65
- ___block_literal_global.6649
- ___block_literal_global.6744
- ___block_literal_global.68.30701
- ___block_literal_global.6961
- ___block_literal_global.7124
- ___block_literal_global.7355
- ___block_literal_global.76.30870
- ___block_literal_global.8.25744
- ___block_literal_global.8073
- ___block_literal_global.81
- ___block_literal_global.8154
- ___block_literal_global.84
- ___block_literal_global.9088
- ___block_literal_global.9884
- __unnamed_array_storage.185
- __unnamed_array_storage.186
- __unnamed_array_storage.203
- __unnamed_array_storage.209
- __unnamed_array_storage.212
- __unnamed_array_storage.213
- __unnamed_array_storage.216
- __unnamed_array_storage.231
- __unnamed_array_storage.237
- __unnamed_array_storage.238
- __unnamed_array_storage.244
- __unnamed_array_storage.247
- __unnamed_array_storage.248
- __unnamed_array_storage.251
- __unnamed_array_storage.257
- __unnamed_array_storage.258
- __unnamed_array_storage.261
- __unnamed_array_storage.271
- __unnamed_array_storage.277
- __unnamed_array_storage.278
- __unnamed_array_storage.284
- __unnamed_array_storage.287
- __unnamed_array_storage.288
- __unnamed_array_storage.294
- __unnamed_array_storage.300
- __unnamed_array_storage.301
- __unnamed_array_storage.30694
- __unnamed_array_storage.307
- __unnamed_array_storage.30849
- __unnamed_array_storage.310
- __unnamed_array_storage.311
- __unnamed_array_storage.314
- __unnamed_array_storage.320
- __unnamed_array_storage.326
- __unnamed_array_storage.327
- __unnamed_array_storage.330
- __unnamed_array_storage.333
- __unnamed_array_storage.334
- __unnamed_array_storage.337
- __unnamed_array_storage.345
- __unnamed_array_storage.346
- __unnamed_array_storage.40404
- __unnamed_array_storage.96.40405
- _arc4random_uniform
- _objc_msgSend$_getUserStatesCacheOnly
- _objc_msgSend$setPerformanceMetrics:
- _sharedCache.sOnceToken.29202
- _sharedCache.sSharedCache.29204
- _sharedController.sOnceToken.34734
- _sharedController.sOnceToken.38086
- _sharedController.sSharedController.34736
- _sharedController.sSharedController.38088
- _sharedManager.sOnceToken.18766
- _sharedManager.sOnceToken.27598
- _sharedManager.sSharedManager.18768
- _sharedManager.sSharedManager.27600
- _sharedMonitor.sOnceToken.17940
- _sharedMonitor.sOnceToken.39024
- _sharedMonitor.sSharedMonitor.17942
- _sharedMonitor.sSharedMonitor.39026
- _sharedProvider.sOnceToken.39294
- _sharedProvider.sSharedProvider.39296
- _time
CStrings:
+ "\x01\x13d!\x11"
+ "    sharedActivityType:%lu\n"
+ "%{public}@ Could not get DSID for userIdentity=%{public}@."
+ "%{public}@ Failed to retrieve listener endpoint. error=%{public}@"
+ "%{public}@ Skipping notification for messageEntry=%{public}@ as there is no bundleIdentifier"
+ "%{public}@ developer token fetch completed for clientInfo %{public}@ with %lu handlers"
+ "%{public}@ fetching developer token with clientInfo %{public}@"
+ "%{public}@: Fetched userStates from init"
+ "%{public}@: Performing request."
+ "<%@ %p statusType:%@, matchEnabled=%@, carrierBundlingStatusType:%@, reasonType:%@, sourceType:%@%@, capabilities:%@, eligibleOffers:[%@], isInFreeTrial:%@, isEligibleForFreeTrial:%@, initialPurchaseTimestamp:%@, serviceBeginsTimestamp:%@>"
+ "<ICPlaybackPositionEntity %p domain=%@ playbackPositionID=%@ itemPID=%@ libraryUID=%@ bookmarkTime=%@ bookmarkTimestamp=%@ playCount=%@ hasBeenPlayed=%@>"
+ "@\"ICCloudClient\""
+ "@64@0:8q16@24@32@40@48@56"
+ "ICPlaybackPositionClient"
+ "ICPlaybackPositionClient - persistPlaybackPositionEntity: Completed. success=%{BOOL}u"
+ "ICPlaybackPositionClient - persistPlaybackPositionEntity: Completed. success=%{BOOL}u error=%{public}@"
+ "ICPlaybackPositionClient - pullPlaybackPositionEntity: Completed. success=%{BOOL}u cloudEntity=%{public}@"
+ "ICPlaybackPositionClient - pullPlaybackPositionEntity: Completed. success=%{BOOL}u cloudEntity=%{public}@ error=%{public}@"
+ "ICPlaybackPositionClient - pullPlaybackPositionEntity: Failed to get remote object proxy. error=%{public}@"
+ "ICPlaybackPositionClient - pushPlaybackPositionEntity: Completed. success=%{BOOL}u cloudEntity=%{public}@"
+ "ICPlaybackPositionClient - pushPlaybackPositionEntity: Completed. success=%{BOOL}u cloudEntity=%{public}@ error=%{public}@"
+ "ICPlaybackPositionClient - pushPlaybackPositionEntity: Failed to get remote object proxy. error=%{public}@"
+ "ICPlaybackPositionClient.m"
+ "ICPlaybackPositionEntity"
+ "ICPlaybackPositionEntity.m"
+ "ICPlaybackPositionService"
+ "ML3TrackPropertyAlbum"
+ "ML3TrackPropertyArtist"
+ "ML3TrackPropertyFeedURL"
+ "ML3TrackPropertyPodcastExternalGUID"
+ "ML3TrackPropertyTitle"
+ "NSString *getML3TrackPropertyAlbum(void)"
+ "NSString *getML3TrackPropertyArtist(void)"
+ "NSString *getML3TrackPropertyFeedURL(void)"
+ "NSString *getML3TrackPropertyPodcastExternalGUID(void)"
+ "NSString *getML3TrackPropertyTitle(void)"
+ "PlaybackPosition"
+ "T@\"AMSProcessInfo\",?,R,C,N"
+ "T@\"ICURLAggregatedPerformanceMetrics\",&,N,V_aggregatedPerformanceMetrics"
+ "T@\"ICURLAggregatedPerformanceMetrics\",R,N,V_aggregatedPerformanceMetrics"
+ "T@\"ICURLPerformanceMetrics\",R,N"
+ "T@\"NSDate\",R,C,N,V_initialPurchaseTimestamp"
+ "T@\"NSDate\",R,C,N,V_serviceBeginsTimestamp"
+ "T@\"NSNumber\",C,N,V_bookmarkTime"
+ "T@\"NSNumber\",C,N,V_bookmarkTimestamp"
+ "T@\"NSNumber\",C,N,V_hasBeenPlayed"
+ "T@\"NSNumber\",C,N,V_itemPersistentIdentifier"
+ "T@\"NSNumber\",C,N,V_userPlayCount"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_libraryIdentifier"
+ "T@\"NSString\",C,N,V_playbackPositionKey"
+ "T@\"NSString\",R,C,N,V_playbackPositionDomain"
+ "Tq,R,N,V_sharedActivityType"
+ "User assigned name requested without entitlement. Returning generic device name."
+ "[%{public}@ deletePlaybackPositionEntitiesFromLibraryWithIdentifier:] Completed for library with identifier %{public}@"
+ "[%{public}@ deletePlaybackPositionEntitiesFromLibraryWithIdentifier:] Failed to get remote object proxy. error=%{public}@"
+ "[%{public}@ deletePlaybackPositionEntity:] Completed for entity %{public}@"
+ "[%{public}@ deletePlaybackPositionEntity:] Failed to get remote object proxy. error=%{public}@"
+ "[%{public}@ getLocalPlaybackPositionForEntityIdentifiers:] Completed with %llu entities for domain %{public}@ with library (%{public}@). success=%{BOOL}u"
+ "[%{public}@ getLocalPlaybackPositionForEntityIdentifiers:] Completed with %llu entities for domain %{public}@ with library (%{public}@). success=%{BOOL}u error=%{public}@"
+ "[%{public}@ persistPlaybackPositionEntity:] Failed to get remote object proxy. error=%{public}@"
+ "[%{public}@ synchronizePlaybackPositionsForLibraryWithIdentifier:] Completed sync for library with identifier %{public}@. checkpoint=%{BOOL}u"
+ "[%{public}@ synchronizePlaybackPositionsForLibraryWithIdentifier:] Failed to get remote object proxy. error=%{public}@"
+ "[%{public}@ updateForeignDatabaseWithValuesFromPlaybackPositionEntity:] Completed for entity %{public}@"
+ "[%{publie}@ getLocalPlaybackPositionForEntityIdentifiers:] Failed to get remote object proxy. error=%{public}@"
+ "[%{publie}@ updateForeignDatabaseWithValuesFromPlaybackPositionEntity:] Failed to get remote object proxy. error=%{public}@"
+ "_aggregatedPerformanceMetrics"
+ "_bookmarkTime"
+ "_bookmarkTimestamp"
+ "_cloudClient"
+ "_hasBeenPlayed"
+ "_initialPurchaseTimestamp"
+ "_itemPersistentIdentifier"
+ "_libraryIdentifier"
+ "_playbackPositionDomain"
+ "_playbackPositionKey"
+ "_serviceBeginsTimestamp"
+ "_sharedActivityType"
+ "_userPlayCount"
+ "aggregatedPerformanceMetrics"
+ "autoupdatingSharedLibrary"
+ "bookmarkTime"
+ "bookmarkTimestamp"
+ "com.apple.developer.device-information.user-assigned-device-name"
+ "com.apple.iTunesCloud.ICPlaybackPositionClient.serialQueue"
+ "com.apple.upp"
+ "com.apple.upp-extras"
+ "contentKeySession:didProvideContentKeyRequests:forInitializationData:"
+ "contentKeySession:externalProtectionStatusDidChangeForContentKey:"
+ "dateFromMilliseconds:"
+ "deletePlaybackPositionEntities"
+ "deletePlaybackPositionEntitiesFromLibraryWithIdentifier:"
+ "deletePlaybackPositionEntity:"
+ "getLocalPlaybackPositionForEntityIdentifiers:completionBlock:"
+ "getLocalPlaybackPositionForEntityIdentifiers:forDomain:fromLibraryWithIdentifier:completionBlock:"
+ "hasBeenPlayed"
+ "https://bookkeeper.itunes.apple.com/WebObjects/MZBookkeeper.woa/wa/sync"
+ "initWithDomain:"
+ "initWithDomain:playbackPositionKey:persistentIdentifier:"
+ "initialPurchaseTimestamp"
+ "itemPersistenIdentifier"
+ "itemPersistentIdentifier"
+ "keyValueStoreItemIdentifierForUniqueStoreID:itemTitle:albumName:itemArtistName:feedURL:feedGUID:"
+ "kvs-get"
+ "kvs-getall"
+ "kvs-put"
+ "kvs-putall"
+ "kvs-sync"
+ "libraryIdentifier"
+ "libraryUID"
+ "persistPlaybackPositionEntity:isCheckpoint:completionBlock:"
+ "playCount"
+ "playbackPosition"
+ "playbackPositionDomain"
+ "playbackPositionKey"
+ "promiseWithTimeout:"
+ "pullPlaybackPositionEntity:completionBlock:"
+ "pushPlaybackPositionEntity:completionBlock:"
+ "serviceBeginsTimestamp"
+ "setAggregatedPerformanceMetrics:"
+ "setBookmarkTime:"
+ "setBookmarkTimestamp:"
+ "setHasBeenPlayed:"
+ "setInitialPurchaseTimestamp:"
+ "setItemPersistentIdentifier:"
+ "setLibraryIdentifier:"
+ "setPlaybackPositionKey:"
+ "setServiceBeginsTimestamp:"
+ "setSharedActivityType:"
+ "setUserPlayCount:"
+ "sharedActivityType"
+ "synchronizePlaybackPositions"
+ "synchronizePlaybackPositionsForLibraryWithIdentifier:forDomain:isCheckpoint:"
+ "ubiquitousIdentifierWithItemTitle:albumName:itemArtistName:"
+ "ubiquitousIdentifierWithPodcastFeedURL:feedGUID:"
+ "ubiquitousIdentifierWithUniqueStoreID:"
+ "ubiquitousIdentifierWithiTunesUFeedURL:feedGUID:"
+ "updateForeignDatabaseWithValuesFromPlaybackPositionEntity:"
+ "userPlayCount"
+ "v24@0:8@\"ICPlaybackPositionEntity\"16"
+ "v28@?0B8@\"NSError\"12@\"ICPlaybackPositionEntity\"20"
+ "v28@?0B8@\"NSError\"12@\"NSArray\"20"
+ "v32@0:8@\"AVContentKeySession\"16@\"AVContentKey\"24"
+ "v32@0:8@\"ICPlaybackPositionEntity\"16@?<v@?B@\"NSError\"@\"ICPlaybackPositionEntity\">24"
+ "v36@0:8@\"ICPlaybackPositionEntity\"16B24@?<v@?B@\"NSError\">28"
+ "v36@0:8@\"NSString\"16@\"NSString\"24B32"
+ "v40@0:8@\"AVContentKeySession\"16@\"NSArray\"24@\"NSData\"32"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\"@\"NSArray\">40"
+ "{?=\"characterDisplayedCount\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sharedActivityType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"isCollaborativePlaylist\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"
- "\x01\x11d!\x11"
- "%{public}@ Setting resolved DSID: %{public}@"
- "%{public}@: Failed to create sync server to get user states cache, err=%{public}@"
- "%{public}@: Fetched cached userStates from init"
- "%{public}@: _getUserStatesForcingRefresh:NO from init"
- "<%@ %p statusType:%@, matchEnabled=%@, carrierBundlingStatusType:%@, reasonType:%@, sourceType:%@%@, capabilities:%@, eligibleOffers:[%@], isInFreeTrial:%@, isEligibleForFreeTrial:%@>"
- "@\"ICURLPerformanceMetrics\""
- "T@\"AMSProcessInfo\",R,C,N"
- "T@\"ICURLPerformanceMetrics\",&,N,V_performanceMetrics"
- "_getUserStatesCacheOnly"
- "{?=\"characterDisplayedCount\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"isCollaborativePlaylist\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"

```
