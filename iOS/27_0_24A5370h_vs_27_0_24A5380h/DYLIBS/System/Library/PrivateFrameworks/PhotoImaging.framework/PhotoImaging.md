## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-  __TEXT.__text: 0x278560
+  __TEXT.__text: 0x27a448
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x163d0
+  __TEXT.__objc_methlist: 0x16410
   __TEXT.__const: 0x8a8c
   __TEXT.__dlopen_cstrs: 0x2a2
   __TEXT.__swift5_typeref: 0x2e9
-  __TEXT.__cstring: 0x46738
+  __TEXT.__cstring: 0x46c53
   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_reflstr: 0x35f
   __TEXT.__swift5_fieldmd: 0x3b8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__oslogstring: 0x6c3f
+  __TEXT.__oslogstring: 0x6bf0
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_capture: 0xf0
-  __TEXT.__gcc_except_tab: 0x4a18
-  __TEXT.__unwind_info: 0x5800
+  __TEXT.__gcc_except_tab: 0x4a64
+  __TEXT.__unwind_info: 0x5828
   __TEXT.__eh_frame: 0x9f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4050
+  __DATA_CONST.__const: 0x4030
   __DATA_CONST.__objc_classlist: 0x10d8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb478
+  __DATA_CONST.__objc_selrefs: 0xb4c0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x6f8
-  __DATA_CONST.__objc_arraydata: 0x9350
+  __DATA_CONST.__objc_superrefs: 0x700
+  __DATA_CONST.__objc_arraydata: 0x9330
   __DATA_CONST.__got: 0x2598
-  __AUTH_CONST.__const: 0x5450
-  __AUTH_CONST.__cfstring: 0x26a20
-  __AUTH_CONST.__objc_const: 0x28240
+  __AUTH_CONST.__const: 0x5470
+  __AUTH_CONST.__cfstring: 0x26c40
+  __AUTH_CONST.__objc_const: 0x282a0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x1458
-  __AUTH_CONST.__objc_dictobj: 0x5af0
-  __AUTH_CONST.__objc_doubleobj: 0xe00
+  __AUTH_CONST.__objc_intobj: 0x1488
+  __AUTH_CONST.__objc_dictobj: 0x5ac8
+  __AUTH_CONST.__objc_doubleobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x558
   __AUTH_CONST.__objc_floatobj: 0xd0
   __AUTH_CONST.__auth_got: 0x1530
-  __AUTH.__objc_data: 0x788
-  __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x1558
-  __DATA.__data: 0x16f0
+  __AUTH.__objc_data: 0x288
+  __DATA.__objc_ivar: 0x1560
+  __DATA.__data: 0x16fc
   __DATA.__bss: 0x1600
