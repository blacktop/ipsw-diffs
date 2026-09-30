## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-26200.26.36.301.0
-  __TEXT.__text: 0x482e84
-  __TEXT.__objc_methlist: 0x17ec0
+26200.26.37.501.0
+  __TEXT.__text: 0x4869d0
+  __TEXT.__objc_methlist: 0x17f30
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__const: 0x10870
-  __TEXT.__oslogstring: 0x4ca61
-  __TEXT.__cstring: 0x25d8d
-  __TEXT.__swift5_typeref: 0x546a
-  __TEXT.__swift5_capture: 0xaef8
+  __TEXT.__const: 0x109c0
+  __TEXT.__oslogstring: 0x4ce5f
+  __TEXT.__cstring: 0x25e6c
+  __TEXT.__swift5_typeref: 0x5486
+  __TEXT.__swift5_capture: 0xaf04
   __TEXT.__constg_swiftt: 0x7b40
-  __TEXT.__swift5_reflstr: 0x5a32
-  __TEXT.__swift5_fieldmd: 0x56a8
+  __TEXT.__swift5_reflstr: 0x5a42
+  __TEXT.__swift5_fieldmd: 0x56b4
   __TEXT.__swift5_builtin: 0x6f4
-  __TEXT.__swift5_mpenum: 0xf0
+  __TEXT.__swift5_mpenum: 0x130
   __TEXT.__swift5_assocty: 0xbc0
   __TEXT.__swift5_proto: 0x92c
   __TEXT.__swift5_types: 0x564

   __TEXT.__swift_as_cont: 0xe14
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x5a3c
+  __TEXT.__gcc_except_tab: 0x5a7c
   __TEXT.__ustring: 0x4dc
-  __TEXT.__unwind_info: 0x106a8
-  __TEXT.__eh_frame: 0x10294
+  __TEXT.__unwind_info: 0x106e0
+  __TEXT.__eh_frame: 0x102b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb98
+  __DATA_CONST.__objc_selrefs: 0xcbe8
   __DATA_CONST.__objc_protorefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x6d8
   __DATA_CONST.__objc_arraydata: 0x298
-  __DATA_CONST.__got: 0x3448
+  __DATA_CONST.__got: 0x3450
   __AUTH_CONST.__const: 0x238e0
-  __AUTH_CONST.__cfstring: 0x1eba0
-  __AUTH_CONST.__objc_const: 0x34898
-  __AUTH_CONST.__objc_intobj: 0x888
+  __AUTH_CONST.__cfstring: 0x1ec60
+  __AUTH_CONST.__objc_const: 0x34920
+  __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x3448
+  __AUTH_CONST.__objc_doubleobj: 0x60
+  __AUTH_CONST.__auth_got: 0x3440
   __AUTH.__objc_data: 0x5a40
   __AUTH.__data: 0x40c0
   __DATA.__objc_ivar: 0x1ad8
-  __DATA.__data: 0x7280
+  __DATA.__data: 0x72a0
   __DATA.__common: 0x240
   __DATA_DIRTY.__objc_data: 0x3590
-  __DATA_DIRTY.__data: 0x4548
+  __DATA_DIRTY.__data: 0x4558
   __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24485
-  Symbols:   24264
-  CStrings:  8271
+  Functions: 24532
+  Symbols:   24283
+  CStrings:  8280
 
