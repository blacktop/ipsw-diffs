## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-608.1.119.0.0
-  __TEXT.__text: 0xbf7cc
-  __TEXT.__auth_stubs: 0x1d50
-  __TEXT.__objc_methlist: 0x92fc
+612.0.160.0.0
+  __TEXT.__text: 0xc0358
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_methlist: 0x939c
   __TEXT.__const: 0x2bc8
-  __TEXT.__gcc_except_tab: 0x29d8
-  __TEXT.__cstring: 0xbf62
-  __TEXT.__oslogstring: 0x64a3
-  __TEXT.__dlopen_cstrs: 0xa7
-  __TEXT.__unwind_info: 0x2e4c
+  __TEXT.__gcc_except_tab: 0x29f0
+  __TEXT.__cstring: 0xbf0b
+  __TEXT.__oslogstring: 0x6599
+  __TEXT.__dlopen_cstrs: 0x15f
+  __TEXT.__unwind_info: 0x2e7c
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1206
-  __TEXT.__objc_methname: 0x190fd
-  __TEXT.__objc_methtype: 0x4e8d
-  __TEXT.__objc_stubs: 0xec60
+  __TEXT.__objc_classname: 0x122e
+  __TEXT.__objc_methname: 0x193d1
+  __TEXT.__objc_methtype: 0x4fac
+  __TEXT.__objc_stubs: 0xed80
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x25c0
+  __DATA_CONST.__const: 0x2610
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10450
-  __DATA_CONST.__objc_selrefs: 0x5268
+  __DATA_CONST.__objc_const: 0x10520
+  __DATA_CONST.__objc_selrefs: 0x52d8
   __DATA_CONST.__objc_arraydata: 0x7d0
-  __AUTH_CONST.__cfstring: 0xab40
+  __AUTH_CONST.__cfstring: 0xabe0
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x1a0
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0xec0
+  __AUTH_CONST.__auth_got: 0xed8
   __DATA.__got_weak: 0xe0
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x5a0
   __DATA.__objc_superrefs: 0x310
-  __DATA.__objc_ivar: 0xb24
+  __DATA.__objc_ivar: 0xb34
   __DATA.__data: 0x1138
-  __DATA.__bss: 0x4a0
+  __DATA.__bss: 0x4c0
   __DATA_DIRTY.__const: 0x1330
   __DATA_DIRTY.__objc_const: 0x38d0
   __DATA_DIRTY.__objc_data: 0x2cb0
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x970
+  __DATA_DIRTY.__bss: 0x950
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6ADCE418-AAE6-32F9-9EF0-895DEA99C671
-  Functions: 4108
-  Symbols:   14161
-  CStrings:  8251
+  UUID: 7E091E70-D463-3DEB-A4C4-CBF3A5A87799
+  Functions: 4126
+  Symbols:   14219
+  CStrings:  8292
 
