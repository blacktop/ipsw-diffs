## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-25110.25.31.601.0
-  __TEXT.__text: 0x3e77cc
-  __TEXT.__auth_stubs: 0x5970
-  __TEXT.__objc_methlist: 0x17008
+25200.25.36.501.0
+  __TEXT.__text: 0x3aef3c
+  __TEXT.__auth_stubs: 0x5830
+  __TEXT.__objc_methlist: 0x16f50
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x15ab0
-  __TEXT.__cstring: 0x2f6bd
-  __TEXT.__constg_swiftt: 0x7550
-  __TEXT.__swift5_typeref: 0x5012
-  __TEXT.__swift5_reflstr: 0x4f32
-  __TEXT.__swift5_fieldmd: 0x4c28
-  __TEXT.__swift5_builtin: 0x758
-  __TEXT.__swift5_assocty: 0xf38
-  __TEXT.__swift5_capture: 0x3364
-  __TEXT.__oslogstring: 0x3bee0
-  __TEXT.__swift5_mpenum: 0x104
-  __TEXT.__swift5_proto: 0x9c8
-  __TEXT.__swift5_types: 0x538
-  __TEXT.__swift_as_entry: 0x3b8
-  __TEXT.__swift_as_ret: 0x4bc
-  __TEXT.__swift5_protos: 0xf0
+  __TEXT.__const: 0x14420
+  __TEXT.__cstring: 0x2e8bb
+  __TEXT.__constg_swiftt: 0x6a34
+  __TEXT.__swift5_typeref: 0x46c0
+  __TEXT.__swift5_reflstr: 0x4428
+  __TEXT.__swift5_fieldmd: 0x42e0
+  __TEXT.__swift5_builtin: 0x71c
+  __TEXT.__swift5_assocty: 0xd68
+  __TEXT.__swift5_capture: 0x2e54
+  __TEXT.__oslogstring: 0x3a7e5
+  __TEXT.__swift5_mpenum: 0xe0
+  __TEXT.__swift5_proto: 0x8f4
+  __TEXT.__swift5_types: 0x4a8
+  __TEXT.__swift_as_entry: 0x30c
+  __TEXT.__swift_as_ret: 0x3e4
+  __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x67f0
+  __TEXT.__gcc_except_tab: 0x67b0
   __TEXT.__ustring: 0x4b4
-  __TEXT.__unwind_info: 0xc0f0
-  __TEXT.__eh_frame: 0xca50
-  __TEXT.__objc_classname: 0x3d25
-  __TEXT.__objc_methname: 0x38aba
-  __TEXT.__objc_methtype: 0x99b9
-  __TEXT.__objc_stubs: 0x26780
-  __DATA_CONST.__got: 0x2eb8
-  __DATA_CONST.__const: 0x90f0
-  __DATA_CONST.__objc_classlist: 0xcc8
+  __TEXT.__unwind_info: 0xb298
+  __TEXT.__eh_frame: 0xa4ac
+  __TEXT.__objc_classname: 0x3d26
+  __TEXT.__objc_methname: 0x38d56
+  __TEXT.__objc_methtype: 0x9a71
+  __TEXT.__objc_stubs: 0x26800
+  __DATA_CONST.__got: 0x2e68
+  __DATA_CONST.__const: 0x9118
+  __DATA_CONST.__objc_classlist: 0xc90
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc228
+  __DATA_CONST.__objc_selrefs: 0xc2a0
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6c0
-  __DATA_CONST.__objc_arraydata: 0x268
-  __AUTH_CONST.__auth_got: 0x2cc8
-  __AUTH_CONST.__const: 0xfaf8
-  __AUTH_CONST.__cfstring: 0x1d360
-  __AUTH_CONST.__objc_const: 0x32820
+  __DATA_CONST.__objc_arraydata: 0x270
+  __AUTH_CONST.__auth_got: 0x2c28
+  __AUTH_CONST.__const: 0xe2f8
+  __AUTH_CONST.__cfstring: 0x1d3c0
+  __AUTH_CONST.__objc_const: 0x31b88
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x4d10
-  __AUTH.__data: 0x3270
-  __DATA.__objc_ivar: 0x19c8
-  __DATA.__data: 0x7178
-  __DATA.__bss: 0x101d0
-  __DATA.__common: 0x1d8
-  __DATA_DIRTY.__objc_data: 0x3930
-  __DATA_DIRTY.__data: 0x4700
+  __AUTH.__objc_data: 0x4c10
+  __AUTH.__data: 0x2950
+  __DATA.__objc_ivar: 0x19d0
+  __DATA.__data: 0x6b68
+  __DATA.__bss: 0xf050
+  __DATA.__common: 0x1d0
+  __DATA_DIRTY.__objc_data: 0x3938
+  __DATA_DIRTY.__data: 0x46b0
   __DATA_DIRTY.__bss: 0x13b0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6043D7E3-AF2C-3478-B684-4694DFDAC63C
-  Functions: 19698
-  Symbols:   38289
-  CStrings:  22462
+  UUID: 31971946-07BA-3E74-AC57-38E7902BEBCD
+  Functions: 18399
+  Symbols:   37260
+  CStrings:  22308
 
