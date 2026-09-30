## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-25115.25.29.101.0
-  __TEXT.__text: 0x3dc9ac
-  __TEXT.__auth_stubs: 0x57f0
-  __TEXT.__objc_methlist: 0x16f88
+25100.25.30.502.0
+  __TEXT.__text: 0x3e5a8c
+  __TEXT.__auth_stubs: 0x58e0
+  __TEXT.__objc_methlist: 0x17000
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x15860
-  __TEXT.__cstring: 0x2f281
-  __TEXT.__constg_swiftt: 0x7418
-  __TEXT.__swift5_typeref: 0x4f4c
-  __TEXT.__swift5_reflstr: 0x4e82
-  __TEXT.__swift5_fieldmd: 0x4b1c
-  __TEXT.__swift5_builtin: 0x744
-  __TEXT.__swift5_assocty: 0xf18
-  __TEXT.__swift5_capture: 0x32c4
-  __TEXT.__oslogstring: 0x3ab40
-  __TEXT.__swift5_mpenum: 0xfc
-  __TEXT.__swift5_proto: 0x9b8
-  __TEXT.__swift5_types: 0x528
-  __TEXT.__swift_as_entry: 0x3a8
-  __TEXT.__swift_as_ret: 0x4b0
+  __TEXT.__const: 0x15aa0
+  __TEXT.__cstring: 0x2f639
+  __TEXT.__constg_swiftt: 0x7538
+  __TEXT.__swift5_typeref: 0x5012
+  __TEXT.__swift5_reflstr: 0x4f22
+  __TEXT.__swift5_fieldmd: 0x4c1c
+  __TEXT.__swift5_builtin: 0x758
+  __TEXT.__swift5_assocty: 0xf38
+  __TEXT.__swift5_capture: 0x3364
+  __TEXT.__oslogstring: 0x3bdb9
+  __TEXT.__swift5_mpenum: 0x104
+  __TEXT.__swift5_proto: 0x9c8
+  __TEXT.__swift5_types: 0x538
+  __TEXT.__swift_as_entry: 0x3b8
+  __TEXT.__swift_as_ret: 0x4bc
   __TEXT.__swift5_protos: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x6978
+  __TEXT.__gcc_except_tab: 0x6988
   __TEXT.__ustring: 0x4b4
-  __TEXT.__unwind_info: 0xc450
-  __TEXT.__eh_frame: 0xc8f8
+  __TEXT.__unwind_info: 0xc0c0
+  __TEXT.__eh_frame: 0xc9e0
   __TEXT.__objc_classname: 0x3d25
-  __TEXT.__objc_methname: 0x38931
-  __TEXT.__objc_methtype: 0x9967
-  __TEXT.__objc_stubs: 0x26680
-  __DATA_CONST.__got: 0x2e68
-  __DATA_CONST.__const: 0x9050
+  __TEXT.__objc_methname: 0x38aed
+  __TEXT.__objc_methtype: 0x9978
+  __TEXT.__objc_stubs: 0x26720
+  __DATA_CONST.__got: 0x2e88
+  __DATA_CONST.__const: 0x90f0
   __DATA_CONST.__objc_classlist: 0xcc8
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc1f0
+  __DATA_CONST.__objc_selrefs: 0xc230
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x270
-  __AUTH_CONST.__auth_got: 0x2c08
-  __AUTH_CONST.__const: 0xf5e0
-  __AUTH_CONST.__cfstring: 0x1d300
-  __AUTH_CONST.__objc_const: 0x32690
-  __AUTH_CONST.__objc_intobj: 0x7c8
+  __AUTH_CONST.__auth_got: 0x2c80
+  __AUTH_CONST.__const: 0xfaa0
+  __AUTH_CONST.__cfstring: 0x1d3c0
+  __AUTH_CONST.__objc_const: 0x32820
+  __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x4d10
   __AUTH.__data: 0x3250
   __DATA.__objc_ivar: 0x19c8
-  __DATA.__data: 0x7088
-  __DATA.__bss: 0xffd0
+  __DATA.__data: 0x7158
+  __DATA.__bss: 0x101d0
   __DATA.__common: 0x1d8
-  __DATA_DIRTY.__objc_data: 0x3918
-  __DATA_DIRTY.__data: 0x46f0
+  __DATA_DIRTY.__objc_data: 0x3930
+  __DATA_DIRTY.__data: 0x4720
   __DATA_DIRTY.__bss: 0x13b0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22CA9337-EC4D-3ADF-92A5-06D6C287B384
-  Functions: 19592
-  Symbols:   38185
-  CStrings:  22388
+  UUID: C12597AB-2248-3C45-AAD9-A767EE4E49EC
+  Functions: 19683
+  Symbols:   38272
+  CStrings:  22462
 
