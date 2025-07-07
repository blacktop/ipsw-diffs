## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2360.66.3.0.0
-  __TEXT.__text: 0x20536c
-  __TEXT.__auth_stubs: 0x3cd0
-  __TEXT.__objc_methlist: 0x1acf4
-  __TEXT.__cstring: 0x31136
+2360.68.4.0.0
+  __TEXT.__text: 0x207d0c
+  __TEXT.__auth_stubs: 0x3ce0
+  __TEXT.__objc_methlist: 0x1aee4
+  __TEXT.__cstring: 0x31566
   __TEXT.__const: 0x1ed0
   __TEXT.__gcc_except_tab: 0x79f0
-  __TEXT.__oslogstring: 0x1b8f6
+  __TEXT.__oslogstring: 0x1be00
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x415
   __TEXT.__constg_swiftt: 0x290

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x93a0
-  __TEXT.__objc_classname: 0x5e38
-  __TEXT.__objc_methname: 0x359d7
-  __TEXT.__objc_methtype: 0x9cc9
-  __TEXT.__objc_stubs: 0x205c0
-  __DATA_CONST.__got: 0x4560
-  __DATA_CONST.__const: 0x5578
-  __DATA_CONST.__objc_classlist: 0x1178
+  __TEXT.__unwind_info: 0x9678
+  __TEXT.__objc_classname: 0x5e9e
+  __TEXT.__objc_methname: 0x35ef1
+  __TEXT.__objc_methtype: 0x9d17
+  __TEXT.__objc_stubs: 0x208a0
+  __DATA_CONST.__got: 0x4598
+  __DATA_CONST.__const: 0x55a0
+  __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaab0
+  __DATA_CONST.__objc_selrefs: 0xab70
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xcc8
+  __DATA_CONST.__objc_superrefs: 0xcd8
   __DATA_CONST.__objc_arraydata: 0x298
-  __AUTH_CONST.__auth_got: 0x1e78
+  __AUTH_CONST.__auth_got: 0x1e80
   __AUTH_CONST.__const: 0x1118
-  __AUTH_CONST.__cfstring: 0x191a0
-  __AUTH_CONST.__objc_const: 0x30288
+  __AUTH_CONST.__cfstring: 0x19260
+  __AUTH_CONST.__objc_const: 0x305a8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x78d0
+  __AUTH.__objc_data: 0x7970
   __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x2524
+  __DATA.__objc_ivar: 0x2550
   __DATA.__data: 0x1890
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x420

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 83311825-417A-33E7-BA32-6E5C0C1301E8
-  Functions: 11401
-  Symbols:   38920
-  CStrings:  18738
+  UUID: 617DF9BF-C69E-37CA-BE1E-8677AA0CDE85
+  Functions: 11442
+  Symbols:   39055
+  CStrings:  18815
 
