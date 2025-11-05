## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/Versions/A/PhotoImaging`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x19e5b4
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xef7c
-  __TEXT.__const: 0x8083
-  __TEXT.__cstring: 0x2d89e
-  __TEXT.__swift5_typeref: 0xb7
-  __TEXT.__constg_swiftt: 0x34
+751.0.104.0.0
+  __TEXT.__text: 0x1a1ae8
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__delay_helper: 0x158
+  __TEXT.__objc_methlist: 0xf894
+  __TEXT.__const: 0x80bb
+  __TEXT.__swift5_typeref: 0xc3
+  __TEXT.__cstring: 0x2d79e
+  __TEXT.__constg_swiftt: 0x50
+  __TEXT.__swift5_reflstr: 0x6d
+  __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x3d
-  __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__oslogstring: 0x4e23
+  __TEXT.__oslogstring: 0x4f63
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x4388
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__gcc_except_tab: 0x4280
   __TEXT.__dlopen_cstrs: 0x1d8
-  __TEXT.__unwind_info: 0x3b28
-  __TEXT.__eh_frame: 0x188
-  __TEXT.__objc_classname: 0x2825
-  __TEXT.__objc_methname: 0x2460e
-  __TEXT.__objc_methtype: 0x3c57
-  __TEXT.__objc_stubs: 0x1bbc0
-  __DATA_CONST.__got: 0x1ba8
-  __DATA_CONST.__const: 0xf40
-  __DATA_CONST.__objc_classlist: 0xaf0
+  __TEXT.__unwind_info: 0x3b88
+  __TEXT.__eh_frame: 0x290
+  __TEXT.__objc_classname: 0x2852
+  __TEXT.__objc_methname: 0x24677
+  __TEXT.__objc_methtype: 0x3b5d
+  __TEXT.__objc_stubs: 0x1ba40
+  __DATA_CONST.__got: 0x1bd8
+  __DATA_CONST.__const: 0xf48
+  __DATA_CONST.__objc_classlist: 0xb08
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8790
+  __DATA_CONST.__objc_selrefs: 0x8828
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x4e8
-  __DATA_CONST.__objc_arraydata: 0x7130
-  __AUTH_CONST.__auth_got: 0xf18
-  __AUTH_CONST.__const: 0x5e18
-  __AUTH_CONST.__cfstring: 0x13b00
-  __AUTH_CONST.__objc_const: 0x1dcd8
-  __AUTH_CONST.__objc_intobj: 0x9d8
+  __DATA_CONST.__objc_superrefs: 0x4f8
+  __DATA_CONST.__objc_arraydata: 0x7238
+  __AUTH_CONST.__auth_got: 0xfb8
+  __AUTH_CONST.__const: 0x5f20
+  __AUTH_CONST.__cfstring: 0x13c40
+  __AUTH_CONST.__objc_const: 0x1d008
+  __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_doubleobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x270
-  __AUTH_CONST.__objc_dictobj: 0x4420
+  __AUTH_CONST.__objc_dictobj: 0x44e8
   __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH.__objc_data: 0x6d80
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x10fc
-  __DATA.__data: 0x1154
-  __DATA.__bss: 0x958
+  __AUTH.__objc_data: 0x6e90
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x10f0
+  __DATA.__data: 0x11dc
+  __DATA.__bss: 0x928
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AutoLoop.framework/Versions/A/AutoLoop
   - /System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture
   - /System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/InertiaCam.framework/Versions/A/InertiaCam
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/Versions/A/ModelCatalog
   - /System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 16981606-DE48-3E19-947D-744675900152
-  Functions: 6151
-  Symbols:   15852
-  CStrings:  13391
+  UUID: 81375A73-5414-369C-920B-18239DB3FC43
+  Functions: 6211
+  Symbols:   15885
+  CStrings:  13406
 
