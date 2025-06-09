## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4024.600.5.0.0
-  __TEXT.__text: 0x30515c
-  __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x173ec
-  __TEXT.__const: 0x19194
+4025.100.97.0.0
+  __TEXT.__text: 0x308224
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0x176b4
+  __TEXT.__const: 0x18e4c
   __TEXT.__dlopen_cstrs: 0x4cf
-  __TEXT.__gcc_except_tab: 0x3438
-  __TEXT.__cstring: 0x16c96
-  __TEXT.__oslogstring: 0x1e868
+  __TEXT.__gcc_except_tab: 0x34d0
+  __TEXT.__cstring: 0x16dc1
+  __TEXT.__oslogstring: 0x1f5cf
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x6840
-  __TEXT.__eh_frame: 0x22f8
-  __TEXT.__objc_classname: 0x3ac5
-  __TEXT.__objc_methname: 0x33d94
-  __TEXT.__objc_methtype: 0x79ee
-  __TEXT.__objc_stubs: 0x1ab40
-  __DATA_CONST.__got: 0xf88
-  __DATA_CONST.__const: 0x70d0
+  __TEXT.__unwind_info: 0x64d0
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x3ac6
+  __TEXT.__objc_methname: 0x34ba0
+  __TEXT.__objc_methtype: 0x7d00
+  __TEXT.__objc_stubs: 0x1afa0
+  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__const: 0x71f8
   __DATA_CONST.__objc_classlist: 0xd50
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9da0
+  __DATA_CONST.__objc_selrefs: 0x9f98
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xb78
   __DATA_CONST.__objc_arraydata: 0x468
-  __AUTH_CONST.__auth_got: 0xa30
-  __AUTH_CONST.__const: 0x11998
-  __AUTH_CONST.__cfstring: 0x17f00
-  __AUTH_CONST.__objc_const: 0x2f150
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__const: 0x11518
+  __AUTH_CONST.__cfstring: 0x18200
+  __AUTH_CONST.__objc_const: 0x2f418
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x4740
-  __DATA.__objc_ivar: 0x22b8
-  __DATA.__data: 0x2590
-  __DATA.__bss: 0x380
-  __DATA.__common: 0xa98
-  __DATA_DIRTY.__objc_data: 0x3de0
+  __AUTH.__objc_data: 0x4ba0
+  __DATA.__objc_ivar: 0x22e4
+  __DATA.__data: 0x2620
+  __DATA.__bss: 0x360
+  __DATA.__common: 0xa90
+  __DATA_DIRTY.__objc_data: 0x3980
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x430
+  __DATA_DIRTY.__bss: 0x450
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AB82E4D9-33DD-3DA3-8ACD-26706D467FC8
-  Functions: 9618
-  Symbols:   30595
-  CStrings:  17372
+  UUID: EFA18131-92AD-395D-BB0F-3FBA52F428EB
+  Functions: 9723
+  Symbols:   30871
+  CStrings:  17549
 