Symbols:
+ +[AVMutableVideoComposition makeSpatialVideoConfigurationsFromVideoTracks:]
+ -[AVAssetExportSession makeLookupableSpatialVideoConfigurations:]
+ -[AVAssetReaderVideoCompositionOutput makeLookupableSpatialVideoConfigurations:]
+ -[AVAsynchronousVideoCompositionRequest _validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:]
+ -[AVAsynchronousVideoCompositionRequest attachSpatialVideoConfiguration:toPixelBuffer:]
+ -[AVAsynchronousVideoCompositionRequest(Internal) initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:lookupableSpatialVideoConfigurations:]
+ -[AVAsynchronousVideoCompositionRequestInternal lookupableSpatialVideoConfigurations]
+ -[AVAsynchronousVideoCompositionRequestInternal setLookupableSpatialVideoConfigurations:]
+ -[AVLookupableSpatialVideoConfiguration dealloc]
+ -[AVLookupableSpatialVideoConfiguration initWithSpatialVideoConfiguration:]
+ -[AVLookupableSpatialVideoConfiguration lookupID]
+ -[AVLookupableSpatialVideoConfiguration setLookupID:]
+ -[AVLookupableSpatialVideoConfiguration spatialVideoConfiguration]
+ -[AVMutableVideoComposition setSpatialVideoConfigurations:]
+ -[AVMutableVideoComposition spatialVideoConfigurations]
+ -[AVPlayer(AVPlayerInterstitialSupport_Internal) _populateInterstitialAssetOptions:fromPrimaryAsset:]
+ -[AVPlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChangedFor:dueTo:]
+ -[AVPlayerItem makeLookupableSpatialVideoConfigurations:]
+ -[AVPlayerLayer _interstitialLayerIsVisible]
+ -[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:]
+ -[AVQueuePlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChangedFor:dueTo:]
+ -[AVSpatialVideoConfiguration cameraCalibrationDataLensCollection]
+ -[AVSpatialVideoConfiguration cameraSystemBaseline]
+ -[AVSpatialVideoConfiguration copyWithZone:]
+ -[AVSpatialVideoConfiguration dealloc]
+ -[AVSpatialVideoConfiguration description]
+ -[AVSpatialVideoConfiguration disparityAdjustment]
+ -[AVSpatialVideoConfiguration hash]
+ -[AVSpatialVideoConfiguration horizontalFieldOfView]
+ -[AVSpatialVideoConfiguration initWithFormatDescription:]
+ -[AVSpatialVideoConfiguration init]
+ -[AVSpatialVideoConfiguration isEqual:]
+ -[AVSpatialVideoConfiguration setCameraCalibrationDataLensCollection:]
+ -[AVSpatialVideoConfiguration setCameraSystemBaseline:]
+ -[AVSpatialVideoConfiguration setDisparityAdjustment:]
+ -[AVSpatialVideoConfiguration setHorizontalFieldOfView:]
+ -[AVSpatialVideoConfiguration(AVSpatialVideoConfigurationInternal) isEmpty]
+ -[AVSpatialVideoConfiguration(AVSpatialVideoConfigurationInternal) toDictionary]
+ -[AVVideoComposition lookupableSpatialVideoConfigurations]
+ -[AVVideoComposition setLookupableSpatialVideoConfigurations:]
+ -[AVVideoComposition setSpatialVideoConfigurations:]
+ -[AVVideoComposition spatialVideoConfigurations]
+ GCC_except_table1003
+ GCC_except_table1005
+ GCC_except_table1016
+ GCC_except_table1020
+ GCC_except_table1024
+ GCC_except_table1028
+ GCC_except_table1033
+ GCC_except_table1035
+ GCC_except_table1038
+ GCC_except_table1042
+ GCC_except_table1044
+ GCC_except_table1050
+ GCC_except_table1054
+ GCC_except_table1058
+ GCC_except_table1062
+ GCC_except_table1068
+ GCC_except_table1070
+ GCC_except_table1073
+ GCC_except_table1078
+ GCC_except_table1082
+ GCC_except_table110
+ GCC_except_table158
+ GCC_except_table188
+ GCC_except_table216
+ GCC_except_table228
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table253
+ GCC_except_table267
+ GCC_except_table274
+ GCC_except_table286
+ GCC_except_table296
+ GCC_except_table302
+ GCC_except_table308
+ GCC_except_table319
+ GCC_except_table328
+ GCC_except_table333
+ GCC_except_table341
+ GCC_except_table363
+ GCC_except_table390
+ GCC_except_table398
+ GCC_except_table402
+ GCC_except_table412
+ GCC_except_table433
+ GCC_except_table438
+ GCC_except_table447
+ GCC_except_table450
+ GCC_except_table454
+ GCC_except_table460
+ GCC_except_table463
+ GCC_except_table472
+ GCC_except_table475
+ GCC_except_table477
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table500
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table513
+ GCC_except_table515
+ GCC_except_table517
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table540
+ GCC_except_table542
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table550
+ GCC_except_table552
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table562
+ GCC_except_table567
+ GCC_except_table572
+ GCC_except_table576
+ GCC_except_table578
+ GCC_except_table580
+ GCC_except_table589
+ GCC_except_table592
+ GCC_except_table594
+ GCC_except_table595
+ GCC_except_table600
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table616
+ GCC_except_table620
+ GCC_except_table626
+ GCC_except_table630
+ GCC_except_table633
+ GCC_except_table635
+ GCC_except_table639
+ GCC_except_table640
+ GCC_except_table646
+ GCC_except_table650
+ GCC_except_table652
+ GCC_except_table657
+ GCC_except_table665
+ GCC_except_table667
+ GCC_except_table669
+ GCC_except_table677
+ GCC_except_table679
+ GCC_except_table683
+ GCC_except_table685
+ GCC_except_table687
+ GCC_except_table690
+ GCC_except_table692
+ GCC_except_table695
+ GCC_except_table700
+ GCC_except_table703
+ GCC_except_table709
+ GCC_except_table711
+ GCC_except_table715
+ GCC_except_table719
+ GCC_except_table723
+ GCC_except_table729
+ GCC_except_table731
+ GCC_except_table735
+ GCC_except_table737
+ GCC_except_table740
+ GCC_except_table750
+ GCC_except_table754
+ GCC_except_table758
+ GCC_except_table760
+ GCC_except_table764
+ GCC_except_table766
+ GCC_except_table769
+ GCC_except_table773
+ GCC_except_table783
+ GCC_except_table786
+ GCC_except_table788
+ GCC_except_table790
+ GCC_except_table793
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table806
+ GCC_except_table813
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table831
+ GCC_except_table834
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table846
+ GCC_except_table850
+ GCC_except_table852
+ GCC_except_table858
+ GCC_except_table865
+ GCC_except_table872
+ GCC_except_table875
+ GCC_except_table880
+ GCC_except_table883
+ GCC_except_table889
+ GCC_except_table891
+ GCC_except_table893
+ GCC_except_table895
+ GCC_except_table897
+ GCC_except_table899
+ GCC_except_table902
+ GCC_except_table911
+ GCC_except_table923
+ GCC_except_table941
+ GCC_except_table943
+ GCC_except_table945
+ GCC_except_table947
+ GCC_except_table965
+ GCC_except_table975
+ GCC_except_table979
+ GCC_except_table986
+ GCC_except_table990
+ GCC_except_table993
+ GCC_except_table996
+ GCC_except_table998
+ _AVLookupableSpatialVideoConfigurationMakeSerializableArray
+ _AVSpatialVideoConfigurationMakeSerializableArray
+ _CVBufferCopyAttachment
+ _OBJC_CLASS_$_AVLookupableSpatialVideoConfiguration
+ _OBJC_CLASS_$_AVSpatialVideoConfiguration
+ _OBJC_IVAR_$_AVAsynchronousVideoCompositionRequestInternal._lookupableSpatialVideoConfigurations
+ _OBJC_IVAR_$_AVLookupableSpatialVideoConfiguration._lookupID
+ _OBJC_IVAR_$_AVLookupableSpatialVideoConfiguration._spatialVideoConfiguration
+ _OBJC_IVAR_$_AVPlaybackCoordinationMedium._condition
+ _OBJC_IVAR_$_AVPlaybackCoordinationMedium._dispatchQueue
+ _OBJC_IVAR_$_AVPlaybackCoordinationMedium._itemIdentifierConditionWaitsOn
+ _OBJC_IVAR_$_AVQueuePlayerInternal.canOverlapConditionState
+ _OBJC_IVAR_$_AVSpatialVideoConfiguration._cameraCalibrationDataLensCollection
+ _OBJC_IVAR_$_AVSpatialVideoConfiguration._cameraSystemBaseline
+ _OBJC_IVAR_$_AVSpatialVideoConfiguration._disparityAdjustment
+ _OBJC_IVAR_$_AVSpatialVideoConfiguration._horizontalFieldOfView
+ _OBJC_IVAR_$_AVVideoCompositionInternal.lookupableSpatialVideoConfigurations
+ _OBJC_IVAR_$_AVVideoCompositionInternal.spatialVideoConfigurations
+ _OBJC_METACLASS_$_AVLookupableSpatialVideoConfiguration
+ _OBJC_METACLASS_$_AVSpatialVideoConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVLookupableSpatialVideoConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVSpatialVideoConfiguration(AVSpatialVideoConfigurationInternal)
+ __OBJC_$_INSTANCE_VARIABLES_AVLookupableSpatialVideoConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVSpatialVideoConfiguration
+ __OBJC_$_PROP_LIST_AVLookupableSpatialVideoConfiguration
+ __OBJC_$_PROP_LIST_AVSpatialVideoConfiguration
+ __OBJC_CLASS_RO_$_AVLookupableSpatialVideoConfiguration
+ __OBJC_CLASS_RO_$_AVSpatialVideoConfiguration
+ __OBJC_METACLASS_RO_$_AVLookupableSpatialVideoConfiguration
+ __OBJC_METACLASS_RO_$_AVSpatialVideoConfiguration
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.453
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.454
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.457
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.455
+ ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.458
+ ___119-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]_block_invoke
+ ___22-[AVPlayer _addLayer:]_block_invoke.616
+ ___22-[AVPlayer _addLayer:]_block_invoke.617
+ ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke.460
+ ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke.512
+ ___35-[AVPlayerLayer setPIPModeEnabled:]_block_invoke
+ ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke.569
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.993
+ ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.994
+ ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.526
+ ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1186
+ ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke.524
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.469
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.470
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.483
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.495
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.504
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.507
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.487
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.496
+ ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.505
+ ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1172
+ ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.610
+ ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1169
+ ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1271
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke.996
+ ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2.997
+ ___99-[AVQueuePlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChangedFor:dueTo:]_block_invoke
+ ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1428
+ ___avplayer_fpNotificationCallback_block_invoke.1442
+ ___avplayer_fpNotificationCallback_block_invoke.1445
+ ___avplayer_fpNotificationCallback_block_invoke.1448
+ ___avplayer_fpNotificationCallback_block_invoke.1458
+ ___avplayer_fpNotificationCallback_block_invoke.1466
+ ___avplayer_fpNotificationCallback_block_invoke_2.1449
+ ___avplayer_fpNotificationCallback_block_invoke_2.1462
+ ___avplayer_fpNotificationCallback_block_invoke_3.1453
+ ___avplayer_fpNotificationCallback_block_invoke_3.1463
+ ___avplayer_fpNotificationCallback_block_invoke_4.1464
+ ___avplayer_iapdNotificationCallback_block_invoke.1469
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1616
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1640
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1641
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1648
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1649
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1650
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1655
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1661
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1662
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1667
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1668
+ ___avplayeritem_fpItemNotificationCallback_block_invoke.1675
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1651
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1656
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1663
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1652
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1664
+ ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1653
+ ___block_descriptor_72_e8_32o40o48o56o64o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32o40r48r56r64r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8
+ ___block_literal_global.1419
+ ___block_literal_global.1472
+ ___block_literal_global.1498
+ ___block_literal_global.591
+ ___block_literal_global.598
+ ___block_literal_global.601
+ ___block_literal_global.622
+ ___block_literal_global.716
+ ___block_literal_global.762
+ ___block_literal_global.775
+ ___block_literal_global.972
+ _getAudioChannelCountForFirstEnabledTrack
+ _kCMFormatDescriptionExtension_CameraCalibrationDataLensCollection
+ _kFigFormatDescriptionExtension_CameraCalibrationDataLensCollection
+ _kFigPlaybackItemProperty_VideoCompositorLookupableSpatialVideoConfigurations
+ _kFigSpatialVideoConfiguration_LookupID
+ _kFigVideoCompositionProcessorProperty_SerializableLookupableSpatialVideoConfigurations
+ _objc_msgSend$_canOverlapPlaybackConditionsChangedFor:dueTo:
+ _objc_msgSend$_canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:
+ _objc_msgSend$_interstitialLayerIsVisible
+ _objc_msgSend$_populateInterstitialAssetOptions:fromPrimaryAsset:
+ _objc_msgSend$_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:
+ _objc_msgSend$cameraCalibrationDataLensCollection
+ _objc_msgSend$cameraSystemBaseline
+ _objc_msgSend$disparityAdjustment
+ _objc_msgSend$horizontalFieldOfView
+ _objc_msgSend$initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:lookupableSpatialVideoConfigurations:
+ _objc_msgSend$initWithFormatDescription:
+ _objc_msgSend$initWithSpatialVideoConfiguration:
+ _objc_msgSend$lookupID
+ _objc_msgSend$lookupableSpatialVideoConfigurations
+ _objc_msgSend$makeLookupableSpatialVideoConfigurations:
+ _objc_msgSend$makeSpatialVideoConfigurationsFromVideoTracks:
+ _objc_msgSend$setCameraCalibrationDataLensCollection:
+ _objc_msgSend$setCameraSystemBaseline:
+ _objc_msgSend$setDisparityAdjustment:
+ _objc_msgSend$setHorizontalFieldOfView:
+ _objc_msgSend$setLookupID:
+ _objc_msgSend$setLookupableSpatialVideoConfigurations:
+ _objc_msgSend$setSpatialVideoConfigurations:
+ _objc_msgSend$spatialVideoConfiguration
+ _objc_msgSend$spatialVideoConfigurations
- -[AVAsynchronousVideoCompositionRequest(Internal) initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:]
- -[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:].cold.2
- -[AVPlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChanged]
- -[AVQueuePlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChanged]
- GCC_except_table1002
- GCC_except_table1004
- GCC_except_table1015
- GCC_except_table1019
- GCC_except_table1023
- GCC_except_table1027
- GCC_except_table1032
- GCC_except_table1034
- GCC_except_table1037
- GCC_except_table1041
- GCC_except_table1043
- GCC_except_table1049
- GCC_except_table1053
- GCC_except_table1057
- GCC_except_table1061
- GCC_except_table1067
- GCC_except_table1069
- GCC_except_table1072
- GCC_except_table1077
- GCC_except_table1081
- GCC_except_table142
- GCC_except_table148
- GCC_except_table157
- GCC_except_table204
- GCC_except_table218
- GCC_except_table221
- GCC_except_table236
- GCC_except_table241
- GCC_except_table250
- GCC_except_table261
- GCC_except_table269
- GCC_except_table278
- GCC_except_table288
- GCC_except_table295
- GCC_except_table300
- GCC_except_table306
- GCC_except_table310
- GCC_except_table321
- GCC_except_table330
- GCC_except_table335
- GCC_except_table343
- GCC_except_table344
- GCC_except_table360
- GCC_except_table369
- GCC_except_table392
- GCC_except_table400
- GCC_except_table404
- GCC_except_table413
- GCC_except_table414
- GCC_except_table435
- GCC_except_table442
- GCC_except_table452
- GCC_except_table458
- GCC_except_table467
- GCC_except_table470
- GCC_except_table476
- GCC_except_table481
- GCC_except_table495
- GCC_except_table501
- GCC_except_table504
- GCC_except_table506
- GCC_except_table512
- GCC_except_table514
- GCC_except_table516
- GCC_except_table520
- GCC_except_table522
- GCC_except_table524
- GCC_except_table526
- GCC_except_table531
- GCC_except_table533
- GCC_except_table535
- GCC_except_table539
- GCC_except_table544
- GCC_except_table548
- GCC_except_table549
- GCC_except_table551
- GCC_except_table555
- GCC_except_table559
- GCC_except_table563
- GCC_except_table569
- GCC_except_table571
- GCC_except_table574
- GCC_except_table579
- GCC_except_table581
- GCC_except_table583
- GCC_except_table585
- GCC_except_table588
- GCC_except_table591
- GCC_except_table593
- GCC_except_table597
- GCC_except_table599
- GCC_except_table601
- GCC_except_table603
- GCC_except_table606
- GCC_except_table609
- GCC_except_table611
- GCC_except_table614
- GCC_except_table618
- GCC_except_table623
- GCC_except_table625
- GCC_except_table628
- GCC_except_table632
- GCC_except_table634
- GCC_except_table638
- GCC_except_table644
- GCC_except_table645
- GCC_except_table648
- GCC_except_table649
- GCC_except_table654
- GCC_except_table660
- GCC_except_table666
- GCC_except_table668
- GCC_except_table672
- GCC_except_table684
- GCC_except_table689
- GCC_except_table698
- GCC_except_table699
- GCC_except_table705
- GCC_except_table712
- GCC_except_table714
- GCC_except_table717
- GCC_except_table718
- GCC_except_table724
- GCC_except_table727
- GCC_except_table728
- GCC_except_table730
- GCC_except_table734
- GCC_except_table736
- GCC_except_table738
- GCC_except_table741
- GCC_except_table751
- GCC_except_table755
- GCC_except_table757
- GCC_except_table759
- GCC_except_table763
- GCC_except_table765
- GCC_except_table767
- GCC_except_table770
- GCC_except_table774
- GCC_except_table784
- GCC_except_table785
- GCC_except_table787
- GCC_except_table789
- GCC_except_table794
- GCC_except_table795
- GCC_except_table801
- GCC_except_table805
- GCC_except_table812
- GCC_except_table816
- GCC_except_table818
- GCC_except_table823
- GCC_except_table828
- GCC_except_table830
- GCC_except_table835
- GCC_except_table838
- GCC_except_table840
- GCC_except_table847
- GCC_except_table849
- GCC_except_table851
- GCC_except_table857
- GCC_except_table864
- GCC_except_table871
- GCC_except_table874
- GCC_except_table879
- GCC_except_table881
- GCC_except_table888
- GCC_except_table890
- GCC_except_table892
- GCC_except_table894
- GCC_except_table896
- GCC_except_table898
- GCC_except_table901
- GCC_except_table910
- GCC_except_table921
- GCC_except_table940
- GCC_except_table942
- GCC_except_table944
- GCC_except_table946
- GCC_except_table964
- GCC_except_table974
- GCC_except_table978
- GCC_except_table985
- GCC_except_table988
- GCC_except_table992
- GCC_except_table995
- GCC_except_table997
- _OBJC_IVAR_$_AVPlayerInternal.currentItemSpatialAudioRenderingDidChangeNotificationToken
- _OBJC_IVAR_$_AVPlayerInternal.currentItemVariantChangedNotificationToken
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.455
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.456
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.459
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.457
- ___109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.460
- ___22-[AVPlayer _addLayer:]_block_invoke.618
- ___22-[AVPlayer _addLayer:]_block_invoke.619
- ___31-[AVPlayer _itemIsReadyToPlay:]_block_invoke.462
- ___34-[AVPlayer setExpectedAssetTypes:]_block_invoke.514
- ___41-[AVPlayer setShouldReduceResourceUsage:]_block_invoke.571
- ___51-[AVPlayer _startObservingPropertiesOfCurrentItem:]_block_invoke_3
- ___51-[AVPlayer _startObservingPropertiesOfCurrentItem:]_block_invoke_4
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.995
- ___58-[AVPlayer(AVPlayerMultitaskSupport) _didEnterBackground:]_block_invoke.996
- ___62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.528
- ___63-[AVPlayer(FigVideoTargetSupport) setShouldWaitForVideoTarget:]_block_invoke.1188
- ___67-[AVPlayer _applyPlayQueueChangesToFigPlayerWithCompletionHandler:]_block_invoke.526
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.471
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.472
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.485
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.497
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.506
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.509
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.489
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.498
- ___67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.507
- ___67-[AVPlayer(AVPlayerPIPSupport) _setSilencesOtherPlaybackDuringPIP:]_block_invoke.1174
- ___87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.612
- ___90-[AVPlayer(AVPlayerPIPSupport) setPrefersPlayingSilentlyWhenConflictingWithOtherPlayback:]_block_invoke.1171
- ___91-[AVPlayer(AVPlayerRoutingPlaybackArbitrationSupport) _setNonMixableAudioPriorityInternal:]_block_invoke.1270
- ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke.998
- ___97-[AVPlayer(AVPlayerMultitaskSupport) _detachVideoDestinationsForSuspensionWithCompletionHandler:]_block_invoke_2.999
- ___avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1427
- ___avplayer_fpNotificationCallback_block_invoke.1441
- ___avplayer_fpNotificationCallback_block_invoke.1444
- ___avplayer_fpNotificationCallback_block_invoke.1447
- ___avplayer_fpNotificationCallback_block_invoke.1457
- ___avplayer_fpNotificationCallback_block_invoke.1465
- ___avplayer_fpNotificationCallback_block_invoke_2.1448
- ___avplayer_fpNotificationCallback_block_invoke_2.1461
- ___avplayer_fpNotificationCallback_block_invoke_3.1452
- ___avplayer_fpNotificationCallback_block_invoke_3.1462
- ___avplayer_fpNotificationCallback_block_invoke_4.1463
- ___avplayer_iapdNotificationCallback_block_invoke.1467
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1614
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1634
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1637
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1643
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1644
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1653
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1659
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1660
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1664
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1665
- ___avplayeritem_fpItemNotificationCallback_block_invoke.1673
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1648
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1654
- ___avplayeritem_fpItemNotificationCallback_block_invoke_2.1661
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1649
- ___avplayeritem_fpItemNotificationCallback_block_invoke_3.1662
- ___avplayeritem_fpItemNotificationCallback_block_invoke_4.1650
- ___avplayeritem_fpItemNotificationCallback_block_invoke_5.1651
- ___block_descriptor_72_e8_32o40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
- ___block_literal_global.1418
- ___block_literal_global.1471
- ___block_literal_global.1499
- ___block_literal_global.590
- ___block_literal_global.600
- ___block_literal_global.603
- ___block_literal_global.624
- ___block_literal_global.707
- ___block_literal_global.761
- ___block_literal_global.774
- ___block_literal_global.974
- _getAudioChannelCountForFirstTrack
- _objc_msgSend$_canOverlapPlaybackConditionsChanged
- _objc_msgSend$initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:
CStrings:
+ "-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:]_block_invoke"
+ "-[AVPlayerItem setAdvanceTimeForOverlappedPlayback:]"
+ "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) _canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:]"
+ "-[AVQueuePlayer(AVPlayer_OverlapPlaybackConditions) _canOverlapPlaybackConditionsChangedFor:dueTo:]_block_invoke"
+ "<%@: %p> horizontalFieldOfView: %@, cameraSystemBaseline: %@, disparityAdjustment: %@, cameraCalibrationDataLensCollection: %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ current transport control state dictionary %@ for item identifier %@ for coordinator %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ signalling condition for item identifier %@"
+ "<<<< AVPlaybackCoordinationMedium >>>> %s: %@ waiting to satisfy condition for identifier %@"
+ "<<<< AVPlayerItem >>>> %s: %{public}@ advanceTime %.3f"
+ "<<<< AVPlayerItem >>>> %s: %{public}@ tracks changed, %@, %@"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, %d channels"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, no decodable format"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. %d tracks available, no format description"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. %s, reason %@, from %@ to %@"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. Y>N, reason %@, not enough items left"
+ "<<<< AVQueuePlayer >>>> %s: %p %@. ignoring since buffered airplay is enabled but first 2 items are not ready for inspection"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. %{public}@ to %{public}@. YES"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. %{public}@ to %{public}@. YES, channel count match"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO because the multichannel audio strategy permits exclusive passthrough"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since %{public}@ has %d channels and %{public}@ has %d channels"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since AirPlay Video is active"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since Buffered AirPlay is active and SenderSideMixing is not enabled"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since action-at-end is NOT advance"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since one of items is HLS"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the first item doesn't have audio track"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the first item's number of tracks is not 1"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the second item doesn't have audio track"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. NO since the second item's number of tracks is not 1"
+ "<<<< AVQueuePlayer >>>> %s: (%c) %p %{public}@. YES, but %{public}@ channel count %d, %{public}@ channel count %d"
+ "@\"AVSpatialVideoConfiguration\""
+ "@96@0:8@16@24^{OpaqueFigVideoCompositorFrame=}32{?=qiIq}40@64@72@80@88"
+ "AVLookupableSpatialVideoConfiguration"
+ "AVSpatialVideoConfiguration"
+ "AVSpatialVideoConfigurationInternal"
+ "AuxilaryVideoAttachmentsLookup"
+ "B36@0:8@16@24B32"
+ "N>Y"
+ "T@\"AVSpatialVideoConfiguration\",R,N,V_spatialVideoConfiguration"
+ "T@\"NSArray\",C,N,V_lookupableSpatialVideoConfigurations"
+ "T@\"NSArray\",C,V_cameraCalibrationDataLensCollection"
+ "T@\"NSNumber\",C,N,V_lookupID"
+ "T@\"NSNumber\",C,V_cameraSystemBaseline"
+ "T@\"NSNumber\",C,V_disparityAdjustment"
+ "T@\"NSNumber\",C,V_horizontalFieldOfView"
+ "Y>N"
+ "_cameraCalibrationDataLensCollection"
+ "_cameraSystemBaseline"
+ "_canOverlapPlaybackConditionsChangedFor:dueTo:"
+ "_canOverlapPlaybackFromPlayerItem:toPlayerItem:isInternal:"
+ "_disparityAdjustment"
+ "_dispatchQueue"
+ "_horizontalFieldOfView"
+ "_interstitialLayerIsVisible"
+ "_itemIdentifierConditionWaitsOn"
+ "_lookupID"
+ "_lookupableSpatialVideoConfigurations"
+ "_populateInterstitialAssetOptions:fromPrimaryAsset:"
+ "_spatialVideoConfiguration"
+ "_validateAttachedSpatialVideoConfigurationInTaggedBufferGroup:"
+ "attachSpatialVideoConfiguration:toPixelBuffer must specify a configuration in the AVVideoComposition's spatialVideoConfigurations list"
+ "attachSpatialVideoConfiguration:toPixelBuffer:"
+ "avplayeritem_fpItemNotificationCallback_block_invoke_5"
+ "calling attachSpatialVideoConfiguration:toPixelBuffer is illegal when AVVideoComposition's spatialVideoConfigurations is nil"
+ "cameraCalibrationDataLensCollection"
+ "cameraSystemBaseline"
+ "canOverlapConditionState"
+ "com.apple.avfoundation.playbackcoordinationmediumdispatchqueue"
+ "disparityAdjustment"
+ "getAudioChannelCountForFirstEnabledTrack"
+ "horizontalFieldOfView"
+ "initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:lookupableSpatialVideoConfigurations:"
+ "initWithFormatDescription:"
+ "initWithSpatialVideoConfiguration:"
+ "lookupID"
+ "lookupableSpatialVideoConfigurations"
+ "makeLookupableSpatialVideoConfigurations:"
+ "makeSpatialVideoConfigurationsFromVideoTracks:"
+ "setCameraCalibrationDataLensCollection:"
+ "setCameraSystemBaseline:"
+ "setDisparityAdjustment:"
+ "setHorizontalFieldOfView:"
+ "setLookupID:"
+ "setLookupableSpatialVideoConfigurations:"
+ "setSpatialVideoConfigurations:"
+ "spatialVideoConfiguration"
+ "spatialVideoConfigurations"
+ "taggedBufferGroup contains pixel buffers associated with different spatial configurations."
+ "taggedBufferGroup contains pixel buffers associated with spatial configurations, but AVVideoComposition's spatialVideoConfigurations is nil"
+ "v32@0:8@16^{__CVBuffer=}24"
- "-[AVQueuePlayer(AVPlayerAdvanceWithOverlap) canOverlapPlaybackFromPlayerItem:toPlayerItem:]"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO because the multichannel audio strategy permits exclusive passthrough"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since AirPlay Video is active"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since Buffered AirPlay is active and SenderSideMixing is not enabled"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since action-at-end is NOT advance"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since one of items is HLS"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item has %d channels and the second item has %d channels"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the first item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item doesn't have audio track"
- "<<<< AVQueuePlayer >>>> %s: %p %@. NO since the second item's number of tracks is not 1"
- "<<<< AVQueuePlayer >>>> %s: %p %@. YES"
- "@88@0:8@16@24^{OpaqueFigVideoCompositorFrame=}32{?=qiIq}40@64@72@80"
- "_canOverlapPlaybackConditionsChanged"
- "avplayeritem_fpItemNotificationCallback_block_invoke_6"
- "currentItemSpatialAudioRenderingDidChangeNotificationToken"
- "currentItemVariantChangedNotificationToken"
- "initUsingSession:withRenderContext:compositionFrame:atTime:usingSources:instruction:withSampleBuffers:"

```
