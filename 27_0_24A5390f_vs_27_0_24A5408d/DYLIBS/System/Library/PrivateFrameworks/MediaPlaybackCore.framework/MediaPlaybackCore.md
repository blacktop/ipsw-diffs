## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-26100.26.28.501.0
-  __TEXT.__text: 0x4989f8
-  __TEXT.__objc_methlist: 0x17dd0
+26115.26.31.201.0
+  __TEXT.__text: 0x4a04dc
+  __TEXT.__objc_methlist: 0x17e90
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x10638
-  __TEXT.__oslogstring: 0x4bfeb
-  __TEXT.__cstring: 0x2563e
-  __TEXT.__swift5_typeref: 0x5410
-  __TEXT.__swift5_capture: 0xab04
-  __TEXT.__constg_swiftt: 0x7aa4
-  __TEXT.__swift5_reflstr: 0x5902
-  __TEXT.__swift5_fieldmd: 0x5638
+  __TEXT.__const: 0x10880
+  __TEXT.__oslogstring: 0x4c5a7
+  __TEXT.__cstring: 0x25a10
+  __TEXT.__swift5_typeref: 0x5474
+  __TEXT.__swift5_capture: 0xaf24
+  __TEXT.__constg_swiftt: 0x7ae8
+  __TEXT.__swift5_reflstr: 0x5972
+  __TEXT.__swift5_fieldmd: 0x5678
   __TEXT.__swift5_builtin: 0x6f4
   __TEXT.__swift5_mpenum: 0xf0
-  __TEXT.__swift5_assocty: 0xb90
-  __TEXT.__swift5_proto: 0x918
-  __TEXT.__swift5_types: 0x560
-  __TEXT.__swift_as_entry: 0x494
-  __TEXT.__swift_as_ret: 0x5b0
-  __TEXT.__swift_as_cont: 0xdec
+  __TEXT.__swift5_assocty: 0xbc0
+  __TEXT.__swift5_proto: 0x92c
+  __TEXT.__swift5_types: 0x564
+  __TEXT.__swift_as_entry: 0x4a4
+  __TEXT.__swift_as_ret: 0x5b4
+  __TEXT.__swift_as_cont: 0xe00
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x580c
+  __TEXT.__gcc_except_tab: 0x58e4
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0xdc38
-  __TEXT.__eh_frame: 0xfeb4
+  __TEXT.__unwind_info: 0xdd28
+  __TEXT.__eh_frame: 0x10154
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9378
-  __DATA_CONST.__objc_classlist: 0xd30
+  __DATA_CONST.__const: 0x9380
+  __DATA_CONST.__objc_classlist: 0xd38
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb00
+  __DATA_CONST.__objc_selrefs: 0xcb68
   __DATA_CONST.__objc_protorefs: 0x3a0
-  __DATA_CONST.__objc_superrefs: 0x6d0
+  __DATA_CONST.__objc_superrefs: 0x6d8
   __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0x3430
-  __AUTH_CONST.__const: 0x22ed0
-  __AUTH_CONST.__cfstring: 0x1e8e0
-  __AUTH_CONST.__objc_const: 0x345b8
-  __AUTH_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__got: 0x3440
+  __AUTH_CONST.__const: 0x238f0
+  __AUTH_CONST.__cfstring: 0x1e9e0
+  __AUTH_CONST.__objc_const: 0x34808
+  __AUTH_CONST.__objc_intobj: 0x888
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x3430
-  __AUTH.__objc_data: 0x5a28
-  __AUTH.__data: 0x4030
-  __DATA.__objc_ivar: 0x1ab0
-  __DATA.__data: 0x7240
-  __DATA.__bss: 0xf1b8
+  __AUTH_CONST.__auth_got: 0x3458
+  __AUTH.__objc_data: 0x5a88
+  __AUTH.__data: 0x4070
+  __DATA.__objc_ivar: 0x1ad0
+  __DATA.__data: 0x72e0
+  __DATA.__bss: 0xf448
   __DATA.__common: 0x230
-  __DATA_DIRTY.__objc_data: 0x3578
+  __DATA_DIRTY.__objc_data: 0x3570
   __DATA_DIRTY.__data: 0x4538
   __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0xc8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24246
