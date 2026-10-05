## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-26200.26.37.501.0
-  __TEXT.__text: 0x4869d0
-  __TEXT.__objc_methlist: 0x17f30
+26200.26.39.301.0
+  __TEXT.__text: 0x48bc5c
+  __TEXT.__objc_methlist: 0x17f58
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x109c0
-  __TEXT.__oslogstring: 0x4ce5f
-  __TEXT.__cstring: 0x25e6c
-  __TEXT.__swift5_typeref: 0x5486
-  __TEXT.__swift5_capture: 0xaf04
-  __TEXT.__constg_swiftt: 0x7b40
-  __TEXT.__swift5_reflstr: 0x5a42
-  __TEXT.__swift5_fieldmd: 0x56b4
+  __TEXT.__const: 0x10a80
+  __TEXT.__oslogstring: 0x4d037
+  __TEXT.__cstring: 0x26068
+  __TEXT.__swift5_typeref: 0x54c2
+  __TEXT.__swift5_capture: 0xb1bc
+  __TEXT.__constg_swiftt: 0x7bd4
+  __TEXT.__swift5_reflstr: 0x5af2
+  __TEXT.__swift5_fieldmd: 0x5718
   __TEXT.__swift5_builtin: 0x6f4
   __TEXT.__swift5_mpenum: 0x130
   __TEXT.__swift5_assocty: 0xbc0
-  __TEXT.__swift5_proto: 0x92c
-  __TEXT.__swift5_types: 0x564
-  __TEXT.__swift_as_entry: 0x4a4
-  __TEXT.__swift_as_ret: 0x5bc
-  __TEXT.__swift_as_cont: 0xe14
+  __TEXT.__swift5_proto: 0x934
+  __TEXT.__swift5_types: 0x568
+  __TEXT.__swift_as_entry: 0x4b0
+  __TEXT.__swift_as_ret: 0x5d8
+  __TEXT.__swift_as_cont: 0xe44
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x5a7c
+  __TEXT.__gcc_except_tab: 0x5a6c
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0x106e0
-  __TEXT.__eh_frame: 0x102b8
+  __TEXT.__unwind_info: 0x10c40
+  __TEXT.__eh_frame: 0x104c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x93d0
+  __DATA_CONST.__const: 0x9498
   __DATA_CONST.__objc_classlist: 0xd30
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcbe8
+  __DATA_CONST.__objc_selrefs: 0xcc08
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6d8
-  __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0x3450
-  __AUTH_CONST.__const: 0x238e0
-  __AUTH_CONST.__cfstring: 0x1ec60
-  __AUTH_CONST.__objc_const: 0x34920
+  __DATA_CONST.__objc_arraydata: 0x290
+  __DATA_CONST.__got: 0x3460
+  __AUTH_CONST.__const: 0x24018
+  __AUTH_CONST.__cfstring: 0x1ee00
+  __AUTH_CONST.__objc_const: 0x349c0
   __AUTH_CONST.__objc_intobj: 0x8a0
-  __AUTH_CONST.__objc_arrayobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x3440
+  __AUTH_CONST.__auth_got: 0x3458
   __AUTH.__objc_data: 0x5a40
-  __AUTH.__data: 0x40c0
-  __DATA.__objc_ivar: 0x1ad8
-  __DATA.__data: 0x72a0
+  __AUTH.__data: 0x40f0
+  __DATA.__objc_ivar: 0x1adc
+  __DATA.__data: 0x7330
   __DATA.__common: 0x240
   __DATA_DIRTY.__objc_data: 0x3590
-  __DATA_DIRTY.__data: 0x4558
+  __DATA_DIRTY.__data: 0x45d8
   __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24532
-  Symbols:   18686
-  CStrings:  8280
+  Functions: 24707
+  Symbols:   18709
+  CStrings:  8298
 
