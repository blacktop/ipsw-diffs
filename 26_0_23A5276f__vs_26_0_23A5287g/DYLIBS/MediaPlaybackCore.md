## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-25115.25.25.201.0
-  __TEXT.__text: 0x3cf924
-  __TEXT.__auth_stubs: 0x5670
-  __TEXT.__objc_methlist: 0x16e98
+25100.25.26.502.0
+  __TEXT.__text: 0x3d9d88
+  __TEXT.__auth_stubs: 0x57e0
+  __TEXT.__objc_methlist: 0x16f48
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x155a0
-  __TEXT.__cstring: 0x2edca
-  __TEXT.__constg_swiftt: 0x7398
-  __TEXT.__swift5_typeref: 0x4eba
-  __TEXT.__swift5_builtin: 0x71c
-  __TEXT.__swift5_reflstr: 0x4ed1
-  __TEXT.__swift5_fieldmd: 0x4b00
-  __TEXT.__swift5_assocty: 0xea0
-  __TEXT.__swift5_proto: 0x99c
-  __TEXT.__swift5_types: 0x520
-  __TEXT.__swift5_capture: 0x3268
-  __TEXT.__oslogstring: 0x39c3c
+  __TEXT.__const: 0x157a0
+  __TEXT.__cstring: 0x2f183
+  __TEXT.__constg_swiftt: 0x73f8
+  __TEXT.__swift5_typeref: 0x4ee6
+  __TEXT.__swift5_reflstr: 0x4ef2
+  __TEXT.__swift5_fieldmd: 0x4b34
+  __TEXT.__swift5_builtin: 0x730
+  __TEXT.__swift5_assocty: 0xf00
+  __TEXT.__swift5_capture: 0x32f4
+  __TEXT.__oslogstring: 0x3a7dc
   __TEXT.__swift5_mpenum: 0xfc
-  __TEXT.__swift_as_entry: 0x3a0
-  __TEXT.__swift_as_ret: 0x49c
+  __TEXT.__swift5_proto: 0x9b0
+  __TEXT.__swift5_types: 0x524
+  __TEXT.__swift_as_entry: 0x3a8
+  __TEXT.__swift_as_ret: 0x4ac
   __TEXT.__swift5_protos: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x6a98
+  __TEXT.__gcc_except_tab: 0x6978
   __TEXT.__ustring: 0x4b4
-  __TEXT.__unwind_info: 0xc168
-  __TEXT.__eh_frame: 0xc3a0
-  __TEXT.__objc_classname: 0x3d35
-  __TEXT.__objc_methname: 0x385ea
-  __TEXT.__objc_methtype: 0x98b5
-  __TEXT.__objc_stubs: 0x264a0
-  __DATA_CONST.__got: 0x2dc8
-  __DATA_CONST.__const: 0x8fc0
+  __TEXT.__unwind_info: 0xc410
+  __TEXT.__eh_frame: 0xc888
+  __TEXT.__objc_classname: 0x3d25
+  __TEXT.__objc_methname: 0x3889d
+  __TEXT.__objc_methtype: 0x9961
+  __TEXT.__objc_stubs: 0x26600
+  __DATA_CONST.__got: 0x2e60
+  __DATA_CONST.__const: 0x9028
   __DATA_CONST.__objc_classlist: 0xcc8
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc148
+  __DATA_CONST.__objc_selrefs: 0xc1b8
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x2b48
-  __AUTH_CONST.__const: 0xf468
-  __AUTH_CONST.__cfstring: 0x1cf40
-  __AUTH_CONST.__objc_const: 0x32560
+  __AUTH_CONST.__auth_got: 0x2c00
+  __AUTH_CONST.__const: 0xf638
+  __AUTH_CONST.__cfstring: 0x1d260
+  __AUTH_CONST.__objc_const: 0x32678
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x4d10
-  __AUTH.__data: 0x3248
-  __DATA.__objc_ivar: 0x19b8
-  __DATA.__data: 0x7008
-  __DATA.__bss: 0xfc48
+  __AUTH.__data: 0x3250
+  __DATA.__objc_ivar: 0x19c8
+  __DATA.__data: 0x7048
+  __DATA.__bss: 0xfed0
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x3918
-  __DATA_DIRTY.__data: 0x46d8
+  __DATA_DIRTY.__data: 0x4740
   __DATA_DIRTY.__bss: 0x13b0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0774310C-A117-347C-86C3-6F9D84564990
-  Functions: 19419
-  Symbols:   37929
-  CStrings:  22254
+  UUID: 4A2EED55-0848-31F5-8B13-CFE42D74C1FE
+  Functions: 19572
+  Symbols:   38168
+  CStrings:  22357
 
