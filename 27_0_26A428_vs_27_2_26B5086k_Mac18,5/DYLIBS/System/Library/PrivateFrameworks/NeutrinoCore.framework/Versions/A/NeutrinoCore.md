## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/Versions/A/NeutrinoCore`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x339830
-  __TEXT.__objc_methlist: 0x20834
-  __TEXT.__const: 0x2918
+916.41.100.0.0
+  __TEXT.__text: 0x343710
+  __TEXT.__objc_methlist: 0x20f0c
+  __TEXT.__const: 0x27a8
   __TEXT.__dlopen_cstrs: 0x45
-  __TEXT.__swift5_typeref: 0x3e7
+  __TEXT.__swift5_typeref: 0x3c9
   __TEXT.__swift5_reflstr: 0x93
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_fieldmd: 0x178
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x3fbf3
-  __TEXT.__swift5_capture: 0x210
-  __TEXT.__gcc_except_tab: 0x8060
-  __TEXT.__oslogstring: 0x57c3
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_fieldmd: 0x15c
+  __TEXT.__swift5_proto: 0x64
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__cstring: 0x40412
+  __TEXT.__swift5_capture: 0x230
+  __TEXT.__gcc_except_tab: 0x81ac
+  __TEXT.__oslogstring: 0x5930
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0xa260
-  __TEXT.__eh_frame: 0x430
+  __TEXT.__unwind_info: 0xa3f0
+  __TEXT.__eh_frame: 0x460
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1610
-  __DATA_CONST.__objc_classlist: 0x15c8
+  __DATA_CONST.__const: 0x1650
+  __DATA_CONST.__objc_classlist: 0x15f8
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x500
+  __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb4a8
-  __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0xfe8
+  __DATA_CONST.__objc_selrefs: 0xb6d0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x1010
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x2240
-  __AUTH_CONST.__const: 0x8108
-  __AUTH_CONST.__cfstring: 0x1cf20
-  __AUTH_CONST.__objc_const: 0x36938
+  __DATA_CONST.__got: 0x2290
+  __AUTH_CONST.__const: 0x8238
+  __AUTH_CONST.__cfstring: 0x1d080
+  __AUTH_CONST.__objc_const: 0x37770
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x8b8
+  __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xfe8
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x19c4
-  __DATA.__data: 0x3958
+  __AUTH_CONST.__auth_got: 0xfd0
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x1a4c
+  __DATA.__data: 0x3938
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xd8e0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11858
-  Symbols:   25430
-  CStrings:  7245
+  Functions: 11995
+  Symbols:   25733
+  CStrings:  7293
 