Symbols:
+ -[MPCMediaRemoteController _initWithResolvedPlayerPath:]
+ -[MPCMediaRemoteMiddleware(MPCPlayerResponseBuilder) playerItemTransitionInfo:atIndexPath:chain:]
+ -[MPCPlayerResponseItem transitionInfo]
+ -[_MPCMediaRemoteNullController _initWithResolvedPlayerPath:]
+ -[_MPCMediaRemotePublisher _commandRequiresMediaServices:]
+ -[_MPCPlaybackEnginePlayer performWhenMediaServicesAreAvailable:identifier:]
+ -[_MPCQueueControllerBehaviorMusic resolvedTransitionStyle]
+ -[_MPCQueueControllerBehaviorMusic shouldDowngradeTransitionStyle]
+ GCC_except_table1911
+ GCC_except_table1933
+ GCC_except_table1961
+ GCC_except_table1970
+ GCC_except_table1975
+ GCC_except_table1985
+ GCC_except_table1995
+ GCC_except_table2105
+ GCC_except_table2135
+ GCC_except_table2160
+ GCC_except_table2164
+ GCC_except_table2167
+ GCC_except_table2216
+ GCC_except_table2248
+ GCC_except_table2343
+ GCC_except_table2359
+ GCC_except_table2546
+ GCC_except_table2574
+ GCC_except_table2600
+ GCC_except_table2748
+ GCC_except_table2767
+ GCC_except_table2774
+ GCC_except_table2775
+ GCC_except_table2801
+ GCC_except_table2805
+ GCC_except_table2815
+ GCC_except_table2818
+ GCC_except_table2843
+ GCC_except_table2850
+ GCC_except_table2857
+ GCC_except_table2860
+ GCC_except_table2865
+ GCC_except_table2866
+ GCC_except_table2871
+ GCC_except_table2874
+ GCC_except_table2877
+ GCC_except_table2897
+ GCC_except_table2905
+ GCC_except_table2947
+ GCC_except_table3025
+ GCC_except_table3036
+ GCC_except_table3037
+ GCC_except_table3061
+ GCC_except_table3069
+ GCC_except_table3110
+ GCC_except_table3111
+ GCC_except_table3127
+ GCC_except_table3185
+ GCC_except_table3200
+ GCC_except_table3205
+ GCC_except_table3244
+ GCC_except_table3251
+ GCC_except_table3262
+ GCC_except_table3267
+ GCC_except_table3303
+ GCC_except_table3348
+ GCC_except_table3470
+ GCC_except_table3493
+ GCC_except_table3494
+ GCC_except_table3522
+ GCC_except_table3526
+ GCC_except_table3536
+ GCC_except_table3712
+ GCC_except_table3716
+ GCC_except_table3727
+ GCC_except_table3739
+ GCC_except_table3741
+ GCC_except_table3747
+ GCC_except_table3756
+ GCC_except_table3880
+ GCC_except_table3924
+ GCC_except_table3925
+ GCC_except_table3944
+ GCC_except_table3952
+ GCC_except_table3970
+ GCC_except_table3975
+ GCC_except_table3977
+ GCC_except_table3991
+ GCC_except_table4014
+ GCC_except_table4025
+ GCC_except_table4111
+ GCC_except_table4116
+ GCC_except_table4120
+ GCC_except_table4129
+ GCC_except_table4152
+ GCC_except_table4168
+ GCC_except_table4273
+ GCC_except_table4394
+ GCC_except_table4395
+ GCC_except_table4579
+ GCC_except_table4613
+ GCC_except_table4615
+ GCC_except_table4623
+ GCC_except_table4631
+ GCC_except_table4646
+ GCC_except_table4654
+ GCC_except_table4662
+ GCC_except_table4671
+ GCC_except_table4686
+ GCC_except_table4731
+ GCC_except_table4755
+ GCC_except_table4758
+ GCC_except_table4766
+ GCC_except_table4819
+ GCC_except_table4845
+ GCC_except_table4956
+ GCC_except_table5056
+ GCC_except_table5296
+ GCC_except_table5297
+ GCC_except_table5369
+ GCC_except_table5456
+ GCC_except_table5605
+ GCC_except_table5630
+ GCC_except_table5743
+ GCC_except_table5824
+ GCC_except_table5832
+ GCC_except_table5833
+ GCC_except_table5897
+ GCC_except_table5922
+ GCC_except_table5957
+ GCC_except_table5960
+ GCC_except_table5963
+ GCC_except_table6049
+ GCC_except_table6265
+ GCC_except_table6282
+ GCC_except_table6330
+ GCC_except_table6343
+ GCC_except_table6847
+ GCC_except_table7188
+ GCC_except_table7280
+ GCC_except_table7289
+ GCC_except_table7369
+ GCC_except_table7376
+ GCC_except_table7394
+ GCC_except_table7444
+ GCC_except_table7447
+ GCC_except_table7452
+ GCC_except_table7468
+ _MSVFastHexStringFromBytes.hexCharacters.30043
+ _OBJC_CLASS_$_AMSMetricsIdentifierKey
+ _OBJC_CLASS_$_AMSMetricsIdentifierStore
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_IVAR_$_MPCPlayerResponseItem._transitionInfo
+ _OBJC_IVAR_$__MPCPlaybackEnginePlayer._mediaServicesWaitingBlocks
+ _OBJC_IVAR_$__MPCQueueControllerBehaviorMusic._userToggledTransitionsInDowngradeState
+ _OUTLINED_FUNCTION_342
+ _OUTLINED_FUNCTION_343
+ _OUTLINED_FUNCTION_344
+ _OUTLINED_FUNCTION_345
+ _OUTLINED_FUNCTION_346
+ _OUTLINED_FUNCTION_347
+ _OUTLINED_FUNCTION_348
+ _OUTLINED_FUNCTION_349
+ _OUTLINED_FUNCTION_350
+ _OUTLINED_FUNCTION_351
+ _OUTLINED_FUNCTION_352
+ __OBJC_$_INSTANCE_METHODS_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|PreferredAudioTimePitchAlgorithm|Reuse|MediaPlaybackCore3|MFQueuePlayerItem|MPCReportingAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|PreferredAudioTimePitchAlgorithm|Reuse|MediaPlaybackCore3|MFQueuePlayerItem|MPCReportingAdditions)
+ __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.37
+ ___54-[MPCPlaybackEngine schedulePlaybackStatePreservation]_block_invoke.194
+ ___55-[MPCPlayActivityFeedEventConsumer _finalizePAFEvents:]_block_invoke.146
+ ___56-[MPCMediaRemoteController _initWithResolvedPlayerPath:]_block_invoke
+ ___56-[MPCMediaRemoteController _initWithResolvedPlayerPath:]_block_invoke_2
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.524
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.574
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.576
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.596
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.644
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.651
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.677
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.699
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.717
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.739
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.743
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.750
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.759
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.774
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.787
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.791
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_10.620
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_11.630
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.532
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.575
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.577
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.597
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.658
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.690
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.700
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.718
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.536
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.601
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.703
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.723
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.540
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.602
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.705
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.728
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.552
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.606
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.733
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.556
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.613
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.560
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.614
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.567
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.618
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.619
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.189
+ ___61-[_MPCMediaRemotePublisher _dispatchCommandEvent:completion:]_block_invoke_2
+ ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.801
+ ___68-[_MPCPlaybackEnginePlayer togglePlaybackWithIdentifier:completion:]_block_invoke.73
+ ___Block_byref_object_copy_.11261
+ ___Block_byref_object_copy_.11434
+ ___Block_byref_object_copy_.11734
+ ___Block_byref_object_copy_.12439
+ ___Block_byref_object_copy_.13603
+ ___Block_byref_object_copy_.15758
+ ___Block_byref_object_copy_.16352
+ ___Block_byref_object_copy_.16761
+ ___Block_byref_object_copy_.17359
+ ___Block_byref_object_copy_.18000
+ ___Block_byref_object_copy_.18875
+ ___Block_byref_object_copy_.19418
+ ___Block_byref_object_copy_.19604
+ ___Block_byref_object_copy_.20062
+ ___Block_byref_object_copy_.21149
+ ___Block_byref_object_copy_.2131
+ ___Block_byref_object_copy_.22085
+ ___Block_byref_object_copy_.25038
+ ___Block_byref_object_copy_.25843
+ ___Block_byref_object_copy_.26265
+ ___Block_byref_object_copy_.26605
+ ___Block_byref_object_copy_.27040
+ ___Block_byref_object_copy_.28446
+ ___Block_byref_object_copy_.29012
+ ___Block_byref_object_copy_.3202
+ ___Block_byref_object_copy_.33851
+ ___Block_byref_object_copy_.34323
+ ___Block_byref_object_copy_.34740
+ ___Block_byref_object_copy_.35099
+ ___Block_byref_object_copy_.3961
+ ___Block_byref_object_copy_.4134
+ ___Block_byref_object_copy_.5081
+ ___Block_byref_object_copy_.6928
+ ___Block_byref_object_copy_.7743
+ ___Block_byref_object_copy_.9835
+ ___Block_byref_object_copy_.9902
+ ___Block_byref_object_dispose_.11262
+ ___Block_byref_object_dispose_.11435
+ ___Block_byref_object_dispose_.11735
+ ___Block_byref_object_dispose_.12440
+ ___Block_byref_object_dispose_.13604
+ ___Block_byref_object_dispose_.15759
+ ___Block_byref_object_dispose_.16353
+ ___Block_byref_object_dispose_.16762
+ ___Block_byref_object_dispose_.17360
+ ___Block_byref_object_dispose_.18001
+ ___Block_byref_object_dispose_.18876
+ ___Block_byref_object_dispose_.19419
+ ___Block_byref_object_dispose_.19605
+ ___Block_byref_object_dispose_.20063
+ ___Block_byref_object_dispose_.21150
+ ___Block_byref_object_dispose_.2132
+ ___Block_byref_object_dispose_.22086
+ ___Block_byref_object_dispose_.25039
+ ___Block_byref_object_dispose_.25844
+ ___Block_byref_object_dispose_.26266
+ ___Block_byref_object_dispose_.26606
+ ___Block_byref_object_dispose_.27041
+ ___Block_byref_object_dispose_.28447
+ ___Block_byref_object_dispose_.29013
+ ___Block_byref_object_dispose_.3203
+ ___Block_byref_object_dispose_.33852
+ ___Block_byref_object_dispose_.34324
+ ___Block_byref_object_dispose_.34741
+ ___Block_byref_object_dispose_.35100
+ ___Block_byref_object_dispose_.3962
+ ___Block_byref_object_dispose_.4135
+ ___Block_byref_object_dispose_.5082
+ ___Block_byref_object_dispose_.6929
+ ___Block_byref_object_dispose_.7744
+ ___Block_byref_object_dispose_.9836
+ ___Block_byref_object_dispose_.9903
+ ___block_descriptor_117_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
+ ___block_descriptor_49_e8_32s40bs_e43_v24?0"MPRemotePlaybackQueue"8"NSError"16ls32l8s40l8
+ ___block_literal_global.10403
+ ___block_literal_global.10563
+ ___block_literal_global.10700
+ ___block_literal_global.10995
+ ___block_literal_global.11.14060
+ ___block_literal_global.110.21064
+ ___block_literal_global.11288
+ ___block_literal_global.11617
+ ___block_literal_global.11801
+ ___block_literal_global.11940
+ ___block_literal_global.121.24424
+ ___block_literal_global.12150
+ ___block_literal_global.1280
+ ___block_literal_global.12906
+ ___block_literal_global.135
+ ___block_literal_global.13725
+ ___block_literal_global.14.21189
+ ___block_literal_global.14074
+ ___block_literal_global.143.24436
+ ___block_literal_global.146.24432
+ ___block_literal_global.14811
+ ___block_literal_global.152.14666
+ ___block_literal_global.157.19592
+ ___block_literal_global.160.19591
+ ___block_literal_global.16216
+ ___block_literal_global.16331
+ ___block_literal_global.167.10671
+ ___block_literal_global.17130
+ ___block_literal_global.17259
+ ___block_literal_global.17300
+ ___block_literal_global.17372
+ ___block_literal_global.17823
+ ___block_literal_global.17993
+ ___block_literal_global.19039
+ ___block_literal_global.19722
+ ___block_literal_global.19796
+ ___block_literal_global.206
+ ___block_literal_global.20678
+ ___block_literal_global.211
+ ___block_literal_global.21188
+ ___block_literal_global.21490
+ ___block_literal_global.2151
+ ___block_literal_global.21840
+ ___block_literal_global.22126
+ ___block_literal_global.23131
+ ___block_literal_global.2409
+ ___block_literal_global.24462
+ ___block_literal_global.25452
+ ___block_literal_global.26505
+ ___block_literal_global.27029
+ ___block_literal_global.27664
+ ___block_literal_global.280
+ ___block_literal_global.282.26277
+ ___block_literal_global.285
+ ___block_literal_global.28882
+ ___block_literal_global.29635
+ ___block_literal_global.30.19723
+ ___block_literal_global.30256
+ ___block_literal_global.322.12690
+ ___block_literal_global.34362
+ ___block_literal_global.34770
+ ___block_literal_global.3485
+ ___block_literal_global.37.21804
+ ___block_literal_global.4034
+ ___block_literal_global.4458
+ ___block_literal_global.45.29622
+ ___block_literal_global.47.24448
+ ___block_literal_global.4780
+ ___block_literal_global.5282
+ ___block_literal_global.542
+ ___block_literal_global.637
+ ___block_literal_global.6506
+ ___block_literal_global.653
+ ___block_literal_global.702
+ ___block_literal_global.7207
+ ___block_literal_global.726
+ ___block_literal_global.730
+ ___block_literal_global.735
+ ___block_literal_global.7442
+ ___block_literal_global.7750
+ ___block_literal_global.9.21809
+ ___block_literal_global.960
+ ___block_literal_global.9980
+ ___swift_memcpy6_1
+ _block_copy_helper.111
+ _block_copy_helper.115
+ _block_copy_helper.146
+ _block_copy_helper.15
+ _block_copy_helper.161
+ _block_copy_helper.164
+ _block_copy_helper.167
+ _block_copy_helper.171
+ _block_copy_helper.185
+ _block_copy_helper.189
+ _block_copy_helper.205
+ _block_copy_helper.213
+ _block_copy_helper.221
+ _block_copy_helper.229
+ _block_copy_helper.34
+ _block_copy_helper.45
+ _block_copy_helper.53
+ _block_copy_helper.56
+ _block_copy_helper.64
+ _block_copy_helper.70
+ _block_copy_helper.97
+ _block_descriptor.113
+ _block_descriptor.117
+ _block_descriptor.148
+ _block_descriptor.163
+ _block_descriptor.166
+ _block_descriptor.169
+ _block_descriptor.17
+ _block_descriptor.173
+ _block_descriptor.187
+ _block_descriptor.191
+ _block_descriptor.207
+ _block_descriptor.215
+ _block_descriptor.223
+ _block_descriptor.231
+ _block_descriptor.36
+ _block_descriptor.47
+ _block_descriptor.55
+ _block_descriptor.58
+ _block_descriptor.66
+ _block_descriptor.72
+ _block_descriptor.99
+ _block_destroy_helper.112
+ _block_destroy_helper.116
+ _block_destroy_helper.147
+ _block_destroy_helper.16
+ _block_destroy_helper.162
+ _block_destroy_helper.165
+ _block_destroy_helper.168
+ _block_destroy_helper.172
+ _block_destroy_helper.186
+ _block_destroy_helper.190
+ _block_destroy_helper.206
+ _block_destroy_helper.214
+ _block_destroy_helper.222
+ _block_destroy_helper.230
+ _block_destroy_helper.35
+ _block_destroy_helper.46
+ _block_destroy_helper.54
+ _block_destroy_helper.57
+ _block_destroy_helper.65
+ _block_destroy_helper.71
+ _block_destroy_helper.98
+ _kCMTimebaseNotificationKey_EventTime
+ _objc_msgSend$_commandRequiresMediaServices:
+ _objc_msgSend$_initWithResolvedPlayerPath:
+ _objc_msgSend$mediaServicesAvailable
+ _objc_msgSend$performWhenMediaServicesAreAvailable:identifier:
+ _objc_msgSend$playerItemTransitionInfo:atIndexPath:chain:
+ _objc_msgSend$resolvedTransitionStyle
+ _objc_msgSend$shouldDowngradeTransitionStyle
+ _objc_msgSend$transitionInfo
+ _objectdestroy.144Tm
+ _objectdestroy.207Tm
+ _objectdestroy.219Tm
+ _objectdestroy.22Tm
+ _objectdestroy.43Tm
+ _objectdestroy.54Tm
+ _objectdestroy.62Tm
+ _sharedManager.onceToken.34361
+ _symbolic SSSgAAIeggg_
+ _symbolic _____Sg So38AVAudioApplicationEnhanceDialogueLevelV
+ _symbolic _____SgXw 17MediaPlaybackCore13PodcastAVItemC22EnhanceDialogueSessionC
- -[MPCMediaRemoteController _init]
- -[MPCMediaRemoteController setResolvedPlayerPath:]
- -[_MPCMediaRemoteNullController _init]
- -[_MPCMediaRemotePublisher engineDidLoseMediaServices:]
- -[_MPCMediaRemotePublisher engineDidResetMediaServices:]
- GCC_except_table1909
- GCC_except_table1929
- GCC_except_table1959
- GCC_except_table1968
- GCC_except_table1973
- GCC_except_table1983
- GCC_except_table1993
- GCC_except_table2103
- GCC_except_table2133
- GCC_except_table2158
- GCC_except_table2162
- GCC_except_table2165
- GCC_except_table2214
- GCC_except_table2246
- GCC_except_table2341
- GCC_except_table2357
- GCC_except_table2544
- GCC_except_table2572
- GCC_except_table2598
- GCC_except_table2746
- GCC_except_table2765
- GCC_except_table2772
- GCC_except_table2773
- GCC_except_table2797
- GCC_except_table2803
- GCC_except_table2807
- GCC_except_table2816
- GCC_except_table2841
- GCC_except_table2848
- GCC_except_table2853
- GCC_except_table2858
- GCC_except_table2863
- GCC_except_table2864
- GCC_except_table2869
- GCC_except_table2872
- GCC_except_table2875
- GCC_except_table2895
- GCC_except_table2903
- GCC_except_table2945
- GCC_except_table3023
- GCC_except_table3034
- GCC_except_table3035
- GCC_except_table3059
- GCC_except_table3067
- GCC_except_table3108
- GCC_except_table3109
- GCC_except_table3125
- GCC_except_table3183
- GCC_except_table3198
- GCC_except_table3203
- GCC_except_table3240
- GCC_except_table3249
- GCC_except_table3260
- GCC_except_table3265
- GCC_except_table3301
- GCC_except_table3346
- GCC_except_table3468
- GCC_except_table3489
- GCC_except_table3492
- GCC_except_table3520
- GCC_except_table3524
- GCC_except_table3534
- GCC_except_table3709
- GCC_except_table3713
- GCC_except_table3724
- GCC_except_table3736
- GCC_except_table3738
- GCC_except_table3744
- GCC_except_table3753
- GCC_except_table3877
- GCC_except_table3921
- GCC_except_table3922
- GCC_except_table3941
- GCC_except_table3949
- GCC_except_table3967
- GCC_except_table3972
- GCC_except_table3974
- GCC_except_table3988
- GCC_except_table4011
- GCC_except_table4022
- GCC_except_table4108
- GCC_except_table4113
- GCC_except_table4117
- GCC_except_table4126
- GCC_except_table4149
- GCC_except_table4165
- GCC_except_table4270
- GCC_except_table4391
- GCC_except_table4392
- GCC_except_table4576
- GCC_except_table4610
- GCC_except_table4612
- GCC_except_table4620
- GCC_except_table4628
- GCC_except_table4643
- GCC_except_table4651
- GCC_except_table4659
- GCC_except_table4668
- GCC_except_table4683
- GCC_except_table4728
- GCC_except_table4752
- GCC_except_table4754
- GCC_except_table4762
- GCC_except_table4815
- GCC_except_table4840
- GCC_except_table4953
- GCC_except_table5053
- GCC_except_table5293
- GCC_except_table5294
- GCC_except_table5366
- GCC_except_table5453
- GCC_except_table5602
- GCC_except_table5627
- GCC_except_table5740
- GCC_except_table5822
- GCC_except_table5830
- GCC_except_table5831
- GCC_except_table5895
- GCC_except_table5920
- GCC_except_table5955
- GCC_except_table5958
- GCC_except_table5961
- GCC_except_table6047
- GCC_except_table6262
- GCC_except_table6279
- GCC_except_table6327
- GCC_except_table6340
- GCC_except_table6843
- GCC_except_table7184
- GCC_except_table7276
- GCC_except_table7285
- GCC_except_table7365
- GCC_except_table7372
- GCC_except_table7390
- GCC_except_table7439
- GCC_except_table7440
- GCC_except_table7448
- GCC_except_table7464
- _MSVFastHexStringFromBytes.hexCharacters.30090
- _OBJC_IVAR_$__MPCMediaRemotePublisher._mediaServerAvailable
- _OBJC_METACLASS_$__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __DATA__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __DATA__TtC17MediaPlaybackCore28TimelineAssetQueueController
- __DATA__TtC17MediaPlaybackCore32MPCPlaybackEngineContentProvider
- __DATA__TtCCO17MediaPlaybackCore11MPCTimeline16InMemoryTimelineP33_4A967C9508C5257B5F66FE833F259B5223TargetEventContinuation
- __DATA__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __DATA__TtCO17MediaPlaybackCore11MPCTimeline10RenderTask
- __DATA__TtCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline
- __INSTANCE_METHODS__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __INSTANCE_METHODS__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __IVARS__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __IVARS__TtC17MediaPlaybackCore28TimelineAssetQueueController
- __IVARS__TtC17MediaPlaybackCore32MPCPlaybackEngineContentProvider
- __IVARS__TtCCO17MediaPlaybackCore11MPCTimeline16InMemoryTimelineP33_4A967C9508C5257B5F66FE833F259B5223TargetEventContinuation
- __IVARS__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __IVARS__TtCO17MediaPlaybackCore11MPCTimeline10RenderTask
- __IVARS__TtCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline
- __IVARS__TtCO17MediaPlaybackCore11MPCTimeline20ChangeEventPublisher
- __IVARS__TtCO17MediaPlaybackCore11MPCTimeline22RendererImplementation
- __METACLASS_DATA__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __METACLASS_DATA__TtC17MediaPlaybackCore28TimelineAssetQueueController
- __METACLASS_DATA__TtC17MediaPlaybackCore32MPCPlaybackEngineContentProvider
- __METACLASS_DATA__TtCCO17MediaPlaybackCore11MPCTimeline16InMemoryTimelineP33_4A967C9508C5257B5F66FE833F259B5223TargetEventContinuation
- __METACLASS_DATA__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __METACLASS_DATA__TtCO17MediaPlaybackCore11MPCTimeline10RenderTask
- __METACLASS_DATA__TtCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline
- __OBJC_$_INSTANCE_METHODS_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|MediaPlaybackCore3|PreferredAudioTimePitchAlgorithm|Reuse|MFQueuePlayerItem|MPCReportingAdditions)
- __OBJC_$_INSTANCE_METHODS__TtC17MediaPlaybackCore28TimelineAssetQueueController(MediaPlaybackCore)
- __OBJC_CLASS_PROTOCOLS_$_MPAVItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore2|MediaPlaybackCore3|PreferredAudioTimePitchAlgorithm|Reuse|MFQueuePlayerItem|MPCReportingAdditions)
- __OBJC_CLASS_PROTOCOLS_$__TtC17MediaPlaybackCore28TimelineAssetQueueController(MediaPlaybackCore)
- __PROPERTIES__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __PROPERTIES__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.39
- __PROTOCOLS__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator
- __PROTOCOLS__TtC17MediaPlaybackCore26MPCTimelineQueueTranslator.2
- __PROTOCOLS__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask
- __PROTOCOLS__TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask.11
- ___33-[MPCMediaRemoteController _init]_block_invoke
- ___33-[MPCMediaRemoteController _init]_block_invoke_2
- ___54-[MPCPlaybackEngine schedulePlaybackStatePreservation]_block_invoke.187
- ___55-[MPCPlayActivityFeedEventConsumer _finalizePAFEvents:]_block_invoke.143
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.501
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.529
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.579
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.581
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.601
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.647
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.657
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.680
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.702
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.720
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.742
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.746
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.753
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.762
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.777
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.790
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.794
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.505
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.537
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.580
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.582
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.602
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.661
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.693
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.703
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.721
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.541
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.606
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.706
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.726
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.545
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.607
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.708
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.731
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.557
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.611
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.736
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.561
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.618
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.565
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.619
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.572
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.623
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.624
- ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.190
- ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.804
- ___68-[_MPCPlaybackEnginePlayer togglePlaybackWithIdentifier:completion:]_block_invoke.75
- ___Block_byref_object_copy_.11262
- ___Block_byref_object_copy_.11436
- ___Block_byref_object_copy_.11736
- ___Block_byref_object_copy_.12441
- ___Block_byref_object_copy_.13596
- ___Block_byref_object_copy_.15737
- ___Block_byref_object_copy_.16331
- ___Block_byref_object_copy_.16740
- ___Block_byref_object_copy_.17339
- ___Block_byref_object_copy_.17980
- ___Block_byref_object_copy_.18855
- ___Block_byref_object_copy_.19396
- ___Block_byref_object_copy_.19580
- ___Block_byref_object_copy_.20030
- ___Block_byref_object_copy_.21195
- ___Block_byref_object_copy_.2135
- ___Block_byref_object_copy_.22131
- ___Block_byref_object_copy_.25084
- ___Block_byref_object_copy_.25888
- ___Block_byref_object_copy_.26308
- ___Block_byref_object_copy_.26659
- ___Block_byref_object_copy_.27094
- ___Block_byref_object_copy_.28497
- ___Block_byref_object_copy_.29061
- ___Block_byref_object_copy_.3208
- ___Block_byref_object_copy_.33906
- ___Block_byref_object_copy_.34378
- ___Block_byref_object_copy_.34795
- ___Block_byref_object_copy_.35154
- ___Block_byref_object_copy_.3973
- ___Block_byref_object_copy_.4146
- ___Block_byref_object_copy_.5094
- ___Block_byref_object_copy_.6941
- ___Block_byref_object_copy_.7753
- ___Block_byref_object_copy_.9843
- ___Block_byref_object_copy_.9910
- ___Block_byref_object_dispose_.11263
- ___Block_byref_object_dispose_.11437
- ___Block_byref_object_dispose_.11737
- ___Block_byref_object_dispose_.12442
- ___Block_byref_object_dispose_.13597
- ___Block_byref_object_dispose_.15738
- ___Block_byref_object_dispose_.16332
- ___Block_byref_object_dispose_.16741
- ___Block_byref_object_dispose_.17340
- ___Block_byref_object_dispose_.17981
- ___Block_byref_object_dispose_.18856
- ___Block_byref_object_dispose_.19397
- ___Block_byref_object_dispose_.19581
- ___Block_byref_object_dispose_.20031
- ___Block_byref_object_dispose_.21196
- ___Block_byref_object_dispose_.2136
- ___Block_byref_object_dispose_.22132
- ___Block_byref_object_dispose_.25085
- ___Block_byref_object_dispose_.25889
- ___Block_byref_object_dispose_.26309
- ___Block_byref_object_dispose_.26660
- ___Block_byref_object_dispose_.27095
- ___Block_byref_object_dispose_.28498
- ___Block_byref_object_dispose_.29062
- ___Block_byref_object_dispose_.3209
- ___Block_byref_object_dispose_.33907
- ___Block_byref_object_dispose_.34379
- ___Block_byref_object_dispose_.34796
- ___Block_byref_object_dispose_.35155
- ___Block_byref_object_dispose_.3974
- ___Block_byref_object_dispose_.4147
- ___Block_byref_object_dispose_.5095
- ___Block_byref_object_dispose_.6942
- ___Block_byref_object_dispose_.7754
- ___Block_byref_object_dispose_.9844
- ___Block_byref_object_dispose_.9911
- ___block_descriptor_41_e8_32bs_e43_v24?0"MPRemotePlaybackQueue"8"NSError"16ls32l8
- ___block_literal_global.10411
- ___block_literal_global.10571
- ___block_literal_global.10705
- ___block_literal_global.10998
- ___block_literal_global.11.14053
- ___block_literal_global.110.21110
- ___block_literal_global.11289
- ___block_literal_global.11619
- ___block_literal_global.11803
- ___block_literal_global.11942
- ___block_literal_global.121.24470
- ___block_literal_global.12152
- ___block_literal_global.1277
- ___block_literal_global.12904
- ___block_literal_global.136
- ___block_literal_global.13718
- ___block_literal_global.14.21235
- ___block_literal_global.14067
- ___block_literal_global.143.24482
- ___block_literal_global.146.24478
- ___block_literal_global.14790
- ___block_literal_global.153.16885
- ___block_literal_global.158
- ___block_literal_global.160.19569
- ___block_literal_global.16195
- ___block_literal_global.16310
- ___block_literal_global.167.10677
- ___block_literal_global.17110
- ___block_literal_global.17239
- ___block_literal_global.17280
- ___block_literal_global.17352
- ___block_literal_global.17803
- ___block_literal_global.17973
- ___block_literal_global.19018
- ___block_literal_global.19698
- ___block_literal_global.19772
- ___block_literal_global.199.23085
- ___block_literal_global.204
- ___block_literal_global.20712
- ___block_literal_global.21234
- ___block_literal_global.21536
- ___block_literal_global.2155
- ___block_literal_global.21886
- ___block_literal_global.22172
- ___block_literal_global.23184
- ___block_literal_global.2415
- ___block_literal_global.24508
- ___block_literal_global.25498
- ___block_literal_global.26545
- ___block_literal_global.27083
- ___block_literal_global.27717
- ___block_literal_global.278
- ___block_literal_global.282.26320
- ___block_literal_global.283
- ___block_literal_global.28931
- ___block_literal_global.29682
- ___block_literal_global.30.19699
- ___block_literal_global.30304
- ___block_literal_global.322.12692
- ___block_literal_global.34417
- ___block_literal_global.34825
- ___block_literal_global.3491
- ___block_literal_global.37.21850
- ___block_literal_global.4046
- ___block_literal_global.4472
- ___block_literal_global.45.29669
- ___block_literal_global.47.24494
- ___block_literal_global.4793
- ___block_literal_global.5295
- ___block_literal_global.547.20262
- ___block_literal_global.640
- ___block_literal_global.6519
- ___block_literal_global.659
- ___block_literal_global.705
- ___block_literal_global.7220
- ___block_literal_global.729
- ___block_literal_global.733
- ___block_literal_global.738
- ___block_literal_global.7452
- ___block_literal_global.7760
- ___block_literal_global.9.21855
- ___block_literal_global.964
- ___block_literal_global.9988
- ___swift_allocate_boxed_opaque_existential_1Tm
- ___swift_memcpy5_1
- _associated conformance 17MediaPlaybackCore11MPCTimelineO10LoadReasonOSHAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO13TimelineErrorO15SonicFoundation0gF4CodeAA8RawValueSY_s17FixedWidthInteger
- _associated conformance 17MediaPlaybackCore11MPCTimelineO13TimelineErrorO15SonicFoundation0gF4CodeAASY
- _associated conformance 17MediaPlaybackCore11MPCTimelineO13TimelineErrorOSHAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO15ItemChangeEventV0F0OSHAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO15PreemptedReasonOSHAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemVAC0gH0AA08RenderedH0AcHP_AC0giH0
- _associated conformance 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemVAC0gH0AA8MetadataAcHP_AC0ghI0
- _associated conformance 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemVSHAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineCAC0G0AA4ItemAcFP_AC0gH0
- _associated conformance 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsVs10SetAlgebraAASQ
- _associated conformance 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
- _associated conformance 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsVs9OptionSetAASY
- _associated conformance 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsVs9OptionSetAAs0H7Algebra
- _associated conformance 17MediaPlaybackCore11MPCTimelineO22RendererImplementationCy_xGAC0E0AA8TimelineAcGP_AC0gF0
- _associated conformance 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC0fG5Error015_53EB48984A90F4K16B231E632570AC9B7LLO15SonicFoundation0pH4CodeAA8RawValueSY_s17FixedWidthInteger
- _associated conformance 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC0fG5Error015_53EB48984A90F4K16B231E632570AC9B7LLO15SonicFoundation0pH4CodeAASY
- _associated conformance 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC0fG5Error015_53EB48984A90F4K16B231E632570AC9B7LLOSHAASQ
- _block_copy_helper.101
- _block_copy_helper.102
- _block_copy_helper.104
- _block_copy_helper.108
- _block_copy_helper.110
- _block_copy_helper.113
- _block_copy_helper.122
- _block_copy_helper.134
- _block_copy_helper.138
- _block_copy_helper.141
- _block_copy_helper.155
- _block_copy_helper.162
- _block_copy_helper.165
- _block_copy_helper.170
- _block_copy_helper.40
- _block_copy_helper.50
- _block_copy_helper.65
- _block_copy_helper.69
- _block_copy_helper.71
- _block_copy_helper.74
- _block_copy_helper.75
- _block_copy_helper.83
- _block_copy_helper.86
- _block_copy_helper.92
- _block_copy_helper.95
- _block_descriptor.103
- _block_descriptor.104
- _block_descriptor.106
- _block_descriptor.110
- _block_descriptor.112
- _block_descriptor.115
- _block_descriptor.124
- _block_descriptor.136
- _block_descriptor.140
- _block_descriptor.143
- _block_descriptor.157
- _block_descriptor.164
- _block_descriptor.167
- _block_descriptor.172
- _block_descriptor.42
- _block_descriptor.52
- _block_descriptor.67
- _block_descriptor.71
- _block_descriptor.73
- _block_descriptor.76
- _block_descriptor.77
- _block_descriptor.85
- _block_descriptor.88
- _block_descriptor.94
- _block_descriptor.97
- _block_destroy_helper.102
- _block_destroy_helper.103
- _block_destroy_helper.105
- _block_destroy_helper.109
- _block_destroy_helper.111
- _block_destroy_helper.114
- _block_destroy_helper.123
- _block_destroy_helper.135
- _block_destroy_helper.139
- _block_destroy_helper.142
- _block_destroy_helper.156
- _block_destroy_helper.163
- _block_destroy_helper.166
- _block_destroy_helper.171
- _block_destroy_helper.41
- _block_destroy_helper.51
- _block_destroy_helper.66
- _block_destroy_helper.70
- _block_destroy_helper.72
- _block_destroy_helper.75
- _block_destroy_helper.76
- _block_destroy_helper.84
- _block_destroy_helper.87
- _block_destroy_helper.93
- _block_destroy_helper.96
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC0E4StepO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC13RunnableStateO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC16SuspensionReasonO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO11TargetEventO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO15PlayerSyncEventV0F6ReasonO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV08RenderedH0VSg
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO19ItemErrorResolutionO
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO19ItemErrorResolutionOSg
- _get_enum_tag_for_layout_string 17MediaPlaybackCore11MPCTimelineO21SessionMigrationEventV0G0O
- _get_enum_tag_for_layout_string s6ResultOySbs5Error_pG
- _get_type_metadata 17MediaPlaybackCore11MPCTimelineO11ChangeEventRzl15Synchronization5MutexVySDy10Foundation4UUIDVScS12ContinuationVy7PayloadQz_GGG.1
- _kMXSessionProperty_HostProcessAttribution
- _kMXSession_HostProcessAttributionKey_AuditToken
- _kMXSession_HostProcessAttributionKey_BundleID
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$remoteHostProcessAuditToken
- _objc_msgSend$setAudioSessionMXProperties:
- _objc_msgSend$setResolvedPlayerPath:
- _object_getClass
- _objectdestroy.168Tm
- _objectdestroy.223Tm
- _objectdestroy.276Tm
- _objectdestroy.48Tm
- _objectdestroy.52Tm
- _objectdestroy.57Tm
- _objectdestroy.67Tm
- _objectdestroy.84Tm
- _objectdestroy.85Tm
- _sharedManager.onceToken.34416
- _swift_dynamicCastObjCProtocolUnconditional
- _symbolic $s17MediaPlaybackCore11MPCTimelineO11ChangeEventP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO11EventStreamP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO12TimelineItemP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC15ContentProviderP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO16RenderDataSourceP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO20TimelineItemMetadataP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO20TimelineRenderedItemP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO21RenderTaskCoordinatorP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO22TimelineImplementationP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO8RendererP
- _symbolic $s17MediaPlaybackCore11MPCTimelineO8TimelineP
- _symbolic 12RenderedItem_____Qz 17MediaPlaybackCore11MPCTimelineO12TimelineItemP
- _symbolic 4Item_____Qz 17MediaPlaybackCore11MPCTimelineO8TimelineP
- _symbolic 8Metadata_____Qz 17MediaPlaybackCore11MPCTimelineO12TimelineItemP
- _symbolic 8Timeline_____Qz 17MediaPlaybackCore11MPCTimelineO8RendererP
- _symbolic SDySS_____G 17MediaPlaybackCore11MPCTimelineO10RenderTaskC
- _symbolic SDySS_____G 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV
- _symbolic SDy__________G 10Foundation4UUIDV 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC23TargetEventContinuation33_4A967C9508C5257B5F66FE833F259B52LLC
- _symbolic SS6itemID_Sd4timetSg
- _symbolic SS6itemID______6changet 17MediaPlaybackCore11MPCTimelineO15ItemChangeEventV0F0O
- _symbolic SS8actionID_Sf10targetRatet
- _symbolic SSSg6itemID_t
- _symbolic SaySSG7itemIDs_Sb18resetPlaybackStatet
- _symbolic SayScTyyt_____GG s5NeverO
- _symbolic ScCy______p_So12AVPlayerItemCt______pG 17MediaPlaybackCore15QueuePlayerItemP s5ErrorP
- _symbolic ScTyyt_____GSg s5NeverO
- _symbolic Sccyyt______pG12continuation______6reasont s5ErrorP 17MediaPlaybackCore11MPCTimelineO10RenderTaskC16SuspensionReasonO
- _symbolic Sccyyt______pGSg s5ErrorP
- _symbolic So10NSProgressC
- _symbolic So27AVPlayerPlaybackCoordinatorCSg
- _symbolic So28MPCPlaybackEngineEventStreamCSgXw
- _symbolic _____ 10Foundation4UUIDV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO0A25ServicesAvailabilityEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO10LoadReasonO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO10RenderTaskC
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO10RenderTaskC0E4StepO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO10RenderTaskC13RunnableStateO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO10RenderTaskC16SuspensionReasonO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO11PausedEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO11TargetEventO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO13RendererStateO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO13TimelineErrorO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO15ItemChangeEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO15ItemChangeEventV0F0O
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO15PlayerSyncEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO15PlayerSyncEventV0F6ReasonO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO15PreemptedReasonO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC23TargetEventContinuation33_4A967C9508C5257B5F66FE833F259B52LLC
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV08RenderedH0V
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC9loadAsset6itemID6reasonySS_AC10LoadReasonOtYaKF0mI4TaskL_C
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO17LeaseRequestEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO19ItemErrorResolutionO
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO20UnresolvedErrorEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO21SessionMigrationEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO21SessionMigrationEventV0G0O
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO22RendererImplementationC
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO25PrebufferItemsChangeEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO26NowPlayingItemsChangeEventV
- _symbolic _____ 17MediaPlaybackCore11MPCTimelineO9PlayEventV
- _symbolic _____ 17MediaPlaybackCore26MPCTimelineQueueTranslatorC
- _symbolic _____ 17MediaPlaybackCore28TimelineAssetQueueControllerC
- _symbolic _____ 17MediaPlaybackCore28TimelineAssetQueueControllerC8FadeTypeO
- _symbolic _____ 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC
- _symbolic _____ 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC0fG5Error015_53EB48984A90F4K16B231E632570AC9B7LLO
- _symbolic _____11preventions_t 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsV
- _symbolic _____6reason_SS2byt 17MediaPlaybackCore11MPCTimelineO15PreemptedReasonO
- _symbolic _____Sg 17MediaPlaybackCore0B12BehaviorTypeO
- _symbolic _____Sg 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV08RenderedH0V
- _symbolic _____Sg 17MediaPlaybackCore11MPCTimelineO19ItemErrorResolutionO
- _symbolic _____Sg 17MediaPlaybackCore26MPCTimelineQueueTranslatorC
- _symbolic _____Sg 17MediaPlaybackCore32MPCPlaybackEngineContentProviderC
- _symbolic _____Sg 18PodcastsFoundation23AnalyticsUserIdentifierC
- _symbolic _____SgXw 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC
- _symbolic _____SgXw 17MediaPlaybackCore28TimelineAssetQueueControllerC
- _symbolic _____SgXwz_Xx 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC
- _symbolic _____SgXwz_Xx 17MediaPlaybackCore28TimelineAssetQueueControllerC
- _symbolic ______pSg 17MediaPlaybackCore11MPCTimelineO8RendererP
- _symbolic ______pSg 17MediaPlaybackCore11MPCTimelineO8TimelineP
- _symbolic ______pSg 17MediaPlaybackCore12AssetLoadingP
- _symbolic ______pSg 17MediaPlaybackCore15ErrorControllerP
- _symbolic ______pSg5error_t s5ErrorP
- _symbolic ______pSgXw 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC15ContentProviderP
- _symbolic ______pSgXw 17MediaPlaybackCore11MPCTimelineO21RenderTaskCoordinatorP
- _symbolic _____ySb______pG6result_t s6ResultOsRi_zRi0_zrlE s5ErrorP
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC010PlayerSyncF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC012LeaseRequestF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC014PrebufferItemseF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015NowPlayingItemseF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015UnresolvedErrorF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC016SessionMigrationF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04ItemeF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04PlayF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC06PausedF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC0a20ServicesAvailabilityF0V
- _symbolic _____y______G 17MediaPlaybackCore11MPCTimelineO22RendererImplementationC AC16InMemoryTimelineC
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC010PlayerSyncF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC012LeaseRequestF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC014PrebufferItemseF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015NowPlayingItemseF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015UnresolvedErrorF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC016SessionMigrationF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04ItemeF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04PlayF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC06PausedF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC0a20ServicesAvailabilityF0V
- _symbolic _____y______GSgXw 17MediaPlaybackCore11MPCTimelineO22RendererImplementationC AC16InMemoryTimelineC
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC010PlayerSyncF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC012LeaseRequestF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC014PrebufferItemseF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015NowPlayingItemseF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC015UnresolvedErrorF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC016SessionMigrationF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04ItemeF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC04PlayF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC06PausedF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO20ChangeEventPublisherC AC0a20ServicesAvailabilityF0V AC0eF0P
- _symbolic _____y_xGSgXwz____________RzlXX 17MediaPlaybackCore11MPCTimelineO22RendererImplementationC AC16InMemoryTimelineC AC0iF0P
- _symbolic yXlSg
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC0E4StepO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC13RunnableStateO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO10RenderTaskC16SuspensionReasonO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO11TargetEventO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO15PlayerSyncEventV0F6ReasonO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO16InMemoryTimelineC4ItemV08RenderedH0V
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO17RenderPreventionsV
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO19ItemErrorResolutionO
- _type_layout_string 17MediaPlaybackCore11MPCTimelineO21SessionMigrationEventV0G0O
CStrings:
+ ", currentQueueControllerItem: "
+ ", targetContentItemID: "
+ "@\"NSDictionary\"40@0:8@\"NSDictionary\"16@\"NSIndexPath\"24@\"MPMiddlewareChain\"32"
+ "Aborting restoration of overlapped outgoing item: "
+ "B20@0:8I16"
+ "CurrentTimeStampHang2"
+ "Debug: \nEvent=%s\nMetadata=%{private,mask.hash}s"
+ "EnhanceDialogueSession: Error getting enhance dialogue level: %@"
+ "EnhanceDialogueSession: Error restoring previous enhance dialogue level: %@"
+ "EnhanceDialogueSession: Error setting enhance dialogue active: %@ for item: %{private,mask.hash}s"
+ "EnhanceDialogueSession: Restoring enhance dialogue level: %s"
+ "EnhanceDialogueSession: Snapshotting enhance dialogue level for restoration later: %s"
+ "EnhanceDialogueSession: Unexpected enhance dialogue level: %s."
+ "PlaybackStackController setup failed"
+ "Podcasts: Unable to create a play event.\nEventType: %{private}s.\nItemID: %{private}s.\nSectionID: %{private}s."
+ "Podcasts: Unable to lookup value for key %{private,mask.hash}s. No related `itemBegin` event found."
+ "PodcastsPlayActivityFeedConsumer.WorkQueue"
+ "Reporting: %{private,mask.hash}s\nEVS: %{private,mask.hash}s\nItemID: %{private,mask.hash}@\nSectionID: %{private,mask.hash}@\nData: %{private,mask.hash}s"
+ "SEED"
+ "SupportsSmartTransitionsOverride"
+ "SupportsTransitionsOverride"
+ "T@\"MPCPlayerPath\",R,N,V_resolvedPlayerPath"
+ "T@\"NSDictionary\",R,C,N,V_transitionInfo"
+ "Unable to fetch user identifiers."
+ "Unable to fetch user identifiers. Account retrieval failed: %s."
+ "[%{private,mask.hash}s] Attempting to emit an event %s without an event stream."
+ "[%{public}@]-MPCPlaybackEngineImplementation: %p - Deferring %{public}@ waiting for Media Services availability"
+ "[%{public}@]-MPCPlaybackEngineImplementation: %p - Flushing %ld deferred blocks that waited for Media Services availability"
+ "[ALC:%{public}s] - Cannot update transition info - missing timing information"
+ "[ALC:%{public}s] - Cannot update transition info - outgoing item is not MPAVItem"
+ "[ALC:%{public}s] - Fetching Smart Transition info. OutgoingItemInfo: %{public}s.  IncomingItemInfo: %{public}s"
+ "[ALC:%{public}s] - Updated outgoing item content with transition info - startTime: %{public}f, pivotTime: %{public}f, transitionProvided: %{public}ld"
+ "[AP] - MPCProcessAudioTap %p - MediaServicesWereLost - clearing AQ"
+ "[AP] - MPCProcessAudioTap %p - MediaServicesWereReset - creating AQ"
+ "[AP] - MPCProcessAudioTap %p - Stopped processing audio queue [MediaServicesWereLost]"
+ "[AP] - MPCProcessAudioTap %p - Stopped processing audio queue [MediaServicesWereLost] error=%{public}@"
+ "[EST:%{public}s)] setting item expectedStartTime=%fs due to setRate with timeContinuity, at %fs from now"
+ "[FAF:%{public}s]: Updated start time to %fs because effective rate was changed at a later time than %fs"
+ "[TSN: %s] Cleared all transition info from content item"
+ "[TSN: %s] Cleared planned transition info from content item"
+ "[TSN: %s] Updated content item with transition info - startTime: %{public}f, pivotTime: %{public}f, style: %{public}ld, debugString: %s"
+ "_commandRequiresMediaServices:"
+ "_initWithResolvedPlayerPath:"
+ "_mediaServicesWaitingBlocks"
+ "_transitionInfo"
+ "_userToggledTransitionsInDowngradeState"
+ "begin media services death"
+ "clearAllContentItemTransitionInfo"
+ "clearPlannedContentItemTransitionInfo"
+ "com.apple.podcasts"
+ "end media services death"
+ "identifierForKey:"
+ "initWithBundleIdentifier:"
+ "initWithKey:ascending:"
+ "keyWithName:crossDeviceSync:"
+ "mediaServicesAvailable"
+ "performWhenMediaServicesAreAvailable:identifier:"
+ "playerItemTransitionInfo:atIndexPath:chain:"
+ "previousEnhanceDialogueLevel"
+ "resolvedTransitionStyle"
+ "setResetInterval:"
+ "setSortUsingAllowedItemIdentifiers:"
+ "setValue:forKey:"
+ "shouldDowngradeTransitionStyle"
+ "transitionInfo"
+ "updateContentItemWithPlannedTransitionStartTime:pivotTime:transitionProvided:debugString:"
+ "v32@0:8@?16@24"
+ "v36@0:8@\"<MPCVideoOutput>\"16B24@\"<AVPlayerViewControllerAnimationCoordinator>\"28"
+ "v48@0:8d16d24q32@40"
+ "videoOutput:willTransitionToVisibilityOfTransportBar:withAnimationCoordinator:"
+ "workQueue"
+ "\xf1"
- " found but player is not playing"
- " has been removed"
- " is unloaded and rendering is prevented"
- " not synchronized to the player [reloadingWithFadeout]"
- " silently to queue end"
- ", resetPlaybackState:"
- "CurrentTimeStampHang"
- "Error getting enhance dialogue level: %@"
- "Error resolution - Resolved ["
- "Error setting enhance dialogue active: %@ for item: %{private,mask.hash}s"
- "Failed to resolve queue item for "
- "HasLoadedAllItems"
- "ImmediateCrossfade"
- "LeaseRequestEvent"
- "LeaseRequestEvent("
- "MediaPlaybackCore/TimelineAssetQueueController.swift"
- "MediaServicesAvailabilityEvent"
- "MediaServicesAvailabilityEvent("
- "No longer supported, use timeline instead"
- "No queue controller found while attempting to load item for "
- "NowPlayingItemsChangeEvent"
- "NowPlayingItemsChangeEvent(items:"
- "PausedEvent(reason:"
- "Playback paused by action: "
- "Playback paused with reason: "
- "Podcasts: Not reporting `contentGUID`. No related `itemBegin` event found."
- "Podcasts: Not reporting `contentLength`. No related `itemEvent` event found."
- "Podcasts: Not reporting `feedURL`. No related `itemBegin` event found."
- "Podcasts: Not reporting `id`. No related `itemBegin` event found."
- "Podcasts: Not reporting `itemType`. No related `itemBegin` event found."
- "Podcasts: Not reporting `mediaType`. No related `itemBegin` event found."
- "Podcasts: Not reporting `musicSubscriptionInformation`. No related `itemBegin` event found."
- "Podcasts: Not reporting `newsSubscriptionInformation`. No related `itemBegin` event found."
- "Podcasts: Not reporting `playContext`. No related `itemBegin` event found."
- "Podcasts: Not reporting `playbackSettingsScope`. No related `itemBegin` event found."
- "Podcasts: Not reporting `podcastID`. No related `itemBegin` event found."
- "Podcasts: Not reporting `priceType`. No related `itemBegin` event found."
- "Podcasts: Not reporting `state`. No related `itemBegin` event found."
- "Podcasts: Reporting `/play` for event type: %{public}s."
- "Podcasts: Unable to create a play event.\nEventType: %{public}s.\nItemID: %{public}s.\nSectionID: %{public}s."
- "Podcasts: Unable to query `contentLength`. No metadata found."
- "Podcasts: Unable to query `enhanceDialogue`. No data found."
- "Podcasts: Unable to query `itemPositionJumpIsUserInitiated`. No data found."
- "Podcasts: Unable to query `musicSubscriptionInformation`. No metadata found."
- "Podcasts: Unable to query `newsSubscriptionInformation`. No metadata found."
- "Podcasts: Unable to query `playbackSettingsScope`. No metadata found."
- "Podcasts: Unable to query `podcastContentGUID`. No metadata found."
- "Podcasts: Unable to query `podcastFeedURL`. No metadata found."
- "Podcasts: Unable to query `podcastID`. No `itemIdentifiers` data found."
- "Podcasts: Unable to query `podcastID`. No `universalStore` data found."
- "Podcasts: Unable to query `podcastItemType`. No metadata found."
- "Podcasts: Unable to query `podcastMediaType`. No metadata found."
- "Podcasts: Unable to query `podcastPageContext`. No metadata found."
- "Podcasts: Unable to query `podcastPriceType`. No metadata found."
- "Podcasts: Unable to query `podcastStoreID`. No metadata found."
- "Podcasts: Unable to query `podcastSubscriptionState`. No metadata found."
- "Podcasts: Unable to report `userId` or `clientId` for event type: %s with error %s."
- "PrebufferItemsChangeEvent"
- "PrebufferItemsChangeEvent(items:"
- "Resource reclamation occurred"
- "SessionMigrationEvent"
- "SetQueue %s completed without a start item [empty queue]"
- "SetQueue %s completed without waiting for ready to play status"
- "Skipping to next item "
- "T@\"AVPlayerPlaybackCoordinator\",N,&,VplaybackCoordinator"
- "T@\"MPCPlayerPath\",&,N,V_resolvedPlayerPath"
- "TVA: ChangeEvent: publishing %s to %ld subscribers"
- "TVA: ChangeEvent: started monitoring %s"
- "TVA: Commit: beginSessionMigration:%s"
- "TVA: Commit: didRequestLease:%{bool}d"
- "TVA: Commit: endSessionMigration:%s error:%s"
- "TVA: Commit: interruptionWasNonresumable:%s"
- "TVA: Commit: item:%s can't retry twice, forcing %s"
- "TVA: Commit: item:%s didFail:%@"
- "TVA: Commit: item:%s does not have renderedItem to update isConfigured"
- "TVA: Commit: item:%s effectiveRate:%f"
- "TVA: Commit: item:%s errorResolution:%s"
- "TVA: Commit: item:%s isConfigured:%{bool}d"
- "TVA: Commit: item:%s isCurrent:%{bool}d"
- "TVA: Commit: item:%s isFullyDownloaded:%{bool}d"
- "TVA: Commit: item:%s isReadyToPlay:%{bool}d"
- "TVA: Commit: item:%s metadata load failed:%@"
- "TVA: Commit: item:%s metadata loaded:%@"
- "TVA: Commit: item:%s metadata removed"
- "TVA: Commit: item:%s not found to update errorResolution"
- "TVA: Commit: item:%s not found to update isConfigured"
- "TVA: Commit: item:%s not found to update isCurrent"
- "TVA: Commit: item:%s not found to update metadata"
- "TVA: Commit: item:%s not found to update renderedItem"
- "TVA: Commit: item:%s overlappedPlaybackDidBegin"
- "TVA: Commit: item:%s overlappedPlaybackDidEnd"
- "TVA: Commit: item:%s renderedItem failed:%@"
- "TVA: Commit: item:%s renderedItem loaded:%s"
- "TVA: Commit: item:%s renderedItem removed"
- "TVA: Commit: mediaServicesAreAvailable:%{bool}d"
- "TVA: Commit: nowPlayingItems: %s targetItem: %s resetPlaybackState: %{bool}d"
- "TVA: Commit: nowPlayingItems: %s targetItem: %s resetPlaybackState: %{bool}d - No changes"
- "TVA: Commit: pausedForReason:%s"
- "TVA: Commit: playerRate:%f"
- "TVA: Commit: prebufferItems:%s"
- "TVA: Commit: prebufferItems:%s - No changes"
- "TVA: Commit: unloadItems:%s pauseRendering:%{bool}d"
- "TVA: Commit: unresolvedErrorOccurred:%@ shouldUnloadItems:%{bool}d"
- "TVA: Commit: willPlayWithActionID:%s targetRate:%f"
- "TVA: Commit: willPlayWithActionID:%s targetRate:%f - Duplicated"
- "TVA: ItemCache: remove item:%s"
- "TVA: ItemTime: preseved for itemID:%s time:%f added offset:%f"
- "TVA: ItemTime: restored for itemID:%s time:%f"
- "TVA: RenderDataSource: item %s has no asset to configure"
- "TVA: RenderDataSource: item %s has no asset to load asset values"
- "TVA: RenderDataSource: item %s nolonger available to configure"
- "TVA: RenderDataSource: item %s nolonger available to load"
- "TVA: RenderDataSource: item %s nolonger available to load asset"
- "TVA: RenderDataSource: item %s nolonger available to load asset values"
- "TVA: RenderDataSource: item %s nolonger available to load metadata"
- "TVA: RenderDataSource: item %s nolonger available to render"
- "TVA: RenderDataSource: item %s nolonger available to resolve error"
- "TVA: RenderDataSource: loaded asset:%@ for:%s"
- "TVA: RenderDataSource: loaded metadata:%@ for:%s"
- "TVA: RenderDataSource: loading asset for:%s reason:%s"
- "TVA: RenderDataSource: loading metadata for:%s replacing:%s reason:%s"
- "TVA: RenderDataSource: reuse asset:%@ for:%s"
- "TVA: RenderTask: %s cancelled"
- "TVA: RenderTask: %s cancelled: %@"
- "TVA: RenderTask: %s resume with error: %@"
- "TVA: RenderTask: %s resumed with reason: %s"
- "TVA: RenderTask: %s starting the next step: %s"
- "TVA: RenderTask: %s suspended with reason: %s"
- "TVA: Renderer: Now Playing: %s"
- "TVA: Renderer: Prebuffered: %s"
- "TVA: Renderer: not creating task for duplicated item:%s because it appeared earlier or is outgoing"
- "TVA: Renderer: state: %s"
- "TVA: Renderer: task restarting for item:%s [clearErrors]"
- "TVA: Renderer: task restarting for item:%s [reborn]"
- "TVA: Renderer: task restarting for item:%s [reload]"
- "TVA: Renderer: task restarting for item:%s [resetPlaybackState]"
- "TVA: Renderer: task restarting for item:%s [retry]"
- "TVA: Renderer: task resuming for item:%s [%s]"
- "TVA: Renderer: task resuming for item:%s [prebuffer]"
- "TVA: Renderer: task starting for item:%s [nowPlaying]"
- "TVA: Renderer: task starting for item:%s [prebuffer]"
- "TVA: Renderer: updating tasks nowPlayingItemIDs:%s prebufferItemIDs:%s clearErrors:%{bool}d resumeReason:%s"
- "TVA: TargetEvent: Failed: %s error:%@"
- "TVA: TargetEvent: Started monitoring: %s"
- "TVA: TargetEvent: Triggered immediately: %s"
- "TVA: TargetEvent: Triggered: %s"
- "TVA: synchronizeToPlayer currentItem:%s target:%s renderedItem:%s hasLoadedAllItems:%{bool}d)"
- "Unexpected enhance dialogue level: %s."
- "UnresolvedErrorEvent"
- "Waiting for next item "
- "[ALC:%{public}s] - Fetching Smart Transition info. OutgoingItemInfo: %s.  IncomingItemInfo: %s"
- "[AP] - MPCProcessAudioTap %p - Stopping processing audio queue [mediaserverd death]"
- "[AP] - MPCProcessAudioTap %p - Stopping processing audio queue [mediaserverd death] error=%{public}@"
- "[AP] - MPCProcessAudioTap %p - mediaserverd died - clearing AQ"
- "[AP] - MPCProcessAudioTap %p - mediaserverd restarted - creating AQ"
- "[BMSP:%s:%s] updatePlayerPlaybackCoordinator:… | updating playback coordinator [engine update] playbackCoordinator=%@"
- "[EST:%{public}s)] setting expected start time due to setRate with timeContinuity"
- "[FAF:%{public}s]: Firing off firstFrame event for currentItem"
- "_TtC17MediaPlaybackCore26MPCTimelineQueueTranslator"
- "_TtC17MediaPlaybackCore28TimelineAssetQueueController"
- "_TtC17MediaPlaybackCore32MPCPlaybackEngineContentProvider"
- "_TtCCO17MediaPlaybackCore11MPCTimeline16InMemoryTimelineP33_4A967C9508C5257B5F66FE833F259B5223TargetEventContinuation"
- "_TtCFCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline9loadAssetFzZT6itemIDSS6reasonOS0_10LoadReason_T_L_13LoadAssetTask"
- "_TtCO17MediaPlaybackCore11MPCTimeline10RenderTask"
- "_TtCO17MediaPlaybackCore11MPCTimeline16InMemoryTimeline"
- "_mediaServerAvailable"
- "actionID targetRate "
- "assetValuesLoading"
- "awaitingPlayAction"
- "begin mediaserverd death"
- "com.apple.sonic.asset.loadBegin"
- "com.apple.sonic.asset.loadBegin?contentItemID="
- "com.apple.sonic.asset.loadEnd"
- "com.apple.sonic.asset.loadEnd?contentItemID="
- "configurationChanged"
- "contentProvider"
- "coordinator"
- "dataWithBytes:length:"
- "end mediaserverd death"
- "enhanceDialogState"
- "itemChangeEventPublisher"
- "itemConfiguration"
- "itemDidStartPlaying"
- "itemID change "
- "itemIDs resetPlaybackState "
- "itemIsReadyToPlay"
- "itemIsRenderedAndConfigured"
- "itemTasks"
- "lastPlayActionID"
- "leaseRequestEventPublisher"
- "loadAssetValues(for:isCurrent:behavior:)"
- "mediaServicesAreAvailable"
- "mediaServicesAvailabilityEventPublisher"
- "mediaserverd not available to perform command"
- "nowPlayingItemIDs"
- "nowPlayingItemsChangePublisher"
- "nowPlayingItemsChanged"
- "outgoingItemID"
- "pausedEventPublisher"
- "playEventPublisher"
- "playbackEngineContentProvider"
- "playbackStateReset"
- "playerCurrentItemID"
- "playerRate"
- "playerSyncEventPublisher"
- "prebufferItemIDs"
- "prebufferItemsChangePublisher"
- "prebufferItemsChanged"
- "progress"
- "renderer"
- "rendererState"
- "rendererStateChanged"
- "restorableTimeSnapshot"
- "runnableState"
- "sessionMigrationEventPublisher"
- "setPlaybackCoordinator:"
- "setResolvedPlayerPath:"
- "step"
- "subscriptions"
- "targetEventContinuations"
- "targetItemID"
- "timeline"
- "timelineMonitors"
- "timelineQueueTranslator"
- "unresolvedErrorEventPublisher"
- "v24@?0@\"_TtC18PodcastsFoundation23AnalyticsUserIdentifier\"8@\"NSError\"16"
- "\xe1"
- "❕-[_MPCMediaRemotePublisher _performCommandEvent:completion:]: mediaserverd unavailable [allowing command] type=%{public}@ id=%{public}@ interface=%{public}@"
- "❕-[_MPCMediaRemotePublisher _performCommandEvent:completion:]: mediaserverd unavailable [failing command] type=%{public}@ id=%{public}@ interface=%{public}@"

```
