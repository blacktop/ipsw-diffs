## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-25100.25.30.502.0
-  __TEXT.__text: 0x3e5a8c
-  __TEXT.__auth_stubs: 0x58e0
-  __TEXT.__objc_methlist: 0x17000
+25110.25.31.601.0
+  __TEXT.__text: 0x3e72ec
+  __TEXT.__auth_stubs: 0x5970
+  __TEXT.__objc_methlist: 0x17008
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x15aa0
-  __TEXT.__cstring: 0x2f639
-  __TEXT.__constg_swiftt: 0x7538
+  __TEXT.__const: 0x15ab0
+  __TEXT.__cstring: 0x2f6c2
+  __TEXT.__constg_swiftt: 0x7550
   __TEXT.__swift5_typeref: 0x5012
-  __TEXT.__swift5_reflstr: 0x4f22
-  __TEXT.__swift5_fieldmd: 0x4c1c
+  __TEXT.__swift5_reflstr: 0x4f32
+  __TEXT.__swift5_fieldmd: 0x4c28
   __TEXT.__swift5_builtin: 0x758
   __TEXT.__swift5_assocty: 0xf38
   __TEXT.__swift5_capture: 0x3364
-  __TEXT.__oslogstring: 0x3bdb9
+  __TEXT.__oslogstring: 0x3bee0
   __TEXT.__swift5_mpenum: 0x104
   __TEXT.__swift5_proto: 0x9c8
   __TEXT.__swift5_types: 0x538

   __TEXT.__swift_as_ret: 0x4bc
   __TEXT.__swift5_protos: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x6988
+  __TEXT.__gcc_except_tab: 0x67f0
   __TEXT.__ustring: 0x4b4
-  __TEXT.__unwind_info: 0xc0c0
-  __TEXT.__eh_frame: 0xc9e0
+  __TEXT.__unwind_info: 0xc0e8
+  __TEXT.__eh_frame: 0xca50
   __TEXT.__objc_classname: 0x3d25
-  __TEXT.__objc_methname: 0x38aed
-  __TEXT.__objc_methtype: 0x9978
+  __TEXT.__objc_methname: 0x38aa4
+  __TEXT.__objc_methtype: 0x99b9
   __TEXT.__objc_stubs: 0x26720
-  __DATA_CONST.__got: 0x2e88
+  __DATA_CONST.__got: 0x2ea0
   __DATA_CONST.__const: 0x90f0
   __DATA_CONST.__objc_classlist: 0xcc8
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc230
+  __DATA_CONST.__objc_selrefs: 0xc220
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x2c80
+  __AUTH_CONST.__auth_got: 0x2cc8
   __AUTH_CONST.__const: 0xfaa0
-  __AUTH_CONST.__cfstring: 0x1d3c0
+  __AUTH_CONST.__cfstring: 0x1d380
   __AUTH_CONST.__objc_const: 0x32820
-  __AUTH_CONST.__objc_intobj: 0x7e0
+  __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x4d10
-  __AUTH.__data: 0x3250
+  __AUTH.__data: 0x3270
   __DATA.__objc_ivar: 0x19c8
-  __DATA.__data: 0x7158
+  __DATA.__data: 0x7178
   __DATA.__bss: 0x101d0
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x3930
-  __DATA_DIRTY.__data: 0x4720
+  __DATA_DIRTY.__data: 0x4700
   __DATA_DIRTY.__bss: 0x13b0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C12597AB-2248-3C45-AAD9-A767EE4E49EC
-  Functions: 19683
-  Symbols:   38272
-  CStrings:  22462
+  UUID: 30208BE6-BC64-3D92-8012-733E5C625785
+  Functions: 19692
+  Symbols:   38271
+  CStrings:  22463
 