Symbols:
+ +[NUAssetCapability HDR]
+ +[NUAssetCapability audio]
+ +[NUAssetCapability hdrGainMap]
+ +[NUAssetCapability rawDecode]
+ +[NUAssetCapability rawDecode_v6]
+ +[NUAssetCapability rawDecode_v7]
+ +[NUAssetCapability rawDecode_v8]
+ +[NUAssetCapability rawDecode_v9]
+ +[NUChannelControlData nullDataWithOptionalFormat:]
+ +[NULivePhotoExportFormat heic]
+ +[NULivePhotoExportFormat jpeg]
+ +[_NUPipeline defaultPipelineNameFromTypeName:]
+ -[NSNull(NUControlDataRepresentable) nu_convertedFromFormat:toFormat:error:]
+ -[NUAssetCapability .cxx_destruct]
+ -[NUAssetCapability description]
+ -[NUAssetCapability evaluateForAsset:]
+ -[NUAssetCapability initWithName:]
+ -[NUAssetCapability name]
+ -[NUAuxiliaryImageRenderRequest setTargetPixelFormat:]
+ -[NUAuxiliaryImageRenderRequest targetPixelFormat]
+ -[NUChannelControlData isNull]
+ -[NUControlDescriptor isOptional]
+ -[NUFixedRegionPolicy initWithRect:scale:]
+ -[NUFixedRegionPolicy initWithRegion:scale:]
+ -[NUGainMapExportOptions .cxx_destruct]
+ -[NUGainMapExportOptions copyWithZone:]
+ -[NUGainMapExportOptions flexRangeProperties]
+ -[NUGainMapExportOptions forceGainMapGeneration]
+ -[NUGainMapExportOptions init]
+ -[NUGainMapExportOptions pixelFormat]
+ -[NUGainMapExportOptions scale]
+ -[NUGainMapExportOptions setFlexRangeProperties:]
+ -[NUGainMapExportOptions setForceGainMapGeneration:]
+ -[NUGainMapExportOptions setPixelFormat:]
+ -[NUGainMapExportOptions setScale:]
+ -[NUHistogramRenderJob mediaToRender:error:]
+ -[NUHistogramRenderJob targetHeadroom]
+ -[NUImageExportJob _defaultGainMapExportOptions:]
+ -[NUImageExportJob _requestedAuxiliaryOptions]
+ -[NUImageExportJob auxErrors]
+ -[NUImageExportJob auxiliaryImageOptions]
+ -[NUImageExportJob setAuxiliaryImageOptions:]
+ -[NUImageExportRequest auxiliaryImageOptions]
+ -[NUImageExportRequest gainMapExportOptions]
+ -[NUImageExportRequest setAuxiliaryImageOptions:]
+ -[NUImageExportRequest setGainMapExportOptions:]
+ -[NULivePhotoExportFormat .cxx_destruct]
+ -[NULivePhotoExportFormat copyWithZone:]
+ -[NULivePhotoExportFormat imageFormat]
+ -[NULivePhotoExportFormat initWithImageFormat:videoCodecType:]
+ -[NULivePhotoExportFormat init]
+ -[NULivePhotoExportFormat videoCodecType]
+ -[NULivePhotoExportJob .cxx_destruct]
+ -[NULivePhotoExportJob _captureImageResponse:]
+ -[NULivePhotoExportJob _captureVideoResponse:]
+ -[NULivePhotoExportJob complete:]
+ -[NULivePhotoExportJob evaluateRenderDependencies:]
+ -[NULivePhotoExportJob initWithExportRequest:]
+ -[NULivePhotoExportJob initWithLivePhotoExportRequest:]
+ -[NULivePhotoExportJob initWithRequest:]
+ -[NULivePhotoExportJob livePhotoRequest]
+ -[NULivePhotoExportJob result]
+ -[NULivePhotoExportJob wantsCompleteStage]
+ -[NULivePhotoExportJob wantsPrepareNodeCached]
+ -[NULivePhotoExportJob wantsRenderNodeCached]
+ -[NULivePhotoExportJob wantsRenderStage]
+ -[NULivePhotoExportRequest .cxx_destruct]
+ -[NULivePhotoExportRequest _commonInit]
+ -[NULivePhotoExportRequest _renderContextWithName:]
+ -[NULivePhotoExportRequest applyImageOrientationAsMetadata]
+ -[NULivePhotoExportRequest applyVideoOrientationAsMetadata]
+ -[NULivePhotoExportRequest auxiliaryImageOptions]
+ -[NULivePhotoExportRequest copyWithZone:]
+ -[NULivePhotoExportRequest format]
+ -[NULivePhotoExportRequest gainMapExportOptions]
+ -[NULivePhotoExportRequest imageColorSpace]
+ -[NULivePhotoExportRequest imageProperties]
+ -[NULivePhotoExportRequest imageRequest]
+ -[NULivePhotoExportRequest initWithComposition:]
+ -[NULivePhotoExportRequest initWithComposition:destinationURL:]
+ -[NULivePhotoExportRequest initWithMedia:destinationURL:]
+ -[NULivePhotoExportRequest initWithMedia:destinationURL:videoComplementURL:]
+ -[NULivePhotoExportRequest initWithRequest:]
+ -[NULivePhotoExportRequest mediaComponentType]
+ -[NULivePhotoExportRequest newRenderJob]
+ -[NULivePhotoExportRequest pairingIdentifier]
+ -[NULivePhotoExportRequest setApplyImageOrientationAsMetadata:]
+ -[NULivePhotoExportRequest setApplyVideoOrientationAsMetadata:]
+ -[NULivePhotoExportRequest setAuxiliaryImageOptions:]
+ -[NULivePhotoExportRequest setFormat:]
+ -[NULivePhotoExportRequest setGainMapExportOptions:]
+ -[NULivePhotoExportRequest setImageColorSpace:]
+ -[NULivePhotoExportRequest setImageProperties:]
+ -[NULivePhotoExportRequest setPairingIdentifier:]
+ -[NULivePhotoExportRequest setTargetHeadroom:]
+ -[NULivePhotoExportRequest setVideoColorSpace:]
+ -[NULivePhotoExportRequest setVideoComplementURL:]
+ -[NULivePhotoExportRequest submit:]
+ -[NULivePhotoExportRequest targetHeadroom]
+ -[NULivePhotoExportRequest videoColorSpace]
+ -[NULivePhotoExportRequest videoComplementURL]
+ -[NULivePhotoExportRequest videoRequest]
+ -[NUPipelineOutputNode contentHeadroom]
+ -[NUPipelineOutputNode targetHeadroom]
+ -[NURenderJob(Media) alternateMediaForMedia:targetHeadroom:error:]
+ -[NURenderJob(Media) containerMediaForMedia:]
+ -[NURenderJob(Media) gainMapMediaFromBaseMedia:alternateMedia:scale:flexRangeProperties:error:]
+ -[NURenderJob(Media) hdrMediaFromBaseMedia:gainMap:targetHeadroom:error:]
+ -[NURenderJob(Media) mixMedia:alternate:targetHeadroom:error:]
+ -[NURenderJob(Media) toneMapHDRMedia:targetHeadroom:error:]
+ -[NUStyleTransferPipeline initWithName:opaque:]
+ -[NUVideoExportRequest audioMode]
+ -[NUVideoExportRequest audioOutputSettings]
+ -[NUVideoExportRequest setAudioMode:]
+ -[NUVideoExportRequest setAudioOutputSettings:]
+ -[_NUAsset _evaluateCapability:]
+ -[_NUAsset dataForCapability:]
+ -[_NUAssetPipeline initWithAsset:name:]
+ -[_NUAssetPipeline initWithName:opaque:]
+ -[_NUCachePipeline initWithName:opaque:]
+ -[_NUChannelPort clearData]
+ -[_NUComposedMedia colorSpace]
+ -[_NUComposedMedia contentHeadroom]
+ -[_NUConstantPipeline initWithName:opaque:]
+ -[_NUContainerMedia colorSpace]
+ -[_NUContainerMedia contentHeadroom]
+ -[_NUContainerMedia isContainer]
+ -[_NUContainerPipeline initWithName:opaque:]
+ -[_NUCropPipeline initWithName:opaque:]
+ -[_NUEDRHeadroomUpdatePipeline initWithName:opaque:]
+ -[_NUGroupPipeline initWithName:opaque:]
+ -[_NUHDRColorVolumePipeline initWithName:opaque:]
+ -[_NUHDRGainMapApplyPipeline initWithName:opaque:]
+ -[_NUHDRGainMapComputePipeline initWithName:opaque:]
+ -[_NUHDRToneMapApplyPipeline initWithName:opaque:]
+ -[_NUHDRToneMapLearnPipeline initWithName:opaque:]
+ -[_NUHDRToneMapPipeline initWithName:opaque:]
+ -[_NUKeyFramePipeline initWithName:opaque:]
+ -[_NULivePhotoExportResult .cxx_destruct]
+ -[_NULivePhotoExportResult destinationURL]
+ -[_NULivePhotoExportResult pairingIdentifier]
+ -[_NULivePhotoExportResult setDestinationURL:]
+ -[_NULivePhotoExportResult setPairingIdentifier:]
+ -[_NULivePhotoExportResult setVideoComplementURL:]
+ -[_NULivePhotoExportResult videoComplementURL]
+ -[_NUMapPipeline initWithName:opaque:]
+ -[_NUMedia colorSpace]
+ -[_NUMedia isContainer]
+ -[_NUOrientationPipeline initWithName:opaque:]
+ -[_NUPipeline _clearInputPort:error:]
+ -[_NUPipeline clearInputChannel:error:]
+ -[_NUPipeline initWithName:opaque:]
+ -[_NUPipeline shouldShowContents]
+ -[_NUPipeline updateInputChannels:error:]
+ -[_NUPipeline updateOutputChannels:error:]
+ -[_NUPlaybackRatePipeline initWithName:opaque:]
+ -[_NUProcessorPipeline initWithName:opaque:]
+ -[_NURawAssetPipeline initWithAsset:name:]
+ -[_NURawAssetPipeline initWithAsset:version:name:]
+ -[_NUReducePipeline initWithName:opaque:]
+ -[_NURenderNodePipeline initWithName:opaque:]
+ -[_NURenderNodePipeline initWithRenderNodeClass:baseSettings:name:]
+ -[_NUSelectorPipeline initWithName:opaque:]
+ -[_NUStraightenPipeline initWithName:opaque:]
+ -[_NUSwitchPipeline initWithName:opaque:]
+ -[_NUTagPipeline initWithName:opaque:]
+ -[_NUTrimPipeline initWithName:opaque:]
+ GCC_except_table10001
+ GCC_except_table10025
+ GCC_except_table10026
+ GCC_except_table10030
+ GCC_except_table10031
+ GCC_except_table10032
+ GCC_except_table10033
+ GCC_except_table10040
+ GCC_except_table10041
+ GCC_except_table10050
+ GCC_except_table10060
+ GCC_except_table10066
+ GCC_except_table10067
+ GCC_except_table10068
+ GCC_except_table10070
+ GCC_except_table10072
+ GCC_except_table10075
+ GCC_except_table10076
+ GCC_except_table10077
+ GCC_except_table10149
+ GCC_except_table10159
+ GCC_except_table10374
+ GCC_except_table10375
+ GCC_except_table10381
+ GCC_except_table10382
+ GCC_except_table10384
+ GCC_except_table10385
+ GCC_except_table10482
+ GCC_except_table10483
+ GCC_except_table10490
+ GCC_except_table10499
+ GCC_except_table10500
+ GCC_except_table10501
+ GCC_except_table10514
+ GCC_except_table10515
+ GCC_except_table10520
+ GCC_except_table10521
+ GCC_except_table10522
+ GCC_except_table10523
+ GCC_except_table10525
+ GCC_except_table10526
+ GCC_except_table10527
+ GCC_except_table10528
+ GCC_except_table10530
+ GCC_except_table10531
+ GCC_except_table10532
+ GCC_except_table10533
+ GCC_except_table10534
+ GCC_except_table10535
+ GCC_except_table10538
+ GCC_except_table10541
+ GCC_except_table10542
+ GCC_except_table10545
+ GCC_except_table10548
+ GCC_except_table10549
+ GCC_except_table10557
+ GCC_except_table10558
+ GCC_except_table10559
+ GCC_except_table10560
+ GCC_except_table10561
+ GCC_except_table10562
+ GCC_except_table10564
+ GCC_except_table10567
+ GCC_except_table10568
+ GCC_except_table10573
+ GCC_except_table10574
+ GCC_except_table10575
+ GCC_except_table10576
+ GCC_except_table10577
+ GCC_except_table10579
+ GCC_except_table10580
+ GCC_except_table10581
+ GCC_except_table10582
+ GCC_except_table10583
+ GCC_except_table10584
+ GCC_except_table10585
+ GCC_except_table10586
+ GCC_except_table10591
+ GCC_except_table10592
+ GCC_except_table10593
+ GCC_except_table10594
+ GCC_except_table10595
+ GCC_except_table10596
+ GCC_except_table10654
+ GCC_except_table10705
+ GCC_except_table10794
+ GCC_except_table10798
+ GCC_except_table1112
+ GCC_except_table11296
+ GCC_except_table11457
+ GCC_except_table11459
+ GCC_except_table11505
+ GCC_except_table11559
+ GCC_except_table11567
+ GCC_except_table11574
+ GCC_except_table11575
+ GCC_except_table11579
+ GCC_except_table1307
+ GCC_except_table1320
+ GCC_except_table1321
+ GCC_except_table1324
+ GCC_except_table1325
+ GCC_except_table1328
+ GCC_except_table1358
+ GCC_except_table1383
+ GCC_except_table1387
+ GCC_except_table1389
+ GCC_except_table1390
+ GCC_except_table1391
+ GCC_except_table1401
+ GCC_except_table1449
+ GCC_except_table1451
+ GCC_except_table1670
+ GCC_except_table1696
+ GCC_except_table1731
+ GCC_except_table1736
+ GCC_except_table1826
+ GCC_except_table1829
+ GCC_except_table1838
+ GCC_except_table1863
+ GCC_except_table1955
+ GCC_except_table2081
+ GCC_except_table2082
+ GCC_except_table2083
+ GCC_except_table2084
+ GCC_except_table2085
+ GCC_except_table2087
+ GCC_except_table2112
+ GCC_except_table2166
+ GCC_except_table2275
+ GCC_except_table2276
+ GCC_except_table2814
+ GCC_except_table2880
+ GCC_except_table2930
+ GCC_except_table2942
+ GCC_except_table3102
+ GCC_except_table3249
+ GCC_except_table3329
+ GCC_except_table3336
+ GCC_except_table3337
+ GCC_except_table3340
+ GCC_except_table3349
+ GCC_except_table3352
+ GCC_except_table3353
+ GCC_except_table3357
+ GCC_except_table3360
+ GCC_except_table3363
+ GCC_except_table3364
+ GCC_except_table3365
+ GCC_except_table3366
+ GCC_except_table3375
+ GCC_except_table3380
+ GCC_except_table3381
+ GCC_except_table3386
+ GCC_except_table3393
+ GCC_except_table3409
+ GCC_except_table3416
+ GCC_except_table3421
+ GCC_except_table3429
+ GCC_except_table3433
+ GCC_except_table3434
+ GCC_except_table3437
+ GCC_except_table3439
+ GCC_except_table3441
+ GCC_except_table3442
+ GCC_except_table3443
+ GCC_except_table3444
+ GCC_except_table3445
+ GCC_except_table3449
+ GCC_except_table3455
+ GCC_except_table346
+ GCC_except_table356
+ GCC_except_table373
+ GCC_except_table3808
+ GCC_except_table3995
+ GCC_except_table4064
+ GCC_except_table4068
+ GCC_except_table4070
+ GCC_except_table418
+ GCC_except_table4217
+ GCC_except_table4218
+ GCC_except_table4225
+ GCC_except_table4233
+ GCC_except_table4238
+ GCC_except_table4261
+ GCC_except_table4268
+ GCC_except_table4273
+ GCC_except_table4275
+ GCC_except_table4402
+ GCC_except_table4403
+ GCC_except_table4404
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4409
+ GCC_except_table4414
+ GCC_except_table4421
+ GCC_except_table4422
+ GCC_except_table4423
+ GCC_except_table4425
+ GCC_except_table4427
+ GCC_except_table4442
+ GCC_except_table4444
+ GCC_except_table446
+ GCC_except_table4469
+ GCC_except_table4505
+ GCC_except_table4506
+ GCC_except_table4509
+ GCC_except_table4510
+ GCC_except_table452
+ GCC_except_table4520
+ GCC_except_table4521
+ GCC_except_table4522
+ GCC_except_table4523
+ GCC_except_table4524
+ GCC_except_table4525
+ GCC_except_table4527
+ GCC_except_table4533
+ GCC_except_table4537
+ GCC_except_table4541
+ GCC_except_table4542
+ GCC_except_table4543
+ GCC_except_table4545
+ GCC_except_table4552
+ GCC_except_table4554
+ GCC_except_table4555
+ GCC_except_table4630
+ GCC_except_table4947
+ GCC_except_table503
+ GCC_except_table5062
+ GCC_except_table5068
+ GCC_except_table5071
+ GCC_except_table5081
+ GCC_except_table5085
+ GCC_except_table5086
+ GCC_except_table5100
+ GCC_except_table5210
+ GCC_except_table5316
+ GCC_except_table5318
+ GCC_except_table5320
+ GCC_except_table5359
+ GCC_except_table5441
+ GCC_except_table5733
+ GCC_except_table5836
+ GCC_except_table5861
+ GCC_except_table5897
+ GCC_except_table5899
+ GCC_except_table590
+ GCC_except_table5901
+ GCC_except_table5906
+ GCC_except_table5916
+ GCC_except_table5920
+ GCC_except_table5956
+ GCC_except_table5975
+ GCC_except_table5996
+ GCC_except_table6020
+ GCC_except_table6023
+ GCC_except_table6062
+ GCC_except_table6063
+ GCC_except_table6069
+ GCC_except_table6071
+ GCC_except_table6077
+ GCC_except_table6078
+ GCC_except_table6079
+ GCC_except_table6080
+ GCC_except_table6081
+ GCC_except_table6082
+ GCC_except_table6083
+ GCC_except_table6084
+ GCC_except_table6085
+ GCC_except_table6086
+ GCC_except_table6087
+ GCC_except_table6092
+ GCC_except_table6093
+ GCC_except_table6099
+ GCC_except_table6100
+ GCC_except_table6105
+ GCC_except_table6106
+ GCC_except_table6107
+ GCC_except_table6109
+ GCC_except_table6110
+ GCC_except_table6111
+ GCC_except_table6112
+ GCC_except_table6113
+ GCC_except_table6118
+ GCC_except_table6119
+ GCC_except_table6120
+ GCC_except_table6121
+ GCC_except_table6123
+ GCC_except_table6124
+ GCC_except_table6128
+ GCC_except_table6129
+ GCC_except_table6130
+ GCC_except_table6131
+ GCC_except_table6132
+ GCC_except_table6133
+ GCC_except_table6134
+ GCC_except_table6135
+ GCC_except_table6137
+ GCC_except_table6139
+ GCC_except_table6142
+ GCC_except_table6143
+ GCC_except_table6144
+ GCC_except_table6145
+ GCC_except_table6146
+ GCC_except_table6148
+ GCC_except_table6150
+ GCC_except_table6151
+ GCC_except_table6153
+ GCC_except_table6154
+ GCC_except_table617
+ GCC_except_table6262
+ GCC_except_table6266
+ GCC_except_table6326
+ GCC_except_table6358
+ GCC_except_table6359
+ GCC_except_table6397
+ GCC_except_table6403
+ GCC_except_table641
+ GCC_except_table6411
+ GCC_except_table6436
+ GCC_except_table651
+ GCC_except_table6516
+ GCC_except_table6528
+ GCC_except_table6533
+ GCC_except_table6540
+ GCC_except_table6558
+ GCC_except_table6576
+ GCC_except_table6579
+ GCC_except_table6580
+ GCC_except_table6584
+ GCC_except_table6585
+ GCC_except_table6689
+ GCC_except_table6698
+ GCC_except_table6718
+ GCC_except_table6735
+ GCC_except_table6809
+ GCC_except_table6875
+ GCC_except_table6880
+ GCC_except_table6883
+ GCC_except_table6906
+ GCC_except_table6950
+ GCC_except_table7093
+ GCC_except_table7168
+ GCC_except_table7183
+ GCC_except_table7184
+ GCC_except_table7185
+ GCC_except_table7198
+ GCC_except_table7199
+ GCC_except_table7200
+ GCC_except_table7201
+ GCC_except_table7216
+ GCC_except_table7217
+ GCC_except_table7231
+ GCC_except_table7232
+ GCC_except_table7237
+ GCC_except_table7350
+ GCC_except_table7351
+ GCC_except_table7355
+ GCC_except_table7357
+ GCC_except_table7361
+ GCC_except_table7363
+ GCC_except_table7365
+ GCC_except_table7366
+ GCC_except_table7370
+ GCC_except_table7374
+ GCC_except_table7375
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7380
+ GCC_except_table7382
+ GCC_except_table7383
+ GCC_except_table7385
+ GCC_except_table7386
+ GCC_except_table7456
+ GCC_except_table7493
+ GCC_except_table7532
+ GCC_except_table7533
+ GCC_except_table7583
+ GCC_except_table8276
+ GCC_except_table8279
+ GCC_except_table8349
+ GCC_except_table8488
+ GCC_except_table8492
+ GCC_except_table8497
+ GCC_except_table8500
+ GCC_except_table8502
+ GCC_except_table8507
+ GCC_except_table8521
+ GCC_except_table8523
+ GCC_except_table8524
+ GCC_except_table8529
+ GCC_except_table8530
+ GCC_except_table8550
+ GCC_except_table8557
+ GCC_except_table8558
+ GCC_except_table8559
+ GCC_except_table8560
+ GCC_except_table8573
+ GCC_except_table8761
+ GCC_except_table8808
+ GCC_except_table9153
+ GCC_except_table9238
+ GCC_except_table9416
+ GCC_except_table9610
+ GCC_except_table9625
+ GCC_except_table9662
+ GCC_except_table9724
+ GCC_except_table9731
+ GCC_except_table9734
+ GCC_except_table9741
+ GCC_except_table9743
+ GCC_except_table9744
+ GCC_except_table9746
+ GCC_except_table9747
+ GCC_except_table9748
+ GCC_except_table9749
+ GCC_except_table9754
+ GCC_except_table9756
+ GCC_except_table9757
+ GCC_except_table9758
+ GCC_except_table9759
+ GCC_except_table9763
+ GCC_except_table9764
+ GCC_except_table9766
+ GCC_except_table9768
+ GCC_except_table9770
+ GCC_except_table9772
+ GCC_except_table9778
+ GCC_except_table9781
+ GCC_except_table9785
+ GCC_except_table9786
+ GCC_except_table9788
+ GCC_except_table9789
+ GCC_except_table9790
+ GCC_except_table9791
+ GCC_except_table9792
+ GCC_except_table9794
+ GCC_except_table9795
+ GCC_except_table9796
+ GCC_except_table9797
+ GCC_except_table9798
+ GCC_except_table9799
+ GCC_except_table9800
+ GCC_except_table9801
+ GCC_except_table9802
+ GCC_except_table9803
+ GCC_except_table9804
+ GCC_except_table9805
+ GCC_except_table9806
+ GCC_except_table9807
+ GCC_except_table9808
+ GCC_except_table9809
+ GCC_except_table9810
+ GCC_except_table9811
+ GCC_except_table9868
+ GCC_except_table9875
+ OBJC_IVAR_$_NUAssetCapability._name
+ OBJC_IVAR_$_NUAuxiliaryImageRenderRequest._targetPixelFormat
+ OBJC_IVAR_$_NUGainMapExportOptions._flexRangeProperties
+ OBJC_IVAR_$_NUGainMapExportOptions._forceGainMapGeneration
+ OBJC_IVAR_$_NUGainMapExportOptions._pixelFormat
+ OBJC_IVAR_$_NUGainMapExportOptions._scale
+ OBJC_IVAR_$_NUImageExportJob._auxErrors
+ OBJC_IVAR_$_NUImageExportJob._auxiliaryImageOptions
+ OBJC_IVAR_$_NUImageExportRequest._auxiliaryImageOptions
+ OBJC_IVAR_$_NUImageExportRequest._gainMapExportOptions
+ OBJC_IVAR_$_NULivePhotoExportFormat._imageFormat
+ OBJC_IVAR_$_NULivePhotoExportFormat._videoCodecType
+ OBJC_IVAR_$_NULivePhotoExportJob._dependentResponseQueue
+ OBJC_IVAR_$_NULivePhotoExportJob._imageResponse
+ OBJC_IVAR_$_NULivePhotoExportJob._videoResponse
+ OBJC_IVAR_$_NULivePhotoExportRequest._applyImageOrientationAsMetadata
+ OBJC_IVAR_$_NULivePhotoExportRequest._applyVideoOrientationAsMetadata
+ OBJC_IVAR_$_NULivePhotoExportRequest._auxiliaryImageOptions
+ OBJC_IVAR_$_NULivePhotoExportRequest._format
+ OBJC_IVAR_$_NULivePhotoExportRequest._gainMapExportOptions
+ OBJC_IVAR_$_NULivePhotoExportRequest._imageColorSpace
+ OBJC_IVAR_$_NULivePhotoExportRequest._imageProperties
+ OBJC_IVAR_$_NULivePhotoExportRequest._pairingIdentifier
+ OBJC_IVAR_$_NULivePhotoExportRequest._targetHeadroom
+ OBJC_IVAR_$_NULivePhotoExportRequest._videoColorSpace
+ OBJC_IVAR_$_NULivePhotoExportRequest._videoComplementURL
+ OBJC_IVAR_$_NUVideoExportRequest._audioMode
+ OBJC_IVAR_$_NUVideoExportRequest._audioOutputSettings
+ OBJC_IVAR_$__NUHDRGainMapComputePipeline._compatibleWithMeteorPlus
+ OBJC_IVAR_$__NUHDRGainMapComputePipeline._gainMapScale
+ OBJC_IVAR_$__NUHDRGainMapComputePipeline._useMeteorPlus
+ OBJC_IVAR_$__NULivePhotoExportResult._destinationURL
+ OBJC_IVAR_$__NULivePhotoExportResult._pairingIdentifier
+ OBJC_IVAR_$__NULivePhotoExportResult._videoComplementURL
+ OBJC_IVAR_$__NUPipeline._isOpaque
+ _AVAppleMakerNote_AssetIdentifier
+ _AVMetadataIdentifierQuickTimeMetadataContentIdentifier
+ _NUAuxiliaryImageExportOptionAuxiliaryType
+ _NUAuxiliaryImageExportOptionChannelName
+ _NUAuxiliaryImageExportOptionPixelFormat
+ _NUAuxiliaryImageExportOptionRequired
+ _NUChannelNameAlternate
+ _NUGainMapComputePipelineOptionMeteorPlusCompatible
+ _NUGainMapComputePipelineOptionScale
+ _NUGainMapComputePipelineOptionUseMeteorPlus
+ _OBJC_CLASS_$_AVMutableMetadataItem
+ _OBJC_CLASS_$_NUAssetCapability
+ _OBJC_CLASS_$_NUGainMapExportOptions
+ _OBJC_CLASS_$_NULivePhotoExportFormat
+ _OBJC_CLASS_$_NULivePhotoExportJob
+ _OBJC_CLASS_$_NULivePhotoExportRequest
+ _OBJC_CLASS_$__NULivePhotoExportResult
+ _OBJC_METACLASS_$_NUAssetCapability
+ _OBJC_METACLASS_$_NUGainMapExportOptions
+ _OBJC_METACLASS_$_NULivePhotoExportFormat
+ _OBJC_METACLASS_$_NULivePhotoExportJob
+ _OBJC_METACLASS_$_NULivePhotoExportRequest
+ _OBJC_METACLASS_$__NULivePhotoExportResult
+ _OUTLINED_FUNCTION_28
+ __51-[NULivePhotoExportJob evaluateRenderDependencies:]_block_invoke
+ __OBJC_$_CLASS_METHODS_NUAssetCapability
+ __OBJC_$_CLASS_METHODS_NULivePhotoExportFormat
+ __OBJC_$_CLASS_PROP_LIST_NUAssetCapability
+ __OBJC_$_INSTANCE_METHODS_NSNull(NUDigest|NUControlDataRepresentable)
+ __OBJC_$_INSTANCE_METHODS_NUAssetCapability
+ __OBJC_$_INSTANCE_METHODS_NUGainMapExportOptions
+ __OBJC_$_INSTANCE_METHODS_NULivePhotoExportFormat
+ __OBJC_$_INSTANCE_METHODS_NULivePhotoExportJob
+ __OBJC_$_INSTANCE_METHODS_NULivePhotoExportRequest
+ __OBJC_$_INSTANCE_METHODS_NURenderJob(Media|RendererSupport|DebugAdditions)
+ __OBJC_$_INSTANCE_METHODS__NULivePhotoExportResult
+ __OBJC_$_INSTANCE_VARIABLES_NUAssetCapability
+ __OBJC_$_INSTANCE_VARIABLES_NUGainMapExportOptions
+ __OBJC_$_INSTANCE_VARIABLES_NULivePhotoExportFormat
+ __OBJC_$_INSTANCE_VARIABLES_NULivePhotoExportJob
+ __OBJC_$_INSTANCE_VARIABLES_NULivePhotoExportRequest
+ __OBJC_$_INSTANCE_VARIABLES__NULivePhotoExportResult
+ __OBJC_$_PROP_LIST_NUAssetCapability
+ __OBJC_$_PROP_LIST_NUGainMapExportOptions
+ __OBJC_$_PROP_LIST_NULivePhotoExportFormat
+ __OBJC_$_PROP_LIST_NULivePhotoExportJob
+ __OBJC_$_PROP_LIST_NULivePhotoExportRequest
+ __OBJC_$_PROP_LIST_NULivePhotoExportResult
+ __OBJC_$_PROP_LIST__NULivePhotoExportResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NULivePhotoExportResult
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NULivePhotoExportResult
+ __OBJC_$_PROTOCOL_REFS_NULivePhotoExportResult
+ __OBJC_CLASS_PROTOCOLS_$_NUGainMapExportOptions
+ __OBJC_CLASS_PROTOCOLS_$_NULivePhotoExportFormat
+ __OBJC_CLASS_PROTOCOLS_$_NULivePhotoExportRequest
+ __OBJC_CLASS_PROTOCOLS_$__NULivePhotoExportResult
+ __OBJC_CLASS_RO_$_NUAssetCapability
+ __OBJC_CLASS_RO_$_NUGainMapExportOptions
+ __OBJC_CLASS_RO_$_NULivePhotoExportFormat
+ __OBJC_CLASS_RO_$_NULivePhotoExportJob
+ __OBJC_CLASS_RO_$_NULivePhotoExportRequest
+ __OBJC_CLASS_RO_$__NULivePhotoExportResult
+ __OBJC_LABEL_PROTOCOL_$_NULivePhotoExportResult
+ __OBJC_METACLASS_RO_$_NUAssetCapability
+ __OBJC_METACLASS_RO_$_NUGainMapExportOptions
+ __OBJC_METACLASS_RO_$_NULivePhotoExportFormat
+ __OBJC_METACLASS_RO_$_NULivePhotoExportJob
+ __OBJC_METACLASS_RO_$_NULivePhotoExportRequest
+ __OBJC_METACLASS_RO_$__NULivePhotoExportResult
+ __OBJC_PROTOCOL_$_NULivePhotoExportResult
+ ___29-[NUImageExportJob auxErrors]_block_invoke
+ ___41-[_NUPipeline updateInputChannels:error:]_block_invoke
+ ___42-[_NUPipeline updateOutputChannels:error:]_block_invoke
+ ___51-[NULivePhotoExportJob evaluateRenderDependencies:]_block_invoke
+ ___block_descriptor_40_e8_32s_e26_B32?0"NUChannel"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e20_v16?0"NUResponse"8l
+ _kCGImagePropertyColorModel
+ _kCGImagePropertyProfileName
+ _objc_msgSend$HDR
+ _objc_msgSend$_captureImageResponse:
+ _objc_msgSend$_captureVideoResponse:
+ _objc_msgSend$_clearInputPort:error:
+ _objc_msgSend$_defaultGainMapExportOptions:
+ _objc_msgSend$_evaluateCapability:
+ _objc_msgSend$_renderContextWithName:
+ _objc_msgSend$_requestedAuxiliaryOptions
+ _objc_msgSend$alternateMediaForMedia:targetHeadroom:error:
+ _objc_msgSend$applyImageOrientationAsMetadata
+ _objc_msgSend$applyVideoOrientationAsMetadata
+ _objc_msgSend$audio
+ _objc_msgSend$audioMode
+ _objc_msgSend$audioOutputSettings
+ _objc_msgSend$auxErrors
+ _objc_msgSend$auxiliaryImageOptions
+ _objc_msgSend$clearData
+ _objc_msgSend$containerMediaForMedia:
+ _objc_msgSend$dataForCapability:
+ _objc_msgSend$defaultPipelineNameFromTypeName:
+ _objc_msgSend$evaluateForAsset:
+ _objc_msgSend$evaluateOutputChannel:error:
+ _objc_msgSend$forceGainMapGeneration
+ _objc_msgSend$gainMapApplyPipeline
+ _objc_msgSend$gainMapComputePipelineWithOptions:
+ _objc_msgSend$gainMapExportOptions
+ _objc_msgSend$gainMapMediaFromBaseMedia:alternateMedia:scale:flexRangeProperties:error:
+ _objc_msgSend$hdrGainMap
+ _objc_msgSend$hdrMediaFromBaseMedia:gainMap:targetHeadroom:error:
+ _objc_msgSend$heic
+ _objc_msgSend$imageColorSpace
+ _objc_msgSend$imageFormat
+ _objc_msgSend$initWithAsset:name:
+ _objc_msgSend$initWithAsset:version:name:
+ _objc_msgSend$initWithImageFormat:videoCodecType:
+ _objc_msgSend$initWithLivePhotoExportRequest:
+ _objc_msgSend$initWithMedia:destinationURL:
+ _objc_msgSend$initWithMedia:exportFormat:
+ _objc_msgSend$initWithName:opaque:
+ _objc_msgSend$initWithRegion:scale:
+ _objc_msgSend$initWithRenderNodeClass:baseSettings:name:
+ _objc_msgSend$isContainer
+ _objc_msgSend$livePhotoRequest
+ _objc_msgSend$metadataItem
+ _objc_msgSend$mixMedia:alternate:targetHeadroom:error:
+ _objc_msgSend$nullDataWithOptionalFormat:
+ _objc_msgSend$pairingIdentifier
+ _objc_msgSend$pipelineIsOpaque
+ _objc_msgSend$pipelineName
+ _objc_msgSend$rawDecode
+ _objc_msgSend$rawDecode_v6
+ _objc_msgSend$rawDecode_v7
+ _objc_msgSend$rawDecode_v8
+ _objc_msgSend$rawDecode_v9
+ _objc_msgSend$removeInputNamed:
+ _objc_msgSend$removeOutputNamed:
+ _objc_msgSend$setApplyImageOrientationAsMetadata:
+ _objc_msgSend$setApplyVideoOrientationAsMetadata:
+ _objc_msgSend$setAuxiliaryImageOptions:
+ _objc_msgSend$setBypassOutputSettingsIfNoComposition:
+ _objc_msgSend$setForceGainMapGeneration:
+ _objc_msgSend$setGainMapExportOptions:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setImageColorSpace:
+ _objc_msgSend$setMinimumRenderInterval:
+ _objc_msgSend$setPairingIdentifier:
+ _objc_msgSend$setTargetPixelFormat:
+ _objc_msgSend$setVideoColorSpace:
+ _objc_msgSend$setVideoComplementURL:
+ _objc_msgSend$shouldShowContents
+ _objc_msgSend$toneMapHDRMedia:targetHeadroom:error:
+ _objc_msgSend$toneMapPipeline
+ _objc_msgSend$videoCodecType
+ _objc_msgSend$videoColorSpace
+ _objc_msgSend$videoComplementURL
+ _objc_msgSend$videoRequest
- +[_NUPipeline defaultPipelineNameWithIdentifier:]
- -[NUFixedRegionPolicy setScale:]
- -[NUImageExportJob auxiliaryImageTypes]
- -[NUStyleTransferPipeline initWithIdentifier:]
- -[_NUAssetPipeline initWithAsset:identifier:]
- -[_NUAssetPipeline initWithIdentifier:]
- -[_NUCachePipeline initWithIdentifier:]
- -[_NUConstantPipeline initWithIdentifier:]
- -[_NUContainerPipeline initWithIdentifier:]
- -[_NUCropPipeline initWithIdentifier:]
- -[_NUEDRHeadroomUpdatePipeline initWithIdentifier:]
- -[_NUGroupPipeline initWithIdentifier:]
- -[_NUHDRColorVolumePipeline initWithIdentifier:]
- -[_NUHDRGainMapApplyPipeline initWithIdentifier:]
- -[_NUHDRGainMapComputePipeline initWithIdentifier:]
- -[_NUHDRToneMapApplyPipeline initWithIdentifier:]
- -[_NUHDRToneMapLearnPipeline initWithIdentifier:]
- -[_NUHDRToneMapPipeline initWithIdentifier:]
- -[_NUKeyFramePipeline initWithIdentifier:]
- -[_NUMapPipeline initWithIdentifier:]
- -[_NUOrientationPipeline initWithIdentifier:]
- -[_NUPipeline identifier]
- -[_NUPipeline initWithIdentifier:]
- -[_NUPlaybackRatePipeline initWithIdentifier:]
- -[_NUPrimitivePipeline isOpaque]
- -[_NUProcessorPipeline initWithIdentifier:]
- -[_NURawAssetPipeline initWithAsset:identifier:]
- -[_NURawAssetPipeline initWithAsset:version:identifier:]
- -[_NUReducePipeline initWithIdentifier:]
- -[_NURenderNodePipeline initWithIdentifier:]
- -[_NURenderNodePipeline initWithRenderNodeClass:baseSettings:identifier:]
- -[_NUSelectorPipeline initWithIdentifier:]
- -[_NUStraightenPipeline initWithIdentifier:]
- -[_NUSwitchPipeline initWithIdentifier:]
- -[_NUTagPipeline initWithIdentifier:]
- -[_NUTrimPipeline initWithIdentifier:]
- GCC_except_table10061
- GCC_except_table10071
- GCC_except_table10286
- GCC_except_table10287
- GCC_except_table10293
- GCC_except_table10294
- GCC_except_table10296
- GCC_except_table10297
- GCC_except_table10394
- GCC_except_table10395
- GCC_except_table10398
- GCC_except_table10399
- GCC_except_table10400
- GCC_except_table10401
- GCC_except_table10402
- GCC_except_table10403
- GCC_except_table10405
- GCC_except_table10408
- GCC_except_table10409
- GCC_except_table10411
- GCC_except_table10412
- GCC_except_table10413
- GCC_except_table10415
- GCC_except_table10416
- GCC_except_table10426
- GCC_except_table10427
- GCC_except_table10432
- GCC_except_table10433
- GCC_except_table10434
- GCC_except_table10435
- GCC_except_table10437
- GCC_except_table10438
- GCC_except_table10439
- GCC_except_table10440
- GCC_except_table10442
- GCC_except_table10443
- GCC_except_table10444
- GCC_except_table10445
- GCC_except_table10446
- GCC_except_table10447
- GCC_except_table10450
- GCC_except_table10453
- GCC_except_table10454
- GCC_except_table10457
- GCC_except_table10460
- GCC_except_table10461
- GCC_except_table10469
- GCC_except_table10470
- GCC_except_table10471
- GCC_except_table10472
- GCC_except_table10473
- GCC_except_table10474
- GCC_except_table10476
- GCC_except_table10478
- GCC_except_table10479
- GCC_except_table10480
- GCC_except_table10485
- GCC_except_table10492
- GCC_except_table10494
- GCC_except_table10495
- GCC_except_table10498
- GCC_except_table10505
- GCC_except_table10506
- GCC_except_table10507
- GCC_except_table10508
- GCC_except_table10617
- GCC_except_table10706
- GCC_except_table10710
- GCC_except_table1103
- GCC_except_table11154
- GCC_except_table11315
- GCC_except_table11317
- GCC_except_table11363
- GCC_except_table11417
- GCC_except_table11425
- GCC_except_table11432
- GCC_except_table11433
- GCC_except_table11437
- GCC_except_table1298
- GCC_except_table1302
- GCC_except_table1310
- GCC_except_table1312
- GCC_except_table1315
- GCC_except_table1316
- GCC_except_table1340
- GCC_except_table1374
- GCC_except_table1378
- GCC_except_table1380
- GCC_except_table1381
- GCC_except_table1382
- GCC_except_table1392
- GCC_except_table1440
- GCC_except_table1442
- GCC_except_table1658
- GCC_except_table1672
- GCC_except_table1707
- GCC_except_table1724
- GCC_except_table1813
- GCC_except_table1816
- GCC_except_table1825
- GCC_except_table1847
- GCC_except_table1939
- GCC_except_table2065
- GCC_except_table2066
- GCC_except_table2067
- GCC_except_table2068
- GCC_except_table2069
- GCC_except_table2071
- GCC_except_table2096
- GCC_except_table2150
- GCC_except_table2259
- GCC_except_table2260
- GCC_except_table2797
- GCC_except_table2862
- GCC_except_table2912
- GCC_except_table2924
- GCC_except_table3083
- GCC_except_table3230
- GCC_except_table3310
- GCC_except_table3317
- GCC_except_table3318
- GCC_except_table3321
- GCC_except_table3322
- GCC_except_table3323
- GCC_except_table3326
- GCC_except_table3327
- GCC_except_table3330
- GCC_except_table3333
- GCC_except_table3334
- GCC_except_table3338
- GCC_except_table3343
- GCC_except_table3344
- GCC_except_table3347
- GCC_except_table3348
- GCC_except_table3356
- GCC_except_table3374
- GCC_except_table338
- GCC_except_table3390
- GCC_except_table3391
- GCC_except_table3396
- GCC_except_table3397
- GCC_except_table3399
- GCC_except_table3402
- GCC_except_table3403
- GCC_except_table3407
- GCC_except_table3411
- GCC_except_table3414
- GCC_except_table3420
- GCC_except_table3423
- GCC_except_table3424
- GCC_except_table3425
- GCC_except_table3436
- GCC_except_table348
- GCC_except_table365
- GCC_except_table3788
- GCC_except_table3969
- GCC_except_table4038
- GCC_except_table4042
- GCC_except_table4044
- GCC_except_table411
- GCC_except_table4181
- GCC_except_table4191
- GCC_except_table4192
- GCC_except_table4199
- GCC_except_table4212
- GCC_except_table4235
- GCC_except_table4242
- GCC_except_table4247
- GCC_except_table4249
- GCC_except_table4376
- GCC_except_table4377
- GCC_except_table4378
- GCC_except_table4381
- GCC_except_table4382
- GCC_except_table4383
- GCC_except_table4388
- GCC_except_table439
- GCC_except_table4390
- GCC_except_table4395
- GCC_except_table4396
- GCC_except_table4397
- GCC_except_table4399
- GCC_except_table4401
- GCC_except_table4418
- GCC_except_table4443
- GCC_except_table445
- GCC_except_table4479
- GCC_except_table4480
- GCC_except_table4483
- GCC_except_table4484
- GCC_except_table4489
- GCC_except_table4490
- GCC_except_table4493
- GCC_except_table4494
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4497
- GCC_except_table4498
- GCC_except_table4499
- GCC_except_table4501
- GCC_except_table4507
- GCC_except_table4511
- GCC_except_table4517
- GCC_except_table4526
- GCC_except_table4528
- GCC_except_table4529
- GCC_except_table4604
- GCC_except_table4906
- GCC_except_table496
- GCC_except_table5017
- GCC_except_table5023
- GCC_except_table5026
- GCC_except_table5036
- GCC_except_table5040
- GCC_except_table5041
- GCC_except_table5055
- GCC_except_table5165
- GCC_except_table5299
- GCC_except_table5381
- GCC_except_table5673
- GCC_except_table5776
- GCC_except_table5801
- GCC_except_table583
- GCC_except_table5837
- GCC_except_table5839
- GCC_except_table5841
- GCC_except_table5846
- GCC_except_table5855
- GCC_except_table5856
- GCC_except_table5860
- GCC_except_table5896
- GCC_except_table5936
- GCC_except_table5941
- GCC_except_table5960
- GCC_except_table5962
- GCC_except_table5963
- GCC_except_table5968
- GCC_except_table5969
- GCC_except_table5971
- GCC_except_table5972
- GCC_except_table5981
- GCC_except_table5984
- GCC_except_table5985
- GCC_except_table5986
- GCC_except_table5988
- GCC_except_table5991
- GCC_except_table5992
- GCC_except_table5993
- GCC_except_table5994
- GCC_except_table5995
- GCC_except_table5997
- GCC_except_table5998
- GCC_except_table5999
- GCC_except_table6000
- GCC_except_table6002
- GCC_except_table6003
- GCC_except_table6004
- GCC_except_table6005
- GCC_except_table6006
- GCC_except_table6007
- GCC_except_table6008
- GCC_except_table6009
- GCC_except_table6014
- GCC_except_table6015
- GCC_except_table6021
- GCC_except_table6027
- GCC_except_table6033
- GCC_except_table6034
- GCC_except_table6035
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table6042
- GCC_except_table6043
- GCC_except_table6045
- GCC_except_table6050
- GCC_except_table6051
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6054
- GCC_except_table6055
- GCC_except_table6056
- GCC_except_table6057
- GCC_except_table6061
- GCC_except_table6065
- GCC_except_table6067
- GCC_except_table6068
- GCC_except_table610
- GCC_except_table6184
- GCC_except_table6188
- GCC_except_table6248
- GCC_except_table6280
- GCC_except_table6281
- GCC_except_table6318
- GCC_except_table6324
- GCC_except_table6332
- GCC_except_table634
- GCC_except_table6353
- GCC_except_table6433
- GCC_except_table644
- GCC_except_table6445
- GCC_except_table6450
- GCC_except_table6457
- GCC_except_table6475
- GCC_except_table6493
- GCC_except_table6496
- GCC_except_table6497
- GCC_except_table6501
- GCC_except_table6502
- GCC_except_table6605
- GCC_except_table6614
- GCC_except_table6634
- GCC_except_table6651
- GCC_except_table6725
- GCC_except_table6791
- GCC_except_table6796
- GCC_except_table6799
- GCC_except_table6822
- GCC_except_table6866
- GCC_except_table7009
- GCC_except_table7084
- GCC_except_table7099
- GCC_except_table7100
- GCC_except_table7101
- GCC_except_table7114
- GCC_except_table7115
- GCC_except_table7116
- GCC_except_table7117
- GCC_except_table7132
- GCC_except_table7133
- GCC_except_table7147
- GCC_except_table7148
- GCC_except_table7153
- GCC_except_table7193
- GCC_except_table7266
- GCC_except_table7267
- GCC_except_table7271
- GCC_except_table7273
- GCC_except_table7279
- GCC_except_table7281
- GCC_except_table7282
- GCC_except_table7286
- GCC_except_table7290
- GCC_except_table7291
- GCC_except_table7294
- GCC_except_table7295
- GCC_except_table7296
- GCC_except_table7298
- GCC_except_table7299
- GCC_except_table7301
- GCC_except_table7302
- GCC_except_table7372
- GCC_except_table7409
- GCC_except_table7448
- GCC_except_table7449
- GCC_except_table7499
- GCC_except_table8192
- GCC_except_table8195
- GCC_except_table8263
- GCC_except_table8402
- GCC_except_table8406
- GCC_except_table8411
- GCC_except_table8414
- GCC_except_table8416
- GCC_except_table8421
- GCC_except_table8435
- GCC_except_table8437
- GCC_except_table8438
- GCC_except_table8443
- GCC_except_table8444
- GCC_except_table8464
- GCC_except_table8471
- GCC_except_table8472
- GCC_except_table8473
- GCC_except_table8474
- GCC_except_table8487
- GCC_except_table8675
- GCC_except_table8722
- GCC_except_table9065
- GCC_except_table9150
- GCC_except_table9328
- GCC_except_table9522
- GCC_except_table9537
- GCC_except_table9574
- GCC_except_table9581
- GCC_except_table9621
- GCC_except_table9622
- GCC_except_table9623
- GCC_except_table9624
- GCC_except_table9629
- GCC_except_table9635
- GCC_except_table9636
- GCC_except_table9643
- GCC_except_table9646
- GCC_except_table9653
- GCC_except_table9655
- GCC_except_table9656
- GCC_except_table9658
- GCC_except_table9659
- GCC_except_table9660
- GCC_except_table9661
- GCC_except_table9666
- GCC_except_table9668
- GCC_except_table9670
- GCC_except_table9671
- GCC_except_table9675
- GCC_except_table9676
- GCC_except_table9678
- GCC_except_table9680
- GCC_except_table9682
- GCC_except_table9684
- GCC_except_table9690
- GCC_except_table9693
- GCC_except_table9697
- GCC_except_table9698
- GCC_except_table9700
- GCC_except_table9701
- GCC_except_table9702
- GCC_except_table9703
- GCC_except_table9704
- GCC_except_table9706
- GCC_except_table9707
- GCC_except_table9708
- GCC_except_table9713
- GCC_except_table9714
- GCC_except_table9715
- GCC_except_table9716
- GCC_except_table9718
- GCC_except_table9719
- GCC_except_table9720
- GCC_except_table9721
- GCC_except_table9722
- GCC_except_table9780
- GCC_except_table9787
- GCC_except_table9865
- GCC_except_table9913
- GCC_except_table9937
- GCC_except_table9938
- GCC_except_table9942
- GCC_except_table9943
- GCC_except_table9944
- GCC_except_table9945
- GCC_except_table9952
- GCC_except_table9962
- GCC_except_table9972
- GCC_except_table9978
- GCC_except_table9979
- GCC_except_table9980
- GCC_except_table9982
- GCC_except_table9984
- GCC_except_table9987
- GCC_except_table9988
- GCC_except_table9989
- OBJC_IVAR_$__NUPipeline._identifier
- _NUAssetCapabilityAudio
- _NUAssetCapabilityHDR
- _NUAssetCapabilityHDRGainMap
- _NUAssetCapabilityRawDecode
- _NUAssetCapabilityRawDecode_v6
- _NUAssetCapabilityRawDecode_v7
- _NUAssetCapabilityRawDecode_v8
- _NUAssetCapabilityRawDecode_v9
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSNull_$_NUDigest
- __OBJC_$_INSTANCE_METHODS_NURenderJob(RendererSupport|DebugAdditions)
- __os_feature_enabled_impl
- _associated conformance So20NUMediaAttachmentKeyaSHSCSQ
- _associated conformance So20NUMediaAttachmentKeyas20_SwiftNewtypeWrapperSCSY
- _associated conformance So20NUMediaAttachmentKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _objc_msgSend$defaultPipelineNameWithIdentifier:
- _objc_msgSend$initWithAsset:identifier:
- _objc_msgSend$initWithAsset:version:identifier:
- _objc_msgSend$initWithRenderNodeClass:baseSettings:identifier:
- _swift_dynamicCastObjCProtocolUnconditional
- _symbolic _____ So20NUMediaAttachmentKeya
CStrings:
+ "%@.image"
+ "%@.video"
+ "((NUControlDescriptor *)format.dataModel).isOptional"
+ "+[NUChannelControlData nullDataWithOptionalFormat:]"
+ "-[NUAssetCapability initWithName:]"
+ "-[NUCompoundDescriptor validate:error:]"
+ "-[NUFixedRegionPolicy initWithRegion:scale:]"
+ "-[NULivePhotoExportFormat init]"
+ "-[NULivePhotoExportJob initWithExportRequest:]"
+ "-[NULivePhotoExportJob initWithRequest:]"
+ "-[NULivePhotoExportRequest initWithComposition:]"
+ "-[NULivePhotoExportRequest initWithComposition:destinationURL:]"
+ "-[NULivePhotoExportRequest initWithMedia:destinationURL:]"
+ "-[NULivePhotoExportRequest initWithMedia:destinationURL:videoComplementURL:]"
+ "-[NULivePhotoExportRequest initWithRequest:]"
+ "-[NUOpaqueDescriptor validate:error:]"
+ "-[NURenderJob(Media) alternateMediaForMedia:targetHeadroom:error:]"
+ "-[NURenderJob(Media) hdrMediaFromBaseMedia:gainMap:targetHeadroom:error:]"
+ "-[NURenderJob(Media) mixMedia:alternate:targetHeadroom:error:]"
+ "-[NURenderJob(Media) toneMapHDRMedia:targetHeadroom:error:]"
+ "-[NUStyleTransferPipeline initWithName:opaque:]"
+ "-[_NUAssetPipeline initWithAsset:name:]"
+ "-[_NUAssetPipeline initWithName:opaque:]"
+ "-[_NUCachePipeline initWithName:opaque:]"
+ "-[_NUConstantPipeline initWithName:opaque:]"
+ "-[_NUContainerPipeline initWithName:opaque:]"
+ "-[_NUCropPipeline initWithName:opaque:]"
+ "-[_NUEDRHeadroomUpdatePipeline initWithName:opaque:]"
+ "-[_NUGroupPipeline initWithName:opaque:]"
+ "-[_NUHDRColorVolumePipeline initWithName:opaque:]"
+ "-[_NUHDRGainMapApplyPipeline initWithName:opaque:]"
+ "-[_NUHDRGainMapComputePipeline initWithName:opaque:]"
+ "-[_NUHDRToneMapApplyPipeline initWithName:opaque:]"
+ "-[_NUHDRToneMapLearnPipeline initWithName:opaque:]"
+ "-[_NUHDRToneMapPipeline initWithName:opaque:]"
+ "-[_NUKeyFramePipeline initWithName:opaque:]"
+ "-[_NUMapPipeline initWithName:opaque:]"
+ "-[_NUMedia colorSpace]"
+ "-[_NUOrientationPipeline initWithName:opaque:]"
+ "-[_NUPipeline clearInputChannel:error:]"
+ "-[_NUPipeline initWithName:opaque:]"
+ "-[_NUPipeline updateInputChannels:error:]"
+ "-[_NUPipeline updateOutputChannels:error:]"
+ "-[_NUPlaybackRatePipeline initWithName:opaque:]"
+ "-[_NUProcessorPipeline initWithName:opaque:]"
+ "-[_NURawAssetPipeline initWithAsset:name:]"
+ "-[_NURawAssetPipeline initWithAsset:version:name:]"
+ "-[_NUReducePipeline initWithName:opaque:]"
+ "-[_NURenderNodePipeline initWithName:opaque:]"
+ "-[_NURenderNodePipeline initWithRenderNodeClass:baseSettings:name:]"
+ "-[_NUSelectorPipeline initWithName:opaque:]"
+ "-[_NUStraightenPipeline initWithName:opaque:]"
+ "-[_NUSwitchPipeline initWithName:opaque:]"
+ "-[_NUTagPipeline initWithName:opaque:]"
+ "-[_NUTrimPipeline initWithName:opaque:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/Core/LivePhoto/NULivePhotoExportJob.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/Core/LivePhoto/NULivePhotoExportRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/Core/Render/NURenderJob+Media.m"
+ "Auxiliary image option missing ChannelName or AuxiliaryType"
+ "Failed to convert subkey"
+ "Failed to render auxiliary image"
+ "Gain-map generation requested but source has no HDR alternate; exporting without gain map"
+ "HDR colorspace (%{public}@) is incompatible with format (%{public}@)"
+ "Invalid colorSpace data: %@"
+ "Invalid compound value"
+ "LivePhotoExportJob: emitting dependents pairingIdentifier=%{public}@"
+ "Missing required auxiliary image"
+ "Missing value for key"
+ "NULivePhotoExportJob.dependents"
+ "NULivePhotoExportRequest requires a videoComplementURL for the current format"
+ "No spatial audio track"
+ "Not an image media"
+ "RGBGainMap"
+ "Warning: output track ID has changed (%i -> %i) for source track %@"
+ "XDR colorspace (%{public}@) is incompatible with format (%{public}@)"
+ "[format.dataModel isKindOfClass:NUControlDescriptor.class]"
+ "alternate != nil"
+ "auxiliaryType"
+ "channelName"
+ "failed to allocate pixel buffer"
+ "gainMapMedia != nil"
+ "hdrMedia != nil"
+ "headroom > 0.f"
+ "headroom >= 1.0f"
+ "meteorPlusCompatible"
+ "newChannels != nil"
+ "primary != nil"
+ "property"
+ "styleTransfer"
+ "targetHeadroom > 0.f"
+ "useMeteorPlus"
+ "videoComplementURL != nil"
- "-[NUFixedRegionPolicy initWithRegion:]"
- "-[NURenderJob(RendererSupport) renderImage:into:colorSpace:roi:alpha:error:]_block_invoke"
- "-[NUStyleTransferPipeline initWithIdentifier:]"
- "-[_NUAssetPipeline initWithAsset:identifier:]"
- "-[_NUAssetPipeline initWithIdentifier:]"
- "-[_NUCachePipeline initWithIdentifier:]"
- "-[_NUConstantPipeline initWithIdentifier:]"
- "-[_NUContainerPipeline initWithIdentifier:]"
- "-[_NUCropPipeline initWithIdentifier:]"
- "-[_NUEDRHeadroomUpdatePipeline initWithIdentifier:]"
- "-[_NUGroupPipeline initWithIdentifier:]"
- "-[_NUHDRColorVolumePipeline initWithIdentifier:]"
- "-[_NUHDRGainMapApplyPipeline initWithIdentifier:]"
- "-[_NUHDRGainMapComputePipeline initWithIdentifier:]"
- "-[_NUHDRToneMapApplyPipeline initWithIdentifier:]"
- "-[_NUHDRToneMapLearnPipeline initWithIdentifier:]"
- "-[_NUHDRToneMapPipeline initWithIdentifier:]"
- "-[_NUKeyFramePipeline initWithIdentifier:]"
- "-[_NUMapPipeline initWithIdentifier:]"
- "-[_NUOrientationPipeline initWithIdentifier:]"
- "-[_NUPipeline initWithIdentifier:]"
- "-[_NUPlaybackRatePipeline initWithIdentifier:]"
- "-[_NUProcessorPipeline initWithIdentifier:]"
- "-[_NURawAssetPipeline initWithAsset:identifier:]"
- "-[_NURawAssetPipeline initWithAsset:version:identifier:]"
- "-[_NUReducePipeline initWithIdentifier:]"
- "-[_NURenderNodePipeline initWithIdentifier:]"
- "-[_NURenderNodePipeline initWithRenderNodeClass:baseSettings:identifier:]"
- "-[_NUSelectorPipeline initWithIdentifier:]"
- "-[_NUStraightenPipeline initWithIdentifier:]"
- "-[_NUSwitchPipeline initWithIdentifier:]"
- "-[_NUTagPipeline initWithIdentifier:]"
- "-[_NUTrimPipeline initWithIdentifier:]"
- "HDR colorspace (%@) is incompatible with format (%@)"
- "Invalid object"
- "Photos"
- "PhotosPipeline"
- "RGB"
- "ResumableVideoExport"
- "StyleTransfer"
- "XDR colorspace (%@) is incompatible with format (%@)"
- "com.apple.neutrino"
- "failed to allocate buffer for depth"
- "object"
```