Symbols:
+ -[MPCAudioAssetTypeSelector descriptionForExpectedAlbumAvailableDateTime:]
+ -[MPCAudioAssetTypeSelector preferredAudioAssetTypeForSongWithTrait:isStartItem:applyJitterTreatment:expectedAlbumAvailableDateTime:]
+ -[MPCAudioAssetTypeSelector stereoAssetTypeWithIsStartItem:applyJitterTreatment:explanation:]
+ -[MPCModelGenericAVItem _albumForPreReleaseTreatment]
+ -[MPCModelGenericAVItem _hasPendingDeferredLeaseAcquisition]
+ -[MPCModelGenericAVItem _setHasPendingDeferredLeaseAcquisition:]
+ -[MPCModelGenericAVItem expectedAlbumAvailableDateTime]
+ -[MPCModelGenericAVItem leaseAcquisitionJitterTime]
+ -[MPCModelGenericAVItem shouldApplyJitterTreatment]
+ -[_MPCPlaybackEnginePlayer _logTimeJumpForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:userInitiated:timeStamp:]
+ -[_MPCPlaybackEnginePlayer _playbackDidStopForItem:source:reason:time:primaryTime:timeStamp:]
+ -[_MPCPlaybackEnginePlayer userSeekCompletedForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:timeStamp:]
+ GCC_except_table3297
+ GCC_except_table3341
+ GCC_except_table3348
+ GCC_except_table3359
+ GCC_except_table3363
+ GCC_except_table3407
+ GCC_except_table3452
+ GCC_except_table3457
+ GCC_except_table3585
+ GCC_except_table3606
+ GCC_except_table3613
+ GCC_except_table3638
+ GCC_except_table3642
+ GCC_except_table3652
+ GCC_except_table3709
+ GCC_except_table3714
+ GCC_except_table3718
+ GCC_except_table3788
+ GCC_except_table3885
+ GCC_except_table3889
+ GCC_except_table3900
+ GCC_except_table3916
+ GCC_except_table3922
+ GCC_except_table3931
+ GCC_except_table4059
+ GCC_except_table4103
+ GCC_except_table4104
+ GCC_except_table4105
+ GCC_except_table4125
+ GCC_except_table4134
+ GCC_except_table4152
+ GCC_except_table4157
+ GCC_except_table4159
+ GCC_except_table4173
+ GCC_except_table4196
+ GCC_except_table4207
+ GCC_except_table4296
+ GCC_except_table4315
+ GCC_except_table4328
+ GCC_except_table4339
+ GCC_except_table4370
+ GCC_except_table4541
+ GCC_except_table4542
+ GCC_except_table4720
+ GCC_except_table4755
+ GCC_except_table4773
+ GCC_except_table4804
+ GCC_except_table4814
+ GCC_except_table4829
+ GCC_except_table4873
+ GCC_except_table4888
+ GCC_except_table4904
+ GCC_except_table4907
+ GCC_except_table4913
+ GCC_except_table4965
+ GCC_except_table5003
+ GCC_except_table5090
+ GCC_except_table5191
+ GCC_except_table5434
+ GCC_except_table5435
+ GCC_except_table5511
+ GCC_except_table5603
+ GCC_except_table5755
+ GCC_except_table5780
+ GCC_except_table5897
+ GCC_except_table5986
+ GCC_except_table5987
+ GCC_except_table6051
+ GCC_except_table6076
+ GCC_except_table6111
+ GCC_except_table6114
+ GCC_except_table6117
+ GCC_except_table6203
+ GCC_except_table6420
+ GCC_except_table6437
+ GCC_except_table6485
+ GCC_except_table6498
+ GCC_except_table7014
+ GCC_except_table7348
+ GCC_except_table7358
+ GCC_except_table7461
+ GCC_except_table7550
+ GCC_except_table7557
+ GCC_except_table7575
+ GCC_except_table7627
+ GCC_except_table7630
+ GCC_except_table7635
+ GCC_except_table7651
+ _MPCPlaybackEngineEventPayloadKeyInterstitialPrimaryPosition
+ _MPCPlaybackEngineEventPayloadKeyItemPrimaryEndPosition
+ _MPCPlaybackEngineEventPayloadKeyItemPrimaryStartPosition
+ _MPCPlaybackEngineEventPayloadKeyVideoRenderingModeDidChangePosition
+ _MPCPlaybackEngineEventPayloadKeyVideoRenderingModeDidChangePrimaryPosition
+ _MPModelPropertyAlbumExpectedReleaseDateComponents
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_4
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_5
+ _arc4random
+ _objc_msgSend$_albumForPreReleaseTreatment
+ _objc_msgSend$_hasPendingDeferredLeaseAcquisition
+ _objc_msgSend$_logTimeJumpForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:userInitiated:timeStamp:
+ _objc_msgSend$_playbackDidStopForItem:source:reason:time:primaryTime:timeStamp:
+ _objc_msgSend$_setHasPendingDeferredLeaseAcquisition:
+ _objc_msgSend$descriptionForExpectedAlbumAvailableDateTime:
+ _objc_msgSend$expectedAlbumAvailableDateTime
+ _objc_msgSend$expectedReleaseDateComponents
+ _objc_msgSend$isHomePodRoute
+ _objc_msgSend$leaseAcquisitionJitterTime
+ _objc_msgSend$preferredAudioAssetTypeForSongWithTrait:isStartItem:applyJitterTreatment:expectedAlbumAvailableDateTime:
+ _objc_msgSend$primaryTime
+ _objc_msgSend$shouldApplyJitterTreatment
+ _objc_msgSend$stereoAssetTypeWithIsStartItem:applyJitterTreatment:explanation:
+ _objc_msgSend$userSeekCompletedForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:timeStamp:
+ _symbolic Sb7success_______pSg4itemSdSg9startTimeAE012primaryStartD0Sd03endD0AE0e3EndD0SS10identifierSb7passive_____9timeStampt 17MediaPlaybackCore10PlayerItemP AA9EventTimeC
- -[MPCAudioAssetTypeSelector preferredAudioAssetTypeForSongWithTrait:isStartItem:]
- -[MPCAudioAssetTypeSelector stereoAssetTypeWithIsStartItem:explanation:]
- -[_MPCPlaybackEnginePlayer _logTimeJumpForItem:fromTime:toTime:userInitiated:timeStamp:]
- -[_MPCPlaybackEnginePlayer _playbackDidStopForItem:source:reason:time:timeStamp:]
- -[_MPCPlaybackEnginePlayer userSeekCompletedForItem:fromTime:toTime:timeStamp:]
- GCC_except_table3295
- GCC_except_table3337
- GCC_except_table3346
- GCC_except_table3357
- GCC_except_table3361
- GCC_except_table3399
- GCC_except_table3444
- GCC_except_table3449
- GCC_except_table3577
- GCC_except_table3598
- GCC_except_table3605
- GCC_except_table3630
- GCC_except_table3634
- GCC_except_table3644
- GCC_except_table3701
- GCC_except_table3706
- GCC_except_table3710
- GCC_except_table3780
- GCC_except_table3877
- GCC_except_table3881
- GCC_except_table3892
- GCC_except_table3908
- GCC_except_table3914
- GCC_except_table3923
- GCC_except_table4051
- GCC_except_table4095
- GCC_except_table4096
- GCC_except_table4097
- GCC_except_table4117
- GCC_except_table4126
- GCC_except_table4144
- GCC_except_table4149
- GCC_except_table4151
- GCC_except_table4165
- GCC_except_table4188
- GCC_except_table4199
- GCC_except_table4288
- GCC_except_table4307
- GCC_except_table4320
- GCC_except_table4331
- GCC_except_table4362
- GCC_except_table4533
- GCC_except_table4534
- GCC_except_table4712
- GCC_except_table4747
- GCC_except_table4749
- GCC_except_table4780
- GCC_except_table4806
- GCC_except_table4821
- GCC_except_table4865
- GCC_except_table4880
- GCC_except_table4896
- GCC_except_table4899
- GCC_except_table4905
- GCC_except_table4957
- GCC_except_table4995
- GCC_except_table5082
- GCC_except_table5183
- GCC_except_table5426
- GCC_except_table5427
- GCC_except_table5503
- GCC_except_table5595
- GCC_except_table5747
- GCC_except_table5772
- GCC_except_table5889
- GCC_except_table5970
- GCC_except_table5979
- GCC_except_table6043
- GCC_except_table6068
- GCC_except_table6103
- GCC_except_table6106
- GCC_except_table6109
- GCC_except_table6195
- GCC_except_table6412
- GCC_except_table6429
- GCC_except_table6477
- GCC_except_table6490
- GCC_except_table7006
- GCC_except_table7340
- GCC_except_table7350
- GCC_except_table7443
- GCC_except_table7541
- GCC_except_table7548
- GCC_except_table7566
- GCC_except_table7617
- GCC_except_table7618
- GCC_except_table7621
- GCC_except_table7642
- _OUTLINED_FUNCTION_620
- ___107-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern _locked_detectVersionHashMismatchIfNeeded:childKey:]_block_invoke
- ___block_descriptor_40_e8_32r_e14_v24?0{?=qiI}8lr32l8
- ___swift_memcpy72_8
- ___swift_memcpy73_8
- _objc_msgSend$_logTimeJumpForItem:fromTime:toTime:userInitiated:timeStamp:
- _objc_msgSend$_playbackDidStopForItem:source:reason:time:timeStamp:
- _objc_msgSend$preferredAudioAssetTypeForSongWithTrait:isStartItem:
- _objc_msgSend$stereoAssetTypeWithIsStartItem:explanation:
- _objc_msgSend$userSeekCompletedForItem:fromTime:toTime:timeStamp:
- _objc_release_x10
- _swift_retain_x11
- _symbolic Sb7success_______pSg4itemSdSg9startTimeSd03endD0SS10identifierSb7passive_____9timeStampt 17MediaPlaybackCore10PlayerItemP AA9EventTimeC
CStrings:
+ "4.AlbumAvailability"
+ "Forcing HLS to apply jitter treatment"
+ "[PIA] %p store resolved a different versionHash than requested [using store version] identifier=%{public}@ requestedVersionHash=%{public}@"
+ "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | populated section [store resolved a different versionHash than requested; using store version] progressiveSection=%{public}@ requestedVersionHash=%{public}@ relatedProgressiveResults.count=%ld"
+ "interstitial-primary-position"
+ "item-primary-end-position"
+ "item-primary-start-position"
+ "lease-acquisition"
+ "primaryStartTime"
+ "success item startTime primaryStartTime endTime primaryEndTime identifier passive timeStamp "
+ "video-rendering-mode-did-change-position"
+ "video-rendering-mode-did-change-primary-position"
+ "|%{public}@ %{public}@ %2i %{public}@  │ primaryEnd: %0.2f"
+ "|%{public}@ %{public}@ %2i %{public}@  │ primaryStart: %0.2f"
+ "|%{public}@ %{public}@ %2i %{public}@  ╰ primaryPosition: %0.2f"
- "AccumulationVersionHashUnavailable"
- "Store did not provide versionHash '%@' for container %@"
- "[PIA] %p failing request [requested versionHash unavailable after load] identifier=%{public}@ versionHash=%{public}@"
- "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | container has no children with any versionHash [treating as empty, not a versionHash mismatch] progressiveSection=%{public}@"
- "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | failing request [store cannot provide requested versionHash] progressiveSection=%{public}@ versionHash=%{public}@"
- "success item startTime endTime identifier passive timeStamp "
```