Symbols:
+ -[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]
+ -[MPCMediaFoundationTranslator cachedQueueItemForContentItemID:]
+ -[MPCPlayActivityFeedEventConsumer _queueSectionIsAODFromSectionIdentifier:cursor:]
+ -[MPCPlaybackAccountManager musicPlaybackRequestEnvironmentForAccount:]
+ -[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartFrom:to:transitionProvided:]
+ -[_MPCPlaybackEnginePlayer smartTransitionWillBeginFrom:to:transitionTime:outgoingItemAveragePrePivotTransitionRate:timeStamp:parameters:]
+ GCC_except_table105
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
+ GCC_except_table183
+ GCC_except_table1909
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1959
+ GCC_except_table1968
+ GCC_except_table1973
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
+ GCC_except_table2746
+ GCC_except_table2765
+ GCC_except_table2772
+ GCC_except_table2773
+ GCC_except_table2797
+ GCC_except_table2799
+ GCC_except_table2807
+ GCC_except_table2811
+ GCC_except_table2816
+ GCC_except_table2841
+ GCC_except_table2848
+ GCC_except_table2853
+ GCC_except_table2855
+ GCC_except_table2858
+ GCC_except_table2863
+ GCC_except_table2872
+ GCC_except_table2895
+ GCC_except_table2903
+ GCC_except_table2945
+ GCC_except_table3023
+ GCC_except_table3034
+ GCC_except_table3035
+ GCC_except_table3059
+ GCC_except_table3067
+ GCC_except_table3108
+ GCC_except_table3109
+ GCC_except_table311
+ GCC_except_table3125
+ GCC_except_table3183
+ GCC_except_table3198
+ GCC_except_table3203
+ GCC_except_table323
+ GCC_except_table3240
+ GCC_except_table3242
+ GCC_except_table3249
+ GCC_except_table3260
+ GCC_except_table3265
+ GCC_except_table3301
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table3346
+ GCC_except_table3468
+ GCC_except_table3489
+ GCC_except_table3491
+ GCC_except_table3492
+ GCC_except_table3520
+ GCC_except_table3524
+ GCC_except_table3534
+ GCC_except_table3709
+ GCC_except_table3713
+ GCC_except_table3724
+ GCC_except_table3736
+ GCC_except_table3738
+ GCC_except_table3753
+ GCC_except_table381
+ GCC_except_table3877
+ GCC_except_table389
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table3941
+ GCC_except_table3949
+ GCC_except_table3967
+ GCC_except_table397
+ GCC_except_table3974
+ GCC_except_table3988
+ GCC_except_table4011
+ GCC_except_table4022
+ GCC_except_table406
+ GCC_except_table4108
+ GCC_except_table4117
+ GCC_except_table4126
+ GCC_except_table4149
+ GCC_except_table4165
+ GCC_except_table4270
+ GCC_except_table4391
+ GCC_except_table4392
+ GCC_except_table454
+ GCC_except_table4576
+ GCC_except_table4610
+ GCC_except_table4612
+ GCC_except_table4620
+ GCC_except_table4628
+ GCC_except_table4643
+ GCC_except_table4651
+ GCC_except_table4659
+ GCC_except_table4668
+ GCC_except_table4683
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table4728
+ GCC_except_table4752
+ GCC_except_table4754
+ GCC_except_table4762
+ GCC_except_table4815
+ GCC_except_table4840
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table4953
+ GCC_except_table5053
+ GCC_except_table5293
+ GCC_except_table5294
+ GCC_except_table5366
+ GCC_except_table5453
+ GCC_except_table5602
+ GCC_except_table5627
+ GCC_except_table5740
+ GCC_except_table5822
+ GCC_except_table5830
+ GCC_except_table5831
+ GCC_except_table5895
+ GCC_except_table5920
+ GCC_except_table5955
+ GCC_except_table5958
+ GCC_except_table5961
+ GCC_except_table6047
+ GCC_except_table6262
+ GCC_except_table6279
+ GCC_except_table6327
+ GCC_except_table6340
+ GCC_except_table6843
+ GCC_except_table7184
+ GCC_except_table7276
+ GCC_except_table7285
+ GCC_except_table7365
+ GCC_except_table7372
+ GCC_except_table739
+ GCC_except_table7390
+ GCC_except_table7439
+ GCC_except_table7440
+ GCC_except_table7443
+ GCC_except_table7464
+ GCC_except_table795
+ GCC_except_table871
+ GCC_except_table903
+ GCC_except_table906
+ GCC_except_table908
+ GCC_except_table913
+ GCC_except_table915
+ GCC_except_table928
+ GCC_except_table932
+ GCC_except_table938
+ GCC_except_table942
+ GCC_except_table945
+ GCC_except_table948
+ _MSVFastHexStringFromBytes.hexCharacters.30091
+ __MPCAudioTapFinalize.1815
+ __MPCAudioTapInit.1816
+ __MPCAudioTapPrepareCallback.1814
+ __MPCAudioTapProcess.1809
+ __MPCAudioTapUnprepareCallback.1808
+ ___123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.689
+ ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.562
+ ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke_2.563
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.10
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.125
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.130
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.136
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.145
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.208
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.22
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.222
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.233
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.249
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.25
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.284
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.295
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.38
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.55
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.77
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.95
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.189
+ ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.223
+ ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.226
+ ___66-[_MPCQueueControllerBehaviorMusic performLoadCommand:completion:]_block_invoke.120
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.265
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.284
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.205
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.211
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.213
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.218
+ ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.220
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.186
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.190
+ ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke_2.191
+ ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.221
+ ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.222
+ ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.219
+ ___76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.711
+ ___80-[_MPCQueueControllerBehaviorMusic reshuffleWithTargetContentItemID:completion:]_block_invoke.358
+ ___90-[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartFrom:to:transitionProvided:]_block_invoke
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.105
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.110
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.149
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.29
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.37
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.50
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.60
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.67
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.74
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.79
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.82
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.84
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke.96
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.112
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.150
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.40
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.64
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.75
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.80
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.88
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_2.99
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_3
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_3.116
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_3.78
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_4
+ ___93-[MPCAssistantCommandInternal sendCommand:toDestination:commandID:commandBuilder:completion:]_block_invoke_5
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.222
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.275
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.281
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.285
+ ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.291
+ ___Block_byref_object_copy_.11262
+ ___Block_byref_object_copy_.11435
+ ___Block_byref_object_copy_.11735
+ ___Block_byref_object_copy_.1205
+ ___Block_byref_object_copy_.12440
+ ___Block_byref_object_copy_.13597
+ ___Block_byref_object_copy_.1539
+ ___Block_byref_object_copy_.15733
+ ___Block_byref_object_copy_.16327
+ ___Block_byref_object_copy_.16736
+ ___Block_byref_object_copy_.17334
+ ___Block_byref_object_copy_.17975
+ ___Block_byref_object_copy_.1817
+ ___Block_byref_object_copy_.18848
+ ___Block_byref_object_copy_.19390
+ ___Block_byref_object_copy_.19576
+ ___Block_byref_object_copy_.20026
+ ___Block_byref_object_copy_.21191
+ ___Block_byref_object_copy_.2131
+ ___Block_byref_object_copy_.22127
+ ___Block_byref_object_copy_.25084
+ ___Block_byref_object_copy_.25887
+ ___Block_byref_object_copy_.26306
+ ___Block_byref_object_copy_.27095
+ ___Block_byref_object_copy_.28498
+ ___Block_byref_object_copy_.29062
+ ___Block_byref_object_copy_.3202
+ ___Block_byref_object_copy_.33909
+ ___Block_byref_object_copy_.34381
+ ___Block_byref_object_copy_.34798
+ ___Block_byref_object_copy_.3961
+ ___Block_byref_object_copy_.4134
+ ___Block_byref_object_copy_.466
+ ___Block_byref_object_copy_.493
+ ___Block_byref_object_copy_.5081
+ ___Block_byref_object_copy_.664
+ ___Block_byref_object_copy_.6929
+ ___Block_byref_object_copy_.7744
+ ___Block_byref_object_copy_.9836
+ ___Block_byref_object_copy_.9903
+ ___Block_byref_object_dispose_.11263
+ ___Block_byref_object_dispose_.11436
+ ___Block_byref_object_dispose_.11736
+ ___Block_byref_object_dispose_.1206
+ ___Block_byref_object_dispose_.12441
+ ___Block_byref_object_dispose_.13598
+ ___Block_byref_object_dispose_.1540
+ ___Block_byref_object_dispose_.15734
+ ___Block_byref_object_dispose_.16328
+ ___Block_byref_object_dispose_.16737
+ ___Block_byref_object_dispose_.17335
+ ___Block_byref_object_dispose_.17976
+ ___Block_byref_object_dispose_.1818
+ ___Block_byref_object_dispose_.18849
+ ___Block_byref_object_dispose_.19391
+ ___Block_byref_object_dispose_.19577
+ ___Block_byref_object_dispose_.20027
+ ___Block_byref_object_dispose_.21192
+ ___Block_byref_object_dispose_.2132
+ ___Block_byref_object_dispose_.22128
+ ___Block_byref_object_dispose_.25085
+ ___Block_byref_object_dispose_.25888
+ ___Block_byref_object_dispose_.26307
+ ___Block_byref_object_dispose_.27096
+ ___Block_byref_object_dispose_.28499
+ ___Block_byref_object_dispose_.29063
+ ___Block_byref_object_dispose_.3203
+ ___Block_byref_object_dispose_.33910
+ ___Block_byref_object_dispose_.34382
+ ___Block_byref_object_dispose_.34799
+ ___Block_byref_object_dispose_.3962
+ ___Block_byref_object_dispose_.4135
+ ___Block_byref_object_dispose_.467
+ ___Block_byref_object_dispose_.494
+ ___Block_byref_object_dispose_.5082
+ ___Block_byref_object_dispose_.665
+ ___Block_byref_object_dispose_.6930
+ ___Block_byref_object_dispose_.7745
+ ___Block_byref_object_dispose_.9837
+ ___Block_byref_object_dispose_.9904
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSDictionary"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e80_v24?0"MPCAssistantRemoteControlDestination"8?<v?"NSDictionary""NSError">16ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56s64s72bs_e39_v16?0"MPCAssistantSendCommandResult"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1014
+ ___block_literal_global.10404
+ ___block_literal_global.10564
+ ___block_literal_global.10701
+ ___block_literal_global.10996
+ ___block_literal_global.11.14054
+ ___block_literal_global.110.21106
+ ___block_literal_global.11289
+ ___block_literal_global.11618
+ ___block_literal_global.11802
+ ___block_literal_global.11941
+ ___block_literal_global.121.24470
+ ___block_literal_global.12151
+ ___block_literal_global.1277
+ ___block_literal_global.128
+ ___block_literal_global.12904
+ ___block_literal_global.132
+ ___block_literal_global.13719
+ ___block_literal_global.14.21231
+ ___block_literal_global.14068
+ ___block_literal_global.143.24482
+ ___block_literal_global.146.24478
+ ___block_literal_global.14783
+ ___block_literal_global.152.14638
+ ___block_literal_global.157.19564
+ ___block_literal_global.159
+ ___block_literal_global.160.19563
+ ___block_literal_global.16191
+ ___block_literal_global.16306
+ ___block_literal_global.167.10672
+ ___block_literal_global.17105
+ ___block_literal_global.17234
+ ___block_literal_global.17275
+ ___block_literal_global.17347
+ ___block_literal_global.17798
+ ___block_literal_global.17968
+ ___block_literal_global.185
+ ___block_literal_global.19012
+ ___block_literal_global.194
+ ___block_literal_global.19694
+ ___block_literal_global.19768
+ ___block_literal_global.199.23083
+ ___block_literal_global.20708
+ ___block_literal_global.210
+ ___block_literal_global.21230
+ ___block_literal_global.214
+ ___block_literal_global.2151
+ ___block_literal_global.21532
+ ___block_literal_global.21882
+ ___block_literal_global.22168
+ ___block_literal_global.23182
+ ___block_literal_global.2409
+ ___block_literal_global.24508
+ ___block_literal_global.25498
+ ___block_literal_global.26546
+ ___block_literal_global.27084
+ ___block_literal_global.27718
+ ___block_literal_global.282.26318
+ ___block_literal_global.28932
+ ___block_literal_global.29683
+ ___block_literal_global.30.19695
+ ___block_literal_global.30305
+ ___block_literal_global.322.12691
+ ___block_literal_global.34420
+ ___block_literal_global.34828
+ ___block_literal_global.3485
+ ___block_literal_global.357
+ ___block_literal_global.37.21846
+ ___block_literal_global.4034
+ ___block_literal_global.4458
+ ___block_literal_global.45.29670
+ ___block_literal_global.454
+ ___block_literal_global.463
+ ___block_literal_global.47.24494
+ ___block_literal_global.4780
+ ___block_literal_global.5282
+ ___block_literal_global.532
+ ___block_literal_global.547.20258
+ ___block_literal_global.549
+ ___block_literal_global.551
+ ___block_literal_global.619
+ ___block_literal_global.6506
+ ___block_literal_global.696
+ ___block_literal_global.7208
+ ___block_literal_global.7443
+ ___block_literal_global.7751
+ ___block_literal_global.786
+ ___block_literal_global.789
+ ___block_literal_global.9.21851
+ ___block_literal_global.900
+ ___block_literal_global.9981
+ _objc_msgSend$_queueSectionIsAODFromSectionIdentifier:cursor:
+ _objc_msgSend$cachedQueueItemForContentItemID:
+ _objc_msgSend$donateMetricsForTransitionWillStartFrom:to:transitionProvided:
+ _objc_msgSend$musicPlaybackRequestEnvironmentForAccount:
+ _objc_msgSend$musicRequestWithUserIdentity:
+ _objc_msgSend$sendCommand:toDestination:commandID:commandBuilder:completion:
+ _objc_msgSend$setInSmartTransition:
+ _sharedManager.onceToken.34419
- +[MPCPlayPerfMetrics metricsWithTransitionWillStartEvent:cursor:queueItem:]
- +[MPCPlaybackAccountManager sharedManagerIfExists]
- -[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]
- -[MPCPlayPerfMetrics set_transitionItemPosition:]
- -[MPCPlayPerfMetrics set_transitionStyle:]
- -[MPCPlayPerfMetrics transitionItemPosition]
- -[MPCPlayPerfMetrics transitionStyle]
- -[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartEvent:cursor:]
- -[_MPCPlaybackEnginePlayer smartTransitionWillBeginFrom:to:transitionTime:outgoingItemAveragePrePivotTransitionRate:timeStamp:]
- GCC_except_table107
- GCC_except_table1129
- GCC_except_table1133
- GCC_except_table1302
- GCC_except_table1304
- GCC_except_table1350
- GCC_except_table1361
- GCC_except_table1368
- GCC_except_table1375
- GCC_except_table1411
- GCC_except_table1423
- GCC_except_table1432
- GCC_except_table1464
- GCC_except_table1636
- GCC_except_table1638
- GCC_except_table1651
- GCC_except_table1656
- GCC_except_table1725
- GCC_except_table1800
- GCC_except_table1801
- GCC_except_table185
- GCC_except_table1915
- GCC_except_table1935
- GCC_except_table1937
- GCC_except_table1965
- GCC_except_table1974
- GCC_except_table1979
- GCC_except_table1989
- GCC_except_table1999
- GCC_except_table2109
- GCC_except_table2139
- GCC_except_table2164
- GCC_except_table2168
- GCC_except_table2171
- GCC_except_table2220
- GCC_except_table2252
- GCC_except_table2347
- GCC_except_table2363
- GCC_except_table2550
- GCC_except_table2578
- GCC_except_table2604
- GCC_except_table2752
- GCC_except_table2771
- GCC_except_table2778
- GCC_except_table2779
- GCC_except_table2805
- GCC_except_table2815
- GCC_except_table2817
- GCC_except_table2819
- GCC_except_table2822
- GCC_except_table2847
- GCC_except_table2854
- GCC_except_table2859
- GCC_except_table2861
- GCC_except_table2870
- GCC_except_table2878
- GCC_except_table2881
- GCC_except_table2901
- GCC_except_table2909
- GCC_except_table2951
- GCC_except_table3029
- GCC_except_table3040
- GCC_except_table3041
- GCC_except_table3065
- GCC_except_table3073
- GCC_except_table3114
- GCC_except_table3115
- GCC_except_table3131
- GCC_except_table315
- GCC_except_table3189
- GCC_except_table3204
- GCC_except_table3209
- GCC_except_table3246
- GCC_except_table3248
- GCC_except_table325
- GCC_except_table3255
- GCC_except_table3266
- GCC_except_table3271
- GCC_except_table3307
- GCC_except_table3352
- GCC_except_table337
- GCC_except_table338
- GCC_except_table34
- GCC_except_table3474
- GCC_except_table3495
- GCC_except_table3497
- GCC_except_table3498
- GCC_except_table3526
- GCC_except_table3530
- GCC_except_table3540
- GCC_except_table3715
- GCC_except_table3719
- GCC_except_table3730
- GCC_except_table3742
- GCC_except_table3750
- GCC_except_table3759
- GCC_except_table383
- GCC_except_table3882
- GCC_except_table391
- GCC_except_table3926
- GCC_except_table3927
- GCC_except_table3946
- GCC_except_table3954
- GCC_except_table3977
- GCC_except_table3979
- GCC_except_table399
- GCC_except_table3993
- GCC_except_table4016
- GCC_except_table4027
- GCC_except_table408
- GCC_except_table4118
- GCC_except_table4122
- GCC_except_table4131
- GCC_except_table4154
- GCC_except_table4170
- GCC_except_table4275
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table456
- GCC_except_table4581
- GCC_except_table4615
- GCC_except_table4617
- GCC_except_table4625
- GCC_except_table4633
- GCC_except_table4648
- GCC_except_table4656
- GCC_except_table4664
- GCC_except_table4673
- GCC_except_table4688
- GCC_except_table472
- GCC_except_table473
- GCC_except_table4733
- GCC_except_table4757
- GCC_except_table4759
- GCC_except_table4767
- GCC_except_table4820
- GCC_except_table4845
- GCC_except_table489
- GCC_except_table490
- GCC_except_table4958
- GCC_except_table5058
- GCC_except_table5298
- GCC_except_table5299
- GCC_except_table5371
- GCC_except_table5458
- GCC_except_table5607
- GCC_except_table5632
- GCC_except_table5745
- GCC_except_table5827
- GCC_except_table5835
- GCC_except_table5836
- GCC_except_table5900
- GCC_except_table5925
- GCC_except_table5960
- GCC_except_table5963
- GCC_except_table5966
- GCC_except_table6052
- GCC_except_table6267
- GCC_except_table6284
- GCC_except_table6332
- GCC_except_table6345
- GCC_except_table6848
- GCC_except_table7189
- GCC_except_table7281
- GCC_except_table7290
- GCC_except_table7370
- GCC_except_table7377
- GCC_except_table7395
- GCC_except_table741
- GCC_except_table7444
- GCC_except_table7445
- GCC_except_table7453
- GCC_except_table7469
- GCC_except_table797
- GCC_except_table873
- GCC_except_table904
- GCC_except_table907
- GCC_except_table909
- GCC_except_table914
- GCC_except_table916
- GCC_except_table929
- GCC_except_table933
- GCC_except_table939
- GCC_except_table943
- GCC_except_table946
- GCC_except_table949
- _MSVFastHexStringFromBytes.hexCharacters.30087
- __MPCAudioTapFinalize.1823
- __MPCAudioTapInit.1824
- __MPCAudioTapPrepareCallback.1822
- __MPCAudioTapProcess.1817
- __MPCAudioTapUnprepareCallback.1816
- ___123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.688
- ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.561
- ___137-[_MPCQueueControllerBehaviorMusic _qfa_performInsertPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke_2.562
- ___46-[MPCPlayPerfConsumer subscribeToEventStream:]_block_invoke_8
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.101
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.128
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.132
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.137
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.14
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.205
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.210
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.227
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.23
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.235
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.279
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.294
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.35
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.53
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.76
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.94
- ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.187
- ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.212
- ___64-[MPCPlaybackAccountManager _enumerateIdentitiesWithCompletion:]_block_invoke.215
- ___66-[_MPCQueueControllerBehaviorMusic performLoadCommand:completion:]_block_invoke_2
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.271
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.290
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.190
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.200
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.202
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.207
- ___71-[MPCPlaybackAccountManager _buildAccountFromLocalIdentity:completion:]_block_invoke.209
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.171
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke.175
- ___72-[MPCPlaybackAccountManager _updateAccountsWithAttemptCount:completion:]_block_invoke_2.176
- ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.210
- ___75-[MPCPlaybackAccountManager _buildAccountFromDelegatedIdentity:completion:]_block_invoke.211
- ___75-[_MPCQueueControllerBehaviorMusic loadAdditionalUpcomingItems:completion:]_block_invoke.215
- ___76-[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartEvent:cursor:]_block_invoke
- ___76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.710
- ___80-[_MPCQueueControllerBehaviorMusic reshuffleWithTargetContentItemID:completion:]_block_invoke.356
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.105
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.110
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.149
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.28
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.37
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.50
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.60
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.67
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.74
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.79
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.82
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.84
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke.96
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.112
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.150
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.40
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.64
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.75
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.80
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.88
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_2.99
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_3
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_3.116
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_3.78
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_4
- ___83-[MPCAssistantCommandInternal sendCommand:toDestination:commandBuilder:completion:]_block_invoke_5
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.220
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.273
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.279
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.283
- ___95-[_MPCQueueControllerBehaviorMusic finalizeStateRestorationWithTargetContentItemID:completion:]_block_invoke.287
- ___Block_byref_object_copy_.11268
- ___Block_byref_object_copy_.11442
- ___Block_byref_object_copy_.11742
- ___Block_byref_object_copy_.1213
- ___Block_byref_object_copy_.12455
- ___Block_byref_object_copy_.13604
- ___Block_byref_object_copy_.1549
- ___Block_byref_object_copy_.15747
- ___Block_byref_object_copy_.16341
- ___Block_byref_object_copy_.16750
- ___Block_byref_object_copy_.17344
- ___Block_byref_object_copy_.17985
- ___Block_byref_object_copy_.1825
- ___Block_byref_object_copy_.18857
- ___Block_byref_object_copy_.19402
- ___Block_byref_object_copy_.19590
- ___Block_byref_object_copy_.20039
- ___Block_byref_object_copy_.21199
- ___Block_byref_object_copy_.2147
- ___Block_byref_object_copy_.22135
- ___Block_byref_object_copy_.25092
- ___Block_byref_object_copy_.25897
- ___Block_byref_object_copy_.26317
- ___Block_byref_object_copy_.27094
- ___Block_byref_object_copy_.275
- ___Block_byref_object_copy_.28495
- ___Block_byref_object_copy_.29059
- ___Block_byref_object_copy_.2935
- ___Block_byref_object_copy_.33910
- ___Block_byref_object_copy_.34382
- ___Block_byref_object_copy_.34799
- ___Block_byref_object_copy_.3883
- ___Block_byref_object_copy_.4057
- ___Block_byref_object_copy_.469
- ___Block_byref_object_copy_.494
- ___Block_byref_object_copy_.5046
- ___Block_byref_object_copy_.660
- ___Block_byref_object_copy_.6969
- ___Block_byref_object_copy_.7785
- ___Block_byref_object_copy_.9841
- ___Block_byref_object_copy_.9908
- ___Block_byref_object_dispose_.11269
- ___Block_byref_object_dispose_.11443
- ___Block_byref_object_dispose_.11743
- ___Block_byref_object_dispose_.1214
- ___Block_byref_object_dispose_.12456
- ___Block_byref_object_dispose_.13605
- ___Block_byref_object_dispose_.1550
- ___Block_byref_object_dispose_.15748
- ___Block_byref_object_dispose_.16342
- ___Block_byref_object_dispose_.16751
- ___Block_byref_object_dispose_.17345
- ___Block_byref_object_dispose_.17986
- ___Block_byref_object_dispose_.1826
- ___Block_byref_object_dispose_.18858
- ___Block_byref_object_dispose_.19403
- ___Block_byref_object_dispose_.19591
- ___Block_byref_object_dispose_.20040
- ___Block_byref_object_dispose_.21200
- ___Block_byref_object_dispose_.2148
- ___Block_byref_object_dispose_.22136
- ___Block_byref_object_dispose_.25093
- ___Block_byref_object_dispose_.25898
- ___Block_byref_object_dispose_.26318
- ___Block_byref_object_dispose_.27095
- ___Block_byref_object_dispose_.276
- ___Block_byref_object_dispose_.28496
- ___Block_byref_object_dispose_.29060
- ___Block_byref_object_dispose_.2936
- ___Block_byref_object_dispose_.33911
- ___Block_byref_object_dispose_.34383
- ___Block_byref_object_dispose_.34800
- ___Block_byref_object_dispose_.3884
- ___Block_byref_object_dispose_.4058
- ___Block_byref_object_dispose_.470
- ___Block_byref_object_dispose_.495
- ___Block_byref_object_dispose_.5047
- ___Block_byref_object_dispose_.661
- ___Block_byref_object_dispose_.6970
- ___Block_byref_object_dispose_.7786
- ___Block_byref_object_dispose_.9842
- ___Block_byref_object_dispose_.9909
- ___block_descriptor_72_e8_32s40s48s56bs64r_e34_v24?0"NSDictionary"8"NSError"16ls56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e80_v24?0"MPCAssistantRemoteControlDestination"8?<v?"NSDictionary""NSError">16ls56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_84_e8_32s40s48s56s64bs72r_e39_v16?0"MPCAssistantSendCommandResult"8ls32l8r72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1017
- ___block_literal_global.10407
- ___block_literal_global.10567
- ___block_literal_global.10708
- ___block_literal_global.11.14057
- ___block_literal_global.110.21114
- ___block_literal_global.11002
- ___block_literal_global.11295
- ___block_literal_global.11625
- ___block_literal_global.11809
- ___block_literal_global.11948
- ___block_literal_global.121.24475
- ___block_literal_global.12158
- ___block_literal_global.127.21085
- ___block_literal_global.1276
- ___block_literal_global.12918
- ___block_literal_global.131.21086
- ___block_literal_global.13725
- ___block_literal_global.14.21239
- ___block_literal_global.14071
- ___block_literal_global.143.24487
- ___block_literal_global.146.24483
- ___block_literal_global.14803
- ___block_literal_global.152.14658
- ___block_literal_global.157.19578
- ___block_literal_global.160.19577
- ___block_literal_global.16205
- ___block_literal_global.16320
- ___block_literal_global.167.10677
- ___block_literal_global.170.10678
- ___block_literal_global.170.686
- ___block_literal_global.17117
- ___block_literal_global.17244
- ___block_literal_global.17285
- ___block_literal_global.17357
- ___block_literal_global.17808
- ___block_literal_global.179
- ___block_literal_global.17978
- ___block_literal_global.19025
- ___block_literal_global.19708
- ___block_literal_global.19782
- ___block_literal_global.199.23088
- ___block_literal_global.20711
- ___block_literal_global.209
- ___block_literal_global.21238
- ___block_literal_global.21540
- ___block_literal_global.2167
- ___block_literal_global.21890
- ___block_literal_global.221
- ___block_literal_global.22176
- ___block_literal_global.23187
- ___block_literal_global.2369
- ___block_literal_global.24513
- ___block_literal_global.25507
- ___block_literal_global.26557
- ___block_literal_global.27083
- ___block_literal_global.27715
- ___block_literal_global.282.26330
- ___block_literal_global.28929
- ___block_literal_global.29679
- ___block_literal_global.30.19709
- ___block_literal_global.30302
- ___block_literal_global.322.12706
- ___block_literal_global.3416
- ___block_literal_global.34421
- ___block_literal_global.34829
- ___block_literal_global.355
- ___block_literal_global.37.21854
- ___block_literal_global.3956
- ___block_literal_global.4379
- ___block_literal_global.45.29666
- ___block_literal_global.458
- ___block_literal_global.462
- ___block_literal_global.4696
- ___block_literal_global.47.24499
- ___block_literal_global.5175
- ___block_literal_global.531
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.550
- ___block_literal_global.618
- ___block_literal_global.6570
- ___block_literal_global.697
- ___block_literal_global.7261
- ___block_literal_global.7499
- ___block_literal_global.7792
- ___block_literal_global.785
- ___block_literal_global.788
- ___block_literal_global.9.21859
- ___block_literal_global.903
- ___block_literal_global.9986
- _objc_msgSend$donateMetricsForTransitionWillStartEvent:cursor:
- _objc_msgSend$metricsWithTransitionWillStartEvent:cursor:queueItem:
- _objc_msgSend$sendCommand:toDestination:commandBuilder:completion:
- _objc_msgSend$setInTransition:
- _objc_msgSend$set_transitionItemPosition:
- _objc_msgSend$set_transitionStyle:
- _objc_msgSend$transitionItemPosition
- _sharedManager.onceToken.34420
CStrings:
+ "@\"<MFQueuePlayerItem>\"24@0:8@\"NSString\"16"
+ "BeatMatchedTransitionHasRendered"
+ "CurrentTimeStampHang"
+ "[ALC] Successfully set BeatMatchedTransitionHasRendered = true"
+ "[SPIR:%{sonic:fourCC}u] setIdentifiers:forDatabase: | failing remaining prioritizedStoreIDs [LOD identifiers lost] prioritizedStoreIDs=%{public}@"
+ "_queueSectionIsAODFromSectionIdentifier:cursor:"
+ "cachedQueueItemForContentItemID:"
+ "donateMetricsForTransitionWillStartFrom:to:transitionProvided:"
+ "musicPlaybackRequestEnvironmentForAccount:"
+ "pauseInitiated"
+ "sendCommand:toDestination:commandID:commandBuilder:completion:"
+ "setInSmartTransition:"
+ "smartTransitionWillBeginFrom:to:transitionTime:outgoingItemAveragePrePivotTransitionRate:timeStamp:parameters:"
+ "v52@0:8I16@20@28@?36@?44"
+ "v64@0:8@\"<MFQueuePlayerItem>\"16@\"<MFQueuePlayerItem>\"24@\"<MFOverlappingTransitionTime>\"32d40@\"<MFTimeStamp>\"48@\"NSDictionary\"56"
+ "v64@0:8@16@24@32d40@48@56"
+ "|%{public}@ %{public}@ %2i %{public}@  │ recommendation-data: %{public}@"
+ "|%{public}@ %{public}@ %2i %{public}@  │ siri-reference-id: %{public}@"
+ "|%{public}@ %{public}@ %2i %{public}@  ╰ siri-wha-metrics: %{public}@"
- "T@\"NSNumber\",&,D,N,Sset_transitionItemPosition:"
- "T@\"NSNumber\",&,D,N,Sset_transitionStyle:"
- "TransitionWillStart event doesn't have corresponding TransitionCreated event (eventID:%{public}@ startItemId:%{public}@ %{public}@)"
- "TransitionWillStart event doesn't have valid item identifiers (eventID:%{public}@)"
- "donateMetricsForTransitionWillStartEvent:cursor:"
- "metricsWithTransitionWillStartEvent:cursor:queueItem:"
- "sendCommand:toDestination:commandBuilder:completion:"
- "setInTransition:"
- "set_transitionItemPosition:"
- "set_transitionStyle:"
- "sharedManagerIfExists"
- "smartTransitionWillBeginFrom:to:transitionTime:outgoingItemAveragePrePivotTransitionRate:timeStamp:"
- "transitionItemPosition"
- "v44@0:8I16@20@?28@?36"
- "v56@0:8@\"<MFQueuePlayerItem>\"16@\"<MFQueuePlayerItem>\"24@\"<MFOverlappingTransitionTime>\"32d40@\"<MFTimeStamp>\"48"
- "v56@0:8@16@24@32d40@48"

```