-  __DATA_DIRTY.__objc_data: 0xa2a0
-  __DATA_DIRTY.__data: 0x120
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__objc_data: 0xa7a0
+  __DATA_DIRTY.__data: 0x170
+  __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9098
-  Symbols:   30339
-  CStrings:  12003
+  Functions: 9113
+  Symbols:   30383
+  CStrings:  12045
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
Symbols:
+ +[PICinematicVideoUtilities cinematicCapabilityForAssetMetadata:hasDisparityTrack:naturalSize:]
+ +[PICinematicVideoUtilities globalRenderingMetadataFromAssetMetadata:error:]
+ +[PICompositionExporter effectiveScalePolicyForComposition:requestedScalePolicy:]
+ +[PICurves_v1 adjustmentDescriptor]
+ +[PISelectiveColor_v1 adjustmentDescriptor]
+ -[PIGANCleanupRequest additionalPipelineInputs:]
+ -[PIParallaxSegmentationItem hadValidSegmentationBeforeOutfill]
+ -[PIParallaxSegmentationItem setHadValidSegmentationBeforeOutfill:]
+ -[PIPrivatePhotosPipeline_v0 _replacePortraitPipeline:]
+ -[PIPrivatePhotosPipeline_v0 _rewirePortraitPipeline:]
+ -[PIPrivatePhotosPipeline_v1 _replacePortraitPipeline:]
+ -[PIPrivatePhotosPipeline_v1 _rewirePortraitPipeline:]
+ -[PISegmentationLoader hadValidSegmentationBeforeOutfill]
+ -[PISegmentationLoader setHadValidSegmentationBeforeOutfill:]
+ GCC_except_table1696
+ GCC_except_table1710
+ GCC_except_table1877
+ GCC_except_table2053
+ GCC_except_table2207
+ GCC_except_table2217
+ GCC_except_table2223
+ GCC_except_table2231
+ GCC_except_table2238
+ GCC_except_table2246
+ GCC_except_table2324
+ GCC_except_table2364
+ GCC_except_table2393
+ GCC_except_table2398
+ GCC_except_table2413
+ GCC_except_table2429
+ GCC_except_table2434
+ GCC_except_table2440
+ GCC_except_table2527
+ GCC_except_table2749
+ GCC_except_table3100
+ GCC_except_table3130
+ GCC_except_table3137
+ GCC_except_table3139
+ GCC_except_table3141
+ GCC_except_table3143
+ GCC_except_table3154
+ GCC_except_table3163
+ GCC_except_table3257
+ GCC_except_table3322
+ GCC_except_table3323
+ GCC_except_table3430
+ GCC_except_table3472
+ GCC_except_table3480
+ GCC_except_table3532
+ GCC_except_table3744
+ GCC_except_table3754
+ GCC_except_table3757
+ GCC_except_table3758
+ GCC_except_table3770
+ GCC_except_table3817
+ GCC_except_table3826
+ GCC_except_table3854
+ GCC_except_table3877
+ GCC_except_table4106
+ GCC_except_table4358
+ GCC_except_table4461
+ GCC_except_table4485
+ GCC_except_table4489
+ GCC_except_table4608
+ GCC_except_table4646
+ GCC_except_table4652
+ GCC_except_table4654
+ GCC_except_table4678
+ GCC_except_table4700
+ GCC_except_table4923
+ GCC_except_table4953
+ GCC_except_table4956
+ GCC_except_table4967
+ GCC_except_table4974
+ GCC_except_table5121
+ GCC_except_table5213
+ GCC_except_table5274
+ GCC_except_table5277
+ GCC_except_table5289
+ GCC_except_table5290
+ GCC_except_table5294
+ GCC_except_table5295
+ GCC_except_table5296
+ GCC_except_table5301
+ GCC_except_table5309
+ GCC_except_table5402
+ GCC_except_table5749
+ GCC_except_table5768
+ GCC_except_table5769
+ GCC_except_table5775
+ GCC_except_table5780
+ GCC_except_table5832
+ GCC_except_table5837
+ GCC_except_table5848
+ GCC_except_table5850
+ GCC_except_table5876
+ GCC_except_table5878
+ GCC_except_table5890
+ GCC_except_table5893
+ GCC_except_table5894
+ GCC_except_table5895
+ GCC_except_table5897
+ GCC_except_table5902
+ GCC_except_table5935
+ GCC_except_table6038
+ GCC_except_table6076
+ GCC_except_table6150
+ GCC_except_table6469
+ GCC_except_table6717
+ GCC_except_table6718
+ GCC_except_table6808
+ GCC_except_table6811
+ GCC_except_table6815
+ GCC_except_table6816
+ GCC_except_table6820
+ GCC_except_table6821
+ GCC_except_table6823
+ GCC_except_table6829
+ GCC_except_table6838
+ GCC_except_table6854
+ GCC_except_table6905
+ GCC_except_table6957
+ GCC_except_table6958
+ GCC_except_table6959
+ GCC_except_table6960
+ GCC_except_table6990
+ GCC_except_table6993
+ GCC_except_table7061
+ GCC_except_table7071
+ GCC_except_table7175
+ GCC_except_table7228
+ GCC_except_table7230
+ GCC_except_table7330
+ GCC_except_table7336
+ GCC_except_table7344
+ GCC_except_table7345
+ GCC_except_table7346
+ GCC_except_table7348
+ GCC_except_table7349
+ GCC_except_table7351
+ GCC_except_table7352
+ GCC_except_table7353
+ GCC_except_table7354
+ GCC_except_table7409
+ GCC_except_table7417
+ GCC_except_table7431
+ GCC_except_table7432
+ GCC_except_table7433
+ GCC_except_table7467
+ GCC_except_table7468
+ GCC_except_table7469
+ GCC_except_table7472
+ GCC_except_table7475
+ GCC_except_table7520
+ GCC_except_table7522
+ GCC_except_table7664
+ GCC_except_table7681
+ GCC_except_table7682
+ GCC_except_table7683
+ GCC_except_table7684
+ GCC_except_table7685
+ GCC_except_table7686
+ GCC_except_table7687
+ GCC_except_table7730
+ GCC_except_table7916
+ GCC_except_table8144
+ GCC_except_table8146
+ GCC_except_table8147
+ GCC_except_table8209
+ GCC_except_table8211
+ GCC_except_table8213
+ GCC_except_table8283
+ GCC_except_table8306
+ GCC_except_table8308
+ GCC_except_table8311
+ GCC_except_table8315
+ GCC_except_table8317
+ GCC_except_table8333
+ GCC_except_table8358
+ GCC_except_table8362
+ GCC_except_table8363
+ GCC_except_table8371
+ GCC_except_table8385
+ GCC_except_table8387
+ GCC_except_table8391
+ GCC_except_table8393
+ GCC_except_table8406
+ _OBJC_CLASS_$_NUOptionalDescriptor
+ _OBJC_IVAR_$_PIParallaxSegmentationItem._hadValidSegmentationBeforeOutfill
+ _OBJC_IVAR_$_PISegmentationLoader._hadValidSegmentationBeforeOutfill
+ _PIPortraitModuleOptionEnableDebugPortraitInfo
+ ___54-[PIPrivatePhotosPipeline_v0 _rewirePortraitPipeline:]_block_invoke
+ ___54-[PIPrivatePhotosPipeline_v1 _rewirePortraitPipeline:]_block_invoke
+ ___block_descriptor_50_e8_32s40s_e48_B32?0"<NUImageBuffer>"8"<NUImageBuffer>"16Q24ls32l8s40l8
+ _objc_msgSend$_replacePortraitPipeline:
+ _objc_msgSend$_rewirePortraitPipeline:
+ _objc_msgSend$applyCleanup:mask:exclusionMask:context:orientation:dilateMask:error:
+ _objc_msgSend$applyCleanupToGainMapImage:inputImage:inputMaskImage:exclusionMaskImage:cleanedUpImage:gainMapTileExtent:dilateMask:context:error:
+ _objc_msgSend$assetHasDisparityTrack:
+ _objc_msgSend$booleanWithDefault:
+ _objc_msgSend$cinematicCapabilityForAssetMetadata:hasDisparityTrack:naturalSize:
+ _objc_msgSend$effectiveFormat
+ _objc_msgSend$effectiveScalePolicyForComposition:requestedScalePolicy:
+ _objc_msgSend$globalRenderingMetadataFromAssetMetadata:error:
+ _objc_msgSend$hadValidSegmentationBeforeOutfill
+ _objc_msgSend$inputPortForChannel:
+ _objc_msgSend$isConnected
+ _objc_msgSend$naturalSize
+ _objc_msgSend$outputPortForChannel:
+ _objc_msgSend$removeSubpipelineWithName:
+ _objc_msgSend$rootPath
+ _objc_msgSend$setHadValidSegmentationBeforeOutfill:
+ _objc_msgSend$subpipelineAtPath:
+ _objc_msgSend$subpipelineWithName:
+ _objc_msgSend$tracksWithMediaType:forAsset:
- +[PICinematicVideoUtilities canRenderCinematicVideoWithAssetMetadata:]
- +[PICinematicVideoUtilities currentSystemRenderingVersion]
- +[PICinematicVideoUtilities hasCinematicVideoMetadata:]
- +[PICompositionExporter _effectiveScalePolicyForComposition:requestedScalePolicy:]
- +[PICurves_v1 adjustmentSchema]
- +[PISelectiveColor_v1 adjustmentSchema]
- -[PIPrivatePhotosPipeline_v0 _rewirePortraitPipeline:error:]
- -[PIPrivatePhotosPipeline_v1 _rewireLivePortraitPipeline:]
- GCC_except_table1694
- GCC_except_table1708
- GCC_except_table1875
- GCC_except_table2051
- GCC_except_table2203
- GCC_except_table2213
- GCC_except_table2219
- GCC_except_table2227
- GCC_except_table2234
- GCC_except_table2242
- GCC_except_table2320
- GCC_except_table2360
- GCC_except_table2389
- GCC_except_table2394
- GCC_except_table2409
- GCC_except_table2425
- GCC_except_table2430
- GCC_except_table2436
- GCC_except_table2522
- GCC_except_table2744
- GCC_except_table3090
- GCC_except_table3125
- GCC_except_table3129
- GCC_except_table3131
- GCC_except_table3132
- GCC_except_table3138
- GCC_except_table3144
- GCC_except_table3158
- GCC_except_table3251
- GCC_except_table3316
- GCC_except_table3317
- GCC_except_table3424
- GCC_except_table3466
- GCC_except_table3474
- GCC_except_table3526
- GCC_except_table3738
- GCC_except_table3748
- GCC_except_table3751
- GCC_except_table3752
- GCC_except_table3764
- GCC_except_table3811
- GCC_except_table3820
- GCC_except_table3848
- GCC_except_table3871
- GCC_except_table4098
- GCC_except_table4350
- GCC_except_table4451
- GCC_except_table4475
- GCC_except_table4479
- GCC_except_table4598
- GCC_except_table4636
- GCC_except_table4642
- GCC_except_table4644
- GCC_except_table4668
- GCC_except_table4690
- GCC_except_table4913
- GCC_except_table4936
- GCC_except_table4943
- GCC_except_table4957
- GCC_except_table4964
- GCC_except_table5111
- GCC_except_table5203
- GCC_except_table5264
- GCC_except_table5267
- GCC_except_table5279
- GCC_except_table5280
- GCC_except_table5284
- GCC_except_table5285
- GCC_except_table5286
- GCC_except_table5291
- GCC_except_table5299
- GCC_except_table5392
- GCC_except_table5739
- GCC_except_table5758
- GCC_except_table5759
- GCC_except_table5765
- GCC_except_table5770
- GCC_except_table5822
- GCC_except_table5827
- GCC_except_table5828
- GCC_except_table5840
- GCC_except_table5864
- GCC_except_table5866
- GCC_except_table5867
- GCC_except_table5868
- GCC_except_table5870
- GCC_except_table5872
- GCC_except_table5883
- GCC_except_table5885
- GCC_except_table5925
- GCC_except_table6028
- GCC_except_table6067
- GCC_except_table6141
- GCC_except_table6460
- GCC_except_table6708
- GCC_except_table6709
- GCC_except_table6797
- GCC_except_table6800
- GCC_except_table6804
- GCC_except_table6805
- GCC_except_table6809
- GCC_except_table6810
- GCC_except_table6812
- GCC_except_table6818
- GCC_except_table6827
- GCC_except_table6843
- GCC_except_table6894
- GCC_except_table6946
- GCC_except_table6947
- GCC_except_table6948
- GCC_except_table6949
- GCC_except_table6979
- GCC_except_table6982
- GCC_except_table7050
- GCC_except_table7060
- GCC_except_table7164
- GCC_except_table7217
- GCC_except_table7219
- GCC_except_table7313
- GCC_except_table7319
- GCC_except_table7322
- GCC_except_table7325
- GCC_except_table7326
- GCC_except_table7327
- GCC_except_table7329
- GCC_except_table7332
- GCC_except_table7334
- GCC_except_table7341
- GCC_except_table7342
- GCC_except_table7398
- GCC_except_table7406
- GCC_except_table7420
- GCC_except_table7421
- GCC_except_table7422
- GCC_except_table7456
- GCC_except_table7457
- GCC_except_table7458
- GCC_except_table7461
- GCC_except_table7464
- GCC_except_table7509
- GCC_except_table7511
- GCC_except_table7653
- GCC_except_table7663
- GCC_except_table7670
- GCC_except_table7671
- GCC_except_table7672
- GCC_except_table7673
- GCC_except_table7675
- GCC_except_table7676
- GCC_except_table7719
- GCC_except_table7904
- GCC_except_table8132
- GCC_except_table8134
- GCC_except_table8135
- GCC_except_table8197
- GCC_except_table8199
- GCC_except_table8201
- GCC_except_table8271
- GCC_except_table8294
- GCC_except_table8296
- GCC_except_table8299
- GCC_except_table8303
- GCC_except_table8305
- GCC_except_table8321
- GCC_except_table8338
- GCC_except_table8346
- GCC_except_table8351
- GCC_except_table8359
- GCC_except_table8369
- GCC_except_table8370
- GCC_except_table8373
- GCC_except_table8375
- GCC_except_table8379
- _OBJC_CLASS_$_NUArraySetting
- ___58-[PIPrivatePhotosPipeline_v1 _rewireLivePortraitPipeline:]_block_invoke
- ___60-[PIPrivatePhotosPipeline_v0 _rewirePortraitPipeline:error:]_block_invoke
- ___block_descriptor_32_e33_B24?0"<NUMutablePipeline>"8^16l
- ___block_descriptor_49_e8_32s40s_e48_B32?0"<NUImageBuffer>"8"<NUImageBuffer>"16Q24ls32l8s40l8
- _objc_msgSend$_effectiveScalePolicyForComposition:requestedScalePolicy:
- _objc_msgSend$_rewireLivePortraitPipeline:
- _objc_msgSend$_rewirePortraitPipeline:error:
- _objc_msgSend$applyCleanup:mask:exclusionMask:context:orientation:error:
- _objc_msgSend$applyCleanupToGainMapImage:inputImage:inputMaskImage:exclusionMaskImage:cleanedUpImage:gainMapTileExtent:context:error:
- _objc_msgSend$canRenderCinematicVideoWithAssetMetadata:
- _objc_msgSend$initWithContent:attributes:
- _objc_msgSend$latestVersion
- _objc_msgSend$reconnect:to:error:
- _objc_msgSend$renderingVersionFromAsset:error:
CStrings:
+ "-[PIADMCleanup buildPipeline:inputs:outputs:error:]_block_invoke"
+ "-[PIADMOutfill buildPipeline:inputs:outputs:error:]_block_invoke"
+ "-[PIGANCleanup buildPipeline:inputs:outputs:error:]_block_invoke"
+ "-[PIPrivatePhotosPipeline_v0 _replacePortraitPipeline:]"
+ "-[PIPrivatePhotosPipeline_v1 _replacePortraitPipeline:]"
+ "-[PIRetouchCleanup buildPipeline:inputs:outputs:error:]_block_invoke"
+ "..:<dilateMask"
+ "/:<cleanupGANDilateMask"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Generative/PIADMCleanup.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Generative/PIGANCleanup.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Generative/PIRetouchCleanup.m"
+ ":<dilateMask"
+ "AutoLoop recipe produced a non-numeric trim end time"
+ "AutoLoop recipe produced a non-numeric trim start time"
+ "Portrait should exist"
+ "cleanupGANDilateMask"
+ "cleanupGANProcessor:<dilateMask"
+ "dilateMask"
+ "enableDebugPortraitInfo"
+ "gainMapProcessor:<dilateMask"
+ "hadValidSegmentationBeforeOutfill"
+ "newPortrait"
+ "newPortrait:<gainMap"
+ "newPortrait:<primary"
+ "newPortrait:>gainMap"
+ "portraitBypass:<outputIfTrue"
+ "portraitGainMapBypass:<outputIfTrue"
+ "processor:<dilateMask"
- "/image/portraitSettings:>settings"
- "Failed to rewire portrait pipeline"
- "currentSystemCanRenderAsset: error retrieving rendering version from asset: %@"

```
