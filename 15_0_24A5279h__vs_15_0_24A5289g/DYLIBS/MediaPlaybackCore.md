## MediaPlaybackCore

> `/System/iOSSupport/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore`

```diff

-24100.24.24.401.0
-  __TEXT.__text: 0x2e5b9c
+24100.24.26.401.0
+  __TEXT.__text: 0x2e6500
   __TEXT.__auth_stubs: 0x4b30
-  __TEXT.__objc_methlist: 0x11068
-  __TEXT.__const: 0x9a98
-  __TEXT.__gcc_except_tab: 0x581c
-  __TEXT.__oslogstring: 0x2b5cc
-  __TEXT.__cstring: 0x26992
+  __TEXT.__objc_methlist: 0x110b8
+  __TEXT.__const: 0x9ab8
+  __TEXT.__gcc_except_tab: 0x583c
+  __TEXT.__oslogstring: 0x2b5dc
+  __TEXT.__cstring: 0x269f2
   __TEXT.__ustring: 0x354
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__constg_swiftt: 0x5598
+  __TEXT.__constg_swiftt: 0x55d8
   __TEXT.__swift5_typeref: 0x3cd9
-  __TEXT.__swift5_reflstr: 0x330e
-  __TEXT.__swift5_fieldmd: 0x3434
+  __TEXT.__swift5_reflstr: 0x337e
+  __TEXT.__swift5_fieldmd: 0x3464
   __TEXT.__swift5_builtin: 0x5f0
   __TEXT.__swift5_assocty: 0xae0
   __TEXT.__swift5_proto: 0x6fc

   __TEXT.__swift5_mpenum: 0xcc
   __TEXT.__swift5_protos: 0xb4
   __TEXT.__swift5_capture: 0x2a88
-  __TEXT.__unwind_info: 0x94d8
-  __TEXT.__eh_frame: 0x67d4
+  __TEXT.__unwind_info: 0x9508
+  __TEXT.__eh_frame: 0x67f4
   __TEXT.__objc_classname: 0x3669
-  __TEXT.__objc_methname: 0x33c8e
-  __TEXT.__objc_methtype: 0x8ab5
-  __TEXT.__objc_stubs: 0x23460
-  __DATA_CONST.__got: 0x2928
-  __DATA_CONST.__const: 0x8b20
+  __TEXT.__objc_methname: 0x33d07
+  __TEXT.__objc_methtype: 0x8adf
+  __TEXT.__objc_stubs: 0x234a0
+  __DATA_CONST.__got: 0x2938
+  __DATA_CONST.__const: 0x8b18
   __DATA_CONST.__objc_classlist: 0xb58
   __DATA_CONST.__objc_catlist: 0x250
   __DATA_CONST.__objc_protolist: 0x708
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xace8
+  __DATA_CONST.__objc_selrefs: 0xad00
   __DATA_CONST.__objc_protorefs: 0x340
   __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x238
   __AUTH_CONST.__auth_got: 0x25a8
-  __AUTH_CONST.__auth_ptr: 0xa40
-  __AUTH_CONST.__const: 0xbb68
-  __AUTH_CONST.__cfstring: 0x1a260
-  __AUTH_CONST.__objc_const: 0x31330
+  __AUTH_CONST.__auth_ptr: 0x9e0
+  __AUTH_CONST.__const: 0xbba8
+  __AUTH_CONST.__cfstring: 0x1a240
+  __AUTH_CONST.__objc_const: 0x31480
   __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x80a0
-  __AUTH.__data: 0x4fd8
+  __AUTH.__objc_data: 0x80f0
+  __AUTH.__data: 0x4fe8
   __DATA.__objc_ivar: 0x17a0
-  __DATA.__data: 0x64b0
+  __DATA.__data: 0x64e0
   __DATA.__bss: 0xc7d0
   __DATA.__common: 0x198
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15153
-  Symbols:   22849
-  CStrings:  5038
+  Functions: 15170
+  Symbols:   22865
+  CStrings:  5042
 
Symbols:
+ -[MPAVItem(MFQueuePlayerItem) activeFormat]
+ -[MPCAssetLoader _configureItem:playerItem:error:]
+ -[MPCPlayerItemConfigurator _setupQueueItemForEnhancedAudioHLSPlayback:playerItem:metadataWaitTime:error:]
+ -[MPCPlayerItemConfigurator _setupQueueItemForHLSPlayback:playerItem:]
+ -[MPCPlayerItemConfigurator _setupQueueItemForLossyAudioPlayback:playerItem:]
+ -[MPCPlayerItemConfigurator configureQueueItem:playerItem:error:]
+ -[MPCPlayerResponse prepare]
+ -[_MPCPlayerSeekCommand changePositionToElapsedInterval:referenceInterval:]
+ -[_MPCQueueControllerBehaviorEmpty isEmpty]
+ -[_MPCQueueControllerBehaviorMusic isEmpty]
+ -[_MPCQueueControllerBehaviorMusicSharePlay isEmpty]
+ GCC_except_table132
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table61
+ GCC_except_table82
+ GCC_except_table85
+ _OUTLINED_FUNCTION_116
+ __123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.605
+ __34-[MPCQueueController _commitEdit:]_block_invoke.362
+ __36-[MPCQueueController _rollbackEdit:]_block_invoke.365
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.358
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.363
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.365
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.395
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.432
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.496
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.540
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.550
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.583
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.607
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.627
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.628
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.635
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.639
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.646
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.655
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.670
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_10.520
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_11.530
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.364
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.373
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.402
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.440
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.497
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.547
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.554
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.596
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.608
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.631
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.444
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.501
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.558
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.611
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.449
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.502
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.613
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.461
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.506
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.465
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.513
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.469
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.514
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.476
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.518
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.480
+ __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.519
+ __62-[MPCQueueController _evaluateContextAwareTriggersWithReason:]_block_invoke.391
+ __62-[MPCQueueController _evaluateContextAwareTriggersWithReason:]_block_invoke.395
+ __65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.680
+ __76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.627
+ ___block_descriptor_32_e66_"MPCSharedSessionParticipant"16?0"<MRGroupSessionParticipant>"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e30_v16?0"MPCPlayerAudioFormat"8ls32l8s40l8s48l8s56l8
+ ___unnamed_12
+ __block_literal_global.1114
+ __block_literal_global.317
+ __block_literal_global.364
+ __block_literal_global.367
+ __block_literal_global.398
+ __block_literal_global.451
+ __block_literal_global.549
+ __block_literal_global.552
+ __block_literal_global.610
+ __block_literal_global.630
+ __block_literal_global.683
+ __block_literal_global.686
+ __block_literal_global.708
+ __block_literal_global.833
+ _kMRMediaRemoteCommandInfoSupportsReferencePosition
+ _kMRMediaRemoteOptionReferencePosition
+ _objc_msgSend$_configureItem:playerItem:error:
+ _objc_msgSend$_setupQueueItemForEnhancedAudioHLSPlayback:playerItem:metadataWaitTime:error:
+ _objc_msgSend$_setupQueueItemForHLSPlayback:playerItem:
+ _objc_msgSend$_setupQueueItemForLossyAudioPlayback:playerItem:
+ _objc_msgSend$activeFormatDidChangeFor:
+ _objc_msgSend$configureQueueItem:playerItem:error:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$setSupportsReferencePosition:
+ block_copy_helper.100
+ block_copy_helper.121
+ block_copy_helper.125
+ block_copy_helper.128
+ block_copy_helper.141
+ block_copy_helper.146
+ block_copy_helper.150
+ block_copy_helper.157
+ block_copy_helper.164
+ block_copy_helper.168
+ block_copy_helper.175
+ block_copy_helper.183
+ block_copy_helper.192
+ block_copy_helper.208
+ block_copy_helper.83
+ block_descriptor.102
+ block_descriptor.123
+ block_descriptor.127
+ block_descriptor.130
+ block_descriptor.143
+ block_descriptor.148
+ block_descriptor.152
+ block_descriptor.159
+ block_descriptor.166
+ block_descriptor.170
+ block_descriptor.177
+ block_descriptor.185
+ block_descriptor.194
+ block_descriptor.210
+ block_descriptor.85
+ block_destroy_helper.101
+ block_destroy_helper.122
+ block_destroy_helper.126
+ block_destroy_helper.129
+ block_destroy_helper.142
+ block_destroy_helper.147
+ block_destroy_helper.151
+ block_destroy_helper.158
+ block_destroy_helper.165
+ block_destroy_helper.169
+ block_destroy_helper.176
+ block_destroy_helper.184
+ block_destroy_helper.193
+ block_destroy_helper.209
+ block_destroy_helper.84
+ objectdestroy.123Tm
+ objectdestroy.47Tm
+ objectdestroy.72Tm
+ objectdestroy.81Tm
- -[MPCAssetLoader _configureItem:error:]
- -[MPCPlayerItemConfigurator _setupQueueItemForEnhancedAudioHLSPlayback:metadataWaitTime:error:]
- -[MPCPlayerItemConfigurator _setupQueueItemForHLSPlayback:]
- -[MPCPlayerItemConfigurator _setupQueueItemForLossyAudioPlayback:]
- -[MPCPlayerItemConfigurator configureQueuePlayerItem:error:]
- -[_MPCQueueControllerBehaviorMusic _mpcParticipantForGroupSessionParticipant:]
- GCC_except_table100
- GCC_except_table131
- GCC_except_table162
- GCC_except_table163
- GCC_except_table60
- GCC_except_table87
- __123-[_MPCQueueControllerBehaviorMusic _addPlaybackContext:atPosition:afterContentItemID:sectionIdentifier:actions:completion:]_block_invoke.610
- __34-[MPCQueueController _commitEdit:]_block_invoke.360
- __36-[MPCQueueController _rollbackEdit:]_block_invoke.363
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.355
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.360
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.362
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.392
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.429
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.493
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.534
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.544
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.577
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.601
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.621
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.622
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.629
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.633
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.640
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.649
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.664
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_10.517
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_11.524
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.361
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.370
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.399
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.437
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.494
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.541
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.548
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.590
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.602
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.625
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.441
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.498
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.552
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.605
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.446
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.499
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.607
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.458
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.503
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.462
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.510
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.466
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.511
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.473
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.515
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.477
- __60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.516
- __62-[MPCQueueController _evaluateContextAwareTriggersWithReason:]_block_invoke.389
- __62-[MPCQueueController _evaluateContextAwareTriggersWithReason:]_block_invoke.393
- __65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.674
- __76-[_MPCQueueControllerBehaviorMusic _evaluateLoadingDataSourceItemThresholds]_block_invoke.632
- ___block_descriptor_40_e8_32s_e66_"MPCSharedSessionParticipant"16?0"<MRGroupSessionParticipant>"8ls32l8
- ___block_descriptor_56_e8_32s40s48s_e30_v16?0"MPCPlayerAudioFormat"8ls32l8s40l8s48l8
- ___unnamed_11
- __block_literal_global.1112
- __block_literal_global.314
- __block_literal_global.362
- __block_literal_global.365
- __block_literal_global.395
- __block_literal_global.448
- __block_literal_global.543
- __block_literal_global.546
- __block_literal_global.599
- __block_literal_global.604
- __block_literal_global.624
- __block_literal_global.706
- __block_literal_global.831
- _objc_msgSend$_configureItem:error:
- _objc_msgSend$_mpcParticipantForGroupSessionParticipant:
- _objc_msgSend$_setupQueueItemForEnhancedAudioHLSPlayback:metadataWaitTime:error:
- _objc_msgSend$_setupQueueItemForHLSPlayback:
- _objc_msgSend$_setupQueueItemForLossyAudioPlayback:
- _objc_msgSend$configureQueuePlayerItem:error:
- block_copy_helper.120
- block_copy_helper.123
- block_copy_helper.127
- block_copy_helper.138
- block_copy_helper.144
- block_copy_helper.148
- block_copy_helper.155
- block_copy_helper.162
- block_copy_helper.166
- block_copy_helper.173
- block_copy_helper.181
- block_copy_helper.190
- block_copy_helper.206
- block_copy_helper.82
- block_copy_helper.99
- block_descriptor.101
- block_descriptor.122
- block_descriptor.125
- block_descriptor.129
- block_descriptor.140
- block_descriptor.146
- block_descriptor.150
- block_descriptor.157
- block_descriptor.164
- block_descriptor.168
- block_descriptor.175
- block_descriptor.183
- block_descriptor.192
- block_descriptor.208
- block_descriptor.84
- block_destroy_helper.100
- block_destroy_helper.121
- block_destroy_helper.124
- block_destroy_helper.128
- block_destroy_helper.139
- block_destroy_helper.145
- block_destroy_helper.149
- block_destroy_helper.156
- block_destroy_helper.163
- block_destroy_helper.167
- block_destroy_helper.174
- block_destroy_helper.182
- block_destroy_helper.191
- block_destroy_helper.207
- block_destroy_helper.83
- objectdestroy.121Tm
- objectdestroy.46Tm
- objectdestroy.71Tm
- objectdestroy.80Tm
CStrings:
+ "%!@(MISSING) behavior"
+ "<MISSING REASON>"
+ "@\"MPCPlayerAudioFormat\"16@0:8"
+ "behavior has no items"
+ "isEmpty"
+ "isEnabled"
+ "nextItemTrackChangesPublisher"
+ "nextItemTracksChangeSubscription"
+ "unsupported command [%!@(MISSING) behavior]"
- "Asset is not loaded"
- "MPCPlayerItemConfigurator.m"
- "non-music behavior[%!@(MISSING)]"
- "queueItem.isAssetLoaded"
- "uninitialized music behavior"

```
