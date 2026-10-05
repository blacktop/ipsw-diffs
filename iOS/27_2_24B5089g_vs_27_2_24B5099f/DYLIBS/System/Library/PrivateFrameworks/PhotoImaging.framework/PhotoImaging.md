## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0x295514
+916.51.202.0.0
+  __TEXT.__text: 0x297fa8
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x17460
-  __TEXT.__const: 0x8d04
+  __TEXT.__objc_methlist: 0x175a0
+  __TEXT.__const: 0x8d54
   __TEXT.__dlopen_cstrs: 0x2a2
-  __TEXT.__swift5_typeref: 0x2d8
-  __TEXT.__cstring: 0x4ac49
   __TEXT.__constg_swiftt: 0x230
-  __TEXT.__swift5_reflstr: 0x35f
-  __TEXT.__swift5_fieldmd: 0x3d4
+  __TEXT.__swift5_typeref: 0x34e
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_reflstr: 0x38f
+  __TEXT.__swift5_fieldmd: 0x3ec
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__oslogstring: 0x7e71
+  __TEXT.__swift5_capture: 0x8c
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x38
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__swift_as_cont: 0x28
-  __TEXT.__swift5_capture: 0x50
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__swift_as_cont: 0x34
+  __TEXT.__cstring: 0x4ae87
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__oslogstring: 0x7f8b
   __TEXT.__gcc_except_tab: 0x4f0c
-  __TEXT.__unwind_info: 0x6ef8
-  __TEXT.__eh_frame: 0xa60
+  __TEXT.__unwind_info: 0x7008
+  __TEXT.__eh_frame: 0xbb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x44b8
-  __DATA_CONST.__objc_classlist: 0x11b0
+  __DATA_CONST.__const: 0x4550
+  __DATA_CONST.__objc_classlist: 0x11e0
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1a0
+  __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbd70
+  __DATA_CONST.__objc_selrefs: 0xbda8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x758
-  __DATA_CONST.__objc_arraydata: 0x9660
-  __DATA_CONST.__got: 0x2820
-  __AUTH_CONST.__const: 0x5688
-  __AUTH_CONST.__cfstring: 0x29f40
-  __AUTH_CONST.__objc_const: 0x29e08
+  __DATA_CONST.__objc_superrefs: 0x778
+  __DATA_CONST.__objc_arraydata: 0x8fb8
+  __DATA_CONST.__got: 0x2878
+  __AUTH_CONST.__const: 0x57a0
+  __AUTH_CONST.__cfstring: 0x29c00
+  __AUTH_CONST.__objc_const: 0x2a380
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x1668
-  __AUTH_CONST.__objc_dictobj: 0x5c08
-  __AUTH_CONST.__objc_doubleobj: 0xe10
-  __AUTH_CONST.__objc_arrayobj: 0x6f0
-  __AUTH_CONST.__objc_floatobj: 0xd0
-  __AUTH_CONST.__auth_got: 0x1508
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1608
-  __DATA.__data: 0x3c4
-  __DATA_DIRTY.__objc_data: 0xb1f8
+  __AUTH_CONST.__objc_intobj: 0x1638
+  __AUTH_CONST.__objc_dictobj: 0x55f0
+  __AUTH_CONST.__objc_doubleobj: 0xdf0
+  __AUTH_CONST.__objc_arrayobj: 0x708
+  __AUTH_CONST.__objc_floatobj: 0xb0
+  __AUTH_CONST.__auth_got: 0x1610
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x1620
+  __DATA.__data: 0x444
+  __DATA_DIRTY.__objc_data: 0xb0b8
   __DATA_DIRTY.__data: 0x1598
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9508
-  Symbols:   16441
-  CStrings:  7616
+  Functions: 9572
+  Symbols:   16531
+  CStrings:  7611
 