Symbols:
+ +[PIAutoLoopAutoCalculator pipelineFilterForRevertedOriginal]
+ +[PIAutoLoopAutoCalculator pipelineFilterForUnRevertedOriginal]
+ +[PICleanupAvailability _deviceSupportsCleanup]
+ +[PICleanupAvailability _fetchCleanupAvailability]
+ +[PICleanupAvailability ensureAvailability:]
+ +[PICleanupAvailability status]
+ +[PICleanupAvailability updateAvailability]
+ +[PICompositionSerializerFormatVersion adjustmentHasRetouchStyleCleanupOperations:settings:]
+ +[PIInpaintRendering configureFilter:withOptions:]
+ +[PIInpaintRendering inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:operation:]
+ +[PIInpaintRendering sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:operation:]
+ +[PIObjectRemoval _warmUpOperation:context:]
+ +[PIObjectRemoval maskIsMostlyWithinFace:imageSize:imageOrientation:intAreaOverMaskAreaThreshold:intAreaOverFaceAreaThreshold:detectedFaces:]
+ +[PIRepairUtilities transcodePixelBuffer:toBuffer:error:]
+ -[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]
+ -[PIBrushStrokeHistory playbackHistoryToReceiver:options:pauseInterval:completion:]
+ -[PIBrushStrokeHistoryEntry initWithStroke:closed:skipSegmentationIntersections:needsFacePixellation:subjectHitTestRadius:]
+ -[PIBrushStrokeHistoryEntry needsFacePixellation]
+ -[PIBrushStrokeHistoryEntry setNeedsFacePixellation:]
+ -[PIGenerativeModelsStatus availabilityStatus]
+ -[PIGenerativeModelsStatus initWithStatus:]
+ -[PIInpaintAdjustmentController appendCloneStroke:sourceOffset:repairEdges:]
+ -[PIInpaintAdjustmentController(DeltaApplying) applyDelta:]
+ -[PIInpaintAdjustmentController(DeltaApplying) deltaFromComposition:]
+ -[PIInpaintAdjustmentDelta .cxx_destruct]
+ -[PIInpaintAdjustmentDelta initWithOperations:masks:]
+ -[PIInpaintAdjustmentDelta isEmpty]
+ -[PIInpaintAdjustmentDelta masks]
+ -[PIInpaintAdjustmentDelta operations]
+ -[PIInpaintAdjustmentDelta redactedCopy]
+ -[PIInpaintAdjustmentDelta setMasks:]
+ -[PIInpaintAdjustmentDelta setOperations:]
+ -[PIInpaintOperation repairEdges]
+ -[PIInpaintOperation sourceOffset]
+ -[PIParallaxAsset cancelCropRectsRequest:]
+ -[PIParallaxAsset loadCropRectsWithResultHandler:]
+ -[PISensitiveContentAnalysisRequest copyWithZone:]
+ -[PISensitiveContentAnalysisRequest performRegionSpecificChecks]
+ -[PISensitiveContentAnalysisRequest setPerformRegionSpecificChecks:]
+ -[PIThumbnailGenerator resetUnadjustedThumbnails]
+ -[_PICleanupAvailability initWithStatus:]
+ -[_PICleanupAvailability status]
+ -[_PISegmentationNullAsset cancelCropRectsRequest:]
+ -[_PISegmentationNullAsset loadCropRectsWithResultHandler:]
+ GCC_except_table1240
+ GCC_except_table1250
+ GCC_except_table1362
+ GCC_except_table142
+ GCC_except_table1440
+ GCC_except_table1559
+ GCC_except_table1577
+ GCC_except_table1587
+ GCC_except_table1594
+ GCC_except_table1604
+ GCC_except_table1681
+ GCC_except_table1721
+ GCC_except_table1748
+ GCC_except_table1755
+ GCC_except_table1775
+ GCC_except_table1780
+ GCC_except_table1796
+ GCC_except_table1976
+ GCC_except_table2227
+ GCC_except_table2259
+ GCC_except_table2263
+ GCC_except_table2265
+ GCC_except_table2266
+ GCC_except_table2268
+ GCC_except_table2270
+ GCC_except_table2272
+ GCC_except_table2279
+ GCC_except_table2284
+ GCC_except_table2293
+ GCC_except_table2355
+ GCC_except_table2417
+ GCC_except_table2418
+ GCC_except_table2511
+ GCC_except_table2553
+ GCC_except_table2561
+ GCC_except_table2608
+ GCC_except_table2774
+ GCC_except_table2816
+ GCC_except_table2842
+ GCC_except_table2867
+ GCC_except_table299
+ GCC_except_table3039
+ GCC_except_table3285
+ GCC_except_table3309
+ GCC_except_table3313
+ GCC_except_table3432
+ GCC_except_table3441
+ GCC_except_table3449
+ GCC_except_table3451
+ GCC_except_table3479
+ GCC_except_table3501
+ GCC_except_table3682
+ GCC_except_table3689
+ GCC_except_table3693
+ GCC_except_table3704
+ GCC_except_table3711
+ GCC_except_table3822
+ GCC_except_table3937
+ GCC_except_table3952
+ GCC_except_table3953
+ GCC_except_table3959
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3966
+ GCC_except_table3974
+ GCC_except_table4189
+ GCC_except_table4201
+ GCC_except_table4206
+ GCC_except_table4258
+ GCC_except_table4263
+ GCC_except_table4264
+ GCC_except_table4301
+ GCC_except_table4303
+ GCC_except_table4304
+ GCC_except_table4305
+ GCC_except_table4307
+ GCC_except_table4311
+ GCC_except_table4314
+ GCC_except_table4317
+ GCC_except_table4318
+ GCC_except_table4319
+ GCC_except_table4321
+ GCC_except_table4392
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table4695
+ GCC_except_table4998
+ GCC_except_table5008
+ GCC_except_table5019
+ GCC_except_table5078
+ GCC_except_table5198
+ GCC_except_table5276
+ GCC_except_table5332
+ GCC_except_table5334
+ GCC_except_table5432
+ GCC_except_table5433
+ GCC_except_table5446
+ GCC_except_table5447
+ GCC_except_table5448
+ GCC_except_table5449
+ GCC_except_table5450
+ GCC_except_table5451
+ GCC_except_table5452
+ GCC_except_table5453
+ GCC_except_table5454
+ GCC_except_table5455
+ GCC_except_table5457
+ GCC_except_table5523
+ GCC_except_table5524
+ GCC_except_table5525
+ GCC_except_table5559
+ GCC_except_table5560
+ GCC_except_table5561
+ GCC_except_table5564
+ GCC_except_table5567
+ GCC_except_table5603
+ GCC_except_table5713
+ GCC_except_table5730
+ GCC_except_table5731
+ GCC_except_table5732
+ GCC_except_table5733
+ GCC_except_table5734
+ GCC_except_table5735
+ GCC_except_table5737
+ GCC_except_table5871
+ GCC_except_table5907
+ GCC_except_table5918
+ GCC_except_table5920
+ GCC_except_table5923
+ GCC_except_table5930
+ GCC_except_table5941
+ GCC_except_table5963
+ GCC_except_table5967
+ GCC_except_table5968
+ GCC_except_table5986
+ GCC_except_table5987
+ GCC_except_table5990
+ GCC_except_table5992
+ GCC_except_table5996
+ GCC_except_table5998
+ GCC_except_table5999
+ GCC_except_table6011
+ GCC_except_table690
+ ImageHarmonizationKitLibraryCore.frameworkLibrary.19413
+ MediaAnalysisLibrary.18731
+ MediaAnalysisLibraryCore.frameworkLibrary.18742
+ MediaAnalysisLibraryCore.frameworkLibrary.25510
+ NUAssertLogger.10039
+ NUAssertLogger.1011
+ NUAssertLogger.10415
+ NUAssertLogger.10460
+ NUAssertLogger.1073
+ NUAssertLogger.10877
+ NUAssertLogger.11134
+ NUAssertLogger.11438
+ NUAssertLogger.11539
+ NUAssertLogger.11676
+ NUAssertLogger.11956
+ NUAssertLogger.1214
+ NUAssertLogger.12658
+ NUAssertLogger.12880
+ NUAssertLogger.13034
+ NUAssertLogger.1340
+ NUAssertLogger.13756
+ NUAssertLogger.14129
+ NUAssertLogger.14462
+ NUAssertLogger.14687
+ NUAssertLogger.148
+ NUAssertLogger.15021
+ NUAssertLogger.15283
+ NUAssertLogger.1530
+ NUAssertLogger.15861
+ NUAssertLogger.1616
+ NUAssertLogger.16656
+ NUAssertLogger.16896
+ NUAssertLogger.17500
+ NUAssertLogger.18227
+ NUAssertLogger.18370
+ NUAssertLogger.18492
+ NUAssertLogger.18757
+ NUAssertLogger.19401
+ NUAssertLogger.1955
+ NUAssertLogger.19577
+ NUAssertLogger.20056
+ NUAssertLogger.20178
+ NUAssertLogger.20369
+ NUAssertLogger.20854
+ NUAssertLogger.2131
+ NUAssertLogger.22111
+ NUAssertLogger.2231
+ NUAssertLogger.22530
+ NUAssertLogger.22720
+ NUAssertLogger.23193
+ NUAssertLogger.23353
+ NUAssertLogger.2390
+ NUAssertLogger.23951
+ NUAssertLogger.24324
+ NUAssertLogger.24693
+ NUAssertLogger.24850
+ NUAssertLogger.252
+ NUAssertLogger.25385
+ NUAssertLogger.25651
+ NUAssertLogger.25890
+ NUAssertLogger.26450
+ NUAssertLogger.2667
+ NUAssertLogger.26838
+ NUAssertLogger.27027
+ NUAssertLogger.27162
+ NUAssertLogger.27394
+ NUAssertLogger.27474
+ NUAssertLogger.27675
+ NUAssertLogger.2794
+ NUAssertLogger.3108
+ NUAssertLogger.325
+ NUAssertLogger.3273
+ NUAssertLogger.3425
+ NUAssertLogger.3633
+ NUAssertLogger.3840
+ NUAssertLogger.406
+ NUAssertLogger.4091
+ NUAssertLogger.4419
+ NUAssertLogger.4679
+ NUAssertLogger.4976
+ NUAssertLogger.5072
+ NUAssertLogger.5267
+ NUAssertLogger.537
+ NUAssertLogger.5477
+ NUAssertLogger.5764
+ NUAssertLogger.6037
+ NUAssertLogger.6169
+ NUAssertLogger.6273
+ NUAssertLogger.6464
+ NUAssertLogger.6633
+ NUAssertLogger.7270
+ NUAssertLogger.7492
+ NUAssertLogger.767
+ NUAssertLogger.7874
+ NUAssertLogger.8423
+ NUAssertLogger.8533
+ NUAssertLogger.8877
+ NUAssertLogger.902
+ NUAssertLogger.9046
+ NUAssertLogger.9400
+ NUAssertLogger.9540
+ NUAssertLogger.9620
+ NULogger.10090
+ NULogger.12643
+ NULogger.14564
+ NULogger.22728
+ NULogger.23996
+ NULogger.26007
+ NULogger.4154
+ NURenderLogger.21316
+ OBJC_IVAR_$_PIBrushStrokeHistoryEntry._needsFacePixellation
+ OBJC_IVAR_$_PIGenerativeModelsStatus._availabilityStatus
+ OBJC_IVAR_$_PIInpaintAdjustmentDelta._masks
+ OBJC_IVAR_$_PIInpaintAdjustmentDelta._operations
+ OBJC_IVAR_$_PIInpaintOperation._repairEdges
+ OBJC_IVAR_$_PIInpaintOperation._sourceOffset
+ OBJC_IVAR_$_PISensitiveContentAnalysisRequest._performRegionSpecificChecks
+ OBJC_IVAR_$__PICleanupAvailability._status
+ _CVPixelBufferCreateWithBytes
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NUVideoMetadataExtractor
+ _OBJC_CLASS_$_PICleanupAvailability
+ _OBJC_CLASS_$_PIGenerativeModels
+ _OBJC_CLASS_$_PIGenerativeModelsStatus
+ _OBJC_CLASS_$_PIInpaintAdjustmentDelta
+ _OBJC_CLASS_$_SCMLImageSanitizerRequest
+ _OBJC_CLASS_$__PICleanupAvailability
+ _OBJC_METACLASS_$_PICleanupAvailability
+ _OBJC_METACLASS_$_PIGenerativeModels
+ _OBJC_METACLASS_$_PIGenerativeModelsStatus
+ _OBJC_METACLASS_$_PIInpaintAdjustmentDelta
+ _OBJC_METACLASS_$__PICleanupAvailability
+ _OperationUsesLegacyFilter
+ _SCMLErrorDomain
+ _ZL14NUAssertLoggerv.17349
+ _ZL14NUAssertLoggerv.18948
+ _ZL14NUAssertLoggerv.24899
+ _ZL14NUAssertLoggerv.25765
+ _ZL14NUAssertLoggerv.26668
+ __45+[PIPhotoEditHelper filterNameForEffectName:]_block_invoke.409
+ __48-[PISegmentationLoader _loadRegions:completion:]_block_invoke.199
+ __48-[PISegmentationLoader _loadRegions:completion:]_block_invoke.201
+ __48-[PISegmentationLoader _loadRegions:completion:]_block_invoke.204
+ __48-[_PISensitiveContentAnalysisResult description]_block_invoke.28
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke.1157
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke.882
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_10.1080
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_11.1098
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_12.1152
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_2.1163
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_2.909
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_3.1190
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_3.921
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_4.951
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_5.966
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_6.990
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_7.1005
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_8.1023
+ __49+[PICompositionSerializerConstants conversionMap]_block_invoke_9.1071
+ __50-[PISegmentationLoader _performLayout:completion:]_block_invoke.208
+ __50-[PISegmentationLoader _performLayout:completion:]_block_invoke.209
+ __79-[PISensitiveContentAnalysisRequest resolveWithInputBufferResponse:completion:]_block_invoke.136
+ __85+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:renderer:error:]_block_invoke.151
+ __85+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:renderer:error:]_block_invoke.157
+ __90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke.119
+ __90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke.122
+ __90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke_2.123
+ __Block_byref_object_copy_.10121
+ __Block_byref_object_copy_.10531
+ __Block_byref_object_copy_.10934
+ __Block_byref_object_copy_.11798
+ __Block_byref_object_copy_.12020
+ __Block_byref_object_copy_.12637
+ __Block_byref_object_copy_.13968
+ __Block_byref_object_copy_.14142
+ __Block_byref_object_copy_.14734
+ __Block_byref_object_copy_.15936
+ __Block_byref_object_copy_.16747
+ __Block_byref_object_copy_.18317
+ __Block_byref_object_copy_.18975
+ __Block_byref_object_copy_.22743
+ __Block_byref_object_copy_.24352
+ __Block_byref_object_copy_.24919
+ __Block_byref_object_copy_.4697
+ __Block_byref_object_copy_.5762
+ __Block_byref_object_copy_.6657
+ __Block_byref_object_copy_.7299
+ __Block_byref_object_copy_.8458
+ __Block_byref_object_dispose_.10122
+ __Block_byref_object_dispose_.10532
+ __Block_byref_object_dispose_.10935
+ __Block_byref_object_dispose_.11799
+ __Block_byref_object_dispose_.12021
+ __Block_byref_object_dispose_.12638
+ __Block_byref_object_dispose_.13969
+ __Block_byref_object_dispose_.14143
+ __Block_byref_object_dispose_.14735
+ __Block_byref_object_dispose_.15937
+ __Block_byref_object_dispose_.16748
+ __Block_byref_object_dispose_.18318
+ __Block_byref_object_dispose_.18976
+ __Block_byref_object_dispose_.22744
+ __Block_byref_object_dispose_.24353
+ __Block_byref_object_dispose_.24920
+ __Block_byref_object_dispose_.4698
+ __Block_byref_object_dispose_.5763
+ __Block_byref_object_dispose_.6658
+ __Block_byref_object_dispose_.7300
+ __Block_byref_object_dispose_.8459
+ __CLASS_METHODS_PIGenerativeModels
+ __DATA_PIGenerativeModels
+ __INSTANCE_METHODS_PIGenerativeModels
+ __ImageHarmonizationKitLibraryCore_block_invoke.19414
+ __METACLASS_DATA_PIGenerativeModels
+ __MediaAnalysisLibraryCore_block_invoke.18743
+ __MediaAnalysisLibraryCore_block_invoke.25511
+ __NUAssertLogger_block_invoke.10071
+ __NUAssertLogger_block_invoke.1025
+ __NUAssertLogger_block_invoke.10434
+ __NUAssertLogger_block_invoke.10523
+ __NUAssertLogger_block_invoke.10899
+ __NUAssertLogger_block_invoke.1106
+ __NUAssertLogger_block_invoke.11191
+ __NUAssertLogger_block_invoke.11454
+ __NUAssertLogger_block_invoke.11614
+ __NUAssertLogger_block_invoke.11707
+ __NUAssertLogger_block_invoke.11838
+ __NUAssertLogger_block_invoke.11983
+ __NUAssertLogger_block_invoke.1220
+ __NUAssertLogger_block_invoke.12666
+ __NUAssertLogger_block_invoke.12899
+ __NUAssertLogger_block_invoke.13050
+ __NUAssertLogger_block_invoke.13772
+ __NUAssertLogger_block_invoke.14105
+ __NUAssertLogger_block_invoke.14511
+ __NUAssertLogger_block_invoke.14725
+ __NUAssertLogger_block_invoke.15040
+ __NUAssertLogger_block_invoke.1535
+ __NUAssertLogger_block_invoke.15426
+ __NUAssertLogger_block_invoke.155
+ __NUAssertLogger_block_invoke.15884
+ __NUAssertLogger_block_invoke.1613
+ __NUAssertLogger_block_invoke.16694
+ __NUAssertLogger_block_invoke.16920
+ __NUAssertLogger_block_invoke.17521
+ __NUAssertLogger_block_invoke.18252
+ __NUAssertLogger_block_invoke.18422
+ __NUAssertLogger_block_invoke.18520
+ __NUAssertLogger_block_invoke.18771
+ __NUAssertLogger_block_invoke.19437
+ __NUAssertLogger_block_invoke.19597
+ __NUAssertLogger_block_invoke.1964
+ __NUAssertLogger_block_invoke.20095
+ __NUAssertLogger_block_invoke.20177
+ __NUAssertLogger_block_invoke.20381
+ __NUAssertLogger_block_invoke.20878
+ __NUAssertLogger_block_invoke.2096
+ __NUAssertLogger_block_invoke.2165
+ __NUAssertLogger_block_invoke.22133
+ __NUAssertLogger_block_invoke.2245
+ __NUAssertLogger_block_invoke.22546
+ __NUAssertLogger_block_invoke.22734
+ __NUAssertLogger_block_invoke.23210
+ __NUAssertLogger_block_invoke.2335
+ __NUAssertLogger_block_invoke.23364
+ __NUAssertLogger_block_invoke.24047
+ __NUAssertLogger_block_invoke.24375
+ __NUAssertLogger_block_invoke.2444
+ __NUAssertLogger_block_invoke.24714
+ __NUAssertLogger_block_invoke.24873
+ __NUAssertLogger_block_invoke.25342
+ __NUAssertLogger_block_invoke.25677
+ __NUAssertLogger_block_invoke.26045
+ __NUAssertLogger_block_invoke.26466
+ __NUAssertLogger_block_invoke.2682
+ __NUAssertLogger_block_invoke.26855
+ __NUAssertLogger_block_invoke.27043
+ __NUAssertLogger_block_invoke.27182
+ __NUAssertLogger_block_invoke.274
+ __NUAssertLogger_block_invoke.27415
+ __NUAssertLogger_block_invoke.27507
+ __NUAssertLogger_block_invoke.27674
+ __NUAssertLogger_block_invoke.2815
+ __NUAssertLogger_block_invoke.3095
+ __NUAssertLogger_block_invoke.3213
+ __NUAssertLogger_block_invoke.3295
+ __NUAssertLogger_block_invoke.330
+ __NUAssertLogger_block_invoke.3459
+ __NUAssertLogger_block_invoke.3616
+ __NUAssertLogger_block_invoke.3795
+ __NUAssertLogger_block_invoke.4133
+ __NUAssertLogger_block_invoke.415
+ __NUAssertLogger_block_invoke.4438
+ __NUAssertLogger_block_invoke.4696
+ __NUAssertLogger_block_invoke.5004
+ __NUAssertLogger_block_invoke.5132
+ __NUAssertLogger_block_invoke.5399
+ __NUAssertLogger_block_invoke.5518
+ __NUAssertLogger_block_invoke.557
+ __NUAssertLogger_block_invoke.5778
+ __NUAssertLogger_block_invoke.6071
+ __NUAssertLogger_block_invoke.6192
+ __NUAssertLogger_block_invoke.6301
+ __NUAssertLogger_block_invoke.6517
+ __NUAssertLogger_block_invoke.6645
+ __NUAssertLogger_block_invoke.7235
+ __NUAssertLogger_block_invoke.7507
+ __NUAssertLogger_block_invoke.7914
+ __NUAssertLogger_block_invoke.792
+ __NUAssertLogger_block_invoke.8447
+ __NUAssertLogger_block_invoke.8566
+ __NUAssertLogger_block_invoke.8893
+ __NUAssertLogger_block_invoke.9102
+ __NUAssertLogger_block_invoke.9224
+ __NUAssertLogger_block_invoke.923
+ __NUAssertLogger_block_invoke.9569
+ __NUAssertLogger_block_invoke.9689
+ __NULogger_block_invoke.10036
+ __NULogger_block_invoke.10786
+ __NULogger_block_invoke.10893
+ __NULogger_block_invoke.1092
+ __NULogger_block_invoke.11701
+ __NULogger_block_invoke.11975
+ __NULogger_block_invoke.12518
+ __NULogger_block_invoke.1274
+ __NULogger_block_invoke.1389
+ __NULogger_block_invoke.14212
+ __NULogger_block_invoke.14571
+ __NULogger_block_invoke.15054
+ __NULogger_block_invoke.1515
+ __NULogger_block_invoke.15756
+ __NULogger_block_invoke.15845
+ __NULogger_block_invoke.16590
+ __NULogger_block_invoke.18298
+ __NULogger_block_invoke.19290
+ __NULogger_block_invoke.19543
+ __NULogger_block_invoke.20085
+ __NULogger_block_invoke.20872
+ __NULogger_block_invoke.21994
+ __NULogger_block_invoke.22719
+ __NULogger_block_invoke.24001
+ __NULogger_block_invoke.24435
+ __NULogger_block_invoke.2486
+ __NULogger_block_invoke.25455
+ __NULogger_block_invoke.26013
+ __NULogger_block_invoke.268
+ __NULogger_block_invoke.27702
+ __NULogger_block_invoke.3500
+ __NULogger_block_invoke.3630
+ __NULogger_block_invoke.3909
+ __NULogger_block_invoke.4157
+ __NULogger_block_invoke.461
+ __NULogger_block_invoke.4776
+ __NULogger_block_invoke.5112
+ __NULogger_block_invoke.5300
+ __NULogger_block_invoke.5802
+ __NULogger_block_invoke.6691
+ __NULogger_block_invoke.715
+ __NULogger_block_invoke.7269
+ __NULogger_block_invoke.7655
+ __NULogger_block_invoke.8416
+ __NULogger_block_invoke.8631
+ __NULogger_block_invoke.9399
+ __NURenderLogger_block_invoke.18408
+ __NURenderLogger_block_invoke.21345
+ __OBJC_$_CLASS_METHODS_PICleanupAvailability
+ __OBJC_$_CLASS_PROP_LIST_PICleanupAvailability
+ __OBJC_$_INSTANCE_METHODS_PIGenerativeModelsStatus
+ __OBJC_$_INSTANCE_METHODS_PIInpaintAdjustmentController(DeltaApplying)
+ __OBJC_$_INSTANCE_METHODS_PIInpaintAdjustmentDelta
+ __OBJC_$_INSTANCE_METHODS__PICleanupAvailability
+ __OBJC_$_INSTANCE_VARIABLES_PIGenerativeModelsStatus
+ __OBJC_$_INSTANCE_VARIABLES_PIInpaintAdjustmentDelta
+ __OBJC_$_INSTANCE_VARIABLES__PICleanupAvailability
+ __OBJC_$_PROP_LIST_PIGenerativeModelsStatus
+ __OBJC_$_PROP_LIST_PIInpaintAdjustmentDelta
+ __OBJC_$_PROP_LIST__PICleanupAvailability
+ __OBJC_CLASS_RO_$_PICleanupAvailability
+ __OBJC_CLASS_RO_$_PIGenerativeModelsStatus
+ __OBJC_CLASS_RO_$_PIInpaintAdjustmentDelta
+ __OBJC_CLASS_RO_$__PICleanupAvailability
+ __OBJC_METACLASS_RO_$_PICleanupAvailability
+ __OBJC_METACLASS_RO_$_PIGenerativeModelsStatus
+ __OBJC_METACLASS_RO_$_PIInpaintAdjustmentDelta
+ __OBJC_METACLASS_RO_$__PICleanupAvailability
+ __ZN12_GLOBAL__N_119_NTKUltraCubeFillerD1Ev
+ __ZNKSt3__16vectorI5SKnotNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIDv2_sNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIDv4_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDv2_sEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102EmRKd
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___35-[PIAutoLoopAutoCalculator submit:]_block_invoke_4
+ ___44+[PICleanupAvailability ensureAvailability:]_block_invoke
+ ___44+[PICleanupAvailability ensureAvailability:]_block_invoke_2
+ ___53+[PICompositionSerializerFormatVersion _versionRules]_block_invoke_13
+ ___61+[PIAutoLoopAutoCalculator pipelineFilterForRevertedOriginal]_block_invoke
+ ___63+[PIAutoLoopAutoCalculator pipelineFilterForUnRevertedOriginal]_block_invoke
+ ___90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke
+ ___90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke_2
+ ___90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke_3
+ ___90-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:pauseInterval:completion:]_block_invoke_4
+ ___ZL14NUAssertLoggerv_block_invoke.17380
+ ___ZL14NUAssertLoggerv_block_invoke.18974
+ ___ZL14NUAssertLoggerv_block_invoke.24950
+ ___ZL14NUAssertLoggerv_block_invoke.25781
+ ___ZL14NUAssertLoggerv_block_invoke.26710
+ ___ZL8NULoggerv_block_invoke.25808
+ ___block_descriptor_112_e8_32s40bs48r56r64r72r80r88r96r104r_e5_v8?0l
+ ___block_descriptor_48_e8_32bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r48r_e85_v80?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40"NSError"72l
+ ___block_descriptor_64_e8_32s40s48bs_e43_v24?0"SCMLImageSanitization"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48r56r64r72r80r88r96r104r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r96r104r
+ ___lightMapImageFromData_block_invoke.18568
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_memcpy24_8
+ ___swift_noop_void_return
+ __block_literal_global.100.16561
+ __block_literal_global.1007
+ __block_literal_global.1007.13461
+ __block_literal_global.101.12896
+ __block_literal_global.10172
+ __block_literal_global.10238
+ __block_literal_global.1025
+ __block_literal_global.10431
+ __block_literal_global.10520
+ __block_literal_global.106
+ __block_literal_global.106.16170
+ __block_literal_global.1073
+ __block_literal_global.10781
+ __block_literal_global.1082
+ __block_literal_global.109
+ __block_literal_global.10930
+ __block_literal_global.10999
+ __block_literal_global.1100
+ __block_literal_global.1103
+ __block_literal_global.11188
+ __block_literal_global.112.27659
+ __block_literal_global.114.27696
+ __block_literal_global.11451
+ __block_literal_global.1154
+ __block_literal_global.1159
+ __block_literal_global.116.26376
+ __block_literal_global.11611
+ __block_literal_global.1165
+ __block_literal_global.11691
+ __block_literal_global.11781
+ __block_literal_global.118.21308
+ __block_literal_global.1192
+ __block_literal_global.1197
+ __block_literal_global.1199
+ __block_literal_global.1204
+ __block_literal_global.1206
+ __block_literal_global.1208
+ __block_literal_global.1212
+ __block_literal_global.122.2082
+ __block_literal_global.122.26371
+ __block_literal_global.12210
+ __block_literal_global.1226
+ __block_literal_global.1228
+ __block_literal_global.1230
+ __block_literal_global.1232
+ __block_literal_global.1234
+ __block_literal_global.12457
+ __block_literal_global.1253
+ __block_literal_global.1255
+ __block_literal_global.1260
+ __block_literal_global.1262
+ __block_literal_global.12648
+ __block_literal_global.1274
+ __block_literal_global.1276
+ __block_literal_global.1278
+ __block_literal_global.128.24711
+ __block_literal_global.1280
+ __block_literal_global.12980
+ __block_literal_global.13047
+ __block_literal_global.134
+ __block_literal_global.13452
+ __block_literal_global.13555
+ __block_literal_global.13769
+ __block_literal_global.139.8444
+ __block_literal_global.14091
+ __block_literal_global.143.26357
+ __block_literal_global.145
+ __block_literal_global.14508
+ __block_literal_global.14728
+ __block_literal_global.15037
+ __block_literal_global.152
+ __block_literal_global.15423
+ __block_literal_global.1546
+ __block_literal_global.15746
+ __block_literal_global.16.10933
+ __block_literal_global.16079
+ __block_literal_global.161.26352
+ __block_literal_global.16405
+ __block_literal_global.16598
+ __block_literal_global.16691
+ __block_literal_global.16917
+ __block_literal_global.17013
+ __block_literal_global.171
+ __block_literal_global.1714
+ __block_literal_global.17190
+ __block_literal_global.17223
+ __block_literal_global.17402
+ __block_literal_global.17514
+ __block_literal_global.17532
+ __block_literal_global.180
+ __block_literal_global.18123
+ __block_literal_global.182.16183
+ __block_literal_global.182.22527
+ __block_literal_global.18299
+ __block_literal_global.18440
+ __block_literal_global.18517
+ __block_literal_global.18599
+ __block_literal_global.18776
+ __block_literal_global.188.24947
+ __block_literal_global.18971
+ __block_literal_global.190.26289
+ __block_literal_global.19160
+ __block_literal_global.19286
+ __block_literal_global.193
+ __block_literal_global.19434
+ __block_literal_global.195.21184
+ __block_literal_global.19539
+ __block_literal_global.1969
+ __block_literal_global.197
+ __block_literal_global.199.18249
+ __block_literal_global.20092
+ __block_literal_global.201
+ __block_literal_global.20162
+ __block_literal_global.202
+ __block_literal_global.20382
+ __block_literal_global.2048
+ __block_literal_global.20578
+ __block_literal_global.20648
+ __block_literal_global.21358
+ __block_literal_global.21483
+ __block_literal_global.2162
+ __block_literal_global.2226
+ __block_literal_global.22307
+ __block_literal_global.226
+ __block_literal_global.22845
+ __block_literal_global.2320
+ __block_literal_global.23207
+ __block_literal_global.23361
+ __block_literal_global.240.26463
+ __block_literal_global.24044
+ __block_literal_global.243.23998
+ __block_literal_global.24428
+ __block_literal_global.24596
+ __block_literal_global.24758
+ __block_literal_global.24862
+ __block_literal_global.2488
+ __block_literal_global.24895
+ __block_literal_global.25
+ __block_literal_global.25224
+ __block_literal_global.25327
+ __block_literal_global.25674
+ __block_literal_global.25778
+ __block_literal_global.26042
+ __block_literal_global.26485
+ __block_literal_global.266
+ __block_literal_global.26707
+ __block_literal_global.26852
+ __block_literal_global.2693
+ __block_literal_global.271.3903
+ __block_literal_global.27179
+ __block_literal_global.27422
+ __block_literal_global.27585
+ __block_literal_global.27631
+ __block_literal_global.2812
+ __block_literal_global.292.14722
+ __block_literal_global.294.14739
+ __block_literal_global.298.15881
+ __block_literal_global.305
+ __block_literal_global.307.11980
+ __block_literal_global.3081
+ __block_literal_global.311.25430
+ __block_literal_global.3198
+ __block_literal_global.3292
+ __block_literal_global.33.7816
+ __block_literal_global.333
+ __block_literal_global.34
+ __block_literal_global.3489
+ __block_literal_global.3601
+ __block_literal_global.3796
+ __block_literal_global.38.7811
+ __block_literal_global.40
+ __block_literal_global.41.18779
+ __block_literal_global.416
+ __block_literal_global.420
+ __block_literal_global.428
+ __block_literal_global.43.7806
+ __block_literal_global.4307
+ __block_literal_global.439
+ __block_literal_global.441.12544
+ __block_literal_global.4430
+ __block_literal_global.4687
+ __block_literal_global.48.7800
+ __block_literal_global.4930
+ __block_literal_global.5129
+ __block_literal_global.54.27412
+ __block_literal_global.5444
+ __block_literal_global.554
+ __block_literal_global.56.21304
+ __block_literal_global.56.24530
+ __block_literal_global.56.26422
+ __block_literal_global.5669
+ __block_literal_global.58.18388
+ __block_literal_global.58.21302
+ __block_literal_global.5815
+ __block_literal_global.6
+ __block_literal_global.6087
+ __block_literal_global.6101
+ __block_literal_global.6189
+ __block_literal_global.6298
+ __block_literal_global.63.20068
+ __block_literal_global.642
+ __block_literal_global.644
+ __block_literal_global.6514
+ __block_literal_global.658
+ __block_literal_global.6748
+ __block_literal_global.6874
+ __block_literal_global.709
+ __block_literal_global.71.26411
+ __block_literal_global.7332
+ __block_literal_global.7435
+ __block_literal_global.761
+ __block_literal_global.763
+ __block_literal_global.7651
+ __block_literal_global.7821
+ __block_literal_global.7911
+ __block_literal_global.8044
+ __block_literal_global.81.20567
+ __block_literal_global.817.13460
+ __block_literal_global.8409
+ __block_literal_global.8624
+ __block_literal_global.884
+ __block_literal_global.8890
+ __block_literal_global.89.16168
+ __block_literal_global.9.12452
+ __block_literal_global.9.25218
+ __block_literal_global.9099
+ __block_literal_global.91.19181
+ __block_literal_global.91.20558
+ __block_literal_global.911
+ __block_literal_global.920
+ __block_literal_global.9209
+ __block_literal_global.923
+ __block_literal_global.93.10888
+ __block_literal_global.93.27504
+ __block_literal_global.95.24870
+ __block_literal_global.953
+ __block_literal_global.9566
+ __block_literal_global.968
+ __block_literal_global.9686
+ __block_literal_global.992
+ __getMediaAnalysisResultAttributesKeySymbolLoc_block_invoke.18783
+ __getMediaAnalysisResultsKeySymbolLoc_block_invoke.18773
+ __getVCPMediaAnalysisServiceClass_block_invoke.18730
+ __getVCPMediaAnalysisServiceClass_block_invoke.25500
+ _gotLoadHelper_x8$_OBJC_CLASS_$_SCMLImageSanitizerRequest
+ _gotLoadHelper_x8$_SCMLErrorDomain
+ _objc_msgSend$_deviceSupportsCleanup
+ _objc_msgSend$_fetchCleanupAvailability
+ _objc_msgSend$_playbackHistoryIndex:toReceiver:options:pauseInterval:completion:
+ _objc_msgSend$_warmUpOperation:context:
+ _objc_msgSend$addImageSpaceInpaintingStroke:exclusionMask:closeAndFillStroke:needsFacePixellation:recordStroke:completion:
+ _objc_msgSend$adjustmentHasRetouchStyleCleanupOperations:settings:
+ _objc_msgSend$configureFilter:withOptions:
+ _objc_msgSend$domain
+ _objc_msgSend$ensureAvailability:
+ _objc_msgSend$initWithOperations:masks:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:operation:
+ _objc_msgSend$loadCropRectsWithResultHandler:
+ _objc_msgSend$masks
+ _objc_msgSend$needsFacePixellation
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$operations
+ _objc_msgSend$overrideCleanupHardwareCheck
+ _objc_msgSend$pipelineFilterForRevertedOriginal
+ _objc_msgSend$pipelineFilterForUnRevertedOriginal
+ _objc_msgSend$playbackHistoryToReceiver:options:pauseInterval:completion:
+ _objc_msgSend$sanitizeRequestAsynchronously:completionHandler:
+ _objc_msgSend$setModelManagerServicesUseCaseID:
+ _objc_msgSend$setNeedsFacePixellation:
+ _objc_msgSend$setPerformRegionSpecificChecks:
+ _objc_msgSend$sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:operation:
+ _objc_msgSend$transcodePixelBuffer:toBuffer:error:
+ _swift_bridgeObjectRelease_n
+ _symbolic Sd
+ _symbolic Si
+ _symbolic _____ So14PIModelCatalogC12PhotoImagingE16DownloadProgressV
+ _symbolic _____Sg 10Foundation6LocaleV12LanguageCodeV
+ audit_stringImageHarmonizationKit.19428
+ audit_stringMediaAnalysis.18749
+ audit_stringMediaAnalysis.25522
+ colorBalanceKernels.colorBalanceKernels.24787
+ colorBalanceKernels.onceToken.24786
+ ensureAvailability:.availability
+ ensureAvailability:.availabilityQueue
+ ensureAvailability:.once
+ getMediaAnalysisResultAttributesKeySymbolLoc.ptr.18782
+ getMediaAnalysisResultsKey.18755
+ getMediaAnalysisResultsKeySymbolLoc.ptr.18772
+ getVCPMediaAnalysisServiceClass.18728
+ getVCPMediaAnalysisServiceClass.softClass.18729
+ getVCPMediaAnalysisServiceClass.softClass.25499
+ initialize.onceToken.12216
+ initialize.onceToken.21382
+ initialize.onceToken.23064
+ initialize.onceToken.24496
+ kernel.kernel.2227
+ kernel.onceToken.2225
+ roiCallback_block_invoke.24865
+ s_log.12036
+ s_log.22716
+ s_log.24342
+ s_signpost.12037
+ s_signpost.22717
+ s_signpost.24343
- +[PIAutoLoopAutoCalculator pipelineFilterForCorruptedVideoMitigation]
- +[PIInpaintRendering inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:]
- +[PIInpaintRendering sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:]
- +[PIObjectRemoval _regionSupportsObjectRemoval]
- +[PIObjectRemoval deviceSupportsObjectRemoval]
- +[PIObjectRemoval macOSDeviceIsAppleSilicon]
- +[PIObjectRemoval maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:]
- +[PIPerspectiveAutoCalculator requestVisionCleanUp]
- +[PISensitiveContentAnalysisRequest currentSensitivityExceedsThresholdsV1:initialSensitivity:]
- +[PIVideoReframeMetadataExtractor canProvideMetadataForAVAsset:]
- -[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]
- -[PIBrushStrokeHistoryEntry initWithStroke:closed:skipSegmentationIntersections:needsPixellation:subjectHitTestRadius:]
- -[PIBrushStrokeHistoryEntry needsPixellation]
- -[PIBrushStrokeHistoryEntry setNeedsPixellation:]
- -[PIGlobalSettings sensitivityCheckVersion2Thresholds]
- -[PIGlobalSettings setSensitivityCheckVersion2Thresholds:]
- -[PIInpaintAdjustmentController takeNewOperationsFromComposition:redactNewOperations:]
- -[PIVideoReframeMetadataExtractor .cxx_destruct]
- -[PIVideoReframeMetadataExtractor centerMotionVectorFromMetadata:]
- -[PIVideoReframeMetadataExtractor extractMetadata]
- -[PIVideoReframeMetadataExtractor initWithAVAsset:]
- -[PIVideoReframeMetadataExtractor init]
- -[PIVideoReframeMetadataExtractor motionBlurVectorFromMetadata:]
- -[PIVideoReframeMetadataExtractor timedMetadataArray]
- -[PIVideoReframeMetadataExtractor trajectoryeHomographyFromMetadata:containsV3Metadata:]
- -[PIVideoReframeTimedMetadata estimatedCenterMotion]
- -[PIVideoReframeTimedMetadata estimatedMotionBlur]
- -[PIVideoReframeTimedMetadata setEstimatedCenterMotion:]
- -[PIVideoReframeTimedMetadata setEstimatedMotionBlur:]
- -[PIVideoReframeTimedMetadata setTime:]
- -[PIVideoReframeTimedMetadata setTrajectoryHomography:]
- -[PIVideoReframeTimedMetadata time]
- -[PIVideoReframeTimedMetadata trajectoryHomography]
- GCC_except_table1234
- GCC_except_table1244
- GCC_except_table1356
- GCC_except_table138
- GCC_except_table1434
- GCC_except_table1553
- GCC_except_table1565
- GCC_except_table1581
- GCC_except_table1588
- GCC_except_table1598
- GCC_except_table1672
- GCC_except_table1712
- GCC_except_table1739
- GCC_except_table1746
- GCC_except_table1766
- GCC_except_table1771
- GCC_except_table1788
- GCC_except_table1968
- GCC_except_table2211
- GCC_except_table2251
- GCC_except_table2255
- GCC_except_table2257
- GCC_except_table2258
- GCC_except_table2260
- GCC_except_table2262
- GCC_except_table2264
- GCC_except_table2271
- GCC_except_table2276
- GCC_except_table2285
- GCC_except_table2347
- GCC_except_table2399
- GCC_except_table2400
- GCC_except_table2493
- GCC_except_table2535
- GCC_except_table2543
- GCC_except_table2590
- GCC_except_table2759
- GCC_except_table2801
- GCC_except_table2826
- GCC_except_table2851
- GCC_except_table295
- GCC_except_table3027
- GCC_except_table3273
- GCC_except_table3297
- GCC_except_table3301
- GCC_except_table3420
- GCC_except_table3429
- GCC_except_table3437
- GCC_except_table3439
- GCC_except_table3467
- GCC_except_table3489
- GCC_except_table3659
- GCC_except_table3666
- GCC_except_table3670
- GCC_except_table3681
- GCC_except_table3688
- GCC_except_table3797
- GCC_except_table3888
- GCC_except_table3911
- GCC_except_table3926
- GCC_except_table3927
- GCC_except_table3933
- GCC_except_table3934
- GCC_except_table3935
- GCC_except_table3948
- GCC_except_table4164
- GCC_except_table4176
- GCC_except_table4181
- GCC_except_table4233
- GCC_except_table4238
- GCC_except_table4239
- GCC_except_table4247
- GCC_except_table4249
- GCC_except_table4277
- GCC_except_table4278
- GCC_except_table4280
- GCC_except_table4284
- GCC_except_table4287
- GCC_except_table4290
- GCC_except_table4291
- GCC_except_table4292
- GCC_except_table4294
- GCC_except_table4365
- GCC_except_table458
- GCC_except_table460
- GCC_except_table461
- GCC_except_table4668
- GCC_except_table4971
- GCC_except_table4981
- GCC_except_table4991
- GCC_except_table5050
- GCC_except_table5168
- GCC_except_table5246
- GCC_except_table5302
- GCC_except_table5304
- GCC_except_table5379
- GCC_except_table5384
- GCC_except_table5385
- GCC_except_table5386
- GCC_except_table5387
- GCC_except_table5416
- GCC_except_table5420
- GCC_except_table5421
- GCC_except_table5422
- GCC_except_table5427
- GCC_except_table5429
- GCC_except_table5431
- GCC_except_table5435
- GCC_except_table5436
- GCC_except_table5437
- GCC_except_table5438
- GCC_except_table5442
- GCC_except_table5445
- GCC_except_table5500
- GCC_except_table5511
- GCC_except_table5513
- GCC_except_table5547
- GCC_except_table5548
- GCC_except_table5549
- GCC_except_table5552
- GCC_except_table5555
- GCC_except_table5591
- GCC_except_table5701
- GCC_except_table5710
- GCC_except_table5717
- GCC_except_table5718
- GCC_except_table5719
- GCC_except_table5720
- GCC_except_table5721
- GCC_except_table5857
- GCC_except_table5893
- GCC_except_table5902
- GCC_except_table5904
- GCC_except_table5906
- GCC_except_table5909
- GCC_except_table5913
- GCC_except_table5940
- GCC_except_table5948
- GCC_except_table5949
- GCC_except_table5953
- GCC_except_table5972
- GCC_except_table5973
- GCC_except_table5978
- GCC_except_table5982
- GCC_except_table5984
- GCC_except_table5985
- GCC_except_table5997
- GCC_except_table685
- ImageHarmonizationKitLibraryCore.frameworkLibrary.19360
- MediaAnalysisLibrary.18675
- MediaAnalysisLibraryCore.frameworkLibrary.18686
- MediaAnalysisLibraryCore.frameworkLibrary.25552
- NUAssertLogger.1026
- NUAssertLogger.10336
- NUAssertLogger.10381
- NUAssertLogger.10801
- NUAssertLogger.1088
- NUAssertLogger.10976
- NUAssertLogger.11387
- NUAssertLogger.11488
- NUAssertLogger.11625
- NUAssertLogger.11907
- NUAssertLogger.1220
- NUAssertLogger.12632
- NUAssertLogger.12896
- NUAssertLogger.13051
- NUAssertLogger.1343
- NUAssertLogger.13762
- NUAssertLogger.14141
- NUAssertLogger.14486
- NUAssertLogger.14712
- NUAssertLogger.150
- NUAssertLogger.15049
- NUAssertLogger.1528
- NUAssertLogger.15311
- NUAssertLogger.15845
- NUAssertLogger.1612
- NUAssertLogger.16610
- NUAssertLogger.16840
- NUAssertLogger.17440
- NUAssertLogger.18174
- NUAssertLogger.18319
- NUAssertLogger.18439
- NUAssertLogger.18701
- NUAssertLogger.19348
- NUAssertLogger.1952
- NUAssertLogger.19524
- NUAssertLogger.20037
- NUAssertLogger.20159
- NUAssertLogger.20350
- NUAssertLogger.20837
- NUAssertLogger.2103
- NUAssertLogger.2204
- NUAssertLogger.22049
- NUAssertLogger.22469
- NUAssertLogger.22672
- NUAssertLogger.23142
- NUAssertLogger.23302
- NUAssertLogger.2360
- NUAssertLogger.23911
- NUAssertLogger.24282
- NUAssertLogger.24638
- NUAssertLogger.24890
- NUAssertLogger.25428
- NUAssertLogger.25693
- NUAssertLogger.25935
- NUAssertLogger.262
- NUAssertLogger.2640
- NUAssertLogger.26494
- NUAssertLogger.26860
- NUAssertLogger.27048
- NUAssertLogger.27183
- NUAssertLogger.27415
- NUAssertLogger.27494
- NUAssertLogger.2761
- NUAssertLogger.27695
- NUAssertLogger.3061
- NUAssertLogger.3226
- NUAssertLogger.3378
- NUAssertLogger.338
- NUAssertLogger.3589
- NUAssertLogger.3795
- NUAssertLogger.4059
- NUAssertLogger.433
- NUAssertLogger.4397
- NUAssertLogger.4660
- NUAssertLogger.4954
- NUAssertLogger.5051
- NUAssertLogger.5246
- NUAssertLogger.5456
- NUAssertLogger.562
- NUAssertLogger.5739
- NUAssertLogger.6012
- NUAssertLogger.6142
- NUAssertLogger.6245
- NUAssertLogger.6436
- NUAssertLogger.6603
- NUAssertLogger.7241
- NUAssertLogger.7462
- NUAssertLogger.7841
- NUAssertLogger.794
- NUAssertLogger.8391
- NUAssertLogger.8499
- NUAssertLogger.8843
- NUAssertLogger.9026
- NUAssertLogger.932
- NUAssertLogger.9324
- NUAssertLogger.9464
- NUAssertLogger.9544
- NUAssertLogger.9962
- NULogger.10013
- NULogger.12611
- NULogger.14589
- NULogger.22680
- NULogger.23956
- NULogger.26052
- NULogger.4131
- NURenderLogger.21298
- OBJC_IVAR_$_PIBrushStrokeHistoryEntry._needsPixellation
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor._asset
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor._mdataTrack
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor._videoTrack
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor.ndcMetadataTransform
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor.pxlMetadataTransform
- OBJC_IVAR_$_PIVideoReframeMetadataExtractor.timedMetadataArray
- OBJC_IVAR_$_PIVideoReframeTimedMetadata._estimatedCenterMotion
- OBJC_IVAR_$_PIVideoReframeTimedMetadata._estimatedMotionBlur
- OBJC_IVAR_$_PIVideoReframeTimedMetadata._time
- OBJC_IVAR_$_PIVideoReframeTimedMetadata._trajectoryHomography
- _CMMetadataFormatDescriptionGetIdentifiers
- _FigLivePhotoMetadataComputeDeserializationSize
- _FigLivePhotoMetadataDeserializeIntoBuffer
- _MergedGlobals.7
- _NSInternalInconsistencyException
- _OBJC_CLASS_$_AVAssetReader
- _OBJC_CLASS_$_AVAssetReaderOutputMetadataAdaptor
- _OBJC_CLASS_$_AVAssetReaderTrackOutput
- _OBJC_CLASS_$_PIVideoReframeMetadataExtractor
- _OBJC_CLASS_$_PIVideoReframeTimedMetadata
- _OBJC_METACLASS_$_PIVideoReframeMetadataExtractor
- _OBJC_METACLASS_$_PIVideoReframeTimedMetadata
- _ZL14NUAssertLoggerv.17289
- _ZL14NUAssertLoggerv.18895
- _ZL14NUAssertLoggerv.24939
- _ZL14NUAssertLoggerv.25807
- _ZL14NUAssertLoggerv.26710
- __45+[PIPhotoEditHelper filterNameForEffectName:]_block_invoke.295
- __48-[PISegmentationLoader _loadRegions:completion:]_block_invoke.195
- __48-[PISegmentationLoader _loadRegions:completion:]_block_invoke.198
- __48-[_PISensitiveContentAnalysisResult description]_block_invoke.32
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke.1147
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke.878
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_10.1070
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_11.1088
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_12.1142
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_2.1153
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_2.899
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_3.1180
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_3.911
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_4.941
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_5.956
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_6.980
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_7.995
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_8.1013
- __49+[PICompositionSerializerConstants conversionMap]_block_invoke_9.1061
- __50-[PISegmentationLoader _performLayout:completion:]_block_invoke.202
- __50-[PISegmentationLoader _performLayout:completion:]_block_invoke.203
- __76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke.116
- __76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke.117
- __76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke_2.118
- __79-[PISensitiveContentAnalysisRequest resolveWithInputBufferResponse:completion:]_block_invoke.148
- __85+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:renderer:error:]_block_invoke.141
- __85+[PIInpaintRendering renderImage:intoMutableBuffer:destinationBounds:renderer:error:]_block_invoke.147
- __Block_byref_object_copy_.10042
- __Block_byref_object_copy_.10452
- __Block_byref_object_copy_.10858
- __Block_byref_object_copy_.11747
- __Block_byref_object_copy_.11969
- __Block_byref_object_copy_.12604
- __Block_byref_object_copy_.13980
- __Block_byref_object_copy_.14154
- __Block_byref_object_copy_.14759
- __Block_byref_object_copy_.15908
- __Block_byref_object_copy_.16701
- __Block_byref_object_copy_.18265
- __Block_byref_object_copy_.18922
- __Block_byref_object_copy_.22695
- __Block_byref_object_copy_.24310
- __Block_byref_object_copy_.24959
- __Block_byref_object_copy_.4678
- __Block_byref_object_copy_.5737
- __Block_byref_object_copy_.6627
- __Block_byref_object_copy_.7269
- __Block_byref_object_copy_.8426
- __Block_byref_object_dispose_.10043
- __Block_byref_object_dispose_.10453
- __Block_byref_object_dispose_.10859
- __Block_byref_object_dispose_.11748
- __Block_byref_object_dispose_.11970
- __Block_byref_object_dispose_.12605
- __Block_byref_object_dispose_.13981
- __Block_byref_object_dispose_.14155
- __Block_byref_object_dispose_.14760
- __Block_byref_object_dispose_.15909
- __Block_byref_object_dispose_.16702
- __Block_byref_object_dispose_.18266
- __Block_byref_object_dispose_.18923
- __Block_byref_object_dispose_.22696
- __Block_byref_object_dispose_.24311
- __Block_byref_object_dispose_.24960
- __Block_byref_object_dispose_.4679
- __Block_byref_object_dispose_.5738
- __Block_byref_object_dispose_.6628
- __Block_byref_object_dispose_.7270
- __Block_byref_object_dispose_.8427
- __ImageHarmonizationKitLibraryCore_block_invoke.19361
- __MediaAnalysisLibraryCore_block_invoke.18687
- __MediaAnalysisLibraryCore_block_invoke.25553
- __MergedGlobals
- __NUAssertLogger_block_invoke.10355
- __NUAssertLogger_block_invoke.1040
- __NUAssertLogger_block_invoke.10444
- __NUAssertLogger_block_invoke.10823
- __NUAssertLogger_block_invoke.11070
- __NUAssertLogger_block_invoke.1120
- __NUAssertLogger_block_invoke.11403
- __NUAssertLogger_block_invoke.11563
- __NUAssertLogger_block_invoke.11656
- __NUAssertLogger_block_invoke.11787
- __NUAssertLogger_block_invoke.11931
- __NUAssertLogger_block_invoke.1223
- __NUAssertLogger_block_invoke.12643
- __NUAssertLogger_block_invoke.12915
- __NUAssertLogger_block_invoke.13067
- __NUAssertLogger_block_invoke.13778
- __NUAssertLogger_block_invoke.14117
- __NUAssertLogger_block_invoke.14535
- __NUAssertLogger_block_invoke.14750
- __NUAssertLogger_block_invoke.15068
- __NUAssertLogger_block_invoke.1533
- __NUAssertLogger_block_invoke.15454
- __NUAssertLogger_block_invoke.15867
- __NUAssertLogger_block_invoke.160
- __NUAssertLogger_block_invoke.1609
- __NUAssertLogger_block_invoke.16648
- __NUAssertLogger_block_invoke.16865
- __NUAssertLogger_block_invoke.17461
- __NUAssertLogger_block_invoke.18199
- __NUAssertLogger_block_invoke.18369
- __NUAssertLogger_block_invoke.18467
- __NUAssertLogger_block_invoke.18717
- __NUAssertLogger_block_invoke.19384
- __NUAssertLogger_block_invoke.19544
- __NUAssertLogger_block_invoke.1963
- __NUAssertLogger_block_invoke.20076
- __NUAssertLogger_block_invoke.20158
- __NUAssertLogger_block_invoke.20364
- __NUAssertLogger_block_invoke.2071
- __NUAssertLogger_block_invoke.20861
- __NUAssertLogger_block_invoke.2139
- __NUAssertLogger_block_invoke.22073
- __NUAssertLogger_block_invoke.2218
- __NUAssertLogger_block_invoke.22485
- __NUAssertLogger_block_invoke.22686
- __NUAssertLogger_block_invoke.2308
- __NUAssertLogger_block_invoke.23159
- __NUAssertLogger_block_invoke.23315
- __NUAssertLogger_block_invoke.24005
- __NUAssertLogger_block_invoke.2413
- __NUAssertLogger_block_invoke.24333
- __NUAssertLogger_block_invoke.24659
- __NUAssertLogger_block_invoke.24913
- __NUAssertLogger_block_invoke.25383
- __NUAssertLogger_block_invoke.25719
- __NUAssertLogger_block_invoke.26090
- __NUAssertLogger_block_invoke.26510
- __NUAssertLogger_block_invoke.2655
- __NUAssertLogger_block_invoke.26877
- __NUAssertLogger_block_invoke.27064
- __NUAssertLogger_block_invoke.27203
- __NUAssertLogger_block_invoke.27436
- __NUAssertLogger_block_invoke.27527
- __NUAssertLogger_block_invoke.27694
- __NUAssertLogger_block_invoke.2782
- __NUAssertLogger_block_invoke.285
- __NUAssertLogger_block_invoke.3048
- __NUAssertLogger_block_invoke.3166
- __NUAssertLogger_block_invoke.3248
- __NUAssertLogger_block_invoke.3412
- __NUAssertLogger_block_invoke.348
- __NUAssertLogger_block_invoke.3571
- __NUAssertLogger_block_invoke.3750
- __NUAssertLogger_block_invoke.4104
- __NUAssertLogger_block_invoke.4418
- __NUAssertLogger_block_invoke.442
- __NUAssertLogger_block_invoke.4677
- __NUAssertLogger_block_invoke.4983
- __NUAssertLogger_block_invoke.5111
- __NUAssertLogger_block_invoke.5378
- __NUAssertLogger_block_invoke.5497
- __NUAssertLogger_block_invoke.5753
- __NUAssertLogger_block_invoke.582
- __NUAssertLogger_block_invoke.6050
- __NUAssertLogger_block_invoke.6165
- __NUAssertLogger_block_invoke.6273
- __NUAssertLogger_block_invoke.6489
- __NUAssertLogger_block_invoke.6615
- __NUAssertLogger_block_invoke.7206
- __NUAssertLogger_block_invoke.7477
- __NUAssertLogger_block_invoke.7881
- __NUAssertLogger_block_invoke.816
- __NUAssertLogger_block_invoke.8415
- __NUAssertLogger_block_invoke.8532
- __NUAssertLogger_block_invoke.8859
- __NUAssertLogger_block_invoke.9074
- __NUAssertLogger_block_invoke.9150
- __NUAssertLogger_block_invoke.946
- __NUAssertLogger_block_invoke.9493
- __NUAssertLogger_block_invoke.9613
- __NUAssertLogger_block_invoke.9994
- __NULogger_block_invoke.10708
- __NULogger_block_invoke.10817
- __NULogger_block_invoke.1106
- __NULogger_block_invoke.11239
- __NULogger_block_invoke.11650
- __NULogger_block_invoke.11925
- __NULogger_block_invoke.12469
- __NULogger_block_invoke.1279
- __NULogger_block_invoke.1391
- __NULogger_block_invoke.14223
- __NULogger_block_invoke.14596
- __NULogger_block_invoke.15082
- __NULogger_block_invoke.1512
- __NULogger_block_invoke.15837
- __NULogger_block_invoke.16544
- __NULogger_block_invoke.18246
- __NULogger_block_invoke.19236
- __NULogger_block_invoke.19490
- __NULogger_block_invoke.20066
- __NULogger_block_invoke.20855
- __NULogger_block_invoke.21932
- __NULogger_block_invoke.22671
- __NULogger_block_invoke.23959
- __NULogger_block_invoke.24400
- __NULogger_block_invoke.2455
- __NULogger_block_invoke.25497
- __NULogger_block_invoke.26058
- __NULogger_block_invoke.277
- __NULogger_block_invoke.27720
- __NULogger_block_invoke.3453
- __NULogger_block_invoke.3586
- __NULogger_block_invoke.3864
- __NULogger_block_invoke.4134
- __NULogger_block_invoke.4754
- __NULogger_block_invoke.486
- __NULogger_block_invoke.5091
- __NULogger_block_invoke.5279
- __NULogger_block_invoke.5777
- __NULogger_block_invoke.6661
- __NULogger_block_invoke.7240
- __NULogger_block_invoke.738
- __NULogger_block_invoke.7624
- __NULogger_block_invoke.8384
- __NULogger_block_invoke.8597
- __NULogger_block_invoke.9323
- __NULogger_block_invoke.9959
- __NURenderLogger_block_invoke.18355
- __NURenderLogger_block_invoke.21327
- __OBJC_$_CLASS_METHODS_PIVideoReframeMetadataExtractor
- __OBJC_$_INSTANCE_METHODS_PIInpaintAdjustmentController
- __OBJC_$_INSTANCE_METHODS_PIVideoReframeMetadataExtractor
- __OBJC_$_INSTANCE_METHODS_PIVideoReframeTimedMetadata
- __OBJC_$_INSTANCE_VARIABLES_PIVideoReframeMetadataExtractor
- __OBJC_$_INSTANCE_VARIABLES_PIVideoReframeTimedMetadata
- __OBJC_$_PROP_LIST_PIVideoReframeMetadataExtractor
- __OBJC_$_PROP_LIST_PIVideoReframeTimedMetadata
- __OBJC_CLASS_RO_$_PIVideoReframeMetadataExtractor
- __OBJC_CLASS_RO_$_PIVideoReframeTimedMetadata
- __OBJC_METACLASS_RO_$_PIVideoReframeMetadataExtractor
- __OBJC_METACLASS_RO_$_PIVideoReframeTimedMetadata
- __Z24isLivePhotoMetadataTrackP12AVAssetTrack
- __ZNKSt3__16vectorI5SKnotNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIDv2_sNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIDv4_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIDv2_sEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2EmRKd
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___47+[PIObjectRemoval _regionSupportsObjectRemoval]_block_invoke
- ___51+[PIPerspectiveAutoCalculator requestVisionCleanUp]_block_invoke
- ___69+[PIAutoLoopAutoCalculator pipelineFilterForCorruptedVideoMitigation]_block_invoke
- ___76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke
- ___76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke_2
- ___76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke_3
- ___76-[PIBrushStrokeHistory _playbackHistoryIndex:toReceiver:options:completion:]_block_invoke_4
- ___ZL14NUAssertLoggerv_block_invoke.17320
- ___ZL14NUAssertLoggerv_block_invoke.18921
- ___ZL14NUAssertLoggerv_block_invoke.24988
- ___ZL14NUAssertLoggerv_block_invoke.25823
- ___ZL14NUAssertLoggerv_block_invoke.26752
- ___ZL8NULoggerv_block_invoke.24991
- ___ZL8NULoggerv_block_invoke.25850
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
- ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_96_e8_32s40bs48r56r64r72r80r88r_e5_v8?0l
- ___copy_helper_block_e8_32s40b48r56r64r72r80r88r
- ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r
- ___lightMapImageFromData_block_invoke.18515
- __block_literal_global.100.16515
- __block_literal_global.10093
- __block_literal_global.101.12912
- __block_literal_global.1015
- __block_literal_global.10159
- __block_literal_global.1022
- __block_literal_global.10352
- __block_literal_global.10441
- __block_literal_global.1063
- __block_literal_global.10703
- __block_literal_global.1072
- __block_literal_global.108.20361
- __block_literal_global.10854
- __block_literal_global.1090
- __block_literal_global.10923
- __block_literal_global.1117
- __block_literal_global.112.22796
- __block_literal_global.112.27679
- __block_literal_global.11235
- __block_literal_global.11400
- __block_literal_global.1144
- __block_literal_global.1149
- __block_literal_global.1155
- __block_literal_global.11560
- __block_literal_global.116.26420
- __block_literal_global.11640
- __block_literal_global.11730
- __block_literal_global.118.21290
- __block_literal_global.1182
- __block_literal_global.1184
- __block_literal_global.1187
- __block_literal_global.1189
- __block_literal_global.119
- __block_literal_global.1196
- __block_literal_global.1198
- __block_literal_global.1214
- __block_literal_global.12155
- __block_literal_global.1216
- __block_literal_global.1218
- __block_literal_global.1218.13257
- __block_literal_global.122.26415
- __block_literal_global.1220
- __block_literal_global.1222
- __block_literal_global.12400
- __block_literal_global.1243
- __block_literal_global.1245
- __block_literal_global.1250
- __block_literal_global.1252
- __block_literal_global.1254
- __block_literal_global.1256
- __block_literal_global.12618
- __block_literal_global.1268.22070
- __block_literal_global.1270.21432
- __block_literal_global.128.24656
- __block_literal_global.12996
- __block_literal_global.130
- __block_literal_global.13064
- __block_literal_global.13466
- __block_literal_global.13560
- __block_literal_global.13775
- __block_literal_global.139.8412
- __block_literal_global.14103
- __block_literal_global.143.26401
- __block_literal_global.14532
- __block_literal_global.14753
- __block_literal_global.15065
- __block_literal_global.1544
- __block_literal_global.15451
- __block_literal_global.156
- __block_literal_global.157
- __block_literal_global.158
- __block_literal_global.16.10857
- __block_literal_global.16052
- __block_literal_global.161.26396
- __block_literal_global.16358
- __block_literal_global.16552
- __block_literal_global.16645
- __block_literal_global.167
- __block_literal_global.16862
- __block_literal_global.16956
- __block_literal_global.1707
- __block_literal_global.17131
- __block_literal_global.17163
- __block_literal_global.17342
- __block_literal_global.17454
- __block_literal_global.17472
- __block_literal_global.177.18714
- __block_literal_global.179
- __block_literal_global.18071
- __block_literal_global.181
- __block_literal_global.182.22466
- __block_literal_global.18247
- __block_literal_global.18387
- __block_literal_global.18464
- __block_literal_global.185
- __block_literal_global.18546
- __block_literal_global.18722
- __block_literal_global.18918
- __block_literal_global.19104
- __block_literal_global.19232
- __block_literal_global.19381
- __block_literal_global.19486
- __block_literal_global.195.21167
- __block_literal_global.196
- __block_literal_global.1968
- __block_literal_global.198.18196
- __block_literal_global.200.18223
- __block_literal_global.20073
- __block_literal_global.20143
- __block_literal_global.2031
- __block_literal_global.20365
- __block_literal_global.20561
- __block_literal_global.20631
- __block_literal_global.211
- __block_literal_global.21340
- __block_literal_global.2136
- __block_literal_global.21467
- __block_literal_global.2199
- __block_literal_global.22247
- __block_literal_global.22799
- __block_literal_global.228
- __block_literal_global.2293
- __block_literal_global.23156
- __block_literal_global.23312
- __block_literal_global.240.26507
- __block_literal_global.24002
- __block_literal_global.24393
- __block_literal_global.24541
- __block_literal_global.2457
- __block_literal_global.24703
- __block_literal_global.24767
- __block_literal_global.24902
- __block_literal_global.24935
- __block_literal_global.251
- __block_literal_global.25265
- __block_literal_global.25368
- __block_literal_global.25716
- __block_literal_global.25820
- __block_literal_global.26087
- __block_literal_global.26529
- __block_literal_global.2666
- __block_literal_global.26749
- __block_literal_global.26874
- __block_literal_global.27200
- __block_literal_global.27442
- __block_literal_global.27605
- __block_literal_global.27651
- __block_literal_global.2779
- __block_literal_global.282
- __block_literal_global.284
- __block_literal_global.286
- __block_literal_global.29.25229
- __block_literal_global.292.14747
- __block_literal_global.294.14764
- __block_literal_global.302
- __block_literal_global.3034
- __block_literal_global.306
- __block_literal_global.31.4410
- __block_literal_global.311.25473
- __block_literal_global.314
- __block_literal_global.3151
- __block_literal_global.3245
- __block_literal_global.325
- __block_literal_global.327
- __block_literal_global.33.6030
- __block_literal_global.33.7783
- __block_literal_global.3442
- __block_literal_global.351
- __block_literal_global.3556
- __block_literal_global.3751
- __block_literal_global.41.18725
- __block_literal_global.4286
- __block_literal_global.4408
- __block_literal_global.4668
- __block_literal_global.468
- __block_literal_global.48.7771
- __block_literal_global.4908
- __block_literal_global.50.6047
- __block_literal_global.500
- __block_literal_global.502
- __block_literal_global.5108
- __block_literal_global.54.27433
- __block_literal_global.5423
- __block_literal_global.56.21286
- __block_literal_global.56.24475
- __block_literal_global.56.26466
- __block_literal_global.5647
- __block_literal_global.579
- __block_literal_global.5791
- __block_literal_global.58.21284
- __block_literal_global.6058
- __block_literal_global.6074
- __block_literal_global.6162
- __block_literal_global.6270
- __block_literal_global.63.20049
- __block_literal_global.633
- __block_literal_global.635
- __block_literal_global.647
- __block_literal_global.6486
- __block_literal_global.649
- __block_literal_global.6718
- __block_literal_global.683
- __block_literal_global.6845
- __block_literal_global.71.26455
- __block_literal_global.7302
- __block_literal_global.733
- __block_literal_global.74
- __block_literal_global.7405
- __block_literal_global.7620
- __block_literal_global.7788
- __block_literal_global.7878
- __block_literal_global.8012
- __block_literal_global.81.20550
- __block_literal_global.813
- __block_literal_global.8377
- __block_literal_global.8590
- __block_literal_global.880
- __block_literal_global.8856
- __block_literal_global.9.12395
- __block_literal_global.9.25259
- __block_literal_global.901
- __block_literal_global.9071
- __block_literal_global.91.16139
- __block_literal_global.91.19127
- __block_literal_global.91.20541
- __block_literal_global.913
- __block_literal_global.9135
- __block_literal_global.93.10812
- __block_literal_global.93.27524
- __block_literal_global.943
- __block_literal_global.943.13473
- __block_literal_global.9490
- __block_literal_global.95.24910
- __block_literal_global.958
- __block_literal_global.9610
- __block_literal_global.98
- __block_literal_global.982
- __block_literal_global.99.19119
- __block_literal_global.997
- __getMediaAnalysisResultAttributesKeySymbolLoc_block_invoke.18729
- __getMediaAnalysisResultsKeySymbolLoc_block_invoke.18719
- __getVCPMediaAnalysisServiceClass_block_invoke.18674
- __getVCPMediaAnalysisServiceClass_block_invoke.25542
- _angular_error
- _kFigMetadataDataType_QuickTimeMetadataLivePhotoInfo
- _kFigMetadataIdentifier_QuickTimeMetadataLivePhotoInfo
- _objc_exception_throw
- _objc_msgSend$_playbackHistoryIndex:toReceiver:options:completion:
- _objc_msgSend$_regionSupportsObjectRemoval
- _objc_msgSend$addImageSpaceInpaintingStroke:exclusionMask:closeAndFillStroke:needsPixellation:recordStroke:completion:
- _objc_msgSend$addOutput:
- _objc_msgSend$assetReaderWithAsset:error:
- _objc_msgSend$canAddOutput:
- _objc_msgSend$centerMotionVectorFromMetadata:
- _objc_msgSend$currentSensitivityExceedsThresholdsV1:initialSensitivity:
- _objc_msgSend$dataType
- _objc_msgSend$dataValue
- _objc_msgSend$deviceSupportsObjectRemoval
- _objc_msgSend$encodedPixelSizeOfTrack:oriented:
- _objc_msgSend$exceptionWithName:reason:userInfo:
- _objc_msgSend$extractMetadata
- _objc_msgSend$formatDescriptions
- _objc_msgSend$initWithAssetReaderTrackOutput:
- _objc_msgSend$initWithTrack:outputSettings:
- _objc_msgSend$inpaintEnablesRefinementPass
- _objc_msgSend$inpaintPixellationIntersectionAreaToFaceAreaThreshold
- _objc_msgSend$inpaintPixellationIntersectionAreaToMaskAreaThreshold
- _objc_msgSend$inpaintShowsSurroundOutline
- _objc_msgSend$inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:
- _objc_msgSend$macOSDeviceIsAppleSilicon
- _objc_msgSend$motionBlurVectorFromMetadata:
- _objc_msgSend$needsPixellation
- _objc_msgSend$nextTimedMetadataGroup
- _objc_msgSend$objectRemovalRegionOverride
- _objc_msgSend$pipelineFilterForCorruptedVideoMitigation
- _objc_msgSend$releaseCachedResources
- _objc_msgSend$sanitizePixelBuffer:error:
- _objc_msgSend$sensitivityCheckVersion2Thresholds
- _objc_msgSend$setBackends:
- _objc_msgSend$setEstimatedCenterMotion:
- _objc_msgSend$setEstimatedMotionBlur:
- _objc_msgSend$setNeedsPixellation:
- _objc_msgSend$setTrajectoryHomography:
- _objc_msgSend$sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:
- _objc_msgSend$tracks
- _objc_msgSend$trajectoryeHomographyFromMetadata:containsV3Metadata:
- _regionSupportsObjectRemoval.cleanupSupported
- _regionSupportsObjectRemoval.once
- _symbolic _____yypG s23_ContiguousArrayStorageC
- audit_stringImageHarmonizationKit.19375
- audit_stringMediaAnalysis.18693
- audit_stringMediaAnalysis.25564
- colorBalanceKernels.colorBalanceKernels.24827
- colorBalanceKernels.onceToken.24826
- getMediaAnalysisResultAttributesKeySymbolLoc.ptr.18728
- getMediaAnalysisResultsKey.18699
- getMediaAnalysisResultsKeySymbolLoc.ptr.18718
- getVCPMediaAnalysisServiceClass.18672
- getVCPMediaAnalysisServiceClass.softClass.18673
- getVCPMediaAnalysisServiceClass.softClass.25541
- initialize.onceToken.12159
- initialize.onceToken.21364
- initialize.onceToken.23014
- initialize.onceToken.24441
- kernel.kernel.2200
- kernel.onceToken.2198
- roiCallback_block_invoke.24905
- s_log.11980
- s_log.22668
- s_log.24300
- s_signpost.11981
- s_signpost.22669
- s_signpost.24301
CStrings:
+ "+[PIInpaintRendering inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:operation:]"
+ "+[PIObjectRemoval maskIsMostlyWithinFace:imageSize:imageOrientation:intAreaOverMaskAreaThreshold:intAreaOverFaceAreaThreshold:detectedFaces:]"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/ApertureRedEye/PIApertureRedEye.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/ApertureRedEye/PIApertureRedEyeFilter.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PIFalseColorHDRDebug.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PILevelsFilterHDR.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PIPhotoEffectHDR.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIBilateralFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIColorBalanceFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIColorNormalizationFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PICoreImageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PICurvesFilter.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIFakeBoost.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIHighKey.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIIPTHueChromaFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PILevelsFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PINeutralGrayWhiteBalanceFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PISpillSuppression.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PITempTintFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/Retouch/PIObjectRemoval.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/Retouch/PIRepair.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoop.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopFrameNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+Analysis.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+Export.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+LongExposure.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopRequests.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopStabVideoNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopVideoNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIApertureRedEyeAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIAutoCalculators.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIAutoLoopAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIColorNormalizationAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PICropAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PICurvesAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIDisparitySampleRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PILevelsAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PILongExposureFusionAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIPerspectiveAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIPortraitAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISemanticStyleAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISensitiveContentAnalysisRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISmartBlackAndWhiteAutoCalculator.mm"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PITapToTrackRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIVideoStabilizeRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIWhiteBalanceAutoCalculators.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/SliderNet/PISliderNetAdjustmentsRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/SliderNet/PISmartCopyPasteAutoCalculator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/Conversion/PICompositionSerializer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/Conversion/PICompositionSidecarData.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICompositionController+AdjustmentExtensions.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICompositionController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICropAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIInpaintAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIOrientationAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PISemanticStyleAdjustmentController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxAsset.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxClockLayoutRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxClockMaterialRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorAnalysis.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorAnalysisRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorPalette.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorSuggester.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxCompoundLayerStackRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxInfillRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxLayerStackRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxLegacyPosterStyle.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxRecipeFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyle.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipe.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipeArchiver.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipeRegistry.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterInactiveFrameLayoutRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterLayoutHelper.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterLayoutRequest.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterSettlingEffectLoader.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentation.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationHelper.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationInfillFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationItem.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationLayoutRegions.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationLoader.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIInpaintCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIModernPhotosPipeline.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPhotosPipelineHelper.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPipelineFilters.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPortraitNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIRetouchCacheNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PISchema.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PICinematicAudioRenderNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintAuxiliaryImageNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintOperation.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintRendering.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoDebugDetectionsRenderNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoRenderNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoRenderer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PISemanticStyleFilter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PISemanticStyleRenderNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIVideoReframeNode.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIBrushStrokeHistory.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PICompositionExporter.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIHDRUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIImageIO.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIPerfPowerService.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIPhotoEditHelper.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIThumbnailGenerator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Video Stabilization/PIVideoCrossfadeLoopNode.m"
+ "/System/AppleInternal/Library/Frameworks/PhotosIntelligence.framework/PhotosIntelligence"
+ "1.12.2"
+ "3"
+ "@52@0:8@16@24@32f40@44"
+ "B72@0:8@16{?=qq}24q40d48d56@64"
+ "Bad float->half conversion"
+ "Bad half->float conversion"
+ "Cleanup"
+ "Cleanup available"
+ "Cleanup device support YES (AS Mac)"
+ "Cleanup device support check overridden to YES"
+ "Cleanup restricted (eligibility %ld)"
+ "Cleanup unavailable (device support)"
+ "Cleanup unavailable (eligibility %ld)"
+ "Cleanup: Disabling refinement for legacy models"
+ "Cleanup: Selecting legacy face model"
+ "Cleanup: Selecting legacy general model"
+ "CleanupPlusRetouch"
+ "Could not create cleanup model bundle URL"
+ "Couldn't transcode from accumulation buffer to float: %@"
+ "Couldn't transcode from float to accumulation buffer: %@"
+ "DeltaApplying"
+ "Did not get the expected signal. Expected %@, got %@"
+ "Downloaded %s / %s bytes for Clean Up resource (%f %%)"
+ "Failed to run SCMLImageSanitizer: asset out of date"
+ "Generative models available"
+ "Generative models restricted: %s"
+ "Generative models unavailable: %s"
+ "GenerativeEdit.CleanUp"
+ "Language code not available, unable to check Apple Intelligence availability, the status is set to unsupported"
+ "PICleanupAvailability"
+ "PIGenerativeModels"
+ "PIGenerativeModelsStatus"
+ "PIInpaintAdjustmentDelta"
+ "PIRepair.mm"
+ "PISensitiveContent: sanitization returned GuardrailOutOfDate error: %@"
+ "PISensitiveContent: sanitization returned general error: %@"
+ "T@\"NSArray\",C,N,V_masks"
+ "T@\"NSArray\",C,N,V_operations"
+ "T@\"NSDictionary\",N,C"
+ "T@\"NSString\",N,C"
+ "TB,N,V_needsFacePixellation"
+ "TB,N,V_performRegionSpecificChecks"
+ "TB,R,N,V_repairEdges"
+ "Tq,R,N,V_availabilityStatus"
+ "Tq,R,N,V_status"
+ "T{CGPoint=dd},R,N,V_sourceOffset"
+ "Unexpected state: %s"
+ "_PICleanupAvailability"
+ "_availabilityStatus"
+ "_deviceSupportsCleanup"
+ "_fetchCleanupAvailability"
+ "_masks"
+ "_needsFacePixellation"
+ "_performRegionSpecificChecks"
+ "_playbackHistoryIndex:toReceiver:options:pauseInterval:completion:"
+ "_status"
+ "_warmUpOperation:context:"
+ "addImageSpaceInpaintingStroke:exclusionMask:closeAndFillStroke:needsFacePixellation:recordStroke:completion:"
+ "adjustmentHasRetouchStyleCleanupOperations:settings:"
+ "allowRetouchAndCleanup"
+ "appendCloneStroke:sourceOffset:repairEdges:"
+ "applyDelta:"
+ "availabilityStatus"
+ "cancelCropRectsRequest:"
+ "configureFilter:withOptions:"
+ "couldn't create dest buffer"
+ "couldn't create source buffer"
+ "deltaFromComposition:"
+ "domain"
+ "ensureAvailability:"
+ "generativemodels"
+ "i24@0:8@?<v@?{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}@\"NSError\">16"
+ "initWithInteger:"
+ "initWithOperations:masks:"
+ "initWithStatus:"
+ "initWithStroke:closed:skipSegmentationIntersections:needsFacePixellation:subjectHitTestRadius:"
+ "inp_fcs_eds2_00_q16_s30"
+ "inp_gen_eds2_00_q16"
+ "inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:operation:"
+ "loadCropRectsWithResultHandler:"
+ "maskIsMostlyWithinFace:imageSize:imageOrientation:intAreaOverMaskAreaThreshold:intAreaOverFaceAreaThreshold:detectedFaces:"
+ "masks"
+ "needsFacePixellation"
+ "numberWithLong:"
+ "overrideCleanupHardwareCheck"
+ "performRegionSpecificChecks"
+ "pipelineFilterForRevertedOriginal"
+ "pipelineFilterForUnRevertedOriginal"
+ "playbackHistoryToReceiver:options:pauseInterval:completion:"
+ "redactedCopy"
+ "resetUnadjustedThumbnails"
+ "sanitizeRequestAsynchronously:completionHandler:"
+ "setMasks:"
+ "setModelManagerServicesUseCaseID:"
+ "setNeedsFacePixellation:"
+ "setNumberStyle:"
+ "setOperations:"
+ "setPerformRegionSpecificChecks:"
+ "set_cleanupModelBundleURLString:"
+ "set_metadataVersionInfo:"
+ "sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:operation:"
+ "stringFromNumber:"
+ "transcodePixelBuffer:toBuffer:error:"
+ "updateAvailability"
+ "useOldFilterForOldModelStrokes"
+ "useRefinementForOldModelStrokes"
+ "v24@?0@\"SCMLImageSanitization\"8@\"NSError\"16"
+ "v44@0:8@16{CGPoint=dd}24B40"
+ "v48@0:8@16Q24d32@?40"
+ "v56@0:8Q16@24Q32d40@?48"
+ "v80@?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40@\"NSError\"72"
+ "{?={?=qq}{?=qq}}120@0:8{?={?=qq}{?=qq}}16{?={?=qq}{?=qq}}48{?={?=qq}{?=qq}}80@112"
- "+[PIInpaintRendering inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:]"
- "+[PIObjectRemoval _regionSupportsObjectRemoval] is overridden to YES via defaults"
- "+[PIObjectRemoval maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:]"
- "-[PIVideoReframeMetadataExtractor extractMetadata]"
- "-[PIVideoReframeMetadataExtractor motionBlurVectorFromMetadata:]"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/ApertureRedEye/PIApertureRedEye.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/ApertureRedEye/PIApertureRedEyeFilter.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PIFalseColorHDRDebug.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PILevelsFilterHDR.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/HDR/PIPhotoEffectHDR.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIBilateralFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIColorBalanceFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIColorNormalizationFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PICoreImageUtilities.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PICurvesFilter.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIFakeBoost.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIHighKey.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PIIPTHueChromaFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PILevelsFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PINeutralGrayWhiteBalanceFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PISpillSuppression.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PITempTintFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/Retouch/PIObjectRemoval.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/Retouch/PIRepair.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoop.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopCacheNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopFrameNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+Analysis.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+Export.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopJob+LongExposure.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopRequests.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopStabVideoNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/AutoLoop/PIAutoLoopVideoNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIApertureRedEyeAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIAutoCalculators.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIAutoLoopAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIColorNormalizationAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PICropAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PICurvesAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIDisparitySampleRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PILevelsAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PILongExposureFusionAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIPerspectiveAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIPortraitAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISemanticStyleAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISensitiveContentAnalysisRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISmartBlackAndWhiteAutoCalculator.mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PITapToTrackRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIVideoStabilizeRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PIWhiteBalanceAutoCalculators.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/SliderNet/PISliderNetAdjustmentsRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/SliderNet/PISmartCopyPasteAutoCalculator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/Conversion/PICompositionSerializer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/Conversion/PICompositionSidecarData.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICompositionController+AdjustmentExtensions.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICompositionController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PICropAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIInpaintAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PIOrientationAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Controllers/PISemanticStyleAdjustmentController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxAsset.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxClockLayoutRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxClockMaterialRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorAnalysis.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorAnalysisRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorPalette.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxColorSuggester.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxCompoundLayerStackRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxInfillRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxLayerStackRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxLegacyPosterStyle.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxRecipeFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyle.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipe.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipeArchiver.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIParallaxStyleRecipeRegistry.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterInactiveFrameLayoutRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterLayoutHelper.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterLayoutRequest.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterSettlingEffectLoader.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentation.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationHelper.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationInfillFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationItem.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationLayoutRegions.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PISegmentationLoader.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIInpaintCacheNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIModernPhotosPipeline.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPhotosPipelineHelper.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPipelineFilters.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIPortraitNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PIRetouchCacheNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/PISchema.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PICinematicAudioRenderNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintAuxiliaryImageNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintOperation.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIInpaintRendering.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoDebugDetectionsRenderNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoRenderNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIPortraitVideoRenderer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PISemanticStyleFilter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PISemanticStyleRenderNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Render/PIVideoReframeNode.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIBrushStrokeHistory.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PICompositionExporter.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIHDRUtilities.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIImageIO.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIPerfPowerService.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIPhotoEditHelper.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIThumbnailGenerator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Video Stabilization/PIVideoCrossfadeLoopNode.m"
- "0 && \"unexpected metadata data type\""
- "0 && \"unexpected metadata identifier\""
- "@\"AVAssetTrack\""
- "@44@0:8@16@24@32f40"
- "Asset does not contain Live Photo metadata track"
- "Bad fixed float to half float conversion"
- "Bad half float to float conversion"
- "Can't add metadata output for asset"
- "Can't find enabled video track in asset: %@"
- "Did not get the expected signal: %@"
- "Error creating asset reader: %@"
- "Failed to start reading asset"
- "Fatal error"
- "Finished metadata extraction"
- "Insufficient space allocated to copy string contents"
- "PIObjectRemoval: Clean up unavailable due to result of os_eligibility checks"
- "PIRepair expects the incoming image to be RGBAh, not %@"
- "PIVideoReframeMetadataExtractor"
- "PIVideoReframeMetadataExtractor.mm"
- "PIVideoReframeTimedMetadata"
- "PI_SENSITIVITY_V2_THRESHOLDS"
- "Requesting forced cleanup of Vision caches"
- "Starting metadata extraction"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSArray\",R,N,VtimedMetadataArray"
- "TB,N,V_needsPixellation"
- "Track does not contain V3 metadata"
- "T{?=[3]},R,V_trajectoryHomography"
- "T{?=qiIq},R,V_time"
- "T{CGVector=dd},R,V_estimatedCenterMotion"
- "T{CGVector=dd},R,V_estimatedMotionBlur"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_estimatedCenterMotion"
- "_estimatedMotionBlur"
- "_mdataTrack"
- "_needsPixellation"
- "_playbackHistoryIndex:toReceiver:options:completion:"
- "_regionSupportsObjectRemoval"
- "_trajectoryHomography"
- "_videoTrack"
- "addImageSpaceInpaintingStroke:exclusionMask:closeAndFillStroke:needsPixellation:recordStroke:completion:"
- "addOutput:"
- "assetReaderWithAsset:error:"
- "canAddOutput:"
- "centerMotionVectorFromMetadata:"
- "currentSensitivityExceedsThresholdsV1:initialSensitivity:"
- "dataType"
- "dataValue"
- "deviceSupportsObjectRemoval"
- "encodedPixelSizeOfTrack:oriented:"
- "err == noErr"
- "estimatedCenterMotion"
- "estimatedMotionBlur"
- "exceptionWithName:reason:userInfo:"
- "extractMetadata"
- "formatDescriptions"
- "init is not a valid initializer"
- "initWithAssetReaderTrackOutput:"
- "initWithStroke:closed:skipSegmentationIntersections:needsPixellation:subjectHitTestRadius:"
- "initWithTrack:outputSettings:"
- "inpaintEnablesRefinementPass"
- "inpaintShowsSurroundOutline"
- "inpaintedImageWithInputImage:maskImage:exclusionMaskImage:headroom:"
- "invalid Collection: less than 'count' elements in collection"
- "ivs.nsfw_any"
- "macOSDeviceIsAppleSilicon"
- "maskIsMostlyWithinFace:imageSize:imageOrientation:detectedFaces:"
- "mdataGroup.items.count == 1"
- "motionBlurVectorFromMetadata:"
- "ndcMetadataTransform"
- "nextTimedMetadataGroup"
- "pipelineFilterForCorruptedVideoMitigation"
- "pxlMetadataTransform"
- "releaseCachedResources"
- "requestVisionCleanUp"
- "sanitizePixelBuffer:error:"
- "sensitivityCheckVersion2Thresholds"
- "setBackends:"
- "setEstimatedCenterMotion:"
- "setEstimatedMotionBlur:"
- "setNeedsPixellation:"
- "setSensitivityCheckVersion2Thresholds:"
- "setTrajectoryHomography:"
- "sourceExtentForMaskExtent:exclusionMaskExtent:imageExtent:"
- "takeNewOperationsFromComposition:redactNewOperations:"
- "tracks"
- "trajectoryeHomographyFromMetadata:containsV3Metadata:"
- "v1"
- "v28@0:8@16B24"
- "v32@0:8{CGVector=dd}16"
- "v48@0:8Q16@24Q32@?40"
- "v64@0:8{?=[3]}16"
- "{?=[3]}32@0:8r^{FigLivePhotoMetadata=I{FigLivePhotoMetadataV1Struct=fqffffffccSI[0{FigLivePhotoDetectedFaceV1Struct=qffffisS}]}}16^B24"
- "{?={?=qq}{?=qq}}112@0:8{?={?=qq}{?=qq}}16{?={?=qq}{?=qq}}48{?={?=qq}{?=qq}}80"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGVector=\"dx\"d\"dy\"d}"
- "{CGVector=dd}16@0:8"
- "{CGVector=dd}24@0:8r^{FigLivePhotoMetadata=I{FigLivePhotoMetadataV1Struct=fqffffffccSI[0{FigLivePhotoDetectedFaceV1Struct=qffffisS}]}}16"

```
