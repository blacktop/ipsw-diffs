## MediaPlaybackCore

> `/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore`

```diff

-4023.210.3.0.0
-  __TEXT.__text: 0x2a7d10
-  __TEXT.__auth_stubs: 0x37b0
-  __TEXT.__objc_methlist: 0x10fb8
-  __TEXT.__const: 0x8518
-  __TEXT.__cstring: 0x264f3
-  __TEXT.__swift5_typeref: 0x33ad
-  __TEXT.__swift5_fieldmd: 0x2dc0
-  __TEXT.__constg_swiftt: 0x474c
-  __TEXT.__swift5_builtin: 0x528
-  __TEXT.__swift5_reflstr: 0x28f1
+4023.310.4.0.0
+  __TEXT.__text: 0x2ad0b8
+  __TEXT.__auth_stubs: 0x3820
+  __TEXT.__objc_methlist: 0x110e0
+  __TEXT.__const: 0x8738
+  __TEXT.__cstring: 0x269ea
+  __TEXT.__swift5_typeref: 0x3443
+  __TEXT.__swift5_fieldmd: 0x2e64
+  __TEXT.__constg_swiftt: 0x47e4
+  __TEXT.__swift5_builtin: 0x564
+  __TEXT.__swift5_reflstr: 0x29a1
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__swift5_assocty: 0x9b8
+  __TEXT.__swift5_assocty: 0xa00
   __TEXT.__swift5_protos: 0xd0
-  __TEXT.__swift5_proto: 0x630
-  __TEXT.__swift5_types: 0x33c
-  __TEXT.__swift5_capture: 0x2270
-  __TEXT.__gcc_except_tab: 0x3b78
-  __TEXT.__oslogstring: 0x27658
+  __TEXT.__swift5_proto: 0x64c
+  __TEXT.__swift5_types: 0x34c
+  __TEXT.__swift5_capture: 0x22a4
+  __TEXT.__gcc_except_tab: 0x3c60
+  __TEXT.__oslogstring: 0x277f5
   __TEXT.__ustring: 0x338
   __TEXT.__dlopen_cstrs: 0x114
-  __TEXT.__unwind_info: 0x9374
-  __TEXT.__eh_frame: 0x4bb8
+  __TEXT.__unwind_info: 0x95e4
+  __TEXT.__eh_frame: 0x4cd8
   __TEXT.__objc_classname: 0x389a
-  __TEXT.__objc_methname: 0x34848
-  __TEXT.__objc_methtype: 0x8f52
-  __TEXT.__objc_stubs: 0x24440
-  __DATA_CONST.__got: 0x1620
-  __DATA_CONST.__const: 0x8d10
+  __TEXT.__objc_methname: 0x34cac
+  __TEXT.__objc_methtype: 0x8fdd
+  __TEXT.__objc_stubs: 0x24740
+  __DATA_CONST.__got: 0x1660
+  __DATA_CONST.__const: 0x8e38
   __DATA_CONST.__objc_classlist: 0xb00
   __DATA_CONST.__objc_catlist: 0x250
   __DATA_CONST.__objc_protolist: 0x5f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28160
-  __DATA_CONST.__objc_selrefs: 0xad78
-  __DATA_CONST.__objc_arraydata: 0x1a8
-  __AUTH_CONST.__const: 0xb868
+  __DATA_CONST.__objc_const: 0x28258
+  __DATA_CONST.__objc_selrefs: 0xae60
+  __DATA_CONST.__objc_arraydata: 0x180
+  __AUTH_CONST.__const: 0xb9b0
   __AUTH_CONST.__objc_const: 0x7ce8
-  __AUTH_CONST.__cfstring: 0x191a0
-  __AUTH_CONST.__objc_intobj: 0x798
+  __AUTH_CONST.__cfstring: 0x19880
+  __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_arrayobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__auth_got: 0x1be8
+  __AUTH_CONST.__auth_got: 0x1c20
   __AUTH.__objc_data: 0x2fc8
   __AUTH.__data: 0xd50
   __DATA.__objc_protorefs: 0x250
   __DATA.__objc_classrefs: 0x12f0
   __DATA.__objc_superrefs: 0x6a8
-  __DATA.__objc_ivar: 0x18f8
-  __DATA.__objc_data: 0x1040
-  __DATA.__data: 0x50c0
-  __DATA.__bss: 0x9268
+  __DATA.__objc_ivar: 0x18fc
+  __DATA.__objc_data: 0x1070
+  __DATA.__data: 0x5280
+  __DATA.__bss: 0x95f8
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x37b0
-  __DATA_DIRTY.__data: 0x40b8
+  __DATA_DIRTY.__objc_data: 0x37b8
+  __DATA_DIRTY.__data: 0x40c8
   __DATA_DIRTY.__bss: 0x1b38
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0CC8B211-AB93-3443-8775-AB3F4AB0667B
-  Functions: 14641
-  Symbols:   30674
-  CStrings:  19207
+  UUID: 94086456-A22B-3A88-BAD1-F239CB666C46
+  Functions: 14774
+  Symbols:   30833
+  CStrings:  19372
 
Symbols:
+ +[MPCVocalAttenuationModel _filePathsForModelAtURL:]
+ -[AVPlayerItem(MediaPlaybackCore) mpc_setReportingValue:forKey:]
+ -[AVPlayerItem(MediaPlaybackCore) mpc_setupWithSpatialPreference:maxResolution:]
+ -[MPCAudioAssetTypeSelector maxResolution]
+ -[MPCAudioAssetTypeSelector spatialPreference]
+ -[MPCModelGenericAVItem _getSubscriptionStatusWithStoreRequestContext:completion:]
+ -[MPCModelGenericAVItem _prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:isStoreKeyServer:]
+ -[MPCPlayPerfMetrics set_timeSinceBoot:]
+ -[MPCPlayPerfMetrics set_timeSinceLaunch:]
+ -[MPCPlayPerfMetrics set_timeSincePaused:]
+ -[MPCPlayPerfMetrics timeSinceBoot]
+ -[MPCPlayPerfMetrics timeSinceLaunch]
+ -[MPCPlayPerfMetrics timeSincePaused]
+ -[MPCPlayerAudioFormat audioFormatWithRenderingMode:]
+ -[MPCPlayerAudioFormat initWithTier:codec:spatialized:multiChannel:channelLayout:sampleRate:stableVariantID:]
+ -[MPCPlayerAudioFormat renderingMode]
+ -[MPCPlayerItemConfigurator _setupQueueItemForVideoHLSPlayback:]
+ -[MPCPlayerResponseTracklist representativeSectionForDisplaySection:]
+ -[MPCSingleTrackAudioProcessor audioProcessingTap]
+ -[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]
+ -[_MPCMusicPlayerControllerServer _handleMPAVItemTitlesDidChange:]
+ -[_MPCMusicPlayerControllerServer _registerForMPAVItemTitlesDidChangeNotification]
+ -[_MPCPlaybackEnginePlayer donateMetricsToPlayerItem:]
+ -[_MPCPlaybackEnginePlayer renderingModeDidChange:timeStamp:]
+ GCC_except_table1021
+ GCC_except_table1077
+ GCC_except_table1128
+ GCC_except_table1227
+ GCC_except_table1366
+ GCC_except_table1367
+ GCC_except_table1371
+ GCC_except_table1421
+ GCC_except_table1430
+ GCC_except_table1441
+ GCC_except_table1566
+ GCC_except_table1573
+ GCC_except_table1580
+ GCC_except_table1593
+ GCC_except_table1625
+ GCC_except_table1646
+ GCC_except_table1665
+ GCC_except_table1723
+ GCC_except_table1824
+ GCC_except_table1839
+ GCC_except_table1867
+ GCC_except_table1876
+ GCC_except_table1890
+ GCC_except_table2082
+ GCC_except_table2150
+ GCC_except_table2190
+ GCC_except_table2203
+ GCC_except_table2238
+ GCC_except_table2432
+ GCC_except_table2443
+ GCC_except_table2452
+ GCC_except_table2459
+ GCC_except_table2493
+ GCC_except_table2535
+ GCC_except_table2536
+ GCC_except_table2539
+ GCC_except_table2544
+ GCC_except_table2560
+ GCC_except_table2622
+ GCC_except_table264
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table2943
+ GCC_except_table298
+ GCC_except_table307
+ GCC_except_table3088
+ GCC_except_table3130
+ GCC_except_table3223
+ GCC_except_table3240
+ GCC_except_table3242
+ GCC_except_table3244
+ GCC_except_table3245
+ GCC_except_table3269
+ GCC_except_table3273
+ GCC_except_table3382
+ GCC_except_table3385
+ GCC_except_table3387
+ GCC_except_table3392
+ GCC_except_table3397
+ GCC_except_table3407
+ GCC_except_table3411
+ GCC_except_table3414
+ GCC_except_table3417
+ GCC_except_table343
+ GCC_except_table345
+ GCC_except_table3486
+ GCC_except_table3608
+ GCC_except_table3609
+ GCC_except_table3667
+ GCC_except_table3672
+ GCC_except_table3674
+ GCC_except_table3768
+ GCC_except_table3783
+ GCC_except_table3846
+ GCC_except_table4017
+ GCC_except_table4047
+ GCC_except_table4071
+ GCC_except_table4075
+ GCC_except_table4078
+ GCC_except_table412
+ GCC_except_table4122
+ GCC_except_table413
+ GCC_except_table4152
+ GCC_except_table4200
+ GCC_except_table4202
+ GCC_except_table4341
+ GCC_except_table4358
+ GCC_except_table436
+ GCC_except_table4398
+ GCC_except_table446
+ GCC_except_table4469
+ GCC_except_table4504
+ GCC_except_table4512
+ GCC_except_table4727
+ GCC_except_table4728
+ GCC_except_table4835
+ GCC_except_table4844
+ GCC_except_table487
+ GCC_except_table488
+ GCC_except_table4935
+ GCC_except_table4942
+ GCC_except_table4943
+ GCC_except_table4993
+ GCC_except_table5016
+ GCC_except_table505
+ GCC_except_table5062
+ GCC_except_table5068
+ GCC_except_table5108
+ GCC_except_table5113
+ GCC_except_table5157
+ GCC_except_table5173
+ GCC_except_table5184
+ GCC_except_table5200
+ GCC_except_table5241
+ GCC_except_table5258
+ GCC_except_table5264
+ GCC_except_table5279
+ GCC_except_table5280
+ GCC_except_table5328
+ GCC_except_table5329
+ GCC_except_table557
+ GCC_except_table5571
+ GCC_except_table5574
+ GCC_except_table5587
+ GCC_except_table5590
+ GCC_except_table5593
+ GCC_except_table571
+ GCC_except_table576
+ GCC_except_table5965
+ GCC_except_table6009
+ GCC_except_table6071
+ GCC_except_table6080
+ GCC_except_table6089
+ GCC_except_table6098
+ GCC_except_table611
+ GCC_except_table620
+ GCC_except_table631
+ GCC_except_table634
+ GCC_except_table6347
+ GCC_except_table6358
+ GCC_except_table6408
+ GCC_except_table6453
+ GCC_except_table6454
+ GCC_except_table6497
+ GCC_except_table6502
+ GCC_except_table6506
+ GCC_except_table6524
+ GCC_except_table6533
+ GCC_except_table6636
+ GCC_except_table6659
+ GCC_except_table6674
+ GCC_except_table669
+ GCC_except_table6722
+ GCC_except_table6747
+ GCC_except_table6751
+ GCC_except_table6915
+ GCC_except_table6917
+ GCC_except_table7029
+ GCC_except_table710
+ GCC_except_table741
+ GCC_except_table797
+ GCC_except_table893
+ GCC_except_table899
+ GCC_except_table913
+ GCC_except_table971
+ _AVAudioSessionRenderingModeChangeNotification
+ _AVMediaTypeAudio
+ _MPCPlaybackEngineEventPayloadKeyAudioRenderingMode
+ _MPCPlaybackEngineEventTypeAudioRenderingModeChanged
+ _MPCPlayerAudioFormatRenderingModeFrom
+ _MPModelPropertyPlaylistCollaboratorStatus
+ _MSVFastHexStringFromBytes.hexCharacters.28086
+ _NSStringFromMPCPlayerAudioFormatRenderingMode
+ _NSURLNameKey
+ _OBJC_IVAR_$_MPCPlayerAudioFormat._renderingMode
+ __MPCAudioTapFinalize.30040
+ __MPCAudioTapInit.30041
+ __MPCAudioTapPrepareCallback.30039
+ __MPCAudioTapProcess.30034
+ __MPCAudioTapUnprepareCallback.30033
+ __MPCSPIRAddFailedStoreIDs.4287
+ __MPCSPIRCopyFailedStoreIDs.4230
+ __MPCSessionTypeIdentifierForStorefront.26799
+ __MPCSessionTypeIdentifierFromHashedDSID.26796
+ __OBJC_$_CLASS_METHODS_AVPlayerItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore)
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItem(MediaPlaybackCore|MediaPlaybackCore1|MediaPlaybackCore)
+ __PROTOCOL_PROPERTIES_MFAudioSessionControlling
+ ___129-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _classicalMusicAppPlaybackContextForPlayParametersQueue:]_block_invoke.118
+ ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.307
+ ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.308
+ ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.309
+ ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.316
+ ___164-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _playbackContextForStorePlayParameters:libraryItems:radioPlaybackContext:containsStartItem:]_block_invoke.49
+ ___164-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _playbackContextForStorePlayParameters:libraryItems:radioPlaybackContext:containsStartItem:]_block_invoke_2.52
+ ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke
+ ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke.29
+ ___204-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:]_block_invoke_2
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.199
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.203
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.209
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.223
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.246
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke_2.227
+ ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke_2.250
+ ___54-[_MPCPlaybackEnginePlayer donateMetricsToPlayerItem:]_block_invoke
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.347
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.354
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.355
+ ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_2.352
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.151
+ ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.165
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.361
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.387
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.451
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.493
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.503
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.512
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.526
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.539
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.546
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.553
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.574
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.578
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.585
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.594
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.612
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.395
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.452
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.500
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.507
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.522
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.530
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.542
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.554
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.399
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.456
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.532
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.558
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.404
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.460
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.563
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.416
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.464
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.568
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.420
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.471
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.424
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.472
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.431
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.476
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.435
+ ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.477
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke.202
+ ___60-[_MPCPlaybackEnginePlayer _updateActiveFormatForQueueItem:]_block_invoke_2
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.458
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.459
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.463
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.464
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.466
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke_2.465
+ ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke_2.467
+ ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.622
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.265
+ ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.284
+ ___69-[MPCPlayerResponseTracklist representativeSectionForDisplaySection:]_block_invoke
+ ___71-[MPCModelGenericAVItem _getSubscriptionLeasePropertiesWithCompletion:]_block_invoke.523
+ ___71-[MPCModelGenericAVItem _getSubscriptionLeasePropertiesWithCompletion:]_block_invoke.525
+ ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.528
+ ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.529
+ ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.532
+ ___82-[MPCModelGenericAVItem _getSubscriptionStatusWithStoreRequestContext:completion:]_block_invoke
+ ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.357
+ ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.405
+ ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.409
+ ___97-[MPCModelGenericAVItem _createOrUpdateDatabaseEntry:loadResult:urlBag:destinationURL:purgeable:]_block_invoke.303
+ ___Block_byref_object_copy_.11649
+ ___Block_byref_object_copy_.1223
+ ___Block_byref_object_copy_.12916
+ ___Block_byref_object_copy_.13472
+ ___Block_byref_object_copy_.14251
+ ___Block_byref_object_copy_.14622
+ ___Block_byref_object_copy_.1550
+ ___Block_byref_object_copy_.16746
+ ___Block_byref_object_copy_.17478
+ ___Block_byref_object_copy_.1756
+ ___Block_byref_object_copy_.18053
+ ___Block_byref_object_copy_.18836
+ ___Block_byref_object_copy_.1966
+ ___Block_byref_object_copy_.20474
+ ___Block_byref_object_copy_.21117
+ ___Block_byref_object_copy_.21590
+ ___Block_byref_object_copy_.21965
+ ___Block_byref_object_copy_.22637
+ ___Block_byref_object_copy_.22852
+ ___Block_byref_object_copy_.23077
+ ___Block_byref_object_copy_.23396
+ ___Block_byref_object_copy_.2483
+ ___Block_byref_object_copy_.25023
+ ___Block_byref_object_copy_.28072
+ ___Block_byref_object_copy_.29762
+ ___Block_byref_object_copy_.30042
+ ___Block_byref_object_copy_.30425
+ ___Block_byref_object_copy_.3047
+ ___Block_byref_object_copy_.30552
+ ___Block_byref_object_copy_.30677
+ ___Block_byref_object_copy_.31422
+ ___Block_byref_object_copy_.31880
+ ___Block_byref_object_copy_.32425
+ ___Block_byref_object_copy_.3880
+ ___Block_byref_object_copy_.4925
+ ___Block_byref_object_copy_.523
+ ___Block_byref_object_copy_.6652
+ ___Block_byref_object_copy_.7834
+ ___Block_byref_object_copy_.8139
+ ___Block_byref_object_copy_.951
+ ___Block_byref_object_copy_.9740
+ ___Block_byref_object_dispose_.11650
+ ___Block_byref_object_dispose_.1224
+ ___Block_byref_object_dispose_.12917
+ ___Block_byref_object_dispose_.13473
+ ___Block_byref_object_dispose_.14252
+ ___Block_byref_object_dispose_.14623
+ ___Block_byref_object_dispose_.1551
+ ___Block_byref_object_dispose_.16747
+ ___Block_byref_object_dispose_.17479
+ ___Block_byref_object_dispose_.1757
+ ___Block_byref_object_dispose_.18054
+ ___Block_byref_object_dispose_.18837
+ ___Block_byref_object_dispose_.1967
+ ___Block_byref_object_dispose_.20475
+ ___Block_byref_object_dispose_.21118
+ ___Block_byref_object_dispose_.21591
+ ___Block_byref_object_dispose_.21966
+ ___Block_byref_object_dispose_.22638
+ ___Block_byref_object_dispose_.22853
+ ___Block_byref_object_dispose_.23078
+ ___Block_byref_object_dispose_.23397
+ ___Block_byref_object_dispose_.2484
+ ___Block_byref_object_dispose_.25024
+ ___Block_byref_object_dispose_.28073
+ ___Block_byref_object_dispose_.29763
+ ___Block_byref_object_dispose_.30043
+ ___Block_byref_object_dispose_.30426
+ ___Block_byref_object_dispose_.3048
+ ___Block_byref_object_dispose_.30553
+ ___Block_byref_object_dispose_.30678
+ ___Block_byref_object_dispose_.31423
+ ___Block_byref_object_dispose_.31881
+ ___Block_byref_object_dispose_.32426
+ ___Block_byref_object_dispose_.3881
+ ___Block_byref_object_dispose_.4926
+ ___Block_byref_object_dispose_.524
+ ___Block_byref_object_dispose_.6653
+ ___Block_byref_object_dispose_.7835
+ ___Block_byref_object_dispose_.8140
+ ___Block_byref_object_dispose_.952
+ ___Block_byref_object_dispose_.9741
+ ___MPCSPIRFailedItemsLock.4231
+ ___block_descriptor_40_e8_32bs_e55_v24?0"ICMusicSubscriptionStatusResponse"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e47_v24?0"ICMusicSubscriptionStatus"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v16?0"MPCPlayerAudioFormat"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"MPCPlayerAudioFormat"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e80_v40?0"NSMutableArray"8^16"MPIdentifierSet"24"MPMusicPlayerPlayParameters"32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e113_v48?0"NSMutableArray"8^16"MPIdentifierSet"24"MPMusicPlayerPlayParameters"32"MPCModelRadioPlaybackContext"40ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.109.20485
+ ___block_literal_global.11295
+ ___block_literal_global.117.13235
+ ___block_literal_global.117.28135
+ ___block_literal_global.11731
+ ___block_literal_global.120
+ ___block_literal_global.12005
+ ___block_literal_global.121.2392
+ ___block_literal_global.12122
+ ___block_literal_global.123.13237
+ ___block_literal_global.123.4217
+ ___block_literal_global.125.13243
+ ___block_literal_global.125.2393
+ ___block_literal_global.127.13238
+ ___block_literal_global.13262
+ ___block_literal_global.13584
+ ___block_literal_global.1385
+ ___block_literal_global.13969
+ ___block_literal_global.14273
+ ___block_literal_global.1573
+ ___block_literal_global.16759
+ ___block_literal_global.17484
+ ___block_literal_global.18041
+ ___block_literal_global.19123
+ ___block_literal_global.19382
+ ___block_literal_global.19601
+ ___block_literal_global.20095
+ ___block_literal_global.20467
+ ___block_literal_global.21155
+ ___block_literal_global.21790
+ ___block_literal_global.21992
+ ___block_literal_global.22422
+ ___block_literal_global.226
+ ___block_literal_global.23179
+ ___block_literal_global.23398
+ ___block_literal_global.23804
+ ___block_literal_global.24822
+ ___block_literal_global.2512
+ ___block_literal_global.25661
+ ___block_literal_global.25801
+ ___block_literal_global.26955
+ ___block_literal_global.27205
+ ___block_literal_global.28152
+ ___block_literal_global.2824
+ ___block_literal_global.28883
+ ___block_literal_global.29143
+ ___block_literal_global.29281
+ ___block_literal_global.29740
+ ___block_literal_global.302
+ ___block_literal_global.30270
+ ___block_literal_global.30730
+ ___block_literal_global.30941
+ ___block_literal_global.31467
+ ___block_literal_global.316
+ ___block_literal_global.32.29141
+ ___block_literal_global.32465
+ ___block_literal_global.325
+ ___block_literal_global.3350
+ ___block_literal_global.384
+ ___block_literal_global.4.11720
+ ___block_literal_global.4.21777
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.42.28884
+ ___block_literal_global.4350
+ ___block_literal_global.44
+ ___block_literal_global.455
+ ___block_literal_global.505
+ ___block_literal_global.51
+ ___block_literal_global.513
+ ___block_literal_global.5183
+ ___block_literal_global.528
+ ___block_literal_global.541
+ ___block_literal_global.5495
+ ___block_literal_global.561
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.576
+ ___block_literal_global.58
+ ___block_literal_global.60
+ ___block_literal_global.65.26071
+ ___block_literal_global.6524
+ ___block_literal_global.675
+ ___block_literal_global.6955
+ ___block_literal_global.7109
+ ___block_literal_global.7899
+ ___block_literal_global.8324
+ ___block_literal_global.84.31356
+ ___block_literal_global.91.4227
+ ___block_literal_global.9847
+ ___block_literal_global.993
+ ___failedStoreIDs.4232
+ __activeTaps
+ __activeTapsLock
+ __unnamed_array_storage.11655
+ __unnamed_array_storage.11696
+ __unnamed_array_storage.12986
+ __unnamed_array_storage.14221
+ __unnamed_array_storage.18481
+ __unnamed_array_storage.19946
+ __unnamed_array_storage.207
+ __unnamed_array_storage.21581
+ __unnamed_array_storage.22345
+ __unnamed_array_storage.233
+ __unnamed_array_storage.238
+ __unnamed_array_storage.26075
+ __unnamed_array_storage.29115
+ __unnamed_array_storage.30055
+ __unnamed_array_storage.315
+ __unnamed_array_storage.321
+ __unnamed_array_storage.3373
+ __unnamed_array_storage.35
+ __unnamed_array_storage.39
+ __unnamed_array_storage.4260
+ _associated conformance So21AVMediaCharacteristicaSHSCSQ
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$AVPlayerItemPerformanceMetrics
+ _objc_msgSend$_filePathsForModelAtURL:
+ _objc_msgSend$_getSubscriptionStatusWithStoreRequestContext:completion:
+ _objc_msgSend$_prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:isStoreKeyServer:
+ _objc_msgSend$_registerForMPAVItemTitlesDidChangeNotification
+ _objc_msgSend$_setupQueueItemForVideoHLSPlayback:
+ _objc_msgSend$_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:
+ _objc_msgSend$audioFormatWithRenderingMode:
+ _objc_msgSend$audioProcessingTap
+ _objc_msgSend$donateMetricsToPlayerItem:
+ _objc_msgSend$loadCurrentTrackAudioFormatWithCompletion:
+ _objc_msgSend$maxResolution
+ _objc_msgSend$mpc_setReportingValue:forKey:
+ _objc_msgSend$mpc_setupWithSpatialPreference:maxResolution:
+ _objc_msgSend$renderingMode
+ _objc_msgSend$rewrittenAssetInfo
+ _objc_msgSend$setHasTimeMetadata:
+ _objc_msgSend$setIsStoreKeyServer:
+ _objc_msgSend$setRenderingMode:
+ _objc_msgSend$setReportingValueWithNumber:forKey:
+ _objc_msgSend$setReportingValueWithString:forKey:
+ _objc_msgSend$set_timeSinceBoot:
+ _objc_msgSend$set_timeSinceLaunch:
+ _objc_msgSend$set_timeSincePaused:
+ _objc_msgSend$skipDescendants
+ _objc_msgSend$spatialPreference
+ _objc_msgSend$timeSinceBoot
+ _objc_msgSend$timeSinceLaunch
+ _objc_msgSend$timeSincePaused
+ _sharedController.__sharedController.23805
+ _sharedController.onceToken.23803
+ _sharedManager.onceToken.28151
+ _symbolic So20MPCPlayerAudioFormatCSgSo7NSErrorCSgIeyByy_
+ _symbolic So24_MPCMediaRemotePublisherC
+ _symbolic So24_MPCMediaRemotePublisherCSgXw
+ _symbolic _____ So21AVMediaCharacteristica
+ _symbolic _____ So27AVAudioSessionRenderingModeV
+ _symbolic _____ So27AudioStreamBasicDescriptionV
+ _symbolic _____4mode______9timeStampt So27AVAudioSessionRenderingModeV 17MediaPlaybackCore9EventTimeC
- +[MPCVocalAttenuationModel _filePathsForModelAtURL:error:]
- -[MPCModelGenericAVItem _prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:]
- -[MPCModelGenericAVItem currentPlayerAudioFormat]
- GCC_except_table1013
- GCC_except_table1069
- GCC_except_table1118
- GCC_except_table1217
- GCC_except_table1356
- GCC_except_table1357
- GCC_except_table1361
- GCC_except_table1411
- GCC_except_table1420
- GCC_except_table1431
- GCC_except_table1556
- GCC_except_table1563
- GCC_except_table1570
- GCC_except_table1583
- GCC_except_table1615
- GCC_except_table1636
- GCC_except_table1655
- GCC_except_table1713
- GCC_except_table1814
- GCC_except_table1829
- GCC_except_table1857
- GCC_except_table1866
- GCC_except_table1870
- GCC_except_table2072
- GCC_except_table2140
- GCC_except_table2180
- GCC_except_table2193
- GCC_except_table2228
- GCC_except_table2422
- GCC_except_table2433
- GCC_except_table2442
- GCC_except_table2449
- GCC_except_table2483
- GCC_except_table2525
- GCC_except_table2526
- GCC_except_table2529
- GCC_except_table2534
- GCC_except_table2550
- GCC_except_table258
- GCC_except_table2612
- GCC_except_table283
- GCC_except_table285
- GCC_except_table292
- GCC_except_table2933
- GCC_except_table301
- GCC_except_table3078
- GCC_except_table3120
- GCC_except_table3210
- GCC_except_table3227
- GCC_except_table3229
- GCC_except_table3231
- GCC_except_table3232
- GCC_except_table3256
- GCC_except_table3260
- GCC_except_table3369
- GCC_except_table337
- GCC_except_table3372
- GCC_except_table3374
- GCC_except_table3379
- GCC_except_table3381
- GCC_except_table3384
- GCC_except_table3388
- GCC_except_table339
- GCC_except_table3398
- GCC_except_table3404
- GCC_except_table3473
- GCC_except_table3595
- GCC_except_table3596
- GCC_except_table3654
- GCC_except_table3659
- GCC_except_table3661
- GCC_except_table3755
- GCC_except_table3756
- GCC_except_table3832
- GCC_except_table4003
- GCC_except_table4033
- GCC_except_table4057
- GCC_except_table406
- GCC_except_table4061
- GCC_except_table4064
- GCC_except_table407
- GCC_except_table4108
- GCC_except_table4138
- GCC_except_table4186
- GCC_except_table4188
- GCC_except_table430
- GCC_except_table4342
- GCC_except_table4382
- GCC_except_table440
- GCC_except_table4453
- GCC_except_table4480
- GCC_except_table4488
- GCC_except_table4711
- GCC_except_table4712
- GCC_except_table479
- GCC_except_table480
- GCC_except_table4817
- GCC_except_table4826
- GCC_except_table4915
- GCC_except_table4922
- GCC_except_table4923
- GCC_except_table497
- GCC_except_table4973
- GCC_except_table4996
- GCC_except_table5042
- GCC_except_table5048
- GCC_except_table5088
- GCC_except_table5093
- GCC_except_table5137
- GCC_except_table5153
- GCC_except_table5164
- GCC_except_table5180
- GCC_except_table5221
- GCC_except_table5238
- GCC_except_table5244
- GCC_except_table5259
- GCC_except_table5260
- GCC_except_table5308
- GCC_except_table5309
- GCC_except_table549
- GCC_except_table5551
- GCC_except_table5554
- GCC_except_table5567
- GCC_except_table5570
- GCC_except_table5573
- GCC_except_table563
- GCC_except_table568
- GCC_except_table5940
- GCC_except_table5984
- GCC_except_table604
- GCC_except_table6046
- GCC_except_table6055
- GCC_except_table606
- GCC_except_table6064
- GCC_except_table6073
- GCC_except_table624
- GCC_except_table627
- GCC_except_table6322
- GCC_except_table6333
- GCC_except_table6383
- GCC_except_table6427
- GCC_except_table6428
- GCC_except_table6471
- GCC_except_table6476
- GCC_except_table6480
- GCC_except_table6498
- GCC_except_table6507
- GCC_except_table6610
- GCC_except_table662
- GCC_except_table6633
- GCC_except_table6648
- GCC_except_table6696
- GCC_except_table6721
- GCC_except_table6725
- GCC_except_table6883
- GCC_except_table6885
- GCC_except_table6997
- GCC_except_table703
- GCC_except_table734
- GCC_except_table790
- GCC_except_table885
- GCC_except_table891
- GCC_except_table905
- GCC_except_table963
- _MSVFastHexStringFromBytes.hexCharacters.27789
- __MPCAudioTapFinalize.29737
- __MPCAudioTapInit.29738
- __MPCAudioTapPrepareCallback.29736
- __MPCAudioTapProcess.29731
- __MPCAudioTapUnprepareCallback.29730
- __MPCSPIRAddFailedStoreIDs.4353
- __MPCSPIRCopyFailedStoreIDs.4296
- __MPCSessionTypeIdentifierForStorefront.26508
- __MPCSessionTypeIdentifierFromHashedDSID.26505
- __OBJC_$_CLASS_METHODS_AVPlayerItem(MediaPlaybackCore|MediaPlaybackCore)
- __OBJC_$_INSTANCE_METHODS_AVPlayerItem(MediaPlaybackCore|MediaPlaybackCore)
- ___129-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _classicalMusicAppPlaybackContextForPlayParametersQueue:]_block_invoke.116
- ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.291
- ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.292
- ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.294
- ___157-[MPCModelGenericAVItem _downloadHLSAsset:destinationURL:sharedCacheURL:assetLoadProperties:loadResult:storeRequestContext:urlBag:fileUpgradeRecommendation:]_block_invoke.301
- ___164-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _playbackContextForStorePlayParameters:libraryItems:radioPlaybackContext:containsStartItem:]_block_invoke.46
- ___164-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) _playbackContextForStorePlayParameters:libraryItems:radioPlaybackContext:containsStartItem:]_block_invoke_2.49
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.183
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.187
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.193
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.207
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke.230
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke_2.211
- ___47-[MPCModelGenericAVItem loadAssetAndPlayerItem]_block_invoke_2.234
- ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.332
- ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.339
- ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke.340
- ___58-[MPCModelGenericAVItem prepareForRate:completionHandler:]_block_invoke_2.337
- ___59-[MPCPlaybackEngineLoggingConsumer subscribeToEventStream:]_block_invoke.152
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.358
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.384
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.448
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.490
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.500
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.509
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.523
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.533
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.540
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.541
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.568
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.572
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.579
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.588
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke.606
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.392
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.449
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.497
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.504
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.519
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.527
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.536
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_2.548
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.396
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.453
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.529
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_3.552
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.401
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.457
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_4.557
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.413
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.461
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_5.562
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.417
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_6.468
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.421
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_7.469
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.428
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_8.473
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.432
- ___60-[_MPCMediaRemotePublisher _performCommandEvent:completion:]_block_invoke_9.474
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.443
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.444
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.448
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.449
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke.451
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke_2.450
- ___61-[MPCModelGenericAVItem resolvePlaybackError:withCompletion:]_block_invoke_2.452
- ___65-[_MPCMediaRemotePublisher performSetQueueWithIntent:completion:]_block_invoke.616
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.256
- ___69+[MPCPlayPerfMetrics playMetricsWithItemReadyForMetricsEvent:cursor:]_block_invoke.275
- ___71-[MPCModelGenericAVItem _getSubscriptionLeasePropertiesWithCompletion:]_block_invoke.506
- ___71-[MPCModelGenericAVItem _getSubscriptionLeasePropertiesWithCompletion:]_block_invoke.508
- ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.511
- ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.512
- ___78-[MPCModelGenericAVItem _getUnverifiedSubscriptionLeaseSessionWithCompletion:]_block_invoke.515
- ___89-[MPMusicPlayerPlayParametersQueueDescriptor(MPCModelPlaybackAdditions) playbackContexts]_block_invoke.26
- ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.342
- ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.390
- ___90-[MPCModelGenericAVItem _prepareLeaseWithShouldRequireLeaseAcquisition:completionHandler:]_block_invoke.394
- ___97-[MPCModelGenericAVItem _createOrUpdateDatabaseEntry:loadResult:urlBag:destinationURL:purgeable:]_block_invoke.287
- ___Block_byref_object_copy_.1125
- ___Block_byref_object_copy_.11498
- ___Block_byref_object_copy_.12773
- ___Block_byref_object_copy_.13330
- ___Block_byref_object_copy_.14109
- ___Block_byref_object_copy_.14480
- ___Block_byref_object_copy_.1466
- ___Block_byref_object_copy_.16605
- ___Block_byref_object_copy_.1671
- ___Block_byref_object_copy_.17313
- ___Block_byref_object_copy_.17879
- ___Block_byref_object_copy_.18642
- ___Block_byref_object_copy_.1881
- ___Block_byref_object_copy_.20271
- ___Block_byref_object_copy_.20913
- ___Block_byref_object_copy_.21385
- ___Block_byref_object_copy_.21760
- ___Block_byref_object_copy_.22430
- ___Block_byref_object_copy_.22645
- ___Block_byref_object_copy_.22871
- ___Block_byref_object_copy_.23187
- ___Block_byref_object_copy_.24819
- ___Block_byref_object_copy_.2489
- ___Block_byref_object_copy_.27775
- ___Block_byref_object_copy_.29462
- ___Block_byref_object_copy_.29739
- ___Block_byref_object_copy_.30123
- ___Block_byref_object_copy_.30250
- ___Block_byref_object_copy_.30375
- ___Block_byref_object_copy_.3056
- ___Block_byref_object_copy_.31121
- ___Block_byref_object_copy_.31579
- ___Block_byref_object_copy_.32109
- ___Block_byref_object_copy_.3944
- ___Block_byref_object_copy_.486
- ___Block_byref_object_copy_.4926
- ___Block_byref_object_copy_.6636
- ___Block_byref_object_copy_.7789
- ___Block_byref_object_copy_.8094
- ___Block_byref_object_copy_.901
- ___Block_byref_object_copy_.9678
- ___Block_byref_object_dispose_.1126
- ___Block_byref_object_dispose_.11499
- ___Block_byref_object_dispose_.12774
- ___Block_byref_object_dispose_.13331
- ___Block_byref_object_dispose_.14110
- ___Block_byref_object_dispose_.14481
- ___Block_byref_object_dispose_.1467
- ___Block_byref_object_dispose_.16606
- ___Block_byref_object_dispose_.1672
- ___Block_byref_object_dispose_.17314
- ___Block_byref_object_dispose_.17880
- ___Block_byref_object_dispose_.18643
- ___Block_byref_object_dispose_.1882
- ___Block_byref_object_dispose_.20272
- ___Block_byref_object_dispose_.20914
- ___Block_byref_object_dispose_.21386
- ___Block_byref_object_dispose_.21761
- ___Block_byref_object_dispose_.22431
- ___Block_byref_object_dispose_.22646
- ___Block_byref_object_dispose_.22872
- ___Block_byref_object_dispose_.23188
- ___Block_byref_object_dispose_.24820
- ___Block_byref_object_dispose_.2490
- ___Block_byref_object_dispose_.27776
- ___Block_byref_object_dispose_.29463
- ___Block_byref_object_dispose_.29740
- ___Block_byref_object_dispose_.30124
- ___Block_byref_object_dispose_.30251
- ___Block_byref_object_dispose_.30376
- ___Block_byref_object_dispose_.3057
- ___Block_byref_object_dispose_.31122
- ___Block_byref_object_dispose_.31580
- ___Block_byref_object_dispose_.32110
- ___Block_byref_object_dispose_.3945
- ___Block_byref_object_dispose_.487
- ___Block_byref_object_dispose_.4927
- ___Block_byref_object_dispose_.6637
- ___Block_byref_object_dispose_.7790
- ___Block_byref_object_dispose_.8095
- ___Block_byref_object_dispose_.902
- ___Block_byref_object_dispose_.9679
- ___MPCSPIRFailedItemsLock.4297
- ___block_descriptor_48_e8_32s40bs_e55_v24?0"ICMusicSubscriptionStatusResponse"8"NSError"16ls32l8s40l8
- ___block_literal_global.109.20282
- ___block_literal_global.11144
- ___block_literal_global.115.13097
- ___block_literal_global.11580
- ___block_literal_global.117.27838
- ___block_literal_global.118
- ___block_literal_global.11854
- ___block_literal_global.11979
- ___block_literal_global.121.13099
- ___block_literal_global.121.2398
- ___block_literal_global.123.13105
- ___block_literal_global.123.4283
- ___block_literal_global.125.13100
- ___block_literal_global.125.2399
- ___block_literal_global.1298
- ___block_literal_global.13123
- ___block_literal_global.13442
- ___block_literal_global.13827
- ___block_literal_global.14131
- ___block_literal_global.1489
- ___block_literal_global.16618
- ___block_literal_global.17319
- ___block_literal_global.17867
- ___block_literal_global.18914
- ___block_literal_global.19177
- ___block_literal_global.19396
- ___block_literal_global.19892
- ___block_literal_global.20264
- ___block_literal_global.20951
- ___block_literal_global.210
- ___block_literal_global.21585
- ___block_literal_global.21787
- ___block_literal_global.22217
- ___block_literal_global.22973
- ___block_literal_global.23189
- ___block_literal_global.23595
- ___block_literal_global.24618
- ___block_literal_global.2518
- ___block_literal_global.25393
- ___block_literal_global.25532
- ___block_literal_global.26662
- ___block_literal_global.26908
- ___block_literal_global.27855
- ___block_literal_global.2830
- ___block_literal_global.28586
- ___block_literal_global.286
- ___block_literal_global.28840
- ___block_literal_global.28981
- ___block_literal_global.29440
- ___block_literal_global.29968
- ___block_literal_global.30428
- ___block_literal_global.30639
- ___block_literal_global.310
- ___block_literal_global.31166
- ___block_literal_global.313
- ___block_literal_global.32149
- ___block_literal_global.3411
- ___block_literal_global.35
- ___block_literal_global.383
- ___block_literal_global.4.11569
- ___block_literal_global.4.21572
- ___block_literal_global.403
- ___block_literal_global.41
- ___block_literal_global.418
- ___block_literal_global.42.28587
- ___block_literal_global.440
- ___block_literal_global.4415
- ___block_literal_global.45
- ___block_literal_global.498.4756
- ___block_literal_global.499
- ___block_literal_global.5170
- ___block_literal_global.52
- ___block_literal_global.525
- ___block_literal_global.535
- ___block_literal_global.5484
- ___block_literal_global.555
- ___block_literal_global.559
- ___block_literal_global.559.3075
- ___block_literal_global.564
- ___block_literal_global.57
- ___block_literal_global.605
- ___block_literal_global.65.25794
- ___block_literal_global.6508
- ___block_literal_global.6923
- ___block_literal_global.7061
- ___block_literal_global.7854
- ___block_literal_global.8279
- ___block_literal_global.84.31055
- ___block_literal_global.91.4293
- ___block_literal_global.9785
- ___block_literal_global.996
- ___failedStoreIDs.4298
- __unnamed_array_storage.11504
- __unnamed_array_storage.11545
- __unnamed_array_storage.11956
- __unnamed_array_storage.12843
- __unnamed_array_storage.14079
- __unnamed_array_storage.18300
- __unnamed_array_storage.191
- __unnamed_array_storage.19744
- __unnamed_array_storage.21373
- __unnamed_array_storage.22137
- __unnamed_array_storage.230
- __unnamed_array_storage.235
- __unnamed_array_storage.25798
- __unnamed_array_storage.28824
- __unnamed_array_storage.29752
- __unnamed_array_storage.300
- __unnamed_array_storage.303
- __unnamed_array_storage.33
- __unnamed_array_storage.3434
- __unnamed_array_storage.37
- __unnamed_array_storage.4326
- _objc_msgSend$URLByDeletingLastPathComponent
- _objc_msgSend$_filePathsForModelAtURL:error:
- _objc_msgSend$_prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:
- _objc_msgSend$currentPlayerAudioFormat
- _objc_msgSend$mpc_setupWithAudioAssetType:forceSpatial:
- _sharedController.__sharedController.23596
- _sharedController.onceToken.23594
- _sharedManager.onceToken.27854
- _symbolic So24_MPCMediaRemotePublisherCXo
CStrings:
+ "@56@0:8q16I24B28B32I36q40@48"
+ "DolbyAtmos"
+ "DolbyAudio"
+ "MonoStereo"
+ "Playback engine deallocated"
+ "SpatialAudio"
+ "Surround"
+ "T@\"NSNumber\",&,D,N,Sset_timeSinceBoot:"
+ "T@\"NSNumber\",&,D,N,Sset_timeSinceLaunch:"
+ "T@\"NSNumber\",&,D,N,Sset_timeSincePaused:"
+ "T^{opaqueMTAudioProcessingTap=},R,N"
+ "Tq,R,N,V_renderingMode"
+ "Unsupported model object type %@"
+ "[%{public}@]-%{public}@ - Failed to load track audio format for stableVariantID=%{public}@ error=%{public}@"
+ "[%{public}@]-%{public}@ - No session-data audio format found for stableVariantID=%{public}@"
+ "[%{public}@]-%{public}@ - renderingModeDidChange:%ld"
+ "[%{public}@]-[AL] - %{public}@: Original asset %{public}@ is rewrriten by defaults with %{public}@"
+ "[BMUS:%{public}@:%{public}@] enumerator nextObject: | returning nil [encountered radio tail while reverse enumerating in display mode] sectionID=%{public}@"
+ "[PBLSH:%{public}@] _performCommandEvent:%{public}@… | failing CreateRadioStation command [unsupported model object type] type=%{public}@"
+ "^{opaqueMTAudioProcessingTap=}16@0:8"
+ "_filePathsForModelAtURL:"
+ "_getSubscriptionStatusWithStoreRequestContext:completion:"
+ "_handleMPAVItemTitlesDidChange:"
+ "_prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:isStoreKeyServer:"
+ "_registerForMPAVItemTitlesDidChangeNotification"
+ "_renderingMode"
+ "_setupQueueItemForVideoHLSPlayback:"
+ "_updatePlaybackContextsForPlaybackParametersQueue:libraryItems:radioPlaybackContext:storePlayParameters:contexts:containsStartItem:"
+ "assetTrack"
+ "audio-rendering-mode"
+ "audio-rendering-mode-changed"
+ "audioFormatWithRenderingMode:"
+ "audioProcessingTap"
+ "bin"
+ "czutbtg4y9"
+ "donateMetricsToPlayerItem:"
+ "initWithTier:codec:spatialized:multiChannel:channelLayout:sampleRate:stableVariantID:"
+ "isStoreKeyServer"
+ "item is not a Song"
+ "keyCertURL"
+ "loadCurrentTrackAudioFormatWithCompletion:"
+ "maxResolution"
+ "mil"
+ "mpc_setReportingValue:forKey:"
+ "mpc_setupWithSpatialPreference:maxResolution:"
+ "msc_AL"
+ "msc_FAF"
+ "msc_MPP"
+ "msc_MPT"
+ "msc_MWT"
+ "msc_QL"
+ "msc_RC"
+ "msc_RTP"
+ "msc_SQ"
+ "msc_accountInfo"
+ "msc_acrtiveAccount"
+ "msc_asstLoc"
+ "msc_asstSource"
+ "msc_asstType"
+ "msc_autoPlay"
+ "msc_delegatedPB"
+ "msc_endpointType"
+ "msc_errorResAppld"
+ "msc_errorSig"
+ "msc_experimentID"
+ "msc_featureName"
+ "msc_firstItem"
+ "msc_firstPlay"
+ "msc_nwTime"
+ "msc_nwType"
+ "msc_offlinePBkeys"
+ "msc_onlinePBkeys"
+ "msc_protectionType"
+ "msc_queueComType"
+ "msc_queueType"
+ "msc_remoteSQ"
+ "msc_replacingPB"
+ "msc_routeType"
+ "msc_seek"
+ "msc_sharePlay"
+ "msc_shuffled"
+ "msc_storefront"
+ "msc_treatmentID"
+ "public.binaural-for-headphones"
+ "rdm"
+ "rendering: %@"
+ "renderingMode"
+ "renderingModeDidChange: "
+ "renderingModeDidChange:timeStamp:"
+ "representativeSectionForDisplaySection:"
+ "rewrittenAssetInfo"
+ "s"
+ "setHasTimeMetadata:"
+ "setIsStoreKeyServer:"
+ "setRenderingMode:"
+ "setReportingValueWithNumber:forKey:"
+ "setReportingValueWithString:forKey:"
+ "set_timeSinceBoot:"
+ "set_timeSinceLaunch:"
+ "set_timeSincePaused:"
+ "skipDescendants"
+ "spatialPreference"
+ "timeSinceBoot"
+ "timeSinceLaunch"
+ "timeSincePaused"
+ "v16@?0@\"MPCPlayerAudioFormat\"8"
+ "v24@0:8@?<v@?@\"MPCPlayerAudioFormat\"@\"NSError\">16"
+ "v24@?0@\"MPCPlayerAudioFormat\"8@\"NSError\"16"
+ "v32@0:8q16@\"<MFTimeStamp>\"24"
+ "v32@0:8q16q24"
+ "v32@?0@\"NSString\"8q16^B24"
+ "v40@?0@\"NSMutableArray\"8^@16@\"MPIdentifierSet\"24@\"MPMusicPlayerPlayParameters\"32"
+ "v48@?0@\"NSMutableArray\"8^@16@\"MPIdentifierSet\"24@\"MPMusicPlayerPlayParameters\"32@\"MPCModelRadioPlaybackContext\"40"
+ "v64@0:8@16@24@32@40@48^@56"
+ "v68@0:8@16@24@32@40@48@56B64"
+ "vi-nnet.mil"
+ "vi-nnet.weight.bin"
+ "|%{public}@ %{public}@ %2i %{public}@\U00100951 RENDERING MODE CHANGE      %{public}@"
- "URLByDeletingLastPathComponent"
- "[%{public}@]-%{public}@ - No existing formats on item"
- "[%{public}@]-%{public}@ - active audio format from AV: %{public}@"
- "[AP] - MPCVAModel - Error getting content of directory at URL %{public}@: %{public}@"
- "[AP] - MPCVAModel - Missing model file for extension %{public}@ - Files:%{public}@ - Found files: %{public}@"
- "_filePathsForModelAtURL:error:"
- "_prepareAssetForHLSPlayback:loadResult:destinationURL:storeRequestContext:urlBag:identityProperties:"
- "aufx-nnet-appl"
- "c"
- "currentPlayerAudioFormat"
- "espresso"
- "net"
- "shape"
- "v64@0:8@16@24@32@40@48@56"
- "weights"

```
