## MediaPlaybackCore

> `/System/iOSSupport/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore`

```diff

-26100.26.28.501.0
-  __TEXT.__text: 0x44f6f0
-  __TEXT.__objc_methlist: 0x174e0
+26140.26.31.301.0
+  __TEXT.__text: 0x458d88
+  __TEXT.__objc_methlist: 0x175a0
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__const: 0xf728
-  __TEXT.__cstring: 0x240ee
-  __TEXT.__constg_swiftt: 0x7784
-  __TEXT.__swift5_typeref: 0x50a2
+  __TEXT.__const: 0xf980
+  __TEXT.__cstring: 0x245bc
+  __TEXT.__constg_swiftt: 0x7820
+  __TEXT.__swift5_typeref: 0x510c
   __TEXT.__swift5_builtin: 0x67c
-  __TEXT.__swift5_reflstr: 0x55e2
-  __TEXT.__swift5_fieldmd: 0x5230
-  __TEXT.__swift5_assocty: 0xb28
-  __TEXT.__oslogstring: 0x47f4e
-  __TEXT.__swift5_proto: 0x8a4
-  __TEXT.__swift5_types: 0x510
-  __TEXT.__swift5_capture: 0x8044
-  __TEXT.__swift_as_entry: 0x47c
-  __TEXT.__swift_as_ret: 0x584
-  __TEXT.__swift_as_cont: 0xd74
+  __TEXT.__swift5_reflstr: 0x56e2
+  __TEXT.__swift5_fieldmd: 0x5294
+  __TEXT.__swift5_assocty: 0xb58
+  __TEXT.__oslogstring: 0x486c0
+  __TEXT.__swift5_proto: 0x8b8
+  __TEXT.__swift5_types: 0x514
+  __TEXT.__swift5_capture: 0x8424
+  __TEXT.__swift_as_entry: 0x48c
+  __TEXT.__swift_as_ret: 0x590
+  __TEXT.__swift_as_cont: 0xd9c
   __TEXT.__swift5_mpenum: 0xb8
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x54e0
+  __TEXT.__gcc_except_tab: 0x5654
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0xccc0
-  __TEXT.__eh_frame: 0xf39c
+  __TEXT.__unwind_info: 0xce78
+  __TEXT.__eh_frame: 0xf764
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8ea8
-  __DATA_CONST.__objc_classlist: 0xce8
+  __DATA_CONST.__const: 0x8eb0
+  __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x280
   __DATA_CONST.__objc_protolist: 0x7a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc580
+  __DATA_CONST.__objc_selrefs: 0xc5e8
   __DATA_CONST.__objc_protorefs: 0x380
-  __DATA_CONST.__objc_superrefs: 0x6b8
+  __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0x30d8
-  __AUTH_CONST.__const: 0x1b908
-  __AUTH_CONST.__cfstring: 0x1e100
-  __AUTH_CONST.__objc_const: 0x33170
-  __AUTH_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__got: 0x30e8
+  __AUTH_CONST.__const: 0x1c2b0
+  __AUTH_CONST.__cfstring: 0x1e240
+  __AUTH_CONST.__objc_const: 0x33420
+  __AUTH_CONST.__objc_intobj: 0x888
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x32c8
-  __AUTH.__objc_data: 0x53b0
-  __AUTH.__data: 0x2a40
-  __DATA.__objc_ivar: 0x1a48
-  __DATA.__data: 0x6598
-  __DATA.__bss: 0xdab8
-  __DATA.__common: 0x1f0
-  __DATA_DIRTY.__objc_data: 0x38e8
-  __DATA_DIRTY.__data: 0x5cc0
+  __AUTH_CONST.__auth_got: 0x32f8
+  __AUTH.__objc_data: 0x5418
+  __AUTH.__data: 0x2a70
+  __DATA.__objc_ivar: 0x1a68
+  __DATA.__data: 0x6668
+  __DATA.__bss: 0xdd48
+  __DATA.__common: 0x200
+  __DATA_DIRTY.__objc_data: 0x3900
+  __DATA_DIRTY.__data: 0x5d40
   __DATA_DIRTY.__bss: 0x1b28
   __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22298
-  Symbols:   23507
-  CStrings:  7900
+  Functions: 22517
+  Symbols:   23581
+  CStrings:  7939
 
Symbols:
+ +[MPCAUHostingServiceKeepalive startIfNeeded]
+ -[MPCAUHostingServiceKeepalive .cxx_destruct]
+ -[MPCAUHostingServiceKeepalive _arm]
+ -[MPCAUHostingServiceKeepalive _mediaServerDidDie:]
+ -[MPCAUHostingServiceKeepalive _mediaServerDidRestart:]
+ -[MPCAUHostingServiceKeepalive _start]
+ -[MPCAUHostingServiceKeepalive _teardown]
+ -[MPCAUHostingServiceKeepalive dealloc]
+ -[MPCAUHostingServiceKeepalive init]
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
+ GCC_except_table1001
+ GCC_except_table1004
+ GCC_except_table1007
+ GCC_except_table1194
+ GCC_except_table1198
+ GCC_except_table1200
+ GCC_except_table1368
+ GCC_except_table1370
+ GCC_except_table1411
+ GCC_except_table1422
+ GCC_except_table1429
+ GCC_except_table1436
+ GCC_except_table1473
+ GCC_except_table1485
+ GCC_except_table1494
+ GCC_except_table1537
+ GCC_except_table1712
+ GCC_except_table1725
+ GCC_except_table1730
+ GCC_except_table1800
+ GCC_except_table1884
+ GCC_except_table1885
+ GCC_except_table1993
+ GCC_except_table2013
+ GCC_except_table2015
+ GCC_except_table2043
+ GCC_except_table2052
+ GCC_except_table2057
+ GCC_except_table2059
+ GCC_except_table2062
+ GCC_except_table2073
+ GCC_except_table2083
+ GCC_except_table2198
+ GCC_except_table2249
+ GCC_except_table2253
+ GCC_except_table2256
+ GCC_except_table2282
+ GCC_except_table2306
+ GCC_except_table2338
+ GCC_except_table2579
+ GCC_except_table2607
+ GCC_except_table2634
+ GCC_except_table2777
+ GCC_except_table2798
+ GCC_except_table2805
+ GCC_except_table2806
+ GCC_except_table2838
+ GCC_except_table2842
+ GCC_except_table2844
+ GCC_except_table2846
+ GCC_except_table2848
+ GCC_except_table2851
+ GCC_except_table2877
+ GCC_except_table2884
+ GCC_except_table2889
+ GCC_except_table2895
+ GCC_except_table2900
+ GCC_except_table2901
+ GCC_except_table2906
+ GCC_except_table2909
+ GCC_except_table2912
+ GCC_except_table2932
+ GCC_except_table2982
+ GCC_except_table3072
+ GCC_except_table3083
+ GCC_except_table3084
+ GCC_except_table3108
+ GCC_except_table3116
+ GCC_except_table3157
+ GCC_except_table3158
+ GCC_except_table3165
+ GCC_except_table3222
+ GCC_except_table3240
+ GCC_except_table3247
+ GCC_except_table3289
+ GCC_except_table3291
+ GCC_except_table3309
+ GCC_except_table3313
+ GCC_except_table3351
+ GCC_except_table3396
+ GCC_except_table3401
+ GCC_except_table344
+ GCC_except_table346
+ GCC_except_table3518
+ GCC_except_table3539
+ GCC_except_table3546
+ GCC_except_table3571
+ GCC_except_table3575
+ GCC_except_table3585
+ GCC_except_table3642
+ GCC_except_table3647
+ GCC_except_table3651
+ GCC_except_table3720
+ GCC_except_table3821
+ GCC_except_table3832
+ GCC_except_table3848
+ GCC_except_table3854
+ GCC_except_table3864
+ GCC_except_table392
+ GCC_except_table3992
+ GCC_except_table400
+ GCC_except_table4037
+ GCC_except_table4038
+ GCC_except_table4039
+ GCC_except_table4059
+ GCC_except_table4070
+ GCC_except_table408
+ GCC_except_table4088
+ GCC_except_table4093
+ GCC_except_table4109
+ GCC_except_table4132
+ GCC_except_table4143
+ GCC_except_table417
+ GCC_except_table4232
+ GCC_except_table4251
+ GCC_except_table4264
+ GCC_except_table4275
+ GCC_except_table4306
+ GCC_except_table4477
+ GCC_except_table4478
+ GCC_except_table4655
+ GCC_except_table4690
+ GCC_except_table4692
+ GCC_except_table4700
+ GCC_except_table4708
+ GCC_except_table4723
+ GCC_except_table4731
+ GCC_except_table4739
+ GCC_except_table4762
+ GCC_except_table4806
+ GCC_except_table4821
+ GCC_except_table4837
+ GCC_except_table4840
+ GCC_except_table4846
+ GCC_except_table4893
+ GCC_except_table4930
+ GCC_except_table500
+ GCC_except_table5015
+ GCC_except_table517
+ GCC_except_table5336
+ GCC_except_table5337
+ GCC_except_table534
+ GCC_except_table5408
+ GCC_except_table5503
+ GCC_except_table5653
+ GCC_except_table5678
+ GCC_except_table5847
+ GCC_except_table5912
+ GCC_except_table5937
+ GCC_except_table5972
+ GCC_except_table5975
+ GCC_except_table5978
+ GCC_except_table6064
+ GCC_except_table6281
+ GCC_except_table6298
+ GCC_except_table6769
+ GCC_except_table7109
+ GCC_except_table7119
+ GCC_except_table7209
+ GCC_except_table7218
+ GCC_except_table7302
+ GCC_except_table7309
+ GCC_except_table7327
+ GCC_except_table7378
+ GCC_except_table7382
+ GCC_except_table7387
+ GCC_except_table7403
+ GCC_except_table785
+ GCC_except_table841
+ GCC_except_table931
+ GCC_except_table962
+ GCC_except_table965
+ GCC_except_table967
+ GCC_except_table974
+ GCC_except_table987
+ GCC_except_table991
+ GCC_except_table997
+ OBJC_IVAR_$_MPCAUHostingServiceKeepalive._keepaliveNode
+ OBJC_IVAR_$_MPCAUHostingServiceKeepalive._keepaliveQueue
+ OBJC_IVAR_$_MPCAUHostingServiceKeepalive._workQueue
+ OBJC_IVAR_$_MPCQueueController._lastChangeDirection
+ OBJC_IVAR_$__MPCMediaRemotePublisher._activeCommandCriticalSectionAssertions
+ OBJC_IVAR_$__MPCMediaRemotePublisher._errorReturningCommandID
+ OBJC_IVAR_$__MPCToggleTransitionsCommand._dialogCapable
+ OBJC_IVAR_$__MPCToggleTransitionsCommand._disabled
+ _ATAudioProcessingNodeDispose
+ _ATAudioProcessingNodeInstantiate
+ _AudioQueueNewOutput
+ _OBJC_CLASS_$_MPCAUHostingServiceKeepalive
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_METACLASS_$_MPCAUHostingServiceKeepalive
+ __237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke
+ __78-[MPCQueueController finalizeStateRestorationWithLoadingItemReady:completion:]_block_invoke
+ __88-[_MPCQueueControllerBehaviorMusic performInsertCommand:targetContentItemID:completion:]_block_invoke
+ __MPCAUHostingKeepaliveOutputCallback
+ __MPCEnsureNowPlayingContentItemCached
+ __OBJC_$_CLASS_METHODS_MPCAUHostingServiceKeepalive
+ __OBJC_$_INSTANCE_METHODS_MPCAUHostingServiceKeepalive
+ __OBJC_$_INSTANCE_VARIABLES_MPCAUHostingServiceKeepalive
+ __OBJC_$_INSTANCE_VARIABLES__MPCToggleTransitionsCommand
+ __OBJC_$_PROP_LIST_MPCToggleTransitionsCommand
+ __OBJC_CLASS_RO_$_MPCAUHostingServiceKeepalive
+ __OBJC_METACLASS_RO_$_MPCAUHostingServiceKeepalive
+ ___237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke
+ ___237-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:]_block_invoke_2
+ ___38-[MPCAUHostingServiceKeepalive _start]_block_invoke
+ ___45+[MPCAUHostingServiceKeepalive startIfNeeded]_block_invoke
+ ___51-[MPCAUHostingServiceKeepalive _mediaServerDidDie:]_block_invoke
+ ___55-[MPCAUHostingServiceKeepalive _mediaServerDidRestart:]_block_invoke
+ ____MPCEnsureNowPlayingContentItemCached_block_invoke
+ ___block_descriptor_117_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0ls32l8s40l8s48l8s56l8r96l8s88l8s64l8s72l8s80l8
+ ___block_descriptor_117_e8_32s40s48s56s64s72s80s88bs96r_e61_v32?0"MPRemoteCommandStatus"8"NSString"16"NSDictionary"24ls32l8s40l8s48l8r96l8s56l8s88l8s64l8s72l8s80l8
+ ___block_descriptor_56_e8_32s40s48s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8ls32l8s40l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8ls32l8s40l8r72l8s48l8s56l8s64l8r80l8
+ __swift_closure_destructor.106Tm
+ __swift_closure_destructor.112Tm
+ __swift_closure_destructor.11Tm
+ __swift_closure_destructor.124Tm
+ __swift_closure_destructor.137Tm
+ __swift_closure_destructor.58Tm
+ __swift_closure_destructor.72Tm
+ __swift_closure_destructor.96Tm
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
+ _objc_moveWeak
+ _objc_msgSend$_arm
+ _objc_msgSend$_clearErrorReturningCommandID:
+ _objc_msgSend$_invalidateAllCommandCriticalSectionAssertions
+ _objc_msgSend$_setErrorReturningCommandID:
+ _objc_msgSend$_setTargetContentItemID:source:direction:
+ _objc_msgSend$_start
+ _objc_msgSend$_teardown
+ _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:preferResolvableStoreIdentifiers:
+ _objc_msgSend$isPerformingErrorReturningCommand
+ _objc_msgSend$setDialogCapable:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$sharedPrivacyInfoForUserIdentity:
+ _objc_msgSend$shouldBlockPersonalizedNetworkRequestsForMusic
+ _objc_msgSend$startIfNeeded
+ _objc_msgSend$stringFromItems:
+ _symbolic _____ 18PodcastsFoundation16AlignmentStorageC0C8SnapshotV
+ _symbolic _____ SC34MPCPlaybackEngineInternalErrorCodeLeV
+ _symbolic _____ So34MPCPlaybackEngineInternalErrorCodeV
+ _symbolic yyYbcSg
+ _symbolic yycSg
+ startIfNeeded.onceToken
+ startIfNeeded.sharedKeepalive
- -[MPAVItem(MFQueuePlayerItem) setCurrentItemTransition:]
- -[MPCQueueController _setTargetContentItemID:source:]
- -[MPCQueueController jumpToContentItemID:]
- -[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]
- GCC_except_table1179
- GCC_except_table1183
- GCC_except_table1185
- GCC_except_table1353
- GCC_except_table1355
- GCC_except_table1396
- GCC_except_table1407
- GCC_except_table1414
- GCC_except_table1421
- GCC_except_table1458
- GCC_except_table1470
- GCC_except_table1479
- GCC_except_table1522
- GCC_except_table1695
- GCC_except_table1697
- GCC_except_table1715
- GCC_except_table1785
- GCC_except_table1869
- GCC_except_table1870
- GCC_except_table1978
- GCC_except_table1998
- GCC_except_table2000
- GCC_except_table2028
- GCC_except_table2037
- GCC_except_table2042
- GCC_except_table2044
- GCC_except_table2047
- GCC_except_table2058
- GCC_except_table2068
- GCC_except_table2183
- GCC_except_table2234
- GCC_except_table2238
- GCC_except_table2241
- GCC_except_table2267
- GCC_except_table2291
- GCC_except_table2323
- GCC_except_table2564
- GCC_except_table2592
- GCC_except_table2619
- GCC_except_table2762
- GCC_except_table2783
- GCC_except_table2790
- GCC_except_table2791
- GCC_except_table2816
- GCC_except_table2818
- GCC_except_table2823
- GCC_except_table2827
- GCC_except_table2829
- GCC_except_table2836
- GCC_except_table2862
- GCC_except_table2869
- GCC_except_table2874
- GCC_except_table2876
- GCC_except_table2880
- GCC_except_table2885
- GCC_except_table2886
- GCC_except_table2894
- GCC_except_table2897
- GCC_except_table2917
- GCC_except_table2967
- GCC_except_table3053
- GCC_except_table3057
- GCC_except_table3069
- GCC_except_table3093
- GCC_except_table3101
- GCC_except_table3142
- GCC_except_table3143
- GCC_except_table3150
- GCC_except_table3207
- GCC_except_table3225
- GCC_except_table3232
- GCC_except_table3274
- GCC_except_table3276
- GCC_except_table3283
- GCC_except_table3294
- GCC_except_table3336
- GCC_except_table3381
- GCC_except_table3386
- GCC_except_table343
- GCC_except_table345
- GCC_except_table3503
- GCC_except_table3524
- GCC_except_table3531
- GCC_except_table3556
- GCC_except_table3560
- GCC_except_table3570
- GCC_except_table3627
- GCC_except_table3632
- GCC_except_table3636
- GCC_except_table3705
- GCC_except_table3802
- GCC_except_table3806
- GCC_except_table3833
- GCC_except_table3839
- GCC_except_table3849
- GCC_except_table391
- GCC_except_table3978
- GCC_except_table399
- GCC_except_table4023
- GCC_except_table4024
- GCC_except_table4025
- GCC_except_table4045
- GCC_except_table4056
- GCC_except_table407
- GCC_except_table4074
- GCC_except_table4079
- GCC_except_table4081
- GCC_except_table4118
- GCC_except_table4129
- GCC_except_table416
- GCC_except_table4218
- GCC_except_table4237
- GCC_except_table4250
- GCC_except_table4261
- GCC_except_table4292
- GCC_except_table4463
- GCC_except_table4464
- GCC_except_table4643
- GCC_except_table4677
- GCC_except_table4679
- GCC_except_table4687
- GCC_except_table4695
- GCC_except_table4710
- GCC_except_table4718
- GCC_except_table4726
- GCC_except_table4736
- GCC_except_table4793
- GCC_except_table4808
- GCC_except_table4824
- GCC_except_table4827
- GCC_except_table4833
- GCC_except_table4880
- GCC_except_table4915
- GCC_except_table499
- GCC_except_table4996
- GCC_except_table515
- GCC_except_table5318
- GCC_except_table5319
- GCC_except_table532
- GCC_except_table5390
- GCC_except_table5485
- GCC_except_table5635
- GCC_except_table5660
- GCC_except_table5829
- GCC_except_table5894
- GCC_except_table5919
- GCC_except_table5954
- GCC_except_table5957
- GCC_except_table5960
- GCC_except_table6046
- GCC_except_table6263
- GCC_except_table6280
- GCC_except_table6747
- GCC_except_table7087
- GCC_except_table7097
- GCC_except_table7187
- GCC_except_table7196
- GCC_except_table7278
- GCC_except_table7285
- GCC_except_table7303
- GCC_except_table7354
- GCC_except_table7355
- GCC_except_table7358
- GCC_except_table7363
- GCC_except_table784
- GCC_except_table840
- GCC_except_table916
- GCC_except_table947
- GCC_except_table950
- GCC_except_table952
- GCC_except_table957
- GCC_except_table959
- GCC_except_table976
- GCC_except_table982
- GCC_except_table986
- GCC_except_table989
- GCC_except_table992
- __204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke_2
- ___42-[MPCQueueController jumpToContentItemID:]_block_invoke
- ___81-[_MPCMusicPlayerControllerServer _ensureCacheFilledForContentItemID:completion:]_block_invoke
- ___88-[_MPCQueueControllerBehaviorMusic performInsertCommand:targetContentItemID:completion:]_block_invoke_2
- ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
- ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e61_v32?0"MPRemoteCommandStatus"8"NSString"16"NSDictionary"24ls32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
- ___block_descriptor_64_e8_32s40s48s56s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8ls32l8s40l8r72l8s48l8s56l8s64l8r80l8
- __swift_closure_destructor.105Tm
- __swift_closure_destructor.10Tm
- __swift_closure_destructor.130Tm
- __swift_closure_destructor.86Tm
- __swift_closure_destructor.95Tm
- _associated conformance 17MediaPlaybackCore14ItemTransitionOSHAASQ
- _objc_msgSend$_setTargetContentItemID:source:
- _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:
- _objc_msgSend$currentItemTransition
- _objc_msgSend$setAppBundleID:
- _objc_msgSend$setCurrentItemTransition:
- _symbolic _____ 17MediaPlaybackCore14ItemTransitionO
CStrings:
+ "%{private,mask.hash}s ┃┃   │ reason: transition"
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
+ "Unexpected event type"
+ "[ALC:%{public}s] - Effective start %{public}f within cold-start margin %{public}f of overlap start %{public}f, cancelling transition"
+ "[AUKeepalive] AUHostingService keepalive established (idle AudioQueue + bypassed 'dspg' node)"
+ "[AUKeepalive] Failed to create idle AudioQueue (status=%d) — AUHostingService will not be kept warm"
+ "[AUKeepalive] Failed to instantiate ATAudioProcessingNode (status=%d) — AUHostingService will not be kept warm"
+ "[AUKeepalive] MediaServicesWereLost — releasing keepalive (will re-arm on reset)"
+ "[AUKeepalive] MediaServicesWereReset — re-arming keepalive"
+ "[AccountManager] Unexpected combo account, recovering with first/last tokens: %{public}@"
+ "[AccountManager] combining an already-combo borrowing account ID: %@"
+ "[AccountManager] combining an already-combo primary account ID: %@"
+ "[AssetReaderImplementation]: restoreAlignmentSession=%{bool,public}d (sessionActive=%{bool,public}d, HLS=%{bool,public}d)"
+ "[BMUS:%{public}@:%{public}@] performInsertCommand: | failed [insertion position %ld requires a non-empty afterContentItemID]"
+ "[PL:%{public}s] AUDIO SESSION CONTROLLER: Invalidating - Alarm category"
+ "[PL:%{public}s] STACK PROCESSING: Skipping snapshot restore of non-positive start time %{public}f for: %{public}s [%{public}s]"
+ "[PL:%{public}s] TRANSITION: Effective start %{public}f within cold-start margin %{public}f of overlap start %{public}f, cancelling crossfade [%{public}s]"
+ "[PL:%{public}s] TRANSITION: Jump during an ongoing crossfade, cancelling [%{public}s]"
+ "[PSYNC:%{public}@:%{public}@] setTargetContentItemID:%{public}@ source:%{public}@ direction:%{public}@ | updating target"
+ "[PUB:%{public}@] _invalidateAllCommandCriticalSectionAssertions | force-invalidating stranded critical section assertion [publisher torn down before _performCommandEvent completion] commandID=%{public}@"
+ "[PUB:%{public}@] commandCenter:didTimeoutCommandEvent:%{public}@ | force-invalidating stranded critical section assertion [command timed out before _performCommandEvent completion]"
+ "[TranscriptAlignmentProvider] Deferred scouting until first live alignment"
+ "[TranscriptAlignmentProvider] First-alignment fallback fired; configuring scouting"
+ "com.apple.MediaPlaybackCore.AUHostingServiceKeepalive"
+ "com.apple.WorkflowKit.BackgroundShortcutRunner"
+ "\xe1"
+ "⏹️ [SampleBufferOutput] processLoop exited after %ld buffers"
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
- "\xc1"
```
