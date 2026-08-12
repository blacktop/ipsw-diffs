## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x27b740
+912.0.111.0.0
+  __TEXT.__text: 0x27c598
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x164a0
-  __TEXT.__const: 0x8a9c
+  __TEXT.__objc_methlist: 0x165d0
+  __TEXT.__const: 0x8a7c
   __TEXT.__dlopen_cstrs: 0x2a2
-  __TEXT.__swift5_typeref: 0x2e9
-  __TEXT.__cstring: 0x46c85
+  __TEXT.__swift5_typeref: 0x299
+  __TEXT.__cstring: 0x46e60
   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_reflstr: 0x35f
   __TEXT.__swift5_fieldmd: 0x3b8
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__oslogstring: 0x6d75
+  __TEXT.__oslogstring: 0x6c42
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__swift5_capture: 0xf0
-  __TEXT.__gcc_except_tab: 0x4a64
-  __TEXT.__unwind_info: 0x5858
+  __TEXT.__swift5_capture: 0x50
+  __TEXT.__gcc_except_tab: 0x4b34
+  __TEXT.__unwind_info: 0x5888
   __TEXT.__eh_frame: 0x9f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40d0
-  __DATA_CONST.__objc_classlist: 0x10d8
+  __DATA_CONST.__const: 0x4100
+  __DATA_CONST.__objc_classlist: 0x10f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb528
+  __DATA_CONST.__objc_selrefs: 0xb5b8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x700
-  __DATA_CONST.__objc_arraydata: 0x9340
-  __DATA_CONST.__got: 0x25a0
-  __AUTH_CONST.__const: 0x54b0
-  __AUTH_CONST.__cfstring: 0x26cc0
-  __AUTH_CONST.__objc_const: 0x28370
+  __DATA_CONST.__objc_superrefs: 0x710
+  __DATA_CONST.__objc_arraydata: 0x9350
+  __DATA_CONST.__got: 0x25b8
+  __AUTH_CONST.__const: 0x5320
+  __AUTH_CONST.__cfstring: 0x26da0
+  __AUTH_CONST.__objc_const: 0x286f0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x1488
-  __AUTH_CONST.__objc_dictobj: 0x5af0
+  __AUTH_CONST.__objc_dictobj: 0x5b18
   __AUTH_CONST.__objc_doubleobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x558
   __AUTH_CONST.__objc_floatobj: 0xd0
-  __AUTH_CONST.__auth_got: 0x1558
-  __AUTH.__objc_data: 0x288
-  __DATA.__objc_ivar: 0x1570
-  __DATA.__data: 0x16fc
+  __AUTH_CONST.__auth_got: 0x14f8
+  __AUTH.__objc_data: 0x378
+  __DATA.__objc_ivar: 0x1594
+  __DATA.__data: 0x16f0
   __DATA.__bss: 0x1600
   __DATA_DIRTY.__objc_data: 0xa7a0
-  __DATA_DIRTY.__data: 0x170
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__data: 0x178
+  __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9130
-  Symbols:   20568
-  CStrings:  7086
+  Functions: 9134
+  Symbols:   20620
+  CStrings:  7095
 