Symbols:
+ +[NUAssetCapability(PIAudioMix) audioMix]
+ +[NUAssetCapability(PICinematicVideo) cinematicVideo]
+ +[NUAssetCapability(PIPhotographicStyle) photographicStyle]
+ +[NUAssetCapability(PIPortrait) portrait]
+ +[PICleanup cleanupAdjustmentDescriptor]
+ +[PIDefinition_v1 adjustmentDescriptor]
+ +[PIGlobalSettings photosAppEditSettings]
+ +[PIGrain_v1 adjustmentDescriptor]
+ +[PIHighResolutionFusion_v1 adjustmentDescriptor]
+ +[PILevels_v1 adjustmentDescriptor]
+ +[PILivePhotoEffect_v1 adjustmentDescriptor]
+ +[PILivePhotoEffect_v1 flavorDescriptor]
+ +[PILivePhotoEffect_v1 recipeDescriptor]
+ +[PIModularPhotosPipeline_v0 controlDataWithSemanticStyleAdjustment:]
+ +[PIModularPhotosPipeline_v1 controlDataWithSemanticStyleAdjustment:textureStyleAdjustment:]
+ +[PINoiseReduction_v1 adjustmentDescriptor]
+ +[PIPhotographicStyle adjustmentDescriptor]
+ +[PIPhotographicStyle adjustmentFormat]
+ +[PIPhotographicStyle castDescriptor]
+ +[PIPhotographicStyle connectPhotographicStyleToPipeline:stylePipeline:primaryInput:adjustmentInput:assetMedia:isVideo:]
+ +[PIPhotographicStyleApply pipelineName]
+ +[PIPhotographicStyleCapability setLivePhotoVideoPhotographicStyleCapability:imageVersion:]
+ +[PIPhotographicStyleLearn pipelineName]
+ +[PIRedEye_v1 adjustmentDescriptor]
+ +[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]
+ +[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]
+ +[PISharpen_v1 adjustmentDescriptor]
+ +[PISmartBlackAndWhite_v1 adjustmentDescriptor]
+ +[PISmartColor_v1 adjustmentDescriptor]
+ +[PISmartCopyPaste pasteAdjustmentDescriptor]
+ +[PISmartTone_v1 adjustmentDescriptor]
+ +[PISmartTone_v1 statisticsDescriptor]
+ +[PISpatialReframe adjustmentDescriptor]
+ +[PIVignette_v1 adjustmentDescriptor]
+ -[PIGlobalSettings outfillSafetyEnabled]
+ -[PIGlobalSettings outfillSafetyThreshold]
+ -[PIParallaxSegmentationItem needsOutfillSafeEdgesCheck]
+ -[PIPhotographicStyle .cxx_destruct]
+ -[PIPhotographicStyle _versionedClassForAsset:]
+ -[PIPhotographicStyle asset]
+ -[PIPhotographicStyle buildPipeline:error:]
+ -[PIPhotographicStyle initWithAsset:options:]
+ -[PIPhotographicStyle init]
+ -[PIPhotographicStyle options]
+ -[PIPhotographicStyle versionedClassForAsset:]
+ -[PIPhotographicStyleApply _versionedClassForAsset:]
+ -[PIPhotographicStyleApply initWithAsset:options:]
+ -[PIPhotographicStyleApply pipelineName]
+ -[PIPhotographicStyleCapability evaluateForAsset:]
+ -[PIPhotographicStyleLearn _versionedClassForAsset:]
+ -[PIPhotographicStyleLearn initWithAsset:options:]
+ -[PIPhotographicStyleLearn pipelineName]
+ -[PIPortrait hasOption:]
+ -[PIPortraitLightingEffectV1Processor outputImageWithInputs:controlData:error:]
+ -[PIPosterOutfillSafetyRequest copyWithZone:]
+ -[PIPosterOutfillSafetyRequest initWithSegmentationItem:]
+ -[PIPosterOutfillSafetyRequest initWithSegmentationItem:threshold:]
+ -[PIPosterOutfillSafetyRequest mediaComponentType]
+ -[PIPosterOutfillSafetyRequest submit:]
+ -[PIPosterOutfillSafetyRequest threshold]
+ -[PIPrivatePhotosPipeline_v0 _addVideoPosterFramePipeline:sourceMedia:outputMedia:videoPosterFrameTime:]
+ -[PIPrivatePhotosPipeline_v1 _addVideoPosterFramePipeline:sourceMedia:outputMedia:videoPosterFrameTime:]
+ -[PISegmentationLoader _checkOutfillSafeEdges:completion:]
+ -[_PIAudioMixCapability evaluateForAsset:]
+ -[_PICinematicVideoCapability _evaluateCinematicCapabilityWithAsset:]
+ -[_PICinematicVideoCapability evaluateForAsset:]
+ -[_PIParallaxCompoundLayerStackResult partialFailureError]
+ -[_PIParallaxCompoundLayerStackResult setPartialFailureError:]
+ -[_PIPhotographicStyleSettingsExpressionFunction evaluateWithArguments:error:]
+ -[_PIPhotographicStyleSettingsExpressionFunction format]
+ -[_PIPortraitCapability _evaluateForImageAsset:]
+ -[_PIPortraitCapability _evaluateForLivePhotoAsset:]
+ -[_PIPortraitCapability evaluateForAsset:]
+ -[_PIPosterOutfillSafetyResult .cxx_destruct]
+ -[_PIPosterOutfillSafetyResult initWithSafeEdges:]
+ -[_PIPosterOutfillSafetyResult safeEdges]
+ GCC_except_table1137
+ GCC_except_table1739
+ GCC_except_table1753
+ GCC_except_table1923
+ GCC_except_table2097
+ GCC_except_table2250
+ GCC_except_table2260
+ GCC_except_table2266
+ GCC_except_table2274
+ GCC_except_table2281
+ GCC_except_table2289
+ GCC_except_table2367
+ GCC_except_table2407
+ GCC_except_table2436
+ GCC_except_table2441
+ GCC_except_table2456
+ GCC_except_table2472
+ GCC_except_table2477
+ GCC_except_table2483
+ GCC_except_table2570
+ GCC_except_table2805
+ GCC_except_table3159
+ GCC_except_table3164
+ GCC_except_table3194
+ GCC_except_table3198
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3203
+ GCC_except_table3207
+ GCC_except_table3213
+ GCC_except_table3218
+ GCC_except_table3227
+ GCC_except_table3322
+ GCC_except_table3391
+ GCC_except_table3392
+ GCC_except_table3501
+ GCC_except_table3551
+ GCC_except_table3603
+ GCC_except_table3795
+ GCC_except_table3915
+ GCC_except_table3925
+ GCC_except_table3928
+ GCC_except_table3941
+ GCC_except_table3988
+ GCC_except_table3997
+ GCC_except_table4025
+ GCC_except_table4049
+ GCC_except_table4277
+ GCC_except_table4449
+ GCC_except_table4538
+ GCC_except_table4639
+ GCC_except_table4663
+ GCC_except_table4667
+ GCC_except_table4786
+ GCC_except_table4823
+ GCC_except_table4829
+ GCC_except_table4831
+ GCC_except_table4855
+ GCC_except_table4877
+ GCC_except_table4981
+ GCC_except_table5038
+ GCC_except_table507
+ GCC_except_table5078
+ GCC_except_table5295
+ GCC_except_table5302
+ GCC_except_table5305
+ GCC_except_table5316
+ GCC_except_table5323
+ GCC_except_table5469
+ GCC_except_table5561
+ GCC_except_table5622
+ GCC_except_table5625
+ GCC_except_table5637
+ GCC_except_table5638
+ GCC_except_table5642
+ GCC_except_table5643
+ GCC_except_table5644
+ GCC_except_table5649
+ GCC_except_table5657
+ GCC_except_table5750
+ GCC_except_table6144
+ GCC_except_table6163
+ GCC_except_table6164
+ GCC_except_table6170
+ GCC_except_table6175
+ GCC_except_table6227
+ GCC_except_table6232
+ GCC_except_table6233
+ GCC_except_table6243
+ GCC_except_table6245
+ GCC_except_table6269
+ GCC_except_table6271
+ GCC_except_table6272
+ GCC_except_table6273
+ GCC_except_table6275
+ GCC_except_table6277
+ GCC_except_table6279
+ GCC_except_table6282
+ GCC_except_table6285
+ GCC_except_table6287
+ GCC_except_table6288
+ GCC_except_table6289
+ GCC_except_table6290
+ GCC_except_table6292
+ GCC_except_table6330
+ GCC_except_table6433
+ GCC_except_table6436
+ GCC_except_table6443
+ GCC_except_table6501
+ GCC_except_table6575
+ GCC_except_table6896
+ GCC_except_table7144
+ GCC_except_table7145
+ GCC_except_table7237
+ GCC_except_table7240
+ GCC_except_table7244
+ GCC_except_table7245
+ GCC_except_table7249
+ GCC_except_table7252
+ GCC_except_table7258
+ GCC_except_table7267
+ GCC_except_table7283
+ GCC_except_table7334
+ GCC_except_table7387
+ GCC_except_table7389
+ GCC_except_table7390
+ GCC_except_table7423
+ GCC_except_table7426
+ GCC_except_table7494
+ GCC_except_table7504
+ GCC_except_table7608
+ GCC_except_table7661
+ GCC_except_table7663
+ GCC_except_table7757
+ GCC_except_table7763
+ GCC_except_table7766
+ GCC_except_table7768
+ GCC_except_table7769
+ GCC_except_table7770
+ GCC_except_table7771
+ GCC_except_table7773
+ GCC_except_table7776
+ GCC_except_table7777
+ GCC_except_table7778
+ GCC_except_table7779
+ GCC_except_table778
+ GCC_except_table7781
+ GCC_except_table7782
+ GCC_except_table7784
+ GCC_except_table7785
+ GCC_except_table7786
+ GCC_except_table7787
+ GCC_except_table7842
+ GCC_except_table7850
+ GCC_except_table7864
+ GCC_except_table789
+ GCC_except_table7900
+ GCC_except_table7901
+ GCC_except_table7902
+ GCC_except_table7905
+ GCC_except_table7908
+ GCC_except_table7953
+ GCC_except_table7955
+ GCC_except_table799
+ GCC_except_table8099
+ GCC_except_table8109
+ GCC_except_table8116
+ GCC_except_table8117
+ GCC_except_table8118
+ GCC_except_table8119
+ GCC_except_table8120
+ GCC_except_table8121
+ GCC_except_table8122
+ GCC_except_table8166
+ GCC_except_table830
+ GCC_except_table8353
+ GCC_except_table8576
+ GCC_except_table8578
+ GCC_except_table8579
+ GCC_except_table8640
+ GCC_except_table8642
+ GCC_except_table8644
+ GCC_except_table8712
+ GCC_except_table8735
+ GCC_except_table8737
+ GCC_except_table8740
+ GCC_except_table8744
+ GCC_except_table8746
+ GCC_except_table8779
+ GCC_except_table8787
+ GCC_except_table8791
+ GCC_except_table8800
+ GCC_except_table8810
+ GCC_except_table8811
+ GCC_except_table8814
+ GCC_except_table8816
+ GCC_except_table8820
+ GCC_except_table8822
+ GCC_except_table8823
+ GCC_except_table8835
+ GCC_except_table896
+ GCC_except_table897
+ _OBJC_CLASS_$_PIPhotographicStyle
+ _OBJC_CLASS_$_PIPhotographicStyleApply
+ _OBJC_CLASS_$_PIPhotographicStyleCapability
+ _OBJC_CLASS_$_PIPhotographicStyleLearn
+ _OBJC_CLASS_$_PIPosterOutfillSafetyRequest
+ _OBJC_CLASS_$__PIAudioMixCapability
+ _OBJC_CLASS_$__PICinematicVideoCapability
+ _OBJC_CLASS_$__PIPhotographicStyleSettingsExpressionFunction
+ _OBJC_CLASS_$__PIPortraitCapability
+ _OBJC_CLASS_$__PIPosterOutfillSafetyResult
+ _OBJC_IVAR_$_PIParallaxCompoundLayerStackRequest._partialFailureError
+ _OBJC_IVAR_$_PIParallaxSegmentationItem._outfillSafeEdges
+ _OBJC_IVAR_$_PIPhotographicStyle._asset
+ _OBJC_IVAR_$_PIPhotographicStyle._options
+ _OBJC_IVAR_$_PIPosterOutfillSafetyRequest._threshold
+ _OBJC_IVAR_$__PIParallaxCompoundLayerStackResult._partialFailureError
+ _OBJC_IVAR_$__PIPosterOutfillSafetyResult._safeEdges
+ _OBJC_METACLASS_$_NUAssetCapability
+ _OBJC_METACLASS_$_PIPhotographicStyle
+ _OBJC_METACLASS_$_PIPhotographicStyleApply
+ _OBJC_METACLASS_$_PIPhotographicStyleCapability
+ _OBJC_METACLASS_$_PIPhotographicStyleLearn
+ _OBJC_METACLASS_$_PIPosterOutfillSafetyRequest
+ _OBJC_METACLASS_$__PIAudioMixCapability
+ _OBJC_METACLASS_$__PICinematicVideoCapability
+ _OBJC_METACLASS_$__PIPhotographicStyleSettingsExpressionFunction
+ _OBJC_METACLASS_$__PIPortraitCapability
+ _OBJC_METACLASS_$__PIPosterOutfillSafetyResult
+ _PIAutoLoopStabilizedVideoGeometry
+ _PICinematicVideoVersionForAsset
+ _PIPhotographicStyleVersionForAsset
+ _PIPortraitVersionForAsset
+ __OBJC_$_CATEGORY_NUAssetCapability_$_PIPortrait
+ __OBJC_$_CLASS_METHODS_NUAssetCapability(PIPortrait|PIAudioMix|PICinematicVideo|PIPhotographicStyle)
+ __OBJC_$_CLASS_METHODS_PIPhotographicStyle
+ __OBJC_$_CLASS_METHODS_PIPhotographicStyleApply
+ __OBJC_$_CLASS_METHODS_PIPhotographicStyleCapability
+ __OBJC_$_CLASS_METHODS_PIPhotographicStyleLearn
+ __OBJC_$_CLASS_PROP_LIST_PIPhotographicStyle
+ __OBJC_$_CLASS_PROP_LIST_PIPhotographicStyleApply
+ __OBJC_$_CLASS_PROP_LIST_PIPhotographicStyleLearn
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyle
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyleApply
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyleCapability
+ __OBJC_$_INSTANCE_METHODS_PIPhotographicStyleLearn
+ __OBJC_$_INSTANCE_METHODS_PIPosterOutfillSafetyRequest(Guardrail)
+ __OBJC_$_INSTANCE_METHODS__PIAudioMixCapability
+ __OBJC_$_INSTANCE_METHODS__PICinematicVideoCapability
+ __OBJC_$_INSTANCE_METHODS__PIPhotographicStyleSettingsExpressionFunction
+ __OBJC_$_INSTANCE_METHODS__PIPortraitCapability
+ __OBJC_$_INSTANCE_METHODS__PIPosterOutfillSafetyResult
+ __OBJC_$_INSTANCE_VARIABLES_PIPhotographicStyle
+ __OBJC_$_INSTANCE_VARIABLES_PIPosterOutfillSafetyRequest
+ __OBJC_$_INSTANCE_VARIABLES__PIPosterOutfillSafetyResult
+ __OBJC_$_PROP_LIST_PIPhotographicStyle
+ __OBJC_$_PROP_LIST_PIPosterOutfillSafetyRequest
+ __OBJC_$_PROP_LIST_PIPosterOutfillSafetyResult
+ __OBJC_$_PROP_LIST__PIPosterOutfillSafetyResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PIPosterOutfillSafetyResult
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PIPosterOutfillSafetyResult
+ __OBJC_$_PROTOCOL_REFS_PIPosterOutfillSafetyResult
+ __OBJC_CLASS_PROTOCOLS_$_PIPhotographicStyle
+ __OBJC_CLASS_PROTOCOLS_$__PIPosterOutfillSafetyResult
+ __OBJC_CLASS_RO_$_PIPhotographicStyle
+ __OBJC_CLASS_RO_$_PIPhotographicStyleApply
+ __OBJC_CLASS_RO_$_PIPhotographicStyleCapability
+ __OBJC_CLASS_RO_$_PIPhotographicStyleLearn
+ __OBJC_CLASS_RO_$_PIPosterOutfillSafetyRequest
+ __OBJC_CLASS_RO_$__PIAudioMixCapability
+ __OBJC_CLASS_RO_$__PICinematicVideoCapability
+ __OBJC_CLASS_RO_$__PIPhotographicStyleSettingsExpressionFunction
+ __OBJC_CLASS_RO_$__PIPortraitCapability
+ __OBJC_CLASS_RO_$__PIPosterOutfillSafetyResult
+ __OBJC_LABEL_PROTOCOL_$_PIPosterOutfillSafetyResult
+ __OBJC_METACLASS_RO_$_PIPhotographicStyle
+ __OBJC_METACLASS_RO_$_PIPhotographicStyleApply
+ __OBJC_METACLASS_RO_$_PIPhotographicStyleCapability
+ __OBJC_METACLASS_RO_$_PIPhotographicStyleLearn
+ __OBJC_METACLASS_RO_$_PIPosterOutfillSafetyRequest
+ __OBJC_METACLASS_RO_$__PIAudioMixCapability
+ __OBJC_METACLASS_RO_$__PICinematicVideoCapability
+ __OBJC_METACLASS_RO_$__PIPhotographicStyleSettingsExpressionFunction
+ __OBJC_METACLASS_RO_$__PIPortraitCapability
+ __OBJC_METACLASS_RO_$__PIPosterOutfillSafetyResult
+ __OBJC_PROTOCOL_$_PIPosterOutfillSafetyResult
+ ___104+[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]_block_invoke
+ ___105+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]_block_invoke
+ ___105+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]_block_invoke_2
+ ___39-[PIPosterOutfillSafetyRequest submit:]_block_invoke
+ ___39-[PIPosterOutfillSafetyRequest submit:]_block_invoke_2
+ ___39-[PIPosterOutfillSafetyRequest submit:]_block_invoke_3
+ ___39-[PIPosterOutfillSafetyRequest submit:]_block_invoke_4
+ ___40+[PISpatialReframe adjustmentDescriptor]_block_invoke
+ ___45-[PISegmentationLoader _loadItem:completion:]_block_invoke_3
+ ___48-[PIParallaxSegmentationItem contentsDictionary]_block_invoke
+ ___58-[PISegmentationLoader _checkOutfillSafeEdges:completion:]_block_invoke
+ ___79-[PIPortraitLightingEffectV1Processor outputImageWithInputs:controlData:error:]_block_invoke
+ ___79-[PIPortraitLightingEffectV1Processor outputImageWithInputs:controlData:error:]_block_invoke_2
+ ___80+[PISegmentationLoader reloadSegmentationItemFromWallpaperURL:asset:completion:]_block_invoke_2
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSSet"8"NSError"16ls32l8
+ ___block_descriptor_57_e8_32s40bs_e20_v16?0"NUResponse"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e42_v24?0"<PISegmentationItem>"8"NSError"16ls32l8s40l8s48l8
+ ___swift_memcpy90_8
+ __swiftEmptySetSingleton
+ _adjustmentDescriptor.descriptor
+ _adjustmentDescriptor.onceToken
+ _swift_release_x21
+ _swift_retain_x19
+ _swift_task_create
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ShySo8NSNumberCG______pSgIeggg_ s5ErrorP
+ _symbolic So5NSSetCSo7NSErrorCSgIeyByy_
+ _symbolic So7CIImageC
+ _symbolic _____ySo8NSNumberCG s11_SetStorageC
+ _symbolic ytIeAgHr_
+ _type_layout_string So7CGPointV
- +[NUAssetCapability(PhotoImaging) audioMix]
- +[NUAssetCapability(PhotoImaging) cinematicVideoV1]
- +[NUAssetCapability(PhotoImaging) cinematicVideoV2]
- +[NUAssetCapability(PhotoImaging) photographicStyleV1]
- +[NUAssetCapability(PhotoImaging) photographicStyleV2]
- +[NUAssetCapability(PhotoImaging) photographicStyle]
- +[NUAssetCapability(PhotoImaging) portraitV1]
- +[NUAssetCapability(PhotoImaging) portraitV2]
- +[PIAssetLoader evaluateAssetCapabilities:]
- +[PIAssetLoader evaluateImageAssetCapabilities:]
- +[PIAssetLoader evaluateLivePhotoAssetCapabilities:]
- +[PIAssetLoader evaluateLivePhotoVideoAssetCapabilities:]
- +[PIAssetLoader evaluateVideoAssetCapabilities:]
- +[PIAssetLoader loadAsset:options:error:]
- +[PICleanup cleanupAdjustmentSchema]
- +[PIDefinition_v1 adjustmentSchema]
- +[PIDefinition_v1 identifier]
- +[PIGenerativeEdits identifier]
- +[PIGrain_v1 adjustmentSchema]
- +[PIGrain_v1 identifier]
- +[PIHighResolutionFusion_v1 adjustmentSchema]
- +[PIHighResolutionFusion_v1 identifier]
- +[PILevels_v1 adjustmentSchema]
- +[PILivePhotoEffect_v1 adjustmentSchema]
- +[PILivePhotoEffect_v1 flavorSetting]
- +[PILivePhotoEffect_v1 identifier]
- +[PILivePhotoEffect_v1 recipeSetting]
- +[PINoiseReduction_v1 adjustmentSchema]
- +[PINoiseReduction_v1 identifier]
- +[PIPhotographicStyleApplyV1 adjustmentFormat]
- +[PIPhotographicStyleLearnV1 adjustmentDescriptor]
- +[PIPhotographicStyleLearnV1 adjustmentFormat]
- +[PIPhotosPipeline_v1 addPhotographicStyleApplyV2ToPipeline:options:primaryInput:styleInput:adjustmentInput:assetMedia:error:]
- +[PIPhotosPipeline_v1 addPhotographicStyleLearnV2ToPipeline:options:primaryInput:adjustmentInput:assetMedia:error:]
- +[PIPhotosPipeline_v1 connectPhotographicStyleV2ToPipeline:name:primaryInput:adjustmentInput:assetMedia:isVideo:]
- +[PIRedEye_v1 adjustmentSchema]
- +[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]
- +[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]
- +[PISharpen_v1 adjustmentSchema]
- +[PISharpen_v1 identifier]
- +[PISmartBlackAndWhite_v1 adjustmentSchema]
- +[PISmartBlackAndWhite_v1 identifier]
- +[PISmartColor_v1 adjustmentSchema]
- +[PISmartColor_v1 identifier]
- +[PISmartCopyPaste identifier]
- +[PISmartCopyPaste pasteAdjustmentSchema]
- +[PISmartTone_v1 adjustmentSchema]
- +[PISmartTone_v1 identifier]
- +[PISmartTone_v1 statisticsSetting]
- +[PISpatialReframe adjustmentSchema]
- +[PISpatialReframe identifier]
- +[PIVignette_v1 adjustmentSchema]
- +[PIVignette_v1 identifier]
- +[_PISemanticStyleAdjustmentExpressionFunction adjustmentInfoDescriptor]
- -[PIPhotosPipeline_v0 _buildVideoPosterFramePipeline:format:sourceMedia:outputMedia:videoPosterFrameTime:]
- -[PIPhotosPipeline_v1 _buildVideoPosterFramePipeline:format:sourceMedia:outputMedia:videoPosterFrameTime:]
- -[PIPortraitLightingEffectV1Processor outputImageWithInputs:settings:error:]
- -[PISemanticStyleSettingsExpressionFunction evaluateWithArguments:error:]
- -[PISemanticStyleSettingsExpressionFunction format]
- -[_PISemanticStyleAdjustmentExpressionFunction evaluateWithArguments:error:]
- -[_PISemanticStyleAdjustmentExpressionFunction format]
- -[_PITextureStyleSettingsExpressionFunction evaluateWithArguments:error:]
- -[_PITextureStyleSettingsExpressionFunction format]
- GCC_except_table1134
- GCC_except_table1735
- GCC_except_table1749
- GCC_except_table1918
- GCC_except_table2093
- GCC_except_table2246
- GCC_except_table2256
- GCC_except_table2262
- GCC_except_table2270
- GCC_except_table2277
- GCC_except_table2285
- GCC_except_table2363
- GCC_except_table2403
- GCC_except_table2432
- GCC_except_table2437
- GCC_except_table2452
- GCC_except_table2468
- GCC_except_table2473
- GCC_except_table2479
- GCC_except_table2566
- GCC_except_table2798
- GCC_except_table3151
- GCC_except_table3156
- GCC_except_table3186
- GCC_except_table3190
- GCC_except_table3192
- GCC_except_table3193
- GCC_except_table3195
- GCC_except_table3197
- GCC_except_table3199
- GCC_except_table3210
- GCC_except_table3219
- GCC_except_table3314
- GCC_except_table3383
- GCC_except_table3384
- GCC_except_table3493
- GCC_except_table3535
- GCC_except_table3595
- GCC_except_table3809
- GCC_except_table3939
- GCC_except_table3942
- GCC_except_table3943
- GCC_except_table3955
- GCC_except_table4002
- GCC_except_table4011
- GCC_except_table4039
- GCC_except_table4063
- GCC_except_table4292
- GCC_except_table4464
- GCC_except_table4549
- GCC_except_table4650
- GCC_except_table4674
- GCC_except_table4678
- GCC_except_table4797
- GCC_except_table4835
- GCC_except_table4841
- GCC_except_table4843
- GCC_except_table4867
- GCC_except_table4889
- GCC_except_table4993
- GCC_except_table505
- GCC_except_table5050
- GCC_except_table5090
- GCC_except_table5242
- GCC_except_table5265
- GCC_except_table5275
- GCC_except_table5286
- GCC_except_table5293
- GCC_except_table5440
- GCC_except_table5532
- GCC_except_table5593
- GCC_except_table5596
- GCC_except_table5608
- GCC_except_table5609
- GCC_except_table5613
- GCC_except_table5614
- GCC_except_table5615
- GCC_except_table5620
- GCC_except_table5628
- GCC_except_table5722
- GCC_except_table6111
- GCC_except_table6130
- GCC_except_table6131
- GCC_except_table6137
- GCC_except_table6142
- GCC_except_table6194
- GCC_except_table6199
- GCC_except_table6200
- GCC_except_table6210
- GCC_except_table6212
- GCC_except_table6236
- GCC_except_table6238
- GCC_except_table6239
- GCC_except_table6240
- GCC_except_table6242
- GCC_except_table6244
- GCC_except_table6246
- GCC_except_table6249
- GCC_except_table6252
- GCC_except_table6254
- GCC_except_table6255
- GCC_except_table6256
- GCC_except_table6257
- GCC_except_table6259
- GCC_except_table6264
- GCC_except_table6400
- GCC_except_table6403
- GCC_except_table6410
- GCC_except_table6470
- GCC_except_table6544
- GCC_except_table6865
- GCC_except_table7113
- GCC_except_table7114
- GCC_except_table7204
- GCC_except_table7207
- GCC_except_table7211
- GCC_except_table7212
- GCC_except_table7216
- GCC_except_table7217
- GCC_except_table7219
- GCC_except_table7225
- GCC_except_table7234
- GCC_except_table7301
- GCC_except_table7353
- GCC_except_table7354
- GCC_except_table7355
- GCC_except_table7356
- GCC_except_table7391
- GCC_except_table7459
- GCC_except_table7469
- GCC_except_table7573
- GCC_except_table7626
- GCC_except_table7628
- GCC_except_table7722
- GCC_except_table7728
- GCC_except_table7731
- GCC_except_table7733
- GCC_except_table7734
- GCC_except_table7735
- GCC_except_table7736
- GCC_except_table7738
- GCC_except_table7741
- GCC_except_table7742
- GCC_except_table7743
- GCC_except_table7744
- GCC_except_table7746
- GCC_except_table7747
- GCC_except_table7749
- GCC_except_table7750
- GCC_except_table7751
- GCC_except_table7752
- GCC_except_table780
- GCC_except_table7807
- GCC_except_table7815
- GCC_except_table7829
- GCC_except_table7830
- GCC_except_table7831
- GCC_except_table7867
- GCC_except_table7870
- GCC_except_table7873
- GCC_except_table791
- GCC_except_table7918
- GCC_except_table7920
- GCC_except_table801
- GCC_except_table8064
- GCC_except_table8074
- GCC_except_table8081
- GCC_except_table8082
- GCC_except_table8083
- GCC_except_table8084
- GCC_except_table8085
- GCC_except_table8086
- GCC_except_table8087
- GCC_except_table8131
- GCC_except_table8317
- GCC_except_table832
- GCC_except_table8543
- GCC_except_table8545
- GCC_except_table8546
- GCC_except_table8608
- GCC_except_table8610
- GCC_except_table8612
- GCC_except_table8682
- GCC_except_table8705
- GCC_except_table8707
- GCC_except_table8710
- GCC_except_table8714
- GCC_except_table8716
- GCC_except_table8732
- GCC_except_table8749
- GCC_except_table8757
- GCC_except_table8761
- GCC_except_table8770
- GCC_except_table8780
- GCC_except_table8781
- GCC_except_table8784
- GCC_except_table8786
- GCC_except_table8790
- GCC_except_table8793
- GCC_except_table8805
- GCC_except_table889
- GCC_except_table892
- _OBJC_CLASS_$_NUAdjustmentSchema
- _OBJC_CLASS_$_PIAssetLoader
- _OBJC_CLASS_$_PISemanticStyleSettingsExpressionFunction
- _OBJC_CLASS_$__PISemanticStyleAdjustmentExpressionFunction
- _OBJC_CLASS_$__PITextureStyleSettingsExpressionFunction
- _OBJC_IVAR_$_PIParallaxSegmentationItem.outfillSafeEdges
- _OBJC_METACLASS_$_NUAssetLoader
- _OBJC_METACLASS_$_PIAssetLoader
- _OBJC_METACLASS_$_PISemanticStyleSettingsExpressionFunction
- _OBJC_METACLASS_$__PISemanticStyleAdjustmentExpressionFunction
- _OBJC_METACLASS_$__PITextureStyleSettingsExpressionFunction
- __OBJC_$_CATEGORY_CLASS_METHODS_NUAssetCapability_$_PhotoImaging
- __OBJC_$_CATEGORY_NUAssetCapability_$_PhotoImaging
- __OBJC_$_CLASS_METHODS_PIAssetLoader
- __OBJC_$_CLASS_METHODS_PIPhotographicStyleApplyV1
- __OBJC_$_CLASS_METHODS_PIPhotographicStyleLearnV1
- __OBJC_$_CLASS_METHODS__PISemanticStyleAdjustmentExpressionFunction
- __OBJC_$_CLASS_PROP_LIST_NUAssetCapability_$_PhotoImaging
- __OBJC_$_CLASS_PROP_LIST_PIPhotographicStyleApplyV1
- __OBJC_$_CLASS_PROP_LIST_PIPhotographicStyleLearnV1
- __OBJC_$_INSTANCE_METHODS_PISemanticStyleSettingsExpressionFunction
- __OBJC_$_INSTANCE_METHODS__PISemanticStyleAdjustmentExpressionFunction
- __OBJC_$_INSTANCE_METHODS__PITextureStyleSettingsExpressionFunction
- __OBJC_CLASS_RO_$_PIAssetLoader
- __OBJC_CLASS_RO_$_PISemanticStyleSettingsExpressionFunction
- __OBJC_CLASS_RO_$__PISemanticStyleAdjustmentExpressionFunction
- __OBJC_CLASS_RO_$__PITextureStyleSettingsExpressionFunction
- __OBJC_METACLASS_RO_$_PIAssetLoader
- __OBJC_METACLASS_RO_$_PISemanticStyleSettingsExpressionFunction
- __OBJC_METACLASS_RO_$__PISemanticStyleAdjustmentExpressionFunction
- __OBJC_METACLASS_RO_$__PITextureStyleSettingsExpressionFunction
- ___36+[PISpatialReframe adjustmentSchema]_block_invoke
- ___76-[PIPortraitLightingEffectV1Processor outputImageWithInputs:settings:error:]_block_invoke
- ___76-[PIPortraitLightingEffectV1Processor outputImageWithInputs:settings:error:]_block_invoke_2
- ___89+[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]_block_invoke
- ___90+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]_block_invoke
- ___90+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]_block_invoke_2
- ___swift_memcpy89_8
- _adjustmentSchema.onceToken
- _adjustmentSchema.schema
- _type_layout_string So6CGSizeV
CStrings:
+ "+[PIPhotographicStyle connectPhotographicStyleToPipeline:stylePipeline:primaryInput:adjustmentInput:assetMedia:isVideo:]"
+ "+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]"
+ "+[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:displayContext:completion:]"
+ "-[PIPhotographicStyle _versionedClassForAsset:]"
+ "-[PIPhotographicStyle buildPipeline:error:]"
+ "-[PIPhotographicStyle initWithAsset:options:]"
+ "-[PIPhotographicStyle init]"
+ "-[PIPhotographicStyle versionedClassForAsset:]"
+ "-[PIPortraitLightingEffectV1Processor outputImageWithInputs:controlData:error:]"
+ "-[PIPosterOutfillSafetyRequest initWithSegmentationItem:]"
+ "-[_PIPhotographicStyleSettingsExpressionFunction evaluateWithArguments:error:]"
+ "..:<optimizeForExport"
+ "/:<adjustment.effect"
+ "/:<cropGeometry"
+ "/:<optimizeForExport"
+ "/:<photographicStyle"
+ "/:<photographicStyle.enabled"
+ "/:<photographicStyle.texture.enabled"
+ "/:>defaultPhotographicStyle"
+ "/:adjustment.cast"
+ "/:adjustment.color"
+ "/:adjustment.enabled"
+ "/:adjustment.texture"
+ "/:adjustment.tone"
+ "/:defaultPhotographicStyle"
+ "/:photographicStyle"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Adjustments/PISemanticStyle.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Parallax/PIPosterOutfillSafetyRequest.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/API/PIPhotographicStyle.m"
+ ":adjustment.cast"
+ ":adjustment.color"
+ ":adjustment.intensity"
+ ":adjustment.tone"
+ "Asset does not support photographic styles"
+ "Asset does not support texture styles"
+ "Asset must be portrait capable"
+ "CinematicVideo"
+ "Debug.Unused"
+ "Failed to add photographicStyleLearn pipeline"
+ "Failed to setup crop geometry pipeline"
+ "HighResolutionFusion.Alignment"
+ "NSDictionary * _Nonnull PISemanticStyleSettingsFromMakerNoteProperties(NSDictionary *__strong _Nonnull)"
+ "NUImageGeometry * _Nonnull PIAutoLoopStabilizedVideoGeometry(NUPixelRect, NUOrientation, NUScale)"
+ "NUOrientationIsValid(outputOrientation)"
+ "No edge cleared by the outfill guardrail, disabling outfill"
+ "Outfill guardrail failed, disabling outfill: %{public}@"
+ "OutfillSafety"
+ "PICleanupMaskIdentifier"
+ "PICleanupModelVersion"
+ "PILivePhotoEffectRecipe"
+ "PIRedEyeCorrectionInfo"
+ "Portrait"
+ "Portrait layout has an unrenderable visible frame %.4f,%.4f %.4fx%.4f in image %.0fx%.0f for screen %.0fx%.0f"
+ "RAW.Value"
+ "Refusing to save layer stack for display %{public}@: %{public}@"
+ "SmartColorStatistics"
+ "SmartToneLightMap"
+ "Spatial photo layers are missing from the generated layer stack"
+ "Unexpected failure - asset capable of styles but neither v1 nor v2"
+ "[asset hasCapability:NUAssetCapability.photographicStyle]"
+ "_PIPhotographicStyleSettingsExpressionFunction"
+ "adjustment.cast"
+ "adjustment.color"
+ "adjustment.intensity"
+ "adjustment.texture.enabled"
+ "adjustment.tone"
+ "adjustmentInput != nil"
+ "assetMedia != nil"
+ "cropGeometry"
+ "cropGeometry:<adjustment"
+ "cropGeometry:<media"
+ "cropGeometry:>media"
+ "defaultPhotographicStyle"
+ "earsMatte"
+ "eyebrowsMatte"
+ "faceSkinMatte"
+ "filter:<adjustment"
+ "filter:<primary"
+ "filter:>primary"
+ "glassesMatteV2"
+ "hairMatte"
+ "handsMatte"
+ "lightingEffectV1:<optimizeForExport"
+ "lightingEffectV2:<optimizeForExport"
+ "lipsMatte"
+ "nonFaceSkinMatte"
+ "noseMatte"
+ "optimizeForExport"
+ "outfillSafeEdges"
+ "outfillSafety"
+ "outfillSafetyThreshold"
+ "personInstances"
+ "personMatte"
+ "photograhicStyleRevertBypass"
+ "photographicStyle"
+ "photographicStyleApply:<adjustment"
+ "photographicStyleApply:<style"
+ "photographicStyleLPFXBypass"
+ "photographicStyleLearn:<adjustment"
+ "photographicStyleLearn:<linearThumbnail"
+ "photographicStyleLearn:<portraitMatte"
+ "photographicStyleLearn:<primary"
+ "photographicStyleLearn:<skinMatte"
+ "photographicStyleLearn:<skyMatte"
+ "photographicStyleLearn:>default"
+ "photographicStyleLearn:default"
+ "photographicStyleRevertBypass"
+ "portrait:<%@"
+ "portrait:<debugPortraitInfo"
+ "portrait:<optimizeForExport"
+ "primaryInput != nil"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "requiresCenteredSubject"
+ "semanticStyleApply:adjustment.cast"
+ "semanticStyleApply:adjustment.color"
+ "semanticStyleApply:adjustment.enabled"
+ "semanticStyleApply:adjustment.intensity"
+ "semanticStyleApply:adjustment.tone"
+ "skinMatteV2"
+ "stylePipeline != nil"
+ "tattooMatte"
+ "teethMatteV2"
+ "texture"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
- "+[PICleanup cleanupAdjustmentSchema]"
- "+[PISegmentationLoader _renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]"
- "+[PISegmentationLoader renderPreviewLayerStackFromWallpaperURL:styleCategory:completion:]"
- "-[PIPortraitLightingEffectV1Processor outputImageWithInputs:settings:error:]"
- "-[PISemanticStyleSettingsExpressionFunction evaluateWithArguments:error:]"
- "-[_PISemanticStyleAdjustmentExpressionFunction evaluateWithArguments:error:]"
- "-[_PITextureStyleSettingsExpressionFunction evaluateWithArguments:error:]"
- "..:<oneShot"
- "/"
- "/:<adjustment.kind"
- "/:<crop"
- "/:<enablePortraitOneShot"
- "/:<semanticStyle"
- "/:<semanticStyle.enabled"
- "/:<textureStyle.enabled"
- "/:>defaultSemanticStyle"
- "/:defaultSemanticStyle"
- "/:defaultTextureStyle"
- "/:semanticStyleAdjustment"
- "/:semanticStyleAdjustment.cast"
- "/:semanticStyleAdjustment.color"
- "/:textureStyleAdjustment"
- "/image/portrait:<oneShot"
- "/portrait:<oneShot"
- "/video/semanticStyleLearn:>style"
- "/video/semanticStyleLearn:style"
- ":<adjustment.version"
- ":<semanticStyleAdjustment.cast"
- ":<semanticStyleAdjustment.color"
- ":<semanticStyleAdjustment.intensity"
- ":<semanticStyleAdjustment.tone"
- ":<semanticStyleAdjustment.version"
- ":>defaultSemanticStyle"
- ":>defaultTextureStyle"
- ":adjustment"
- ":earsMatte"
- ":eyebrowsMatte"
- ":faceInfoTimedMetadata"
- ":faceSkinMatte"
- ":glassesMatteV2"
- ":hairMatte"
- ":handsMatte"
- ":linearThumbnail"
- ":lipsMatte"
- ":nonFaceSkinMatte"
- ":noseMatte"
- ":personInstances"
- ":personMatte"
- ":semanticStyle"
- ":semanticStyleAdjustment"
- ":semanticStyleCast"
- ":semanticStyleColor"
- ":semanticStyleTimedMetadata"
- ":skinMatteV2"
- ":style"
- ":tattooMatte"
- ":teethMatteV2"
- ":textureStyle"
- ":textureStyleAdjustment"
- ":textureStyleTimedMetadata"
- "CinematicVideoV1"
- "CinematicVideoV2"
- "Failed to add SemanticStyleLearn pipeline"
- "Failed to add texture style apply pipeline"
- "Failed to add texture style learn pipeline"
- "Failed to build photographicStyleApply pipeline"
- "Failed to build photographicStyleLearn pipeline"
- "Failed to deserialize schema %@: %@"
- "Failed to setup crop/straighten pipeline"
- "Invalid semantic style adjustment"
- "Missing semantic style adjustment"
- "PISemanticStyleSettingsExpressionFunction"
- "PhotographicStyleV1"
- "PhotographicStyleV2"
- "Portrait layout has an empty visible frame"
- "PortraitV1"
- "SmartCopyPaste"
- "SpatialReframe"
- "_PISemanticStyleAdjustmentExpressionFunction"
- "_PITextureStyleSettingsExpressionFunction"
- "com.apple.photos"
- "crop:<adjustment"
- "defaultSemanticStyle"
- "defaultTextureStyle"
- "enablePortraitOneShot"
- "filterEffect:<adjustment"
- "filterEffect:<primary"
- "filterEffect:>primary"
- "learn:<version"
- "lightingEffectV1:<oneShot"
- "lightingEffectV2:<oneShot"
- "oneShot"
- "photographicStyleLearn:defaultSemanticStyle"
- "photographicStyleLearn:defaultTextureStyle"
- "portrait:<glassesMatte"
- "portrait:<hairMatte"
- "portrait:<portraitMatte"
- "portrait:<skinMatte"
- "portrait:<teethMatte"
- "semanticStyleAdjustment"
- "semanticStyleAdjustment.cast"
- "semanticStyleAdjustment.color"
- "semanticStyleAdjustment.enabled"
- "semanticStyleAdjustment.intensity"
- "semanticStyleAdjustment.tone"
- "semanticStyleAdjustment.version"
- "semanticStyleApply:<adjustment"
- "semanticStyleApply:<primary"
- "semanticStyleApply:<style"
- "semanticStyleApply:>primary"
- "semanticStyleApply:adjustment"
- "semanticStyleLPFXBypass"
- "semanticStyleLearn:<adjustment"
- "semanticStyleLearn:<linearThumbnail"
- "semanticStyleLearn:<portraitMatte"
- "semanticStyleLearn:<primary"
- "semanticStyleLearn:<skinMatte"
- "semanticStyleLearn:<skyMatte"
- "semanticStyleLearn:>default"
- "semanticStyleLearn:>style"
- "semanticStyleLearn:default"
- "semanticStyleRevertBypass"
- "semanticStyleTarget:version"
- "target:<version"
- "textureStyleAdjustment"
- "textureStyleAdjustment.enabled"
- "textureStyleTarget:>default"
- "thumbnail:<version"
- "thumbnail:version"
```
