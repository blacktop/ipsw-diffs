## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4023.110.8.0.0
-  __TEXT.__text: 0x281464
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x147e8
+4023.210.3.0.0
+  __TEXT.__text: 0x286040
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_methlist: 0x149d0
   __TEXT.__const: 0x1653c
-  __TEXT.__gcc_except_tab: 0x246c
-  __TEXT.__cstring: 0x1590c
-  __TEXT.__oslogstring: 0x1c333
+  __TEXT.__gcc_except_tab: 0x2514
+  __TEXT.__cstring: 0x15cb4
+  __TEXT.__oslogstring: 0x1c65b
   __TEXT.__ustring: 0x8e
-  __TEXT.__dlopen_cstrs: 0x376
-  __TEXT.__unwind_info: 0x6140
+  __TEXT.__dlopen_cstrs: 0x3de
+  __TEXT.__unwind_info: 0x6204
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x394d
-  __TEXT.__objc_methname: 0x3108a
-  __TEXT.__objc_methtype: 0x71fa
-  __TEXT.__objc_stubs: 0x19aa0
+  __TEXT.__objc_classname: 0x39ac
+  __TEXT.__objc_methname: 0x3173a
+  __TEXT.__objc_methtype: 0x73c2
+  __TEXT.__objc_stubs: 0x19dc0
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x7d18
-  __DATA_CONST.__objc_classlist: 0xd10
+  __DATA_CONST.__const: 0x7df0
+  __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x26fe0
-  __DATA_CONST.__objc_selrefs: 0x91b8
+  __DATA_CONST.__objc_const: 0x27388
+  __DATA_CONST.__objc_selrefs: 0x92c8
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__const: 0x10580
-  __AUTH_CONST.__cfstring: 0x16ec0
-  __AUTH_CONST.__objc_intobj: 0x3d8
-  __AUTH_CONST.__objc_const: 0xa2a8
+  __AUTH_CONST.__cfstring: 0x171a0
+  __AUTH_CONST.__objc_intobj: 0x408
+  __AUTH_CONST.__objc_const: 0xa380
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0xa80
-  __AUTH.__objc_data: 0x4ba0
+  __AUTH_CONST.__auth_got: 0xa90
+  __AUTH.__objc_data: 0x4c40
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0xf10
-  __DATA.__objc_superrefs: 0xb40
-  __DATA.__objc_ivar: 0x21d4
-  __DATA.__data: 0x24f8
+  __DATA.__objc_classrefs: 0xf20
+  __DATA.__objc_superrefs: 0xb50
+  __DATA.__objc_ivar: 0x2204
+  __DATA.__data: 0x24d0
   __DATA.__common: 0xa8c
-  __DATA.__bss: 0x248
+  __DATA.__bss: 0x278
   __DATA_DIRTY.__objc_data: 0x3700
   __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0x400

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 055ED7EF-0CDD-3B7B-BC58-140946A6165F
-  Functions: 9518
-  Symbols:   29709
-  CStrings:  16619
+  UUID: 32837148-96FA-3D72-8886-74A1F98CD2AA
+  Functions: 9574
+  Symbols:   29890
+  CStrings:  16744
 