-  Symbols:   24189
-  CStrings:  8215
+  Functions: 24424
+  Symbols:   24259
+  CStrings:  8248
 
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
+ GCC_except_table1004
+ GCC_except_table1008
+ GCC_except_table1011
+ GCC_except_table1014
+ GCC_except_table1201
+ GCC_except_table1205
+ GCC_except_table1207
+ GCC_except_table1375
+ GCC_except_table1377
+ GCC_except_table1424
+ GCC_except_table1435
+ GCC_except_table1442
+ GCC_except_table1449
+ GCC_except_table1486
+ GCC_except_table1498
+ GCC_except_table1507
+ GCC_except_table1550
+ GCC_except_table1725
+ GCC_except_table1738
+ GCC_except_table1743
+ GCC_except_table1813
+ GCC_except_table1899
+ GCC_except_table1900
+ GCC_except_table2011
+ GCC_except_table2031
+ GCC_except_table2033
+ GCC_except_table2061
+ GCC_except_table2070
+ GCC_except_table2075
+ GCC_except_table2077
+ GCC_except_table2080
+ GCC_except_table2091
+ GCC_except_table2101
+ GCC_except_table2216
+ GCC_except_table2267
+ GCC_except_table2271
+ GCC_except_table2274
+ GCC_except_table2300
+ GCC_except_table2324
+ GCC_except_table2356
+ GCC_except_table2436
+ GCC_except_table2623
+ GCC_except_table2651
+ GCC_except_table2678
+ GCC_except_table2821
+ GCC_except_table2842
+ GCC_except_table2849
+ GCC_except_table2850
+ GCC_except_table2882
+ GCC_except_table2886
+ GCC_except_table2888
+ GCC_except_table2890
+ GCC_except_table2892
+ GCC_except_table2895
+ GCC_except_table2921
+ GCC_except_table2928
+ GCC_except_table2933
+ GCC_except_table2939
+ GCC_except_table2944
+ GCC_except_table2945
+ GCC_except_table2950
+ GCC_except_table2953
+ GCC_except_table2956
+ GCC_except_table2976
+ GCC_except_table2984
+ GCC_except_table3027
+ GCC_except_table3117
+ GCC_except_table3128
+ GCC_except_table3129
+ GCC_except_table3153
+ GCC_except_table3161
+ GCC_except_table3202
+ GCC_except_table3203
+ GCC_except_table3219
+ GCC_except_table3276
+ GCC_except_table3294
+ GCC_except_table3301
+ GCC_except_table3343
+ GCC_except_table3345
+ GCC_except_table3363
+ GCC_except_table3367
+ GCC_except_table3405
+ GCC_except_table3450
+ GCC_except_table3455
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table3583
+ GCC_except_table3604
+ GCC_except_table3611
+ GCC_except_table3636
+ GCC_except_table3640
+ GCC_except_table3650
+ GCC_except_table3707
+ GCC_except_table3712
+ GCC_except_table3716
+ GCC_except_table3786
+ GCC_except_table3887
+ GCC_except_table3898
+ GCC_except_table3920
+ GCC_except_table3929
+ GCC_except_table399
+ GCC_except_table4057
+ GCC_except_table407
+ GCC_except_table4101
+ GCC_except_table4102
+ GCC_except_table4103
+ GCC_except_table4123
+ GCC_except_table4132
+ GCC_except_table415
+ GCC_except_table4150
+ GCC_except_table4155
+ GCC_except_table4171
+ GCC_except_table4194
+ GCC_except_table4205
+ GCC_except_table424
+ GCC_except_table4294
+ GCC_except_table4313
+ GCC_except_table4326
+ GCC_except_table4337
+ GCC_except_table4368
+ GCC_except_table4539
+ GCC_except_table4540
+ GCC_except_table4718
+ GCC_except_table4753
+ GCC_except_table4755
+ GCC_except_table4763
+ GCC_except_table4771
+ GCC_except_table4786
+ GCC_except_table4794
+ GCC_except_table4802
+ GCC_except_table4812
+ GCC_except_table4827
+ GCC_except_table4871
+ GCC_except_table4886
+ GCC_except_table4902
+ GCC_except_table4905
+ GCC_except_table4911
+ GCC_except_table4963
+ GCC_except_table4999
+ GCC_except_table507
+ GCC_except_table5086
+ GCC_except_table5187
+ GCC_except_table524
+ GCC_except_table541
+ GCC_except_table5425
+ GCC_except_table5426
+ GCC_except_table5501
+ GCC_except_table5592
+ GCC_except_table5744
+ GCC_except_table5769
+ GCC_except_table5886
+ GCC_except_table5967
+ GCC_except_table5975
+ GCC_except_table5976
+ GCC_except_table6040
+ GCC_except_table6065
+ GCC_except_table6100
+ GCC_except_table6103
+ GCC_except_table6106
+ GCC_except_table6192
+ GCC_except_table6409
+ GCC_except_table6426
+ GCC_except_table6474
+ GCC_except_table6487
+ GCC_except_table7003
+ GCC_except_table7337
+ GCC_except_table7347
+ GCC_except_table7440
+ GCC_except_table7449
+ GCC_except_table7533
+ GCC_except_table7540
+ GCC_except_table7558
+ GCC_except_table7609
+ GCC_except_table7610
+ GCC_except_table7613
+ GCC_except_table7618
+ GCC_except_table7634
+ GCC_except_table792
+ GCC_except_table848
+ GCC_except_table938
+ GCC_except_table969
+ GCC_except_table972
+ GCC_except_table974
+ GCC_except_table981
+ GCC_except_table994
+ GCC_except_table998
+ _ATAudioProcessingNodeDispose
+ _ATAudioProcessingNodeInstantiate
+ _AudioQueueNewOutput
+ _OBJC_CLASS_$_MPCAUHostingServiceKeepalive
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_IVAR_$_MPCAUHostingServiceKeepalive._keepaliveNode
+ _OBJC_IVAR_$_MPCAUHostingServiceKeepalive._keepaliveQueue
+ _OBJC_IVAR_$_MPCAUHostingServiceKeepalive._workQueue
+ _OBJC_IVAR_$_MPCQueueController._lastChangeDirection
+ _OBJC_IVAR_$__MPCMediaRemotePublisher._activeCommandCriticalSectionAssertions
+ _OBJC_IVAR_$__MPCMediaRemotePublisher._errorReturningCommandID
+ _OBJC_IVAR_$__MPCToggleTransitionsCommand._dialogCapable
+ _OBJC_IVAR_$__MPCToggleTransitionsCommand._disabled
+ _OBJC_METACLASS_$_MPCAUHostingServiceKeepalive
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
+ ___block_descriptor_56_e8_32s40s48s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8ls32l8s40l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8ls32l8s40l8r72l8s48l8s56l8s64l8r80l8
+ ___swift_closure_destructor.112Tm
+ ___swift_closure_destructor.11Tm
+ ___swift_closure_destructor.124Tm
+ ___swift_closure_destructor.72Tm
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
+ _startIfNeeded.onceToken
+ _startIfNeeded.sharedKeepalive
+ _symbolic _____ 18PodcastsFoundation16AlignmentStorageC0C8SnapshotV
+ _symbolic _____ SC34MPCPlaybackEngineInternalErrorCodeLeV
+ _symbolic _____ So34MPCPlaybackEngineInternalErrorCodeV
+ _symbolic yyYbcSg
- -[MPAVItem(MFQueuePlayerItem) setCurrentItemTransition:]
- -[MPCQueueController _setTargetContentItemID:source:]
- -[MPCQueueController jumpToContentItemID:]
- -[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]
- GCC_except_table1186
- GCC_except_table1190
- GCC_except_table1192
- GCC_except_table1360
- GCC_except_table1362
- GCC_except_table1409
- GCC_except_table1420
- GCC_except_table1427
- GCC_except_table1434
- GCC_except_table1471
- GCC_except_table1483
- GCC_except_table1492
- GCC_except_table1535
- GCC_except_table1708
- GCC_except_table1710
- GCC_except_table1728
- GCC_except_table1798
- GCC_except_table1884
- GCC_except_table1885
- GCC_except_table1996
- GCC_except_table2016
- GCC_except_table2018
- GCC_except_table2046
- GCC_except_table2055
- GCC_except_table2060
- GCC_except_table2062
- GCC_except_table2065
- GCC_except_table2076
- GCC_except_table2086
- GCC_except_table2201
- GCC_except_table2252
- GCC_except_table2256
- GCC_except_table2259
- GCC_except_table2285
- GCC_except_table2309
- GCC_except_table2341
- GCC_except_table2421
- GCC_except_table2608
- GCC_except_table2636
- GCC_except_table2663
- GCC_except_table2806
- GCC_except_table2827
- GCC_except_table2834
- GCC_except_table2835
- GCC_except_table2860
- GCC_except_table2862
- GCC_except_table2867
- GCC_except_table2871
- GCC_except_table2873
- GCC_except_table2880
- GCC_except_table2906
- GCC_except_table2913
- GCC_except_table2918
- GCC_except_table2920
- GCC_except_table2924
- GCC_except_table2929
- GCC_except_table2930
- GCC_except_table2938
- GCC_except_table2941
- GCC_except_table2961
- GCC_except_table2969
- GCC_except_table3012
- GCC_except_table3098
- GCC_except_table3102
- GCC_except_table3114
- GCC_except_table3138
- GCC_except_table3146
- GCC_except_table3187
- GCC_except_table3188
- GCC_except_table3204
- GCC_except_table3261
- GCC_except_table3279
- GCC_except_table3286
- GCC_except_table3328
- GCC_except_table3330
- GCC_except_table3337
- GCC_except_table3348
- GCC_except_table3390
- GCC_except_table3435
- GCC_except_table3440
- GCC_except_table350
- GCC_except_table352
- GCC_except_table3568
- GCC_except_table3589
- GCC_except_table3596
- GCC_except_table3621
- GCC_except_table3625
- GCC_except_table3635
- GCC_except_table3692
- GCC_except_table3697
- GCC_except_table3701
- GCC_except_table3771
- GCC_except_table3868
- GCC_except_table3872
- GCC_except_table3899
- GCC_except_table3905
- GCC_except_table398
- GCC_except_table4043
- GCC_except_table406
- GCC_except_table4087
- GCC_except_table4088
- GCC_except_table4089
- GCC_except_table4109
- GCC_except_table4118
- GCC_except_table4136
- GCC_except_table414
- GCC_except_table4141
- GCC_except_table4143
- GCC_except_table4180
- GCC_except_table4191
- GCC_except_table423
- GCC_except_table4280
- GCC_except_table4299
- GCC_except_table4312
- GCC_except_table4323
- GCC_except_table4354
- GCC_except_table4525
- GCC_except_table4526
- GCC_except_table4706
- GCC_except_table4740
- GCC_except_table4742
- GCC_except_table4750
- GCC_except_table4758
- GCC_except_table4773
- GCC_except_table4781
- GCC_except_table4789
- GCC_except_table4799
- GCC_except_table4814
- GCC_except_table4858
- GCC_except_table4873
- GCC_except_table4889
- GCC_except_table4892
- GCC_except_table4898
- GCC_except_table4950
- GCC_except_table4986
- GCC_except_table506
- GCC_except_table5069
- GCC_except_table5170
- GCC_except_table522
- GCC_except_table539
- GCC_except_table5409
- GCC_except_table5410
- GCC_except_table5485
- GCC_except_table5576
- GCC_except_table5728
- GCC_except_table5753
- GCC_except_table5870
- GCC_except_table5951
- GCC_except_table5959
- GCC_except_table5960
- GCC_except_table6024
- GCC_except_table6049
- GCC_except_table6084
- GCC_except_table6087
- GCC_except_table6090
- GCC_except_table6176
- GCC_except_table6393
- GCC_except_table6410
- GCC_except_table6458
- GCC_except_table6471
- GCC_except_table6983
- GCC_except_table7317
- GCC_except_table7327
- GCC_except_table7420
- GCC_except_table7429
- GCC_except_table7511
- GCC_except_table7518
- GCC_except_table7536
- GCC_except_table7587
- GCC_except_table7588
- GCC_except_table7591
- GCC_except_table7596
- GCC_except_table7612
- GCC_except_table791
- GCC_except_table847
- GCC_except_table923
- GCC_except_table954
- GCC_except_table957
- GCC_except_table959
- GCC_except_table964
- GCC_except_table966
- GCC_except_table983
- GCC_except_table989
- GCC_except_table993
- GCC_except_table996
- GCC_except_table999
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
- ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke_2
- ___42-[MPCQueueController jumpToContentItemID:]_block_invoke
- ___81-[_MPCMusicPlayerControllerServer _ensureCacheFilledForContentItemID:completion:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e53_v16?0?<v?"MPCAssistantRemoteControlDestination">8ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e31_v16?0"MPRemoteCommandStatus"8ls32l8s40l8r72l8s48l8s56l8s64l8r80l8
- ___swift_closure_destructor.10Tm
- ___swift_closure_destructor.86Tm
- _associated conformance 17MediaPlaybackCore14ItemTransitionOSHAASQ
- _objc_msgSend$_setTargetContentItemID:source:
- _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:
- _objc_msgSend$currentItemTransition
- _objc_msgSend$setAppBundleID:
- _objc_msgSend$setCurrentItemTransition:
- _symbolic _____ 17MediaPlaybackCore14ItemTransitionO
CStrings:
+ "%{private,mask.hash}s ┃┃   │ reason: transition"
+ "Audio session is in invalid activation state "
+ "Audio session is not activated"
+ "InvalidAudioSessionActivation"
+ "MPCTransitionStyle"
+ "MPCTransitionsSettingsErrorCodes"
+ "MediaPlaybackCore.ensureNowPlayingContentItemCached"
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
+ "[AUKeepalive] AUHostingService keepalive established (idle AudioQueue + bypassed 'dspg' node)"
+ "[AUKeepalive] Failed to create idle AudioQueue (status=%d) — AUHostingService will not be kept warm"
+ "[AUKeepalive] Failed to instantiate ATAudioProcessingNode (status=%d) — AUHostingService will not be kept warm"
+ "[AUKeepalive] MediaServicesWereLost — releasing keepalive (will re-arm on reset)"
+ "[AUKeepalive] MediaServicesWereReset — re-arming keepalive"
+ "[PL:%{public}s] AUDIO SESSION CONTROLLER: Invalidating - Alarm category"
+ "[PL:%{public}s] PLAYER CONTROLLER: Failing user event due to an audio session activation error: %@"
+ "[PL:%{public}s] STACK PROCESSING: Skipping snapshot restore of non-positive start time %{public}f for: %{public}s [%{public}s]"
+ "[PSYNC:%{public}@:%{public}@] setTargetContentItemID:%{public}@ source:%{public}@ direction:%{public}@ | updating target"
+ "[PUB:%{public}@] _invalidateAllCommandCriticalSectionAssertions | force-invalidating stranded critical section assertion [publisher torn down before _performCommandEvent completion] commandID=%{public}@"
+ "[PUB:%{public}@] commandCenter:didTimeoutCommandEvent:%{public}@ | force-invalidating stranded critical section assertion [command timed out before _performCommandEvent completion]"
+ "[TranscriptAlignmentProvider] Deferred scouting until first live alignment"
+ "[TranscriptAlignmentProvider] First-alignment fallback fired; configuring scouting"
+ "com.apple.MediaPlaybackCore.AUHostingServiceKeepalive"
+ "\xe1"
+ "⚠️ [SampleBufferOutput] processLoop finished from nil sequence"
- "MPCMusicPlayerControllerServer.ensureCacheFilled"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | failing skip [%{public}@]"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | updating target"
- "[PSYNC:%{public}@:%{public}@] jumpToContentItemID:%{public}@ | validating item [] behavior=%{public}@"
- "[PSYNC:%{public}@:%{public}@] setTargetContentItemID:%{public}@ source:%{public}@ | updating target"
- "com.apple.NanoBooks"
- "com.apple.iBooks"
- "\xc1"
```
