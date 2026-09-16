## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-912.0.235.0.0
-  __TEXT.__text: 0x292768
+916.40.110.0.0
+  __TEXT.__text: 0x293d64
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x173c8
+  __TEXT.__objc_methlist: 0x17340
   __TEXT.__const: 0x8d04
   __TEXT.__dlopen_cstrs: 0x2a2
   __TEXT.__swift5_typeref: 0x2d8
-  __TEXT.__cstring: 0x4a6de
+  __TEXT.__cstring: 0x4aabd
   __TEXT.__constg_swiftt: 0x230
   __TEXT.__swift5_reflstr: 0x35f
   __TEXT.__swift5_fieldmd: 0x3d4
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__oslogstring: 0x7d58
+  __TEXT.__oslogstring: 0x7db1
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_capture: 0x50
   __TEXT.__gcc_except_tab: 0x4ee0
-  __TEXT.__unwind_info: 0x6ed8
+  __TEXT.__unwind_info: 0x6e98
   __TEXT.__eh_frame: 0xa60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x44d0
+  __DATA_CONST.__const: 0x4490
   __DATA_CONST.__objc_classlist: 0x11a0
-  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbca0
+  __DATA_CONST.__objc_selrefs: 0xbd10
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x750
-  __DATA_CONST.__objc_arraydata: 0x9718
-  __DATA_CONST.__got: 0x2830
-  __AUTH_CONST.__const: 0x5648
-  __AUTH_CONST.__cfstring: 0x29bc0
-  __AUTH_CONST.__objc_const: 0x29ad0
+  __DATA_CONST.__objc_arraydata: 0x9518
+  __DATA_CONST.__got: 0x2810
+  __AUTH_CONST.__const: 0x5628
+  __AUTH_CONST.__cfstring: 0x29ea0
+  __AUTH_CONST.__objc_const: 0x29c40
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x1668
-  __AUTH_CONST.__objc_dictobj: 0x5c58
+  __AUTH_CONST.__objc_dictobj: 0x5b90
   __AUTH_CONST.__objc_doubleobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0xd0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9495
-  Symbols:   21410
-  CStrings:  7578
+  Functions: 9484
+  Symbols:   21401
+  CStrings:  7602
 