Symbols:
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) copyCGImageFromImageGenerator:atTime:actualTime:error:]
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) insertTimeRange:ofAsset:atTime:intoMutableComposition:error:]
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) metadataForFormat:forAsset:]
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) metadataForFormat:forAssetTrack:]
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) trackWithTrackID:forAsset:]
+ +[PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers) tracksWithMediaType:forAsset:]
+ -[PFMetadataCore setSpatialVideoRecommendationForImmersiveMode:]
+ -[PFMetadataCore spatialVideoRecommendationForImmersiveMode]
+ -[PFMetadataMovie _spatialVideoRecommendationForImmersiveModeForAssetVideoTrack:]
+ -[PFParallaxIntermediateLayout hasTopEdgeContact]
+ -[PFParallaxIntermediateLayout initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:hasTopEdgeContact:]
+ -[PFParallaxLayoutHelper hasTopEdgeContact]
+ -[PFParallaxLayoutHelper initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:]
+ -[PFPosterOrientedLayout canApplyHeadroom]
+ -[PFPosterOrientedLayout hasTopEdgeContact]
+ -[PFPosterOrientedLayout initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:]
+ -[PFPosterShuffleConfiguration albumCloudIdentifiers]
+ -[PFPosterShuffleConfiguration setAlbumCloudIdentifiers:]
+ GCC_except_table1198
+ GCC_except_table1300
+ GCC_except_table1307
+ GCC_except_table1310
+ GCC_except_table1349
+ GCC_except_table1363
+ GCC_except_table1463
+ GCC_except_table1509
+ GCC_except_table1530
+ GCC_except_table1532
+ GCC_except_table1608
+ GCC_except_table1612
+ GCC_except_table1623
+ GCC_except_table1659
+ GCC_except_table1661
+ GCC_except_table1682
+ GCC_except_table1697
+ GCC_except_table1701
+ GCC_except_table1708
+ GCC_except_table1719
+ GCC_except_table1731
+ GCC_except_table1800
+ GCC_except_table1836
+ GCC_except_table1846
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1867
+ GCC_except_table1923
+ GCC_except_table1932
+ GCC_except_table1952
+ GCC_except_table2016
+ GCC_except_table2019
+ GCC_except_table2026
+ GCC_except_table2152
+ GCC_except_table2159
+ GCC_except_table2161
+ GCC_except_table2162
+ GCC_except_table2164
+ GCC_except_table2167
+ GCC_except_table2211
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2329
+ GCC_except_table2501
+ GCC_except_table2566
+ GCC_except_table2571
+ GCC_except_table2582
+ GCC_except_table2585
+ GCC_except_table2592
+ GCC_except_table2596
+ GCC_except_table2603
+ GCC_except_table2604
+ GCC_except_table2605
+ GCC_except_table2606
+ GCC_except_table2608
+ GCC_except_table2609
+ GCC_except_table2625
+ GCC_except_table2627
+ GCC_except_table2629
+ GCC_except_table2635
+ GCC_except_table2636
+ GCC_except_table2637
+ GCC_except_table2659
+ GCC_except_table2661
+ GCC_except_table2662
+ GCC_except_table2667
+ GCC_except_table2668
+ GCC_except_table2670
+ GCC_except_table2671
+ GCC_except_table2681
+ GCC_except_table2684
+ GCC_except_table2739
+ GCC_except_table2831
+ GCC_except_table2833
+ GCC_except_table2835
+ GCC_except_table2837
+ GCC_except_table2839
+ GCC_except_table2841
+ GCC_except_table2843
+ GCC_except_table2847
+ GCC_except_table2857
+ GCC_except_table2859
+ GCC_except_table2865
+ GCC_except_table2866
+ GCC_except_table2867
+ GCC_except_table2879
+ GCC_except_table2892
+ GCC_except_table2893
+ GCC_except_table2900
+ GCC_except_table2901
+ GCC_except_table2903
+ GCC_except_table2904
+ GCC_except_table2905
+ GCC_except_table2906
+ GCC_except_table2917
+ GCC_except_table2951
+ GCC_except_table2961
+ GCC_except_table2965
+ GCC_except_table2968
+ GCC_except_table2969
+ GCC_except_table3017
+ GCC_except_table3026
+ GCC_except_table3079
+ GCC_except_table3147
+ GCC_except_table3149
+ GCC_except_table3166
+ GCC_except_table3191
+ GCC_except_table3193
+ GCC_except_table3430
+ GCC_except_table3432
+ GCC_except_table3434
+ GCC_except_table3441
+ GCC_except_table3446
+ GCC_except_table3466
+ GCC_except_table3468
+ GCC_except_table3472
+ GCC_except_table3498
+ GCC_except_table3499
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3510
+ GCC_except_table3512
+ GCC_except_table3515
+ GCC_except_table3520
+ GCC_except_table3521
+ GCC_except_table3522
+ GCC_except_table3523
+ GCC_except_table3524
+ GCC_except_table3525
+ GCC_except_table3526
+ GCC_except_table3529
+ GCC_except_table3532
+ GCC_except_table3552
+ GCC_except_table3557
+ GCC_except_table3567
+ GCC_except_table3577
+ GCC_except_table3584
+ GCC_except_table3593
+ GCC_except_table3594
+ GCC_except_table3596
+ GCC_except_table3597
+ GCC_except_table3598
+ GCC_except_table3599
+ GCC_except_table3600
+ GCC_except_table3601
+ GCC_except_table3603
+ GCC_except_table3604
+ GCC_except_table3606
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3610
+ GCC_except_table3613
+ GCC_except_table3676
+ GCC_except_table3743
+ GCC_except_table3749
+ GCC_except_table3818
+ GCC_except_table3822
+ GCC_except_table3824
+ GCC_except_table3828
+ GCC_except_table3857
+ GCC_except_table3858
+ GCC_except_table3859
+ GCC_except_table3861
+ GCC_except_table3863
+ GCC_except_table4098
+ GCC_except_table4105
+ GCC_except_table4107
+ GCC_except_table585
+ GCC_except_table713
+ GCC_except_table724
+ GCC_except_table727
+ GCC_except_table781
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table849
+ GCC_except_table852
+ GCC_except_table864
+ GCC_except_table867
+ GCC_except_table877
+ GCC_except_table881
+ GCC_except_table882
+ GCC_except_table890
+ GCC_except_table895
+ GCC_except_table904
+ GCC_except_table905
+ GCC_except_table910
+ GCC_except_table918
+ GCC_except_table921
+ GCC_except_table926
+ GCC_except_table935
+ GCC_except_table939
+ GCC_except_table943
+ GCC_except_table963
+ GCC_except_table966
+ GCC_except_table978
+ GCC_except_table979
+ _OBJC_IVAR_$_PFMetadataCore._spatialVideoRecommendationForImmersiveMode
+ _OBJC_IVAR_$_PFParallaxIntermediateLayout._hasTopEdgeContact
+ _OBJC_IVAR_$_PFParallaxLayoutHelper._hasTopEdgeContact
+ _OBJC_IVAR_$_PFPosterOrientedLayout._hasTopEdgeContact
+ _OBJC_IVAR_$_PFPosterShuffleConfiguration._albumCloudIdentifiers
+ _PFDeviceLockScreenApproximateTimeRectNormalized_SBS
+ _PFPosterShuffleFavoriteAlbumCloudIdentifier
+ _PosterBoardUIServicesLibraryCore.frameworkLibrary
+ _PosterKitLibraryCore.frameworkLibrary
+ _Vertices.11051
+ __AuxiliaryImageCVPixelBufferReleaseBytesCallback.3660
+ __OBJC_$_CLASS_METHODS_PFMediaUtilities(DeprecatedAVFoundationSyncAPIHelpers)
+ __OBJC_$_PROP_LIST_PFMetadataCore.646
+ __OBJC_$_PROP_LIST_PFMetadataImage.6216
+ __ZN5boost12interprocessL8ec_tableE.7884
+ ___86-[PFLivePhotoEditSession _prepareForPlaybackWithTargetSize:options:completionHandler:]_block_invoke.107
+ ___86-[PFLivePhotoEditSession _prepareForPlaybackWithTargetSize:options:completionHandler:]_block_invoke_2.110
+ ___Block_byref_object_copy_.10810
+ ___Block_byref_object_copy_.11438
+ ___Block_byref_object_copy_.12688
+ ___Block_byref_object_copy_.4187
+ ___Block_byref_object_copy_.4742
+ ___Block_byref_object_copy_.5094
+ ___Block_byref_object_copy_.5208
+ ___Block_byref_object_copy_.5770
+ ___Block_byref_object_copy_.6450
+ ___Block_byref_object_copy_.7413
+ ___Block_byref_object_copy_.8315
+ ___Block_byref_object_copy_.8823
+ ___Block_byref_object_copy_.9097
+ ___Block_byref_object_copy_.9509
+ ___Block_byref_object_dispose_.10811
+ ___Block_byref_object_dispose_.11439
+ ___Block_byref_object_dispose_.12689
+ ___Block_byref_object_dispose_.4188
+ ___Block_byref_object_dispose_.4743
+ ___Block_byref_object_dispose_.5095
+ ___Block_byref_object_dispose_.5209
+ ___Block_byref_object_dispose_.5771
+ ___Block_byref_object_dispose_.6451
+ ___Block_byref_object_dispose_.7414
+ ___Block_byref_object_dispose_.8316
+ ___Block_byref_object_dispose_.8824
+ ___Block_byref_object_dispose_.9098
+ ___Block_byref_object_dispose_.9510
+ ___PFDeviceLockScreenApproximateTimeRectNormalized_SBS_block_invoke
+ ___PosterBoardUIServicesLibraryCore_block_invoke
+ ___PosterKitLibraryCore_block_invoke
+ ___block_literal_global.102.2248
+ ___block_literal_global.10804
+ ___block_literal_global.11097
+ ___block_literal_global.11435
+ ___block_literal_global.11687
+ ___block_literal_global.11831
+ ___block_literal_global.12.5780
+ ___block_literal_global.12231
+ ___block_literal_global.123.8812
+ ___block_literal_global.12380
+ ___block_literal_global.12506
+ ___block_literal_global.127.5591
+ ___block_literal_global.132.5586
+ ___block_literal_global.1355
+ ___block_literal_global.142.10364
+ ___block_literal_global.1501
+ ___block_literal_global.162.10286
+ ___block_literal_global.2085
+ ___block_literal_global.2303
+ ___block_literal_global.2526
+ ___block_literal_global.3337
+ ___block_literal_global.3492
+ ___block_literal_global.3784
+ ___block_literal_global.4046
+ ___block_literal_global.4279
+ ___block_literal_global.4340
+ ___block_literal_global.4349
+ ___block_literal_global.4755
+ ___block_literal_global.4926
+ ___block_literal_global.5151
+ ___block_literal_global.5233
+ ___block_literal_global.5608
+ ___block_literal_global.57.4337
+ ___block_literal_global.5704
+ ___block_literal_global.5750
+ ___block_literal_global.5762
+ ___block_literal_global.6502
+ ___block_literal_global.6560
+ ___block_literal_global.6847
+ ___block_literal_global.7117
+ ___block_literal_global.7260
+ ___block_literal_global.8.12377
+ ___block_literal_global.8018
+ ___block_literal_global.8873
+ ___block_literal_global.909
+ ___block_literal_global.9253
+ ___block_literal_global.9625
+ ___block_literal_global.97.8830
+ ___getPRPosterRoleLockScreenSymbolLoc_block_invoke
+ ___getPRUISPosterLayoutUtilitiesClass_block_invoke
+ __exifDateTimeFormatter.dateTimeFormatter.5705
+ __exifDateTimeFormatter.onceToken.5703
+ __exifSubsecTimeFormatter.onceToken.5689
+ __exifSubsecTimeFormatter.subsecTimeFormatter.5690
+ __gpsDateFormatter.dateFormatter.5726
+ __gpsDateFormatter.onceToken.5725
+ __gpsTimeFormatter.onceToken.5730
+ __gpsTimeFormatter.timeFormatter.5731
+ __unnamed_array_storage.10269
+ __unnamed_array_storage.12742
+ __unnamed_array_storage.134.4509
+ __unnamed_array_storage.1819
+ __unnamed_array_storage.191.2521
+ __unnamed_array_storage.2089
+ __unnamed_array_storage.2525
+ __unnamed_array_storage.3358
+ __unnamed_array_storage.366
+ __unnamed_array_storage.4094
+ __unnamed_array_storage.4675
+ __unnamed_array_storage.50
+ __unnamed_array_storage.6476
+ __unnamed_array_storage.8011
+ __unnamed_array_storage.9262
+ _audit_stringPosterBoardUIServices
+ _audit_stringPosterKit
+ _dlerror
+ _dlsym
+ _getPRPosterRoleLockScreenSymbolLoc.ptr
+ _getPRUISPosterLayoutUtilitiesClass.softClass
+ _objc_msgSend$_spatialVideoRecommendationForImmersiveModeForAssetVideoTrack:
+ _objc_msgSend$albumCloudIdentifiers
+ _objc_msgSend$canApplyHeadroom
+ _objc_msgSend$copyCGImageAtTime:actualTime:error:
+ _objc_msgSend$hasTopEdgeContact
+ _objc_msgSend$initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:
+ _objc_msgSend$initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:
+ _objc_msgSend$initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:hasTopEdgeContact:
+ _objc_msgSend$insertTimeRange:ofAsset:atTime:intoMutableComposition:error:
+ _objc_msgSend$metadataForFormat:forAssetTrack:
+ _objc_msgSend$setSpatialVideoRecommendationForImmersiveMode:
+ _objc_msgSend$titleBoundsForLayout:orientation:role:error:
+ _objc_msgSend$trackWithTrackID:
+ _objc_msgSend$tracksWithMediaType:forAsset:
+ _objc_retain_x6
- -[PFMetadataCore isSpatialVideoRecommendedForImmersiveMode]
- -[PFMetadataCore setIsSpatialVideoRecommendedForImmersiveMode:]
- -[PFMetadataMovie _isSpatialVideoRecommendedForImmersiveModeForAssetVideoTrack:]
- -[PFParallaxIntermediateLayout initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:]
- -[PFParallaxLayoutHelper initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:layoutType:layoutConfiguration:]
- GCC_except_table1196
- GCC_except_table1298
- GCC_except_table1305
- GCC_except_table1308
- GCC_except_table1347
- GCC_except_table1361
- GCC_except_table1461
- GCC_except_table1501
- GCC_except_table1522
- GCC_except_table1524
- GCC_except_table1600
- GCC_except_table1604
- GCC_except_table1615
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1674
- GCC_except_table1689
- GCC_except_table1693
- GCC_except_table1700
- GCC_except_table1711
- GCC_except_table1723
- GCC_except_table1792
- GCC_except_table1828
- GCC_except_table1838
- GCC_except_table1843
- GCC_except_table1854
- GCC_except_table1910
- GCC_except_table1919
- GCC_except_table1939
- GCC_except_table2003
- GCC_except_table2006
- GCC_except_table2013
- GCC_except_table2138
- GCC_except_table2139
- GCC_except_table2146
- GCC_except_table2148
- GCC_except_table2149
- GCC_except_table2154
- GCC_except_table2198
- GCC_except_table2221
- GCC_except_table2223
- GCC_except_table2316
- GCC_except_table2486
- GCC_except_table2551
- GCC_except_table2552
- GCC_except_table2556
- GCC_except_table2558
- GCC_except_table2560
- GCC_except_table2562
- GCC_except_table2570
- GCC_except_table2579
- GCC_except_table2581
- GCC_except_table2589
- GCC_except_table2591
- GCC_except_table2593
- GCC_except_table2595
- GCC_except_table2597
- GCC_except_table2614
- GCC_except_table2620
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2644
- GCC_except_table2646
- GCC_except_table2647
- GCC_except_table2652
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2655
- GCC_except_table2656
- GCC_except_table2666
- GCC_except_table2724
- GCC_except_table2811
- GCC_except_table2813
- GCC_except_table2816
- GCC_except_table2818
- GCC_except_table2820
- GCC_except_table2821
- GCC_except_table2822
- GCC_except_table2824
- GCC_except_table2829
- GCC_except_table2832
- GCC_except_table2842
- GCC_except_table2848
- GCC_except_table2850
- GCC_except_table2852
- GCC_except_table2855
- GCC_except_table2862
- GCC_except_table2864
- GCC_except_table2871
- GCC_except_table2887
- GCC_except_table2888
- GCC_except_table2889
- GCC_except_table2890
- GCC_except_table2891
- GCC_except_table2936
- GCC_except_table2946
- GCC_except_table2950
- GCC_except_table2953
- GCC_except_table2954
- GCC_except_table3002
- GCC_except_table3011
- GCC_except_table3064
- GCC_except_table3132
- GCC_except_table3134
- GCC_except_table3151
- GCC_except_table3161
- GCC_except_table3178
- GCC_except_table3412
- GCC_except_table3414
- GCC_except_table3416
- GCC_except_table3423
- GCC_except_table3428
- GCC_except_table3438
- GCC_except_table3448
- GCC_except_table3449
- GCC_except_table3450
- GCC_except_table3454
- GCC_except_table3463
- GCC_except_table3464
- GCC_except_table3476
- GCC_except_table3479
- GCC_except_table3480
- GCC_except_table3483
- GCC_except_table3484
- GCC_except_table3493
- GCC_except_table3504
- GCC_except_table3505
- GCC_except_table3506
- GCC_except_table3507
- GCC_except_table3508
- GCC_except_table3514
- GCC_except_table3527
- GCC_except_table3534
- GCC_except_table3539
- GCC_except_table3540
- GCC_except_table3549
- GCC_except_table3559
- GCC_except_table3560
- GCC_except_table3564
- GCC_except_table3565
- GCC_except_table3566
- GCC_except_table3568
- GCC_except_table3572
- GCC_except_table3574
- GCC_except_table3575
- GCC_except_table3579
- GCC_except_table3580
- GCC_except_table3585
- GCC_except_table3588
- GCC_except_table3589
- GCC_except_table3595
- GCC_except_table3658
- GCC_except_table3725
- GCC_except_table3731
- GCC_except_table3800
- GCC_except_table3804
- GCC_except_table3806
- GCC_except_table3809
- GCC_except_table3810
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3843
- GCC_except_table4080
- GCC_except_table4087
- GCC_except_table4089
- GCC_except_table583
- GCC_except_table711
- GCC_except_table722
- GCC_except_table725
- GCC_except_table779
- GCC_except_table815
- GCC_except_table819
- GCC_except_table820
- GCC_except_table836
- GCC_except_table837
- GCC_except_table843
- GCC_except_table850
- GCC_except_table859
- GCC_except_table860
- GCC_except_table874
- GCC_except_table875
- GCC_except_table879
- GCC_except_table886
- GCC_except_table893
- GCC_except_table899
- GCC_except_table900
- GCC_except_table906
- GCC_except_table912
- GCC_except_table915
- GCC_except_table924
- GCC_except_table933
- GCC_except_table937
- GCC_except_table941
- GCC_except_table960
- GCC_except_table961
- GCC_except_table973
- GCC_except_table976
- _OBJC_IVAR_$_PFMetadataCore._isSpatialVideoRecommendedForImmersiveMode
- _PFDeviceLockScreenApproximateTimeRectNormalized.sApproximateTimeRect
- _Vertices.11016
- __AuxiliaryImageCVPixelBufferReleaseBytesCallback.3661
- __OBJC_$_CLASS_METHODS_PFMediaUtilities
- __OBJC_$_PROP_LIST_PFMetadataCore.648
- __OBJC_$_PROP_LIST_PFMetadataImage.6203
- __ZN5boost12interprocessL8ec_tableE.7876
- ___86-[PFLivePhotoEditSession _prepareForPlaybackWithTargetSize:options:completionHandler:]_block_invoke.106
- ___86-[PFLivePhotoEditSession _prepareForPlaybackWithTargetSize:options:completionHandler:]_block_invoke_2.109
- ___Block_byref_object_copy_.10775
- ___Block_byref_object_copy_.11405
- ___Block_byref_object_copy_.12653
- ___Block_byref_object_copy_.4184
- ___Block_byref_object_copy_.4738
- ___Block_byref_object_copy_.5087
- ___Block_byref_object_copy_.5201
- ___Block_byref_object_copy_.5763
- ___Block_byref_object_copy_.6433
- ___Block_byref_object_copy_.7415
- ___Block_byref_object_copy_.8308
- ___Block_byref_object_copy_.8808
- ___Block_byref_object_copy_.9077
- ___Block_byref_object_copy_.9488
- ___Block_byref_object_dispose_.10776
- ___Block_byref_object_dispose_.11406
- ___Block_byref_object_dispose_.12654
- ___Block_byref_object_dispose_.4185
- ___Block_byref_object_dispose_.4739
- ___Block_byref_object_dispose_.5088
- ___Block_byref_object_dispose_.5202
- ___Block_byref_object_dispose_.5764
- ___Block_byref_object_dispose_.6434
- ___Block_byref_object_dispose_.7416
- ___Block_byref_object_dispose_.8309
- ___Block_byref_object_dispose_.8809
- ___Block_byref_object_dispose_.9078
- ___Block_byref_object_dispose_.9489
- ___PFDeviceLockScreenApproximateTimeRectNormalized_block_invoke
- ___block_literal_global.102.2239
- ___block_literal_global.10769
- ___block_literal_global.11062
- ___block_literal_global.11402
- ___block_literal_global.11654
- ___block_literal_global.11798
- ___block_literal_global.12.5773
- ___block_literal_global.12197
- ___block_literal_global.123.8797
- ___block_literal_global.12346
- ___block_literal_global.12471
- ___block_literal_global.127.5585
- ___block_literal_global.132.5580
- ___block_literal_global.1361
- ___block_literal_global.142.10337
- ___block_literal_global.1510
- ___block_literal_global.162.10259
- ___block_literal_global.2081
- ___block_literal_global.2289
- ___block_literal_global.2509
- ___block_literal_global.3336
- ___block_literal_global.3490
- ___block_literal_global.3785
- ___block_literal_global.4044
- ___block_literal_global.4276
- ___block_literal_global.4337
- ___block_literal_global.4346
- ___block_literal_global.4753
- ___block_literal_global.4924
- ___block_literal_global.5144
- ___block_literal_global.5226
- ___block_literal_global.5602
- ___block_literal_global.5697
- ___block_literal_global.57.4334
- ___block_literal_global.5743
- ___block_literal_global.5755
- ___block_literal_global.6485
- ___block_literal_global.6543
- ___block_literal_global.6850
- ___block_literal_global.7121
- ___block_literal_global.7263
- ___block_literal_global.8.12343
- ___block_literal_global.8009
- ___block_literal_global.8857
- ___block_literal_global.905
- ___block_literal_global.9233
- ___block_literal_global.9606
- ___block_literal_global.97.8815
- __exifDateTimeFormatter.dateTimeFormatter.5698
- __exifDateTimeFormatter.onceToken.5696
- __exifSubsecTimeFormatter.onceToken.5682
- __exifSubsecTimeFormatter.subsecTimeFormatter.5683
- __gpsDateFormatter.dateFormatter.5719
- __gpsDateFormatter.onceToken.5718
- __gpsTimeFormatter.onceToken.5723
- __gpsTimeFormatter.timeFormatter.5724
- __unnamed_array_storage.10242
- __unnamed_array_storage.12707
- __unnamed_array_storage.134.4506
- __unnamed_array_storage.1816
- __unnamed_array_storage.191.2504
- __unnamed_array_storage.2085
- __unnamed_array_storage.2508
- __unnamed_array_storage.3357
- __unnamed_array_storage.367
- __unnamed_array_storage.4090
- __unnamed_array_storage.44.1799
- __unnamed_array_storage.4672
- __unnamed_array_storage.6459
- __unnamed_array_storage.8002
- __unnamed_array_storage.9242
- _objc_msgSend$_isSpatialVideoRecommendedForImmersiveModeForAssetVideoTrack:
- _objc_msgSend$initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:debugLayouts:
- _objc_msgSend$initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:layoutType:layoutConfiguration:
- _objc_msgSend$initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:
- _objc_msgSend$setIsSpatialVideoRecommendedForImmersiveMode:
CStrings:
+ "!\x11"
+ "/AppleInternal/Library/BuildRoots/15e1e7ef-63a8-11ee-9fd1-926038f30c31/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
+ "<%@ %p; type: %@; frequency: %@; person IDs: %@, Smart Albums: %@ albumCloudIdentifiers: %@>"
+ "@172@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48Q80Q88Q96Q104Q112d120d128d136d144d152d160B168"
+ "@188@0:8{CGSize=dd}16{CGSize=dd}32{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128@160Q168B176@180"
+ "@192@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGSize=dd}56{CGRect={CGPoint=dd}{CGSize=dd}}72{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136B168B172Q176@184"
+ "@28@0:8i16@20"
+ "B112@0:8{?={?=qiIq}{?=qiIq}}16@64{?=qiIq}72@96^@104"
+ "DeprecatedAVFoundationSyncAPIHelpers"
+ "FailedFRC"
+ "FailedFeatureDisabled"
+ "FailedGenericError"
+ "FailedHardwareUnsupported"
+ "FailedLayoutDecision"
+ "FailedMetadataCheck"
+ "FailedMetadataIntegrity"
+ "FailedResourceAvailability"
+ "FailedStabilization"
+ "FailedStillTransition"
+ "FailedUnsupportedAdjustments"
+ "FailedVideoDecision"
+ "FailedVideoQuality"
+ "PFDeviceLockScreenApproximateTimeRect: Falling back to SBS"
+ "PFDeviceLockScreenApproximateTimeRect: PRUISPosterLayoutUtilities.getTitleBounds returned an error: %{public}@"
+ "PRPosterRoleLockScreen"
+ "PRUISPosterLayoutUtilities"
+ "T@\"NSSet\",&,N,V_albumCloudIdentifiers"
+ "TB,R,N,V_hasTopEdgeContact"
+ "Tq,N,V_spatialVideoRecommendationForImmersiveMode"
+ "User Album"
+ "UserAlbum"
+ "[PFDeviceLockScreenApproximateTimeRectNormalized_SBS] Returning: %@"
+ "[PFDeviceLockScreenApproximateTimeRectNormalized_SBS] Time rect from limited occlusion bounds: %@"
+ "[PFDeviceLockScreenApproximateTimeRectNormalized_SBS] Using limited occlusion bounds for time rect: %@"
+ "^{CGImage=}64@0:8@16{?=qiIq}24^{?=qiIq}48^@56"
+ "_albumCloudIdentifiers"
+ "_hasTopEdgeContact"
+ "_spatialVideoRecommendationForImmersiveMode"
+ "_spatialVideoRecommendationForImmersiveModeForAssetVideoTrack:"
+ "albumCloudIdentifiers"
+ "canApplyHeadroom"
+ "copyCGImageAtTime:actualTime:error:"
+ "copyCGImageFromImageGenerator:atTime:actualTime:error:"
+ "favorites"
+ "hasTopEdgeContact"
+ "initWithImageSize:deviceResolution:parallaxPadding:visibleFrame:inactiveFrame:timeFrame:clockLayerOrder:clockIntersection:hasTopEdgeContact:debugLayouts:"
+ "initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:hasTopEdgeContact:layoutType:layoutConfiguration:"
+ "initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:hasTopEdgeContact:"
+ "insertTimeRange:ofAsset:atTime:intoMutableComposition:error:"
+ "metadataForFormat:forAsset:"
+ "metadataForFormat:forAssetTrack:"
+ "setAlbumCloudIdentifiers:"
+ "setSpatialVideoRecommendationForImmersiveMode:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PosterKit.framework/PosterKit"
+ "spatialVideoRecommendationForImmersiveMode"
+ "titleBoundsForLayout:orientation:role:error:"
+ "trackWithTrackID:"
+ "trackWithTrackID:forAsset:"
+ "tracksWithMediaType:forAsset:"
- "/AppleInternal/Library/BuildRoots/0c82dae5-52ea-11ee-a2fd-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/boost/geometry/index/detail/exception.hpp"
- "<%@ %p; type: %@; frequency: %@; person IDs: %@, Smart Albums: %@>"
- "@168@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48Q80Q88Q96Q104Q112d120d128d136d144d152d160"
- "@188@0:8Q16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGSize=dd}56{CGRect={CGPoint=dd}{CGSize=dd}}72{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136B168Q172@180"
- "LivePhotoWallpaperFailedFRC"
- "LivePhotoWallpaperFailedFeatureDisabled"
- "LivePhotoWallpaperFailedGenericError"
- "LivePhotoWallpaperFailedHardwareUnsupported"
- "LivePhotoWallpaperFailedLayoutDecision"
- "LivePhotoWallpaperFailedMetadataCheck"
- "LivePhotoWallpaperFailedMetadataIntegrity"
- "LivePhotoWallpaperFailedResourceAvailability"
- "LivePhotoWallpaperFailedStabilization"
- "LivePhotoWallpaperFailedStillTransition"
- "LivePhotoWallpaperFailedUnsupportedAdjustments"
- "LivePhotoWallpaperFailedVideoDecision"
- "LivePhotoWallpaperFailedVideoQuality"
- "TB,N,V_isSpatialVideoRecommendedForImmersiveMode"
- "[PFDeviceLockScreenApproximateTimeRectNormalized] Time rect from limited occlusion bounds: %@"
- "[PFDeviceLockScreenApproximateTimeRectNormalized] Using limited occlusion bounds for time rect: %@"
- "_isSpatialVideoRecommendedForImmersiveMode"
- "_isSpatialVideoRecommendedForImmersiveModeForAssetVideoTrack:"
- "initWithPosterClassification:initialRect:imageSize:effectiveAcceptableRect:effectivePreferredRect:validBoundsNormalized:headroomFeasible:layoutType:layoutConfiguration:"
- "initWithVisibleRect:inactiveRect:zoomStrategy:overlapStrategy:parallaxStrategy:inactiveStrategy:headroomStrategy:cropScore:layoutScore:timeBottomOverlap:timeTopOverlap:unsafeAreaOverlap:uninflatedUnsafeAreaOverlap:"
- "isSpatialVideoRecommendedForImmersiveMode"
- "setIsSpatialVideoRecommendedForImmersiveMode:"

```