Symbols:
+ +[PIModularPhotosPipeline clearPipelineCache]
+ +[PIPhotographicStyleCorruptionReport reportForImageProperties:]
+ +[PIPhotographicStyleCorruptionReport reportForVideoProperties:]
+ +[PISegmentationLoader _baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:]
+ +[PISemanticStyleAdjustmentController defaultValuesForCast:smartStyleRenderingVersion:]
+ -[PIModularPhotosPipelineCache clearCache]
+ -[PIParallaxClockLayoutRequest displayContext]
+ -[PIParallaxClockLayoutRequest setDisplayContext:]
+ -[PIParallaxCompoundLayerStackRequest layoutConfiguration]
+ -[PIParallaxCompoundLayerStackRequest setLayoutConfiguration:]
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
+ GCC_except_table1104
+ GCC_except_table1706
+ GCC_except_table1720
+ GCC_except_table1887
+ GCC_except_table2063
+ GCC_except_table2217
+ GCC_except_table2227
+ GCC_except_table2233
+ GCC_except_table2241
+ GCC_except_table2248
+ GCC_except_table2256
+ GCC_except_table2334
+ GCC_except_table2374
+ GCC_except_table2403
+ GCC_except_table2408
+ GCC_except_table2423
+ GCC_except_table2439
+ GCC_except_table2444
+ GCC_except_table2450
+ GCC_except_table2537
+ GCC_except_table2759
+ GCC_except_table309
+ GCC_except_table3112
+ GCC_except_table3117
+ GCC_except_table3151
+ GCC_except_table3153
+ GCC_except_table3156
+ GCC_except_table3158
+ GCC_except_table3166
+ GCC_except_table3171
+ GCC_except_table3180
+ GCC_except_table3275
+ GCC_except_table3344
+ GCC_except_table3345
+ GCC_except_table3454
+ GCC_except_table3496
+ GCC_except_table3504
+ GCC_except_table3556
+ GCC_except_table3782
+ GCC_except_table3792
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3808
+ GCC_except_table3855
+ GCC_except_table3864
+ GCC_except_table387
+ GCC_except_table3892
+ GCC_except_table3915
+ GCC_except_table4144
+ GCC_except_table4396
+ GCC_except_table4499
+ GCC_except_table4523
+ GCC_except_table4527
+ GCC_except_table4646
+ GCC_except_table4684
+ GCC_except_table4690
+ GCC_except_table4692
+ GCC_except_table4716
+ GCC_except_table4738
+ GCC_except_table4961
+ GCC_except_table498
+ GCC_except_table4984
+ GCC_except_table4991
+ GCC_except_table4994
+ GCC_except_table5005
+ GCC_except_table5012
+ GCC_except_table5159
+ GCC_except_table5251
+ GCC_except_table5312
+ GCC_except_table5315
+ GCC_except_table5327
+ GCC_except_table5328
+ GCC_except_table5332
+ GCC_except_table5333
+ GCC_except_table5334
+ GCC_except_table5339
+ GCC_except_table5347
+ GCC_except_table5440
+ GCC_except_table5790
+ GCC_except_table5809
+ GCC_except_table5810
+ GCC_except_table5816
+ GCC_except_table5821
+ GCC_except_table5873
+ GCC_except_table5878
+ GCC_except_table5879
+ GCC_except_table5917
+ GCC_except_table5918
+ GCC_except_table5919
+ GCC_except_table5921
+ GCC_except_table5923
+ GCC_except_table5925
+ GCC_except_table5928
+ GCC_except_table5931
+ GCC_except_table5933
+ GCC_except_table5934
+ GCC_except_table5935
+ GCC_except_table5936
+ GCC_except_table5938
+ GCC_except_table5943
+ GCC_except_table5976
+ GCC_except_table6079
+ GCC_except_table6118
+ GCC_except_table6192
+ GCC_except_table6511
+ GCC_except_table6759
+ GCC_except_table6760
+ GCC_except_table6850
+ GCC_except_table6853
+ GCC_except_table6857
+ GCC_except_table6858
+ GCC_except_table6862
+ GCC_except_table6863
+ GCC_except_table6865
+ GCC_except_table6871
+ GCC_except_table6880
+ GCC_except_table6896
+ GCC_except_table6947
+ GCC_except_table6999
+ GCC_except_table7000
+ GCC_except_table7001
+ GCC_except_table7002
+ GCC_except_table7033
+ GCC_except_table7036
+ GCC_except_table7104
+ GCC_except_table7114
+ GCC_except_table7218
+ GCC_except_table7271
+ GCC_except_table7273
+ GCC_except_table7373
+ GCC_except_table7376
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7380
+ GCC_except_table7381
+ GCC_except_table7383
+ GCC_except_table7386
+ GCC_except_table7387
+ GCC_except_table7388
+ GCC_except_table7389
+ GCC_except_table7391
+ GCC_except_table7392
+ GCC_except_table7394
+ GCC_except_table7395
+ GCC_except_table7396
+ GCC_except_table7397
+ GCC_except_table7452
+ GCC_except_table7460
+ GCC_except_table7474
+ GCC_except_table7475
+ GCC_except_table7476
+ GCC_except_table7510
+ GCC_except_table7511
+ GCC_except_table7512
+ GCC_except_table7515
+ GCC_except_table7518
+ GCC_except_table7563
+ GCC_except_table7565
+ GCC_except_table7709
+ GCC_except_table771
+ GCC_except_table7719
+ GCC_except_table7726
+ GCC_except_table7727
+ GCC_except_table7728
+ GCC_except_table7729
+ GCC_except_table7730
+ GCC_except_table7731
+ GCC_except_table7732
+ GCC_except_table7775
+ GCC_except_table782
+ GCC_except_table792
+ GCC_except_table7961
+ GCC_except_table812
+ GCC_except_table8189
+ GCC_except_table8191
+ GCC_except_table8192
+ GCC_except_table8254
+ GCC_except_table8256
+ GCC_except_table8258
+ GCC_except_table8328
+ GCC_except_table8351
+ GCC_except_table8353
+ GCC_except_table8356
+ GCC_except_table8360
+ GCC_except_table8362
+ GCC_except_table8395
+ GCC_except_table8408
+ GCC_except_table8416
+ GCC_except_table8426
+ GCC_except_table8427
+ GCC_except_table8430
+ GCC_except_table8432
+ GCC_except_table8436
+ GCC_except_table8438
+ GCC_except_table8439
+ GCC_except_table8451
+ GCC_except_table862
+ GCC_except_table863
+ _NUMediaCharacteristicSkinMatte
+ _OBJC_CLASS_$_PIPhotographicStyleCorruption
+ _OBJC_CLASS_$_PIPhotographicStyleCorruptionReport
+ _OBJC_CLASS_$_PISpatialReframeAutoCalculator
+ _OBJC_IVAR_$_PIParallaxClockLayoutRequest._displayContext
+ _OBJC_IVAR_$_PIParallaxCompoundLayerStackRequest._layoutConfiguration
+ _OBJC_IVAR_$_PIPhotographicStyleCorruption._kind
+ _OBJC_IVAR_$_PIPhotographicStyleCorruption._notes
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._corruptions
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._linearThumbnailCorrupted
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._mainVideoCorrupted
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._photographicStyleV1Capable
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._photographicStyleV2Capable
+ _OBJC_IVAR_$_PIPhotographicStyleCorruptionReport._skinMatteCorrupted
+ _OBJC_METACLASS_$_PIPhotographicStyleCorruption
+ _OBJC_METACLASS_$_PIPhotographicStyleCorruptionReport
+ _OBJC_METACLASS_$_PISpatialReframeAutoCalculator
+ _PISemanticStyleDefaultValuesForCast
+ _PISpatialReframeSceneKey
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
+ ___30-[PIGenerativeRequest submit:]_block_invoke_7
+ ___42-[PIModularPhotosPipelineCache clearCache]_block_invoke
+ ___78-[PIParallaxCompoundLayerStackRequest _chooseLayoutForOrientation:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e39_v16?0"PFParallaxLayoutConfiguration"8ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s48l8s56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e20_v16?0"NUResponse"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e48_v16?0"PFWallpaperCompoundDeviceConfiguration"8ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:
+ _objc_msgSend$channelInfo
+ _objc_msgSend$clearCache
+ _objc_msgSend$defaultValuesForCast:smartStyleRenderingVersion:
+ _objc_msgSend$geometryWithRoundingPolicy:
+ _objc_msgSend$initWithKind:notes:
+ _objc_msgSend$initWithPhotographicStyleV1Capable:photographicStyleV2Capable:mainVideoCorrupted:linearThumbnailCorrupted:skinMatteCorrupted:corruptions:
+ _objc_msgSend$isEquivalentToDynamicDeviceConfiguration:
+ _objc_msgSend$linearThumbnailCorrupted
+ _objc_msgSend$mainVideoCorrupted
+ _objc_msgSend$photographicStyleV1Capable
+ _objc_msgSend$reportForImageProperties:
+ _objc_msgSend$reportForVideoProperties:
- -[PIParallaxSegmentationItem savedLayoutUsesHeadroom]
- -[PIParallaxSegmentationItem setSavedLayoutUsesHeadroom:]
- GCC_except_table1101
- GCC_except_table1705
- GCC_except_table1719
- GCC_except_table1886
- GCC_except_table2062
- GCC_except_table2216
- GCC_except_table2226
- GCC_except_table2232
- GCC_except_table2240
- GCC_except_table2247
- GCC_except_table2255
- GCC_except_table2333
- GCC_except_table2373
- GCC_except_table2402
- GCC_except_table2407
- GCC_except_table2422
- GCC_except_table2438
- GCC_except_table2443
- GCC_except_table2449
- GCC_except_table2536
- GCC_except_table2758
- GCC_except_table3106
- GCC_except_table3111
- GCC_except_table312
- GCC_except_table3141
- GCC_except_table3145
- GCC_except_table3148
- GCC_except_table3150
- GCC_except_table3152
- GCC_except_table3165
- GCC_except_table3174
- GCC_except_table3268
- GCC_except_table3333
- GCC_except_table3334
- GCC_except_table3443
- GCC_except_table3485
- GCC_except_table3493
- GCC_except_table3545
- GCC_except_table3757
- GCC_except_table3767
- GCC_except_table3770
- GCC_except_table3771
- GCC_except_table3783
- GCC_except_table3830
- GCC_except_table3839
- GCC_except_table3867
- GCC_except_table3890
- GCC_except_table4119
- GCC_except_table4371
- GCC_except_table4474
- GCC_except_table4498
- GCC_except_table4502
- GCC_except_table4621
- GCC_except_table4659
- GCC_except_table4665
- GCC_except_table4667
- GCC_except_table4691
- GCC_except_table4713
- GCC_except_table4936
- GCC_except_table4959
- GCC_except_table4966
- GCC_except_table4969
- GCC_except_table497
- GCC_except_table4980
- GCC_except_table4987
- GCC_except_table5134
- GCC_except_table5226
- GCC_except_table5287
- GCC_except_table5290
- GCC_except_table5302
- GCC_except_table5303
- GCC_except_table5307
- GCC_except_table5308
- GCC_except_table5309
- GCC_except_table5314
- GCC_except_table5322
- GCC_except_table5415
- GCC_except_table5762
- GCC_except_table5781
- GCC_except_table5782
- GCC_except_table5788
- GCC_except_table5793
- GCC_except_table5845
- GCC_except_table5850
- GCC_except_table5851
- GCC_except_table5861
- GCC_except_table5863
- GCC_except_table5887
- GCC_except_table5890
- GCC_except_table5893
- GCC_except_table5895
- GCC_except_table5897
- GCC_except_table5900
- GCC_except_table5903
- GCC_except_table5905
- GCC_except_table5906
- GCC_except_table5907
- GCC_except_table5908
- GCC_except_table5910
- GCC_except_table5948
- GCC_except_table6051
- GCC_except_table6090
- GCC_except_table6164
- GCC_except_table6483
- GCC_except_table6731
- GCC_except_table6732
- GCC_except_table6822
- GCC_except_table6825
- GCC_except_table6829
- GCC_except_table6830
- GCC_except_table6834
- GCC_except_table6835
- GCC_except_table6837
- GCC_except_table6843
- GCC_except_table6852
- GCC_except_table6868
- GCC_except_table6919
- GCC_except_table6971
- GCC_except_table6972
- GCC_except_table6973
- GCC_except_table6974
- GCC_except_table7004
- GCC_except_table7007
- GCC_except_table7075
- GCC_except_table7085
- GCC_except_table7189
- GCC_except_table7242
- GCC_except_table7244
- GCC_except_table7338
- GCC_except_table7344
- GCC_except_table7347
- GCC_except_table7349
- GCC_except_table7350
- GCC_except_table7351
- GCC_except_table7352
- GCC_except_table7354
- GCC_except_table7357
- GCC_except_table7358
- GCC_except_table7359
- GCC_except_table7360
- GCC_except_table7362
- GCC_except_table7363
- GCC_except_table7365
- GCC_except_table7366
- GCC_except_table7368
- GCC_except_table7423
- GCC_except_table7431
- GCC_except_table7445
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7481
- GCC_except_table7482
- GCC_except_table7483
- GCC_except_table7486
- GCC_except_table7489
- GCC_except_table7534
- GCC_except_table7536
- GCC_except_table768
- GCC_except_table7680
- GCC_except_table7690
- GCC_except_table7697
- GCC_except_table7698
- GCC_except_table7699
- GCC_except_table7700
- GCC_except_table7701
- GCC_except_table7702
- GCC_except_table7703
- GCC_except_table7746
- GCC_except_table779
- GCC_except_table789
- GCC_except_table7932
- GCC_except_table809
- GCC_except_table8160
- GCC_except_table8162
- GCC_except_table8163
- GCC_except_table8225
- GCC_except_table8227
- GCC_except_table8229
- GCC_except_table8299
- GCC_except_table8322
- GCC_except_table8324
- GCC_except_table8327
- GCC_except_table8331
- GCC_except_table8333
- GCC_except_table8349
- GCC_except_table8366
- GCC_except_table8374
- GCC_except_table8379
- GCC_except_table8387
- GCC_except_table8397
- GCC_except_table8398
- GCC_except_table8401
- GCC_except_table8409
- GCC_except_table8410
- GCC_except_table8422
- GCC_except_table856
- GCC_except_table860
- _OBJC_IVAR_$_PIParallaxSegmentationItem._savedLayoutUsesHeadroom
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke_2
- ___57+[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e31_B16?0"NUVideoCorruptionInfo"8ls32l8
- ___block_descriptor_56_e8_32s40bs_e20_v16?0"NUResponse"8ls40l8s32l8
- _objc_msgSend$defaultValuesForCast:
- _swift_deallocClassInstance
- _swift_release_x24
- _swift_release_x25
- _swift_release_x26
- _swift_retain_x20
- _swift_retain_x23
- _swift_retain_x25
- _swift_retain_x26
- _swift_retain_x27
- _swift_retain_x28
- _swift_retain_x8
- _swift_setDeallocating
- _symbolic SSIego_
- _symbolic Say_____GIegr_ So6CGRectV
- _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
- _symbolic yyc
CStrings:
+ "%@ %lu/%lu"
+ "-[PISpatialReframeAutoCalculator processComputedData:error:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISpatialReframeAutoCalculator.m"
+ "Asset does not support spatial reframe"
+ "Extend"
+ "Spatial reframe scene is missing a value"
+ "duplicatePTS"
+ "scene"
+ "useOriginalExtent"
+ "v16@?0@\"PFParallaxLayoutConfiguration\"8"
+ "v16@?0@\"PFWallpaperCompoundDeviceConfiguration\"8"
- "[headroom-blackout] fill-gate: needHeadroom=%d isBackfill=%d headroomDisabled=%d lock=%d needHeadroomForOutfill=%d -> willFill=%d"
- "[headroom-blackout] flags: lock=%d origPixelLayoutLacksHeadroom=%d outfillStatus=%ld savedLayoutUsesHeadroom=%d needHeadroomForOutfill=%d headroomDisabled=%d layerStackMode=%ld"
```
