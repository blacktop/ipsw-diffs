## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore`

```diff

-26100.26.28.501.0
-  __TEXT.__text: 0x3c9184
-  __TEXT.__objc_methlist: 0x16490
+26140.26.31.301.0
+  __TEXT.__text: 0x3cd590
+  __TEXT.__objc_methlist: 0x164e0
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__const: 0xd698
-  __TEXT.__cstring: 0x22c34
-  __TEXT.__constg_swiftt: 0x6568
-  __TEXT.__swift5_typeref: 0x4574
+  __TEXT.__const: 0xd880
+  __TEXT.__cstring: 0x230cc
+  __TEXT.__constg_swiftt: 0x65f8
+  __TEXT.__swift5_typeref: 0x462a
   __TEXT.__swift5_builtin: 0x578
-  __TEXT.__swift5_reflstr: 0x4902
-  __TEXT.__swift5_fieldmd: 0x47f0
-  __TEXT.__swift5_assocty: 0x9f0
-  __TEXT.__oslogstring: 0x41a8b
-  __TEXT.__swift5_proto: 0x794
-  __TEXT.__swift5_types: 0x448
-  __TEXT.__swift5_capture: 0x642c
-  __TEXT.__swift_as_entry: 0x2bc
+  __TEXT.__swift5_reflstr: 0x4972
+  __TEXT.__swift5_fieldmd: 0x4824
+  __TEXT.__swift5_assocty: 0xa20
+  __TEXT.__oslogstring: 0x41d88
+  __TEXT.__swift5_proto: 0x7a8
+  __TEXT.__swift5_types: 0x44c
+  __TEXT.__swift5_capture: 0x6514
+  __TEXT.__swift_as_entry: 0x2c0
   __TEXT.__swift_as_ret: 0x320
-  __TEXT.__swift_as_cont: 0x8a8
+  __TEXT.__swift_as_cont: 0x8ac
   __TEXT.__swift5_mpenum: 0xb8
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x5480
+  __TEXT.__gcc_except_tab: 0x560c
   __TEXT.__ustring: 0x4d4
-  __TEXT.__unwind_info: 0xb010
-  __TEXT.__eh_frame: 0x9c98
+  __TEXT.__unwind_info: 0xac30
+  __TEXT.__eh_frame: 0x9da0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c00
+  __DATA_CONST.__const: 0x2c08
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x280
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbef8
+  __DATA_CONST.__objc_selrefs: 0xbf40
   __DATA_CONST.__objc_protorefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0x2a50
-  __AUTH_CONST.__const: 0x1e1d0
-  __AUTH_CONST.__cfstring: 0x1dd80
-  __AUTH_CONST.__objc_const: 0x30a08
-  __AUTH_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__got: 0x2a68
+  __AUTH_CONST.__const: 0x1e4a0
+  __AUTH_CONST.__cfstring: 0x1dec0
+  __AUTH_CONST.__objc_const: 0x30b40
+  __AUTH_CONST.__objc_intobj: 0x888
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x26a0
+  __AUTH_CONST.__auth_got: 0x26f8
   __AUTH.__objc_data: 0x4808
-  __AUTH.__data: 0x1ec0
-  __DATA.__objc_ivar: 0x1a20
-  __DATA.__data: 0x5670
-  __DATA.__bss: 0xbd98
-  __DATA.__common: 0xe0
-  __DATA_DIRTY.__objc_data: 0x3108
-  __DATA_DIRTY.__data: 0x5b48
+  __AUTH.__data: 0x1ef0
+  __DATA.__objc_ivar: 0x1a34
+  __DATA.__data: 0x56d0
+  __DATA.__bss: 0xc018
+  __DATA.__common: 0xe8
+  __DATA_DIRTY.__objc_data: 0x3100
+  __DATA_DIRTY.__data: 0x5ba8
   __DATA_DIRTY.__bss: 0x1b30
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19030
-  Symbols:   22739
-  CStrings:  7532
+  Functions: 19119
+  Symbols:   22781
+  CStrings:  7559
 
Symbols:
+ -[MPCAssistantSendCommandResult optionalError]
+ -[MPCQueueController _setTargetContentItemID:source:direction:]
+ -[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]
+ -[_MPCMediaRemotePublisher _clearErrorReturningCommandID:]
+ -[_MPCMediaRemotePublisher _invalidateAllCommandCriticalSectionAssertions]
+ -[_MPCMediaRemotePublisher _setErrorReturningCommandID:]
+ -[_MPCMediaRemotePublisher isPerformingErrorReturningCommand]
+ -[_MPCToggleTransitionsCommand isDialogCapable]
+ -[_MPCToggleTransitionsCommand isDisabled]
+ -[_MPCToggleTransitionsCommand setDialogCapable:]
+ -[_MPCToggleTransitionsCommand setDisabled:]
+ GCC_except_table1003
+ GCC_except_table1006
+ GCC_except_table1008
+ GCC_except_table1015
+ GCC_except_table1017
+ GCC_except_table1030
+ GCC_except_table1034
+ GCC_except_table1040
+ GCC_except_table1046
+ GCC_except_table1049
+ GCC_except_table1052
+ GCC_except_table1241
+ GCC_except_table1245
+ GCC_except_table1247
+ GCC_except_table1415
+ GCC_except_table1419
+ GCC_except_table1463
+ GCC_except_table1474
+ GCC_except_table1481
+ GCC_except_table1488
+ GCC_except_table1525
+ GCC_except_table1537
+ GCC_except_table1546
+ GCC_except_table1589
+ GCC_except_table1762
+ GCC_except_table1764
+ GCC_except_table1777
+ GCC_except_table1782
+ GCC_except_table1852
+ GCC_except_table1938
+ GCC_except_table2052
+ GCC_except_table2072
+ GCC_except_table2074
+ GCC_except_table2102
+ GCC_except_table2113
+ GCC_except_table2119
+ GCC_except_table2121
+ GCC_except_table2124
+ GCC_except_table2135
+ GCC_except_table2145
+ GCC_except_table2261
+ GCC_except_table2312
+ GCC_except_table2316
+ GCC_except_table2319
+ GCC_except_table2347
+ GCC_except_table2371
+ GCC_except_table2404
+ GCC_except_table2645
+ GCC_except_table2673
+ GCC_except_table2700
+ GCC_except_table2843
+ GCC_except_table2864
+ GCC_except_table2872
+ GCC_except_table2897
+ GCC_except_table2899
+ GCC_except_table2904
+ GCC_except_table2908
+ GCC_except_table2910
+ GCC_except_table2912
+ GCC_except_table2914
+ GCC_except_table2917
+ GCC_except_table2945
+ GCC_except_table2952
+ GCC_except_table2957
+ GCC_except_table2959
+ GCC_except_table2963
+ GCC_except_table2969
+ GCC_except_table2974
+ GCC_except_table2977
+ GCC_except_table2980
+ GCC_except_table3000
+ GCC_except_table3050
+ GCC_except_table3136
+ GCC_except_table3140
+ GCC_except_table3152
+ GCC_except_table3176
+ GCC_except_table3188
+ GCC_except_table3235
+ GCC_except_table3244
+ GCC_except_table3301
+ GCC_except_table3319
+ GCC_except_table3326
+ GCC_except_table3367
+ GCC_except_table3371
+ GCC_except_table3381
+ GCC_except_table3392
+ GCC_except_table3396
+ GCC_except_table3440
+ GCC_except_table3485
+ GCC_except_table3490
+ GCC_except_table3606
+ GCC_except_table3627
+ GCC_except_table3634
+ GCC_except_table3661
+ GCC_except_table3665
+ GCC_except_table3675
+ GCC_except_table3732
+ GCC_except_table3739
+ GCC_except_table3743
+ GCC_except_table3814
+ GCC_except_table387
+ GCC_except_table389
+ GCC_except_table3917
+ GCC_except_table3921
+ GCC_except_table3933
+ GCC_except_table3949
+ GCC_except_table3956
+ GCC_except_table3966
+ GCC_except_table442
+ GCC_except_table450
+ GCC_except_table460
+ GCC_except_table471
+ GCC_except_table4759
+ GCC_except_table4794
+ GCC_except_table4796
+ GCC_except_table4804
+ GCC_except_table4812
+ GCC_except_table4828
+ GCC_except_table4840
+ GCC_except_table4850
+ GCC_except_table4861
+ GCC_except_table4874
+ GCC_except_table4921
+ GCC_except_table4936
+ GCC_except_table4953
+ GCC_except_table4958
+ GCC_except_table4964
+ GCC_except_table5009
+ GCC_except_table5044
+ GCC_except_table5127
+ GCC_except_table5482
+ GCC_except_table554
+ GCC_except_table5583
+ GCC_except_table571
+ GCC_except_table5733
+ GCC_except_table5758
+ GCC_except_table588
+ GCC_except_table5930
+ GCC_except_table5996
+ GCC_except_table6021
+ GCC_except_table6056
+ GCC_except_table6059
+ GCC_except_table6062
+ GCC_except_table6148
+ GCC_except_table6365
+ GCC_except_table6382
+ GCC_except_table6833
+ GCC_except_table7177
+ GCC_except_table7187
+ GCC_except_table7277
+ GCC_except_table7286
+ GCC_except_table7370
+ GCC_except_table7377
+ GCC_except_table7395
+ GCC_except_table7446
+ GCC_except_table7450
+ GCC_except_table7455
+ GCC_except_table7471
+ GCC_except_table839
+ GCC_except_table895
+ GCC_except_table971
+ OBJC_IVAR_$_MPCQueueController._lastChangeDirection
+ OBJC_IVAR_$__MPCMediaRemotePublisher._activeCommandCriticalSectionAssertions
+ OBJC_IVAR_$__MPCMediaRemotePublisher._errorReturningCommandID
+ OBJC_IVAR_$__MPCToggleTransitionsCommand._dialogCapable
+ OBJC_IVAR_$__MPCToggleTransitionsCommand._disabled
+ _OBJC_CLASS_$_NSListFormatter
+ __237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke
+ __78-[MPCQueueController finalizeStateRestorationWithLoadingItemReady:completion:]_block_invoke
+ __88-[_MPCQueueControllerBehaviorMusic performInsertCommand:targetContentItemID:completion:]_block_invoke
+ __MPCEnsureNowPlayingContentItemCached
+ __OBJC_$_INSTANCE_VARIABLES__MPCToggleTransitionsCommand
+ __OBJC_$_PROP_LIST_MPCToggleTransitionsCommand
+ ___237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke
+ ___237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke_2
+ ____MPCEnsureNowPlayingContentItemCached_block_invoke
+ ___block_descriptor_117_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0l
+ ___block_descriptor_117_e8_32s40s48s56s64s72s80s88bs96r_e61_v32?0"MPRemoteCommandStatus"8"NSString"16"NSDictionary"24l
+ ___block_descriptor_56_e8_32s40s48s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8l
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r
+ __swift_closure_destructor.11Tm
+ __swift_closure_destructor.137Tm
+ __swift_closure_destructor.64Tm
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation021_ObjectiveCBridgeableD0SCs0D0
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation13CustomNSErrorSCs0D0
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_AC01_dE8Protocol
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_SY
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableD0
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomI0
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC34MPCPlaybackEngineInternalErrorCodeLeVSHSCSQ
+ _associated conformance So34MPCPlaybackEngineInternalErrorCodeV10Foundation01_dE8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So34MPCPlaybackEngineInternalErrorCodeV10Foundation01_dE8ProtocolSCSQ
+ _kMRMediaRemoteSystemBooksApplicationDisplayIdentifier
+ _objc_msgSend$_clearErrorReturningCommandID:
+ _objc_msgSend$_invalidateAllCommandCriticalSectionAssertions
+ _objc_msgSend$_setErrorReturningCommandID:
+ _objc_msgSend$_setTargetContentItemID:source:direction:
+ _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:
+ _objc_msgSend$isPerformingErrorReturningCommand
+ _objc_msgSend$setDialogCapable:
+ _objc_msgSend$setDisabled:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$sharedPrivacyInfoForUserIdentity:
+ _objc_msgSend$shouldBlockPersonalizedNetworkRequestsForMusic
+ _objc_msgSend$stringFromItems:
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic So7NSErrorC
+ _symbolic _____ SC34MPCPlaybackEngineInternalErrorCodeLeV
+ _symbolic _____ So34MPCPlaybackEngineInternalErrorCodeV
+ _symbolic yyYbcSg
+ _type_layout_string SC34MPCPlaybackEngineInternalErrorCodeLeV
- -[MPAVItem(MFQueuePlayerItem) setCurrentItemTransition:]
- -[MPCQueueController _setTargetContentItemID:source:]
- -[MPCQueueController jumpToContentItemID:]
- -[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]
- GCC_except_table1002
- GCC_except_table1005
- GCC_except_table1007
- GCC_except_table1014
- GCC_except_table1016
- GCC_except_table1029
- GCC_except_table1033
- GCC_except_table1039
- GCC_except_table1045
- GCC_except_table1048
- GCC_except_table1051
- GCC_except_table1240
- GCC_except_table1244
- GCC_except_table1246
- GCC_except_table1414
- GCC_except_table1418
- GCC_except_table1462
- GCC_except_table1473
- GCC_except_table1480
- GCC_except_table1487
- GCC_except_table1524
- GCC_except_table1536
- GCC_except_table1545
- GCC_except_table1588
- GCC_except_table1761
- GCC_except_table1763
- GCC_except_table1776
- GCC_except_table1781
- GCC_except_table1851
- GCC_except_table1936
- GCC_except_table2051
- GCC_except_table2071
- GCC_except_table2073
- GCC_except_table2101
- GCC_except_table2112
- GCC_except_table2118
- GCC_except_table2120
- GCC_except_table2123
- GCC_except_table2134
- GCC_except_table2144
- GCC_except_table2260
- GCC_except_table2311
- GCC_except_table2315
- GCC_except_table2318
- GCC_except_table2346
- GCC_except_table2370
- GCC_except_table2403
- GCC_except_table2644
- GCC_except_table2672
- GCC_except_table2699
- GCC_except_table2842
- GCC_except_table2863
- GCC_except_table2870
- GCC_except_table2896
- GCC_except_table2898
- GCC_except_table2903
- GCC_except_table2907
- GCC_except_table2909
- GCC_except_table2911
- GCC_except_table2913
- GCC_except_table2916
- GCC_except_table2944
- GCC_except_table2951
- GCC_except_table2956
- GCC_except_table2958
- GCC_except_table2962
- GCC_except_table2967
- GCC_except_table2973
- GCC_except_table2976
- GCC_except_table2979
- GCC_except_table2999
- GCC_except_table3049
- GCC_except_table3135
- GCC_except_table3139
- GCC_except_table3150
- GCC_except_table3175
- GCC_except_table3187
- GCC_except_table3233
- GCC_except_table3243
- GCC_except_table3300
- GCC_except_table3318
- GCC_except_table3325
- GCC_except_table3366
- GCC_except_table3370
- GCC_except_table3380
- GCC_except_table3391
- GCC_except_table3395
- GCC_except_table3439
- GCC_except_table3484
- GCC_except_table3489
- GCC_except_table3605
- GCC_except_table3626
- GCC_except_table3633
- GCC_except_table3660
- GCC_except_table3664
- GCC_except_table3674
- GCC_except_table3731
- GCC_except_table3738
- GCC_except_table3742
- GCC_except_table3813
- GCC_except_table386
- GCC_except_table388
- GCC_except_table3916
- GCC_except_table3920
- GCC_except_table3932
- GCC_except_table3948
- GCC_except_table3955
- GCC_except_table3965
- GCC_except_table441
- GCC_except_table449
- GCC_except_table459
- GCC_except_table470
- GCC_except_table4761
- GCC_except_table4795
- GCC_except_table4797
- GCC_except_table4805
- GCC_except_table4813
- GCC_except_table4829
- GCC_except_table4841
- GCC_except_table4851
- GCC_except_table4862
- GCC_except_table4875
- GCC_except_table4922
- GCC_except_table4937
- GCC_except_table4954
- GCC_except_table4959
- GCC_except_table4965
- GCC_except_table5010
- GCC_except_table5045
- GCC_except_table5124
- GCC_except_table5480
- GCC_except_table553
- GCC_except_table5581
- GCC_except_table569
- GCC_except_table5731
- GCC_except_table5756
- GCC_except_table586
- GCC_except_table5928
- GCC_except_table5994
- GCC_except_table6019
- GCC_except_table6054
- GCC_except_table6057
- GCC_except_table6060
- GCC_except_table6146
- GCC_except_table6363
- GCC_except_table6380
- GCC_except_table6827
- GCC_except_table7171
- GCC_except_table7181
- GCC_except_table7271
- GCC_except_table7280
- GCC_except_table7362
- GCC_except_table7369
- GCC_except_table7387
- GCC_except_table7438
- GCC_except_table7439
- GCC_except_table7442
- GCC_except_table7463
- GCC_except_table838
- GCC_except_table894
- GCC_except_table970
- __204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke_2
- ___42-[MPCQueueController jumpToContentItemID:]_block_invoke
- ___81-[_MPCMusicPlayerControllerServer _ensureCacheFilledForContentItemID:completion:]_block_invoke
- ___88-[_MPCQueueControllerBehaviorMusic performInsertCommand:targetContentItemID:completion:]_block_invoke_2
- ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
- ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e61_v32?0"MPRemoteCommandStatus"8"NSString"16"NSDictionary"24l
- ___block_descriptor_64_e8_32s40s48s56s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8l
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
- __swift_closure_destructor.130Tm
- _associated conformance 17MediaPlaybackCore14ItemTransitionOSHAASQ
- _objc_msgSend$_setTargetContentItemID:source:
- _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:
- _objc_msgSend$currentItemTransition
- _objc_msgSend$setAppBundleID:
- _objc_msgSend$setCurrentItemTransition:
- _symbolic _____ 17MediaPlaybackCore14ItemTransitionO
CStrings:
+ "Insertion position requires a non-empty afterContentItemID."
+ "InvalidAudioSessionActivation"
+ "MPCTransitionStyle"
+ "MPCTransitionsSettingsErrorCodes"
+ "MediaPlaybackCore.ensureNowPlayingContentItemCached"
+ "NSString *_MPCPlaybackAccountIDForAccountIDs(NSString *__strong, NSString *__strong)"
+ "Playback stopped"
+ "Song transitions are currently unavailable"
+ "TRANSITIONS_UNAVAILABLE_ACTION_HIRES"
+ "TRANSITIONS_UNAVAILABLE_ACTION_SHAREPLAY"
+ "TRANSITIONS_UNAVAILABLE_ACTION_SING"
+ "TRANSITIONS_UNAVAILABLE_ALERT_MESSAGE"
+ "TRANSITIONS_UNAVAILABLE_ALERT_TITLE"
+ "TRANSITIONS_UNAVAILABLE_ALERT_TITLE_GENERIC"
+ "TRANSITIONS_UNAVAILABLE_BODY_NAME_GENERIC"
+ "TRANSITIONS_UNAVAILABLE_LIVESTREAM_ALERT_MESSAGE"
+ "TRANSITIONS_UNAVAILABLE_MUSIC_VIDEO_ALERT_MESSAGE"
+ "TRANSITIONS_UNAVAILABLE_SETTINGS"
+ "TransitionsUnavailable"
+ "TransitionsUnavailableHighResolutionLossless"
+ "TransitionsUnavailableMusicVideo"
+ "TransitionsUnavailableSharePlay"
+ "TransitionsUnavailableUnsupportedContent"
+ "TransitionsUnavailableVocalAttenuation"
+ "[ALC:%{public}s] - Effective start %{public}f within cold-start margin %{public}f of overlap start %{public}f, cancelling transition"
+ "[AccountManager] Unexpected combo account, recovering with first/last tokens: %{public}@"
+ "[AccountManager] combining an already-combo borrowing account ID: %@"
+ "[AccountManager] combining an already-combo primary account ID: %@"
+ "[BMUS:%{public}@:%{public}@] performInsertCommand: | failed [insertion position %ld requires a non-empty afterContentItemID]"
+ "[PL:%{public}s] AUDIO SESSION CONTROLLER: Invalidating - Alarm category"
+ "[PL:%{public}s] STACK PROCESSING: Skipping snapshot restore of non-positive start time %{public}f for: %{public}s [%{public}s]"
+ "[PL:%{public}s] TRANSITION: Effective start %{public}f within cold-start margin %{public}f of overlap start %{public}f, cancelling crossfade [%{public}s]"
+ "[PL:%{public}s] TRANSITION: Jump during an ongoing crossfade, cancelling [%{public}s]"
+ "[PSYNC:%{public}@:%{public}@] setTargetContentItemID:%{public}@ source:%{public}@ direction:%{public}@ | updating target"
+ "[PUB:%{public}@] _invalidateAllCommandCriticalSectionAssertions | force-invalidating stranded critical section assertion [publisher torn down before _performCommandEvent completion] commandID=%{public}@"
+ "[PUB:%{public}@] commandCenter:didTimeoutCommandEvent:%{public}@ | force-invalidating stranded critical section assertion [command timed out before _performCommandEvent completion]"
+ "com.apple.WorkflowKit.BackgroundShortcutRunner"
- "MPCMusicPlayerControllerServer.ensureCacheFilled"
- "Unexpected combo account: %@"
- "[ALC:%{public}s] - Jump position passes overlap start, cancelling transition"
- "[PL:%{public}s] TRANSITION: Jump position passes overlap start, cancelling crossfade [%{public}s]"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | failing skip [%{public}@]"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | updating target"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | validating item [] behavior=%{public}@"
- "[PSYNC:%{public}@:%{public}@] setTargetContentItemID:%{public}@ source:%{public}@ | updating target"
- "com.apple.NanoBooks"
- "com.apple.iBooks"
```
