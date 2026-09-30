## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/Versions/A/PhotoImaging`

```diff

-910.34.101.0.0
-  __TEXT.__text: 0x2a2b7c
+911.0.134.0.0
+  __TEXT.__text: 0x2a4680
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x16470
-  __TEXT.__const: 0x8bf8
+  __TEXT.__objc_methlist: 0x16610
+  __TEXT.__const: 0x8be8
   __TEXT.__dlopen_cstrs: 0x2a2
-  __TEXT.__swift5_typeref: 0x2e9
-  __TEXT.__cstring: 0x48637
+  __TEXT.__swift5_typeref: 0x299
+  __TEXT.__cstring: 0x4894f
   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_reflstr: 0x35f
   __TEXT.__swift5_fieldmd: 0x3b8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__oslogstring: 0x6bc9
+  __TEXT.__oslogstring: 0x6b99
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__swift5_capture: 0xf0
-  __TEXT.__gcc_except_tab: 0x4bc8
-  __TEXT.__unwind_info: 0x5938
+  __TEXT.__swift5_capture: 0x50
+  __TEXT.__gcc_except_tab: 0x4cd0
+  __TEXT.__unwind_info: 0x5988
   __TEXT.__eh_frame: 0x9f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1388
-  __DATA_CONST.__objc_classlist: 0x10d8
+  __DATA_CONST.__const: 0x1390
+  __DATA_CONST.__objc_classlist: 0x10f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb4b8
+  __DATA_CONST.__objc_selrefs: 0xb580
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x708
-  __DATA_CONST.__objc_arraydata: 0x9340
-  __DATA_CONST.__got: 0x25a8
-  __AUTH_CONST.__const: 0x8c40
-  __AUTH_CONST.__cfstring: 0x26d00
-  __AUTH_CONST.__objc_const: 0x282b0
+  __DATA_CONST.__objc_superrefs: 0x718
+  __DATA_CONST.__objc_arraydata: 0x9350
+  __DATA_CONST.__got: 0x25c0
+  __AUTH_CONST.__const: 0x8b10
+  __AUTH_CONST.__cfstring: 0x26e80
+  __AUTH_CONST.__objc_const: 0x286f0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x14d0
-  __AUTH_CONST.__objc_dictobj: 0x5af0
+  __AUTH_CONST.__objc_dictobj: 0x5b18
   __AUTH_CONST.__objc_doubleobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x558
   __AUTH_CONST.__objc_floatobj: 0xd0
-  __AUTH_CONST.__auth_got: 0x13d8
-  __AUTH.__objc_data: 0x288
-  __DATA.__objc_ivar: 0x1560
-  __DATA.__data: 0x16ec
-  __DATA.__bss: 0x15e0
+  __AUTH_CONST.__auth_got: 0x13c8
+  __AUTH.__objc_data: 0x378
+  __DATA.__objc_ivar: 0x1594
+  __DATA.__data: 0x16e0
+  __DATA.__bss: 0x15f0
   __DATA_DIRTY.__objc_data: 0xa7a0
-  __DATA_DIRTY.__data: 0x16c
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__data: 0x174
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9238
-  Symbols:   20695
-  CStrings:  7089
+  Functions: 9254
+  Symbols:   20782
+  CStrings:  7105
 
Symbols:
+ +[PICinematicVideoUtilities loadCinematographyScriptWithVideoURLString:changesDictionary:error:]
+ +[PIModularPhotosPipeline clearPipelineCache]
+ +[PIPhotographicStyleCorruptionReport reportForImageProperties:]
+ +[PIPhotographicStyleCorruptionReport reportForVideoProperties:]
+ +[PISegmentationHelper layoutProxyScalePolicy]
+ +[PISegmentationLoader _baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:]
+ +[PISemanticStyleAdjustmentController defaultValuesForCast:smartStyleRenderingVersion:]
+ -[PIModularPhotosPipelineCache clearCache]
+ -[PIParallaxClockLayoutRequest displayContext]
+ -[PIParallaxClockLayoutRequest setDisplayContext:]
+ -[PIParallaxCompoundLayerStackRequest layoutConfiguration]
+ -[PIParallaxCompoundLayerStackRequest savedLayoutUsesHeadroom]
+ -[PIParallaxCompoundLayerStackRequest setLayoutConfiguration:]
+ -[PIParallaxCompoundLayerStackRequest setSavedLayoutUsesHeadroom:]
+ -[PIParallaxSegmentationItem gainMapMedia]
+ -[PIParallaxSegmentationItem sensitiveContentEvaluated]
+ -[PIParallaxSegmentationItem setGainMapMedia:]
+ -[PIParallaxSegmentationItem setSensitiveContentEvaluated:]
+ -[PIPhotographicStyleCorruption .cxx_destruct]
+ -[PIPhotographicStyleCorruption initWithKind:notes:]
+ -[PIPhotographicStyleCorruption kind]
+ -[PIPhotographicStyleCorruption notes]
+ -[PIPhotographicStyleCorruptionReport .cxx_destruct]
+ -[PIPhotographicStyleCorruptionReport corruptions]
+ -[PIPhotographicStyleCorruptionReport initWithPhotographicStyleV1Capable:photographicStyleV2Capable:mainVideoCorrupted:linearThumbnailCorrupted:skinMatteCorrupted:corruptions:]
+ -[PIPhotographicStyleCorruptionReport linearThumbnailCorrupted]
+ -[PIPhotographicStyleCorruptionReport mainVideoCorrupted]
+ -[PIPhotographicStyleCorruptionReport photographicStyleV1Capable]
+ -[PIPhotographicStyleCorruptionReport photographicStyleV2Capable]
+ -[PIPhotographicStyleCorruptionReport skinMatteCorrupted]
+ -[PISpatialReframeAutoCalculator pipelineOutput]
+ -[PISpatialReframeAutoCalculator processComputedData:error:]
+ GCC_except_table1122
+ GCC_except_table1726
+ GCC_except_table1740
+ GCC_except_table1908
+ GCC_except_table2086
+ GCC_except_table2240
+ GCC_except_table2251
+ GCC_except_table2257
+ GCC_except_table2267
+ GCC_except_table2274
+ GCC_except_table2284
+ GCC_except_table2364
+ GCC_except_table2404
+ GCC_except_table2433
+ GCC_except_table2440
+ GCC_except_table2455
+ GCC_except_table2473
+ GCC_except_table2478
+ GCC_except_table2574
+ GCC_except_table2796
+ GCC_except_table3153
+ GCC_except_table316
+ GCC_except_table3160
+ GCC_except_table3191
+ GCC_except_table3195
+ GCC_except_table3197
+ GCC_except_table3198
+ GCC_except_table3200
+ GCC_except_table3202
+ GCC_except_table3204
+ GCC_except_table3211
+ GCC_except_table3216
+ GCC_except_table3225
+ GCC_except_table3320
+ GCC_except_table3389
+ GCC_except_table3390
+ GCC_except_table3499
+ GCC_except_table3543
+ GCC_except_table3551
+ GCC_except_table3603
+ GCC_except_table3829
+ GCC_except_table3839
+ GCC_except_table3842
+ GCC_except_table3843
+ GCC_except_table3855
+ GCC_except_table3902
+ GCC_except_table3911
+ GCC_except_table3939
+ GCC_except_table396
+ GCC_except_table3964
+ GCC_except_table4195
+ GCC_except_table4449
+ GCC_except_table4552
+ GCC_except_table4576
+ GCC_except_table4580
+ GCC_except_table4699
+ GCC_except_table4737
+ GCC_except_table4745
+ GCC_except_table4747
+ GCC_except_table4775
+ GCC_except_table4797
+ GCC_except_table5044
+ GCC_except_table5051
+ GCC_except_table5055
+ GCC_except_table5066
+ GCC_except_table5073
+ GCC_except_table512
+ GCC_except_table5220
+ GCC_except_table5312
+ GCC_except_table5373
+ GCC_except_table5376
+ GCC_except_table5388
+ GCC_except_table5389
+ GCC_except_table5395
+ GCC_except_table5396
+ GCC_except_table5397
+ GCC_except_table5402
+ GCC_except_table5410
+ GCC_except_table5503
+ GCC_except_table5854
+ GCC_except_table5873
+ GCC_except_table5874
+ GCC_except_table5884
+ GCC_except_table5889
+ GCC_except_table5941
+ GCC_except_table5946
+ GCC_except_table5959
+ GCC_except_table5983
+ GCC_except_table5985
+ GCC_except_table5986
+ GCC_except_table5987
+ GCC_except_table5989
+ GCC_except_table5993
+ GCC_except_table5995
+ GCC_except_table5998
+ GCC_except_table6001
+ GCC_except_table6003
+ GCC_except_table6004
+ GCC_except_table6005
+ GCC_except_table6012
+ GCC_except_table6045
+ GCC_except_table6149
+ GCC_except_table6152
+ GCC_except_table6192
+ GCC_except_table6266
+ GCC_except_table6585
+ GCC_except_table6836
+ GCC_except_table6837
+ GCC_except_table6927
+ GCC_except_table6930
+ GCC_except_table6934
+ GCC_except_table6935
+ GCC_except_table6939
+ GCC_except_table6940
+ GCC_except_table6942
+ GCC_except_table6948
+ GCC_except_table6961
+ GCC_except_table6978
+ GCC_except_table7032
+ GCC_except_table7084
+ GCC_except_table7085
+ GCC_except_table7086
+ GCC_except_table7087
+ GCC_except_table7119
+ GCC_except_table7124
+ GCC_except_table7192
+ GCC_except_table7202
+ GCC_except_table7306
+ GCC_except_table7359
+ GCC_except_table7361
+ GCC_except_table7455
+ GCC_except_table7461
+ GCC_except_table7466
+ GCC_except_table7468
+ GCC_except_table7469
+ GCC_except_table7470
+ GCC_except_table7472
+ GCC_except_table7474
+ GCC_except_table7477
+ GCC_except_table7478
+ GCC_except_table7479
+ GCC_except_table7480
+ GCC_except_table7482
+ GCC_except_table7483
+ GCC_except_table7485
+ GCC_except_table7486
+ GCC_except_table7487
+ GCC_except_table7488
+ GCC_except_table7489
+ GCC_except_table7490
+ GCC_except_table7492
+ GCC_except_table7550
+ GCC_except_table7561
+ GCC_except_table7575
+ GCC_except_table7577
+ GCC_except_table7611
+ GCC_except_table7612
+ GCC_except_table7613
+ GCC_except_table7616
+ GCC_except_table7619
+ GCC_except_table7665
+ GCC_except_table7809
+ GCC_except_table7819
+ GCC_except_table7826
+ GCC_except_table7827
+ GCC_except_table7828
+ GCC_except_table7829
+ GCC_except_table7830
+ GCC_except_table7831
+ GCC_except_table787
+ GCC_except_table7875
+ GCC_except_table798
+ GCC_except_table8061
+ GCC_except_table808
+ GCC_except_table828
+ GCC_except_table8289
+ GCC_except_table8291
+ GCC_except_table8292
+ GCC_except_table8354
+ GCC_except_table8356
+ GCC_except_table8358
+ GCC_except_table8428
+ GCC_except_table8464
+ GCC_except_table8473
+ GCC_except_table8475
+ GCC_except_table8480
+ GCC_except_table8484
+ GCC_except_table8487
+ GCC_except_table8498
+ GCC_except_table8511
+ GCC_except_table8519
+ GCC_except_table8520
+ GCC_except_table8524
+ GCC_except_table8533
+ GCC_except_table8543
+ GCC_except_table8544
+ GCC_except_table8547
+ GCC_except_table8549
+ GCC_except_table8553
+ GCC_except_table8555
+ GCC_except_table8556
+ GCC_except_table8568
+ GCC_except_table875
+ GCC_except_table878
+ GCC_except_table879
+ OBJC_IVAR_$_PIParallaxClockLayoutRequest._displayContext
+ OBJC_IVAR_$_PIParallaxCompoundLayerStackRequest._layoutConfiguration
+ OBJC_IVAR_$_PIParallaxCompoundLayerStackRequest._savedLayoutUsesHeadroom
+ OBJC_IVAR_$_PIParallaxSegmentationItem._gainMapMedia
+ OBJC_IVAR_$_PIParallaxSegmentationItem._sensitiveContentEvaluated
+ OBJC_IVAR_$_PIPhotographicStyleCorruption._kind
+ OBJC_IVAR_$_PIPhotographicStyleCorruption._notes
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._corruptions
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._linearThumbnailCorrupted
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._mainVideoCorrupted
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._photographicStyleV1Capable
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._photographicStyleV2Capable
+ OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._skinMatteCorrupted
+ _NUMediaCharacteristicSkinMatte
+ _OBJC_CLASS_$_PIPhotographicStyleCorruption
+ _OBJC_CLASS_$_PIPhotographicStyleCorruptionReport
+ _OBJC_CLASS_$_PISpatialReframeAutoCalculator
+ _OBJC_METACLASS_$_PIPhotographicStyleCorruption
+ _OBJC_METACLASS_$_PIPhotographicStyleCorruptionReport
+ _OBJC_METACLASS_$_PISpatialReframeAutoCalculator
+ _PISemanticStyleDefaultValuesForCast
+ _PISpatialReframeSceneKey
+ __78-[PIParallaxCompoundLayerStackRequest _chooseLayoutForOrientation:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_PIPhotographicStyleCorruptionReport
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyleCorruption
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyleCorruptionReport
+ __OBJC_$_INSTANCE_METHODS_PISpatialReframeAutoCalculator
+ __OBJC_$_INSTANCE_VARIABLES_PIPhotographicStyleCorruption
+ __OBJC_$_INSTANCE_VARIABLES_PIPhotographicStyleCorruptionReport
+ __OBJC_$_PROP_LIST_PIPhotographicStyleCorruption
+ __OBJC_$_PROP_LIST_PIPhotographicStyleCorruptionReport
+ __OBJC_CLASS_RO_$_PIPhotographicStyleCorruption
+ __OBJC_CLASS_RO_$_PIPhotographicStyleCorruptionReport
+ __OBJC_CLASS_RO_$_PISpatialReframeAutoCalculator
+ __OBJC_METACLASS_RO_$_PIPhotographicStyleCorruption
+ __OBJC_METACLASS_RO_$_PIPhotographicStyleCorruptionReport
+ __OBJC_METACLASS_RO_$_PISpatialReframeAutoCalculator
+ ___42-[PIModularPhotosPipelineCache clearCache]_block_invoke
+ ___78-[PIParallaxCompoundLayerStackRequest _chooseLayoutForOrientation:completion:]_block_invoke_2
+ ___96+[PICinematicVideoUtilities loadCinematographyScriptWithVideoURLString:changesDictionary:error:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e39_v16?0"PFParallaxLayoutConfiguration"8l
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48bs56bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24l
+ ___block_descriptor_72_e8_32s40s48s56bs_e20_v16?0"NUResponse"8l
+ ___block_descriptor_72_e8_32s40s48s56bs_e48_v16?0"PFWallpaperCompoundDeviceConfiguration"8l
+ ___copy_helper_block_e8_32s40s48b56b
+ _objc_msgSend$_baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:
+ _objc_msgSend$channelInfo
+ _objc_msgSend$clearCache
+ _objc_msgSend$defaultValuesForCast:smartStyleRenderingVersion:
+ _objc_msgSend$gainMapMedia
+ _objc_msgSend$geometryWithRoundingPolicy:
+ _objc_msgSend$initWithKind:notes:
+ _objc_msgSend$initWithPhotographicStyleV1Capable:photographicStyleV2Capable:mainVideoCorrupted:linearThumbnailCorrupted:skinMatteCorrupted:corruptions:
+ _objc_msgSend$isEquivalentToDynamicDeviceConfiguration:
+ _objc_msgSend$isOneShot
+ _objc_msgSend$layoutProxyScalePolicy
+ _objc_msgSend$linearThumbnailCorrupted
+ _objc_msgSend$mainVideoCorrupted
+ _objc_msgSend$photographicStyleV1Capable
+ _objc_msgSend$reportForImageProperties:
+ _objc_msgSend$reportForVideoProperties:
+ _objc_msgSend$sensitiveContentEvaluated
+ _objc_msgSend$setGainMapMedia:
+ _objc_msgSend$setSavedLayoutUsesHeadroom:
+ _objc_msgSend$setSensitiveContentEvaluated:
- GCC_except_table1117
- GCC_except_table1717
- GCC_except_table1731
- GCC_except_table1899
- GCC_except_table2077
- GCC_except_table2231
- GCC_except_table2243
- GCC_except_table2249
- GCC_except_table2259
- GCC_except_table2266
- GCC_except_table2276
- GCC_except_table2356
- GCC_except_table2396
- GCC_except_table2425
- GCC_except_table2432
- GCC_except_table2447
- GCC_except_table2465
- GCC_except_table2470
- GCC_except_table2566
- GCC_except_table2788
- GCC_except_table3137
- GCC_except_table3145
- GCC_except_table3176
- GCC_except_table3180
- GCC_except_table3182
- GCC_except_table3183
- GCC_except_table3185
- GCC_except_table3187
- GCC_except_table3189
- GCC_except_table319
- GCC_except_table3196
- GCC_except_table3201
- GCC_except_table3210
- GCC_except_table3304
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3478
- GCC_except_table3522
- GCC_except_table3530
- GCC_except_table3582
- GCC_except_table3794
- GCC_except_table3804
- GCC_except_table3807
- GCC_except_table3808
- GCC_except_table3820
- GCC_except_table3867
- GCC_except_table3876
- GCC_except_table3904
- GCC_except_table3929
- GCC_except_table4160
- GCC_except_table4414
- GCC_except_table4517
- GCC_except_table4541
- GCC_except_table4545
- GCC_except_table4664
- GCC_except_table4702
- GCC_except_table4710
- GCC_except_table4712
- GCC_except_table4740
- GCC_except_table4762
- GCC_except_table4985
- GCC_except_table5009
- GCC_except_table5016
- GCC_except_table5031
- GCC_except_table5038
- GCC_except_table507
- GCC_except_table5185
- GCC_except_table5277
- GCC_except_table5338
- GCC_except_table5341
- GCC_except_table5353
- GCC_except_table5354
- GCC_except_table5360
- GCC_except_table5361
- GCC_except_table5362
- GCC_except_table5367
- GCC_except_table5375
- GCC_except_table5468
- GCC_except_table5816
- GCC_except_table5835
- GCC_except_table5836
- GCC_except_table5846
- GCC_except_table5851
- GCC_except_table5903
- GCC_except_table5908
- GCC_except_table5909
- GCC_except_table5919
- GCC_except_table5921
- GCC_except_table5945
- GCC_except_table5948
- GCC_except_table5949
- GCC_except_table5951
- GCC_except_table5955
- GCC_except_table5960
- GCC_except_table5963
- GCC_except_table5965
- GCC_except_table5966
- GCC_except_table5967
- GCC_except_table5969
- GCC_except_table5974
- GCC_except_table6111
- GCC_except_table6150
- GCC_except_table6224
- GCC_except_table6543
- GCC_except_table6794
- GCC_except_table6795
- GCC_except_table6885
- GCC_except_table6888
- GCC_except_table6892
- GCC_except_table6893
- GCC_except_table6897
- GCC_except_table6898
- GCC_except_table6900
- GCC_except_table6906
- GCC_except_table6919
- GCC_except_table6936
- GCC_except_table6990
- GCC_except_table7042
- GCC_except_table7043
- GCC_except_table7044
- GCC_except_table7045
- GCC_except_table7076
- GCC_except_table7081
- GCC_except_table7149
- GCC_except_table7159
- GCC_except_table7263
- GCC_except_table7316
- GCC_except_table7318
- GCC_except_table7412
- GCC_except_table7418
- GCC_except_table7423
- GCC_except_table7425
- GCC_except_table7426
- GCC_except_table7427
- GCC_except_table7429
- GCC_except_table7431
- GCC_except_table7434
- GCC_except_table7435
- GCC_except_table7436
- GCC_except_table7437
- GCC_except_table7439
- GCC_except_table7440
- GCC_except_table7442
- GCC_except_table7443
- GCC_except_table7444
- GCC_except_table7445
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7449
- GCC_except_table7507
- GCC_except_table7518
- GCC_except_table7532
- GCC_except_table7533
- GCC_except_table7534
- GCC_except_table7568
- GCC_except_table7569
- GCC_except_table7570
- GCC_except_table7573
- GCC_except_table7622
- GCC_except_table7766
- GCC_except_table7776
- GCC_except_table7783
- GCC_except_table7784
- GCC_except_table7785
- GCC_except_table7786
- GCC_except_table7787
- GCC_except_table7788
- GCC_except_table7789
- GCC_except_table780
- GCC_except_table791
- GCC_except_table801
- GCC_except_table8018
- GCC_except_table821
- GCC_except_table8246
- GCC_except_table8248
- GCC_except_table8249
- GCC_except_table8311
- GCC_except_table8313
- GCC_except_table8315
- GCC_except_table8385
- GCC_except_table8421
- GCC_except_table8430
- GCC_except_table8432
- GCC_except_table8434
- GCC_except_table8437
- GCC_except_table8441
- GCC_except_table8444
- GCC_except_table8455
- GCC_except_table8468
- GCC_except_table8476
- GCC_except_table8481
- GCC_except_table8482
- GCC_except_table8490
- GCC_except_table8500
- GCC_except_table8501
- GCC_except_table8504
- GCC_except_table8506
- GCC_except_table8510
- GCC_except_table8512
- GCC_except_table8513
- GCC_except_table868
- GCC_except_table871
- GCC_except_table872
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke_2
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8l
- ___block_descriptor_40_e8_32s_e31_B16?0"NUVideoCorruptionInfo"8l
- ___block_descriptor_56_e8_32s40bs_e20_v16?0"NUResponse"8l
- _objc_msgSend$defaultValuesForCast:
- _swift_deallocClassInstance
- _swift_setDeallocating
- _symbolic SSIego_
- _symbolic Say_____GIegr_ So6CGRectV
- _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
- _symbolic yyc
CStrings:
+ "%@ %lu/%lu"
+ "+[PICinematicVideoUtilities loadCinematographyScriptWithVideoURLString:changesDictionary:error:]"
+ "-[PISpatialReframeAutoCalculator processComputedData:error:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISpatialReframeAutoCalculator.m"
+ "Asset does not support spatial reframe"
+ "Extend"
+ "Failed to load cinematography script"
+ "Invalid video URL for cinematography script"
+ "Spatial reframe scene is missing a value"
+ "Timeout waiting for cinematography script to load"
+ "Unexpected videoURL type"
+ "duplicatePTS"
+ "scene"
+ "sensitiveContentEvaluated"
+ "useOriginalExtent"
+ "v16@?0@\"PFParallaxLayoutConfiguration\"8"
+ "v16@?0@\"PFWallpaperCompoundDeviceConfiguration\"8"
- "Failed to load media for HDR gain map, skipping"
```