Symbols:
+ +[NUAssetCapability(PhotoImaging) audioMix]
+ +[NUAssetCapability(PhotoImaging) cinematicVideoV1]
+ +[NUAssetCapability(PhotoImaging) cinematicVideoV2]
+ +[NUAssetCapability(PhotoImaging) photographicStyleV1]
+ +[NUAssetCapability(PhotoImaging) photographicStyleV2]
+ +[NUAssetCapability(PhotoImaging) photographicStyle]
+ +[NUAssetCapability(PhotoImaging) portraitV1]
+ +[NUAssetCapability(PhotoImaging) portraitV2]
+ +[PIObjectRemoval _instancesForGenerativeEditOperation:context:]
+ +[PIObjectRemoval _nonInstancedOperationsFromComposition:context:]
+ +[PIObjectRemoval _tightImageSpaceBoundsForGenerativeEditOperation:composition:context:error:]
+ +[PIPhotosPipeline pipelineName]
+ +[PIPrivatePhotosPipeline pipelineName]
+ +[PISegmentationLoader _baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:settlingEffectEnabled:]
+ -[PIADMCleanup pipelineName]
+ -[PIADMOutfill pipelineName]
+ -[PIAudioMix_v1 pipelineName]
+ -[PICinematicVideo_v1 pipelineName]
+ -[PICinematicVideo_v2 pipelineName]
+ -[PICleanup pipelineName]
+ -[PICropStraightenAuto_v1 pipelineName]
+ -[PICropStraighten_v1 pipelineName]
+ -[PICurves_v1 pipelineName]
+ -[PIDefinition_v1 pipelineName]
+ -[PIFilterEffect_v1 pipelineName]
+ -[PIGANCleanup pipelineName]
+ -[PIGenerativeEdits pipelineName]
+ -[PIGlobalSettings generativeSeed]
+ -[PIGlobalSettings setGenerativeSeed:]
+ -[PIGrain_v1 pipelineName]
+ -[PIHighResolutionFusion_v1 pipelineName]
+ -[PIInpaintMaskContext setRequestID:]
+ -[PILevels_v1 pipelineName]
+ -[PILivePhotoEffect_v1 pipelineName]
+ -[PILivePhotoKeyFrame_v1 pipelineName]
+ -[PIManualRedEye_v1 pipelineName]
+ -[PIMute_v1 pipelineName]
+ -[PINoiseReduction_v1 pipelineName]
+ -[PIOrientation_v1 pipelineName]
+ -[PIOutfillPlaceholder pipelineName]
+ -[PIPhotographicStyleApplyV1 pipelineName]
+ -[PIPhotographicStyleApplyV2 pipelineName]
+ -[PIPhotographicStyleLearnV1 pipelineName]
+ -[PIPhotographicStyleLearnV2 pipelineName]
+ -[PIPhotosPipeline pipelineIsOpaque]
+ -[PIPhotosPipeline pipelineName]
+ -[PIPhotosPipeline_v1 _buildPostGeometryPipeline:media:error:]
+ -[PIPipelineModule pipelineName]
+ -[PIPlaybackRate_v1 pipelineName]
+ -[PIPortrait_v1 pipelineName]
+ -[PIPortrait_v2 pipelineName]
+ -[PIPrivatePhotosPipeline_v0 buildFiltersGroupPipeline:temporality:outputMediaFormat:error:]
+ -[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:format:temporality:connections:error:]
+ -[PIPrivatePhotosPipeline_v1 buildFiltersGroupPipeline:temporality:outputMediaFormat:error:]
+ -[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:format:temporality:connections:error:]
+ -[PIRedEye_v1 pipelineName]
+ -[PIRetouchCleanup pipelineName]
+ -[PISelectiveColor_v1 pipelineName]
+ -[PISemanticStyleThumbnailApply pipelineName]
+ -[PISharpen_v1 pipelineName]
+ -[PISlowMotion_v1 pipelineName]
+ -[PISmartBlackAndWhite_v1 pipelineName]
+ -[PISmartColor_v1 pipelineName]
+ -[PISmartCopyPaste pipelineName]
+ -[PISmartToneAuto_v1 pipelineName]
+ -[PISmartTone_v1 pipelineName]
+ -[PISpatialReframe pipelineName]
+ -[PITextureStyle pipelineName]
+ -[PITrim_v1 pipelineName]
+ -[PIVignette_v1 pipelineName]
+ -[PIWhiteBalanceAuto_v1 pipelineName]
+ -[PIWhiteBalance_v1 pipelineName]
+ -[_PIGrayColorPipelineBuilder pipelineName]
+ GCC_except_table1114
+ GCC_except_table1715
+ GCC_except_table1729
+ GCC_except_table1898
+ GCC_except_table2073
+ GCC_except_table2226
+ GCC_except_table2236
+ GCC_except_table2242
+ GCC_except_table2250
+ GCC_except_table2257
+ GCC_except_table2265
+ GCC_except_table2343
+ GCC_except_table2383
+ GCC_except_table2412
+ GCC_except_table2417
+ GCC_except_table2432
+ GCC_except_table2448
+ GCC_except_table2453
+ GCC_except_table2459
+ GCC_except_table2546
+ GCC_except_table316
+ GCC_except_table3789
+ GCC_except_table3908
+ GCC_except_table3918
+ GCC_except_table3921
+ GCC_except_table3934
+ GCC_except_table394
+ GCC_except_table3981
+ GCC_except_table3990
+ GCC_except_table4018
+ GCC_except_table4271
+ GCC_except_table4443
+ GCC_except_table4528
+ GCC_except_table4629
+ GCC_except_table4653
+ GCC_except_table4657
+ GCC_except_table4776
+ GCC_except_table4814
+ GCC_except_table4820
+ GCC_except_table4822
+ GCC_except_table4846
+ GCC_except_table4868
+ GCC_except_table4972
+ GCC_except_table5029
+ GCC_except_table505
+ GCC_except_table5069
+ GCC_except_table5221
+ GCC_except_table5244
+ GCC_except_table5251
+ GCC_except_table5254
+ GCC_except_table5265
+ GCC_except_table5272
+ GCC_except_table5419
+ GCC_except_table5511
+ GCC_except_table5572
+ GCC_except_table5575
+ GCC_except_table5587
+ GCC_except_table5588
+ GCC_except_table5594
+ GCC_except_table5607
+ GCC_except_table5701
+ GCC_except_table6090
+ GCC_except_table6109
+ GCC_except_table6110
+ GCC_except_table6116
+ GCC_except_table6121
+ GCC_except_table6173
+ GCC_except_table6178
+ GCC_except_table6179
+ GCC_except_table6189
+ GCC_except_table6191
+ GCC_except_table6215
+ GCC_except_table6217
+ GCC_except_table6219
+ GCC_except_table6223
+ GCC_except_table6225
+ GCC_except_table6233
+ GCC_except_table6235
+ GCC_except_table6243
+ GCC_except_table6276
+ GCC_except_table6378
+ GCC_except_table6381
+ GCC_except_table6446
+ GCC_except_table6520
+ GCC_except_table6841
+ GCC_except_table7089
+ GCC_except_table7090
+ GCC_except_table7180
+ GCC_except_table7183
+ GCC_except_table7187
+ GCC_except_table7188
+ GCC_except_table7192
+ GCC_except_table7195
+ GCC_except_table7210
+ GCC_except_table7226
+ GCC_except_table7277
+ GCC_except_table7329
+ GCC_except_table7330
+ GCC_except_table7331
+ GCC_except_table7332
+ GCC_except_table7364
+ GCC_except_table7367
+ GCC_except_table7435
+ GCC_except_table7445
+ GCC_except_table7549
+ GCC_except_table7602
+ GCC_except_table7604
+ GCC_except_table7698
+ GCC_except_table7704
+ GCC_except_table7707
+ GCC_except_table7709
+ GCC_except_table7710
+ GCC_except_table7712
+ GCC_except_table7720
+ GCC_except_table7722
+ GCC_except_table7723
+ GCC_except_table7728
+ GCC_except_table7783
+ GCC_except_table7791
+ GCC_except_table7805
+ GCC_except_table7806
+ GCC_except_table7807
+ GCC_except_table782
+ GCC_except_table7841
+ GCC_except_table7842
+ GCC_except_table7843
+ GCC_except_table7846
+ GCC_except_table7894
+ GCC_except_table7896
+ GCC_except_table793
+ GCC_except_table803
+ GCC_except_table8040
+ GCC_except_table8050
+ GCC_except_table8058
+ GCC_except_table8059
+ GCC_except_table8060
+ GCC_except_table8061
+ GCC_except_table8062
+ GCC_except_table8063
+ GCC_except_table8107
+ GCC_except_table823
+ GCC_except_table8293
+ GCC_except_table8519
+ GCC_except_table8521
+ GCC_except_table8522
+ GCC_except_table8584
+ GCC_except_table8586
+ GCC_except_table8588
+ GCC_except_table8658
+ GCC_except_table8681
+ GCC_except_table8683
+ GCC_except_table8686
+ GCC_except_table869
+ GCC_except_table8690
+ GCC_except_table8692
+ GCC_except_table8708
+ GCC_except_table872
+ GCC_except_table8725
+ GCC_except_table873
+ GCC_except_table8737
+ GCC_except_table8738
+ GCC_except_table8756
+ GCC_except_table8757
+ GCC_except_table8760
+ GCC_except_table8762
+ GCC_except_table8766
+ GCC_except_table8769
+ GCC_except_table8781
+ _NUChannelNameAlternate
+ _OBJC_CLASS_$_NUAssetCapability
+ __OBJC_$_CATEGORY_CLASS_METHODS_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_CATEGORY_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_CLASS_PROP_LIST_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NUPipelineBuilder
+ ___64+[PIObjectRemoval _instancesForGenerativeEditOperation:context:]_block_invoke
+ ___66+[PIObjectRemoval _nonInstancedOperationsFromComposition:context:]_block_invoke
+ ___66+[PIObjectRemoval _nonInstancedOperationsFromComposition:context:]_block_invoke_2
+ ___67-[PIPhotosPipeline_v0 buildPipeline:assetMedia:outputFormat:error:]_block_invoke_3
+ ___88-[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:format:temporality:connections:error:]_block_invoke
+ ___88-[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:format:temporality:connections:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e29_v16?0"<NUMutablePipeline>"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e37_"NUChannelPortSpec"16?0"NSString"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8ls32l8s40l8s48l8s56l8
+ _objc_msgSend$HDR
+ _objc_msgSend$_baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:settlingEffectEnabled:
+ _objc_msgSend$_buildPostGeometryPipeline:media:error:
+ _objc_msgSend$_instancesForGenerativeEditOperation:context:
+ _objc_msgSend$_nonInstancedOperationsFromComposition:context:
+ _objc_msgSend$_tightImageSpaceBoundsForGenerativeEditOperation:composition:context:error:
+ _objc_msgSend$buildFiltersGroupPipeline:temporality:outputMediaFormat:error:
+ _objc_msgSend$buildFiltersPipeline:format:temporality:connections:error:
+ _objc_msgSend$canApplySideroom
+ _objc_msgSend$cinematicVideoV1
+ _objc_msgSend$cinematicVideoV2
+ _objc_msgSend$generativeSeed
+ _objc_msgSend$hdrGainMap
+ _objc_msgSend$photographicStyle
+ _objc_msgSend$photographicStyleV1
+ _objc_msgSend$photographicStyleV2
+ _objc_msgSend$pipelineName
+ _objc_msgSend$portraitV1
+ _objc_msgSend$portraitV2
+ _objc_msgSend$rawDecode
+ _objc_msgSend$requestID
+ _objc_msgSend$setRequestID:
+ _objc_msgSend$start
- +[PIADMCleanup identifier]
- +[PIADMOutfill identifier]
- +[PIAudioMix_v1 identifier]
- +[PICinematicVideo_v1 identifier]
- +[PICinematicVideo_v2 identifier]
- +[PICropStraightenAuto_v1 identifier]
- +[PICropStraighten_v1 identifier]
- +[PIFilterEffect_v1 identifier]
- +[PIGANCleanup identifier]
- +[PILivePhotoKeyFrame_v1 identifier]
- +[PIMute_v1 identifier]
- +[PIObjectRemoval _instancesForGenerativeEditOperation:]
- +[PIObjectRemoval _nonInstancedOperationsFromComposition:]
- +[PIObjectRemoval _tightImageSpaceBoundsForGenerativeEditOperation:composition:error:]
- +[PIOrientation_v1 identifier]
- +[PIOutfillPlaceholder identifier]
- +[PIPhotographicStyleLearnV2 identifier]
- +[PIPhotosPipeline pipelineIdentifier]
- +[PIPlaybackRate_v1 identifier]
- +[PIPrivatePhotosPipeline pipelineIdentifier]
- +[PIRetouchCleanup identifier]
- +[PISegmentationLoader _baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:]
- +[PISlowMotion_v1 identifier]
- +[PISmartToneAuto_v1 identifier]
- +[PITextureStyle identifier]
- +[PITrim_v1 identifier]
- +[PIWhiteBalance_v1 identifier]
- -[PIADMCleanup identifier]
- -[PIADMOutfill identifier]
- -[PIAudioMix_v1 identifier]
- -[PICinematicVideo_v1 identifier]
- -[PICinematicVideo_v2 identifier]
- -[PICleanup identifier]
- -[PICropStraightenAuto_v1 identifier]
- -[PICropStraighten_v1 identifier]
- -[PICurves_v1 identifier]
- -[PIDefinition_v1 identifier]
- -[PIFilterEffect_v1 identifier]
- -[PIGANCleanup identifier]
- -[PIGenerativeEdits identifier]
- -[PIGrain_v1 identifier]
- -[PIHighResolutionFusion_v1 identifier]
- -[PILevels_v1 identifier]
- -[PILivePhotoEffect_v1 identifier]
- -[PILivePhotoKeyFrame_v1 identifier]
- -[PIManualRedEye_v1 identifier]
- -[PIMute_v1 identifier]
- -[PINoiseReduction_v1 identifier]
- -[PIOrientation_v1 identifier]
- -[PIOutfillPlaceholder identifier]
- -[PIPhotographicStyleApplyV1 identifier]
- -[PIPhotographicStyleApplyV2 identifier]
- -[PIPhotographicStyleLearnV1 identifier]
- -[PIPhotographicStyleLearnV2 identifier]
- -[PIPhotosPipeline identifier]
- -[PIPhotosPipeline_v1 _buildPostGeometryPipeline:error:]
- -[PIPipelineModule identifier]
- -[PIPlaybackRate_v1 identifier]
- -[PIPortrait_v1 identifier]
- -[PIPortrait_v2 identifier]
- -[PIPrivatePhotosPipeline_v0 buildFiltersGroupPipeline:temporality:error:]
- -[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:temporality:connections:error:]
- -[PIPrivatePhotosPipeline_v1 buildFiltersGroupPipeline:temporality:error:]
- -[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:temporality:connections:error:]
- -[PIRedEye_v1 identifier]
- -[PIRetouchCleanup identifier]
- -[PISelectiveColor_v1 identifier]
- -[PISemanticStyleThumbnailApply identifier]
- -[PISharpen_v1 identifier]
- -[PISlowMotion_v1 identifier]
- -[PISmartBlackAndWhite_v1 identifier]
- -[PISmartColor_v1 identifier]
- -[PISmartCopyPaste identifier]
- -[PISmartToneAuto_v1 identifier]
- -[PISmartTone_v1 identifier]
- -[PISpatialReframe identifier]
- -[PITextureStyle identifier]
- -[PITrim_v1 identifier]
- -[PIVignette_v1 identifier]
- -[PIWhiteBalanceAuto_v1 identifier]
- -[PIWhiteBalance_v1 identifier]
- -[_PIGrayColorPipelineBuilder identifier]
- GCC_except_table1108
- GCC_except_table1710
- GCC_except_table1724
- GCC_except_table1893
- GCC_except_table2069
- GCC_except_table2223
- GCC_except_table2233
- GCC_except_table2239
- GCC_except_table2247
- GCC_except_table2254
- GCC_except_table2262
- GCC_except_table2340
- GCC_except_table2380
- GCC_except_table2409
- GCC_except_table2414
- GCC_except_table2429
- GCC_except_table2445
- GCC_except_table2450
- GCC_except_table2456
- GCC_except_table2543
- GCC_except_table309
- GCC_except_table3790
- GCC_except_table387
- GCC_except_table3909
- GCC_except_table3919
- GCC_except_table3923
- GCC_except_table3935
- GCC_except_table3982
- GCC_except_table3991
- GCC_except_table4019
- GCC_except_table4272
- GCC_except_table4445
- GCC_except_table4531
- GCC_except_table4634
- GCC_except_table4658
- GCC_except_table4662
- GCC_except_table4781
- GCC_except_table4819
- GCC_except_table4825
- GCC_except_table4827
- GCC_except_table4851
- GCC_except_table4873
- GCC_except_table4977
- GCC_except_table498
- GCC_except_table5034
- GCC_except_table5074
- GCC_except_table5226
- GCC_except_table5249
- GCC_except_table5256
- GCC_except_table5259
- GCC_except_table5270
- GCC_except_table5277
- GCC_except_table5424
- GCC_except_table5516
- GCC_except_table5577
- GCC_except_table5580
- GCC_except_table5597
- GCC_except_table5598
- GCC_except_table5604
- GCC_except_table5612
- GCC_except_table5705
- GCC_except_table6093
- GCC_except_table6112
- GCC_except_table6113
- GCC_except_table6119
- GCC_except_table6124
- GCC_except_table6176
- GCC_except_table6181
- GCC_except_table6182
- GCC_except_table6192
- GCC_except_table6194
- GCC_except_table6220
- GCC_except_table6222
- GCC_except_table6224
- GCC_except_table6226
- GCC_except_table6237
- GCC_except_table6239
- GCC_except_table6241
- GCC_except_table6246
- GCC_except_table6279
- GCC_except_table6382
- GCC_except_table6385
- GCC_except_table6451
- GCC_except_table6525
- GCC_except_table6847
- GCC_except_table7095
- GCC_except_table7096
- GCC_except_table7186
- GCC_except_table7189
- GCC_except_table7194
- GCC_except_table7198
- GCC_except_table7199
- GCC_except_table7207
- GCC_except_table7216
- GCC_except_table7232
- GCC_except_table7283
- GCC_except_table7335
- GCC_except_table7336
- GCC_except_table7337
- GCC_except_table7338
- GCC_except_table7370
- GCC_except_table7373
- GCC_except_table7441
- GCC_except_table7451
- GCC_except_table7556
- GCC_except_table7609
- GCC_except_table7611
- GCC_except_table7705
- GCC_except_table7716
- GCC_except_table7721
- GCC_except_table7724
- GCC_except_table7729
- GCC_except_table7730
- GCC_except_table7732
- GCC_except_table7733
- GCC_except_table7734
- GCC_except_table7735
- GCC_except_table775
- GCC_except_table7790
- GCC_except_table7798
- GCC_except_table7812
- GCC_except_table7813
- GCC_except_table7814
- GCC_except_table7848
- GCC_except_table7850
- GCC_except_table7853
- GCC_except_table7856
- GCC_except_table786
- GCC_except_table7901
- GCC_except_table7903
- GCC_except_table796
- GCC_except_table8047
- GCC_except_table8064
- GCC_except_table8065
- GCC_except_table8066
- GCC_except_table8067
- GCC_except_table8068
- GCC_except_table8069
- GCC_except_table8070
- GCC_except_table8113
- GCC_except_table816
- GCC_except_table8299
- GCC_except_table8527
- GCC_except_table8529
- GCC_except_table8530
- GCC_except_table8592
- GCC_except_table8594
- GCC_except_table8596
- GCC_except_table863
- GCC_except_table866
- GCC_except_table8666
- GCC_except_table867
- GCC_except_table8689
- GCC_except_table8691
- GCC_except_table8694
- GCC_except_table8698
- GCC_except_table8700
- GCC_except_table8716
- GCC_except_table8741
- GCC_except_table8745
- GCC_except_table8754
- GCC_except_table8764
- GCC_except_table8765
- GCC_except_table8770
- GCC_except_table8774
- GCC_except_table8776
- GCC_except_table8777
- GCC_except_table8789
- _NUAssetCapabilityAudio
- _NUAssetCapabilityAudioMix
- _NUAssetCapabilityCinematicVideoV1
- _NUAssetCapabilityCinematicVideoV2
- _NUAssetCapabilityHDR
- _NUAssetCapabilityHDRGainMap
- _NUAssetCapabilityPhotographicStyle
- _NUAssetCapabilityPhotographicStyleV1
- _NUAssetCapabilityPhotographicStyleV2
- _NUAssetCapabilityPortraitV1
- _NUAssetCapabilityPortraitV2
- _NUAssetCapabilityRawDecode
- _NUPipelineVariableTargetHeadroom
- _OBJC_CLASS_$_NUAspectFitScalePolicy
- __OBJC_$_CLASS_METHODS_PIADMCleanup
- __OBJC_$_CLASS_METHODS_PIADMOutfill
- __OBJC_$_CLASS_METHODS_PICropStraightenAuto_v1
- __OBJC_$_CLASS_METHODS_PIGANCleanup
- __OBJC_$_CLASS_METHODS_PIOutfillPlaceholder
- ___56+[PIObjectRemoval _instancesForGenerativeEditOperation:]_block_invoke
- ___58+[PIObjectRemoval _nonInstancedOperationsFromComposition:]_block_invoke
- ___58+[PIObjectRemoval _nonInstancedOperationsFromComposition:]_block_invoke_2
- ___81-[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:temporality:connections:error:]_block_invoke
- ___81-[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:temporality:connections:error:]_block_invoke
- ___block_descriptor_41_e8_32s_e29_v16?0"<NUMutablePipeline>"8ls32l8
- ___block_descriptor_48_e8_32s_e33_B24?0"<NUMutablePipeline>"8^16ls32l8
- ___block_descriptor_49_e8_32s40s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8ls32l8s40l8s48l8
- _objc_msgSend$_baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:
- _objc_msgSend$_instancesForGenerativeEditOperation:
- _objc_msgSend$_nonInstancedOperationsFromComposition:
- _objc_msgSend$_tightImageSpaceBoundsForGenerativeEditOperation:composition:error:
- _objc_msgSend$buildFiltersGroupPipeline:temporality:error:
- _objc_msgSend$buildFiltersPipeline:temporality:connections:error:
- _objc_msgSend$defaultNamespace
- _objc_msgSend$gainMapLearnPipeline
- _objc_msgSend$pipelineIdentifier
- _objc_msgSend$renderScaleForInput:geometry:outputScale:
- _objc_msgSend$toneMapPipeline
CStrings:
+ "+[PIObjectRemoval _instancesForGenerativeEditOperation:context:]_block_invoke"
+ "-[PIPipelineModule pipelineName]"
+ "../geometry:<<media.gainMap"
+ "../originalMedia:>output.alternate"
+ "../originalMedia:>output.gainMap"
+ "../originalMedia:>output.primary"
+ "./filters/geometry:<media.original-alternate"
+ "./filters/geometry:<media.original-gainMap"
+ "./filters/geometry:<media.original-primary"
+ "./filters/geometry:>media.original-alternate"
+ "./filters/geometry:>media.original-gainMap"
+ "./filters/geometry:>media.original-primary"
+ "./geometry:<media.gainMap"
+ "./geometry:<media.original-alternate"
+ "./geometry:<media.original-gainMap"
+ "./geometry:<media.original-primary"
+ "./orientation:<media.gainMap"
+ "./orientation:<media.original-alternate"
+ "./orientation:<media.original-gainMap"
+ "./orientation:<media.original-primary"
+ "/:>original+geometry.image.alternate"
+ "/:>original+geometry.image.gainMap"
+ "/:>original.image.alternate"
+ "/:>original.image.gainMap"
+ "/originalKeyFrame:>image"
+ "/originalKeyFrame:>video"
+ ":>original+geometry.alternate"
+ ":>original+geometry.gainMap"
+ ":>original.alternate"
+ ":>original.gainMap"
+ "<%@ name:%@ options:%@>"
+ "AudioMix"
+ "CinematicVideoV1"
+ "CinematicVideoV2"
+ "EdgeExtension: backfill=%d visibleFrame=(%ld,%ld,%ld,%ld) imageFrame=(%ld,%ld,%ld,%ld) options=%lu (top=%d left=%d right=%d)"
+ "Failed to generate post-geometry component"
+ "Failed to instantiate original RAW profile pipeline"
+ "PISensitiveContent: user default set, overriding SafetyRequestFailure to YES"
+ "PI_FORCE_REGIONAL_GUARDRAIL_REQUEST_FAILURE"
+ "PI_GENERATIVE_SEED"
+ "PhotographicStyleV1"
+ "PortraitV1"
+ "cleanup"
+ "cropStraightenAuto"
+ "filterEffect"
+ "highResolutionFusion"
+ "livePhotoEffectAudioBypass"
+ "livePhotoKeyFrameSelector"
+ "maskContextRequestID"
+ "media:<input.%@"
+ "media:>output.%@"
+ "media:>output.audio"
+ "original-"
+ "originalMedia"
+ "originalMedia:<input.%@"
+ "originalMedia:<input.alternate"
+ "originalMedia:<input.disparity"
+ "originalMedia:<input.gainMap"
+ "originalMedia:<input.primary"
+ "originalPrimaryLPKFSelector"
+ "originalPrimaryLPKFSelector:<condition"
+ "originalPrimaryLPKFSelector:<outputIfFalse"
+ "originalPrimaryLPKFSelector:<outputIfTrue"
+ "originalPrimaryLPKFSelector:>output"
+ "originalRawProfile"
+ "originalRawProfile:<primary"
+ "originalRawProfile:>primary"
+ "originalRawProfileHDR"
+ "originalRawProfileHDR:<extendedDynamicRangeAmount"
+ "originalRawProfileHDR:<primary"
+ "originalRawProfileHDR:>primary"
+ "originalRawProfileSDR"
+ "originalRawProfileSDR:<extendedDynamicRangeAmount"
+ "originalRawProfileSDR:<primary"
+ "originalRawProfileSDR:>primary"
+ "outfillPlaceholder"
+ "photosPipeline"
+ "privatePhotosPipeline"
+ "retouchCleanup"
+ "semanticStyleThumbnailApply"
+ "semanticStyleVideoCache:<input"
+ "semanticStyleVideoCache:>output"
+ "semanticStyleVideoCacheBypass"
+ "smartCopyPaste"
+ "smartToneAuto"
+ "whiteBalanceAuto"
- "+[PIObjectRemoval _instancesForGenerativeEditOperation:]_block_invoke"
- "-[PIPipelineModule identifier]"
- "./filters/geometry:<media.original"
- "./filters/geometry:>media.original"
- "./geometry:<media.original"
- "./orientation:<media.original"
- "./originalKeyFrame:>image"
- "/asset:>media.gainMap"
- "/asset:>media.image.gainMap"
- "/asset:>media.video.audio"
- "/image/filters/originalKeyFrame:>video"
- "/video/livePhotoEffect:>media.video.primary"
- "<%@ id:%@ options:%@>"
- "CinematicVideo"
- "CropStraightenAuto"
- "EdgeExtension: visibleFrame=(%ld,%ld,%ld,%ld) imageFrame=(%ld,%ld,%ld,%ld) options=%lu (top=%d left=%d right=%d)"
- "Failed to build LivePhotoKeyFrame pipeline"
- "FilterEffect"
- "GrayColor"
- "ManualRedEye"
- "PIADMCleanup"
- "PIADMOutfill"
- "PIGANCleanup"
- "PIOutfillPlaceholder"
- "PIPhotographicStyleApply"
- "PIRetouchCleanup"
- "PhotosPipeline"
- "Portrait"
- "PrivatePhotosPipeline"
- "SemanticStyleApply"
- "SemanticStyleLearn"
- "SemanticStyleThumbnailApply"
- "SmartToneAuto"
- "WhiteBalanceAuto"
- "gainMapApply:<headroom"
- "gainMapApplyBypass"
- "gainMapApplyBypass:<condition"
- "gainMapApplyBypass:<outputIfTrue"
- "gainMapBypass:>output"
- "gainMapRecompute"
- "gainMapRecompute:<hdrImage"
- "gainMapRecompute:<metadata"
- "gainMapRecompute:<sdrImage"
- "gainMapRecompute:>gainMap"
- "gainMapRecomputeBypass"
- "gainMapRecomputeBypass:<condition"
- "newPortrait:>gainMap"
- "originalSelector"
- "originalSelector:<condition"
- "originalSelector:<outputIfFalse"
- "originalSelector:<outputIfTrue"
- "originalSelector:>output"
- "photos"
- "portraitV1"
- "portraitV2"
- "thumbnailToneMap"
- "thumbnailToneMap:<primary"
- "thumbnailToneMap:>primary"
- "toneMap:<primary"
- "toneMap:>primary"
- "videoPosterFrameToneMap"
- "videoPosterFrameToneMap:<primary"
```