Symbols:
+ -[ICCloudClient addStoreItemsWithAdamIDs:referral:completionHandler:]
+ -[ICCloudClient handleAutomaticDownloadPreferenceChangedForPinnedLibraryEntities:]
+ -[ICCloudClient isAutomaticDownloadsEnabledForPinnedLibraryEntities]
+ -[ICCloudClient movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:]
+ -[ICCloudClient movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:]
+ -[ICCloudClient movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:]
+ -[ICCloudClient pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]
+ -[ICCloudClient pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]
+ -[ICCloudClient pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]
+ -[ICCloudClient removePinnedAlbumWithPersistentID:cloudAlbumID:completion:]
+ -[ICCloudClient removePinnedArtistWithPersistentID:cloudArtistID:completion:]
+ -[ICCloudClient removePinnedEntityWithPersistentID:cloudID:type:completion:]
+ -[ICCloudClient updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]
+ -[ICCloudClient updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]
+ -[ICCloudClient updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]
+ -[ICCloudServiceStatusMonitor _musicKit_importTrackWithID:addingToLibrary:completionHandler:]
+ -[ICDefaults shouldAllowUntrustedHosts]
+ -[ICMusicSubscriptionLeaseController didMigratePlaybackSession]
+ -[ICMusicSubscriptionLeaseSession _didMigratePlaybackSession]
+ -[ICMusicSubscriptionLeaseSession lastFairPlayKeyStatusReloadDate]
+ -[ICMusicSubscriptionStatus partner]
+ -[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:]
+ -[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:withCompletionHandler:]
+ -[ICMutableMusicSubscriptionStatus setPartner:]
+ -[ICMutablePlayActivityEvent setTransitionTypeProvided:]
+ -[ICMutablePlayActivityEvent setUserTransitionTypePreference:]
+ -[ICMutablePlayActivityEvent setWallClockPlayDuration:]
+ -[ICMutablePlayActivityEventContainerIDs setCloudPlaylistFolderID:]
+ -[ICPlayActivityEvent setTransitionTypeProvided:]
+ -[ICPlayActivityEvent setUserTransitionTypePreference:]
+ -[ICPlayActivityEvent setWallClockPlayDuration:]
+ -[ICPlayActivityEvent transitionTypeProvided]
+ -[ICPlayActivityEvent userTransitionTypePreference]
+ -[ICPlayActivityEvent wallClockPlayDuration]
+ -[ICPlayActivityEventContainerIDs cloudPlaylistFolderID]
+ -[ICStoreDialogResponseHandler handleAMSDialogRequest:completion:]
+ -[ICURLBagProvider _handleAMSBagInvalidatedNotification:]
+ -[ICURLBagProvider _invalidateCacheEntriesWithProfileName:profileVersion:]
+ -[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]
+ GCC_except_table1041
+ GCC_except_table1067
+ GCC_except_table1201
+ GCC_except_table1280
+ GCC_except_table1448
+ GCC_except_table1461
+ GCC_except_table1714
+ GCC_except_table1897
+ GCC_except_table1926
+ GCC_except_table1941
+ GCC_except_table1981
+ GCC_except_table2093
+ GCC_except_table2108
+ GCC_except_table2157
+ GCC_except_table2159
+ GCC_except_table2165
+ GCC_except_table2172
+ GCC_except_table2200
+ GCC_except_table2215
+ GCC_except_table2220
+ GCC_except_table2222
+ GCC_except_table2227
+ GCC_except_table2230
+ GCC_except_table2243
+ GCC_except_table2320
+ GCC_except_table2329
+ GCC_except_table2332
+ GCC_except_table2335
+ GCC_except_table2338
+ GCC_except_table2340
+ GCC_except_table2342
+ GCC_except_table2344
+ GCC_except_table2351
+ GCC_except_table2353
+ GCC_except_table2370
+ GCC_except_table2409
+ GCC_except_table2440
+ GCC_except_table2442
+ GCC_except_table2444
+ GCC_except_table2446
+ GCC_except_table2796
+ GCC_except_table2841
+ GCC_except_table2987
+ GCC_except_table3004
+ GCC_except_table3014
+ GCC_except_table3037
+ GCC_except_table3047
+ GCC_except_table3145
+ GCC_except_table3413
+ GCC_except_table3417
+ GCC_except_table3420
+ GCC_except_table3435
+ GCC_except_table3446
+ GCC_except_table3465
+ GCC_except_table3505
+ GCC_except_table3519
+ GCC_except_table3632
+ GCC_except_table3790
+ GCC_except_table3951
+ GCC_except_table3993
+ GCC_except_table406
+ GCC_except_table4091
+ GCC_except_table4099
+ GCC_except_table4101
+ GCC_except_table4103
+ GCC_except_table4105
+ GCC_except_table4107
+ GCC_except_table411
+ GCC_except_table4111
+ GCC_except_table4118
+ GCC_except_table4122
+ GCC_except_table4137
+ GCC_except_table4140
+ GCC_except_table4319
+ GCC_except_table4375
+ GCC_except_table4378
+ GCC_except_table4383
+ GCC_except_table4447
+ GCC_except_table4489
+ GCC_except_table4493
+ GCC_except_table4495
+ GCC_except_table4562
+ GCC_except_table4637
+ GCC_except_table4725
+ GCC_except_table4808
+ GCC_except_table4876
+ GCC_except_table4957
+ GCC_except_table5118
+ GCC_except_table5369
+ GCC_except_table5465
+ GCC_except_table5513
+ GCC_except_table5537
+ GCC_except_table5578
+ GCC_except_table5579
+ GCC_except_table5652
+ GCC_except_table5670
+ GCC_except_table5951
+ GCC_except_table5966
+ GCC_except_table5977
+ GCC_except_table5979
+ GCC_except_table5980
+ GCC_except_table5981
+ GCC_except_table5982
+ GCC_except_table5987
+ GCC_except_table5992
+ GCC_except_table5997
+ GCC_except_table6008
+ GCC_except_table6023
+ GCC_except_table6025
+ GCC_except_table6031
+ GCC_except_table6040
+ GCC_except_table6049
+ GCC_except_table6082
+ GCC_except_table6110
+ GCC_except_table6120
+ GCC_except_table6127
+ GCC_except_table6128
+ GCC_except_table6189
+ GCC_except_table6192
+ GCC_except_table6206
+ GCC_except_table6229
+ GCC_except_table6234
+ GCC_except_table6240
+ GCC_except_table6243
+ GCC_except_table6246
+ GCC_except_table6249
+ GCC_except_table6252
+ GCC_except_table6255
+ GCC_except_table6258
+ GCC_except_table6261
+ GCC_except_table6264
+ GCC_except_table6267
+ GCC_except_table6270
+ GCC_except_table6371
+ GCC_except_table6384
+ GCC_except_table6585
+ GCC_except_table6592
+ GCC_except_table6764
+ GCC_except_table6768
+ GCC_except_table6770
+ GCC_except_table678
+ GCC_except_table6797
+ GCC_except_table6843
+ GCC_except_table690
+ GCC_except_table7025
+ GCC_except_table7158
+ GCC_except_table7299
+ GCC_except_table7312
+ GCC_except_table732
+ GCC_except_table7335
+ GCC_except_table7346
+ GCC_except_table7391
+ GCC_except_table7392
+ GCC_except_table7393
+ GCC_except_table7394
+ GCC_except_table7395
+ GCC_except_table7436
+ GCC_except_table7454
+ GCC_except_table7506
+ GCC_except_table7509
+ GCC_except_table7518
+ GCC_except_table7525
+ GCC_except_table7572
+ GCC_except_table7624
+ GCC_except_table7682
+ GCC_except_table7683
+ GCC_except_table7696
+ GCC_except_table8113
+ GCC_except_table8117
+ GCC_except_table8121
+ GCC_except_table8143
+ GCC_except_table8147
+ GCC_except_table8158
+ GCC_except_table8163
+ GCC_except_table8198
+ GCC_except_table8201
+ GCC_except_table8268
+ GCC_except_table8313
+ GCC_except_table8362
+ GCC_except_table8390
+ GCC_except_table8395
+ GCC_except_table8397
+ GCC_except_table8399
+ GCC_except_table8431
+ GCC_except_table844
+ GCC_except_table853
+ GCC_except_table8574
+ GCC_except_table8582
+ GCC_except_table8587
+ GCC_except_table8602
+ GCC_except_table8610
+ GCC_except_table8654
+ GCC_except_table8687
+ GCC_except_table8787
+ GCC_except_table8791
+ GCC_except_table8793
+ GCC_except_table8830
+ GCC_except_table8833
+ GCC_except_table8840
+ GCC_except_table8843
+ GCC_except_table9052
+ GCC_except_table9056
+ GCC_except_table9096
+ GCC_except_table9193
+ GCC_except_table9198
+ GCC_except_table945
+ GCC_except_table953
+ _AMSBagInvalidatedNotification
+ _DAAPPinTypeFromICLibraryPinEntityType
+ _ICArtworkInfoKeyArtworkDictionaryTVCoverArtworkTemplateURL
+ _ICArtworkInfoKeyArtworkDictionaryTVCoverArtworkToken
+ _ICPAPlayActivityEventReadFrom
+ _ICURLBagKeyImagePreconnectURL
+ _MSVDeviceIsROSDevice
+ _MSVDeviceIsiPad
+ _MSVDeviceIsiPhone
+ _MSVFastHexStringFromBytes.hexCharacters.41869
+ _MSVPropertyListDataClasses
+ _MusicLibraryLibraryCore.frameworkLibrary.22206
+ _MusicLibraryLibraryCore.frameworkLibrary.31754
+ _NSStringFromICLibraryPinAction
+ _NSStringFromICLibraryPinEntityType
+ _OBJC_CLASS_$_AVAsset
+ _OBJC_IVAR_$_ICBGTaskScheduler._taskIdentifier
+ _OBJC_IVAR_$_ICMusicSubscriptionLeaseSession._lastFairPlayKeyStatusReloadDate
+ _OBJC_IVAR_$_ICMusicSubscriptionStatus._partner
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._cloudPlaylistFolderID
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._transitionTypeProvided
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._userTransitionTypePreference
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._wallClockPlayDuration
+ _OBJC_IVAR_$_ICPlayActivityEvent._transitionTypeProvided
+ _OBJC_IVAR_$_ICPlayActivityEvent._userTransitionTypePreference
+ _OBJC_IVAR_$_ICPlayActivityEvent._wallClockPlayDuration
+ _OBJC_IVAR_$_ICPlayActivityEventContainerIDs._cloudPlaylistFolderID
+ __MSV_XXH_XXH32_update.11817
+ __MSV_XXH_XXH32_update.17673
+ __MSV_XXH_XXH32_update.17789
+ __MSV_XXH_XXH32_update.20612
+ __MSV_XXH_XXH32_update.31692
+ __MSV_XXH_XXH32_update.41859
+ __MSV_XXH_XXH32_update.496
+ __MSV_XXH_XXH64_digest.17796
+ __MSV_XXH_XXH64_digest.31697
+ __MSV_XXH_XXH64_update.11818
+ __MSV_XXH_XXH64_update.17674
+ __MSV_XXH_XXH64_update.17790
+ __MSV_XXH_XXH64_update.20613
+ __MSV_XXH_XXH64_update.31693
+ __MSV_XXH_XXH64_update.41860
+ __MSV_XXH_XXH64_update.497
+ ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.40
+ ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.41
+ ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.60
+ ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.61
+ ___105-[ICCloudClient _enableCloudLibraryWithPolicy:startinitialImport:isExplicitUserAction:completionHandler:]_block_invoke.91
+ ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.113
+ ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.114
+ ___118-[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:]_block_invoke
+ ___118-[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:]_block_invoke.69
+ ___118-[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:]_block_invoke.70
+ ___118-[ICMusicSubscriptionStatusController setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:]_block_invoke_2
+ ___30-[ICURLBagProvider _loadCache]_block_invoke.128
+ ___31-[ICURLSession _finishRequest:]_block_invoke.64
+ ___31-[ICURLSession _finishRequest:]_block_invoke_2.65
+ ___32-[ICURLSession _processRequest:]_block_invoke_2.62
+ ___34-[ICURLBagProvider _loadMonoCache]_block_invoke.133
+ ___38-[ICBGTaskScheduler _scheduleNextTask]_block_invoke.43
+ ___38-[ICBGTaskScheduler _scheduleNextTask]_block_invoke.46
+ ___39-[ICBGTaskScheduler _postExpiredEvents]_block_invoke.49
+ ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.171
+ ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.166
+ ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.176
+ ___46-[ICSecureKeyDeliveryRequestOperation execute]_block_invoke.29
+ ___47-[ICContentKeySession _scheduleKeyRefreshTimer]_block_invoke.104
+ ___49-[ICSuzeLeaseRequest performWithResponseHandler:]_block_invoke_2.28
+ ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.28
+ ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.49
+ ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.50
+ ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.106
+ ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.107
+ ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.119
+ ___54-[ICCloudClient isMediaKindDisabledForJaliscoLibrary:]_block_invoke.98
+ ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.161
+ ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.146
+ ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.147
+ ___58-[ICCloudClient removeItemsWithSagaIDs:completionHandler:]_block_invoke.38
+ ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.96
+ ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.97
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.204
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.206
+ ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.187
+ ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.188
+ ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.141
+ ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.142
+ ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.54
+ ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.55
+ ___61-[ICCloudClient importScreenshotForSagaID:completionHandler:]_block_invoke.113
+ ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.129
+ ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.130
+ ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.144
+ ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.151
+ ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.152
+ ___62-[ICCloudClient importItemArtworkForSagaID:completionHandler:]_block_invoke.112
+ ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke.36
+ ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke.37
+ ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.104
+ ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.105
+ ___63-[ICMusicSubscriptionLeaseController didMigratePlaybackSession]_block_invoke
+ ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke.34
+ ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke.35
+ ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.153
+ ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.154
+ ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.133
+ ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.134
+ ___64-[ICCloudClient sdk_addStoreItemWithOpaqueID:completionHandler:]_block_invoke.33
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.187
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.188
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.189
+ ___64-[ICMediaUserStateCenter _handleServerStateUpdatedNotification:]_block_invoke
+ ___65-[ICCloudClient disableCloudLibraryWithReason:completionHandler:]_block_invoke.92
+ ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.149
+ ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.94
+ ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.95
+ ___66-[ICStoreDialogResponseHandler handleAMSDialogRequest:completion:]_block_invoke
+ ___67-[ICCloudClient hideItemsWithPurchaseHistoryIDs:completionHandler:]_block_invoke.39
+ ___67-[ICCloudClient importContainerArtworkForSagaID:completionHandler:]_block_invoke.114
+ ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.150
+ ___69-[ICCloudClient addStoreItemsWithAdamIDs:referral:completionHandler:]_block_invoke
+ ___69-[ICCloudClient addStoreItemsWithAdamIDs:referral:completionHandler:]_block_invoke.32
+ ___69-[ICCloudClient addStoreItemsWithAdamIDs:referral:completionHandler:]_block_invoke_2
+ ___69-[ICCloudClient addStoreItemsWithAdamIDs:referral:completionHandler:]_block_invoke_3
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.114
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.115
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.116
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.83
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.87
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.117
+ ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.131
+ ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.132
+ ___72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.119
+ ___72-[ICCloudClient importScreenshotForPurchaseHistoryID:completionHandler:]_block_invoke.111
+ ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.124
+ ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.125
+ ___72-[ICCloudClient loadLastKnownEnableICMLErrorStatusWithCompletionHander:]_block_invoke.108
+ ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.77
+ ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.78
+ ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.79
+ ___73-[ICCloudClient importItemArtworkForPurchaseHistoryID:completionHandler:]_block_invoke.110
+ ___74-[ICURLBagProvider _invalidateCacheEntriesWithProfileName:profileVersion:]_block_invoke
+ ___74-[ICURLBagProvider _invalidateCacheEntriesWithProfileName:profileVersion:]_block_invoke_2
+ ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.127
+ ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.128
+ ___75-[ICCloudClient removePinnedAlbumWithPersistentID:cloudAlbumID:completion:]_block_invoke
+ ___75-[ICCloudClient removePinnedAlbumWithPersistentID:cloudAlbumID:completion:]_block_invoke.77
+ ___75-[ICCloudClient removePinnedAlbumWithPersistentID:cloudAlbumID:completion:]_block_invoke.78
+ ___75-[ICCloudClient removePinnedAlbumWithPersistentID:cloudAlbumID:completion:]_block_invoke_2
+ ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.179
+ ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.180
+ ___76-[ICCloudClient removePinnedEntityWithPersistentID:cloudID:type:completion:]_block_invoke
+ ___76-[ICCloudClient removePinnedEntityWithPersistentID:cloudID:type:completion:]_block_invoke.73
+ ___76-[ICCloudClient removePinnedEntityWithPersistentID:cloudID:type:completion:]_block_invoke.74
+ ___76-[ICCloudClient removePinnedEntityWithPersistentID:cloudID:type:completion:]_block_invoke_2
+ ___77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.120
+ ___77-[ICCloudClient removePinnedArtistWithPersistentID:cloudArtistID:completion:]_block_invoke
+ ___77-[ICCloudClient removePinnedArtistWithPersistentID:cloudArtistID:completion:]_block_invoke.75
+ ___77-[ICCloudClient removePinnedArtistWithPersistentID:cloudArtistID:completion:]_block_invoke.76
+ ___77-[ICCloudClient removePinnedArtistWithPersistentID:cloudArtistID:completion:]_block_invoke_2
+ ___79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.117
+ ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.64
+ ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.65
+ ___80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.116
+ ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.58
+ ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.59
+ ___80-[ICMusicSubscriptionLeaseSession reloadFairPlayKeyStatusWithCompletionHandler:]_block_invoke
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.181
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.182
+ ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.44
+ ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.45
+ ___82-[ICCloudClient handleAutomaticDownloadPreferenceChangedForPinnedLibraryEntities:]_block_invoke
+ ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.137
+ ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.138
+ ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.62
+ ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.63
+ ___82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.118
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.135
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.136
+ ___84-[ICACAccountVerificationOperation authenticateTask:handleDialogRequest:completion:]_block_invoke
+ ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.56
+ ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.57
+ ___84-[ICCloudClient movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:]_block_invoke
+ ___84-[ICCloudClient movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:]_block_invoke.89
+ ___84-[ICCloudClient movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:]_block_invoke.90
+ ___84-[ICCloudClient movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:]_block_invoke_2
+ ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.48
+ ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.49
+ ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.118
+ ___85-[ICCloudClient movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:]_block_invoke
+ ___85-[ICCloudClient movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:]_block_invoke.85
+ ___85-[ICCloudClient movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:]_block_invoke.86
+ ___85-[ICCloudClient movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:]_block_invoke_2
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.30
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.37
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.41
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke_2.38
+ ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.50
+ ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.51
+ ___86-[ICCloudClient importContainerArtworkForSagaID:artworkVariantType:completionHandler:]_block_invoke.115
+ ___86-[ICCloudClient movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:]_block_invoke
+ ___86-[ICCloudClient movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:]_block_invoke.87
+ ___86-[ICCloudClient movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:]_block_invoke.88
+ ___86-[ICCloudClient movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:]_block_invoke_2
+ ___87-[ICCloudClient pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke
+ ___87-[ICCloudClient pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke.71
+ ___87-[ICCloudClient pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke.72
+ ___87-[ICCloudClient pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke_2
+ ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.183
+ ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.184
+ ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.52
+ ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.53
+ ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.139
+ ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.140
+ ___88-[ICCloudClient pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke
+ ___88-[ICCloudClient pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke.67
+ ___88-[ICCloudClient pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke.68
+ ___88-[ICCloudClient pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke_2
+ ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.46
+ ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.47
+ ___89-[ICCloudClient pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke
+ ___89-[ICCloudClient pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke.69
+ ___89-[ICCloudClient pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke.70
+ ___89-[ICCloudClient pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke_2
+ ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.42
+ ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.43
+ ___93-[ICCloudServiceStatusMonitor _musicKit_importTrackWithID:addingToLibrary:completionHandler:]_block_invoke
+ ___93-[ICCloudServiceStatusMonitor _musicKit_importTrackWithID:addingToLibrary:completionHandler:]_block_invoke.206
+ ___93-[ICCloudServiceStatusMonitor _musicKit_importTrackWithID:addingToLibrary:completionHandler:]_block_invoke_2
+ ___96-[ICCloudClient updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke
+ ___96-[ICCloudClient updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke.83
+ ___96-[ICCloudClient updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke.84
+ ___96-[ICCloudClient updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:]_block_invoke_2
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.50
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.52
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.53
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.58
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.59
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.60
+ ___96-[ICURLBagProvider getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:]_block_invoke.62
+ ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.193
+ ___97-[ICCloudClient updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke
+ ___97-[ICCloudClient updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke.79
+ ___97-[ICCloudClient updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke.80
+ ___97-[ICCloudClient updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:]_block_invoke_2
+ ___97-[ICStoreDialogResponseHandler _handleBuyButtonAction:usingRequestContext:withCompletionHandler:]_block_invoke.22
+ ___98-[ICCloudClient updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke
+ ___98-[ICCloudClient updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke.81
+ ___98-[ICCloudClient updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke.82
+ ___98-[ICCloudClient updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:]_block_invoke_2
+ ___Block_byref_object_copy_.10604
+ ___Block_byref_object_copy_.10800
+ ___Block_byref_object_copy_.10928
+ ___Block_byref_object_copy_.1143
+ ___Block_byref_object_copy_.12407
+ ___Block_byref_object_copy_.13783
+ ___Block_byref_object_copy_.14331
+ ___Block_byref_object_copy_.14503
+ ___Block_byref_object_copy_.14768
+ ___Block_byref_object_copy_.15184
+ ___Block_byref_object_copy_.16332
+ ___Block_byref_object_copy_.16837
+ ___Block_byref_object_copy_.17064
+ ___Block_byref_object_copy_.17414
+ ___Block_byref_object_copy_.18887
+ ___Block_byref_object_copy_.19241
+ ___Block_byref_object_copy_.19458
+ ___Block_byref_object_copy_.20446
+ ___Block_byref_object_copy_.21372
+ ___Block_byref_object_copy_.22169
+ ___Block_byref_object_copy_.22775
+ ___Block_byref_object_copy_.22884
+ ___Block_byref_object_copy_.25363
+ ___Block_byref_object_copy_.2577
+ ___Block_byref_object_copy_.25806
+ ___Block_byref_object_copy_.26418
+ ___Block_byref_object_copy_.26779
+ ___Block_byref_object_copy_.26821
+ ___Block_byref_object_copy_.27777
+ ___Block_byref_object_copy_.28733
+ ___Block_byref_object_copy_.29756
+ ___Block_byref_object_copy_.30100
+ ___Block_byref_object_copy_.31133
+ ___Block_byref_object_copy_.32039
+ ___Block_byref_object_copy_.32427
+ ___Block_byref_object_copy_.32613
+ ___Block_byref_object_copy_.327
+ ___Block_byref_object_copy_.32774
+ ___Block_byref_object_copy_.33529
+ ___Block_byref_object_copy_.3512
+ ___Block_byref_object_copy_.35658
+ ___Block_byref_object_copy_.3579
+ ___Block_byref_object_copy_.35882
+ ___Block_byref_object_copy_.36016
+ ___Block_byref_object_copy_.36952
+ ___Block_byref_object_copy_.37114
+ ___Block_byref_object_copy_.37804
+ ___Block_byref_object_copy_.38075
+ ___Block_byref_object_copy_.38635
+ ___Block_byref_object_copy_.38816
+ ___Block_byref_object_copy_.39121
+ ___Block_byref_object_copy_.3921
+ ___Block_byref_object_copy_.39971
+ ___Block_byref_object_copy_.40542
+ ___Block_byref_object_copy_.4263
+ ___Block_byref_object_copy_.4428
+ ___Block_byref_object_copy_.4461
+ ___Block_byref_object_copy_.5354
+ ___Block_byref_object_copy_.5510
+ ___Block_byref_object_copy_.5608
+ ___Block_byref_object_copy_.6354
+ ___Block_byref_object_copy_.6789
+ ___Block_byref_object_copy_.6898
+ ___Block_byref_object_copy_.7393
+ ___Block_byref_object_copy_.9661
+ ___Block_byref_object_copy_.9766
+ ___Block_byref_object_dispose_.10605
+ ___Block_byref_object_dispose_.10801
+ ___Block_byref_object_dispose_.10929
+ ___Block_byref_object_dispose_.1144
+ ___Block_byref_object_dispose_.12408
+ ___Block_byref_object_dispose_.13784
+ ___Block_byref_object_dispose_.14332
+ ___Block_byref_object_dispose_.14504
+ ___Block_byref_object_dispose_.14769
+ ___Block_byref_object_dispose_.15185
+ ___Block_byref_object_dispose_.16333
+ ___Block_byref_object_dispose_.16838
+ ___Block_byref_object_dispose_.17065
+ ___Block_byref_object_dispose_.17415
+ ___Block_byref_object_dispose_.18888
+ ___Block_byref_object_dispose_.19242
+ ___Block_byref_object_dispose_.19459
+ ___Block_byref_object_dispose_.20447
+ ___Block_byref_object_dispose_.21373
+ ___Block_byref_object_dispose_.22170
+ ___Block_byref_object_dispose_.22776
+ ___Block_byref_object_dispose_.22885
+ ___Block_byref_object_dispose_.25364
+ ___Block_byref_object_dispose_.2578
+ ___Block_byref_object_dispose_.25807
+ ___Block_byref_object_dispose_.26419
+ ___Block_byref_object_dispose_.26780
+ ___Block_byref_object_dispose_.26822
+ ___Block_byref_object_dispose_.27778
+ ___Block_byref_object_dispose_.28734
+ ___Block_byref_object_dispose_.29757
+ ___Block_byref_object_dispose_.30101
+ ___Block_byref_object_dispose_.31134
+ ___Block_byref_object_dispose_.32040
+ ___Block_byref_object_dispose_.32428
+ ___Block_byref_object_dispose_.32614
+ ___Block_byref_object_dispose_.32775
+ ___Block_byref_object_dispose_.328
+ ___Block_byref_object_dispose_.33530
+ ___Block_byref_object_dispose_.3513
+ ___Block_byref_object_dispose_.35659
+ ___Block_byref_object_dispose_.3580
+ ___Block_byref_object_dispose_.35883
+ ___Block_byref_object_dispose_.36017
+ ___Block_byref_object_dispose_.36953
+ ___Block_byref_object_dispose_.37115
+ ___Block_byref_object_dispose_.37805
+ ___Block_byref_object_dispose_.38076
+ ___Block_byref_object_dispose_.38636
+ ___Block_byref_object_dispose_.38817
+ ___Block_byref_object_dispose_.39122
+ ___Block_byref_object_dispose_.3922
+ ___Block_byref_object_dispose_.39972
+ ___Block_byref_object_dispose_.40543
+ ___Block_byref_object_dispose_.4264
+ ___Block_byref_object_dispose_.4429
+ ___Block_byref_object_dispose_.4462
+ ___Block_byref_object_dispose_.5355
+ ___Block_byref_object_dispose_.5511
+ ___Block_byref_object_dispose_.5609
+ ___Block_byref_object_dispose_.6355
+ ___Block_byref_object_dispose_.6790
+ ___Block_byref_object_dispose_.6899
+ ___Block_byref_object_dispose_.7394
+ ___Block_byref_object_dispose_.9662
+ ___Block_byref_object_dispose_.9767
+ ___MusicLibraryLibraryCore_block_invoke.22207
+ ___MusicLibraryLibraryCore_block_invoke.31755
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"ICURLBag"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e37_v24?0"AMSDialogResult"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e52_v24?0"ICMusicSubscriptionLeaseStatus"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e30_v24?0"ICURLBag"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v24?0"ICMusicSubscriptionStatus"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"ICURLBag"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs_e68_v24?0"<ICCloudServiceStatusRemoteMonitoringService>"8"NSString"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e30_v24?0"ICURLBag"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e30_v24?0"ICURLBag"8"NSError"16ls32l8s40l8s48l8r56l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.10.26432
+ ___block_literal_global.10162
+ ___block_literal_global.109
+ ___block_literal_global.11554
+ ___block_literal_global.11971
+ ___block_literal_global.12.15221
+ ___block_literal_global.12.25153
+ ___block_literal_global.12.26430
+ ___block_literal_global.12537
+ ___block_literal_global.13.39130
+ ___block_literal_global.13180
+ ___block_literal_global.13222
+ ___block_literal_global.13817
+ ___block_literal_global.1489
+ ___block_literal_global.14954
+ ___block_literal_global.152
+ ___block_literal_global.15237
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.16760
+ ___block_literal_global.168
+ ___block_literal_global.170.29040
+ ___block_literal_global.173
+ ___block_literal_global.17468
+ ___block_literal_global.175
+ ___block_literal_global.17916
+ ___block_literal_global.18.26428
+ ___block_literal_global.18.35716
+ ___block_literal_global.18313
+ ___block_literal_global.186
+ ___block_literal_global.18710
+ ___block_literal_global.18939
+ ___block_literal_global.19146
+ ___block_literal_global.20.26426
+ ___block_literal_global.202.25353
+ ___block_literal_global.20335
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.22.26423
+ ___block_literal_global.22006
+ ___block_literal_global.22229
+ ___block_literal_global.22679
+ ___block_literal_global.22788
+ ___block_literal_global.230
+ ___block_literal_global.2319
+ ___block_literal_global.2410
+ ___block_literal_global.24302
+ ___block_literal_global.24426
+ ___block_literal_global.25152
+ ___block_literal_global.25349
+ ___block_literal_global.25912
+ ___block_literal_global.26081
+ ___block_literal_global.26294
+ ___block_literal_global.26438
+ ___block_literal_global.2690
+ ___block_literal_global.27812
+ ___block_literal_global.28320
+ ___block_literal_global.2891
+ ___block_literal_global.29136
+ ___block_literal_global.29475
+ ___block_literal_global.29771
+ ___block_literal_global.29921
+ ___block_literal_global.3.17923
+ ___block_literal_global.30917
+ ___block_literal_global.31459
+ ___block_literal_global.31518
+ ___block_literal_global.3187
+ ___block_literal_global.31926
+ ___block_literal_global.32506
+ ___block_literal_global.326
+ ___block_literal_global.33125
+ ___block_literal_global.33566
+ ___block_literal_global.34789
+ ___block_literal_global.35297
+ ___block_literal_global.35739
+ ___block_literal_global.36894
+ ___block_literal_global.3735
+ ___block_literal_global.37816
+ ___block_literal_global.38178
+ ___block_literal_global.38276
+ ___block_literal_global.38960
+ ___block_literal_global.39140
+ ___block_literal_global.3940
+ ___block_literal_global.40071
+ ___block_literal_global.40212
+ ___block_literal_global.40359
+ ___block_literal_global.40547
+ ___block_literal_global.41107
+ ___block_literal_global.41355
+ ___block_literal_global.41694
+ ___block_literal_global.4238
+ ___block_literal_global.4479
+ ___block_literal_global.4542
+ ___block_literal_global.4663
+ ___block_literal_global.53.13772
+ ___block_literal_global.56
+ ___block_literal_global.5771
+ ___block_literal_global.581
+ ___block_literal_global.6.26436
+ ___block_literal_global.6235
+ ___block_literal_global.66.22655
+ ___block_literal_global.68.31416
+ ___block_literal_global.6967
+ ___block_literal_global.7063
+ ___block_literal_global.7280
+ ___block_literal_global.7440
+ ___block_literal_global.7674
+ ___block_literal_global.8.2401
+ ___block_literal_global.8.26434
+ ___block_literal_global.804
+ ___block_literal_global.82.31583
+ ___block_literal_global.8389
+ ___block_literal_global.8460
+ ___block_literal_global.9368
+ ___getML3MusicLibraryClass_block_invoke.22205
+ _audit_stringMusicLibrary.22222
+ _audit_stringMusicLibrary.31758
+ _execute.sLastReauthenticationAttemptPerDSID
+ _getML3MusicLibraryClass.22203
+ _getML3MusicLibraryClass.softClass.22204
+ _msv_dispatch_async_on_queue_with_qos
+ _objc_msgSend$_didMigratePlaybackSession
+ _objc_msgSend$_invalidateCacheEntriesWithProfileName:profileVersion:
+ _objc_msgSend$_musicKit_importTrackWithID:addingToLibrary:completionHandler:
+ _objc_msgSend$_setError
+ _objc_msgSend$addStoreItemsWithAdamIDs:referral:configuration:completion:
+ _objc_msgSend$cloudPlaylistFolderID
+ _objc_msgSend$contentKeySession:didStartProcessingKey:isPrefetchKey:isPersistable:isRenew:
+ _objc_msgSend$getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$handleAMSDialogRequest:completion:
+ _objc_msgSend$hasError
+ _objc_msgSend$loggingIdentifier
+ _objc_msgSend$movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:configuration:completion:
+ _objc_msgSend$movePinnedArtistWithPersistentID:cloudArtistID:toPosition:configuration:completion:
+ _objc_msgSend$movePinnedEntityWithPersistentID:cloudID:type:toPosition:configuration:completion:
+ _objc_msgSend$options
+ _objc_msgSend$originatingRecipient
+ _objc_msgSend$pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:configuration:completion:
+ _objc_msgSend$pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:configuration:completion:
+ _objc_msgSend$pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:configuration:completion:
+ _objc_msgSend$position
+ _objc_msgSend$prepareToDownloadAllLibraryPinnedEntitiesForConfiguration:
+ _objc_msgSend$removePinnedAlbumWithPersistentID:cloudAlbumID:configuration:completion:
+ _objc_msgSend$removePinnedArtistWithPersistentID:cloudArtistID:configuration:completion:
+ _objc_msgSend$removePinnedEntityWithPersistentID:cloudID:type:configuration:completion:
+ _objc_msgSend$setCloudPlaylistFolderID:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:
+ _objc_msgSend$shouldAllowUntrustedHosts
+ _objc_msgSend$transitionTypeProvided
+ _objc_msgSend$updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:configuration:completion:
+ _objc_msgSend$updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:configuration:completion:
+ _objc_msgSend$updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:configuration:completion:
+ _objc_msgSend$userTransitionTypePreference
+ _objc_msgSend$wallClockPlayDuration
+ _objc_retain_x11
+ _sharedCache.sOnceToken.29920
+ _sharedCache.sSharedCache.29922
+ _sharedController.sOnceToken.35738
+ _sharedController.sOnceToken.39139
+ _sharedController.sSharedController.35740
+ _sharedController.sSharedController.39141
+ _sharedManager.sOnceToken.19145
+ _sharedManager.sOnceToken.28319
+ _sharedManager.sOnceToken.2890
+ _sharedManager.sSharedManager.19147
+ _sharedManager.sSharedManager.28321
+ _sharedManager.sSharedManager.2892
+ _sharedMonitor.sOnceToken.18312
+ _sharedMonitor.sOnceToken.40070
+ _sharedMonitor.sSharedMonitor.18314
+ _sharedMonitor.sSharedMonitor.40072
+ _sharedProvider.sOnceToken.40358
+ _sharedProvider.sSharedProvider.40360
- GCC_except_table1038
- GCC_except_table1064
- GCC_except_table1198
- GCC_except_table1274
- GCC_except_table1442
- GCC_except_table1455
- GCC_except_table1643
- GCC_except_table1826
- GCC_except_table1855
- GCC_except_table1870
- GCC_except_table1906
- GCC_except_table2019
- GCC_except_table2034
- GCC_except_table2083
- GCC_except_table2085
- GCC_except_table2091
- GCC_except_table2098
- GCC_except_table2126
- GCC_except_table2140
- GCC_except_table2145
- GCC_except_table2147
- GCC_except_table2152
- GCC_except_table2155
- GCC_except_table2168
- GCC_except_table2245
- GCC_except_table2254
- GCC_except_table2257
- GCC_except_table2260
- GCC_except_table2263
- GCC_except_table2265
- GCC_except_table2267
- GCC_except_table2269
- GCC_except_table2276
- GCC_except_table2278
- GCC_except_table2295
- GCC_except_table2334
- GCC_except_table2365
- GCC_except_table2367
- GCC_except_table2369
- GCC_except_table2371
- GCC_except_table2721
- GCC_except_table2766
- GCC_except_table2911
- GCC_except_table2928
- GCC_except_table2938
- GCC_except_table2961
- GCC_except_table2971
- GCC_except_table3069
- GCC_except_table3337
- GCC_except_table3341
- GCC_except_table3344
- GCC_except_table3359
- GCC_except_table3370
- GCC_except_table3389
- GCC_except_table3429
- GCC_except_table3443
- GCC_except_table3556
- GCC_except_table3714
- GCC_except_table3875
- GCC_except_table3917
- GCC_except_table4015
- GCC_except_table4023
- GCC_except_table4025
- GCC_except_table4027
- GCC_except_table4029
- GCC_except_table403
- GCC_except_table4031
- GCC_except_table4035
- GCC_except_table4042
- GCC_except_table4046
- GCC_except_table4061
- GCC_except_table4064
- GCC_except_table408
- GCC_except_table4243
- GCC_except_table4295
- GCC_except_table4299
- GCC_except_table4302
- GCC_except_table4307
- GCC_except_table4413
- GCC_except_table4417
- GCC_except_table4419
- GCC_except_table4486
- GCC_except_table4561
- GCC_except_table4647
- GCC_except_table4729
- GCC_except_table4797
- GCC_except_table4878
- GCC_except_table5039
- GCC_except_table5281
- GCC_except_table5377
- GCC_except_table5425
- GCC_except_table5449
- GCC_except_table5490
- GCC_except_table5491
- GCC_except_table5564
- GCC_except_table5582
- GCC_except_table5860
- GCC_except_table5867
- GCC_except_table5875
- GCC_except_table5886
- GCC_except_table5888
- GCC_except_table5889
- GCC_except_table5890
- GCC_except_table5891
- GCC_except_table5896
- GCC_except_table5901
- GCC_except_table5906
- GCC_except_table5917
- GCC_except_table5932
- GCC_except_table5934
- GCC_except_table5940
- GCC_except_table5949
- GCC_except_table5991
- GCC_except_table6019
- GCC_except_table6029
- GCC_except_table6036
- GCC_except_table6037
- GCC_except_table6097
- GCC_except_table6100
- GCC_except_table6135
- GCC_except_table6140
- GCC_except_table6146
- GCC_except_table6149
- GCC_except_table6152
- GCC_except_table6155
- GCC_except_table6158
- GCC_except_table6161
- GCC_except_table6164
- GCC_except_table6167
- GCC_except_table6170
- GCC_except_table6173
- GCC_except_table6176
- GCC_except_table6277
- GCC_except_table6290
- GCC_except_table6490
- GCC_except_table6497
- GCC_except_table6669
- GCC_except_table6673
- GCC_except_table6675
- GCC_except_table6698
- GCC_except_table6744
- GCC_except_table675
- GCC_except_table687
- GCC_except_table6926
- GCC_except_table7059
- GCC_except_table7200
- GCC_except_table7213
- GCC_except_table7236
- GCC_except_table7247
- GCC_except_table729
- GCC_except_table7292
- GCC_except_table7293
- GCC_except_table7294
- GCC_except_table7295
- GCC_except_table7296
- GCC_except_table7337
- GCC_except_table7355
- GCC_except_table7407
- GCC_except_table7410
- GCC_except_table7419
- GCC_except_table7426
- GCC_except_table7467
- GCC_except_table7486
- GCC_except_table7519
- GCC_except_table7577
- GCC_except_table7578
- GCC_except_table8008
- GCC_except_table8014
- GCC_except_table8036
- GCC_except_table8040
- GCC_except_table8051
- GCC_except_table8056
- GCC_except_table8091
- GCC_except_table8094
- GCC_except_table8161
- GCC_except_table8206
- GCC_except_table8255
- GCC_except_table8283
- GCC_except_table8288
- GCC_except_table8290
- GCC_except_table8292
- GCC_except_table8324
- GCC_except_table841
- GCC_except_table8467
- GCC_except_table8475
- GCC_except_table8480
- GCC_except_table8495
- GCC_except_table850
- GCC_except_table8503
- GCC_except_table8547
- GCC_except_table8680
- GCC_except_table8684
- GCC_except_table8686
- GCC_except_table8723
- GCC_except_table8726
- GCC_except_table8733
- GCC_except_table8736
- GCC_except_table8945
- GCC_except_table8949
- GCC_except_table8989
- GCC_except_table9086
- GCC_except_table9091
- GCC_except_table942
- GCC_except_table950
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _MSVFastHexStringFromBytes.hexCharacters.41862
- _MusicLibraryLibraryCore.frameworkLibrary.22264
- _MusicLibraryLibraryCore.frameworkLibrary.31730
- __MSV_XXH_XXH32_update.11794
- __MSV_XXH_XXH32_update.17655
- __MSV_XXH_XXH32_update.17793
- __MSV_XXH_XXH32_update.20644
- __MSV_XXH_XXH32_update.31665
- __MSV_XXH_XXH32_update.41851
- __MSV_XXH_XXH32_update.498
- __MSV_XXH_XXH64_digest.17798
- __MSV_XXH_XXH64_digest.31670
- __MSV_XXH_XXH64_update.11795
- __MSV_XXH_XXH64_update.17656
- __MSV_XXH_XXH64_update.17794
- __MSV_XXH_XXH64_update.20645
- __MSV_XXH_XXH64_update.31666
- __MSV_XXH_XXH64_update.41852
- __MSV_XXH_XXH64_update.499
- ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.37
- ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.38
- ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.57
- ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.58
- ___105-[ICCloudClient _enableCloudLibraryWithPolicy:startinitialImport:isExplicitUserAction:completionHandler:]_block_invoke.64
- ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.109
- ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.112
- ___30-[ICURLBagProvider _loadCache]_block_invoke.130
- ___31-[ICURLSession _finishRequest:]_block_invoke.63
- ___31-[ICURLSession _finishRequest:]_block_invoke_2.64
- ___34-[ICURLBagProvider _loadMonoCache]_block_invoke.135
- ___35-[ICURLBagProvider invalidateCache]_block_invoke
- ___35-[ICURLBagProvider invalidateCache]_block_invoke.63
- ___38-[ICBGTaskScheduler _scheduleNextTask]_block_invoke.39
- ___38-[ICBGTaskScheduler _scheduleNextTask]_block_invoke.42
- ___39-[ICBGTaskScheduler _postExpiredEvents]_block_invoke.45
- ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.144
- ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.139
- ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.149
- ___46-[ICSecureKeyDeliveryRequestOperation execute]_block_invoke.28
- ___47-[ICContentKeySession _scheduleKeyRefreshTimer]_block_invoke.102
- ___49-[ICSuzeLeaseRequest performWithResponseHandler:]_block_invoke_2.29
- ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.29
- ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke.50
- ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.51
- ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.79
- ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.80
- ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.122
- ___54-[ICCloudClient isMediaKindDisabledForJaliscoLibrary:]_block_invoke.71
- ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.134
- ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.119
- ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.120
- ___58-[ICCloudClient removeItemsWithSagaIDs:completionHandler:]_block_invoke.35
- ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.69
- ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.70
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.203
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.205
- ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.160
- ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.161
- ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.114
- ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.115
- ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.51
- ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.52
- ___61-[ICCloudClient importScreenshotForSagaID:completionHandler:]_block_invoke.86
- ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.102
- ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.103
- ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.117
- ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.124
- ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.125
- ___62-[ICCloudClient importItemArtworkForSagaID:completionHandler:]_block_invoke.85
- ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke.34
- ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke_3
- ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.77
- ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.78
- ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke.33
- ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke_3
- ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.126
- ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.127
- ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.106
- ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.107
- ___64-[ICCloudClient sdk_addStoreItemWithOpaqueID:completionHandler:]_block_invoke.32
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.166
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.167
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.168
- ___65-[ICCloudClient disableCloudLibraryWithReason:completionHandler:]_block_invoke.65
- ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.122
- ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.67
- ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.68
- ___67-[ICCloudClient hideItemsWithPurchaseHistoryIDs:completionHandler:]_block_invoke.36
- ___67-[ICCloudClient importContainerArtworkForSagaID:completionHandler:]_block_invoke.87
- ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.123
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.117
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.118
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.119
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.86
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.90
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.120
- ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.104
- ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.105
- ___72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.92
- ___72-[ICCloudClient importScreenshotForPurchaseHistoryID:completionHandler:]_block_invoke.84
- ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.97
- ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.98
- ___72-[ICCloudClient loadLastKnownEnableICMLErrorStatusWithCompletionHander:]_block_invoke.81
- ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.73
- ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.74
- ___72-[ICMusicSubscriptionStatusController _remoteRequestingClientConnection]_block_invoke.75
- ___73-[ICCloudClient importItemArtworkForPurchaseHistoryID:completionHandler:]_block_invoke.83
- ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.100
- ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.101
- ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.152
- ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.153
- ___77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.93
- ___79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.90
- ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.61
- ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.62
- ___79-[ICURLBagProvider getBagForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke
- ___80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.89
- ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.55
- ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.56
- ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.154
- ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.155
- ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.41
- ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.42
- ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.110
- ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.111
- ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.59
- ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.60
- ___82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.117
- ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.108
- ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.109
- ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.53
- ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.54
- ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.45
- ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.46
- ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.91
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.29
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.36
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.40
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke_2.37
- ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.47
- ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.48
- ___86-[ICCloudClient importContainerArtworkForSagaID:artworkVariantType:completionHandler:]_block_invoke.88
- ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.156
- ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.157
- ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.49
- ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.50
- ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.112
- ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.113
- ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.43
- ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.44
- ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.39
- ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.40
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.49
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.51
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.52
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.57
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.58
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.59
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.61
- ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.166
- ___97-[ICStoreDialogResponseHandler _handleBuyButtonAction:usingRequestContext:withCompletionHandler:]_block_invoke.20
- ___Block_byref_object_copy_.10583
- ___Block_byref_object_copy_.10779
- ___Block_byref_object_copy_.10907
- ___Block_byref_object_copy_.1106
- ___Block_byref_object_copy_.12409
- ___Block_byref_object_copy_.13769
- ___Block_byref_object_copy_.14318
- ___Block_byref_object_copy_.14493
- ___Block_byref_object_copy_.14758
- ___Block_byref_object_copy_.15178
- ___Block_byref_object_copy_.16323
- ___Block_byref_object_copy_.16827
- ___Block_byref_object_copy_.17053
- ___Block_byref_object_copy_.17401
- ___Block_byref_object_copy_.18899
- ___Block_byref_object_copy_.19264
- ___Block_byref_object_copy_.19480
- ___Block_byref_object_copy_.20473
- ___Block_byref_object_copy_.21420
- ___Block_byref_object_copy_.22227
- ___Block_byref_object_copy_.22832
- ___Block_byref_object_copy_.22940
- ___Block_byref_object_copy_.25359
- ___Block_byref_object_copy_.2556
- ___Block_byref_object_copy_.25802
- ___Block_byref_object_copy_.26408
- ___Block_byref_object_copy_.26767
- ___Block_byref_object_copy_.26809
- ___Block_byref_object_copy_.27745
- ___Block_byref_object_copy_.28701
- ___Block_byref_object_copy_.29724
- ___Block_byref_object_copy_.30067
- ___Block_byref_object_copy_.31102
- ___Block_byref_object_copy_.32015
- ___Block_byref_object_copy_.32400
- ___Block_byref_object_copy_.32582
- ___Block_byref_object_copy_.32743
- ___Block_byref_object_copy_.328
- ___Block_byref_object_copy_.33496
- ___Block_byref_object_copy_.3488
- ___Block_byref_object_copy_.3555
- ___Block_byref_object_copy_.35632
- ___Block_byref_object_copy_.35857
- ___Block_byref_object_copy_.35991
- ___Block_byref_object_copy_.36920
- ___Block_byref_object_copy_.37083
- ___Block_byref_object_copy_.37772
- ___Block_byref_object_copy_.38043
- ___Block_byref_object_copy_.38626
- ___Block_byref_object_copy_.38807
- ___Block_byref_object_copy_.3896
- ___Block_byref_object_copy_.39112
- ___Block_byref_object_copy_.39956
- ___Block_byref_object_copy_.40536
- ___Block_byref_object_copy_.4251
- ___Block_byref_object_copy_.4400
- ___Block_byref_object_copy_.4433
- ___Block_byref_object_copy_.5327
- ___Block_byref_object_copy_.5485
- ___Block_byref_object_copy_.5581
- ___Block_byref_object_copy_.6312
- ___Block_byref_object_copy_.6745
- ___Block_byref_object_copy_.6853
- ___Block_byref_object_copy_.7352
- ___Block_byref_object_copy_.9635
- ___Block_byref_object_copy_.9740
- ___Block_byref_object_dispose_.10584
- ___Block_byref_object_dispose_.10780
- ___Block_byref_object_dispose_.10908
- ___Block_byref_object_dispose_.1107
- ___Block_byref_object_dispose_.12410
- ___Block_byref_object_dispose_.13770
- ___Block_byref_object_dispose_.14319
- ___Block_byref_object_dispose_.14494
- ___Block_byref_object_dispose_.14759
- ___Block_byref_object_dispose_.15179
- ___Block_byref_object_dispose_.16324
- ___Block_byref_object_dispose_.16828
- ___Block_byref_object_dispose_.17054
- ___Block_byref_object_dispose_.17402
- ___Block_byref_object_dispose_.18900
- ___Block_byref_object_dispose_.19265
- ___Block_byref_object_dispose_.19481
- ___Block_byref_object_dispose_.20474
- ___Block_byref_object_dispose_.21421
- ___Block_byref_object_dispose_.22228
- ___Block_byref_object_dispose_.22833
- ___Block_byref_object_dispose_.22941
- ___Block_byref_object_dispose_.25360
- ___Block_byref_object_dispose_.2557
- ___Block_byref_object_dispose_.25803
- ___Block_byref_object_dispose_.26409
- ___Block_byref_object_dispose_.26768
- ___Block_byref_object_dispose_.26810
- ___Block_byref_object_dispose_.27746
- ___Block_byref_object_dispose_.28702
- ___Block_byref_object_dispose_.29725
- ___Block_byref_object_dispose_.30068
- ___Block_byref_object_dispose_.31103
- ___Block_byref_object_dispose_.32016
- ___Block_byref_object_dispose_.32401
- ___Block_byref_object_dispose_.32583
- ___Block_byref_object_dispose_.32744
- ___Block_byref_object_dispose_.329
- ___Block_byref_object_dispose_.33497
- ___Block_byref_object_dispose_.3489
- ___Block_byref_object_dispose_.3556
- ___Block_byref_object_dispose_.35633
- ___Block_byref_object_dispose_.35858
- ___Block_byref_object_dispose_.35992
- ___Block_byref_object_dispose_.36921
- ___Block_byref_object_dispose_.37084
- ___Block_byref_object_dispose_.37773
- ___Block_byref_object_dispose_.38044
- ___Block_byref_object_dispose_.38627
- ___Block_byref_object_dispose_.38808
- ___Block_byref_object_dispose_.3897
- ___Block_byref_object_dispose_.39113
- ___Block_byref_object_dispose_.39957
- ___Block_byref_object_dispose_.40537
- ___Block_byref_object_dispose_.4252
- ___Block_byref_object_dispose_.4401
- ___Block_byref_object_dispose_.4434
- ___Block_byref_object_dispose_.5328
- ___Block_byref_object_dispose_.5486
- ___Block_byref_object_dispose_.5582
- ___Block_byref_object_dispose_.6313
- ___Block_byref_object_dispose_.6746
- ___Block_byref_object_dispose_.6854
- ___Block_byref_object_dispose_.7353
- ___Block_byref_object_dispose_.9636
- ___Block_byref_object_dispose_.9741
- ___MusicLibraryLibraryCore_block_invoke.22265
- ___MusicLibraryLibraryCore_block_invoke.31731
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s104l8s96l8
- ___block_descriptor_32_e25_v32?0"ICURLBag"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24ls32l8
- ___block_descriptor_48_e8_32s40s_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24ls32l8s40l8s48l8r56l8
- ___block_literal_global.10.26420
- ___block_literal_global.10142
- ___block_literal_global.107
- ___block_literal_global.11527
- ___block_literal_global.11965
- ___block_literal_global.12.15215
- ___block_literal_global.12.25146
- ___block_literal_global.12.26418
- ___block_literal_global.12536
- ___block_literal_global.13.39121
- ___block_literal_global.131
- ___block_literal_global.13176
- ___block_literal_global.13218
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.138
- ___block_literal_global.13802
- ___block_literal_global.141
- ___block_literal_global.143
- ___block_literal_global.1450
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.14947
- ___block_literal_global.151
- ___block_literal_global.15231
- ___block_literal_global.154
- ___block_literal_global.159
- ___block_literal_global.16750
- ___block_literal_global.170.29004
- ___block_literal_global.172
- ___block_literal_global.174
- ___block_literal_global.17450
- ___block_literal_global.176
- ___block_literal_global.17917
- ___block_literal_global.18.26416
- ___block_literal_global.18.35690
- ___block_literal_global.18325
- ___block_literal_global.18722
- ___block_literal_global.18951
- ___block_literal_global.19.26301
- ___block_literal_global.19168
- ___block_literal_global.20355
- ___block_literal_global.22.26413
- ___block_literal_global.22064
- ___block_literal_global.22287
- ___block_literal_global.227
- ___block_literal_global.22736
- ___block_literal_global.22845
- ___block_literal_global.2297
- ___block_literal_global.2388
- ___block_literal_global.24298
- ___block_literal_global.24422
- ___block_literal_global.25145
- ___block_literal_global.25345
- ___block_literal_global.25909
- ___block_literal_global.26078
- ___block_literal_global.26284
- ___block_literal_global.26426
- ___block_literal_global.2671
- ___block_literal_global.27780
- ___block_literal_global.28287
- ___block_literal_global.2863
- ___block_literal_global.29102
- ___block_literal_global.29442
- ___block_literal_global.29739
- ___block_literal_global.29888
- ___block_literal_global.3.17924
- ___block_literal_global.30875
- ___block_literal_global.31427
- ___block_literal_global.31487
- ___block_literal_global.3163
- ___block_literal_global.31902
- ___block_literal_global.32475
- ___block_literal_global.327
- ___block_literal_global.33090
- ___block_literal_global.33533
- ___block_literal_global.34754
- ___block_literal_global.35273
- ___block_literal_global.35713
- ___block_literal_global.36862
- ___block_literal_global.3712
- ___block_literal_global.37784
- ___block_literal_global.38158
- ___block_literal_global.38256
- ___block_literal_global.38951
- ___block_literal_global.39131
- ___block_literal_global.3915
- ___block_literal_global.40056
- ___block_literal_global.40195
- ___block_literal_global.40342
- ___block_literal_global.40541
- ___block_literal_global.41109
- ___block_literal_global.41332
- ___block_literal_global.41681
- ___block_literal_global.4184
- ___block_literal_global.4451
- ___block_literal_global.4514
- ___block_literal_global.4635
- ___block_literal_global.53.13758
- ___block_literal_global.55.38156
- ___block_literal_global.5729
- ___block_literal_global.575
- ___block_literal_global.6.26424
- ___block_literal_global.6193
- ___block_literal_global.66.22713
- ___block_literal_global.66.5693
- ___block_literal_global.68.31383
- ___block_literal_global.6925
- ___block_literal_global.7021
- ___block_literal_global.7238
- ___block_literal_global.7401
- ___block_literal_global.7634
- ___block_literal_global.777
- ___block_literal_global.8.2379
- ___block_literal_global.8.26422
- ___block_literal_global.82.31552
- ___block_literal_global.8350
- ___block_literal_global.8421
- ___block_literal_global.9342
- ___getML3MusicLibraryClass_block_invoke.22263
- _audit_stringMusicLibrary.22280
- _audit_stringMusicLibrary.31734
- _execute.sLastSilentReauthenticationAttemptPerDSID
- _getML3MusicLibraryClass.22261
- _getML3MusicLibraryClass.softClass.22262
- _objc_msgSend$getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:
- _sharedCache.sOnceToken.29887
- _sharedCache.sSharedCache.29889
- _sharedController.sOnceToken.35712
- _sharedController.sOnceToken.39130
- _sharedController.sSharedController.35714
- _sharedController.sSharedController.39132
- _sharedManager.sOnceToken.19167
- _sharedManager.sOnceToken.28286
- _sharedManager.sOnceToken.2862
- _sharedManager.sSharedManager.19169
- _sharedManager.sSharedManager.28288
- _sharedManager.sSharedManager.2864
- _sharedMonitor.sOnceToken.18324
- _sharedMonitor.sOnceToken.40055
- _sharedMonitor.sSharedMonitor.18326
- _sharedMonitor.sSharedMonitor.40057
- _sharedProvider.sOnceToken.40341
- _sharedProvider.sSharedProvider.40343
CStrings:
+ "    transitionTypeProvided:%lu\n"
+ "    userTransitionTypePreference:%lu\n"
+ "    wallClockPlayDuration:%f\n"
+ " cloudFolderPlaylistID: %llu"
+ "%{public}@ Adjusted authentication type from %{public}@ --> %{public}@"
+ "%{public}@ Adjusting authentication policy based on allowed types: [%{public}@]"
+ "%{public}@ Completed request to move pinned artist"
+ "%{public}@ Completed request to move pinned artist error=%{public}@"
+ "%{public}@ Completed request to move pinned library entity"
+ "%{public}@ Completed request to move pinned library entity error=%{public}@"
+ "%{public}@ Completed request to pin library album"
+ "%{public}@ Completed request to pin library album error=%{public}@"
+ "%{public}@ Completed request to pin library artist"
+ "%{public}@ Completed request to pin library artist error=%{public}@"
+ "%{public}@ Completed request to pin library entity"
+ "%{public}@ Completed request to pin library entity error=%{public}@"
+ "%{public}@ Completed request to remove pinned library album"
+ "%{public}@ Completed request to remove pinned library album error=%{public}@"
+ "%{public}@ Completed request to remove pinned library artist"
+ "%{public}@ Completed request to remove pinned library artist error=%{public}@"
+ "%{public}@ Completed request to remove pinned library entity"
+ "%{public}@ Completed request to remove pinned library entity error=%{public}@"
+ "%{public}@ Completed request to set subscription status for user '%{public}@'"
+ "%{public}@ Completed request to set subscription status for user '%{public}@' error=%{public}@"
+ "%{public}@ Completed request to update pinned library album"
+ "%{public}@ Completed request to update pinned library album error=%{public}@"
+ "%{public}@ Completed request to update pinned library artist"
+ "%{public}@ Completed request to update pinned library artist error=%{public}@"
+ "%{public}@ Completed request to update pinned library entity"
+ "%{public}@ Completed request to update pinned library entity error=%{public}@"
+ "%{public}@ Disallowing authentication because there are no allowed types for this response"
+ "%{public}@ Failed to cancel old task. err=%{public}@"
+ "%{public}@ Failed to obtain remote proxy to perform subscription status update. error = %{public}@."
+ "%{public}@ Handling AMS dialog request %{public}@"
+ "%{public}@ Handling state update notification: %{public}@"
+ "%{public}@ Ignoring dialog as a handler is not configured"
+ "%{public}@ Invalidating cached bag for key '%{public}@'"
+ "%{public}@ Invalidating cached bags with profile %{public}@/%{public}@"
+ "%{public}@ No change in user state data so not relaying change notification"
+ "%{public}@ Received AMSBag change notification for profile %{public}@/%{public}@ and account '%{public}@"
+ "%{public}@ Received AMSBag invalidation notification with userInfo %{public}@"
+ "%{public}@ Received download token '%llu' for download task %{public}@"
+ "%{public}@ Received token response %@"
+ "%{public}@ Sending request to update subscription status for identity %{public}@ with payload: %{public}@"
+ "%{public}@ Skipping authentication attempt due to throttling. last attempt was at %{public}@ (%.2fs ago)"
+ "%{public}@ Updating automatic download preference change for library pins. shouldAutomaticallyDownload=%{BOOL}u, currentAutomaticDownloadPrefs=%{BOOL}u"
+ "%{public}@ received request to handle dialog request %{public}@"
+ "%{public}@: _musicKit_importTrackWithID failed to connect to cloud service status monitor with error: %{public}@."
+ "%{public}@: _musicKit_importTrackWithID with storeID=%lld"
+ "%{public}@: _musicKit_importTrackWithID with storeID=%lld error=%{public}@"
+ ".%@"
+ "<%@ %p statusType:%@, matchEnabled=%@, carrierBundlingStatusType:%@, reasonType:%@, sourceType:%@%@, capabilities:%@, eligibleOffers:[%@], isAutoRenewEnabled:%@, isInFreePeriod:%@, isInFreeTrial:%@, isEligibleForFreeTrial:%@, initialPurchaseTimestamp:%@, serviceBeginsTimestamp:%@, studentExpirationDate:%@, studentVerifier:%@, studentVerificationId:%@, partner:%@>"
+ "Add store items to library failed with error: %{public}@"
+ "Add store playlist with globalID=%{public}@ to library failed with error: %{public}@, completionHandler=%p"
+ "AutomaticDownloadEnabledForLibraryPins"
+ "Dialog handling not desired in this context"
+ "DrillIn"
+ "Error setting automatic download preference for library pins"
+ "Failed to create verification context for identity %{public}@. err=%{public}@"
+ "ICDefaultsKeyAllowUntrustedHosts"
+ "ICPlayActivityEventContainerIDsCloudFolderPlaylistID"
+ "ImagePreconnectUrl"
+ "LibraryPinAlreadyPinned"
+ "LibraryPinCloudLibraryNotEnabled"
+ "LibraryPinIdentityPropertiesLoadFailed"
+ "LibraryPinInvalidRequestIdentifiers"
+ "LibraryPinLocalUpdateError"
+ "LibraryPinNotPinned"
+ "LibraryPinReachedMaxPinLimit"
+ "Must provide a valid status when creating user state object"
+ "Removing playlists with sagaIDs=%{public}@ to library failed with error: %{public}@, completionHandler=%p"
+ "SKD key:%@ persistent:%d recipient:%@"
+ "Shuffle"
+ "T@\"NSDate\",R,C,N,V_lastFairPlayKeyStatusReloadDate"
+ "T@\"NSString\",R,C,N,V_partner"
+ "TQ,R,N,V_cloudPlaylistFolderID"
+ "Td,N,V_wallClockPlayDuration"
+ "Tq,N,V_transitionTypeProvided"
+ "Tq,N,V_userTransitionTypePreference"
+ "Tq,N,V_vocalAttenuationAvailability"
+ "Tq,R,N,V_audioQualityPreference"
+ "Tq,R,N,V_autoPlayMode"
+ "Tq,R,N,V_containerType"
+ "Tq,R,N,V_displayType"
+ "Tq,R,N,V_endReasonType"
+ "Tq,R,N,V_eventType"
+ "Tq,R,N,V_itemType"
+ "Tq,R,N,V_playbackFormatPreference"
+ "Tq,R,N,V_reasonHintType"
+ "Tq,R,N,V_repeatPlayMode"
+ "Tq,R,N,V_shufflePlayMode"
+ "URLSession:assetDownloadTask:didReceiveMetricEvent:"
+ "[Lease] - [%{public}@] - _didMigratePlaybackSession - leaseStatus: %{public}@"
+ "_cloudPlaylistFolderID"
+ "_didMigratePlaybackSession"
+ "_handleAMSBagInvalidatedNotification:"
+ "_invalidateCacheEntriesWithProfileName:profileVersion:"
+ "_lastFairPlayKeyStatusReloadDate"
+ "_musicKit_importTrackWithID:addingToLibrary:completionHandler:"
+ "_partner"
+ "_setError"
+ "_transitionTypeProvided"
+ "_userTransitionTypePreference"
+ "_wallClockPlayDuration"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "accessoryDidSetHasOnboardedForAdaptiveTemperatureAutomations:"
+ "accessoryDidSetHasOnboardedForCleanEnergyAutomation:"
+ "addStoreItemsWithAdamIDs:referral:completionHandler:"
+ "addStoreItemsWithAdamIDs:referral:configuration:completion:"
+ "cloudPlaylistFolderID"
+ "contentKeySession:didStartProcessingKey:isPrefetchKey:isPersistable:isRenew:"
+ "didMigratePlaybackSession"
+ "getBagForRequestContext:qualityOfService:forceRefetch:withCompletionHandler:"
+ "getBytes:range:"
+ "handleAMSDialogRequest:completion:"
+ "handleAutomaticDownloadPreferenceChangedForPinnedLibraryEntities:"
+ "hasError"
+ "import track"
+ "isAutomaticDownloadsEnabledForPinnedLibraryEntities"
+ "lastFairPlayKeyStatusReloadDate"
+ "loggingIdentifier"
+ "loud"
+ "movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:completion:"
+ "movePinnedAlbumWithPersistentID:cloudAlbumID:toPosition:configuration:completion:"
+ "movePinnedArtistWithPersistentID:cloudArtistID:toPosition:completion:"
+ "movePinnedArtistWithPersistentID:cloudArtistID:toPosition:configuration:completion:"
+ "movePinnedEntityWithPersistentID:cloudID:type:toPosition:completion:"
+ "movePinnedEntityWithPersistentID:cloudID:type:toPosition:configuration:completion:"
+ "originatingRecipient"
+ "partner"
+ "pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:"
+ "pinLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:configuration:completion:"
+ "pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:"
+ "pinLibraryArtistWithPersistentID:cloudArtistID:defaultAction:configuration:completion:"
+ "pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:"
+ "pinLibraryEntityWithPersistentID:cloudID:type:defaultAction:configuration:completion:"
+ "prepareToDownloadAllLibraryPinnedEntitiesForConfiguration:"
+ "removePinnedAlbumWithPersistentID:cloudAlbumID:completion:"
+ "removePinnedAlbumWithPersistentID:cloudAlbumID:configuration:completion:"
+ "removePinnedArtistWithPersistentID:cloudArtistID:completion:"
+ "removePinnedArtistWithPersistentID:cloudArtistID:configuration:completion:"
+ "removePinnedEntityWithPersistentID:cloudID:type:completion:"
+ "removePinnedEntityWithPersistentID:cloudID:type:configuration:completion:"
+ "setCloudPlaylistFolderID:"
+ "setOptions:"
+ "setPartner:"
+ "setPosition:"
+ "setSubscriptionStatusFromResponsePayload:forUserIdentity:withCompletionHandler:"
+ "setSubscriptionStatusFromResponsePayload:withCompletionHandler:"
+ "setTransitionTypeProvided:"
+ "setUserTransitionTypePreference:"
+ "setWallClockPlayDuration:"
+ "shouldAllowUntrustedHosts"
+ "transitionTypeProvided"
+ "tv-cover-artwork-template-url"
+ "tv-cover-artwork-token"
+ "updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:completion:"
+ "updatePinnedLibraryAlbumWithPersistentID:cloudAlbumID:defaultAction:configuration:completion:"
+ "updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:completion:"
+ "updatePinnedLibraryArtistWithPersistentID:cloudArtistID:defaultAction:configuration:completion:"
+ "updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:completion:"
+ "updatePinnedLibraryEntityWithPersistentID:cloudID:type:defaultAction:configuration:completion:"
+ "userTransitionTypePreference"
+ "v24@?0@\"ICMusicSubscriptionLeaseStatus\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"ICURLBag\"16^B24"
+ "v40@0:8@\"NSDictionary\"16@\"ICUserIdentity\"24@?<v@?@\"ICMusicSubscriptionStatus\"@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSURLSession\"16@\"AVAssetDownloadTask\"24@\"AVMetricEvent\"32"
+ "v44@0:8@\"ICContentKeySession\"16@\"NSString\"24B32B36B40"
+ "v44@0:8@16@24B32B36B40"
+ "v48@0:8@\"NSArray\"16@\"ICCloudAddReferral\"24@\"ICConnectionConfiguration\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8q16q24q32@?40"
+ "v56@0:8q16@\"NSString\"24q32@\"ICConnectionConfiguration\"40@?<v@?@\"NSError\">48"
+ "v56@0:8q16q24q32@\"ICConnectionConfiguration\"40@?<v@?@\"NSError\">48"
+ "v56@0:8q16q24q32q40@?48"
+ "v64@0:8q16q24q32q40@\"ICConnectionConfiguration\"48@?<v@?@\"NSError\">56"
+ "v64@0:8q16q24q32q40@48@?56"
+ "wallClockPlayDuration"
+ "{?=\"characterDisplayedCount\"b1\"cloudPlaylistFolderID\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"wallClockPlayDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sharedActivityType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"transitionTypeProvided\"b1\"userTransitionTypePreference\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"isCollaborativePlaylist\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"
+ "\xf1"
- "%c%c%c%c"
- "%{public}@ Failed to present dialog. err=%{public}@"
- "%{public}@ Received notification: %{public}@"
- "%{public}@ Recevied AMSBag change notification for profile %{public}@/%{public}@ and account '%{public}@"
- "%{public}@ Recevied token response %@"
- "%{public}@ Skipping silent authentication attempt due to throttling. last attempt was at %{public}@ (%.2fs ago)"
- "%{public}@ handling dialog request %{public}@"
- "<%@ %p statusType:%@, matchEnabled=%@, carrierBundlingStatusType:%@, reasonType:%@, sourceType:%@%@, capabilities:%@, eligibleOffers:[%@], isAutoRenewEnabled:%@, isInFreePeriod:%@, isInFreeTrial:%@, isEligibleForFreeTrial:%@, initialPurchaseTimestamp:%@, serviceBeginsTimestamp:%@, studentExpirationDate:%@, studentVerifier:%@, studentVerificationId:%@>"
- "MSVHasher+SipHash.h"
- "TQ,N,V_vocalAttenuationAvailability"
- "TQ,R,N,V_audioQualityPreference"
- "TQ,R,N,V_autoPlayMode"
- "TQ,R,N,V_containerType"
- "TQ,R,N,V_displayType"
- "TQ,R,N,V_endReasonType"
- "TQ,R,N,V_eventType"
- "TQ,R,N,V_itemType"
- "TQ,R,N,V_mediaType"
- "TQ,R,N,V_playbackFormatPreference"
- "TQ,R,N,V_reasonHintType"
- "TQ,R,N,V_repeatPlayMode"
- "TQ,R,N,V_shufflePlayMode"
- "TQ,R,N,V_sourceType"
- "_MSVHasher_SipHash_1_3_Append32: invalid byte count detected [byteCount & 3]: %lld"
- "_MSVHasher_SipHash_1_3_Append32: invalid byte count detected [byteCount & 7, tail == 0]: %lld"
- "_MSVHasher_SipHash_1_3_Append64: invalid byte count detected [byteCount & 3]: %lld"
- "_MSVHasher_SipHash_1_3_Append64: invalid byte count detected [byteCount & 7, tail == 0]: %lld"
- "v32@?0@\"ICURLBag\"8@\"ICURLAggregatedPerformanceMetrics\"16@\"NSError\"24"
- "v32@?0@\"ICURLBag\"8Q16^B24"
- "void _MSVHasher_SipHash_1_3_Append32(MSVHasherSipHash_1_3 *, uint32_t)"
- "void _MSVHasher_SipHash_1_3_Append64(MSVHasherSipHash_1_3 *, uint64_t)"
- "{?=\"characterDisplayedCount\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sharedActivityType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"isCollaborativePlaylist\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"
- "\xe1"

```