Symbols:
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:completionHandler:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:error:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSMetadataItemInMetadata:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSSessionMetadataItemWithTimeout:completionHandler:]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) _sharedKeySegmentDurationFromHLSSessionDataOfAsset:completionHandler:]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTimeWithCompletionHandler:]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) sharedKeySegmentDurationWithCompletionHandler:]
+ -[MPCPlaybackErrorController playbackDidSucceedForItem:]
+ -[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSAudioAssetMetadataDictionary:]
+ GCC_except_table3589
+ GCC_except_table3610
+ GCC_except_table3617
+ GCC_except_table3646
+ GCC_except_table3656
+ GCC_except_table3713
+ GCC_except_table3722
+ GCC_except_table3792
+ GCC_except_table3893
+ GCC_except_table3904
+ GCC_except_table3920
+ GCC_except_table3926
+ GCC_except_table3935
+ GCC_except_table4063
+ GCC_except_table4108
+ GCC_except_table4109
+ GCC_except_table4110
+ GCC_except_table4129
+ GCC_except_table4138
+ GCC_except_table4156
+ GCC_except_table4161
+ GCC_except_table4163
+ GCC_except_table4177
+ GCC_except_table4200
+ GCC_except_table4211
+ GCC_except_table4300
+ GCC_except_table4319
+ GCC_except_table4332
+ GCC_except_table4343
+ GCC_except_table4374
+ GCC_except_table4545
+ GCC_except_table4546
+ GCC_except_table4724
+ GCC_except_table4759
+ GCC_except_table4761
+ GCC_except_table4769
+ GCC_except_table4777
+ GCC_except_table4792
+ GCC_except_table4800
+ GCC_except_table4808
+ GCC_except_table4818
+ GCC_except_table4833
+ GCC_except_table4877
+ GCC_except_table4891
+ GCC_except_table4910
+ GCC_except_table4916
+ GCC_except_table4968
+ GCC_except_table5006
+ GCC_except_table5094
+ GCC_except_table5195
+ GCC_except_table5438
+ GCC_except_table5439
+ GCC_except_table5515
+ GCC_except_table5607
+ GCC_except_table5759
+ GCC_except_table5784
+ GCC_except_table5901
+ GCC_except_table5982
+ GCC_except_table5990
+ GCC_except_table5991
+ GCC_except_table6055
+ GCC_except_table6080
+ GCC_except_table6115
+ GCC_except_table6118
+ GCC_except_table6121
+ GCC_except_table6207
+ GCC_except_table6424
+ GCC_except_table6441
+ GCC_except_table6489
+ GCC_except_table6502
+ GCC_except_table7018
+ GCC_except_table7352
+ GCC_except_table7367
+ GCC_except_table7470
+ GCC_except_table7559
+ GCC_except_table7566
+ GCC_except_table7584
+ GCC_except_table7636
+ GCC_except_table7639
+ GCC_except_table7644
+ GCC_except_table7660
+ _MPCHLSAudioAssetMetadataDictionaryKey
+ _MPHomeMonitorCurrentHomeDidChangeNotification
+ _MPHomeMonitorHomeUsersDidChangeNotification
+ _OBJC_IVAR_$__MPCMediaRemotePublisher._hostingSharedSessionIDInitialized
+ ___115-[MPCModelGenericAVItem(KeyDeliveryDeferral) _sharedKeySegmentDurationFromHLSSessionDataOfAsset:completionHandler:]_block_invoke
+ ___140-[MPCModelGenericAVItem(KeyDeliveryDeferral) shouldPerformKeyDeliveryRequestForKey:isPrefetchKey:isPersistable:isRenewal:completionHandler:]_block_invoke_4
+ ___86-[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:error:]_block_invoke
+ ___88-[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSAudioAssetMetadataDictionary:]_block_invoke
+ ___89-[AVURLAsset(MPCHLSSessionData) mpc_HLSSessionMetadataItemWithTimeout:completionHandler:]_block_invoke
+ ___89-[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTimeWithCompletionHandler:]_block_invoke
+ ___98-[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"AVMetadataItem"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0d8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___swift_closure_destructor.70Tm
+ _associated conformance 17MediaPlaybackCore23AudioSignatureProcessorV10SliceRange33_70D6E225C33896E6E4196C32A146759DLLVSHAASQ
+ _symbolic _____ 17MediaPlaybackCore23AudioSignatureProcessorV10SliceRange33_70D6E225C33896E6E4196C32A146759DLLV
+ _symbolic _____Iegr_ 17MediaPlaybackCore12PlayingStateC
+ _symbolic _____ySDy_____So11SHSignatureCGG 2os21OSAllocatedUnfairLockV 17MediaPlaybackCore23AudioSignatureProcessorV10SliceRange33_70D6E225C33896E6E4196C32A146759DLLV
+ _type_layout_string SNySdG
- -[AVURLAsset(MPCHLSSessionData) mpc_HLSAVMetadataItemInMetadata:]
- -[AVURLAsset(MPCHLSSessionData) mpc_synchronousHLSSessionDataWithTimeout:error:]
- -[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTime]
- -[MPCModelGenericAVItem(KeyDeliveryDeferral) sharedKeySegmentDuration]
- -[MPCPlayerItemConfigurator _HLSMetadataForAsset:error:]
- -[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSMetadata:]
- GCC_except_table3585
- GCC_except_table3606
- GCC_except_table3613
- GCC_except_table3638
- GCC_except_table3652
- GCC_except_table3709
- GCC_except_table3714
- GCC_except_table3788
- GCC_except_table3885
- GCC_except_table3900
- GCC_except_table3916
- GCC_except_table3922
- GCC_except_table3931
- GCC_except_table4059
- GCC_except_table4103
- GCC_except_table4104
- GCC_except_table4105
- GCC_except_table4125
- GCC_except_table4134
- GCC_except_table4152
- GCC_except_table4157
- GCC_except_table4159
- GCC_except_table4173
- GCC_except_table4196
- GCC_except_table4207
- GCC_except_table4296
- GCC_except_table4315
- GCC_except_table4328
- GCC_except_table4339
- GCC_except_table4370
- GCC_except_table4541
- GCC_except_table4542
- GCC_except_table4720
- GCC_except_table4755
- GCC_except_table4757
- GCC_except_table4765
- GCC_except_table4773
- GCC_except_table4788
- GCC_except_table4796
- GCC_except_table4804
- GCC_except_table4814
- GCC_except_table4829
- GCC_except_table4873
- GCC_except_table4888
- GCC_except_table4904
- GCC_except_table4913
- GCC_except_table4965
- GCC_except_table5003
- GCC_except_table5090
- GCC_except_table5191
- GCC_except_table5434
- GCC_except_table5435
- GCC_except_table5511
- GCC_except_table5603
- GCC_except_table5755
- GCC_except_table5780
- GCC_except_table5897
- GCC_except_table5978
- GCC_except_table5986
- GCC_except_table5987
- GCC_except_table6051
- GCC_except_table6076
- GCC_except_table6111
- GCC_except_table6114
- GCC_except_table6117
- GCC_except_table6203
- GCC_except_table6420
- GCC_except_table6437
- GCC_except_table6485
- GCC_except_table6498
- GCC_except_table7014
- GCC_except_table7348
- GCC_except_table7358
- GCC_except_table7452
- GCC_except_table7550
- GCC_except_table7557
- GCC_except_table7575
- GCC_except_table7626
- GCC_except_table7627
- GCC_except_table7630
- GCC_except_table7651
- ___68-[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSMetadata:]_block_invoke
- ___80-[AVURLAsset(MPCHLSSessionData) mpc_synchronousHLSSessionDataWithTimeout:error:]_block_invoke
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
CStrings:
+ "FIRST-SEGMENT-DURATION"
+ "Failed to decode HLS session data - Asset:%@"
+ "Failed to load HLS session metadata - Asset:%@"
+ "HLSSessionDataDecodingFailed"
+ "HLSSessionDataFetchTimedOut"
+ "HLSSessionDataUnavailable"
+ "MPCModelGenericAVItem+KeyDeliveryDeferral.m"
+ "No HLS session data available - Asset:%@"
+ "Playback queue superseded before response; re-requesting"
+ "SHARED-KEY-SEGMENT-COUNT"
+ "Timed out retrieving HLS session metadata - Asset:%@"
+ "Unexpected nil urlAsset"
+ "[%{public}@]-❗️MPCErrorControllerImplementation %p <%{public}@> - Ending playback [Item failed repeatedly]"
+ "[Chapter/ContentItem] Unable to convert chapter %{private,mask.hash}s to content item without a duration."
+ "[Chapters/%{private,mask.hash}s] Normalizing %{private,mask.hash}ld chapters with duration %{private,mask.hash}s."
+ "[Chapters/%{private,mask.hash}s] Segments changed, re-normalizing chapters with duration %{private,mask.hash}f."
+ "[Chapters/%{private,mask.hash}s] Unable to get duration for episode with %{private,mask.hash}s."
+ "[Chapters/%{private,mask.hash}s] Unable to get duration for episode with error %s."
+ "[Chapters] Finished chapter durations for minimum threshold."
+ "[Chapters] Removing chapter %{private,mask.hash}s."
+ "[Chapters] Verifying chapter durations for minimum threshold %f."
+ "[PL:%{public}s] STACK PROCESSING: setQueueWithInitialItem [new start item %{public}s] - isResend:%{bool,public}d - capturedIntent:%{bool,public}d - shouldPlay:%{bool,public}d"
+ "key-delivery-jitter-window"
+ "v24@?0@\"AVMetadataItem\"8@\"NSError\"16"
- "[%{public}@]-MPCErrorControllerImplementation %p <%{public}@> - Playback has succeeded for at least one item [Ignoring queue failure]"
- "[%{public}@]-MPCPlayerItemConfigurator %p - [AL] - Error decoding HLS metadata [Clearing audioFormatsDictionary] - Error:%{public}@"
- "[%{public}@]-❗️MPCErrorControllerImplementation %p <%{public}@> - Ending playback [Entire queue failure]"
- "[Chapters/%{private,mask.hash}s] Segments changed, re-normalizing chapters with duration %f."
- "[PL:%{public}s] STACK PROCESSING: setQueueWithInitialItem [new start item %{public}s]"
- "\xe1"
```