Symbols:
+ +[MPCPlayPerfMetrics metricsWithTransitionWillStartEvent:cursor:queueItem:]
+ -[MPAVItem(MFQueuePlayerItem) prepareForReuseWithSeekToStartTime:]
+ -[MPCModelStorePlaybackItemsRequest adjustedStartItemIdentifiersForIdentifiers:]
+ -[MPCPlayPerfMetrics set_transitionItemPosition:]
+ -[MPCPlayPerfMetrics set_transitionStyle:]
+ -[MPCPlayPerfMetrics transitionItemPosition]
+ -[MPCPlayPerfMetrics transitionStyle]
+ -[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartEvent:cursor:]
+ GCC_except_table1129
+ GCC_except_table1133
+ GCC_except_table1302
+ GCC_except_table1304
+ GCC_except_table1350
+ GCC_except_table1361
+ GCC_except_table1368
+ GCC_except_table1375
+ GCC_except_table1411
+ GCC_except_table1423
+ GCC_except_table1432
+ GCC_except_table1464
+ GCC_except_table1636
+ GCC_except_table1638
+ GCC_except_table1651
+ GCC_except_table1656
+ GCC_except_table1725
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1915
+ GCC_except_table1935
+ GCC_except_table1937
+ GCC_except_table1965
+ GCC_except_table1974
+ GCC_except_table1979
+ GCC_except_table1989
+ GCC_except_table1999
+ GCC_except_table2109
+ GCC_except_table2139
+ GCC_except_table2164
+ GCC_except_table2168
+ GCC_except_table2171
+ GCC_except_table2220
+ GCC_except_table2252
+ GCC_except_table2347
+ GCC_except_table2363
+ GCC_except_table2550
+ GCC_except_table2578
+ GCC_except_table2604
+ GCC_except_table2752
+ GCC_except_table2771
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table2813
+ GCC_except_table2815
+ GCC_except_table2817
+ GCC_except_table2819
+ GCC_except_table2822
+ GCC_except_table2847
+ GCC_except_table2861
+ GCC_except_table2864
+ GCC_except_table2869
+ GCC_except_table2870
+ GCC_except_table2875
+ GCC_except_table2878
+ GCC_except_table2881
+ GCC_except_table2901
+ GCC_except_table2909
+ GCC_except_table2951
+ GCC_except_table3029
+ GCC_except_table3040
+ GCC_except_table3041
+ GCC_except_table3065
+ GCC_except_table3073
+ GCC_except_table3114
+ GCC_except_table3115
+ GCC_except_table3131
+ GCC_except_table3189
+ GCC_except_table3204
+ GCC_except_table3209
+ GCC_except_table3246
+ GCC_except_table3248
+ GCC_except_table3255
+ GCC_except_table3266
+ GCC_except_table3271
+ GCC_except_table3307
+ GCC_except_table3352
+ GCC_except_table3474
+ GCC_except_table3495
+ GCC_except_table3497
+ GCC_except_table3498
+ GCC_except_table3526
+ GCC_except_table3540
+ GCC_except_table3715
+ GCC_except_table3719
+ GCC_except_table3742
+ GCC_except_table3744
+ GCC_except_table3750
+ GCC_except_table3759
+ GCC_except_table3882
+ GCC_except_table3926
+ GCC_except_table3927
+ GCC_except_table3946
+ GCC_except_table3954
+ GCC_except_table3972
+ GCC_except_table3977
+ GCC_except_table3979
+ GCC_except_table3993
+ GCC_except_table4016
+ GCC_except_table4027
+ GCC_except_table4113
+ GCC_except_table4118
+ GCC_except_table4122
+ GCC_except_table4131
+ GCC_except_table4154
+ GCC_except_table4170
+ GCC_except_table4275
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4581
+ GCC_except_table4615
+ GCC_except_table4617
+ GCC_except_table4625
+ GCC_except_table4633
+ GCC_except_table4648
+ GCC_except_table4656
+ GCC_except_table4664
+ GCC_except_table4673
+ GCC_except_table4688
+ GCC_except_table4733
+ GCC_except_table4757
+ GCC_except_table4759
+ GCC_except_table4767
+ GCC_except_table4820
+ GCC_except_table4845
+ GCC_except_table4958
+ GCC_except_table5058
+ GCC_except_table5298
+ GCC_except_table5299
+ GCC_except_table5371
+ GCC_except_table5458
+ GCC_except_table5607
+ GCC_except_table5632
+ GCC_except_table5745
+ GCC_except_table5827
+ GCC_except_table5835
+ GCC_except_table5836
+ GCC_except_table5900
+ GCC_except_table5925
+ GCC_except_table5960
+ GCC_except_table5963
+ GCC_except_table5966
+ GCC_except_table6052
+ GCC_except_table6267
+ GCC_except_table6284
+ GCC_except_table6332
+ GCC_except_table6345
+ GCC_except_table6848
+ GCC_except_table7189
+ GCC_except_table7281
+ GCC_except_table7290
+ GCC_except_table7370
+ GCC_except_table7377
+ GCC_except_table7395
+ GCC_except_table7444
+ GCC_except_table7445
+ GCC_except_table7448
+ GCC_except_table7453
+ GCC_except_table7469
+ _MPCPlaybackEngineEventItemMetadataKeyDiscNumber
+ _MPCPlaybackEngineEventItemMetadataKeyTrackNumber
+ _MPCPlaybackEngineEventPayloadKeyQueueAdjustedStartItemIdentifiers
+ _MSVFastHexStringFromBytes.hexCharacters.30087
+ _OBJC_IVAR_$_MPCModelGenericAVItem._lock
+ __IVARS__TtC17MediaPlaybackCoreP33_9861911E8ACEE440CB78D6684C8F8D5E24JumpScanningSubscription
+ __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.39
+ ___36-[MPCRequestController setResponse:]_block_invoke.31
+ ___46-[MPCPlayPerfConsumer subscribeToEventStream:]_block_invoke_8
+ ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke.89
+ ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke.93
+ ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke.98
+ ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke_2.90
+ ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke_2.97
+ ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke.263
+ ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke_2.264
+ ___49-[_MPCPlayerPlaybackRateCommand setPlaybackRate:]_block_invoke
+ ___56-[_MPCPlaybackEnginePlayer finalizeSetQueue:completion:]_block_invoke.58
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.129
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.131
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.135
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.145
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.155
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.173
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.96
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_2.143
+ ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_3.147
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.461
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.466
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.468
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.501
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.529
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.579
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.581
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.601
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.647
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.654
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.657
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.680
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.702
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.720
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.742
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.746
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.753
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.762
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.777
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.790
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.794
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.467
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.476
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.505
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.537
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.580
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.582
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.602
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.661
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.693
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.703
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.721
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.541
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.606
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.706
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.726
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.545
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.607
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.708
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.731
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.557
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.611
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.736
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.561
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.618
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.565
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.619
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.572
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.623
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.624
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.187
+ ___62-[_MPCMediaRemotePublisher _backgroundTaskWithReason:timeout:]_block_invoke.439
+ ___65-[MPCRequestController setNeedsReloadForSignificantRequestChange]_block_invoke.38
+ ___65-[MPCRequestController setNeedsReloadForSignificantRequestChange]_block_invoke.43
+ ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.804
+ ___68-[_MPCPlaybackEnginePlayer togglePlaybackWithIdentifier:completion:]_block_invoke.73
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.271
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.290
+ ___76-[_MPCPlaybackEnginePlayer donateMetricsForTransitionWillStartEvent:cursor:]_block_invoke
+ ___80-[MPCModelStorePlaybackItemsRequest adjustedStartItemIdentifiersForIdentifiers:]_block_invoke
+ ___80-[MPCModelStorePlaybackItemsRequest adjustedStartItemIdentifiersForIdentifiers:]_block_invoke_2
+ ___80-[MPCModelStorePlaybackItemsRequest adjustedStartItemIdentifiersForIdentifiers:]_block_invoke_3
+ ___Block_byref_object_copy_.11268
+ ___Block_byref_object_copy_.11442
+ ___Block_byref_object_copy_.11742
+ ___Block_byref_object_copy_.12455
+ ___Block_byref_object_copy_.13604
+ ___Block_byref_object_copy_.15747
+ ___Block_byref_object_copy_.16341
+ ___Block_byref_object_copy_.16750
+ ___Block_byref_object_copy_.17344
+ ___Block_byref_object_copy_.17985
+ ___Block_byref_object_copy_.18857
+ ___Block_byref_object_copy_.19402
+ ___Block_byref_object_copy_.19590
+ ___Block_byref_object_copy_.20039
+ ___Block_byref_object_copy_.21199
+ ___Block_byref_object_copy_.22135
+ ___Block_byref_object_copy_.25092
+ ___Block_byref_object_copy_.25897
+ ___Block_byref_object_copy_.26317
+ ___Block_byref_object_copy_.26660
+ ___Block_byref_object_copy_.27094
+ ___Block_byref_object_copy_.28495
+ ___Block_byref_object_copy_.29059
+ ___Block_byref_object_copy_.2935
+ ___Block_byref_object_copy_.33910
+ ___Block_byref_object_copy_.34382
+ ___Block_byref_object_copy_.34799
+ ___Block_byref_object_copy_.35157
+ ___Block_byref_object_copy_.3883
+ ___Block_byref_object_copy_.4057
+ ___Block_byref_object_copy_.5046
+ ___Block_byref_object_copy_.6969
+ ___Block_byref_object_copy_.7785
+ ___Block_byref_object_copy_.9841
+ ___Block_byref_object_copy_.9908
+ ___Block_byref_object_dispose_.11269
+ ___Block_byref_object_dispose_.11443
+ ___Block_byref_object_dispose_.11743
+ ___Block_byref_object_dispose_.12456
+ ___Block_byref_object_dispose_.13605
+ ___Block_byref_object_dispose_.15748
+ ___Block_byref_object_dispose_.16342
+ ___Block_byref_object_dispose_.16751
+ ___Block_byref_object_dispose_.17345
+ ___Block_byref_object_dispose_.17986
+ ___Block_byref_object_dispose_.18858
+ ___Block_byref_object_dispose_.19403
+ ___Block_byref_object_dispose_.19591
+ ___Block_byref_object_dispose_.20040
+ ___Block_byref_object_dispose_.21200
+ ___Block_byref_object_dispose_.22136
+ ___Block_byref_object_dispose_.25093
+ ___Block_byref_object_dispose_.25898
+ ___Block_byref_object_dispose_.26318
+ ___Block_byref_object_dispose_.26661
+ ___Block_byref_object_dispose_.27095
+ ___Block_byref_object_dispose_.28496
+ ___Block_byref_object_dispose_.29060
+ ___Block_byref_object_dispose_.2936
+ ___Block_byref_object_dispose_.33911
+ ___Block_byref_object_dispose_.34383
+ ___Block_byref_object_dispose_.34800
+ ___Block_byref_object_dispose_.35158
+ ___Block_byref_object_dispose_.3884
+ ___Block_byref_object_dispose_.4058
+ ___Block_byref_object_dispose_.5047
+ ___Block_byref_object_dispose_.6970
+ ___Block_byref_object_dispose_.7786
+ ___Block_byref_object_dispose_.9842
+ ___Block_byref_object_dispose_.9909
+ ___block_descriptor_32_e46_v16?0"<MPMutableUniversalStoreIdentifiers>"8l
+ ___block_descriptor_34_e45_v16?0"<MPMutablePersonalStoreIdentifiers>"8l
+ ___block_descriptor_36_e18_B16?0"NSNumber"8l
+ ___block_descriptor_36_e49_v16?0"MPIdentifierSet<MPMutableIdentifierSet>"8l
+ ___block_literal_global.10407
+ ___block_literal_global.10567
+ ___block_literal_global.10708
+ ___block_literal_global.11.14057
+ ___block_literal_global.110.21114
+ ___block_literal_global.11002
+ ___block_literal_global.11295
+ ___block_literal_global.11625
+ ___block_literal_global.11809
+ ___block_literal_global.11948
+ ___block_literal_global.121.24475
+ ___block_literal_global.12158
+ ___block_literal_global.127.21085
+ ___block_literal_global.12918
+ ___block_literal_global.131.21086
+ ___block_literal_global.135
+ ___block_literal_global.13725
+ ___block_literal_global.14.21239
+ ___block_literal_global.14071
+ ___block_literal_global.143.24487
+ ___block_literal_global.146.24483
+ ___block_literal_global.14803
+ ___block_literal_global.152.14658
+ ___block_literal_global.157.19578
+ ___block_literal_global.160.19577
+ ___block_literal_global.16205
+ ___block_literal_global.16320
+ ___block_literal_global.167.10677
+ ___block_literal_global.170.10678
+ ___block_literal_global.17117
+ ___block_literal_global.17244
+ ___block_literal_global.17285
+ ___block_literal_global.17357
+ ___block_literal_global.178
+ ___block_literal_global.17808
+ ___block_literal_global.17978
+ ___block_literal_global.19025
+ ___block_literal_global.19708
+ ___block_literal_global.19782
+ ___block_literal_global.199.23088
+ ___block_literal_global.20711
+ ___block_literal_global.21238
+ ___block_literal_global.21540
+ ___block_literal_global.21890
+ ___block_literal_global.22176
+ ___block_literal_global.23187
+ ___block_literal_global.24513
+ ___block_literal_global.25507
+ ___block_literal_global.262
+ ___block_literal_global.26557
+ ___block_literal_global.268
+ ___block_literal_global.270
+ ___block_literal_global.27083
+ ___block_literal_global.274
+ ___block_literal_global.27715
+ ___block_literal_global.282.26330
+ ___block_literal_global.289
+ ___block_literal_global.28929
+ ___block_literal_global.294
+ ___block_literal_global.29679
+ ___block_literal_global.30.19709
+ ___block_literal_global.30302
+ ___block_literal_global.322.12706
+ ___block_literal_global.341
+ ___block_literal_global.3416
+ ___block_literal_global.34421
+ ___block_literal_global.34829
+ ___block_literal_global.37.21854
+ ___block_literal_global.3956
+ ___block_literal_global.422
+ ___block_literal_global.4379
+ ___block_literal_global.45.29666
+ ___block_literal_global.4696
+ ___block_literal_global.47.24499
+ ___block_literal_global.5175
+ ___block_literal_global.547
+ ___block_literal_global.640
+ ___block_literal_global.656
+ ___block_literal_global.6570
+ ___block_literal_global.659
+ ___block_literal_global.705
+ ___block_literal_global.7261
+ ___block_literal_global.729
+ ___block_literal_global.733
+ ___block_literal_global.738
+ ___block_literal_global.7499
+ ___block_literal_global.7792
+ ___block_literal_global.9.21859
+ ___block_literal_global.964
+ ___block_literal_global.9986
+ ___unnamed_15
+ ___unnamed_7
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_MediaPlaybackCore
+ _associated conformance 17MediaPlaybackCore24JumpScanningSubscription33_9861911E8ACEE440CB78D6684C8F8D5ELLCyxG7Combine0F0AaF06CustomN21IdentifierConvertible
+ _associated conformance 17MediaPlaybackCore24JumpScanningSubscription33_9861911E8ACEE440CB78D6684C8F8D5ELLCyxG7Combine0F0AaF11Cancellable
+ _associated conformance 7Combine10PublishersO17MediaPlaybackCoreE11JumpScannerVAA9PublisherAD7FailureAaGP_s5Error
+ _block_copy_helper.112
+ _block_copy_helper.131
+ _block_copy_helper.141
+ _block_copy_helper.155
+ _block_copy_helper.165
+ _block_copy_helper.210
+ _block_copy_helper.216
+ _block_copy_helper.28
+ _block_copy_helper.38
+ _block_descriptor.114
+ _block_descriptor.133
+ _block_descriptor.143
+ _block_descriptor.157
+ _block_descriptor.167
+ _block_descriptor.212
+ _block_descriptor.218
+ _block_descriptor.30
+ _block_descriptor.40
+ _block_destroy_helper.113
+ _block_destroy_helper.132
+ _block_destroy_helper.142
+ _block_destroy_helper.156
+ _block_destroy_helper.166
+ _block_destroy_helper.211
+ _block_destroy_helper.217
+ _block_destroy_helper.29
+ _block_destroy_helper.39
+ _objc_msgSend$adjustedStartItemIdentifiersForIdentifiers:
+ _objc_msgSend$beginScanningWithDirection:supportsRateChange:identifier:completion:
+ _objc_msgSend$donateMetricsForTransitionWillStartEvent:cursor:
+ _objc_msgSend$metricsWithTransitionWillStartEvent:cursor:queueItem:
+ _objc_msgSend$pod_updateDurationSnapshotWithElapsedTime:playbackRate:playbackState:
+ _objc_msgSend$resetPlaybackStartTimeForReuseWithSeekToStartTime:
+ _objc_msgSend$set_transitionItemPosition:
+ _objc_msgSend$set_transitionStyle:
+ _objc_msgSend$stageConditionCommand
+ _objc_msgSend$transitionItemPosition
+ _objectdestroy.170Tm
+ _objectdestroy.19Tm
+ _objectdestroy.208Tm
+ _objectdestroy.223Tm
+ _objectdestroy.276Tm
+ _objectdestroy.57Tm
+ _sharedManager.onceToken.34420
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
+ _symbolic _____ 17MediaPlaybackCore15JumpScannerTypeO
+ _symbolic _____ 17MediaPlaybackCore24JumpScannerConfigurationV
+ _symbolic _____ 17MediaPlaybackCore24JumpScanningSubscription33_9861911E8ACEE440CB78D6684C8F8D5ELLC
+ _symbolic _____ 7Combine10PublishersO17MediaPlaybackCoreE11JumpScannerV
+ _symbolic _____9direction_Sb18supportsRateChange_____8metadatat 17MediaPlaybackCore9DirectionO AA18UserActionMetadataV
+ _symbolic _____9direction_Sd16baseJumpIntervalt 17MediaPlaybackCore9DirectionO
+ _symbolic _____yxGSgXw 17MediaPlaybackCore24JumpScanningSubscription33_9861911E8ACEE440CB78D6684C8F8D5ELLC
+ _symbolic _____yxGSgXwz_x______RzSd5Input_____RtzlXX 17MediaPlaybackCore24JumpScanningSubscription33_9861911E8ACEE440CB78D6684C8F8D5ELLC 7Combine10SubscriberP AG
+ _type_layout_string 17MediaPlaybackCore24JumpScannerConfigurationV
+ _type_layout_string 7Combine10PublishersO17MediaPlaybackCoreE11JumpScannerV
- -[MPAVItem(MFQueuePlayerItem) prepareForReuse]
- GCC_except_table1128
- GCC_except_table1132
- GCC_except_table1296
- GCC_except_table1298
- GCC_except_table1344
- GCC_except_table1355
- GCC_except_table1362
- GCC_except_table1369
- GCC_except_table1405
- GCC_except_table1417
- GCC_except_table1426
- GCC_except_table1458
- GCC_except_table1630
- GCC_except_table1632
- GCC_except_table1645
- GCC_except_table1650
- GCC_except_table1719
- GCC_except_table1794
- GCC_except_table1795
- GCC_except_table1909
- GCC_except_table1929
- GCC_except_table1931
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
- GCC_except_table2742
- GCC_except_table2761
- GCC_except_table2768
- GCC_except_table2769
- GCC_except_table2793
- GCC_except_table2795
- GCC_except_table2799
- GCC_except_table2807
- GCC_except_table2812
- GCC_except_table2837
- GCC_except_table2844
- GCC_except_table2849
- GCC_except_table2851
- GCC_except_table2860
- GCC_except_table2865
- GCC_except_table2868
- GCC_except_table2871
- GCC_except_table2891
- GCC_except_table2899
- GCC_except_table2941
- GCC_except_table3022
- GCC_except_table3033
- GCC_except_table3034
- GCC_except_table3058
- GCC_except_table3066
- GCC_except_table3107
- GCC_except_table3108
- GCC_except_table3124
- GCC_except_table3182
- GCC_except_table3197
- GCC_except_table3202
- GCC_except_table3236
- GCC_except_table3238
- GCC_except_table3245
- GCC_except_table3256
- GCC_except_table3261
- GCC_except_table3297
- GCC_except_table3342
- GCC_except_table3464
- GCC_except_table3486
- GCC_except_table3488
- GCC_except_table3489
- GCC_except_table3516
- GCC_except_table3520
- GCC_except_table3703
- GCC_except_table3707
- GCC_except_table3718
- GCC_except_table3732
- GCC_except_table3738
- GCC_except_table3747
- GCC_except_table3870
- GCC_except_table3914
- GCC_except_table3915
- GCC_except_table3934
- GCC_except_table3942
- GCC_except_table3960
- GCC_except_table3965
- GCC_except_table3967
- GCC_except_table3981
- GCC_except_table4004
- GCC_except_table4015
- GCC_except_table4101
- GCC_except_table4106
- GCC_except_table4110
- GCC_except_table4119
- GCC_except_table4142
- GCC_except_table4158
- GCC_except_table4263
- GCC_except_table4384
- GCC_except_table4385
- GCC_except_table4569
- GCC_except_table4603
- GCC_except_table4605
- GCC_except_table4613
- GCC_except_table4621
- GCC_except_table4636
- GCC_except_table4644
- GCC_except_table4652
- GCC_except_table4661
- GCC_except_table4676
- GCC_except_table4721
- GCC_except_table4745
- GCC_except_table4747
- GCC_except_table4755
- GCC_except_table4808
- GCC_except_table4833
- GCC_except_table4946
- GCC_except_table5046
- GCC_except_table5286
- GCC_except_table5287
- GCC_except_table5359
- GCC_except_table5446
- GCC_except_table5595
- GCC_except_table5620
- GCC_except_table5733
- GCC_except_table5815
- GCC_except_table5823
- GCC_except_table5824
- GCC_except_table5888
- GCC_except_table5913
- GCC_except_table5948
- GCC_except_table5951
- GCC_except_table5954
- GCC_except_table6040
- GCC_except_table6255
- GCC_except_table6272
- GCC_except_table6320
- GCC_except_table6333
- GCC_except_table6835
- GCC_except_table7176
- GCC_except_table7268
- GCC_except_table7277
- GCC_except_table7356
- GCC_except_table7363
- GCC_except_table7382
- GCC_except_table7431
- GCC_except_table7432
- GCC_except_table7435
- GCC_except_table7440
- GCC_except_table7456
- _MSVFastHexStringFromBytes.hexCharacters.29999
- _OBJC_IVAR_$_MPCModelGenericAVItem._genericObjectLock
- __PROTOCOLS__TtC17MediaPlaybackCore18LibraryObjectQuery.38
- ___36-[MPCRequestController setResponse:]_block_invoke.27
- ___36-[MPCRequestController setResponse:]_block_invoke.32
- ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke.90
- ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke.97
- ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke_2.91
- ___47-[MPCRequestController _onQueue_reloadIfNeeded]_block_invoke_2.98
- ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke.266
- ___48-[MPCModelQueueFeeder reloadSection:completion:]_block_invoke_2.267
- ___56-[_MPCPlaybackEnginePlayer finalizeSetQueue:completion:]_block_invoke.56
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.132
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.134
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.138
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.148
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.158
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.98
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke.99
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_2.149
- ___60-[MPCModelQueueFeeder controller:defersResponse:completion:]_block_invoke_3.150
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.465
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.470
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.472
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.505
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.533
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.583
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.585
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.605
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.651
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.658
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.661
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.684
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.706
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.721
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.743
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.747
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.754
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.763
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.778
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.791
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.795
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.471
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.480
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.509
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.541
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.584
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.586
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.606
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.665
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.697
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.707
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.722
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.545
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.610
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.710
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.727
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.549
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.611
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.712
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.732
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.561
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.615
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.737
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.565
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.622
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.569
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.623
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.576
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.627
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.628
- ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.185
- ___62-[_MPCMediaRemotePublisher _backgroundTaskWithReason:timeout:]_block_invoke.443
- ___65-[MPCRequestController setNeedsReloadForSignificantRequestChange]_block_invoke.39
- ___65-[MPCRequestController setNeedsReloadForSignificantRequestChange]_block_invoke.44
- ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.805
- ___68-[_MPCPlaybackEnginePlayer togglePlaybackWithIdentifier:completion:]_block_invoke.71
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.265
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.284
- ___Block_byref_object_copy_.11259
- ___Block_byref_object_copy_.11433
- ___Block_byref_object_copy_.11733
- ___Block_byref_object_copy_.12438
- ___Block_byref_object_copy_.13624
- ___Block_byref_object_copy_.15697
- ___Block_byref_object_copy_.16291
- ___Block_byref_object_copy_.16700
- ___Block_byref_object_copy_.17296
- ___Block_byref_object_copy_.17935
- ___Block_byref_object_copy_.18800
- ___Block_byref_object_copy_.19336
- ___Block_byref_object_copy_.19518
- ___Block_byref_object_copy_.19959
- ___Block_byref_object_copy_.21101
- ___Block_byref_object_copy_.22037
- ___Block_byref_object_copy_.24996
- ___Block_byref_object_copy_.25805
- ___Block_byref_object_copy_.26226
- ___Block_byref_object_copy_.26570
- ___Block_byref_object_copy_.27004
- ___Block_byref_object_copy_.28408
- ___Block_byref_object_copy_.28972
- ___Block_byref_object_copy_.2934
- ___Block_byref_object_copy_.33801
- ___Block_byref_object_copy_.34273
- ___Block_byref_object_copy_.34687
- ___Block_byref_object_copy_.35045
- ___Block_byref_object_copy_.3728
- ___Block_byref_object_copy_.3902
- ___Block_byref_object_copy_.4895
- ___Block_byref_object_copy_.6916
- ___Block_byref_object_copy_.7767
- ___Block_byref_object_copy_.9827
- ___Block_byref_object_copy_.9894
- ___Block_byref_object_dispose_.11260
- ___Block_byref_object_dispose_.11434
- ___Block_byref_object_dispose_.11734
- ___Block_byref_object_dispose_.12439
- ___Block_byref_object_dispose_.13625
- ___Block_byref_object_dispose_.15698
- ___Block_byref_object_dispose_.16292
- ___Block_byref_object_dispose_.16701
- ___Block_byref_object_dispose_.17297
- ___Block_byref_object_dispose_.17936
- ___Block_byref_object_dispose_.18801
- ___Block_byref_object_dispose_.19337
- ___Block_byref_object_dispose_.19519
- ___Block_byref_object_dispose_.19960
- ___Block_byref_object_dispose_.21102
- ___Block_byref_object_dispose_.22038
- ___Block_byref_object_dispose_.24997
- ___Block_byref_object_dispose_.25806
- ___Block_byref_object_dispose_.26227
- ___Block_byref_object_dispose_.26571
- ___Block_byref_object_dispose_.27005
- ___Block_byref_object_dispose_.28409
- ___Block_byref_object_dispose_.28973
- ___Block_byref_object_dispose_.2935
- ___Block_byref_object_dispose_.33802
- ___Block_byref_object_dispose_.34274
- ___Block_byref_object_dispose_.34688
- ___Block_byref_object_dispose_.35046
- ___Block_byref_object_dispose_.3729
- ___Block_byref_object_dispose_.3903
- ___Block_byref_object_dispose_.4896
- ___Block_byref_object_dispose_.6917
- ___Block_byref_object_dispose_.7768
- ___Block_byref_object_dispose_.9828
- ___Block_byref_object_dispose_.9895
- ___block_literal_global.10393
- ___block_literal_global.10553
- ___block_literal_global.10695
- ___block_literal_global.10993
- ___block_literal_global.11.14083
- ___block_literal_global.110.21016
- ___block_literal_global.11286
- ___block_literal_global.11616
- ___block_literal_global.11800
- ___block_literal_global.11939
- ___block_literal_global.121.24379
- ___block_literal_global.12149
- ___block_literal_global.127.20985
- ___block_literal_global.12915
- ___block_literal_global.131.20986
- ___block_literal_global.133.20987
- ___block_literal_global.13748
- ___block_literal_global.14.21141
- ___block_literal_global.14097
- ___block_literal_global.143.24391
- ___block_literal_global.146.24387
- ___block_literal_global.14771
- ___block_literal_global.150
- ___block_literal_global.155.16842
- ___block_literal_global.160.19507
- ___block_literal_global.16155
- ___block_literal_global.16270
- ___block_literal_global.167.10662
- ___block_literal_global.170.10663
- ___block_literal_global.17069
- ___block_literal_global.17196
- ___block_literal_global.17237
- ___block_literal_global.17309
- ___block_literal_global.17758
- ___block_literal_global.17928
- ___block_literal_global.18963
- ___block_literal_global.19636
- ___block_literal_global.19710
- ___block_literal_global.199.22993
- ___block_literal_global.20614
- ___block_literal_global.21140
- ___block_literal_global.21442
- ___block_literal_global.21792
- ___block_literal_global.22078
- ___block_literal_global.23091
- ___block_literal_global.24417
- ___block_literal_global.25416
- ___block_literal_global.26466
- ___block_literal_global.265
- ___block_literal_global.26993
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.27628
- ___block_literal_global.277
- ___block_literal_global.282.26240
- ___block_literal_global.28842
- ___block_literal_global.292
- ___block_literal_global.29591
- ___block_literal_global.297
- ___block_literal_global.30.19637
- ___block_literal_global.30216
- ___block_literal_global.322.12703
- ___block_literal_global.3263
- ___block_literal_global.333
- ___block_literal_global.34312
- ___block_literal_global.34717
- ___block_literal_global.37.21756
- ___block_literal_global.3801
- ___block_literal_global.4224
- ___block_literal_global.426
- ___block_literal_global.45.29578
- ___block_literal_global.4542
- ___block_literal_global.47.24403
- ___block_literal_global.5098
- ___block_literal_global.551
- ___block_literal_global.644
- ___block_literal_global.6508
- ___block_literal_global.660
- ___block_literal_global.663
- ___block_literal_global.709
- ___block_literal_global.7229
- ___block_literal_global.730
- ___block_literal_global.734
- ___block_literal_global.739
- ___block_literal_global.7467
- ___block_literal_global.7774
- ___block_literal_global.9.21761
- ___block_literal_global.965
- ___block_literal_global.9972
- ___unnamed_3
- _block_copy_helper.11
- _block_copy_helper.111
- _block_copy_helper.164
- _block_copy_helper.17
- _block_copy_helper.201
- _block_copy_helper.207
- _block_copy_helper.34
- _block_descriptor.113
- _block_descriptor.13
- _block_descriptor.166
- _block_descriptor.19
- _block_descriptor.203
- _block_descriptor.209
- _block_descriptor.36
- _block_destroy_helper.112
- _block_destroy_helper.12
- _block_destroy_helper.165
- _block_destroy_helper.18
- _block_destroy_helper.202
- _block_destroy_helper.208
- _block_destroy_helper.35
- _objc_msgSend$audioFormatsDictionary
- _objc_msgSend$beginScanningWithDirection:identifier:completion:
- _objc_msgSend$resetPlaybackStartTimeForReuse
- _objc_msgSend$setAudioFormatsDictionary:
- _objc_msgSend$setAvailableSortedFormats:
- _objectdestroy.161Tm
- _objectdestroy.199Tm
- _objectdestroy.207Tm
- _objectdestroy.214Tm
- _objectdestroy.267Tm
- _objectdestroy.56Tm
- _sharedManager.onceToken.34311
CStrings:
+ " - supportsRateChange:"
+ "@\"<MFTimeStamp>\""
+ "@\"<MPObjectDatabaseProgressiveResult>\""
+ "Aligning %ld chapters for %{private,mask.hash}s."
+ "DisableOutroItemRetain"
+ "EnableTransitionTeardownCompletionHandler"
+ "Failed to perform CreateStationSetQueue with playback intent: %@"
+ "Failed to perform SetQueue with playback intent: %@"
+ "FailedToPerformSetQueue"
+ "InternalPlayerController - Did seek to end of stream - succeeded: "
+ "PlaybackStackController - overlappedPlaybackDidEnd with outgoingItem: "
+ "PlaybackStackController - overlappedPlaybackWillBegin with outgoingItem: "
+ "PlaybackStackController - playbackDidStart:"
+ "Podcasts: Not reporting `isSignedIn`. No `accountMetadata` event found."
+ "Podcasts: Not reporting `isSignedIn`. No `queueAdd` event found."
+ "Podcasts: Not reporting `playContext`. No related `itemBegin` event found."
+ "Podcasts: Not reporting `playbackSettingsScope`. No related `itemBegin` event found."
+ "Podcasts: Unable to query `playbackSettingsScope`. No metadata found."
+ "Podcasts: Unable to query for `featureName`, no `queueAdd` event found."
+ "Podcasts: Unable to query for `featureName`, no `queueReportingMetadata` found."
+ "Podcasts: Unable to report `userId` or `clientId` for event type: %s with error %s."
+ "Podcasts: Unexpected `featureName` value found - %s."
+ "Reset transition with reason: "
+ "SPIR-Adjusted"
+ "T@\"NSNumber\",&,D,N,Sset_transitionItemPosition:"
+ "T@\"NSNumber\",&,D,N,Sset_transitionStyle:"
+ "TransitionWillStart event doesn't have corresponding TransitionCreated event (eventID:%{public}@ startItemId:%{public}@ %{public}@)"
+ "TransitionWillStart event doesn't have valid item identifiers (eventID:%{public}@)"
+ "Unable to fetch chapters for asset %{private,mask.hash}s identifier %{private,mask.hash}s with error %s."
+ "Unable to fetch chapters for asset %{private,mask.hash}s with error %s."
+ "Updating chapters for %{private,mask.hash}s."
+ "[%{public}@]-%{public}@ - playbackDidStartForItem:rate: - item=%{public}@ - rate:%1.2f - expectedStartTime: %1.3f - from stalling:%{BOOL}u - timeStamp:%{public}@"
+ "[ALC:%{public}s] - Failed to fetch Smart Transition info - unable to resolve outgoing itemID"
+ "[ALC]: 🔴 TransitionController removeSmartTransitionOutroItemReference called with: %s but existing outroItemReference was %s"
+ "[ALC]: 🟡 TransitionController setSmartTransitionOutroItemReference: %s"
+ "[ALC]: 🟢 TransitionController removeSmartTransitionOutroItemReference: %s"
+ "[EST:%{public}s)] clearing expected start time"
+ "[EST:%{public}s)] setting expected start time due to seek"
+ "[EST:%{public}s)] setting expected start time due to setRate with no timeContinuity"
+ "[EST:%{public}s)] setting expected start time due to setRate with timeContinuity"
+ "[EST:%{public}s)] setting expected start time=%f"
+ "[FAF:%{public}s]: Firing off firstFrame event for currentItem"
+ "[FAF:%{public}s]: Setting expected startTime on new currentItem"
+ "[InternalPlayerController:JumpScan] Beginning JumpScan"
+ "[InternalPlayerController:JumpScan] Posting SeekToTimeCompleted"
+ "[InternalPlayerController:JumpScan] jumpInterval=%f currentTime=%f newSeekTime=%f"
+ "[MPAVItem isInContiguousAlbum] Both items are not songs: currentID=%{public}@ - currentType=%ld, nextID=%{public}@ - nextType=%ld"
+ "[MPAVItem isInContiguousAlbum] Current song: contentIdentifier=%{public}@ discNumber=%ld trackNumber=%ld album.identifiers=%{public}@ | Next song: contentIdentifier=%{public}@, discNumber=%ld, trackNumber=%ld, album.identifiers=%{public}@"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler [failure] isFinalResponse=%{BOOL}u error=%{public}@"
+ "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler [start item satisfied] newResponse=%p isFinalResponse=%{BOOL}u startIdentifier=%{public}@"
+ "[MQF:%{public}@:%p] controller:shouldRetryFailedRequestWithError: | calling loadingCompletionHandler [failure]  error=%{public}@"
+ "[MQF:%{public}@:%p] loadPlaybackContext: | updated startItemIdentifiers [cleared misleading IDs] startItemIdentifiers=%{public}@"
+ "[RCO:%p:%p] _onQueue_reloadIfNeeded | skipping load [already delivering response] pendingResponse=%p"
+ "[RCO:%p:%p] _onQueue_reloadIfNeeded | skipping load [already loading] cancelToken=%p"
+ "[RCO:%p:%p] _onQueue_reloadIfNeeded | skipping load [no request]"
+ "[RCO:%p:%p] _onQueue_reloadIfNeeded | skipping load [not needed]"
+ "[RCO:%p:%p] _onQueue_scheduleRetryAfterInterval:%f | reloading [retry timer] retryInterval=%f"
+ "[RCO:%p:%p] _onQueue_scheduleRetryAfterInterval:%f | skipping reload [no longer needed]"
+ "[RCO:%p:%p] _responseDidInvalidate:… | ignoring notification [not current response] notification.object=%p currentResponse=%p pendingResponse=%p"
+ "[RCO:%p:%p] _responseDidInvalidate:… | needs reload [response invalid] invalidatedResponse=%p"
+ "[RCO:%p:%p] _responseDidInvalidate:… | reloading [automatic, response invalid]"
+ "[RCO:%p:%p] beginAutomaticResponseLoading | reloading [automatic, needs reload]"
+ "[RCO:%p:%p] beginAutomaticResponseLoading | starting automatic reloading [first observer] observers=%ld"
+ "[RCO:%p:%p] dealloc | ending automatic reloading"
+ "[RCO:%p:%p] endAutomaticResponseLoading | ending automatic reloading [no observers]"
+ "[RCO:%p:%p] performWithCompletion:… | deferring response replacement [delegate supports deferral] response=%p delegate=%p"
+ "[RCO:%p:%p] performWithCompletion:… | delegate replacing response [deferred completion] delegate=%p response=%p"
+ "[RCO:%p:%p] performWithCompletion:… | delegate retry decision [delegate consulted] delegate=%p shouldRetry=%{BOOL}d"
+ "[RCO:%p:%p] performWithCompletion:… | delegate timeout [completion not called] delegate=%p response=%p"
+ "[RCO:%p:%p] performWithCompletion:… | ignoring error [request revision mismatch] previousRequestID=%{public}@ currentRequestID=%{public}@"
+ "[RCO:%p:%p] performWithCompletion:… | processing error [current request] requestID=%{public}@"
+ "[RCO:%p:%p] performWithCompletion:… | recovering from error [determining retry] shouldRetry=%{BOOL}d automaticLoad=%{BOOL}d"
+ "[RCO:%p:%p] performWithCompletion:… | reloading [request revision mismatch] previousRequestID=%{public}@ currentRequestID=%{public}@"
+ "[RCO:%p:%p] performWithCompletion:… | replacing response [no deferral] response=%p"
+ "[RCO:%p:%p] performWithCompletion:… | request failed [error returned] error=%{public}@"
+ "[RCO:%p:%p] performWithCompletion:… | request finished loading []"
+ "[RCO:%p:%p] performWithCompletion:… | request finished loading [] error=%{public}@"
+ "[RCO:%p:%p] performWithCompletion:… | scheduling retry [will retry] retryInterval=%f"
+ "[RCO:%p:%p] reloadIfNeeded | reloading [client request]"
+ "[RCO:%p:%p] setNeedsReload | canceling request in flight [client request]"
+ "[RCO:%p:%p] setNeedsReload | needs reload [client request]"
+ "[RCO:%p:%p] setNeedsReload | reloading [automatic, client request]"
+ "[RCO:%p:%p] setNeedsReload | removing observer [current response cleanup] response=%p"
+ "[RCO:%p:%p] setNeedsReload | removing observer [pending response cleanup] pendingResponse=%p"
+ "[RCO:%p:%p] setNeedsReloadForSignificantRequestChange | clearing response [deferred completion] delegate=%p"
+ "[RCO:%p:%p] setNeedsReloadForSignificantRequestChange | clearing response [no deferral]"
+ "[RCO:%p:%p] setNeedsReloadForSignificantRequestChange | deferring response clearing [delegate supports deferral] delegate=%p"
+ "[RCO:%p:%p] setNeedsReloadForSignificantRequestChange | delegate timeout [completion not called] delegate=%p"
+ "[RCO:%p:%p] setRequest:… | canceling current request [request changed] oldRequest=%p newRequest=%p"
+ "[RCO:%p:%p] setRequest:… | needs reload [request changed]"
+ "[RCO:%p:%p] setRequest:… | reloading [automatic, request changed]"
+ "[RCO:%p:%p] setResponse:… | adding observer [monitoring invalidation] response=%p"
+ "[RCO:%p:%p] setResponse:… | reloading [response already invalid] response=%p"
+ "[RCO:%p:%p] setResponse:… | reloading [response became invalid] response=%p"
+ "[RCO:%p:%p] setResponse:… | removing observer [previous response cleanup] oldResponse=%p"
+ "[RCO:%p:%p] setResponse:… | signaling response replacement [delegate supports signal] delegate=%p oldResponse=%p newResponse=%p"
+ "[RCO:%p:%p] setResponse:… | updating response [new response set] oldResponse=%p response=%p"
+ "[SNM:%{public}s] performSetSession | pause failed with error=%{public}@"
+ "adjustedStartItemIdentifiersForIdentifiers:"
+ "beginScanning(direction:supportsRateChange:identifier:)"
+ "beginScanningWithDirection:supportsRateChange:identifier:completion:"
+ "currentJumpCount"
+ "disc-number"
+ "donateMetricsForTransitionWillStartEvent:cursor:"
+ "hasBegunPlayback"
+ "initial request failed"
+ "metricsWithTransitionWillStartEvent:cursor:queueItem:"
+ "msc_tstn_itemposition"
+ "msc_tstn_style"
+ "perShowSettingsDidChange:"
+ "playbackSettingsScope"
+ "pod_updateDurationSnapshotWithElapsedTime:playbackRate:playbackState:"
+ "prepareForReuseWithSeekToStartTime:"
+ "queue-adjusted-start-item-ids"
+ "resetPlaybackStartTimeForReuseWithSeekToStartTime:"
+ "set_transitionItemPosition:"
+ "set_transitionStyle:"
+ "smartTransitionOutroItemReference"
+ "success item startTime endTime identifier passive timeStamp "
+ "track-number"
+ "transitionItemPosition"
+ "v36@0:8d16f24q28"
+ "v44@0:8q16B24@\"NSString\"28@?<v@?@\"NSError\">36"
+ "v44@0:8q16B24@\"NSString\"28@?<v@?@\"NSString\"@\"NSError\">36"
+ "v44@0:8q16B24@28@?36"
+ "{?=qiIq}"
+ "|%{public}@ %{public}@ %2i %{public}@  │ adjusted-start-item: %{public}@"
+ "|%{public}@ %{public}@ %2i %{public}@  │ discNumber: %ld : trackNumber: %ld"
+ "\xf0\xf0\xf0\x81"
- "AV does not support FF"
- "AV does not support RW"
- "EnableTransitionDurationMatchingCheck"
- "Failed to load playback intent: %@"
- "Failed to load queue controller with content"
- "FailedToDecodePlaylistManagerArchive"
- "Found %ld chapters"
- "InternalPlayerController - Did seek to end of stream - suceeded: "
- "Podcasts: Not reporting `isSignedIn`. No `accountMetadata` found."
- "Podcasts: Not reporting `podcastPageContext`. No related `itemBegin` event found."
- "Podcasts: Unable to report `userId` or `clientId` for event type: %{public}s with error %{public}s."
- "RCO %{public}@: Adding observer for %p"
- "RCO %{public}@: Canceling request [request by client]"
- "RCO %{public}@: Canceling request [request changed]"
- "RCO %{public}@: Clearing response"
- "RCO %{public}@: Deferring clearing of %p to delegate %p"
- "RCO %{public}@: Delegate %p clearing response with %p"
- "RCO %{public}@: Delegate %p timeout replacing response."
- "RCO %{public}@: Ending automatic reloading"
- "RCO %{public}@: Ending automatic reloading [dealloc]"
- "RCO %{public}@: Needs reload [request by client]"
- "RCO %{public}@: Needs reload [request changed]"
- "RCO %{public}@: Needs reload [response invalid before -setResponse: after adding observer]"
- "RCO %{public}@: Needs reload [response invalid before -setResponse:]"
- "RCO %{public}@: Needs reload [response invalid]"
- "RCO %{public}@: Reloading [automatic, beginLoading]"
- "RCO %{public}@: Reloading [automatic, request changed]"
- "RCO %{public}@: Reloading [automatic, requested by client]"
- "RCO %{public}@: Reloading [automatic, response invalid]"
- "RCO %{public}@: Reloading [requested by client]"
- "RCO %{public}@: Reloading [response invalid before -setResponse: after adding observer]"
- "RCO %{public}@: Reloading [response invalid before -setResponse:]"
- "RCO %{public}@: Reloading [retry mismatched request revision]"
- "RCO %{public}@: Reloading [retry, failed request]"
- "RCO %{public}@: Removing observer for %p"
- "RCO %{public}@: Request loading skipped [already loading]"
- "RCO %{public}@: Request loading skipped [no request]"
- "RCO %{public}@: Request loading skipped [not needed]"
- "RCO %{public}@: Scheduled reload skipped."
- "RCO %{public}@: Starting automatic reloading"
- "RCO %{public}@: Updating response to %p"
- "RCO %{public}@: _responseDidInvalidate [ignoring, not current response] %{public}@"
- "RCO <%{public}@ %p>: Deferring replacement of %p to delegate %p"
- "RCO <%{public}@ %p>: Delegate %p replacing response with %p"
- "RCO <%{public}@ %p>: Delegate %p returned shouldRetry: %d"
- "RCO <%{public}@ %p>: Delegate %p timeout replacing response."
- "RCO <%{public}@ %p>: Needs reload [failed request]"
- "RCO <%{public}@ %p>: Recovering from error. shouldRetry: %d"
- "RCO <%{public}@ %p>: Replacing response"
- "RCO <%{public}@ %p>: Request failed with error: %{public}@"
- "RCO <%{public}@ %p>: Request finished loading"
- "RCO <%{public}@ %p>: Scheduling retry after %fs"
- "RCO <%{public}@ %p>: Signaling replacement of %p -> %p to delegate %p"
- "[%{public}@]-%{public}@ - playbackDidStartForItem:rate: - item=%{public}@ - rate:%1.2f - from stalling:%{BOOL}u - timeStamp:%{public}@"
- "[ALC:%{public}s] - Failed to fetch Smart Transition info - unable to resolve outoing itemID"
- "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler [start item satisfied] newResponse=%p isFinalResponse=%{BOOL}u"
- "[MQF:%{public}@:%p] controller:defersResponse:completion: | calling loadingCompletionHandler with error [%{public}@] newResponse=%p isFinalResponse=YES error=%{public}@"
- "[PodcastAVItem/Chapters] Fetched %{private,mask.hash}s chapters for episode %{private,mask.hash}s."
- "_genericObjectLock"
- "beginScanning(direction:identifier:)"
- "beginScanningWithDirection:identifier:completion:"
- "empty model response"
- "failed to resolve startItem"
- "prepareForReuse"
- "resetPlaybackStartTimeForReuse"
- "v28@0:8d16f24"
- "v40@0:8q16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "\xf0\xf0\xf0a"

```
