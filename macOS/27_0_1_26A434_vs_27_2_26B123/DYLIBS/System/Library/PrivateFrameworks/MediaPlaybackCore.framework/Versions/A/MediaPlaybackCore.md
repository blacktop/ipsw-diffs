## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/Versions/A/MediaPlaybackCore`

```diff

-26140.26.31.301.0
-  __TEXT.__text: 0x3cd644
-  __TEXT.__objc_methlist: 0x164e0
+26240.26.40.301.0
+  __TEXT.__text: 0x3d43f0
+  __TEXT.__objc_methlist: 0x165f8
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__const: 0xd880
-  __TEXT.__cstring: 0x230c7
-  __TEXT.__constg_swiftt: 0x65f8
-  __TEXT.__swift5_typeref: 0x462a
+  __TEXT.__const: 0xd9b0
+  __TEXT.__cstring: 0x235c5
+  __TEXT.__constg_swiftt: 0x6668
+  __TEXT.__swift5_typeref: 0x4642
   __TEXT.__swift5_builtin: 0x578
-  __TEXT.__swift5_reflstr: 0x4972
-  __TEXT.__swift5_fieldmd: 0x4824
+  __TEXT.__swift5_reflstr: 0x4a52
+  __TEXT.__swift5_fieldmd: 0x486c
   __TEXT.__swift5_assocty: 0xa20
-  __TEXT.__oslogstring: 0x41d88
+  __TEXT.__oslogstring: 0x421d7
   __TEXT.__swift5_proto: 0x7a8
   __TEXT.__swift5_types: 0x44c
-  __TEXT.__swift5_capture: 0x6514
+  __TEXT.__swift5_capture: 0x67e4
   __TEXT.__swift_as_entry: 0x2c0
-  __TEXT.__swift_as_ret: 0x320
-  __TEXT.__swift_as_cont: 0x8ac
-  __TEXT.__swift5_mpenum: 0xb8
+  __TEXT.__swift_as_ret: 0x324
+  __TEXT.__swift_as_cont: 0x8b4
+  __TEXT.__swift5_mpenum: 0xf8
   __TEXT.__swift5_protos: 0xc4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x560c
+  __TEXT.__gcc_except_tab: 0x56f0
   __TEXT.__ustring: 0x4d4
-  __TEXT.__unwind_info: 0xac28
-  __TEXT.__eh_frame: 0x9d80
+  __TEXT.__unwind_info: 0xaca0
+  __TEXT.__eh_frame: 0x9cd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c08
+  __DATA_CONST.__const: 0x2c30
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x280
   __DATA_CONST.__objc_protolist: 0x6c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf40
+  __DATA_CONST.__objc_selrefs: 0xc000
   __DATA_CONST.__objc_protorefs: 0x2c8
-  __DATA_CONST.__objc_superrefs: 0x6b0
-  __DATA_CONST.__objc_arraydata: 0x290
-  __DATA_CONST.__got: 0x2a68
-  __AUTH_CONST.__const: 0x1e4a0
-  __AUTH_CONST.__cfstring: 0x1dea0
-  __AUTH_CONST.__objc_const: 0x30b40
-  __AUTH_CONST.__objc_intobj: 0x888
-  __AUTH_CONST.__objc_arrayobj: 0x288
+  __DATA_CONST.__objc_superrefs: 0x6b8
+  __DATA_CONST.__objc_arraydata: 0x288
+  __DATA_CONST.__got: 0x2a80
+  __AUTH_CONST.__const: 0x1ed00
+  __AUTH_CONST.__cfstring: 0x1e240
+  __AUTH_CONST.__objc_const: 0x30d88
+  __AUTH_CONST.__objc_intobj: 0x8a0
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_doubleobj: 0x60
+  __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_got: 0x26f8
   __AUTH_CONST.__auth_ptr: 0xba8
   __AUTH.__objc_data: 0x4808
-  __AUTH.__data: 0x1ef0
-  __DATA.__objc_ivar: 0x1a34
+  __AUTH.__data: 0x1f10
+  __DATA.__objc_ivar: 0x1a4c
   __DATA.__data: 0x56d0
   __DATA.__bss: 0xc018
   __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x3100
-  __DATA_DIRTY.__data: 0x5ba8
+  __DATA_DIRTY.__data: 0x5c18
   __DATA_DIRTY.__bss: 0x1b30
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19133
-  Symbols:   22781
-  CStrings:  7558
+  Functions: 19266
+  Symbols:   22856
+  CStrings:  7600
 
Symbols:
+ +[MPCAssistantRemoteControlDestination companionLocalFallbackPolicy]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:completionHandler:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:error:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSMetadataItemInMetadata:]
+ -[AVURLAsset(MPCHLSSessionData) mpc_HLSSessionMetadataItemWithTimeout:completionHandler:]
+ -[MPCAudioAssetTypeSelector descriptionForExpectedAlbumAvailableDateTime:]
+ -[MPCAudioAssetTypeSelector preferredAudioAssetTypeForSongWithTrait:isStartItem:applyJitterTreatment:expectedAlbumAvailableDateTime:]
+ -[MPCAudioAssetTypeSelector stereoAssetTypeWithIsStartItem:applyJitterTreatment:explanation:]
+ -[MPCFuture _removeInvalidHandler:]
+ -[MPCFuture invalidHandlers]
+ -[MPCFutureInvalidationToken dealloc]
+ -[MPCFutureInvalidationToken handler]
+ -[MPCFutureInvalidationToken setHandler:]
+ -[MPCModelGenericAVItem _albumForPreReleaseTreatment]
+ -[MPCModelGenericAVItem _hasPendingDeferredLeaseAcquisition]
+ -[MPCModelGenericAVItem _setHasPendingDeferredLeaseAcquisition:]
+ -[MPCModelGenericAVItem expectedAlbumAvailableDateTime]
+ -[MPCModelGenericAVItem leaseAcquisitionJitterTime]
+ -[MPCModelGenericAVItem shouldApplyJitterTreatment]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) _sharedKeySegmentDurationFromHLSSessionDataOfAsset:completionHandler:]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTimeWithCompletionHandler:]
+ -[MPCModelGenericAVItem(KeyDeliveryDeferral) sharedKeySegmentDurationWithCompletionHandler:]
+ -[MPCModelStorePlaybackItemsRequest setVersionHashesByStoreID:]
+ -[MPCModelStorePlaybackItemsRequest versionHashesByStoreID]
+ -[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]
+ -[MPCPlaybackErrorController playbackDidSucceedForItem:]
+ -[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSAudioAssetMetadataDictionary:]
+ -[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]
+ -[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]
+ -[_MPCPlaybackEnginePlayer _logTimeJumpForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:userInitiated:timeStamp:]
+ -[_MPCPlaybackEnginePlayer _playbackDidStopForItem:source:reason:time:primaryTime:timeStamp:]
+ -[_MPCPlaybackEnginePlayer userSeekCompletedForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:timeStamp:]
+ -[_MPCVideoLayerOutput customControlItems]
+ -[_MPCVideoLayerOutput setCustomControlItems:]
+ GCC_except_table1011
+ GCC_except_table1013
+ GCC_except_table1020
+ GCC_except_table1022
+ GCC_except_table1035
+ GCC_except_table1039
+ GCC_except_table1045
+ GCC_except_table1051
+ GCC_except_table1054
+ GCC_except_table1057
+ GCC_except_table1246
+ GCC_except_table1250
+ GCC_except_table1252
+ GCC_except_table1420
+ GCC_except_table1424
+ GCC_except_table1468
+ GCC_except_table1479
+ GCC_except_table1486
+ GCC_except_table1493
+ GCC_except_table1530
+ GCC_except_table1542
+ GCC_except_table1551
+ GCC_except_table1594
+ GCC_except_table1767
+ GCC_except_table1769
+ GCC_except_table1787
+ GCC_except_table1857
+ GCC_except_table1942
+ GCC_except_table1943
+ GCC_except_table2057
+ GCC_except_table2077
+ GCC_except_table2079
+ GCC_except_table2107
+ GCC_except_table2118
+ GCC_except_table2126
+ GCC_except_table2129
+ GCC_except_table2140
+ GCC_except_table2150
+ GCC_except_table2266
+ GCC_except_table2317
+ GCC_except_table2321
+ GCC_except_table2324
+ GCC_except_table2352
+ GCC_except_table2376
+ GCC_except_table2409
+ GCC_except_table2650
+ GCC_except_table2678
+ GCC_except_table2705
+ GCC_except_table2850
+ GCC_except_table2878
+ GCC_except_table2879
+ GCC_except_table2906
+ GCC_except_table2911
+ GCC_except_table2915
+ GCC_except_table2919
+ GCC_except_table2921
+ GCC_except_table2924
+ GCC_except_table2961
+ GCC_except_table2966
+ GCC_except_table2972
+ GCC_except_table2978
+ GCC_except_table2983
+ GCC_except_table2986
+ GCC_except_table2989
+ GCC_except_table3009
+ GCC_except_table3059
+ GCC_except_table3145
+ GCC_except_table3149
+ GCC_except_table3160
+ GCC_except_table3161
+ GCC_except_table3185
+ GCC_except_table3197
+ GCC_except_table3243
+ GCC_except_table3253
+ GCC_except_table3310
+ GCC_except_table3328
+ GCC_except_table3337
+ GCC_except_table3378
+ GCC_except_table3382
+ GCC_except_table3403
+ GCC_except_table3407
+ GCC_except_table3457
+ GCC_except_table3502
+ GCC_except_table3507
+ GCC_except_table3648
+ GCC_except_table3655
+ GCC_except_table3682
+ GCC_except_table3686
+ GCC_except_table3696
+ GCC_except_table3753
+ GCC_except_table3760
+ GCC_except_table3764
+ GCC_except_table3835
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table3938
+ GCC_except_table3942
+ GCC_except_table3954
+ GCC_except_table3970
+ GCC_except_table3977
+ GCC_except_table3987
+ GCC_except_table4115
+ GCC_except_table4162
+ GCC_except_table4163
+ GCC_except_table4182
+ GCC_except_table4193
+ GCC_except_table4211
+ GCC_except_table4216
+ GCC_except_table4218
+ GCC_except_table4254
+ GCC_except_table4266
+ GCC_except_table4355
+ GCC_except_table4374
+ GCC_except_table4389
+ GCC_except_table4398
+ GCC_except_table4429
+ GCC_except_table446
+ GCC_except_table454
+ GCC_except_table4600
+ GCC_except_table4601
+ GCC_except_table464
+ GCC_except_table475
+ GCC_except_table4780
+ GCC_except_table4815
+ GCC_except_table4817
+ GCC_except_table4825
+ GCC_except_table4833
+ GCC_except_table4849
+ GCC_except_table4871
+ GCC_except_table4882
+ GCC_except_table4895
+ GCC_except_table4942
+ GCC_except_table4956
+ GCC_except_table4973
+ GCC_except_table4978
+ GCC_except_table4984
+ GCC_except_table5029
+ GCC_except_table5064
+ GCC_except_table5148
+ GCC_except_table5505
+ GCC_except_table559
+ GCC_except_table5607
+ GCC_except_table575
+ GCC_except_table5757
+ GCC_except_table576
+ GCC_except_table5782
+ GCC_except_table592
+ GCC_except_table593
+ GCC_except_table5954
+ GCC_except_table6020
+ GCC_except_table6045
+ GCC_except_table6080
+ GCC_except_table6083
+ GCC_except_table6086
+ GCC_except_table6172
+ GCC_except_table6389
+ GCC_except_table6406
+ GCC_except_table6857
+ GCC_except_table7201
+ GCC_except_table7216
+ GCC_except_table7307
+ GCC_except_table7316
+ GCC_except_table7405
+ GCC_except_table7412
+ GCC_except_table7430
+ GCC_except_table7481
+ GCC_except_table7482
+ GCC_except_table7485
+ GCC_except_table7490
+ GCC_except_table7506
+ GCC_except_table844
+ GCC_except_table900
+ GCC_except_table976
+ OBJC_IVAR_$_MPCFuture._invalidHandlers
+ OBJC_IVAR_$_MPCFutureInvalidationToken._handler
+ OBJC_IVAR_$_MPCModelStorePlaybackItemsRequest._versionHashesByStoreID
+ OBJC_IVAR_$_MPCPlaybackAccountManager._accountsUpdateQueue
+ OBJC_IVAR_$__MPCMediaRemotePublisher._hostingSharedSessionIDInitialized
+ OBJC_IVAR_$__MPCModelStorePlaybackItemsRequestAccumulator_Legacy._hasHandledStoreResponse
+ OBJC_IVAR_$__MPCVideoLayerOutput.customControlItems
+ _MPCHLSAudioAssetMetadataDictionaryKey
+ _MPCPlaybackEngineEventPayloadKeyInterstitialPrimaryPosition
+ _MPCPlaybackEngineEventPayloadKeyItemPrimaryEndPosition
+ _MPCPlaybackEngineEventPayloadKeyItemPrimaryStartPosition
+ _MPCPlaybackEngineEventPayloadKeyVideoRenderingModeDidChangePosition
+ _MPCPlaybackEngineEventPayloadKeyVideoRenderingModeDidChangePrimaryPosition
+ _MPHomeMonitorCurrentHomeDidChangeNotification
+ _MPHomeMonitorHomeUsersDidChangeNotification
+ _MPModelPropertyAlbumExpectedReleaseDateComponents
+ _OBJC_CLASS_$_NSPointerArray
+ _OUTLINED_FUNCTION_468
+ _OUTLINED_FUNCTION_469
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke
+ __101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ __119-[MPCAssistantRemoteControlDestination resolveWithRouteIdentifiers:allowedPlaybackTargets:audioRoutingInfo:completion:]_block_invoke
+ __140-[MPCModelGenericAVItem(KeyDeliveryDeferral) shouldPerformKeyDeliveryRequestForKey:isPrefetchKey:isPersistable:isRenewal:completionHandler:]_block_invoke_2
+ __89-[AVURLAsset(MPCHLSSessionData) mpc_HLSSessionMetadataItemWithTimeout:completionHandler:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:account:]_block_invoke_3
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern _locked_progressiveSectionWithoutVersionHash:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_2
+ ___101-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:account:]_block_invoke_3
+ ___115-[MPCModelGenericAVItem(KeyDeliveryDeferral) _sharedKeySegmentDurationFromHLSSessionDataOfAsset:completionHandler:]_block_invoke
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_2
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_3
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_4
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_5
+ ___175-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:]_block_invoke_6
+ ___35-[MPCFuture _removeInvalidHandler:]_block_invoke
+ ___36+[MPCPlaybackEngine preheatPlayback]_block_invoke_2
+ ___57-[MPCPlaybackAccountManager performAfterLoadingAccounts:]_block_invoke
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_4
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_5
+ ___86-[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:error:]_block_invoke
+ ___88-[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSAudioAssetMetadataDictionary:]_block_invoke
+ ___89-[AVURLAsset(MPCHLSSessionData) mpc_HLSSessionMetadataItemWithTimeout:completionHandler:]_block_invoke
+ ___89-[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTimeWithCompletionHandler:]_block_invoke
+ ___98-[AVURLAsset(MPCHLSSessionData) mpc_HLSAudioAssetMetadataDictionaryWithTimeout:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"AVMetadataItem"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0d8l
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0q8l
+ ___block_descriptor_48_e8_32s40bs_e9_v16?0^v8l
+ ___block_descriptor_49_e8_32s40s_e18_16?0"NSString"8l
+ ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_61_e8_32s40s48s_e49_v16?0"MPIdentifierSet<MPMutableIdentifierSet>"8l
+ ___unnamed_10
+ __swift_closure_destructor.70Tm
+ _arc4random
+ _objc_msgSend$_albumForPreReleaseTreatment
+ _objc_msgSend$_audioFormatsDictionaryWithHLSAudioAssetMetadataDictionary:
+ _objc_msgSend$_hasPendingDeferredLeaseAcquisition
+ _objc_msgSend$_logTimeJumpForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:userInitiated:timeStamp:
+ _objc_msgSend$_playbackDidStopForItem:source:reason:time:primaryTime:timeStamp:
+ _objc_msgSend$_removeInvalidHandler:
+ _objc_msgSend$_setHasPendingDeferredLeaseAcquisition:
+ _objc_msgSend$_sharedKeySegmentDurationFromHLSSessionDataOfAsset:completionHandler:
+ _objc_msgSend$addPointer:
+ _objc_msgSend$descriptionForExpectedAlbumAvailableDateTime:
+ _objc_msgSend$expectedAlbumAvailableDateTime
+ _objc_msgSend$expectedReleaseDateComponents
+ _objc_msgSend$initWithProgressiveResults:properties:personalizationProperties:serverObjectDatabase:libraryObjectDatabase:performanceMetrics:
+ _objc_msgSend$initWithRequest:serverObjectDatabase:account:
+ _objc_msgSend$isHomePodRoute
+ _objc_msgSend$keyDeliveryJitterTimeWithCompletionHandler:
+ _objc_msgSend$leaseAcquisitionJitterTime
+ _objc_msgSend$loadMetadataForFormat:completionHandler:
+ _objc_msgSend$mpc_HLSAudioAssetMetadataDictionaryWithTimeout:completionHandler:
+ _objc_msgSend$mpc_HLSAudioAssetMetadataDictionaryWithTimeout:error:
+ _objc_msgSend$mpc_HLSMetadataItemInMetadata:
+ _objc_msgSend$mpc_HLSSessionMetadataItemWithTimeout:completionHandler:
+ _objc_msgSend$playbackDidSucceedForItem:
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$preferredAudioAssetTypeForSongWithTrait:isStartItem:applyJitterTreatment:expectedAlbumAvailableDateTime:
+ _objc_msgSend$primaryTime
+ _objc_msgSend$replacePointerAtIndex:withPointer:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$setupIfNecessary
+ _objc_msgSend$sharedKeySegmentDurationWithCompletionHandler:
+ _objc_msgSend$shouldApplyJitterTreatment
+ _objc_msgSend$stereoAssetTypeWithIsStartItem:applyJitterTreatment:explanation:
+ _objc_msgSend$strongObjectsPointerArray
+ _objc_msgSend$tokenForDatabase:
+ _objc_msgSend$userSeekCompletedForItem:fromTime:fromPrimaryTime:toTime:toPrimaryTime:timeStamp:
+ _objc_msgSend$versionHashesByStoreID
+ _symbolic Sb7success_______pSg4itemSdSg9startTimeAE012primaryStartD0Sd03endD0AE0e3EndD0SS10identifierSb7passive_____9timeStampt 17MediaPlaybackCore10PlayerItemP AA9EventTimeC
+ _symbolic _____Iegr_ 17MediaPlaybackCore12PlayingStateC
- -[AVURLAsset(MPCHLSSessionData) mpc_HLSAVMetadataItemInMetadata:]
- -[AVURLAsset(MPCHLSSessionData) mpc_synchronousHLSSessionDataWithTimeout:error:]
- -[MPCAudioAssetTypeSelector preferredAudioAssetTypeForSongWithTrait:isStartItem:]
- -[MPCAudioAssetTypeSelector stereoAssetTypeWithIsStartItem:explanation:]
- -[MPCFuture invalidBlocks]
- -[MPCModelGenericAVItem(KeyDeliveryDeferral) keyDeliveryJitterTime]
- -[MPCModelGenericAVItem(KeyDeliveryDeferral) sharedKeySegmentDuration]
- -[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]
- -[MPCPlayerItemConfigurator _HLSMetadataForAsset:error:]
- -[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSMetadata:]
- -[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]
- -[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]
- -[_MPCPlaybackEnginePlayer _logTimeJumpForItem:fromTime:toTime:userInitiated:timeStamp:]
- -[_MPCPlaybackEnginePlayer _playbackDidStopForItem:source:reason:time:timeStamp:]
- -[_MPCPlaybackEnginePlayer userSeekCompletedForItem:fromTime:toTime:timeStamp:]
- GCC_except_table1003
- GCC_except_table1006
- GCC_except_table1015
- GCC_except_table1017
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1040
- GCC_except_table1046
- GCC_except_table1049
- GCC_except_table1052
- GCC_except_table1241
- GCC_except_table1245
- GCC_except_table1247
- GCC_except_table1415
- GCC_except_table1419
- GCC_except_table1463
- GCC_except_table1474
- GCC_except_table1481
- GCC_except_table1488
- GCC_except_table1525
- GCC_except_table1537
- GCC_except_table1546
- GCC_except_table1589
- GCC_except_table1762
- GCC_except_table1764
- GCC_except_table1777
- GCC_except_table1852
- GCC_except_table1937
- GCC_except_table1938
- GCC_except_table2052
- GCC_except_table2072
- GCC_except_table2074
- GCC_except_table2102
- GCC_except_table2113
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2135
- GCC_except_table2145
- GCC_except_table2261
- GCC_except_table2312
- GCC_except_table2316
- GCC_except_table2319
- GCC_except_table2347
- GCC_except_table2371
- GCC_except_table2404
- GCC_except_table2645
- GCC_except_table2673
- GCC_except_table2700
- GCC_except_table2843
- GCC_except_table2864
- GCC_except_table2872
- GCC_except_table2897
- GCC_except_table2899
- GCC_except_table2908
- GCC_except_table2910
- GCC_except_table2912
- GCC_except_table2914
- GCC_except_table2945
- GCC_except_table2957
- GCC_except_table2959
- GCC_except_table2963
- GCC_except_table2969
- GCC_except_table2974
- GCC_except_table2980
- GCC_except_table3000
- GCC_except_table3050
- GCC_except_table3136
- GCC_except_table3140
- GCC_except_table3151
- GCC_except_table3152
- GCC_except_table3176
- GCC_except_table3188
- GCC_except_table3234
- GCC_except_table3235
- GCC_except_table3301
- GCC_except_table3319
- GCC_except_table3326
- GCC_except_table3367
- GCC_except_table3371
- GCC_except_table3381
- GCC_except_table3396
- GCC_except_table3440
- GCC_except_table3485
- GCC_except_table3490
- GCC_except_table3606
- GCC_except_table3634
- GCC_except_table3661
- GCC_except_table3665
- GCC_except_table3675
- GCC_except_table3732
- GCC_except_table3739
- GCC_except_table3743
- GCC_except_table3814
- GCC_except_table387
- GCC_except_table389
- GCC_except_table3917
- GCC_except_table3921
- GCC_except_table3933
- GCC_except_table3949
- GCC_except_table3956
- GCC_except_table3966
- GCC_except_table4094
- GCC_except_table4139
- GCC_except_table4140
- GCC_except_table4141
- GCC_except_table4172
- GCC_except_table4190
- GCC_except_table4195
- GCC_except_table4197
- GCC_except_table4233
- GCC_except_table4245
- GCC_except_table4334
- GCC_except_table4353
- GCC_except_table4368
- GCC_except_table4377
- GCC_except_table4408
- GCC_except_table442
- GCC_except_table450
- GCC_except_table4579
- GCC_except_table4580
- GCC_except_table460
- GCC_except_table471
- GCC_except_table4759
- GCC_except_table4794
- GCC_except_table4796
- GCC_except_table4804
- GCC_except_table4812
- GCC_except_table4828
- GCC_except_table4840
- GCC_except_table4850
- GCC_except_table4874
- GCC_except_table4921
- GCC_except_table4936
- GCC_except_table4953
- GCC_except_table4958
- GCC_except_table4964
- GCC_except_table5009
- GCC_except_table5044
- GCC_except_table5127
- GCC_except_table5482
- GCC_except_table554
- GCC_except_table5583
- GCC_except_table570
- GCC_except_table571
- GCC_except_table5733
- GCC_except_table5758
- GCC_except_table587
- GCC_except_table588
- GCC_except_table5930
- GCC_except_table5996
- GCC_except_table6021
- GCC_except_table6056
- GCC_except_table6059
- GCC_except_table6062
- GCC_except_table6148
- GCC_except_table6365
- GCC_except_table6382
- GCC_except_table6833
- GCC_except_table7177
- GCC_except_table7187
- GCC_except_table7277
- GCC_except_table7286
- GCC_except_table7370
- GCC_except_table7377
- GCC_except_table7395
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7450
- GCC_except_table7455
- GCC_except_table7471
- GCC_except_table839
- GCC_except_table895
- GCC_except_table971
- OBJC_IVAR_$_MPCFuture._invalidBlocks
- __114-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy _locked_resolveContentDescriptorsUsingServerObjectDatabase]_block_invoke_2
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_2
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke
- __93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_2
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_3
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_4
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_5
- ___154-[MPCModelStorePlaybackItemsRequestAccumulation initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:]_block_invoke_6
- ___68-[MPCPlayerItemConfigurator _audioFormatsDictionaryWithHLSMetadata:]_block_invoke
- ___80-[AVURLAsset(MPCHLSSessionData) mpc_synchronousHLSSessionDataWithTimeout:error:]_block_invoke
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Legacy initWithRequest:serverObjectDatabase:]_block_invoke_3
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_2
- ___93-[_MPCModelStorePlaybackItemsRequestAccumulator_Modern initWithRequest:serverObjectDatabase:]_block_invoke_3
- ___block_descriptor_41_e8_32s_e18_16?0"NSString"8l
- ___block_descriptor_53_e8_32s40s_e49_v16?0"MPIdentifierSet<MPMutableIdentifierSet>"8l
- ___swift_memcpy72_8
- ___swift_memcpy73_8
- ___unnamed_11
- _objc_msgSend$_HLSMetadataForAsset:error:
- _objc_msgSend$_audioFormatsDictionaryWithHLSMetadata:
- _objc_msgSend$_logTimeJumpForItem:fromTime:toTime:userInitiated:timeStamp:
- _objc_msgSend$_playbackDidStopForItem:source:reason:time:timeStamp:
- _objc_msgSend$initWithProgressiveResults:properties:personalizationProperties:libraryObjectDatabase:performanceMetrics:
- _objc_msgSend$initWithRequest:serverObjectDatabase:
- _objc_msgSend$keyDeliveryJitterTime
- _objc_msgSend$metadataForFormat:
- _objc_msgSend$mpc_HLSAVMetadataItemInMetadata:
- _objc_msgSend$mpc_synchronousHLSSessionDataWithTimeout:error:
- _objc_msgSend$preferredAudioAssetTypeForSongWithTrait:isStartItem:
- _objc_msgSend$setShouldIgnoreExpiration:
- _objc_msgSend$sharedKeySegmentDuration
- _objc_msgSend$stereoAssetTypeWithIsStartItem:explanation:
- _objc_msgSend$userSeekCompletedForItem:fromTime:toTime:timeStamp:
- _objc_msgSend$weakToStrongObjectsMapTable
- _symbolic Sb7success_______pSg4itemSdSg9startTimeSd03endD0SS10identifierSb7passive_____9timeStampt 17MediaPlaybackCore10PlayerItemP AA9EventTimeC
- _symbolic yt______pIgrzo_ s5ErrorP
CStrings:
+ " versionHashesByStoreID=%@"
+ "4.AlbumAvailability"
+ "5.Outcome"
+ "AccumulationSectionPromotionUnsupported"
+ "Cannot promote items to sections for a request using sectionedModelObjects: %@"
+ "FIRST-SEGMENT-DURATION"
+ "Failed to decode HLS session data - Asset:%@"
+ "Failed to load HLS session metadata - Asset:%@"
+ "Forcing HLS to apply jitter treatment"
+ "Future has accumulated %lu invalidation handlers: %{public}@"
+ "HLSSessionDataDecodingFailed"
+ "HLSSessionDataFetchTimedOut"
+ "HLSSessionDataUnavailable"
+ "MPCModelGenericAVItem+KeyDeliveryDeferral.m"
+ "MPCModelStorePlaybackItemsRequestVersionHashesByStoreID"
+ "No HLS session data available - Asset:%@"
+ "Playback queue superseded before response; re-requesting"
+ "PreheatPlayback"
+ "SHARED-KEY-SEGMENT-COUNT"
+ "Timed out retrieving HLS session metadata - Asset:%@"
+ "Unexpected nil urlAsset"
+ "Update: %{public}@<%{public}@> Falling back to watch due to error=%@. Connect Device Dialog Imminent"
+ "XL-Accumulator-VersionHashLess"
+ "[%{public}@]-MPCPlayerItemConfigurator %p - [AP] - Deferring Alchemy configuration [start item, transitions disabled, audio accessory]: %{public}@"
+ "[%{public}@]-❗️MPCErrorControllerImplementation %p <%{public}@> - Ending playback [Item failed repeatedly]"
+ "[BMUS:%{public}@:%{public}@] _addPlaybackContext: | disabling auto play [%{public}@]"
+ "[PIA] %p container has no children with any versionHash [empty, not a versionHash mismatch] identifier=%{public}@ versionHash=%{public}@"
+ "[PIA] %p failing request [section promotion unsupported for sectionedModelObjects] indexPaths=%{public}@"
+ "[PIA] %p store resolved a different versionHash than requested [using store version] identifier=%{public}@ requestedVersionHash=%{public}@"
+ "[PL:%{public}s] STACK PROCESSING: setQueueWithInitialItem [new start item %{public}s] - isResend:%{bool,public}d - capturedIntent:%{bool,public}d - shouldPlay:%{bool,public}d"
+ "[PL:%{public}s] TRANSITION: Skipping transition setup - a seek/jump is in flight [caller: %{public}s] - will re-evaluate on seek completion"
+ "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized batch reported complete]"
+ "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized batch reported complete] unpersonalizedContentDescriptors=%{public}@"
+ "[SPIR:%{sonic:fourCC}u] execute | loadPage [firstPage]"
+ "[SPIR:%{sonic:fourCC}u] populateSection:sectionIndex: | populated section [store resolved a different versionHash than requested; using store version] progressiveSection=%{public}@ requestedVersionHash=%{public}@ relatedProgressiveResults.count=%ld"
+ "assetQueueDidChange(state:)"
+ "com.apple.mediaplaybackcore.accountmanager.update"
+ "data source unsupported"
+ "guest account unsupported"
+ "interstitial-primary-position"
+ "item-primary-end-position"
+ "item-primary-start-position"
+ "key-delivery-jitter-window"
+ "lease-acquisition"
+ "primaryStartTime"
+ "restoreCurrentTransitionIfNeeded()"
+ "sendOverlappedPlaybackDidEndForOngoingTransition()"
+ "setupNextPlayerItemTransition(_:caller:)"
+ "success item startTime primaryStartTime endTime primaryEndTime identifier passive timeStamp "
+ "v24@?0@\"AVMetadataItem\"8@\"NSError\"16"
+ "video-rendering-mode-did-change-position"
+ "video-rendering-mode-did-change-primary-position"
+ "|%{public}@ %{public}@ %2i %{public}@  │ primaryEnd: %0.2f"
+ "|%{public}@ %{public}@ %2i %{public}@  │ primaryStart: %0.2f"
+ "|%{public}@ %{public}@ %2i %{public}@  ╰ primaryPosition: %0.2f"
- "\nc"
- "4.Outcome"
- "MPC_LIVE_LINK_UNABLE_TO_SHAREPLAY_ALERT_ACTION"
- "MPC_LIVE_LINK_UNABLE_TO_SHAREPLAY_ALERT_TITLE"
- "[%{public}@]-MPCErrorControllerImplementation %p <%{public}@> - Playback has succeeded for at least one item [Ignoring queue failure]"
- "[%{public}@]-MPCPlayerItemConfigurator %p - [AL] - Error decoding HLS metadata [Clearing audioFormatsDictionary] - Error:%{public}@"
- "[%{public}@]-❗️MPCErrorControllerImplementation %p <%{public}@> - Ending playback [Entire queue failure]"
- "[BMUS:%{public}@:%{public}@] _addPlaybackContext: | disabling auto play [data source unsupported]"
- "[PL:%{public}s] STACK PROCESSING: setQueueWithInitialItem [new start item %{public}s]"
- "[SPIR%{sonic:fourCC}u] execute | loadPage [firstPage]"
- "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized IDs loaded]"
- "[SPIR:%{sonic:fourCC}u] execute | finished with placeholders [prioritized IDs loaded] unpersonalizedContentDescriptors=%{public}@"
- "success item startTime endTime identifier passive timeStamp "
```
