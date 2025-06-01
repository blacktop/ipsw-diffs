## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4023.210.3.0.0
-  __TEXT.__text: 0x286040
+4023.310.5.0.0
+  __TEXT.__text: 0x287594
   __TEXT.__auth_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x149d0
-  __TEXT.__const: 0x1653c
-  __TEXT.__gcc_except_tab: 0x2514
-  __TEXT.__cstring: 0x15cb4
-  __TEXT.__oslogstring: 0x1c65b
+  __TEXT.__objc_methlist: 0x14a40
+  __TEXT.__const: 0x1654c
+  __TEXT.__gcc_except_tab: 0x25d4
+  __TEXT.__cstring: 0x15dfd
+  __TEXT.__oslogstring: 0x1ca32
   __TEXT.__ustring: 0x8e
   __TEXT.__dlopen_cstrs: 0x3de
-  __TEXT.__unwind_info: 0x6204
+  __TEXT.__unwind_info: 0x6224
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x39ac
-  __TEXT.__objc_methname: 0x3173a
-  __TEXT.__objc_methtype: 0x73c2
-  __TEXT.__objc_stubs: 0x19dc0
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x7df0
+  __TEXT.__objc_methname: 0x319aa
+  __TEXT.__objc_methtype: 0x736a
+  __TEXT.__objc_stubs: 0x19f00
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x7e40
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x27388
-  __DATA_CONST.__objc_selrefs: 0x92c8
+  __DATA_CONST.__objc_const: 0x27428
+  __DATA_CONST.__objc_selrefs: 0x9340
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__const: 0x10580
-  __AUTH_CONST.__cfstring: 0x171a0
+  __AUTH_CONST.__cfstring: 0x172c0
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_const: 0xa380
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x4c40
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0xf20
+  __DATA.__objc_classrefs: 0xf28
   __DATA.__objc_superrefs: 0xb50
-  __DATA.__objc_ivar: 0x2204
+  __DATA.__objc_ivar: 0x2210
   __DATA.__data: 0x24d0
   __DATA.__common: 0xa8c
   __DATA.__bss: 0x278

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 32837148-96FA-3D72-8886-74A1F98CD2AA
-  Functions: 9574
-  Symbols:   29890
-  CStrings:  16744
+  UUID: 960FDEF9-B47F-3877-8CEE-A4485D85E146
+  Functions: 9589
+  Symbols:   29938
+  CStrings:  16795
 