Symbols:
+ +[ICAuthServiceClientTokenProviderDebugConfiguration supportsSecureCoding]
+ +[ICCloudClientCollaborationEditParams paramsForUnsettingReactionOnTrackWithItemUUID:]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration .cxx_destruct]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration allDSIDsShouldError]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration allDSIDsShouldSucceed]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration commandOption]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration encodeWithCoder:]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration errorDSIDs]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration initWithCoder:]
+ -[ICAuthServiceClientTokenProviderDebugConfiguration initWithCommandOption:allDSIDsShouldError:allDSIDsShouldSucceed:errorDSIDs:]
+ -[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]
+ -[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]
+ -[ICCloudContentTasteRequestListener setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:]
+ -[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:]
+ -[ICContentKeySession _isPrefetchKey:]
+ -[ICContentKeySessionPrefetchKeyConfiguration .cxx_destruct]
+ -[ICContentKeySessionPrefetchKeyConfiguration _fetchWithRequestContext:]
+ -[ICContentKeySessionPrefetchKeyConfiguration initWithRequestContext:]
+ -[ICContentKeySessionPrefetchKeyConfiguration keyCertificateURL]
+ -[ICContentKeySessionPrefetchKeyConfiguration keyIdentifiers]
+ -[ICContentKeySessionPrefetchKeyConfiguration keyServerURL]
+ -[ICDefaults addDebugConfiguration:]
+ -[ICDefaults clearAllPresets]
+ -[ICDefaults clearShouldForceServerToUseDAAPDebugFeatures]
+ -[ICDefaults debugFetchConfiguration]
+ -[ICDefaults debugRefreshConfiguration]
+ -[ICDefaults prefetchKeyIdentifiers]
+ -[ICDefaults presetsFound]
+ -[ICDefaults setPrefetchKeyIdentifiers:]
+ -[ICDefaults shouldForceServerToUseDAAPDebugFeatureAlwaysBackoff]
+ -[ICDefaults shouldForceServerToUseDAAPDebugFeatureAlwaysPerformResetSync]
+ -[ICDefaults shouldForceServerToUseDAAPDebugFeature]
+ -[ICLibraryAuthServiceClientTokenProvider _checkTokenPresetsForDSID:forceRefresh:]
+ -[ICLibraryAuthServiceClientTokenProvider _devicePresetForConfiguration:withDSID:]
+ -[ICMutablePlayActivityEvent setCollaborativePlaylist:]
+ -[ICPlayActivityEvent isCollaborativePlaylist]
+ -[ICPrivacyInfo preflightDisclosureRequiredForBundleIdentifier:]
+ -[ICPrivacyInfo preflightDisclosureRequiredForMusic]
+ -[ICPushNotificationsRegisterAPNSTokenRequest _registerAPNSToken]
+ GCC_except_table2674
+ GCC_except_table2719
+ GCC_except_table2865
+ GCC_except_table2882
+ GCC_except_table2892
+ GCC_except_table2916
+ GCC_except_table2921
+ GCC_except_table2932
+ GCC_except_table3030
+ GCC_except_table3298
+ GCC_except_table3302
+ GCC_except_table3305
+ GCC_except_table3320
+ GCC_except_table3331
+ GCC_except_table3350
+ GCC_except_table3390
+ GCC_except_table3404
+ GCC_except_table3517
+ GCC_except_table3675
+ GCC_except_table3836
+ GCC_except_table3878
+ GCC_except_table3966
+ GCC_except_table3974
+ GCC_except_table3976
+ GCC_except_table3978
+ GCC_except_table3980
+ GCC_except_table3982
+ GCC_except_table3986
+ GCC_except_table3993
+ GCC_except_table3997
+ GCC_except_table4012
+ GCC_except_table4015
+ GCC_except_table4188
+ GCC_except_table4240
+ GCC_except_table4244
+ GCC_except_table4247
+ GCC_except_table4252
+ GCC_except_table4316
+ GCC_except_table4358
+ GCC_except_table4362
+ GCC_except_table4364
+ GCC_except_table4484
+ GCC_except_table4570
+ GCC_except_table4650
+ GCC_except_table4715
+ GCC_except_table4796
+ GCC_except_table4959
+ GCC_except_table5199
+ GCC_except_table5295
+ GCC_except_table5374
+ GCC_except_table5375
+ GCC_except_table5448
+ GCC_except_table5464
+ GCC_except_table5741
+ GCC_except_table5748
+ GCC_except_table5756
+ GCC_except_table5767
+ GCC_except_table5769
+ GCC_except_table5774
+ GCC_except_table5781
+ GCC_except_table5791
+ GCC_except_table5806
+ GCC_except_table5814
+ GCC_except_table5823
+ GCC_except_table5832
+ GCC_except_table5865
+ GCC_except_table5879
+ GCC_except_table5888
+ GCC_except_table5895
+ GCC_except_table5896
+ GCC_except_table5955
+ GCC_except_table5958
+ GCC_except_table5993
+ GCC_except_table5998
+ GCC_except_table6004
+ GCC_except_table6007
+ GCC_except_table6010
+ GCC_except_table6013
+ GCC_except_table6016
+ GCC_except_table6019
+ GCC_except_table6022
+ GCC_except_table6025
+ GCC_except_table6028
+ GCC_except_table6031
+ GCC_except_table6034
+ GCC_except_table6134
+ GCC_except_table6147
+ GCC_except_table6339
+ GCC_except_table6346
+ GCC_except_table6520
+ GCC_except_table6524
+ GCC_except_table6526
+ GCC_except_table6549
+ GCC_except_table6595
+ GCC_except_table6782
+ GCC_except_table6915
+ GCC_except_table7056
+ GCC_except_table7069
+ GCC_except_table7101
+ GCC_except_table7145
+ GCC_except_table7215
+ GCC_except_table7218
+ GCC_except_table7227
+ GCC_except_table7234
+ GCC_except_table7275
+ GCC_except_table7294
+ GCC_except_table7327
+ GCC_except_table7385
+ GCC_except_table7386
+ GCC_except_table7399
+ GCC_except_table7816
+ GCC_except_table7822
+ GCC_except_table7848
+ GCC_except_table7859
+ GCC_except_table7864
+ GCC_except_table7899
+ GCC_except_table7902
+ GCC_except_table7964
+ GCC_except_table8009
+ GCC_except_table8054
+ GCC_except_table8079
+ GCC_except_table8084
+ GCC_except_table8086
+ GCC_except_table8088
+ GCC_except_table8120
+ GCC_except_table8263
+ GCC_except_table8271
+ GCC_except_table8276
+ GCC_except_table8291
+ GCC_except_table8299
+ GCC_except_table8343
+ GCC_except_table8477
+ GCC_except_table8481
+ GCC_except_table8483
+ GCC_except_table8520
+ GCC_except_table8523
+ GCC_except_table8530
+ GCC_except_table8533
+ GCC_except_table8744
+ GCC_except_table8748
+ GCC_except_table8788
+ _ICStoreHTTPHeaderKeyXDAAPClientDebugFeatures
+ _ICStoreHTTPHeaderKeyXDAAPClientFeaturesVersion
+ _ICStoreHTTPHeaderKeyXDAAPSupportedFeatures
+ _ICStoreURLRequestHTTPStatusCodeUserInfoKey
+ _MSVFastHexStringFromBytes.hexCharacters.40577
+ _OBJC_CLASS_$_ICAuthServiceClientTokenProviderDebugConfiguration
+ _OBJC_CLASS_$_ICContentKeySessionPrefetchKeyConfiguration
+ _OBJC_IVAR_$_ICAuthServiceClientTokenProviderDebugConfiguration._allDSIDsShouldError
+ _OBJC_IVAR_$_ICAuthServiceClientTokenProviderDebugConfiguration._allDSIDsShouldSucceed
+ _OBJC_IVAR_$_ICAuthServiceClientTokenProviderDebugConfiguration._commandOption
+ _OBJC_IVAR_$_ICAuthServiceClientTokenProviderDebugConfiguration._errorDSIDs
+ _OBJC_IVAR_$_ICContentKeySession._prefetchKeyConfiguration
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._group
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._initWithDefaultKeyIdentifiers
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._keyCertificateURL
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._keyIdentifiers
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._keyServerURL
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._queue
+ _OBJC_IVAR_$_ICContentKeySessionPrefetchKeyConfiguration._timeout
+ _OBJC_IVAR_$_ICPAPlayActivityEvent._isCollaborativePlaylist
+ _OBJC_IVAR_$_ICPlayActivityEvent._collaborativePlaylist
+ _OBJC_IVAR_$_ICPrivacyInfo._preflightManager
+ _OBJC_METACLASS_$_ICAuthServiceClientTokenProviderDebugConfiguration
+ _OBJC_METACLASS_$_ICContentKeySessionPrefetchKeyConfiguration
+ _PrivacyDisclosureCoreLibraryCore.frameworkLibrary
+ __MSV_XXH_XXH32_update.11514
+ __MSV_XXH_XXH32_update.17234
+ __MSV_XXH_XXH32_update.20159
+ __MSV_XXH_XXH32_update.40566
+ __MSV_XXH_XXH64_digest.17354
+ __MSV_XXH_XXH64_update.11515
+ __MSV_XXH_XXH64_update.17235
+ __MSV_XXH_XXH64_update.20160
+ __MSV_XXH_XXH64_update.40567
+ __OBJC_$_CLASS_METHODS_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_$_CLASS_PROP_LIST_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_$_INSTANCE_METHODS_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_$_INSTANCE_METHODS_ICContentKeySessionPrefetchKeyConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ICContentKeySessionPrefetchKeyConfiguration
+ __OBJC_$_PROP_LIST_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_$_PROP_LIST_ICContentKeySessionPrefetchKeyConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_CLASS_RO_$_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_CLASS_RO_$_ICContentKeySessionPrefetchKeyConfiguration
+ __OBJC_METACLASS_RO_$_ICAuthServiceClientTokenProviderDebugConfiguration
+ __OBJC_METACLASS_RO_$_ICContentKeySessionPrefetchKeyConfiguration
+ ___106-[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:configuration:withCompletionHandler:]_block_invoke.7
+ ___107-[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:configuration:withCompletionHandler:]_block_invoke.9
+ ___110-[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:configuration:withCompletionHandler:]_block_invoke.5
+ ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.109
+ ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.111
+ ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.112
+ ___129-[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke
+ ___129-[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke.8
+ ___129-[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke_2
+ ___129-[ICCloudContentTasteRequestListener updateContentTasteForMediaItemsAndInvalidateLocalCache:configuration:withCompletionHandler:]_block_invoke.11
+ ___130-[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke
+ ___130-[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke.10
+ ___130-[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke_2
+ ___133-[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke
+ ___133-[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke.6
+ ___133-[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke_2
+ ___142-[ICCloudContentTasteRequestListener setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke
+ ___142-[ICCloudContentTasteRequestListener setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke.4
+ ___142-[ICCloudContentTasteRequestListener setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:]_block_invoke_2
+ ___47-[ICContentKeySession _scheduleKeyRefreshTimer]_block_invoke.102
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.187
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.188
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.190
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.206
+ ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.208
+ ___61-[ICContentKeySessionPrefetchKeyConfiguration keyIdentifiers]_block_invoke
+ ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.178
+ ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.179
+ ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.180
+ ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.181
+ ___65-[ICPushNotificationsRegisterAPNSTokenRequest _registerAPNSToken]_block_invoke
+ ___65-[ICPushNotificationsRegisterAPNSTokenRequest _registerAPNSToken]_block_invoke.37
+ ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.78
+ ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.81
+ ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.82
+ ___72-[ICContentKeySessionPrefetchKeyConfiguration _fetchWithRequestContext:]_block_invoke
+ ___72-[ICContentKeySessionPrefetchKeyConfiguration _fetchWithRequestContext:]_block_invoke.13
+ ___72-[ICContentKeySessionPrefetchKeyConfiguration _fetchWithRequestContext:]_block_invoke_2
+ ___73-[ICCloudContentTasteRequestListener _setupContentTasteServiceConnection]_block_invoke.82
+ ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.191
+ ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.194
+ ___78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.198
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.29
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.40
+ ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke_2.37
+ ___86-[ICStoreURLResponseHandler processCompletedResponse:toRequest:withCompletionHandler:]_block_invoke.45
+ ___86-[ICStoreURLResponseHandler processCompletedResponse:toRequest:withCompletionHandler:]_block_invoke.48
+ ___92-[ICStoreURLRequest buildStoreURLRequestWithURLRequest:builderProperties:completionHandler:]_block_invoke.247
+ ___Block_byref_object_copy_.10212
+ ___Block_byref_object_copy_.10511
+ ___Block_byref_object_copy_.10639
+ ___Block_byref_object_copy_.12167
+ ___Block_byref_object_copy_.13519
+ ___Block_byref_object_copy_.14063
+ ___Block_byref_object_copy_.14237
+ ___Block_byref_object_copy_.14502
+ ___Block_byref_object_copy_.14910
+ ___Block_byref_object_copy_.16039
+ ___Block_byref_object_copy_.16517
+ ___Block_byref_object_copy_.16744
+ ___Block_byref_object_copy_.18438
+ ___Block_byref_object_copy_.18803
+ ___Block_byref_object_copy_.19012
+ ___Block_byref_object_copy_.19988
+ ___Block_byref_object_copy_.20880
+ ___Block_byref_object_copy_.22147
+ ___Block_byref_object_copy_.22248
+ ___Block_byref_object_copy_.24655
+ ___Block_byref_object_copy_.25084
+ ___Block_byref_object_copy_.25645
+ ___Block_byref_object_copy_.26000
+ ___Block_byref_object_copy_.26042
+ ___Block_byref_object_copy_.26954
+ ___Block_byref_object_copy_.27918
+ ___Block_byref_object_copy_.28948
+ ___Block_byref_object_copy_.29291
+ ___Block_byref_object_copy_.30327
+ ___Block_byref_object_copy_.31046
+ ___Block_byref_object_copy_.31427
+ ___Block_byref_object_copy_.31604
+ ___Block_byref_object_copy_.31764
+ ___Block_byref_object_copy_.32516
+ ___Block_byref_object_copy_.34548
+ ___Block_byref_object_copy_.34773
+ ___Block_byref_object_copy_.34907
+ ___Block_byref_object_copy_.35756
+ ___Block_byref_object_copy_.35919
+ ___Block_byref_object_copy_.36604
+ ___Block_byref_object_copy_.36874
+ ___Block_byref_object_copy_.37465
+ ___Block_byref_object_copy_.37645
+ ___Block_byref_object_copy_.37950
+ ___Block_byref_object_copy_.38796
+ ___Block_byref_object_copy_.9291
+ ___Block_byref_object_copy_.9396
+ ___Block_byref_object_dispose_.10213
+ ___Block_byref_object_dispose_.10512
+ ___Block_byref_object_dispose_.10640
+ ___Block_byref_object_dispose_.12168
+ ___Block_byref_object_dispose_.13520
+ ___Block_byref_object_dispose_.14064
+ ___Block_byref_object_dispose_.14238
+ ___Block_byref_object_dispose_.14503
+ ___Block_byref_object_dispose_.14911
+ ___Block_byref_object_dispose_.16040
+ ___Block_byref_object_dispose_.16518
+ ___Block_byref_object_dispose_.16745
+ ___Block_byref_object_dispose_.18439
+ ___Block_byref_object_dispose_.18804
+ ___Block_byref_object_dispose_.19013
+ ___Block_byref_object_dispose_.19989
+ ___Block_byref_object_dispose_.20881
+ ___Block_byref_object_dispose_.22148
+ ___Block_byref_object_dispose_.22249
+ ___Block_byref_object_dispose_.24656
+ ___Block_byref_object_dispose_.25085
+ ___Block_byref_object_dispose_.25646
+ ___Block_byref_object_dispose_.26001
+ ___Block_byref_object_dispose_.26043
+ ___Block_byref_object_dispose_.26955
+ ___Block_byref_object_dispose_.27919
+ ___Block_byref_object_dispose_.28949
+ ___Block_byref_object_dispose_.29292
+ ___Block_byref_object_dispose_.30328
+ ___Block_byref_object_dispose_.31047
+ ___Block_byref_object_dispose_.31428
+ ___Block_byref_object_dispose_.31605
+ ___Block_byref_object_dispose_.31765
+ ___Block_byref_object_dispose_.32517
+ ___Block_byref_object_dispose_.34549
+ ___Block_byref_object_dispose_.34774
+ ___Block_byref_object_dispose_.34908
+ ___Block_byref_object_dispose_.35757
+ ___Block_byref_object_dispose_.35920
+ ___Block_byref_object_dispose_.36605
+ ___Block_byref_object_dispose_.36875
+ ___Block_byref_object_dispose_.37466
+ ___Block_byref_object_dispose_.37646
+ ___Block_byref_object_dispose_.37951
+ ___Block_byref_object_dispose_.38797
+ ___Block_byref_object_dispose_.9292
+ ___Block_byref_object_dispose_.9397
+ ___PrivacyDisclosureCoreLibraryCore_block_invoke
+ ___block_descriptor_64_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_literal_global.10.25655
+ ___block_literal_global.10304
+ ___block_literal_global.107
+ ___block_literal_global.11253
+ ___block_literal_global.11692
+ ___block_literal_global.12.24449
+ ___block_literal_global.12.25653
+ ___block_literal_global.12280
+ ___block_literal_global.12923
+ ___block_literal_global.12965
+ ___block_literal_global.13.37959
+ ___block_literal_global.13550
+ ___block_literal_global.14949
+ ___block_literal_global.16441
+ ___block_literal_global.169.9686
+ ___block_literal_global.173.10298
+ ___block_literal_global.17473
+ ___block_literal_global.17878
+ ___block_literal_global.18.25651
+ ___block_literal_global.18.34606
+ ___block_literal_global.18270
+ ___block_literal_global.18490
+ ___block_literal_global.18704
+ ___block_literal_global.19.25538
+ ___block_literal_global.193
+ ___block_literal_global.19866
+ ___block_literal_global.21523
+ ___block_literal_global.22049
+ ___block_literal_global.23601
+ ___block_literal_global.23725
+ ___block_literal_global.24448
+ ___block_literal_global.24642
+ ___block_literal_global.25152
+ ___block_literal_global.25317
+ ___block_literal_global.25520
+ ___block_literal_global.25661
+ ___block_literal_global.26991
+ ___block_literal_global.27507
+ ___block_literal_global.28317
+ ___block_literal_global.28657
+ ___block_literal_global.28963
+ ___block_literal_global.29113
+ ___block_literal_global.3.14947
+ ___block_literal_global.3.17480
+ ___block_literal_global.30102
+ ___block_literal_global.30649
+ ___block_literal_global.30709
+ ___block_literal_global.30933
+ ___block_literal_global.31501
+ ___block_literal_global.32112
+ ___block_literal_global.32553
+ ___block_literal_global.33669
+ ___block_literal_global.34191
+ ___block_literal_global.34629
+ ___block_literal_global.35697
+ ___block_literal_global.36617
+ ___block_literal_global.36984
+ ___block_literal_global.37081
+ ___block_literal_global.37789
+ ___block_literal_global.37969
+ ___block_literal_global.38907
+ ___block_literal_global.39046
+ ___block_literal_global.39176
+ ___block_literal_global.39871
+ ___block_literal_global.40062
+ ___block_literal_global.40396
+ ___block_literal_global.47.30749
+ ___block_literal_global.52.28920
+ ___block_literal_global.52.30752
+ ___block_literal_global.6.25659
+ ___block_literal_global.68.30605
+ ___block_literal_global.76.30772
+ ___block_literal_global.8.25657
+ ___block_literal_global.81
+ ___block_literal_global.84
+ ___block_literal_global.8997
+ ___block_literal_global.9802
+ ___destructor_8_s0_s8
+ ___getPDCPreflightManagerClass_block_invoke
+ __unnamed_array_storage.30751
+ __unnamed_array_storage.40288
+ __unnamed_array_storage.96.40289
+ _audit_stringPrivacyDisclosureCore
+ _dispatch_group_wait
+ _getPDCPreflightManagerClass.softClass
+ _msv_dispatch_sync_on_queue
+ _objc_msgSend$_checkTokenPresetsForDSID:forceRefresh:
+ _objc_msgSend$_devicePresetForConfiguration:withDSID:
+ _objc_msgSend$_fetchWithRequestContext:
+ _objc_msgSend$_isPrefetchKey:
+ _objc_msgSend$_registerAPNSToken
+ _objc_msgSend$allDSIDsShouldError
+ _objc_msgSend$allDSIDsShouldSucceed
+ _objc_msgSend$commandOption
+ _objc_msgSend$debugFetchConfiguration
+ _objc_msgSend$debugRefreshConfiguration
+ _objc_msgSend$errorDSIDs
+ _objc_msgSend$initWithTargetQueue:
+ _objc_msgSend$isCollaborativePlaylist
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$keyIdentifiers
+ _objc_msgSend$prefetchKeyIdentifiers
+ _objc_msgSend$preflightDisclosureRequiredForBundleIdentifier:
+ _objc_msgSend$presetsFound
+ _objc_msgSend$requiresPreflightForApplicationRecord:
+ _objc_msgSend$setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:
+ _objc_msgSend$setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:
+ _objc_msgSend$setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:
+ _objc_msgSend$setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:
+ _objc_msgSend$setPrefetchKeyIdentifiers:
+ _sharedCache.sOnceToken.29112
+ _sharedCache.sSharedCache.29114
+ _sharedController.sOnceToken.34628
+ _sharedController.sOnceToken.37968
+ _sharedController.sSharedController.34630
+ _sharedController.sSharedController.37970
+ _sharedManager.sOnceToken.18703
+ _sharedManager.sOnceToken.27506
+ _sharedManager.sSharedManager.18705
+ _sharedManager.sSharedManager.27508
+ _sharedMonitor.sOnceToken.17877
+ _sharedMonitor.sOnceToken.38906
+ _sharedMonitor.sSharedMonitor.17879
+ _sharedMonitor.sSharedMonitor.38908
+ _sharedProvider.sOnceToken.39175
+ _sharedProvider.sSharedProvider.39177
- +[ICCloudClientCollaborationEditParams paramsForUnsettingReaction:onTrackWithItemUUID:]
- GCC_except_table2673
- GCC_except_table2718
- GCC_except_table2864
- GCC_except_table2881
- GCC_except_table2891
- GCC_except_table2915
- GCC_except_table2920
- GCC_except_table2931
- GCC_except_table3029
- GCC_except_table3297
- GCC_except_table3301
- GCC_except_table3304
- GCC_except_table3319
- GCC_except_table3330
- GCC_except_table3349
- GCC_except_table3389
- GCC_except_table3403
- GCC_except_table3516
- GCC_except_table3674
- GCC_except_table3835
- GCC_except_table3877
- GCC_except_table3965
- GCC_except_table3973
- GCC_except_table3975
- GCC_except_table3977
- GCC_except_table3979
- GCC_except_table3981
- GCC_except_table3985
- GCC_except_table3992
- GCC_except_table3996
- GCC_except_table4011
- GCC_except_table4014
- GCC_except_table4187
- GCC_except_table4239
- GCC_except_table4243
- GCC_except_table4246
- GCC_except_table4251
- GCC_except_table4315
- GCC_except_table4357
- GCC_except_table4361
- GCC_except_table4363
- GCC_except_table4483
- GCC_except_table4569
- GCC_except_table4649
- GCC_except_table4714
- GCC_except_table4795
- GCC_except_table4958
- GCC_except_table5196
- GCC_except_table5292
- GCC_except_table5371
- GCC_except_table5372
- GCC_except_table5445
- GCC_except_table5461
- GCC_except_table5738
- GCC_except_table5745
- GCC_except_table5753
- GCC_except_table5768
- GCC_except_table5775
- GCC_except_table5785
- GCC_except_table5800
- GCC_except_table5817
- GCC_except_table5826
- GCC_except_table5859
- GCC_except_table5878
- GCC_except_table5885
- GCC_except_table5886
- GCC_except_table5945
- GCC_except_table5948
- GCC_except_table5983
- GCC_except_table5988
- GCC_except_table5994
- GCC_except_table5997
- GCC_except_table6000
- GCC_except_table6003
- GCC_except_table6006
- GCC_except_table6009
- GCC_except_table6012
- GCC_except_table6015
- GCC_except_table6018
- GCC_except_table6021
- GCC_except_table6024
- GCC_except_table6124
- GCC_except_table6137
- GCC_except_table6309
- GCC_except_table6316
- GCC_except_table6490
- GCC_except_table6494
- GCC_except_table6496
- GCC_except_table6519
- GCC_except_table6565
- GCC_except_table6736
- GCC_except_table6869
- GCC_except_table6998
- GCC_except_table7012
- GCC_except_table7033
- GCC_except_table7046
- GCC_except_table7108
- GCC_except_table7160
- GCC_except_table7172
- GCC_except_table7179
- GCC_except_table7220
- GCC_except_table7239
- GCC_except_table7272
- GCC_except_table7330
- GCC_except_table7331
- GCC_except_table7344
- GCC_except_table7761
- GCC_except_table7767
- GCC_except_table7789
- GCC_except_table7793
- GCC_except_table7804
- GCC_except_table7809
- GCC_except_table7847
- GCC_except_table7909
- GCC_except_table7954
- GCC_except_table7999
- GCC_except_table8024
- GCC_except_table8029
- GCC_except_table8031
- GCC_except_table8033
- GCC_except_table8065
- GCC_except_table8208
- GCC_except_table8216
- GCC_except_table8221
- GCC_except_table8236
- GCC_except_table8244
- GCC_except_table8288
- GCC_except_table8422
- GCC_except_table8426
- GCC_except_table8428
- GCC_except_table8465
- GCC_except_table8468
- GCC_except_table8475
- GCC_except_table8478
- GCC_except_table8689
- GCC_except_table8693
- GCC_except_table8733
- _MSVFastHexStringFromBytes.hexCharacters.40373
- _OBJC_IVAR_$_ICContentKeySession._prefetchKeyCertificateURL
- _OBJC_IVAR_$_ICContentKeySession._prefetchKeyIdentifiers
- _OBJC_IVAR_$_ICContentKeySession._prefetchKeyServerURL
- __MSV_XXH_XXH32_update.11502
- __MSV_XXH_XXH32_update.17222
- __MSV_XXH_XXH32_update.20150
- __MSV_XXH_XXH32_update.40362
- __MSV_XXH_XXH64_digest.17342
- __MSV_XXH_XXH64_update.11503
- __MSV_XXH_XXH64_update.17223
- __MSV_XXH_XXH64_update.20151
- __MSV_XXH_XXH64_update.40363
- ___106-[ICCloudContentTasteRequestListener setContentTaste:forAlbumStoreID:configuration:withCompletionHandler:]_block_invoke.5
- ___107-[ICCloudContentTasteRequestListener setContentTaste:forArtistStoreID:configuration:withCompletionHandler:]_block_invoke.6
- ___110-[ICCloudContentTasteRequestListener setContentTaste:forPlaylistGlobalID:configuration:withCompletionHandler:]_block_invoke.4
- ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.76
- ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.78
- ___110-[ICContentKeySession _invalidateKeyWithIdentifier:forAdamID:offline:usingAccountDSID:keyData:withCompletion:]_block_invoke.79
- ___129-[ICCloudContentTasteRequestListener updateContentTasteForMediaItemsAndInvalidateLocalCache:configuration:withCompletionHandler:]_block_invoke.7
- ___47-[ICContentKeySession _scheduleKeyRefreshTimer]_block_invoke.69
- ___54-[ICPushNotificationsRegisterAPNSTokenRequest execute]_block_invoke
- ___54-[ICPushNotificationsRegisterAPNSTokenRequest execute]_block_invoke.27
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.175
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.176
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.178
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke.194
- ___58-[ICStoreURLRequest buildURLRequestWithCompletionHandler:]_block_invoke_2.196
- ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.153
- ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.154
- ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.155
- ___62-[ICLibraryAuthServiceClientTokenProvider _updateRefreshTimer]_block_invoke.156
- ___64-[ICContentKeySession initWithRequestContext:keyStore:delegate:]_block_invoke
- ___64-[ICContentKeySession initWithRequestContext:keyStore:delegate:]_block_invoke_2
- ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.44
- ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.47
- ___66-[ICContentKeySession stopSessionInvalidatingKeys:withCompletion:]_block_invoke.48
- ___73-[ICCloudContentTasteRequestListener _setupContentTasteServiceConnection]_block_invoke.69
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.166
- ___75-[ICLibraryAuthServiceClientTokenProvider _updateEntriesForAccountsChanges]_block_invoke.169
- ___78-[ICLibraryAuthServiceClientTokenProvider listener:shouldAcceptNewConnection:]_block_invoke.173
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.25
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke.32
- ___85-[ICMusicSubscriptionLeaseSession _newOperationForPlaybackRequest:completionHandler:]_block_invoke_2.33
- ___86-[ICStoreURLResponseHandler processCompletedResponse:toRequest:withCompletionHandler:]_block_invoke.43
- ___86-[ICStoreURLResponseHandler processCompletedResponse:toRequest:withCompletionHandler:]_block_invoke.46
- ___92-[ICStoreURLRequest buildStoreURLRequestWithURLRequest:builderProperties:completionHandler:]_block_invoke.235
- ___Block_byref_object_copy_.10200
- ___Block_byref_object_copy_.10499
- ___Block_byref_object_copy_.10627
- ___Block_byref_object_copy_.12155
- ___Block_byref_object_copy_.13507
- ___Block_byref_object_copy_.14051
- ___Block_byref_object_copy_.14225
- ___Block_byref_object_copy_.14490
- ___Block_byref_object_copy_.14898
- ___Block_byref_object_copy_.16027
- ___Block_byref_object_copy_.16505
- ___Block_byref_object_copy_.16732
- ___Block_byref_object_copy_.18426
- ___Block_byref_object_copy_.18791
- ___Block_byref_object_copy_.19000
- ___Block_byref_object_copy_.19979
- ___Block_byref_object_copy_.20876
- ___Block_byref_object_copy_.22142
- ___Block_byref_object_copy_.22243
- ___Block_byref_object_copy_.24639
- ___Block_byref_object_copy_.25031
- ___Block_byref_object_copy_.25583
- ___Block_byref_object_copy_.25938
- ___Block_byref_object_copy_.25980
- ___Block_byref_object_copy_.26839
- ___Block_byref_object_copy_.27795
- ___Block_byref_object_copy_.28812
- ___Block_byref_object_copy_.29155
- ___Block_byref_object_copy_.30354
- ___Block_byref_object_copy_.30887
- ___Block_byref_object_copy_.31270
- ___Block_byref_object_copy_.31447
- ___Block_byref_object_copy_.31607
- ___Block_byref_object_copy_.32356
- ___Block_byref_object_copy_.34358
- ___Block_byref_object_copy_.34583
- ___Block_byref_object_copy_.34717
- ___Block_byref_object_copy_.35564
- ___Block_byref_object_copy_.35726
- ___Block_byref_object_copy_.36410
- ___Block_byref_object_copy_.36680
- ___Block_byref_object_copy_.37271
- ___Block_byref_object_copy_.37451
- ___Block_byref_object_copy_.37756
- ___Block_byref_object_copy_.38604
- ___Block_byref_object_copy_.9279
- ___Block_byref_object_copy_.9384
- ___Block_byref_object_dispose_.10201
- ___Block_byref_object_dispose_.10500
- ___Block_byref_object_dispose_.10628
- ___Block_byref_object_dispose_.12156
- ___Block_byref_object_dispose_.13508
- ___Block_byref_object_dispose_.14052
- ___Block_byref_object_dispose_.14226
- ___Block_byref_object_dispose_.14491
- ___Block_byref_object_dispose_.14899
- ___Block_byref_object_dispose_.16028
- ___Block_byref_object_dispose_.16506
- ___Block_byref_object_dispose_.16733
- ___Block_byref_object_dispose_.18427
- ___Block_byref_object_dispose_.18792
- ___Block_byref_object_dispose_.19001
- ___Block_byref_object_dispose_.19980
- ___Block_byref_object_dispose_.20877
- ___Block_byref_object_dispose_.22143
- ___Block_byref_object_dispose_.22244
- ___Block_byref_object_dispose_.24640
- ___Block_byref_object_dispose_.25032
- ___Block_byref_object_dispose_.25584
- ___Block_byref_object_dispose_.25939
- ___Block_byref_object_dispose_.25981
- ___Block_byref_object_dispose_.26840
- ___Block_byref_object_dispose_.27796
- ___Block_byref_object_dispose_.28813
- ___Block_byref_object_dispose_.29156
- ___Block_byref_object_dispose_.30355
- ___Block_byref_object_dispose_.30888
- ___Block_byref_object_dispose_.31271
- ___Block_byref_object_dispose_.31448
- ___Block_byref_object_dispose_.31608
- ___Block_byref_object_dispose_.32357
- ___Block_byref_object_dispose_.34359
- ___Block_byref_object_dispose_.34584
- ___Block_byref_object_dispose_.34718
- ___Block_byref_object_dispose_.35565
- ___Block_byref_object_dispose_.35727
- ___Block_byref_object_dispose_.36411
- ___Block_byref_object_dispose_.36681
- ___Block_byref_object_dispose_.37272
- ___Block_byref_object_dispose_.37452
- ___Block_byref_object_dispose_.37757
- ___Block_byref_object_dispose_.38605
- ___Block_byref_object_dispose_.9280
- ___Block_byref_object_dispose_.9385
- ___block_literal_global.10.25593
- ___block_literal_global.10292
- ___block_literal_global.11241
- ___block_literal_global.11680
- ___block_literal_global.12.24436
- ___block_literal_global.12.25591
- ___block_literal_global.12268
- ___block_literal_global.12911
- ___block_literal_global.12953
- ___block_literal_global.13.37765
- ___block_literal_global.13538
- ___block_literal_global.14937
- ___block_literal_global.15
- ___block_literal_global.16429
- ___block_literal_global.168.28097
- ___block_literal_global.169.9674
- ___block_literal_global.173.10286
- ___block_literal_global.17461
- ___block_literal_global.17866
- ___block_literal_global.18.25589
- ___block_literal_global.18.34416
- ___block_literal_global.18258
- ___block_literal_global.18478
- ___block_literal_global.18692
- ___block_literal_global.19847
- ___block_literal_global.21518
- ___block_literal_global.22044
- ___block_literal_global.23588
- ___block_literal_global.23712
- ___block_literal_global.24435
- ___block_literal_global.24627
- ___block_literal_global.25095
- ___block_literal_global.25260
- ___block_literal_global.25459
- ___block_literal_global.25599
- ___block_literal_global.26877
- ___block_literal_global.27384
- ___block_literal_global.28197
- ___block_literal_global.28521
- ___block_literal_global.28827
- ___block_literal_global.28977
- ___block_literal_global.29966
- ___block_literal_global.3.14935
- ___block_literal_global.3.17468
- ___block_literal_global.30489
- ___block_literal_global.30550
- ___block_literal_global.30774
- ___block_literal_global.31344
- ___block_literal_global.31951
- ___block_literal_global.32393
- ___block_literal_global.33479
- ___block_literal_global.34
- ___block_literal_global.34001
- ___block_literal_global.34439
- ___block_literal_global.35506
- ___block_literal_global.36423
- ___block_literal_global.36790
- ___block_literal_global.36887
- ___block_literal_global.37595
- ___block_literal_global.37775
- ___block_literal_global.38715
- ___block_literal_global.38853
- ___block_literal_global.38983
- ___block_literal_global.39674
- ___block_literal_global.39863
- ___block_literal_global.40192
- ___block_literal_global.47.30590
- ___block_literal_global.52.28784
- ___block_literal_global.52.30593
- ___block_literal_global.6.25597
- ___block_literal_global.68.28489
- ___block_literal_global.71
- ___block_literal_global.74
- ___block_literal_global.76.30613
- ___block_literal_global.8.25595
- ___block_literal_global.8985
- ___block_literal_global.9790
- __unnamed_array_storage.30592
- __unnamed_array_storage.40089
- __unnamed_array_storage.96.40090
- _sharedCache.sOnceToken.28976
- _sharedCache.sSharedCache.28978
- _sharedController.sOnceToken.34438
- _sharedController.sOnceToken.37774
- _sharedController.sSharedController.34440
- _sharedController.sSharedController.37776
- _sharedManager.sOnceToken.18691
- _sharedManager.sOnceToken.27383
- _sharedManager.sSharedManager.18693
- _sharedManager.sSharedManager.27385
- _sharedMonitor.sOnceToken.17865
- _sharedMonitor.sOnceToken.38714
- _sharedMonitor.sSharedMonitor.17867
- _sharedMonitor.sSharedMonitor.38716
- _sharedProvider.sOnceToken.38982
- _sharedProvider.sSharedProvider.38984
CStrings:
+ "\x0f\x03D"
+ "    isCollaborativePlaylist:true\n"
+ "%{public}@ Cannot register nil token."
+ "%{public}@ Invalid [LSApplicationRecord applicationState] for bundleID: %{public}@"
+ "%{public}@ [SKD] - Timed out waiting for the enhanced audio configuration (prefetchKeyCertificateURL) to load."
+ "%{public}@ [SKD] - Timed out waiting for the enhanced audio configuration (prefetchKeyIdentifiers) to load."
+ "%{public}@ [SKD] - Timed out waiting for the enhanced audio configuration (prefetchKeyServerURL) to load."
+ "%{public}@ [SKD] - Updated prefetch identifiers %{public}@"
+ "@\"ICContentKeySessionPrefetchKeyConfiguration\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"PDCPreflightManager\""
+ "@40@0:8Q16B24B28@32"
+ "AllDSIDsShouldError"
+ "AllDSIDsShouldSucceed"
+ "Class getPDCPreflightManagerClass(void)_block_invoke"
+ "CommandOption"
+ "ErrorDSIDs"
+ "Favoriting"
+ "FuseNoActiveSubscription"
+ "ICAuthServiceClientTokenProviderDebugConfiguration"
+ "ICContentKeySessionPrefetchKeyConfiguration"
+ "ICDefaultsKeyDebugFetchConfiguration"
+ "ICDefaultsKeyDebugRefreshConfiguration"
+ "ICDefaultsKeyPrefetchKeyIdentifiers"
+ "ICInternalDefaultsKeyForceBackoffResponseFromCloudLibrary"
+ "ICInternalDefaultsKeyForceResetSyncRequiredResponseFromCloudLibrary"
+ "ICStoreURLRequestHTTPStatusCodeUserInfoKey"
+ "ItemNotFoundForFuse"
+ "PDCPreflightManager"
+ "PurchaseBlockedForSpecialEdu"
+ "SecondaryAuthRequired"
+ "Set content taste type on album storeID %lld, persistentID %lld, timeStamp %{public}@ with error %{public}@."
+ "Set content taste type on artist storeID %lld, persistentID %lld, timeStamp %{public}@ with error %{public}@."
+ "Set content taste type on global playlist %{public}@ with error %{public}@."
+ "Set content taste type on global playlist %{public}@, persistentID %lld with error %{public}@."
+ "Set content taste type on media item with storeID %lld with error %{public}@."
+ "SlotTransferWarningFuseBuy"
+ "StoragePurchaseOnNonStorageCapableAccount"
+ "T@\"ICAuthServiceClientTokenProviderDebugConfiguration\",R,N"
+ "T@\"NSArray\",R,N,V_errorDSIDs"
+ "T@\"NSSet\",R,C,N"
+ "TB,D,N,GisCollaborativePlaylist"
+ "TB,R,N,GisCollaborativePlaylist,V_collaborativePlaylist"
+ "TB,R,N,V_allDSIDsShouldError"
+ "TB,R,N,V_allDSIDsShouldSucceed"
+ "TQ,R,N,V_commandOption"
+ "Token is nil"
+ "X-DAAP-Client-Features-Versions"
+ "X-DAAP-Supported-Features"
+ "X-DAAP-debug-features"
+ "[<ICMusicUserProfile:%p> socialProfile=%@; isOnboarded=%d, collaborationAllowed=%d]"
+ "[Lease] - [%{public}@] - _handleRemoteServerDidBecomeLikelyReachable: %{public}s renewal"
+ "_allDSIDsShouldError"
+ "_allDSIDsShouldSucceed"
+ "_checkTokenPresetsForDSID:forceRefresh:"
+ "_collaborativePlaylist"
+ "_commandOption"
+ "_devicePresetForConfiguration:withDSID:"
+ "_errorDSIDs"
+ "_fetchWithRequestContext:"
+ "_group"
+ "_initWithDefaultKeyIdentifiers"
+ "_isCollaborativePlaylist"
+ "_isPrefetchKey:"
+ "_keyIdentifiers"
+ "_prefetchKeyConfiguration"
+ "_preflightManager"
+ "_registerAPNSToken"
+ "addDebugConfiguration:"
+ "allDSIDsShouldError"
+ "allDSIDsShouldSucceed"
+ "clearAllPresets"
+ "clearShouldForceServerToUseDAAPDebugFeatures"
+ "collaborativePlaylist"
+ "com.apple.iTunesCloud.ICContentKeySession.prefetchKeyConfig"
+ "commandOption"
+ "debugFetchConfiguration"
+ "debugRefreshConfiguration"
+ "errorDSIDs"
+ "initWithCommandOption:allDSIDsShouldError:allDSIDsShouldSucceed:errorDSIDs:"
+ "initWithTargetQueue:"
+ "isCollaborativePlaylist"
+ "isEqualToSet:"
+ "isLowPowerModeEnabled"
+ "keyIdentifiers"
+ "paramsForUnsettingReactionOnTrackWithItemUUID:"
+ "performing"
+ "prefetchKeyIdentifiers"
+ "preflightDisclosureRequiredForBundleIdentifier:"
+ "preflightDisclosureRequiredForMusic"
+ "presetsFound"
+ "requiresPreflightForApplicationRecord:"
+ "setCollaborativePlaylist:"
+ "setContentTaste:forAlbumStoreID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forArtistStoreID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forMediaItem:storeIdentifier:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setContentTaste:forPlaylistGlobalID:persistentID:timeStamp:configuration:withCompletionHandler:"
+ "setPrefetchKeyIdentifiers:"
+ "shouldForceServerToUseDAAPDebugFeature"
+ "shouldForceServerToUseDAAPDebugFeatureAlwaysBackoff"
+ "shouldForceServerToUseDAAPDebugFeatureAlwaysPerformResetSync"
+ "skipping"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore"
+ "v64@0:8q16@\"NSString\"24q32@\"NSDate\"40@\"ICConnectionConfiguration\"48@?<v@?@\"NSError\">56"
+ "v64@0:8q16@24q32@40@48@?56"
+ "v72@0:8q16q24q32q40@\"NSDate\"48@\"ICConnectionConfiguration\"56@?<v@?@\"NSError\">64"
+ "v72@0:8q16q24q32q40@48@56@?64"
+ "void *PrivacyDisclosureCoreLibrary(void)"
+ "{?=\"characterDisplayedCount\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"isCollaborativePlaylist\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"
+ "{DevicePresetTokenResult=@@B}28@0:8@16B24"
+ "{DevicePresetTokenResult=@@B}32@0:8@16@24"
+ "\xf0A"
- "\x0f\x05D"
- "%{public}@ [SKD] - Timed out waiting for the enhanced audio configuration to load. we may fail to fetch the shared key"
- "%{public}@ [SKD] - loaded prefetch identifiers %{public}@"
- "FavoritesPlaylist"
- "Set content taste type on global playlist %{public}@} with error %{public}@."
- "[<ICMusicUserProfile:%p> socialProfile=%@]"
- "_prefetchKeyCertificateURL"
- "_prefetchKeyIdentifiers"
- "_prefetchKeyServerURL"
- "paramsForUnsettingReaction:onTrackWithItemUUID:"
- "{?=\"characterDisplayedCount\"b1\"cloudPlaylistID\"b1\"containerAdamID\"b1\"equivalencySourceAdamID\"b1\"eventDateTimestamp\"b1\"eventSecondsFromGMT\"b1\"itemCloudID\"b1\"itemDuration\"b1\"itemEndTime\"b1\"itemStartTime\"b1\"persistentID\"b1\"purchasedAdamID\"b1\"radioAdamID\"b1\"reportingAdamID\"b1\"sharedActivityGroupSizeCurrent\"b1\"sharedActivityGroupSizeMax\"b1\"stationID\"b1\"storeAccountID\"b1\"subscriptionAdamID\"b1\"tvShowPurchasedAdamID\"b1\"tvShowSubscriptionAdamID\"b1\"vocalAttenuationDuration\"b1\"audioQualityPreference\"b1\"containerType\"b1\"displayType\"b1\"endReasonType\"b1\"eventType\"b1\"itemType\"b1\"mediaType\"b1\"playbackFormatPreference\"b1\"reasonHintType\"b1\"sourceType\"b1\"systemReleaseType\"b1\"vocalAttenuationAvailibility\"b1\"continuityCameraUsed\"b1\"internalBuild\"b1\"offline\"b1\"privateListeningEnabled\"b1\"sBEnabled\"b1\"siriInitiated\"b1}"
- "\xf0a"

```