Symbols:
+ -[MPCItemBookmarker itemTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:]
+ -[MPCModelQueueFeeder clearSectionProxy]
+ -[MPCModelQueueFeeder controller:defersResponse:completion:]
+ -[MPCPlaybackAccountManager _handleURLBagProviderDidUpdateBagNotification:]
+ -[MPCPlaybackAccountManager _notifyObserversForChange:]
+ -[MPCReportingLyricsViewEvent continuityMicrophoneUsed]
+ -[MPCReportingLyricsViewEvent displayTranslationEnabled]
+ -[MPCReportingLyricsViewEvent displayTransliterationEnabled]
+ -[MPCReportingLyricsViewEvent setContinuityMicrophoneUsed:]
+ -[MPCReportingLyricsViewEvent setDisplayTranslationEnabled:]
+ -[MPCReportingLyricsViewEvent setDisplayTransliterationEnabled:]
+ -[MPIdentifierSet(MPCAdditions) mpc_intersectsSet:ignoringModelKind:]
+ -[MPSectionedCollection(MPCModelQueueFeederAdditions) mpc_indexPathForIdentifiers:]
+ -[_MPCPlaybackEnginePlayer overlappingTransitionDidReachPivotPointFrom:to:transitionTime:incomingItemAveragePostPivotTransitionRate:transitionType:timeStamp:]
+ -[_MPCQueueControllerBehaviorMusic _setRepeatType:reason:]
+ -[_MPCQueueControllerBehaviorMusicDataSourceState cloneWithNewStartItemIdentifiers:identifierRegistry:]
+ GCC_except_table0
+ GCC_except_table1128
+ GCC_except_table1132
+ GCC_except_table1296
+ GCC_except_table1298
+ GCC_except_table1344
+ GCC_except_table1355
+ GCC_except_table1362
+ GCC_except_table1369
+ GCC_except_table1405
+ GCC_except_table1417
+ GCC_except_table1426
+ GCC_except_table1458
+ GCC_except_table1630
+ GCC_except_table1632
+ GCC_except_table1645
+ GCC_except_table1650
+ GCC_except_table1719
+ GCC_except_table1794
+ GCC_except_table1795
+ GCC_except_table185
+ GCC_except_table1909
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1959
+ GCC_except_table1968
+ GCC_except_table1983
+ GCC_except_table1993
+ GCC_except_table2103
+ GCC_except_table2133
+ GCC_except_table2158
+ GCC_except_table2162
+ GCC_except_table2165
+ GCC_except_table2214
+ GCC_except_table2246
+ GCC_except_table2341
+ GCC_except_table2357
+ GCC_except_table2544
+ GCC_except_table2572
+ GCC_except_table2598
+ GCC_except_table2742
+ GCC_except_table2761
+ GCC_except_table2768
+ GCC_except_table2769
+ GCC_except_table2793
+ GCC_except_table2795
+ GCC_except_table2799
+ GCC_except_table2803
+ GCC_except_table2805
+ GCC_except_table2807
+ GCC_except_table2809
+ GCC_except_table2812
+ GCC_except_table2837
+ GCC_except_table2844
+ GCC_except_table2849
+ GCC_except_table2851
+ GCC_except_table2854
+ GCC_except_table2859
+ GCC_except_table2860
+ GCC_except_table2865
+ GCC_except_table2868
+ GCC_except_table2871
+ GCC_except_table2891
+ GCC_except_table2899
+ GCC_except_table2941
+ GCC_except_table3022
+ GCC_except_table3033
+ GCC_except_table3034
+ GCC_except_table3058
+ GCC_except_table3066
+ GCC_except_table3107
+ GCC_except_table3108
+ GCC_except_table3124
+ GCC_except_table313
+ GCC_except_table315
+ GCC_except_table3182
+ GCC_except_table3197
+ GCC_except_table3202
+ GCC_except_table3236
+ GCC_except_table3238
+ GCC_except_table3245
+ GCC_except_table325
+ GCC_except_table3256
+ GCC_except_table3261
+ GCC_except_table3297
+ GCC_except_table334
+ GCC_except_table3342
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table34
+ GCC_except_table3464
+ GCC_except_table3486
+ GCC_except_table3488
+ GCC_except_table3489
+ GCC_except_table3516
+ GCC_except_table3520
+ GCC_except_table3530
+ GCC_except_table3703
+ GCC_except_table3707
+ GCC_except_table3718
+ GCC_except_table3730
+ GCC_except_table3732
+ GCC_except_table3738
+ GCC_except_table3747
+ GCC_except_table383
+ GCC_except_table3870
+ GCC_except_table391
+ GCC_except_table3914
+ GCC_except_table3915
+ GCC_except_table3934
+ GCC_except_table3942
+ GCC_except_table3960
+ GCC_except_table3965
+ GCC_except_table3967
+ GCC_except_table3981
+ GCC_except_table399
+ GCC_except_table4004
+ GCC_except_table4015
+ GCC_except_table408
+ GCC_except_table4101
+ GCC_except_table4106
+ GCC_except_table4110
+ GCC_except_table4119
+ GCC_except_table4158
+ GCC_except_table4263
+ GCC_except_table4384
+ GCC_except_table4385
+ GCC_except_table456
+ GCC_except_table4569
+ GCC_except_table4603
+ GCC_except_table4621
+ GCC_except_table4636
+ GCC_except_table4644
+ GCC_except_table4652
+ GCC_except_table4661
+ GCC_except_table4676
+ GCC_except_table472
+ GCC_except_table4721
+ GCC_except_table473
+ GCC_except_table4745
+ GCC_except_table4747
+ GCC_except_table4755
+ GCC_except_table4808
+ GCC_except_table4833
+ GCC_except_table489
+ GCC_except_table490
+ GCC_except_table4946
+ GCC_except_table5046
+ GCC_except_table5286
+ GCC_except_table5287
+ GCC_except_table5359
+ GCC_except_table5594
+ GCC_except_table5619
+ GCC_except_table5732
+ GCC_except_table5814
+ GCC_except_table5822
+ GCC_except_table5887
+ GCC_except_table5912
+ GCC_except_table5947
+ GCC_except_table5950
+ GCC_except_table5953
+ GCC_except_table6254
+ GCC_except_table6271
+ GCC_except_table6319
+ GCC_except_table6332
+ GCC_except_table6834
+ GCC_except_table7175
+ GCC_except_table7267
+ GCC_except_table7276
+ GCC_except_table7355
+ GCC_except_table7362
+ GCC_except_table7381
+ GCC_except_table741
+ GCC_except_table7430
+ GCC_except_table7431
+ GCC_except_table7434
+ GCC_except_table7439
+ GCC_except_table7455
+ GCC_except_table797
+ GCC_except_table873
+ GCC_except_table904
+ GCC_except_table907
+ GCC_except_table909
+ GCC_except_table914
+ GCC_except_table916
+ GCC_except_table929
+ GCC_except_table933
+ GCC_except_table939
+ GCC_except_table943
+ GCC_except_table946
+ GCC_except_table949
+ _ICURLBagProviderDidUpdateBagNotificationRequestContextUserInfoKey
+ _MPNowPlayingContentItemUserInfoKeyPodcastEpisodeStreamURL
+ _MSVFastHexStringFromBytes.hexCharacters.29982
+ _OBJC_IVAR_$_MPCModelQueueFeeder._automaticResponseLoadingCriticalSection
+ _OBJC_IVAR_$_MPCModelQueueFeeder._loadNextPageCriticalSection
+ _OBJC_IVAR_$_MPCModelQueueFeeder._lock
+ _OBJC_IVAR_$_MPCReportingLyricsViewEvent._continuityMicrophoneUsed
+ _OBJC_IVAR_$_MPCReportingLyricsViewEvent._displayTranslationEnabled
+ _OBJC_IVAR_$_MPCReportingLyricsViewEvent._displayTransliterationEnabled
+ _OUTLINED_FUNCTION_337
+ _OUTLINED_FUNCTION_338
+ _OUTLINED_FUNCTION_339
+ _OUTLINED_FUNCTION_340
+ _OUTLINED_FUNCTION_341
+ _OUTLINED_FUNCTION_342
+ _OUTLINED_FUNCTION_343
+ __MPCAudioTapFinalize.1829
+ __MPCAudioTapInit.1830
+ __MPCAudioTapPrepareCallback.1828
+ __MPCAudioTapProcess.1823
+ __MPCAudioTapUnprepareCallback.1822
+ __MSV_XXH_XXH32_update
+ __OBJC_$_CATEGORY_CLASS_METHODS_MPIdentifierSet_$_MPCPlaybackEngineEventPayload
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_MPModelPlaylist_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_MPModelRadioStation_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPIdentifierSet_$_MPCPlaybackEngineEventPayload
+ __OBJC_$_CATEGORY_MPModelAlbum_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelGenericObject_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelObject_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelPlaylistEntry_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelPlaylist_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelRadioStation_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPModelSong_$_BehaviorMusicSharePlayAdditions
+ __OBJC_$_CATEGORY_MPPlaybackContext_$_MPCSharedListening
+ __OBJC_$_CATEGORY_MPSectionedCollection_$_MPCModelQueueFeederAdditions
+ __OBJC_$_CATEGORY_NSError_$_MPCPlaybackEngineEventPayload
+ __OBJC_$_CLASS_METHODS_MPModelAlbum(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|ICRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelGenericObject(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|Playability|MPCModelRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelObject(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|MPCModelRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelPlaylist(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelPlaylistEntry(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelRadioStation(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions)
+ __OBJC_$_CLASS_METHODS_MPModelSong(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|ICRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_CLASS_METHODS_NSError(MPCPlaybackEngineEventPayload|MPCErrorController|ICErrorProcessing|MPCDialogs)
+ __OBJC_$_INSTANCE_METHODS_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|PreferredAudioTimePitchAlgorithm|Reuse|MFQueuePlayerItem|MPCReportingAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPCModelPlaybackContext(MPCSharedListening|MPCPlaybackQueue)
+ __OBJC_$_INSTANCE_METHODS_MPIdentifierSet(MPCPlaybackEngineEventPayload|MPCAccumulatorAdditions|MPCAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPModelAlbum(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|ICRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPModelGenericObject(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|Playability|MPCModelRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPModelObject(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|MPCModelRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPModelPlaylistEntry(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPModelSong(BehaviorMusicSharePlayAdditions|MPCModelQueueFeederAdditions|ICRadioContentReference|MPCStoreFrontLocalEquivalencyMiddlewareAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPPlaybackContext(MPCSharedListening|MPCPlaybackQueue)
+ __OBJC_$_INSTANCE_METHODS_MPSectionedCollection(MPCModelQueueFeederAdditions|MQFDebugging)
+ __OBJC_$_INSTANCE_METHODS_NSError(MPCPlaybackEngineEventPayload|MPCErrorController|ICErrorProcessing|MPCDialogs)
+ __OBJC_$_PROP_LIST_MPModelObject_$_BehaviorMusicSharePlayAdditions
+ __OBJC_CATEGORY_PROTOCOLS_$_MPIdentifierSet_$_MPCPlaybackEngineEventPayload
+ __OBJC_CATEGORY_PROTOCOLS_$_NSError_$_MPCPlaybackEngineEventPayload
+ __OBJC_CLASS_PROTOCOLS_$_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|PreferredAudioTimePitchAlgorithm|Reuse|MFQueuePlayerItem|MPCReportingAdditions)
+ __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.38
+ ___123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.688
+ ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.561
+ ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke_2.562
+ ___34-[MPCPlaybackAccountManager _init]_block_invoke
+ ___43-[MPCModelQueueFeeder playbackInfoForItem:]_block_invoke.8
+ ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke.266
+ ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke_2.267
+ ___55-[MPCPlaybackAccountManager _notifyObserversForChange:]_block_invoke
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.132
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.134
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.138
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.148
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.158
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.98
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.99
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_2
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_2.146
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_2.149
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_3
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_3.150
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_4
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_5
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_6
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_7
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_8
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_9
+ ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.215
+ ___69-[MPIdentifierSet(MPCAdditions) mpc_intersectsSet:ignoringModelKind:]_block_invoke
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.190
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.200
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.202
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.207
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.209
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.171
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.175
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke_2.176
+ ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.210
+ ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.211
+ ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.215
+ ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.217
+ ___76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.710
+ ___76-[_MPCQueueControllerBehaviorMusicDataSourceState reloadSection:completion:]_block_invoke.96
+ ___76-[_MPCQueueControllerBehaviorMusicDataSourceState reloadSection:completion:]_block_invoke.97
+ ___80-[_MPCQueueControllerBehaviorMusic reshuffleWithTargetContentItemID:completion:]_block_invoke
+ ___80-[_MPCQueueControllerBehaviorMusic reshuffleWithTargetContentItemID:completion:]_block_invoke.356
+ ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke.134
+ ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke.153
+ ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke_2.136
+ ___83-[MPSectionedCollection(MPCModelQueueFeederAdditions) mpc_indexPathForIdentifiers:]_block_invoke
+ ___83-[MPSectionedCollection(MPCModelQueueFeederAdditions) mpc_indexPathForIdentifiers:]_block_invoke_2
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.220
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.273
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.279
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.283
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.287
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.289
+ ___Block_byref_object_copy_.11257
+ ___Block_byref_object_copy_.11431
+ ___Block_byref_object_copy_.11731
+ ___Block_byref_object_copy_.1220
+ ___Block_byref_object_copy_.12436
+ ___Block_byref_object_copy_.13617
+ ___Block_byref_object_copy_.1555
+ ___Block_byref_object_copy_.15688
+ ___Block_byref_object_copy_.16282
+ ___Block_byref_object_copy_.16691
+ ___Block_byref_object_copy_.17290
+ ___Block_byref_object_copy_.17928
+ ___Block_byref_object_copy_.1831
+ ___Block_byref_object_copy_.18792
+ ___Block_byref_object_copy_.19327
+ ___Block_byref_object_copy_.19513
+ ___Block_byref_object_copy_.19957
+ ___Block_byref_object_copy_.21099
+ ___Block_byref_object_copy_.2128
+ ___Block_byref_object_copy_.22035
+ ___Block_byref_object_copy_.24971
+ ___Block_byref_object_copy_.25783
+ ___Block_byref_object_copy_.26204
+ ___Block_byref_object_copy_.26549
+ ___Block_byref_object_copy_.26983
+ ___Block_byref_object_copy_.276
+ ___Block_byref_object_copy_.28387
+ ___Block_byref_object_copy_.28951
+ ___Block_byref_object_copy_.2925
+ ___Block_byref_object_copy_.33784
+ ___Block_byref_object_copy_.34256
+ ___Block_byref_object_copy_.34670
+ ___Block_byref_object_copy_.35028
+ ___Block_byref_object_copy_.3733
+ ___Block_byref_object_copy_.3907
+ ___Block_byref_object_copy_.474
+ ___Block_byref_object_copy_.4903
+ ___Block_byref_object_copy_.499
+ ___Block_byref_object_copy_.669
+ ___Block_byref_object_copy_.6918
+ ___Block_byref_object_copy_.7768
+ ___Block_byref_object_copy_.9826
+ ___Block_byref_object_copy_.9893
+ ___Block_byref_object_dispose_.11258
+ ___Block_byref_object_dispose_.11432
+ ___Block_byref_object_dispose_.11732
+ ___Block_byref_object_dispose_.1221
+ ___Block_byref_object_dispose_.12437
+ ___Block_byref_object_dispose_.13618
+ ___Block_byref_object_dispose_.1556
+ ___Block_byref_object_dispose_.15689
+ ___Block_byref_object_dispose_.16283
+ ___Block_byref_object_dispose_.16692
+ ___Block_byref_object_dispose_.17291
+ ___Block_byref_object_dispose_.17929
+ ___Block_byref_object_dispose_.1832
+ ___Block_byref_object_dispose_.18793
+ ___Block_byref_object_dispose_.19328
+ ___Block_byref_object_dispose_.19514
+ ___Block_byref_object_dispose_.19958
+ ___Block_byref_object_dispose_.21100
+ ___Block_byref_object_dispose_.2129
+ ___Block_byref_object_dispose_.22036
+ ___Block_byref_object_dispose_.24972
+ ___Block_byref_object_dispose_.25784
+ ___Block_byref_object_dispose_.26205
+ ___Block_byref_object_dispose_.26550
+ ___Block_byref_object_dispose_.26984
+ ___Block_byref_object_dispose_.277
+ ___Block_byref_object_dispose_.28388
+ ___Block_byref_object_dispose_.28952
+ ___Block_byref_object_dispose_.2926
+ ___Block_byref_object_dispose_.33785
+ ___Block_byref_object_dispose_.34257
+ ___Block_byref_object_dispose_.34671
+ ___Block_byref_object_dispose_.35029
+ ___Block_byref_object_dispose_.3734
+ ___Block_byref_object_dispose_.3908
+ ___Block_byref_object_dispose_.475
+ ___Block_byref_object_dispose_.4904
+ ___Block_byref_object_dispose_.500
+ ___Block_byref_object_dispose_.670
+ ___Block_byref_object_dispose_.6919
+ ___Block_byref_object_dispose_.7769
+ ___Block_byref_object_dispose_.9827
+ ___Block_byref_object_dispose_.9894
+ ___block_descriptor_112_e8_32s40s48s56s64bs72r80r88r96r_e5_v8?0ls32l8s40l8s48l8r72l8r80l8r88l8r96l8s56l8s64l8
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"MPPlaybackContext"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8s32l8w48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e39_v24?0"MPPlaybackContext"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e43_v24?0"MPRemotePlaybackQueue"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e32_v32?0q8"MPIdentifierSet"16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_57_e8_32s40s48s_e31_v16?0"ICStoreRequestContext"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r_e32_v32?0q8"MPIdentifierSet"16^B24ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e36_v24?0"MPCPlaybackEngineEvent"8^B16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e8_v16?0q8ls32l8w56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1024
+ ___block_literal_global.10390
+ ___block_literal_global.10550
+ ___block_literal_global.10692
+ ___block_literal_global.10990
+ ___block_literal_global.11.14077
+ ___block_literal_global.110.21014
+ ___block_literal_global.11284
+ ___block_literal_global.11614
+ ___block_literal_global.11798
+ ___block_literal_global.11937
+ ___block_literal_global.121.24354
+ ___block_literal_global.12147
+ ___block_literal_global.127.20983
+ ___block_literal_global.1276
+ ___block_literal_global.12913
+ ___block_literal_global.131.20984
+ ___block_literal_global.133.20985
+ ___block_literal_global.13741
+ ___block_literal_global.14.21139
+ ___block_literal_global.14091
+ ___block_literal_global.143.24366
+ ___block_literal_global.146.24362
+ ___block_literal_global.14764
+ ___block_literal_global.155.16836
+ ___block_literal_global.160.19502
+ ___block_literal_global.16146
+ ___block_literal_global.16261
+ ___block_literal_global.165.16821
+ ___block_literal_global.167.10659
+ ___block_literal_global.170.10660
+ ___block_literal_global.17063
+ ___block_literal_global.17190
+ ___block_literal_global.17231
+ ___block_literal_global.17751
+ ___block_literal_global.179
+ ___block_literal_global.17921
+ ___block_literal_global.18954
+ ___block_literal_global.19631
+ ___block_literal_global.19705
+ ___block_literal_global.198.26303
+ ___block_literal_global.20613
+ ___block_literal_global.21138
+ ___block_literal_global.21440
+ ___block_literal_global.2148
+ ___block_literal_global.21790
+ ___block_literal_global.22076
+ ___block_literal_global.221
+ ___block_literal_global.23069
+ ___block_literal_global.2361
+ ___block_literal_global.24392
+ ___block_literal_global.25391
+ ___block_literal_global.26446
+ ___block_literal_global.265
+ ___block_literal_global.26972
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.27607
+ ___block_literal_global.277
+ ___block_literal_global.282.26218
+ ___block_literal_global.28821
+ ___block_literal_global.292
+ ___block_literal_global.29574
+ ___block_literal_global.297
+ ___block_literal_global.30.19632
+ ___block_literal_global.30199
+ ___block_literal_global.322.12701
+ ___block_literal_global.3267
+ ___block_literal_global.34295
+ ___block_literal_global.34700
+ ___block_literal_global.355
+ ___block_literal_global.37.21754
+ ___block_literal_global.3806
+ ___block_literal_global.4233
+ ___block_literal_global.45.29561
+ ___block_literal_global.4553
+ ___block_literal_global.462
+ ___block_literal_global.463
+ ___block_literal_global.47.24378
+ ___block_literal_global.5109
+ ___block_literal_global.546
+ ___block_literal_global.548
+ ___block_literal_global.550
+ ___block_literal_global.618
+ ___block_literal_global.6515
+ ___block_literal_global.700
+ ___block_literal_global.7231
+ ___block_literal_global.7469
+ ___block_literal_global.7775
+ ___block_literal_global.785
+ ___block_literal_global.788
+ ___block_literal_global.9.21759
+ ___block_literal_global.910
+ ___block_literal_global.9969
+ ___unnamed_20
+ _associated conformance So31AVAudioSessionActivationOptionsVs10SetAlgebraSCSQ
+ _associated conformance So31AVAudioSessionActivationOptionsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So31AVAudioSessionActivationOptionsVs9OptionSetSCSY
+ _associated conformance So31AVAudioSessionActivationOptionsVs9OptionSetSCs0F7Algebra
+ _block_copy_helper.110
+ _block_copy_helper.111
+ _block_copy_helper.164
+ _block_copy_helper.170
+ _block_copy_helper.201
+ _block_copy_helper.207
+ _block_copy_helper.37
+ _block_copy_helper.49
+ _block_copy_helper.5
+ _block_copy_helper.58
+ _block_copy_helper.67
+ _block_copy_helper.73
+ _block_copy_helper.8
+ _block_copy_helper.85
+ _block_copy_helper.92
+ _block_descriptor.10
+ _block_descriptor.112
+ _block_descriptor.113
+ _block_descriptor.166
+ _block_descriptor.172
+ _block_descriptor.203
+ _block_descriptor.209
+ _block_descriptor.39
+ _block_descriptor.51
+ _block_descriptor.60
+ _block_descriptor.69
+ _block_descriptor.7
+ _block_descriptor.75
+ _block_descriptor.87
+ _block_descriptor.94
+ _block_destroy_helper.111
+ _block_destroy_helper.112
+ _block_destroy_helper.165
+ _block_destroy_helper.171
+ _block_destroy_helper.202
+ _block_destroy_helper.208
+ _block_destroy_helper.38
+ _block_destroy_helper.50
+ _block_destroy_helper.59
+ _block_destroy_helper.6
+ _block_destroy_helper.68
+ _block_destroy_helper.74
+ _block_destroy_helper.86
+ _block_destroy_helper.9
+ _block_destroy_helper.93
+ _get_type_metadata 15Synchronization6AtomicVySiG.27
+ _kMTDefaultDisplayScale
+ _objc_msgSend$_notifyObserversForChange:
+ _objc_msgSend$_setRepeatType:reason:
+ _objc_msgSend$clearSection
+ _objc_msgSend$cloneWithNewStartItemIdentifiers:identifierRegistry:
+ _objc_msgSend$computedRateForChangePlaybackRateCommandEvent:
+ _objc_msgSend$continuityMicrophoneUsed
+ _objc_msgSend$controller:defersResponse:completion:
+ _objc_msgSend$displayTranslationEnabled
+ _objc_msgSend$displayTransliterationEnabled
+ _objc_msgSend$identifiersForSectionAtIndex:
+ _objc_msgSend$itemTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:
+ _objc_msgSend$mpc_indexPathForIdentifiers:
+ _objc_msgSend$setContinuityMicrophoneUsed:
+ _objc_msgSend$setDisplayTranslationEnabled:
+ _objc_msgSend$setDisplayTransliterationEnabled:
+ _objc_msgSend$setPreloadedBag:
+ _objectdestroy.161Tm
+ _objectdestroy.168Tm
+ _objectdestroy.199Tm
+ _objectdestroy.207Tm
+ _objectdestroy.214Tm
+ _objectdestroy.267Tm
+ _objectdestroy.47Tm
+ _sharedManager.onceToken.34294
+ _symbolic _____ 18PodcastsFoundation15MediaIdentifierO
+ _symbolic _____ So31AVAudioSessionActivationOptionsV
+ _type_layout_string So29AVAudioSessionCategoryOptionsV
+ _type_layout_string So32MPCPlaybackEngineEventPayloadKeya
- -[MPCItemBookmarker itemSmartTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:]
- -[MPCModelQueueFeeder controller:defersResponseReplacement:]
- -[MPIdentifierSet(MPCMQFAdditions) mpc_intersectsSet:ignoringModelKind:]
- -[_MPCPlaybackEnginePlayer smartTransitionDidReachPivotPointFrom:to:transitionTime:incomingItemAveragePostPivotTransitionRate:timeStamp:]
- -[_MPCQueueControllerBehaviorMusic _setRepeatType:]
- GCC_except_table1013
- GCC_except_table1262
- GCC_except_table1273
- GCC_except_table1291
- GCC_except_table1372
- GCC_except_table1373
- GCC_except_table1376
- GCC_except_table1381
- GCC_except_table1397
- GCC_except_table1487
- GCC_except_table1495
- GCC_except_table1503
- GCC_except_table17
- GCC_except_table1746
- GCC_except_table176
- GCC_except_table179
- GCC_except_table181
- GCC_except_table1840
- GCC_except_table1841
- GCC_except_table186
- GCC_except_table188
- GCC_except_table1955
- GCC_except_table1975
- GCC_except_table2003
- GCC_except_table201
- GCC_except_table2012
- GCC_except_table2017
- GCC_except_table2027
- GCC_except_table2037
- GCC_except_table205
- GCC_except_table2090
- GCC_except_table211
- GCC_except_table2121
- GCC_except_table215
- GCC_except_table2156
- GCC_except_table2157
- GCC_except_table2176
- GCC_except_table218
- GCC_except_table2184
- GCC_except_table2195
- GCC_except_table221
- GCC_except_table2218
- GCC_except_table2234
- GCC_except_table2463
- GCC_except_table2509
- GCC_except_table2565
- GCC_except_table261
- GCC_except_table2610
- GCC_except_table2612
- GCC_except_table2620
- GCC_except_table2673
- GCC_except_table2698
- GCC_except_table2881
- GCC_except_table2952
- GCC_except_table2963
- GCC_except_table2964
- GCC_except_table2988
- GCC_except_table2996
- GCC_except_table3037
- GCC_except_table3038
- GCC_except_table3054
- GCC_except_table3112
- GCC_except_table3127
- GCC_except_table3132
- GCC_except_table3166
- GCC_except_table3168
- GCC_except_table3175
- GCC_except_table3186
- GCC_except_table3191
- GCC_except_table3227
- GCC_except_table3272
- GCC_except_table3331
- GCC_except_table3350
- GCC_except_table3353
- GCC_except_table3355
- GCC_except_table3356
- GCC_except_table3385
- GCC_except_table3389
- GCC_except_table3456
- GCC_except_table3588
- GCC_except_table3589
- GCC_except_table3629
- GCC_except_table3631
- GCC_except_table3746
- GCC_except_table3780
- GCC_except_table3782
- GCC_except_table3790
- GCC_except_table3798
- GCC_except_table3864
- GCC_except_table3877
- GCC_except_table397
- GCC_except_table4083
- GCC_except_table4127
- GCC_except_table4129
- GCC_except_table4147
- GCC_except_table4216
- GCC_except_table426
- GCC_except_table4298
- GCC_except_table4426
- GCC_except_table4430
- GCC_except_table4441
- GCC_except_table4453
- GCC_except_table4455
- GCC_except_table4461
- GCC_except_table4470
- GCC_except_table4543
- GCC_except_table4614
- GCC_except_table4678
- GCC_except_table4703
- GCC_except_table474
- GCC_except_table479
- GCC_except_table4806
- GCC_except_table4814
- GCC_except_table4822
- GCC_except_table483
- GCC_except_table4831
- GCC_except_table4914
- GCC_except_table4921
- GCC_except_table4922
- GCC_except_table50
- GCC_except_table5038
- GCC_except_table509
- GCC_except_table5124
- GCC_except_table518
- GCC_except_table5181
- GCC_except_table5211
- GCC_except_table5236
- GCC_except_table5240
- GCC_except_table5243
- GCC_except_table5292
- GCC_except_table5324
- GCC_except_table535
- GCC_except_table538
- GCC_except_table541
- GCC_except_table5438
- GCC_except_table5443
- GCC_except_table5534
- GCC_except_table5781
- GCC_except_table5793
- GCC_except_table5802
- GCC_except_table5803
- GCC_except_table5804
- GCC_except_table5805
- GCC_except_table5806
- GCC_except_table5829
- GCC_except_table5844
- GCC_except_table6014
- GCC_except_table6025
- GCC_except_table6032
- GCC_except_table6075
- GCC_except_table621
- GCC_except_table6273
- GCC_except_table6364
- GCC_except_table637
- GCC_except_table638
- GCC_except_table6464
- GCC_except_table6506
- GCC_except_table654
- GCC_except_table655
- GCC_except_table6625
- GCC_except_table6657
- GCC_except_table6743
- GCC_except_table6841
- GCC_except_table6991
- GCC_except_table6995
- GCC_except_table7159
- GCC_except_table7161
- GCC_except_table7174
- GCC_except_table7209
- GCC_except_table7211
- GCC_except_table7215
- GCC_except_table7219
- GCC_except_table7221
- GCC_except_table7223
- GCC_except_table7225
- GCC_except_table7228
- GCC_except_table726
- GCC_except_table7286
- GCC_except_table7287
- GCC_except_table7451
- GCC_except_table81
- GCC_except_table88
- GCC_except_table893
- GCC_except_table959
- GCC_except_table966
- GCC_except_table971
- GCC_except_table973
- GCC_except_table976
- GCC_except_table981
- GCC_except_table982
- GCC_except_table987
- GCC_except_table990
- GCC_except_table993
- _MSVFastHexStringFromBytes.hexCharacters.30063
- _OBJC_CLASS_$_NSLock
- _OBJC_IVAR_$_MPCModelQueueFeeder._accessQueue
- _OBJC_IVAR_$_MPCModelQueueFeeder._diffLock
- __MPCAudioTapFinalize.2135
- __MPCAudioTapInit.2136
- __MPCAudioTapPrepareCallback.2134
- __MPCAudioTapProcess.2129
- __MPCAudioTapUnprepareCallback.2128
- __MSV_XXH_XXH32_update.10282
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelAlbum_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelGenericObject_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelObject_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelPlaylistEntry_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelPlaylist_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelRadioStation_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_CLASS_METHODS_MPModelSong_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_INSTANCE_METHODS_MPSectionedCollection_$_MQFDebugging
- __OBJC_$_CATEGORY_MPIdentifierSet_$_MPCAccumulatorAdditions
- __OBJC_$_CATEGORY_MPModelAlbum_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelGenericObject_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelObject_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelPlaylistEntry_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelPlaylist_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelRadioStation_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPModelSong_$_MPCModelQueueFeederAdditions
- __OBJC_$_CATEGORY_MPPlaybackContext_$_MPCPlaybackQueue
- __OBJC_$_CATEGORY_MPSectionedCollection_$_MQFDebugging
- __OBJC_$_CATEGORY_NSError_$_MPCDialogs
- __OBJC_$_CLASS_METHODS_MPIdentifierSet(MPCAccumulatorAdditions|MPCPlaybackEngineEventPayload|MPCMQFAdditions)
- __OBJC_$_CLASS_METHODS_NSError(MPCDialogs|MPCErrorController|MPCPlaybackEngineEventPayload|ICErrorProcessing)
- __OBJC_$_INSTANCE_METHODS_MPAVItem(MediaPlaybackCore|PreferredAudioTimePitchAlgorithm|Reuse|MediaPlaybackCore1|MediaPlaybackCore2|MFQueuePlayerItem|MPCReportingAdditions)
- __OBJC_$_INSTANCE_METHODS_MPCModelPlaybackContext(MPCPlaybackQueue|MPCSharedListening)
- __OBJC_$_INSTANCE_METHODS_MPIdentifierSet(MPCAccumulatorAdditions|MPCPlaybackEngineEventPayload|MPCMQFAdditions)
- __OBJC_$_INSTANCE_METHODS_MPModelAlbum(MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions|BehaviorMusicSharePlayAdditions|ICRadioContentReference)
- __OBJC_$_INSTANCE_METHODS_MPModelGenericObject(MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions|BehaviorMusicSharePlayAdditions|MPCModelRadioContentReference|Playability)
- __OBJC_$_INSTANCE_METHODS_MPModelObject(MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions|BehaviorMusicSharePlayAdditions|MPCModelRadioContentReference)
- __OBJC_$_INSTANCE_METHODS_MPModelPlaylist(MPCModelQueueFeederAdditions|BehaviorMusicSharePlayAdditions)
- __OBJC_$_INSTANCE_METHODS_MPModelPlaylistEntry(MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions|BehaviorMusicSharePlayAdditions)
- __OBJC_$_INSTANCE_METHODS_MPModelRadioStation(MPCModelQueueFeederAdditions|BehaviorMusicSharePlayAdditions)
- __OBJC_$_INSTANCE_METHODS_MPModelSong(MPCModelQueueFeederAdditions|MPCStoreFrontLocalEquivalencyMiddlewareAdditions|BehaviorMusicSharePlayAdditions|ICRadioContentReference)
- __OBJC_$_INSTANCE_METHODS_MPPlaybackContext(MPCPlaybackQueue|MPCSharedListening)
- __OBJC_$_INSTANCE_METHODS_NSError(MPCDialogs|MPCErrorController|MPCPlaybackEngineEventPayload|ICErrorProcessing)
- __OBJC_CLASS_PROTOCOLS_$_MPAVItem(MediaPlaybackCore|PreferredAudioTimePitchAlgorithm|Reuse|MediaPlaybackCore1|MediaPlaybackCore2|MFQueuePlayerItem|MPCReportingAdditions)
- __OBJC_CLASS_PROTOCOLS_$_MPIdentifierSet(MPCAccumulatorAdditions|MPCPlaybackEngineEventPayload|MPCMQFAdditions)
- __OBJC_CLASS_PROTOCOLS_$_NSError(MPCDialogs|MPCErrorController|MPCPlaybackEngineEventPayload|ICErrorProcessing)
- __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.5
- ___123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.626
- ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.502
- ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke_2.503
- ___43-[MPCModelQueueFeeder playbackInfoForItem:]_block_invoke.10
- ___45-[MPCModelQueueFeeder itemForItem:inSection:]_block_invoke.261
- ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke.265
- ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke_2.266
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.131
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.133
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.137
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.147
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.155
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.159
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.97
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke.98
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_2
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_2.145
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_2.148
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_3
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_3.149
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_4
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_4.150
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_5
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_6
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_7
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_8
- ___60-[MPCModelQueueFeeder controller:defersResponseReplacement:]_block_invoke_9
- ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.209
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.187
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.197
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.199
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.204
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.206
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.169
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.173
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.174
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke_2.175
- ___72-[MPIdentifierSet(MPCMQFAdditions) mpc_intersectsSet:ignoringModelKind:]_block_invoke
- ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.207
- ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.208
- ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.212
- ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.214
- ___76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.648
- ___76-[_MPCQueueControllerBehaviorMusicDataSourceState reloadSection:completion:]_block_invoke.91
- ___76-[_MPCQueueControllerBehaviorMusicDataSourceState reloadSection:completion:]_block_invoke.92
- ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke.132
- ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke.151
- ___82-[MPCMusicPlaybackIntentDataSource getArchiveFromIntent:configuration:completion:]_block_invoke_2.134
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.217
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.270
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.276
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.280
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.284
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.286
- ___Block_byref_object_copy_.10928
- ___Block_byref_object_copy_.11065
- ___Block_byref_object_copy_.1124
- ___Block_byref_object_copy_.11487
- ___Block_byref_object_copy_.12281
- ___Block_byref_object_copy_.1230
- ___Block_byref_object_copy_.13525
- ___Block_byref_object_copy_.1359
- ___Block_byref_object_copy_.13704
- ___Block_byref_object_copy_.14013
- ___Block_byref_object_copy_.1444
- ___Block_byref_object_copy_.14734
- ___Block_byref_object_copy_.15827
- ___Block_byref_object_copy_.16697
- ___Block_byref_object_copy_.18061
- ___Block_byref_object_copy_.18799
- ___Block_byref_object_copy_.20582
- ___Block_byref_object_copy_.2137
- ___Block_byref_object_copy_.23473
- ___Block_byref_object_copy_.23589
- ___Block_byref_object_copy_.23923
- ___Block_byref_object_copy_.25871
- ___Block_byref_object_copy_.29470
- ___Block_byref_object_copy_.3003
- ___Block_byref_object_copy_.30561
- ___Block_byref_object_copy_.30705
- ___Block_byref_object_copy_.31048
- ___Block_byref_object_copy_.31925
- ___Block_byref_object_copy_.32557
- ___Block_byref_object_copy_.33082
- ___Block_byref_object_copy_.33477
- ___Block_byref_object_copy_.347
- ___Block_byref_object_copy_.4237
- ___Block_byref_object_copy_.4360
- ___Block_byref_object_copy_.49
- ___Block_byref_object_copy_.4966
- ___Block_byref_object_copy_.5414
- ___Block_byref_object_copy_.7316
- ___Block_byref_object_copy_.7813
- ___Block_byref_object_copy_.80
- ___Block_byref_object_copy_.9390
- ___Block_byref_object_copy_.9560
- ___Block_byref_object_copy_.9897
- ___Block_byref_object_dispose_.10929
- ___Block_byref_object_dispose_.11066
- ___Block_byref_object_dispose_.1125
- ___Block_byref_object_dispose_.11488
- ___Block_byref_object_dispose_.12282
- ___Block_byref_object_dispose_.1231
- ___Block_byref_object_dispose_.13526
- ___Block_byref_object_dispose_.1360
- ___Block_byref_object_dispose_.13705
- ___Block_byref_object_dispose_.14014
- ___Block_byref_object_dispose_.1445
- ___Block_byref_object_dispose_.14735
- ___Block_byref_object_dispose_.15828
- ___Block_byref_object_dispose_.16698
- ___Block_byref_object_dispose_.18062
- ___Block_byref_object_dispose_.18800
- ___Block_byref_object_dispose_.20583
- ___Block_byref_object_dispose_.2138
- ___Block_byref_object_dispose_.23474
- ___Block_byref_object_dispose_.23590
- ___Block_byref_object_dispose_.23924
- ___Block_byref_object_dispose_.25872
- ___Block_byref_object_dispose_.29471
- ___Block_byref_object_dispose_.3004
- ___Block_byref_object_dispose_.30562
- ___Block_byref_object_dispose_.30706
- ___Block_byref_object_dispose_.31049
- ___Block_byref_object_dispose_.31926
- ___Block_byref_object_dispose_.32558
- ___Block_byref_object_dispose_.33083
- ___Block_byref_object_dispose_.33478
- ___Block_byref_object_dispose_.348
- ___Block_byref_object_dispose_.4238
- ___Block_byref_object_dispose_.4361
- ___Block_byref_object_dispose_.4967
- ___Block_byref_object_dispose_.50
- ___Block_byref_object_dispose_.5415
- ___Block_byref_object_dispose_.7317
- ___Block_byref_object_dispose_.7814
- ___Block_byref_object_dispose_.81
- ___Block_byref_object_dispose_.9391
- ___Block_byref_object_dispose_.9561
- ___Block_byref_object_dispose_.9898
- ___block_descriptor_104_e8_32s40s48r56r64r72r80r88r_e5_v8?0lr48l8s32l8r56l8r64l8r72l8r80l8r88l8s40l8
- ___block_descriptor_48_e8_32s40bs_e39_v24?0"MPPlaybackContext"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e39_v24?0"MPPlaybackContext"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e43_v24?0"MPRemotePlaybackQueue"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e32_v32?0q8"MPIdentifierSet"16^B24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e36_v24?0"MPCPlaybackEngineEvent"8^B16ls32l8r48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48s56w_e8_v16?0q8ls32l8s40l8s48l8w56l8
- ___block_descriptor_66_e8_32s40r48r_e5_v8?0lr40l8r48l8s32l8
- ___block_descriptor_72_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
- ___block_literal_global.10447
- ___block_literal_global.10683
- ___block_literal_global.10969
- ___block_literal_global.11.19264
- ___block_literal_global.110.29385
- ___block_literal_global.11132
- ___block_literal_global.11942
- ___block_literal_global.121.29367
- ___block_literal_global.1213
- ___block_literal_global.12406
- ___block_literal_global.127.29352
- ___block_literal_global.131.29353
- ___block_literal_global.133.29354
- ___block_literal_global.13518
- ___block_literal_global.13691
- ___block_literal_global.1394
- ___block_literal_global.14.29511
- ___block_literal_global.14148
- ___block_literal_global.143.21849
- ___block_literal_global.14506
- ___block_literal_global.146.21845
- ___block_literal_global.14619
- ___block_literal_global.152.19237
- ___block_literal_global.155.17169
- ___block_literal_global.160.23910
- ___block_literal_global.16058
- ___block_literal_global.165.18865
- ___block_literal_global.16612
- ___block_literal_global.168.23912
- ___block_literal_global.17416
- ___block_literal_global.178
- ___block_literal_global.18286
- ___block_literal_global.18877
- ___block_literal_global.19263
- ___block_literal_global.19544
- ___block_literal_global.198.20037
- ___block_literal_global.199
- ___block_literal_global.20135
- ___block_literal_global.20590
- ___block_literal_global.21510
- ___block_literal_global.21874
- ___block_literal_global.22531
- ___block_literal_global.2332
- ___block_literal_global.23461
- ___block_literal_global.24041
- ___block_literal_global.24426
- ___block_literal_global.25419
- ___block_literal_global.25946
- ___block_literal_global.264
- ___block_literal_global.2663
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.276
- ___block_literal_global.2775
- ___block_literal_global.27990
- ___block_literal_global.282.18075
- ___block_literal_global.28443
- ___block_literal_global.291
- ___block_literal_global.29510
- ___block_literal_global.296
- ___block_literal_global.30.24042
- ___block_literal_global.30429
- ___block_literal_global.30764
- ___block_literal_global.3135
- ___block_literal_global.31571
- ___block_literal_global.322.20592
- ___block_literal_global.3266
- ___block_literal_global.33504
- ___block_literal_global.3404
- ___block_literal_global.35073
- ___block_literal_global.365
- ___block_literal_global.37.33472
- ___block_literal_global.403.7301
- ___block_literal_global.4217
- ___block_literal_global.45.3405
- ___block_literal_global.47.21860
- ___block_literal_global.4707
- ___block_literal_global.487
- ___block_literal_global.489
- ___block_literal_global.491
- ___block_literal_global.496
- ___block_literal_global.556.12083
- ___block_literal_global.5709
- ___block_literal_global.6086
- ___block_literal_global.6243
- ___block_literal_global.723
- ___block_literal_global.726
- ___block_literal_global.7535
- ___block_literal_global.780
- ___block_literal_global.7889
- ___block_literal_global.8559
- ___block_literal_global.9.6078
- ___block_literal_global.9174
- ___unnamed_28
- _block_copy_helper.105
- _block_copy_helper.146
- _block_copy_helper.181
- _block_copy_helper.187
- _block_copy_helper.28
- _block_copy_helper.36
- _block_copy_helper.55
- _block_copy_helper.59
- _block_copy_helper.64
- _block_copy_helper.7
- _block_copy_helper.70
- _block_copy_helper.76
- _block_copy_helper.87
- _block_copy_helper.93
- _block_descriptor.107
- _block_descriptor.148
- _block_descriptor.183
- _block_descriptor.189
- _block_descriptor.30
- _block_descriptor.38
- _block_descriptor.57
- _block_descriptor.61
- _block_descriptor.66
- _block_descriptor.72
- _block_descriptor.78
- _block_descriptor.89
- _block_descriptor.9
- _block_descriptor.95
- _block_destroy_helper.106
- _block_destroy_helper.147
- _block_destroy_helper.182
- _block_destroy_helper.188
- _block_destroy_helper.29
- _block_destroy_helper.37
- _block_destroy_helper.56
- _block_destroy_helper.60
- _block_destroy_helper.65
- _block_destroy_helper.71
- _block_destroy_helper.77
- _block_destroy_helper.8
- _block_destroy_helper.88
- _block_destroy_helper.94
- _get_type_metadata 15Synchronization6AtomicVySiG.24
- _objc_msgSend$_setRepeatType:
- _objc_msgSend$controller:defersResponseReplacement:
- _objc_msgSend$itemSmartTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:
- _objc_msgSend$lock
- _objc_msgSend$unlock
- _objectdestroy.136Tm
- _objectdestroy.14Tm
- _objectdestroy.152Tm
- _objectdestroy.179Tm
- _objectdestroy.194Tm
- _objectdestroy.247Tm
- _objectdestroy.34Tm
- _objectdestroy.44Tm
- _objectdestroy.68Tm
- _sharedManager.onceToken.18876
- _type_layout_string So19NSKeyValueChangeKeya
- _type_layout_string So27MSVBackgroundTaskIdentifiera
CStrings:
+ " - activationToken: "
+ "@\"<MPCCriticalSectionTaskCancellable>\""
+ "ActiveItemIsAutoPlay"
+ "Attempt to connect section for different ID | %@ != %@"
+ "BehaviorMusic-setRepeatType-%@"
+ "ClearAllItems"
+ "DataSourceFailedToLoad"
+ "ExternalSetRepeatType"
+ "Failed to replace data source during reshuffle"
+ "FailedToFindDataSource"
+ "Item still placeholder after data source replacement: %@"
+ "MPCModelQueueFeeder expects non-nil response"
+ "MPCRequestController delegate did not call block passed to defersResponse:completion:."
+ "PrepareForCreateStation"
+ "Re-entering Playing state with a new item [itemChangeEvent: "
+ "ReshuffleFailedToFindStartItem"
+ "Returning static chapter artwork %{private,mask.hash}s for elapsed time %{private,mask.hash}f."
+ "Returning store backed chapter artwork with token %{private,mask.hash}@ for elapsed time: %{private,mask.hash}f."
+ "SetAutoPlayEnabled"
+ "TB,N,V_continuityMicrophoneUsed"
+ "TB,N,V_displayTranslationEnabled"
+ "TB,N,V_displayTransliterationEnabled"
+ "[%{public}@]-%{public}@ - overlappingTransitionDidReachPivotPoint - %{public}@ [%3.2fs] -> %{public}@ [%3.2fs] - timeStamp:%{public}@"
+ "[ALC:%{public}s] - Jump during an ongoing transition, cancelling transition"
+ "[ALC:%{public}s] - Jump with a previousTransitionOffsetData, cancelling transition"
+ "[AOT:%{public}@:%{public}@] setAutoPlayEnabled:%{BOOL}u | begin [] autoPlayState=%{public}@"
+ "[AOT:%{public}@:%{public}@] setAutoPlayEnabled:%{BOOL}u | ignoring setter [%{public}@] autoPlayState=%{public}@"
+ "[AOT:%{public}@:%{public}@] setAutoPlayEnabled:%{BOOL}u | transitioning [%{public}@] nextState=%{public}@"
+ "[AccountManager] - Updated account for bag change notification: %{public}@"
+ "[BMUS:%{public}@:%{public}@] _setRepeatType:reason: | committing edit [repeatType changed: %{public}@] repeatType=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | clearing data source section []"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | committing edit [data source replacement completed] resolvedStartingContentItemID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | data source replacement succeeded, re-enumerating []"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | enabled shuffle [] shuffleType=Songs wasShuffled=%{BOOL}u"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | extracted identifier registry [] identifierRegistry=%p"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | recreating data source [placeholder start item] sectionID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | replacing data source in identifier list []"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | reshuffle completed successfully []"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | rolling back edit [data source replacement failed] error=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | rolling back edit [failed to find datasource] sectionID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | rolling back edit [failed to find new start item] "
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | rolling back edit [item still placeholder after replacement] resolvedStartingContentItemID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | selected new start item identifiers [] startItemIdentifiers=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | starting reshuffle [] targetContentItemID=%{public}@"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | updating data source [] oldDataSource=%p newDataSource=%p"
+ "[BMUS:%{public}@:%{public}@] reshuffleWithTargetContentItemID:completion: | verified resolved item [] resolvedStartingContentItemID=%{public}@ type=%d"
+ "[MQF:%{public}@:%p] clearSectionProxy | clearing section proxy"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | applying new response [] newResponse=%p totalItemCount=%ld changeDetails=%{public}@"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler [start item satisfied] newResponse=%p isFinalResponse=%{BOOL}u"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler with error [%{public}@] newResponse=%p isFinalResponse=YES error=%{public}@"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | clearing old response.results [] oldResponse=%p newResponse=%p"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | clearing startIdentifiers [matched section ignoring modelKind] startIdentifiers=%{public}@ sectionIdentifiers=%{public}@"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | processing new response [] newResponse=%p progress=[%lld + %lld/%lld]"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | requestController.setNeedsReload [received non-final response]"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | updating Section [promoting storeRequest.storeIDs to sectionedModelObjects]"
+ "[MQF:%{public}@:%p] defersResponse:completion: | change details out of sync [identifierRegistry count mismatch] countDuringDiff=%ld countDuringApply=%ld"
+ "[MQF:%{public}@:%p] defersResponse:completion: | crashing [exception while computing change details] exception=%{public}@"
+ "[MQF:%{public}@:%p] defersResponse:completion: | crashing [invalid change details] reason=%{public}@ changeDetails=%{public}@"
+ "[PodcastAVItem/Chapters] Fetched %{private,mask.hash}s chapters for episode %{private,mask.hash}s."
+ "[PodcastAVItem] Failed to resolve chapter start time for %s: %@"
+ "_automaticResponseLoadingCriticalSection"
+ "_continuityMicrophoneUsed"
+ "_displayTranslationEnabled"
+ "_displayTransliterationEnabled"
+ "_loadNextPageCriticalSection"
+ "_notifyObserversForChange:"
+ "_setRepeatType:reason:"
+ "activeItem.isAutoPlay"
+ "already disabled"
+ "already enabled"
+ "already pending disable"
+ "already unknown"
+ "already unsupported"
+ "already waiting"
+ "clearSection"
+ "clearSectionProxy"
+ "cloneWithNewStartItemIdentifiers:identifierRegistry:"
+ "computedRateForChangePlaybackRateCommandEvent:"
+ "continuityMicrophoneUsed"
+ "controller:defersResponse:completion:"
+ "disabling"
+ "displayTranslationEnabled"
+ "displayTransliterationEnabled"
+ "enabling"
+ "enumerator produced no items after enabling shuffle"
+ "itemTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:"
+ "mpc_indexPathForIdentifiers returned nil"
+ "mpc_indexPathForIdentifiers:"
+ "mpc_indexPathForIdentifiers: returned invalid indexPath: %@"
+ "no datasource for section: %@"
+ "overlappingTransitionDidReachPivotPoint:"
+ "overlappingTransitionDidReachPivotPointFrom:to:transitionTime:incomingItemAveragePostPivotTransitionRate:transitionType:timeStamp:"
+ "pending disable - activeItem.isAutoPlay"
+ "recentItemChangeEvent"
+ "selectionDisabled"
+ "setContinuityMicrophoneUsed:"
+ "setDisplayTranslationEnabled:"
+ "setDisplayTransliterationEnabled:"
+ "setPlayable:"
+ "setPreloadedBag:"
+ "v40@0:8@\"MPCRequestController\"16@24@?<v@?>32"
+ "v64@0:8@\"<MFQueuePlayerItem>\"16@\"<MFQueuePlayerItem>\"24@\"<MFOverlappingTransitionTime>\"32d40q48@\"<MFTimeStamp>\"56"
+ "v64@0:8@16@24@32d40q48@56"
+ "wasPreviouslyActivated"
+ "\xf0Q"
- "@\"NSLock\""
- "BehaviorMusic-setRepeatType"
- "MPCMQFAdditions"
- "MPCRequestController delegate did not call block passed to defersResponseReplacement."
- "Re-entering Playing state with a new item"
- "[%{public}@]-%{public}@ - smartTransitionDidReachPivotPoint - %{public}@ [%3.2fs] -> %{public}@ [%3.2fs] - timeStamp:%{public}@"
- "[AOT:%{public}@:%{public}@] setAutoPlayEnabled:targetContentItemID:completion: | autoplay waiting for trigger [set enabled]"
- "[AOT:%{public}@:%{public}@] setAutoPlayEnabled:targetContentItemID:completion: | ignoring setter [autoPlayState=%{public}@] autoPlayEnabled:%{BOOL}u"
- "[BMUS:%{public}@:%{public}@] _setRepeatType: | committing edit [repeatType changed] repeatType=%{public}@"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | applying new response [] newResponse=%p totalItemCount=%ld changeDetails=%{public}@"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | calling loadingCompletionHandler [start item satisfied] newResponse=%p isFinalResponse=%{BOOL}u"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | calling loadingCompletionHandler with error [%{public}@] newResponse=%p isFinalResponse=YES error=%{public}@"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | clearing old response.results [] oldResponse=%p newResponse=%p"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | clearing startIdentifiers [matched section ignoring modelKind] startIdentifiers=%{public}@ sectionIdentifiers=%{public}@"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | processing new response [] newResponse=%p progress=[%lld + %lld/%lld]"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | requestController.setNeedsReload [received non-final response]"
- "[MQF:%{public}@:%p] controller:defersResponseReplacement: | updating Section [promoting storeRequest.storeIDs to sectionedModelObjects]"
- "[MQF:%{public}@:%p] defersResponseReplacement | change details out of sync [identifierRegistry count mismatch] countDuringDiff=%ld countDuringApply=%ld"
- "[MQF:%{public}@:%p] defersResponseReplacement | crashing [exception while computing change details] exception=%{public}@"
- "[MQF:%{public}@:%p] defersResponseReplacement | crashing [invalid change details] reason=%{public}@ changeDetails=%{public}@"
- "_diffLock"
- "_setRepeatType:"
- "com.apple.MediaPlaybackCore.MPCModelQueueFeeder.accessQueue"
- "indexPathForItemWithIdentifiersIntersectingSet returned nil"
- "itemSmartTransitionDidReachPivotPoint:to:incomingItemAveragePostPivotTransitionRate:time:"
- "smartTransitionDidReachPivotPoint:"
- "smartTransitionDidReachPivotPointFrom:to:transitionTime:incomingItemAveragePostPivotTransitionRate:timeStamp:"
- "unlock"
- "v32@0:8@\"MPCRequestController\"16@?<v@?>24"
- "\xf0A"

```