Symbols:
+ +[ICCloudClientCollaborationEditParams newIdentifierString]
+ +[ICCloudClientCollaborationEditParams paramsForAddingTrackWithAdamID:itemUUID:itemPositionUUID:afterReferencePositionUUD:]
+ +[ICCloudClientCollaborationEditParams paramsForAddingTrackWithAdamID:itemUUID:itemPositionUUID:atPosition:]
+ +[ICCloudClientCollaborationEditParams paramsForMovingTrackWithItemUUID:withNewItemPositionUUID:afterReferencePositionUUD:]
+ +[ICCloudClientCollaborationEditParams paramsForMovingTrackWithItemUUID:withNewItemPositionUUID:toPosition:]
+ +[ICCloudClientCollaborationEditParams paramsForUnsettingReaction:onTrackWithItemUUID:]
+ -[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]
+ -[ICCloudClient setCloudFavoriteSongAddToLibraryBehavior:completionHandler:]
+ -[ICCloudClientCollaborationEditParams itemPositionUUID]
+ -[ICCloudClientCollaborationEditParams setReactionString:]
+ -[ICContentKeySession isStoreKeyServer]
+ -[ICContentKeySession setIsStoreKeyServer:]
+ -[ICURLBagProvider _cacheDirectoryPath]
+ -[ICURLBagProvider _cleanBagCacheExcludingPaths:]
+ -[ICURLBagProvider _loadMonoCache]
+ -[ICURLBagProvider _loadPlistAtPath:]
+ -[ICURLBagProvider _persistBagToDisk:withKey:]
+ GCC_except_table1613
+ GCC_except_table1788
+ GCC_except_table1817
+ GCC_except_table1832
+ GCC_except_table1868
+ GCC_except_table1983
+ GCC_except_table1998
+ GCC_except_table2047
+ GCC_except_table2049
+ GCC_except_table2055
+ GCC_except_table2062
+ GCC_except_table2090
+ GCC_except_table2104
+ GCC_except_table2110
+ GCC_except_table2113
+ GCC_except_table2118
+ GCC_except_table2121
+ GCC_except_table2134
+ GCC_except_table2209
+ GCC_except_table2218
+ GCC_except_table2221
+ GCC_except_table2224
+ GCC_except_table2227
+ GCC_except_table2229
+ GCC_except_table2240
+ GCC_except_table2242
+ GCC_except_table2259
+ GCC_except_table2298
+ GCC_except_table2329
+ GCC_except_table2331
+ GCC_except_table2333
+ GCC_except_table2335
+ GCC_except_table2684
+ GCC_except_table2729
+ GCC_except_table2875
+ GCC_except_table2902
+ GCC_except_table2926
+ GCC_except_table2931
+ GCC_except_table2942
+ GCC_except_table3040
+ GCC_except_table3308
+ GCC_except_table3312
+ GCC_except_table3315
+ GCC_except_table3330
+ GCC_except_table3341
+ GCC_except_table3360
+ GCC_except_table3400
+ GCC_except_table3414
+ GCC_except_table3527
+ GCC_except_table3685
+ GCC_except_table3846
+ GCC_except_table3888
+ GCC_except_table3984
+ GCC_except_table3988
+ GCC_except_table3990
+ GCC_except_table3992
+ GCC_except_table3996
+ GCC_except_table4003
+ GCC_except_table4007
+ GCC_except_table4022
+ GCC_except_table4025
+ GCC_except_table4198
+ GCC_except_table4250
+ GCC_except_table4254
+ GCC_except_table4257
+ GCC_except_table4262
+ GCC_except_table4326
+ GCC_except_table4368
+ GCC_except_table4372
+ GCC_except_table4374
+ GCC_except_table4494
+ GCC_except_table4580
+ GCC_except_table4660
+ GCC_except_table4725
+ GCC_except_table4806
+ GCC_except_table4969
+ GCC_except_table5209
+ GCC_except_table5305
+ GCC_except_table5384
+ GCC_except_table5385
+ GCC_except_table5458
+ GCC_except_table5474
+ GCC_except_table5751
+ GCC_except_table5758
+ GCC_except_table5766
+ GCC_except_table5777
+ GCC_except_table5779
+ GCC_except_table5784
+ GCC_except_table5801
+ GCC_except_table5816
+ GCC_except_table5824
+ GCC_except_table5833
+ GCC_except_table5842
+ GCC_except_table5875
+ GCC_except_table5889
+ GCC_except_table5898
+ GCC_except_table5905
+ GCC_except_table5906
+ GCC_except_table5965
+ GCC_except_table5968
+ GCC_except_table6003
+ GCC_except_table6008
+ GCC_except_table6014
+ GCC_except_table6017
+ GCC_except_table6020
+ GCC_except_table6023
+ GCC_except_table6026
+ GCC_except_table6029
+ GCC_except_table6032
+ GCC_except_table6035
+ GCC_except_table6038
+ GCC_except_table6041
+ GCC_except_table6044
+ GCC_except_table6144
+ GCC_except_table6157
+ GCC_except_table6349
+ GCC_except_table6356
+ GCC_except_table6530
+ GCC_except_table6534
+ GCC_except_table6536
+ GCC_except_table6559
+ GCC_except_table6605
+ GCC_except_table6792
+ GCC_except_table6925
+ GCC_except_table7068
+ GCC_except_table7081
+ GCC_except_table7102
+ GCC_except_table7113
+ GCC_except_table7157
+ GCC_except_table7175
+ GCC_except_table7230
+ GCC_except_table7239
+ GCC_except_table7246
+ GCC_except_table7287
+ GCC_except_table7306
+ GCC_except_table7339
+ GCC_except_table7397
+ GCC_except_table7398
+ GCC_except_table7411
+ GCC_except_table7828
+ GCC_except_table7834
+ GCC_except_table7856
+ GCC_except_table7860
+ GCC_except_table7871
+ GCC_except_table7876
+ GCC_except_table7911
+ GCC_except_table7914
+ GCC_except_table7976
+ GCC_except_table8021
+ GCC_except_table8069
+ GCC_except_table8094
+ GCC_except_table8099
+ GCC_except_table8101
+ GCC_except_table8103
+ GCC_except_table8135
+ GCC_except_table8278
+ GCC_except_table8286
+ GCC_except_table8306
+ GCC_except_table8314
+ GCC_except_table8358
+ GCC_except_table8492
+ GCC_except_table8496
+ GCC_except_table8498
+ GCC_except_table8535
+ GCC_except_table8538
+ GCC_except_table8545
+ GCC_except_table8548
+ GCC_except_table8759
+ GCC_except_table8763
+ GCC_except_table8803
+ _ICCloudClientCloudFavoriteSongAddToLibraryBehaviorDidChangeNotification
+ _ICCloudClientGetStringForAddToLibraryBehavior
+ _ICStoreURLRequestParsedBodyInfoKey
+ _MSVFastHexStringFromBytes.hexCharacters.40607
+ _NSFileModificationDate
+ _OBJC_CLASS_$_MSVLRUDictionary
+ _OBJC_IVAR_$_ICCloudClientCollaborationEditParams._itemPositionUUID
+ _OBJC_IVAR_$_ICContentKeySession._isStoreKeyServer
+ _OBJC_IVAR_$_ICDefaults._lock
+ __MSV_XXH_XXH32_update.11553
+ __MSV_XXH_XXH32_update.17259
+ __MSV_XXH_XXH32_update.20189
+ __MSV_XXH_XXH32_update.40596
+ __MSV_XXH_XXH64_digest.17379
+ __MSV_XXH_XXH64_update.11554
+ __MSV_XXH_XXH64_update.17260
+ __MSV_XXH_XXH64_update.20190
+ __MSV_XXH_XXH64_update.40597
+ ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.37
+ ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.57
+ ___105-[ICCloudClient _enableCloudLibraryWithPolicy:startinitialImport:isExplicitUserAction:completionHandler:]_block_invoke.63
+ ___30-[ICURLBagProvider _loadCache]_block_invoke.134
+ ___34-[ICURLBagProvider _loadMonoCache]_block_invoke
+ ___34-[ICURLBagProvider _loadMonoCache]_block_invoke.139
+ ___35-[ICURLBagProvider invalidateCache]_block_invoke.66
+ ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.142
+ ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.137
+ ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.147
+ ___46-[ICURLBagProvider _persistBagToDisk:withKey:]_block_invoke
+ ___49-[ICURLBagProvider _cleanBagCacheExcludingPaths:]_block_invoke
+ ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.79
+ ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.126
+ ___54-[ICCloudClient isMediaKindDisabledForJaliscoLibrary:]_block_invoke.70
+ ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.132
+ ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.118
+ ___58-[ICCloudClient removeItemsWithSagaIDs:completionHandler:]_block_invoke.34
+ ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.69
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.191
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.193
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.209
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.211
+ ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.159
+ ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.113
+ ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.51
+ ___61-[ICCloudClient importScreenshotForSagaID:completionHandler:]_block_invoke.85
+ ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.101
+ ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.115
+ ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.123
+ ___61-[ICCloudClient publishPlaylistWithSagaID:completionHandler:]_block_invoke.25
+ ___62-[ICCloudClient importItemArtworkForSagaID:completionHandler:]_block_invoke.84
+ ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke.33
+ ___63-[ICCloudClient updatePinnedSubscribedPlaylistsWithCompletion:]_block_invoke.29
+ ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.77
+ ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke.32
+ ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.125
+ ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.105
+ ___64-[ICCloudClient sdk_addStoreItemWithOpaqueID:completionHandler:]_block_invoke.31
+ ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.161
+ ___65-[ICCloudClient disableCloudLibraryWithReason:completionHandler:]_block_invoke.64
+ ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.120
+ ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.67
+ ___67-[ICCloudClient addStoreItemWithAdamID:referral:completionHandler:]_block_invoke.30
+ ___67-[ICCloudClient hideItemsWithPurchaseHistoryIDs:completionHandler:]_block_invoke.35
+ ___67-[ICCloudClient importContainerArtworkForSagaID:completionHandler:]_block_invoke.86
+ ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.121
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.122
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.123
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.88
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.92
+ ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.124
+ ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.103
+ ___72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.90
+ ___72-[ICCloudClient importScreenshotForPurchaseHistoryID:completionHandler:]_block_invoke.83
+ ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.96
+ ___72-[ICCloudClient loadLastKnownEnableICMLErrorStatusWithCompletionHander:]_block_invoke.80
+ ___73-[ICCloudClient importItemArtworkForPurchaseHistoryID:completionHandler:]_block_invoke.82
+ ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.99
+ ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.151
+ ___76-[ICCloudClient setCloudFavoriteSongAddToLibraryBehavior:completionHandler:]_block_invoke
+ ___76-[ICCloudClient setCloudFavoriteSongAddToLibraryBehavior:completionHandler:]_block_invoke.12
+ ___76-[ICCloudClient setCloudFavoriteSongAddToLibraryBehavior:completionHandler:]_block_invoke_2
+ ___76-[ICCloudClient setCloudFavoriteSongAddToLibraryBehavior:completionHandler:]_block_invoke_3
+ ___76-[ICCloudClient uploadArtworkForPlaylistWithPersistentID:completionHandler:]_block_invoke.27
+ ___77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.91
+ ___79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.88
+ ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.61
+ ___80-[ICCloudClient addItemWithSagaID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.21
+ ___80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.87
+ ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.55
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.152
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke.153
+ ___81-[ICCloudClient setAlbumEntityProperties:forAlbumPersistentID:completionHandler:]_block_invoke_2
+ ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.41
+ ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.109
+ ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.59
+ ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.107
+ ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.53
+ ___84-[ICCloudClient sdk_addItemWithSagaID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.24
+ ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.45
+ ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.89
+ ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.47
+ ___87-[ICCloudClient createPlaylistWithPersistentID:properties:trackList:completionHandler:]_block_invoke.15
+ ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.155
+ ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.49
+ ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.111
+ ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.43
+ ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.39
+ ___91-[ICCloudClient sdk_addStoreItemWithOpaqueID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.22
+ ___91-[ICCloudClient sdk_createPlaylistWithPersistentID:properties:tracklist:completionHandler:]_block_invoke.17
+ ___91-[ICCloudClient setPlaylistProperties:trackList:forPlaylistPersistentID:completionHandler:]_block_invoke.18
+ ___92-[ICStoreURLRequest buildStoreURLRequestWithURLRequest:builderProperties:completionHandler:]_block_invoke.250
+ ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.52
+ ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.60
+ ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.61
+ ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.62
+ ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.64
+ ___94-[ICCloudClient addStoreItemWithAdamID:referral:toPlaylistWithPersistentID:completionHandler:]_block_invoke.20
+ ___95-[ICCloudClient sdk_setPlaylistProperties:trackList:forPlaylistPersistentID:completionHandler:]_block_invoke.19
+ ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.163
+ ___97-[ICCloudClient updateSubscribedPlaylistsWithSagaIDs:ignoreMinRefreshInterval:completionHandler:]_block_invoke.28
+ ___Block_byref_object_copy_.10256
+ ___Block_byref_object_copy_.10545
+ ___Block_byref_object_copy_.10673
+ ___Block_byref_object_copy_.1103
+ ___Block_byref_object_copy_.12194
+ ___Block_byref_object_copy_.13544
+ ___Block_byref_object_copy_.14086
+ ___Block_byref_object_copy_.14259
+ ___Block_byref_object_copy_.14524
+ ___Block_byref_object_copy_.14933
+ ___Block_byref_object_copy_.16062
+ ___Block_byref_object_copy_.16541
+ ___Block_byref_object_copy_.16768
+ ___Block_byref_object_copy_.18464
+ ___Block_byref_object_copy_.18829
+ ___Block_byref_object_copy_.19039
+ ___Block_byref_object_copy_.20018
+ ___Block_byref_object_copy_.20905
+ ___Block_byref_object_copy_.22172
+ ___Block_byref_object_copy_.22273
+ ___Block_byref_object_copy_.24681
+ ___Block_byref_object_copy_.25107
+ ___Block_byref_object_copy_.25668
+ ___Block_byref_object_copy_.26023
+ ___Block_byref_object_copy_.26065
+ ___Block_byref_object_copy_.26975
+ ___Block_byref_object_copy_.27938
+ ___Block_byref_object_copy_.28965
+ ___Block_byref_object_copy_.29307
+ ___Block_byref_object_copy_.30343
+ ___Block_byref_object_copy_.31065
+ ___Block_byref_object_copy_.31446
+ ___Block_byref_object_copy_.31623
+ ___Block_byref_object_copy_.31783
+ ___Block_byref_object_copy_.32536
+ ___Block_byref_object_copy_.34566
+ ___Block_byref_object_copy_.34791
+ ___Block_byref_object_copy_.34925
+ ___Block_byref_object_copy_.35784
+ ___Block_byref_object_copy_.35947
+ ___Block_byref_object_copy_.3597
+ ___Block_byref_object_copy_.36632
+ ___Block_byref_object_copy_.36902
+ ___Block_byref_object_copy_.37493
+ ___Block_byref_object_copy_.37672
+ ___Block_byref_object_copy_.37977
+ ___Block_byref_object_copy_.38824
+ ___Block_byref_object_copy_.3954
+ ___Block_byref_object_copy_.4093
+ ___Block_byref_object_copy_.4126
+ ___Block_byref_object_copy_.4992
+ ___Block_byref_object_copy_.5150
+ ___Block_byref_object_copy_.5240
+ ___Block_byref_object_copy_.5990
+ ___Block_byref_object_copy_.6423
+ ___Block_byref_object_copy_.6535
+ ___Block_byref_object_copy_.7037
+ ___Block_byref_object_copy_.9344
+ ___Block_byref_object_copy_.9449
+ ___Block_byref_object_dispose_.10257
+ ___Block_byref_object_dispose_.10546
+ ___Block_byref_object_dispose_.10674
+ ___Block_byref_object_dispose_.1104
+ ___Block_byref_object_dispose_.12195
+ ___Block_byref_object_dispose_.13545
+ ___Block_byref_object_dispose_.14087
+ ___Block_byref_object_dispose_.14260
+ ___Block_byref_object_dispose_.14525
+ ___Block_byref_object_dispose_.14934
+ ___Block_byref_object_dispose_.16063
+ ___Block_byref_object_dispose_.16542
+ ___Block_byref_object_dispose_.16769
+ ___Block_byref_object_dispose_.18465
+ ___Block_byref_object_dispose_.18830
+ ___Block_byref_object_dispose_.19040
+ ___Block_byref_object_dispose_.20019
+ ___Block_byref_object_dispose_.20906
+ ___Block_byref_object_dispose_.22173
+ ___Block_byref_object_dispose_.22274
+ ___Block_byref_object_dispose_.24682
+ ___Block_byref_object_dispose_.25108
+ ___Block_byref_object_dispose_.25669
+ ___Block_byref_object_dispose_.26024
+ ___Block_byref_object_dispose_.26066
+ ___Block_byref_object_dispose_.26976
+ ___Block_byref_object_dispose_.27939
+ ___Block_byref_object_dispose_.28966
+ ___Block_byref_object_dispose_.29308
+ ___Block_byref_object_dispose_.30344
+ ___Block_byref_object_dispose_.31066
+ ___Block_byref_object_dispose_.31447
+ ___Block_byref_object_dispose_.31624
+ ___Block_byref_object_dispose_.31784
+ ___Block_byref_object_dispose_.32537
+ ___Block_byref_object_dispose_.34567
+ ___Block_byref_object_dispose_.34792
+ ___Block_byref_object_dispose_.34926
+ ___Block_byref_object_dispose_.35785
+ ___Block_byref_object_dispose_.35948
+ ___Block_byref_object_dispose_.3598
+ ___Block_byref_object_dispose_.36633
+ ___Block_byref_object_dispose_.36903
+ ___Block_byref_object_dispose_.37494
+ ___Block_byref_object_dispose_.37673
+ ___Block_byref_object_dispose_.37978
+ ___Block_byref_object_dispose_.38825
+ ___Block_byref_object_dispose_.3955
+ ___Block_byref_object_dispose_.4094
+ ___Block_byref_object_dispose_.4127
+ ___Block_byref_object_dispose_.4993
+ ___Block_byref_object_dispose_.5151
+ ___Block_byref_object_dispose_.5241
+ ___Block_byref_object_dispose_.5991
+ ___Block_byref_object_dispose_.6424
+ ___Block_byref_object_dispose_.6536
+ ___Block_byref_object_dispose_.7038
+ ___Block_byref_object_dispose_.9345
+ ___Block_byref_object_dispose_.9450
+ ___block_descriptor_40_e8_32s_e11_q24?0816ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24ls32l8s40l8s48l8r56l8
+ ___block_literal_global.10.25678
+ ___block_literal_global.10346
+ ___block_literal_global.11290
+ ___block_literal_global.11733
+ ___block_literal_global.12.24475
+ ___block_literal_global.12.25676
+ ___block_literal_global.12305
+ ___block_literal_global.129
+ ___block_literal_global.12948
+ ___block_literal_global.12990
+ ___block_literal_global.13.37986
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.13575
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.141
+ ___block_literal_global.144
+ ___block_literal_global.1440
+ ___block_literal_global.146
+ ___block_literal_global.149
+ ___block_literal_global.14972
+ ___block_literal_global.157
+ ___block_literal_global.157.5228
+ ___block_literal_global.16465
+ ___block_literal_global.168.28237
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.17498
+ ___block_literal_global.176
+ ___block_literal_global.17904
+ ___block_literal_global.18.25674
+ ___block_literal_global.18.34624
+ ___block_literal_global.18296
+ ___block_literal_global.18516
+ ___block_literal_global.18730
+ ___block_literal_global.19.25561
+ ___block_literal_global.19894
+ ___block_literal_global.21548
+ ___block_literal_global.22074
+ ___block_literal_global.23627
+ ___block_literal_global.23751
+ ___block_literal_global.24474
+ ___block_literal_global.24668
+ ___block_literal_global.25175
+ ___block_literal_global.25340
+ ___block_literal_global.25543
+ ___block_literal_global.25684
+ ___block_literal_global.27012
+ ___block_literal_global.27527
+ ___block_literal_global.28336
+ ___block_literal_global.28676
+ ___block_literal_global.28979
+ ___block_literal_global.29129
+ ___block_literal_global.3.14970
+ ___block_literal_global.3.17505
+ ___block_literal_global.30118
+ ___block_literal_global.30668
+ ___block_literal_global.30728
+ ___block_literal_global.30952
+ ___block_literal_global.31520
+ ___block_literal_global.32130
+ ___block_literal_global.32573
+ ___block_literal_global.33687
+ ___block_literal_global.3410
+ ___block_literal_global.34209
+ ___block_literal_global.34647
+ ___block_literal_global.35725
+ ___block_literal_global.3616
+ ___block_literal_global.36645
+ ___block_literal_global.37012
+ ___block_literal_global.37109
+ ___block_literal_global.37816
+ ___block_literal_global.37996
+ ___block_literal_global.3888
+ ___block_literal_global.38935
+ ___block_literal_global.39075
+ ___block_literal_global.39205
+ ___block_literal_global.39898
+ ___block_literal_global.40090
+ ___block_literal_global.40426
+ ___block_literal_global.4144
+ ___block_literal_global.4203
+ ___block_literal_global.4323
+ ___block_literal_global.47.30768
+ ___block_literal_global.52.30771
+ ___block_literal_global.5405
+ ___block_literal_global.58
+ ___block_literal_global.5870
+ ___block_literal_global.6.25682
+ ___block_literal_global.6610
+ ___block_literal_global.6705
+ ___block_literal_global.68.30624
+ ___block_literal_global.69
+ ___block_literal_global.6922
+ ___block_literal_global.7083
+ ___block_literal_global.7314
+ ___block_literal_global.76.30791
+ ___block_literal_global.8.25680
+ ___block_literal_global.8035
+ ___block_literal_global.8116
+ ___block_literal_global.9050
+ ___block_literal_global.9846
+ __unnamed_array_storage.30770
+ __unnamed_array_storage.40316
+ __unnamed_array_storage.96.40317
+ _objc_msgSend$_cacheDirectoryPath
+ _objc_msgSend$_cleanBagCacheExcludingPaths:
+ _objc_msgSend$_loadMonoCache
+ _objc_msgSend$_loadPlistAtPath:
+ _objc_msgSend$_persistBagToDisk:withKey:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$initWithMaximumCapacity:
+ _objc_msgSend$isStoreKeyServer
+ _objc_msgSend$setAlbumEntityProperties:forAlbumPersistentID:configuration:completion:
+ _objc_msgSend$setCloudFavoriteSongAddToLibraryBehavior:forConfiguration:completion:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByDeletingPathExtension
+ _sharedCache.sOnceToken.29128
+ _sharedCache.sSharedCache.29130
+ _sharedController.sOnceToken.34646
+ _sharedController.sOnceToken.37995
+ _sharedController.sSharedController.34648
+ _sharedController.sSharedController.37997
+ _sharedManager.sOnceToken.18729
+ _sharedManager.sOnceToken.27526
+ _sharedManager.sSharedManager.18731
+ _sharedManager.sSharedManager.27528
+ _sharedMonitor.sOnceToken.17903
+ _sharedMonitor.sOnceToken.38934
+ _sharedMonitor.sSharedMonitor.17905
+ _sharedMonitor.sSharedMonitor.38936
+ _sharedProvider.sOnceToken.39204
+ _sharedProvider.sSharedProvider.39206
- +[ICCloudClientCollaborationEditParams paramsForAddingTrackWithAdamID:itemUUID:afterReferencePositionUUD:]
- +[ICCloudClientCollaborationEditParams paramsForAddingTrackWithAdamID:itemUUID:atPosition:]
- +[ICCloudClientCollaborationEditParams paramsForMovingTrackWithItemUUID:afterReferencePositionUUD:]
- +[ICCloudClientCollaborationEditParams paramsForMovingTrackWithItemUUID:toPosition:]
- +[ICCloudClientCollaborationEditParams paramsForUnsettingReactionOnTrackWithItemUUID:]
- -[ICCloudClient setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:]
- -[ICURLBagProvider _cacheFilePath]
- -[ICURLBagProvider _saveCache]
- GCC_except_table1608
- GCC_except_table1782
- GCC_except_table1811
- GCC_except_table1826
- GCC_except_table1973
- GCC_except_table1988
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2045
- GCC_except_table2052
- GCC_except_table2080
- GCC_except_table2094
- GCC_except_table2098
- GCC_except_table2100
- GCC_except_table2103
- GCC_except_table2111
- GCC_except_table2124
- GCC_except_table2199
- GCC_except_table2208
- GCC_except_table2211
- GCC_except_table2214
- GCC_except_table2217
- GCC_except_table2219
- GCC_except_table2230
- GCC_except_table2232
- GCC_except_table2249
- GCC_except_table2288
- GCC_except_table2319
- GCC_except_table2321
- GCC_except_table2323
- GCC_except_table2325
- GCC_except_table2674
- GCC_except_table2719
- GCC_except_table2865
- GCC_except_table2882
- GCC_except_table2916
- GCC_except_table2921
- GCC_except_table2932
- GCC_except_table3030
- GCC_except_table3298
- GCC_except_table3302
- GCC_except_table3305
- GCC_except_table3320
- GCC_except_table3331
- GCC_except_table3350
- GCC_except_table3390
- GCC_except_table3404
- GCC_except_table3517
- GCC_except_table3675
- GCC_except_table3836
- GCC_except_table3878
- GCC_except_table3966
- GCC_except_table3974
- GCC_except_table3978
- GCC_except_table3980
- GCC_except_table3982
- GCC_except_table3993
- GCC_except_table3997
- GCC_except_table4012
- GCC_except_table4015
- GCC_except_table4188
- GCC_except_table4240
- GCC_except_table4244
- GCC_except_table4247
- GCC_except_table4252
- GCC_except_table4316
- GCC_except_table4358
- GCC_except_table4362
- GCC_except_table4364
- GCC_except_table4484
- GCC_except_table4570
- GCC_except_table4650
- GCC_except_table4715
- GCC_except_table4796
- GCC_except_table4959
- GCC_except_table5199
- GCC_except_table5295
- GCC_except_table5374
- GCC_except_table5375
- GCC_except_table5448
- GCC_except_table5464
- GCC_except_table5741
- GCC_except_table5748
- GCC_except_table5756
- GCC_except_table5767
- GCC_except_table5769
- GCC_except_table5774
- GCC_except_table5781
- GCC_except_table5806
- GCC_except_table5814
- GCC_except_table5823
- GCC_except_table5832
- GCC_except_table5865
- GCC_except_table5879
- GCC_except_table5888
- GCC_except_table5895
- GCC_except_table5896
- GCC_except_table5955
- GCC_except_table5958
- GCC_except_table5993
- GCC_except_table5998
- GCC_except_table6004
- GCC_except_table6007
- GCC_except_table6010
- GCC_except_table6013
- GCC_except_table6016
- GCC_except_table6019
- GCC_except_table6022
- GCC_except_table6025
- GCC_except_table6028
- GCC_except_table6031
- GCC_except_table6034
- GCC_except_table6134
- GCC_except_table6147
- GCC_except_table6339
- GCC_except_table6346
- GCC_except_table6520
- GCC_except_table6524
- GCC_except_table6526
- GCC_except_table6549
- GCC_except_table6595
- GCC_except_table6782
- GCC_except_table6915
- GCC_except_table7056
- GCC_except_table7069
- GCC_except_table7090
- GCC_except_table7101
- GCC_except_table7145
- GCC_except_table7163
- GCC_except_table7215
- GCC_except_table7218
- GCC_except_table7234
- GCC_except_table7275
- GCC_except_table7294
- GCC_except_table7327
- GCC_except_table7385
- GCC_except_table7386
- GCC_except_table7399
- GCC_except_table7816
- GCC_except_table7822
- GCC_except_table7844
- GCC_except_table7848
- GCC_except_table7859
- GCC_except_table7864
- GCC_except_table7899
- GCC_except_table7902
- GCC_except_table7964
- GCC_except_table8009
- GCC_except_table8054
- GCC_except_table8079
- GCC_except_table8084
- GCC_except_table8086
- GCC_except_table8088
- GCC_except_table8120
- GCC_except_table8263
- GCC_except_table8271
- GCC_except_table8276
- GCC_except_table8299
- GCC_except_table8343
- GCC_except_table8477
- GCC_except_table8481
- GCC_except_table8483
- GCC_except_table8520
- GCC_except_table8523
- GCC_except_table8530
- GCC_except_table8533
- GCC_except_table8744
- GCC_except_table8748
- GCC_except_table8788
- _MSVFastHexStringFromBytes.hexCharacters.40577
- __MSV_XXH_XXH32_update.11514
- __MSV_XXH_XXH32_update.17234
- __MSV_XXH_XXH32_update.20159
- __MSV_XXH_XXH32_update.40566
- __MSV_XXH_XXH64_digest.17354
- __MSV_XXH_XXH64_update.11515
- __MSV_XXH_XXH64_update.17235
- __MSV_XXH_XXH64_update.20160
- __MSV_XXH_XXH64_update.40567
- ___102-[ICCloudClient addGeniusPlaylistWithPersistentID:name:seedItemSagaIDs:itemSagaIDs:completionHandler:]_block_invoke.35
- ___102-[ICCloudClient respondToPendingCollaborator:onCollaborationWithPersistentID:withApproval:completion:]_block_invoke.55
- ___105-[ICCloudClient _enableCloudLibraryWithPolicy:startinitialImport:isExplicitUserAction:completionHandler:]_block_invoke.62
- ___30-[ICURLBagProvider _loadCache]_block_invoke.127
- ___30-[ICURLBagProvider _saveCache]_block_invoke
- ___30-[ICURLBagProvider _saveCache]_block_invoke.129
- ___30-[ICURLBagProvider _saveCache]_block_invoke_2
- ___35-[ICURLBagProvider invalidateCache]_block_invoke.60
- ___42-[ICCloudClient uploadCloudItemProperties]_block_invoke.141
- ___45-[ICCloudClient setItemProperties:forSagaID:]_block_invoke.136
- ___46-[ICCloudClient uploadCloudPlaylistProperties]_block_invoke.146
- ___53-[ICCloudClient deauthenticateWithCompletionHandler:]_block_invoke.77
- ___53-[ICURLBagProvider _handleAMSBagChangedNotification:]_block_invoke.122
- ___54-[ICCloudClient isMediaKindDisabledForJaliscoLibrary:]_block_invoke.69
- ___56-[ICCloudClient setItemProperties:forPurchaseHistoryID:]_block_invoke.131
- ___57-[ICCloudClient loadUpdateProgressWithCompletionHandler:]_block_invoke.116
- ___58-[ICCloudClient removeItemsWithSagaIDs:completionHandler:]_block_invoke.33
- ___58-[ICCloudClient removeJaliscoLibraryWithCompletionHander:]_block_invoke.67
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.187
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.188
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.206
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.208
- ___60-[ICCloudClient loadBooksForStoreIDs:withCompletionHandler:]_block_invoke.157
- ___60-[ICCloudClient loadGeniusItemsForSagaID:completionHandler:]_block_invoke.111
- ___61-[ICCloudClient endCollaborationWithPersistentID:completion:]_block_invoke.49
- ___61-[ICCloudClient importScreenshotForSagaID:completionHandler:]_block_invoke.84
- ___61-[ICCloudClient loadArtworkInfoForSagaIDs:completionHandler:]_block_invoke.99
- ___61-[ICCloudClient loadIsUpdateInProgressWithCompletionHandler:]_block_invoke.114
- ___61-[ICCloudClient loadSagaUpdateProgressWithCompletionHandler:]_block_invoke.121
- ___61-[ICCloudClient publishPlaylistWithSagaID:completionHandler:]_block_invoke.24
- ___62-[ICCloudClient importItemArtworkForSagaID:completionHandler:]_block_invoke.83
- ___62-[ICCloudClient removePlaylistsWithSagaIDs:completionHandler:]_block_invoke.32
- ___63-[ICCloudClient updatePinnedSubscribedPlaylistsWithCompletion:]_block_invoke.28
- ___63-[ICCloudClient updateSagaLibraryWithReason:completionHandler:]_block_invoke.75
- ___64-[ICCloudClient addStorePlaylistWithGlobalID:completionHandler:]_block_invoke.31
- ___64-[ICCloudClient loadJaliscoUpdateProgressWithCompletionHandler:]_block_invoke.123
- ___64-[ICCloudClient loadScreenshotInfoForSagaIDs:completionHandler:]_block_invoke.103
- ___64-[ICCloudClient sdk_addStoreItemWithOpaqueID:completionHandler:]_block_invoke.30
- ___64-[ICCloudClientCloudService _xpcConnectionWithListenerEndpoint:]_block_invoke.164
- ___65-[ICCloudClient disableCloudLibraryWithReason:completionHandler:]_block_invoke.63
- ___65-[ICCloudClient loadIsSagaUpdateInProgressWithCompletionHandler:]_block_invoke.119
- ___66-[ICCloudClient updateJaliscoLibraryWithReason:completionHandler:]_block_invoke.65
- ___67-[ICCloudClient addStoreItemWithAdamID:referral:completionHandler:]_block_invoke.29
- ___67-[ICCloudClient hideItemsWithPurchaseHistoryIDs:completionHandler:]_block_invoke.34
- ___67-[ICCloudClient importContainerArtworkForSagaID:completionHandler:]_block_invoke.85
- ___68-[ICCloudClient loadIsJaliscoUpdateInProgressWithCompletionHandler:]_block_invoke.120
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.115
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.118
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.83
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke.87
- ___69-[ICURLBagProvider _fetchBagForRequestContext:withCompletionHandler:]_block_invoke_2.120
- ___70-[ICCloudClient loadArtworkInfoForContainerSagaIDs:completionHandler:]_block_invoke.101
- ___72-[ICCloudClient importArtistHeroImageForPersistentID:completionHandler:]_block_invoke.89
- ___72-[ICCloudClient importScreenshotForPurchaseHistoryID:completionHandler:]_block_invoke.82
- ___72-[ICCloudClient loadArtworkInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.94
- ___72-[ICCloudClient loadLastKnownEnableICMLErrorStatusWithCompletionHander:]_block_invoke.79
- ___73-[ICCloudClient importItemArtworkForPurchaseHistoryID:completionHandler:]_block_invoke.81
- ___75-[ICCloudClient loadScreenshotInfoForPurchaseHistoryIDs:completionHandler:]_block_invoke.97
- ___75-[ICCloudClient setAlbumProperties:forAlbumPersistentID:completionHandler:]_block_invoke.149
- ___76-[ICCloudClient uploadArtworkForPlaylistWithPersistentID:completionHandler:]_block_invoke.26
- ___77-[ICCloudClient importAlbumArtistHeroImageForPersistentID:completionHandler:]_block_invoke.90
- ___79-[ICCloudClient importSubscriptionScreenshotForPersistentID:completionHandler:]_block_invoke.87
- ___79-[ICCloudClient resetInvitationURLForCollaborationWithPersistentID:completion:]_block_invoke.59
- ___80-[ICCloudClient addItemWithSagaID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.20
- ___80-[ICCloudClient importSubscriptionItemArtworkForPersistentID:completionHandler:]_block_invoke.86
- ___80-[ICCloudClient joinCollaborationWithGlobalPlaylistID:invitationURL:completion:]_block_invoke.53
- ___82-[ICCloudClient favoritePlaylistWithPersistentID:globalID:time:completionHandler:]_block_invoke.39
- ___82-[ICCloudClient loadScreenshotInfoForSubscriptionPersistentIDs:completionHandler:]_block_invoke.107
- ___82-[ICCloudClient removeCollaborators:fromCollaborationWithPersistentID:completion:]_block_invoke.57
- ___83-[ICCloudClient loadArtworkInfoForSubscriptionItemPersistentIDs:completionHandler:]_block_invoke.105
- ___84-[ICCloudClient editCollaborationWithPersistentID:properties:trackEdits:completion:]_block_invoke.51
- ___84-[ICCloudClient sdk_addItemWithSagaID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.23
- ___85-[ICCloudClient favoriteAlbumWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.43
- ___85-[ICCloudClient importSubscriptionContainerArtworkForPersistentID:completionHandler:]_block_invoke.88
- ___86-[ICCloudClient favoriteArtistWithPersistentID:cloudLibraryID:time:completionHandler:]_block_invoke.45
- ___87-[ICCloudClient createPlaylistWithPersistentID:properties:trackList:completionHandler:]_block_invoke.14
- ___87-[ICCloudClient setAlbumArtistProperties:forAlbumArtistPersistentID:completionHandler:]_block_invoke.153
- ___88-[ICCloudClient beginCollaborationUsingPlaylistWithPersistentID:sharingMode:completion:]_block_invoke.47
- ___88-[ICCloudClient loadArtworkInfoForSubscriptionContainerPersistentIDs:completionHandler:]_block_invoke.109
- ___89-[ICCloudClient favoriteEntityWithPersistentID:sagaID:entityType:time:completionHandler:]_block_invoke.41
- ___90-[ICCloudClient favoriteEntityWithPersistentID:storeID:entityType:time:completionHandler:]_block_invoke.37
- ___90-[ICCloudClient setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:]_block_invoke
- ___90-[ICCloudClient setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:]_block_invoke.151
- ___90-[ICCloudClient setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:]_block_invoke.152
- ___90-[ICCloudClient setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:]_block_invoke_2
- ___91-[ICCloudClient sdk_addStoreItemWithOpaqueID:toPlaylistWithPersistentID:completionHandler:]_block_invoke.21
- ___91-[ICCloudClient sdk_createPlaylistWithPersistentID:properties:tracklist:completionHandler:]_block_invoke.16
- ___91-[ICCloudClient setPlaylistProperties:trackList:forPlaylistPersistentID:completionHandler:]_block_invoke.17
- ___92-[ICStoreURLRequest buildStoreURLRequestWithURLRequest:builderProperties:completionHandler:]_block_invoke.247
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.46
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.48
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.49
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.56
- ___92-[ICURLBagProvider getBagAndURLMetricsForRequestContext:forceRefetch:withCompletionHandler:]_block_invoke.58
- ___94-[ICCloudClient addStoreItemWithAdamID:referral:toPlaylistWithPersistentID:completionHandler:]_block_invoke.19
- ___95-[ICCloudClient sdk_setPlaylistProperties:trackList:forPlaylistPersistentID:completionHandler:]_block_invoke.18
- ___97-[ICCloudClient handleAutomaticDownloadPreferenceChangedForMediaKindMusic:withCompletionHandler:]_block_invoke.162
- ___97-[ICCloudClient updateSubscribedPlaylistsWithSagaIDs:ignoreMinRefreshInterval:completionHandler:]_block_invoke.27
- ___Block_byref_object_copy_.10212
- ___Block_byref_object_copy_.10511
- ___Block_byref_object_copy_.10639
- ___Block_byref_object_copy_.1106
- ___Block_byref_object_copy_.12167
- ___Block_byref_object_copy_.13519
- ___Block_byref_object_copy_.14063
- ___Block_byref_object_copy_.14237
- ___Block_byref_object_copy_.14502
- ___Block_byref_object_copy_.14910
- ___Block_byref_object_copy_.16039
- ___Block_byref_object_copy_.16517
- ___Block_byref_object_copy_.16744
- ___Block_byref_object_copy_.18438
- ___Block_byref_object_copy_.18803
- ___Block_byref_object_copy_.19012
- ___Block_byref_object_copy_.19988
- ___Block_byref_object_copy_.20880
- ___Block_byref_object_copy_.22147
- ___Block_byref_object_copy_.22248
- ___Block_byref_object_copy_.24655
- ___Block_byref_object_copy_.25084
- ___Block_byref_object_copy_.25645
- ___Block_byref_object_copy_.26000
- ___Block_byref_object_copy_.26042
- ___Block_byref_object_copy_.26954
- ___Block_byref_object_copy_.27918
- ___Block_byref_object_copy_.28948
- ___Block_byref_object_copy_.29291
- ___Block_byref_object_copy_.30327
- ___Block_byref_object_copy_.31046
- ___Block_byref_object_copy_.31427
- ___Block_byref_object_copy_.31604
- ___Block_byref_object_copy_.31764
- ___Block_byref_object_copy_.32516
- ___Block_byref_object_copy_.34548
- ___Block_byref_object_copy_.34773
- ___Block_byref_object_copy_.34907
- ___Block_byref_object_copy_.35756
- ___Block_byref_object_copy_.35919
- ___Block_byref_object_copy_.3593
- ___Block_byref_object_copy_.36604
- ___Block_byref_object_copy_.36874
- ___Block_byref_object_copy_.37465
- ___Block_byref_object_copy_.37645
- ___Block_byref_object_copy_.37950
- ___Block_byref_object_copy_.38796
- ___Block_byref_object_copy_.3943
- ___Block_byref_object_copy_.4082
- ___Block_byref_object_copy_.4115
- ___Block_byref_object_copy_.4982
- ___Block_byref_object_copy_.5140
- ___Block_byref_object_copy_.5232
- ___Block_byref_object_copy_.5934
- ___Block_byref_object_copy_.6367
- ___Block_byref_object_copy_.6479
- ___Block_byref_object_copy_.6981
- ___Block_byref_object_copy_.9291
- ___Block_byref_object_copy_.9396
- ___Block_byref_object_dispose_.10213
- ___Block_byref_object_dispose_.10512
- ___Block_byref_object_dispose_.10640
- ___Block_byref_object_dispose_.1107
- ___Block_byref_object_dispose_.12168
- ___Block_byref_object_dispose_.13520
- ___Block_byref_object_dispose_.14064
- ___Block_byref_object_dispose_.14238
- ___Block_byref_object_dispose_.14503
- ___Block_byref_object_dispose_.14911
- ___Block_byref_object_dispose_.16040
- ___Block_byref_object_dispose_.16518
- ___Block_byref_object_dispose_.16745
- ___Block_byref_object_dispose_.18439
- ___Block_byref_object_dispose_.18804
- ___Block_byref_object_dispose_.19013
- ___Block_byref_object_dispose_.19989
- ___Block_byref_object_dispose_.20881
- ___Block_byref_object_dispose_.22148
- ___Block_byref_object_dispose_.22249
- ___Block_byref_object_dispose_.24656
- ___Block_byref_object_dispose_.25085
- ___Block_byref_object_dispose_.25646
- ___Block_byref_object_dispose_.26001
- ___Block_byref_object_dispose_.26043
- ___Block_byref_object_dispose_.26955
- ___Block_byref_object_dispose_.27919
- ___Block_byref_object_dispose_.28949
- ___Block_byref_object_dispose_.29292
- ___Block_byref_object_dispose_.30328
- ___Block_byref_object_dispose_.31047
- ___Block_byref_object_dispose_.31428
- ___Block_byref_object_dispose_.31605
- ___Block_byref_object_dispose_.31765
- ___Block_byref_object_dispose_.32517
- ___Block_byref_object_dispose_.34549
- ___Block_byref_object_dispose_.34774
- ___Block_byref_object_dispose_.34908
- ___Block_byref_object_dispose_.35757
- ___Block_byref_object_dispose_.35920
- ___Block_byref_object_dispose_.3594
- ___Block_byref_object_dispose_.36605
- ___Block_byref_object_dispose_.36875
- ___Block_byref_object_dispose_.37466
- ___Block_byref_object_dispose_.37646
- ___Block_byref_object_dispose_.37951
- ___Block_byref_object_dispose_.38797
- ___Block_byref_object_dispose_.3944
- ___Block_byref_object_dispose_.4083
- ___Block_byref_object_dispose_.4116
- ___Block_byref_object_dispose_.4983
- ___Block_byref_object_dispose_.5141
- ___Block_byref_object_dispose_.5233
- ___Block_byref_object_dispose_.5935
- ___Block_byref_object_dispose_.6368
- ___Block_byref_object_dispose_.6480
- ___Block_byref_object_dispose_.6982
- ___Block_byref_object_dispose_.9292
- ___Block_byref_object_dispose_.9397
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"ICURLBag"16^B24ls32l8
- ___block_descriptor_64_e8_32s40s48s56s_e68_v32?0"ICURLBag"8"ICURLAggregatedPerformanceMetrics"16"NSError"24ls32l8s40l8s48l8s56l8
- ___block_literal_global.10.25655
- ___block_literal_global.10304
- ___block_literal_global.11253
- ___block_literal_global.11692
- ___block_literal_global.12.24449
- ___block_literal_global.12.25653
- ___block_literal_global.12280
- ___block_literal_global.128
- ___block_literal_global.12923
- ___block_literal_global.12965
- ___block_literal_global.13.37959
- ___block_literal_global.130
- ___block_literal_global.133
- ___block_literal_global.135
- ___block_literal_global.13550
- ___block_literal_global.138
- ___block_literal_global.140
- ___block_literal_global.143
- ___block_literal_global.1443
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.148
- ___block_literal_global.14949
- ___block_literal_global.156
- ___block_literal_global.16441
- ___block_literal_global.167
- ___block_literal_global.169.9686
- ___block_literal_global.171
- ___block_literal_global.173.10298
- ___block_literal_global.17473
- ___block_literal_global.175
- ___block_literal_global.17878
- ___block_literal_global.18.25651
- ___block_literal_global.18.34606
- ___block_literal_global.18270
- ___block_literal_global.18490
- ___block_literal_global.18704
- ___block_literal_global.19.25538
- ___block_literal_global.19866
- ___block_literal_global.21523
- ___block_literal_global.22049
- ___block_literal_global.23601
- ___block_literal_global.23725
- ___block_literal_global.24448
- ___block_literal_global.24642
- ___block_literal_global.25152
- ___block_literal_global.25317
- ___block_literal_global.25520
- ___block_literal_global.25661
- ___block_literal_global.26991
- ___block_literal_global.27507
- ___block_literal_global.28317
- ___block_literal_global.28657
- ___block_literal_global.28963
- ___block_literal_global.29113
- ___block_literal_global.3.14947
- ___block_literal_global.3.17480
- ___block_literal_global.30102
- ___block_literal_global.30649
- ___block_literal_global.30709
- ___block_literal_global.30933
- ___block_literal_global.31501
- ___block_literal_global.32112
- ___block_literal_global.32553
- ___block_literal_global.33669
- ___block_literal_global.3406
- ___block_literal_global.34191
- ___block_literal_global.34629
- ___block_literal_global.35697
- ___block_literal_global.3612
- ___block_literal_global.36617
- ___block_literal_global.36984
- ___block_literal_global.37081
- ___block_literal_global.37789
- ___block_literal_global.37969
- ___block_literal_global.3876
- ___block_literal_global.38907
- ___block_literal_global.39046
- ___block_literal_global.39176
- ___block_literal_global.39871
- ___block_literal_global.40062
- ___block_literal_global.40396
- ___block_literal_global.4133
- ___block_literal_global.4192
- ___block_literal_global.4312
- ___block_literal_global.47.30749
- ___block_literal_global.52.28920
- ___block_literal_global.52.30752
- ___block_literal_global.5350
- ___block_literal_global.5814
- ___block_literal_global.6.25659
- ___block_literal_global.63
- ___block_literal_global.6554
- ___block_literal_global.6649
- ___block_literal_global.68.30605
- ___block_literal_global.6866
- ___block_literal_global.7029
- ___block_literal_global.7261
- ___block_literal_global.76.30772
- ___block_literal_global.7980
- ___block_literal_global.8.25657
- ___block_literal_global.8064
- ___block_literal_global.8997
- ___block_literal_global.9802
- __unnamed_array_storage.30751
- __unnamed_array_storage.40288
- __unnamed_array_storage.96.40289
- _objc_msgSend$_cacheFilePath
- _objc_msgSend$_saveCache
- _objc_msgSend$setAlbumProperties:forAlbumPersistentID:cloudLibraryID:configuration:completion:
- _sharedCache.sOnceToken.29112
- _sharedCache.sSharedCache.29114
- _sharedController.sOnceToken.34628
- _sharedController.sOnceToken.37968
- _sharedController.sSharedController.34630
- _sharedController.sSharedController.37970
- _sharedManager.sOnceToken.18703
- _sharedManager.sOnceToken.27506
- _sharedManager.sSharedManager.18705
- _sharedManager.sSharedManager.27508
- _sharedMonitor.sOnceToken.17877
- _sharedMonitor.sOnceToken.38906
- _sharedMonitor.sSharedMonitor.17879
- _sharedMonitor.sSharedMonitor.38908
- _sharedProvider.sOnceToken.39175
- _sharedProvider.sSharedProvider.39177
CStrings:
+ "\x13\""
+ "%@/%@.plist"
+ "%{public}@ Cleanup excluding path: %{public}@"
+ "%{public}@ Could not load plist at path '%{public}@' error=%{public}@"
+ "%{public}@ Encountered error creating cache directory at %{public}@. error=%{public}@"
+ "%{public}@ Encountered error removing file at path %{public}@"
+ "%{public}@ Error reading file attributes at path %{public}@. error=%{public}@"
+ "%{public}@ Failed to create bag from cached data for key: %{public}@"
+ "%{public}@ Failed to create cache file at path %{public}@ error=%{public}@"
+ "%{public}@ Failed to load cache at path %{public}@"
+ "%{public}@ Failed to remove monoCache at path: %{public}@. error=%{public}@"
+ "%{public}@ Failed to write cache at path %{public}@ error=%{public}@"
+ "%{public}@ Loading bag cache from mono cache file '%{public}@'"
+ "%{public}@ Loading bag caches from '%{public}@'"
+ "%{public}@ Loading cached bags for keys '%{public}@'"
+ "%{public}@ Persisted cache at path %{public}@."
+ "%{public}@ Removed mono cache at path %{public}@"
+ "%{public}@ Removing stale cache at path: %{public}@"
+ "%{public}@ Retrieved persisted cache from disk for cache key: %{public}@"
+ "%{public}@ fetched new bag which expires in %fs (expiration time: %{time_t}zd, adjusted from %{time_t}zd)"
+ ".plist"
+ "<%@ %p: [ADD %lld %@/%@ %s %@]>"
+ "<%@ %p: [MOVE %@/%@ %s %@]>"
+ "@\"MSVLRUDictionary\""
+ "@48@0:8Q16@24@32@40"
+ "@48@0:8Q16@24@32q40"
+ "ICCloudClientCollaborationEditParamsItemPositionUUIDKey"
+ "ICFavoriteSongAddToLibraryBehaviorAlwaysAddToLibrary"
+ "ICFavoriteSongAddToLibraryBehaviorOnlyAddToPlaylist"
+ "ICFavoriteSongAddToLibraryBehaviorUndecided"
+ "ICStoreURLRequestParsedBodyInfoKey"
+ "Set cloud favorite-to-library behavior failed with error: %{public}@"
+ "Setting album properties %{public}@ for persistent ID %llu ..."
+ "T@\"NSString\",C,N,V_reactionString"
+ "T@\"NSString\",R,C,N,V_itemPositionUUID"
+ "TB,N,V_isStoreKeyServer"
+ "_cacheDirectoryPath"
+ "_cleanBagCacheExcludingPaths:"
+ "_isStoreKeyServer"
+ "_itemPositionUUID"
+ "_loadMonoCache"
+ "_loadPlistAtPath:"
+ "_persistBagToDisk:withKey:"
+ "attributesOfItemAtPath:error:"
+ "com.apple.itunescloudd.cloudFavoriteSongAddToLibraryBehaviorDidChangeNotification"
+ "createFileAtPath:contents:attributes:"
+ "initWithMaximumCapacity:"
+ "isStoreKeyServer"
+ "itemPositionUUID"
+ "newIdentifierString"
+ "paramsForAddingTrackWithAdamID:itemUUID:itemPositionUUID:afterReferencePositionUUD:"
+ "paramsForAddingTrackWithAdamID:itemUUID:itemPositionUUID:atPosition:"
+ "paramsForMovingTrackWithItemUUID:withNewItemPositionUUID:afterReferencePositionUUD:"
+ "paramsForMovingTrackWithItemUUID:withNewItemPositionUUID:toPosition:"
+ "paramsForUnsettingReaction:onTrackWithItemUUID:"
+ "plist"
+ "q24@?0@8@16"
+ "setAlbumEntityProperties:forAlbumPersistentID:completionHandler:"
+ "setAlbumEntityProperties:forAlbumPersistentID:configuration:completion:"
+ "setCloudFavoriteSongAddToLibraryBehavior:completionHandler:"
+ "setCloudFavoriteSongAddToLibraryBehavior:forConfiguration:completion:"
+ "setIsStoreKeyServer:"
+ "setReactionString:"
+ "stringByAppendingPathExtension:"
+ "stringByDeletingPathExtension"
- "\x12\""
- "%{public}@ Failed to create cache directory. err=%{public}@"
- "%{public}@ Failed to persist bag data. err=%{public}@"
- "%{public}@ Loading bag cache from file '%{public}@'"
- "%{public}@ Saving bag cache to file '%{public}@'. keys=%{public}@"
- "<%@ %p: [ADD %lld/%@ %s %@]>"
- "<%@ %p: [MOVE %@ %s %@]>"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16@24q32"
- "Setting album properties %{public}@ for persistent ID %llu, cloudLibraryID %{public}@ ..."
- "T@\"NSString\",R,C,N,V_reactionString"
- "_cacheFilePath"
- "_saveCache"
- "paramsForAddingTrackWithAdamID:itemUUID:afterReferencePositionUUD:"
- "paramsForAddingTrackWithAdamID:itemUUID:atPosition:"
- "paramsForMovingTrackWithItemUUID:afterReferencePositionUUD:"
- "paramsForMovingTrackWithItemUUID:toPosition:"
- "paramsForUnsettingReactionOnTrackWithItemUUID:"
- "setAlbumProperties:forAlbumPersistentID:cloudLibraryID:completionHandler:"
- "setAlbumProperties:forAlbumPersistentID:cloudLibraryID:configuration:completion:"
- "v32@?0@\"NSString\"8@\"ICURLBag\"16^B24"
- "v56@0:8@\"NSDictionary\"16q24@\"NSString\"32@\"ICConnectionConfiguration\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16q24@32@40@?48"

```
