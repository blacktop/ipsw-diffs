## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/Versions/A/PhotoImaging`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x2bc000
+916.41.100.0.0
+  __TEXT.__text: 0x2bd908
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_methlist: 0x173f8
+  __TEXT.__objc_methlist: 0x17378
   __TEXT.__const: 0x8e70
   __TEXT.__dlopen_cstrs: 0x2a2
   __TEXT.__swift5_typeref: 0x2d8
-  __TEXT.__cstring: 0x4c19a
+  __TEXT.__cstring: 0x4c593
   __TEXT.__constg_swiftt: 0x230
   __TEXT.__swift5_reflstr: 0x35f
   __TEXT.__swift5_fieldmd: 0x3d4
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__oslogstring: 0x7c02
+  __TEXT.__oslogstring: 0x7d08
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_capture: 0x50
   __TEXT.__gcc_except_tab: 0x5048
-  __TEXT.__unwind_info: 0x70a8
+  __TEXT.__unwind_info: 0x7068
   __TEXT.__eh_frame: 0xa60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15d0
+  __DATA_CONST.__const: 0x1590
   __DATA_CONST.__objc_classlist: 0x11a0
-  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc50
+  __DATA_CONST.__objc_selrefs: 0xbcd0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x758
-  __DATA_CONST.__objc_arraydata: 0x9718
-  __DATA_CONST.__got: 0x2830
-  __AUTH_CONST.__const: 0x8fe8
-  __AUTH_CONST.__cfstring: 0x29c00
-  __AUTH_CONST.__objc_const: 0x29ad0
+  __DATA_CONST.__objc_arraydata: 0x9518
+  __DATA_CONST.__got: 0x2818
+  __AUTH_CONST.__const: 0x8fc8
+  __AUTH_CONST.__cfstring: 0x29f00
+  __AUTH_CONST.__objc_const: 0x29c40
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x16b0
-  __AUTH_CONST.__objc_dictobj: 0x5c58
+  __AUTH_CONST.__objc_dictobj: 0x5b90
   __AUTH_CONST.__objc_doubleobj: 0xe10
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0xd0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9612
-  Symbols:   21567
-  CStrings:  7580
+  Functions: 9602
+  Symbols:   21562
+  CStrings:  7607
 
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
+ +[PISegmentationLoader _baseLayout:reusableForConfiguration:]
+ +[PISegmentationLoader _baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:settlingEffectEnabled:]
+ +[PISegmentationLoader ensureLayoutsForAllDisplayContexts:preservesLayout:completion:]
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
+ GCC_except_table1132
+ GCC_except_table1735
+ GCC_except_table1749
+ GCC_except_table1919
+ GCC_except_table2096
+ GCC_except_table2249
+ GCC_except_table2260
+ GCC_except_table2266
+ GCC_except_table2276
+ GCC_except_table2283
+ GCC_except_table2293
+ GCC_except_table2373
+ GCC_except_table2413
+ GCC_except_table2442
+ GCC_except_table2449
+ GCC_except_table2464
+ GCC_except_table2482
+ GCC_except_table2487
+ GCC_except_table2583
+ GCC_except_table323
+ GCC_except_table3836
+ GCC_except_table3957
+ GCC_except_table3967
+ GCC_except_table3970
+ GCC_except_table3983
+ GCC_except_table403
+ GCC_except_table4030
+ GCC_except_table4039
+ GCC_except_table4067
+ GCC_except_table4324
+ GCC_except_table4496
+ GCC_except_table4585
+ GCC_except_table4686
+ GCC_except_table4710
+ GCC_except_table4714
+ GCC_except_table4833
+ GCC_except_table4871
+ GCC_except_table4879
+ GCC_except_table4881
+ GCC_except_table4907
+ GCC_except_table4929
+ GCC_except_table5033
+ GCC_except_table5090
+ GCC_except_table5130
+ GCC_except_table519
+ GCC_except_table5282
+ GCC_except_table5306
+ GCC_except_table5313
+ GCC_except_table5317
+ GCC_except_table5328
+ GCC_except_table5335
+ GCC_except_table5482
+ GCC_except_table5574
+ GCC_except_table5635
+ GCC_except_table5638
+ GCC_except_table5650
+ GCC_except_table5651
+ GCC_except_table5657
+ GCC_except_table5658
+ GCC_except_table5659
+ GCC_except_table5672
+ GCC_except_table5766
+ GCC_except_table6156
+ GCC_except_table6175
+ GCC_except_table6176
+ GCC_except_table6186
+ GCC_except_table6191
+ GCC_except_table6243
+ GCC_except_table6248
+ GCC_except_table6249
+ GCC_except_table6259
+ GCC_except_table6261
+ GCC_except_table6285
+ GCC_except_table6287
+ GCC_except_table6289
+ GCC_except_table6295
+ GCC_except_table6297
+ GCC_except_table6305
+ GCC_except_table6307
+ GCC_except_table6314
+ GCC_except_table6347
+ GCC_except_table6450
+ GCC_except_table6453
+ GCC_except_table6518
+ GCC_except_table6592
+ GCC_except_table6913
+ GCC_except_table7164
+ GCC_except_table7165
+ GCC_except_table7255
+ GCC_except_table7258
+ GCC_except_table7262
+ GCC_except_table7263
+ GCC_except_table7267
+ GCC_except_table7270
+ GCC_except_table7289
+ GCC_except_table7306
+ GCC_except_table7360
+ GCC_except_table7412
+ GCC_except_table7413
+ GCC_except_table7414
+ GCC_except_table7415
+ GCC_except_table7448
+ GCC_except_table7521
+ GCC_except_table7531
+ GCC_except_table7635
+ GCC_except_table7688
+ GCC_except_table7690
+ GCC_except_table7784
+ GCC_except_table7795
+ GCC_except_table7797
+ GCC_except_table7798
+ GCC_except_table7799
+ GCC_except_table7806
+ GCC_except_table7808
+ GCC_except_table7811
+ GCC_except_table7816
+ GCC_except_table7819
+ GCC_except_table7879
+ GCC_except_table7890
+ GCC_except_table7904
+ GCC_except_table7905
+ GCC_except_table7906
+ GCC_except_table7940
+ GCC_except_table7941
+ GCC_except_table7942
+ GCC_except_table7945
+ GCC_except_table798
+ GCC_except_table7994
+ GCC_except_table809
+ GCC_except_table8138
+ GCC_except_table8148
+ GCC_except_table8155
+ GCC_except_table8156
+ GCC_except_table8157
+ GCC_except_table8158
+ GCC_except_table8159
+ GCC_except_table8160
+ GCC_except_table819
+ GCC_except_table8205
+ GCC_except_table839
+ GCC_except_table8391
+ GCC_except_table8617
+ GCC_except_table8619
+ GCC_except_table8620
+ GCC_except_table8682
+ GCC_except_table8684
+ GCC_except_table8686
+ GCC_except_table8756
+ GCC_except_table8792
+ GCC_except_table8801
+ GCC_except_table8803
+ GCC_except_table8805
+ GCC_except_table8826
+ GCC_except_table8839
+ GCC_except_table8847
+ GCC_except_table8848
+ GCC_except_table885
+ GCC_except_table8852
+ GCC_except_table8853
+ GCC_except_table8861
+ GCC_except_table8871
+ GCC_except_table8872
+ GCC_except_table8875
+ GCC_except_table8877
+ GCC_except_table888
+ GCC_except_table8881
+ GCC_except_table8883
+ GCC_except_table889
+ GCC_except_table8896
+ _NUChannelNameAlternate
+ _OBJC_CLASS_$_NUAssetCapability
+ _OBJC_CLASS_$_NURenderPipelineRegistry
+ __86+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:preservesLayout:completion:]_block_invoke
+ __OBJC_$_CATEGORY_CLASS_METHODS_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_CATEGORY_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_CLASS_PROP_LIST_NUAssetCapability_$_PhotoImaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NUPipelineBuilder
+ ___64+[PIObjectRemoval _instancesForGenerativeEditOperation:context:]_block_invoke
+ ___66+[PIObjectRemoval _nonInstancedOperationsFromComposition:context:]_block_invoke
+ ___66+[PIObjectRemoval _nonInstancedOperationsFromComposition:context:]_block_invoke_2
+ ___67-[PIPhotosPipeline_v0 buildPipeline:assetMedia:outputFormat:error:]_block_invoke_2
+ ___86+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:preservesLayout:completion:]_block_invoke
+ ___88-[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:format:temporality:connections:error:]_block_invoke
+ ___88-[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:format:temporality:connections:error:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e29_v16?0"<NUMutablePipeline>"8l
+ ___block_descriptor_57_e8_32s40s48s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e37_"NUChannelPortSpec"16?0"NSString"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8l
+ _objc_msgSend$HDR
+ _objc_msgSend$_baseLayout:reusableForConfiguration:
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
+ _objc_msgSend$ensureLayoutsForAllDisplayContexts:preservesLayout:completion:
+ _objc_msgSend$generativeSeed
+ _objc_msgSend$hdrGainMap
+ _objc_msgSend$isAnyFrameUsingHeadroom
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
- +[PISegmentationLoader ensureLayoutsForAllDisplayContexts:completion:]
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
- GCC_except_table1126
- GCC_except_table1730
- GCC_except_table1744
- GCC_except_table1914
- GCC_except_table2092
- GCC_except_table2246
- GCC_except_table2257
- GCC_except_table2263
- GCC_except_table2273
- GCC_except_table2280
- GCC_except_table2290
- GCC_except_table2370
- GCC_except_table2410
- GCC_except_table2439
- GCC_except_table2446
- GCC_except_table2461
- GCC_except_table2479
- GCC_except_table2484
- GCC_except_table2580
- GCC_except_table316
- GCC_except_table3837
- GCC_except_table3958
- GCC_except_table396
- GCC_except_table3968
- GCC_except_table3972
- GCC_except_table3984
- GCC_except_table4031
- GCC_except_table4040
- GCC_except_table4068
- GCC_except_table4325
- GCC_except_table4498
- GCC_except_table4588
- GCC_except_table4691
- GCC_except_table4715
- GCC_except_table4719
- GCC_except_table4838
- GCC_except_table4876
- GCC_except_table4884
- GCC_except_table4886
- GCC_except_table4912
- GCC_except_table4934
- GCC_except_table5038
- GCC_except_table5095
- GCC_except_table512
- GCC_except_table5135
- GCC_except_table5287
- GCC_except_table5311
- GCC_except_table5318
- GCC_except_table5322
- GCC_except_table5333
- GCC_except_table5340
- GCC_except_table5487
- GCC_except_table5579
- GCC_except_table5640
- GCC_except_table5643
- GCC_except_table5655
- GCC_except_table5656
- GCC_except_table5662
- GCC_except_table5663
- GCC_except_table5669
- GCC_except_table5677
- GCC_except_table5770
- GCC_except_table6159
- GCC_except_table6178
- GCC_except_table6179
- GCC_except_table6189
- GCC_except_table6194
- GCC_except_table6246
- GCC_except_table6251
- GCC_except_table6252
- GCC_except_table6262
- GCC_except_table6264
- GCC_except_table6290
- GCC_except_table6292
- GCC_except_table6294
- GCC_except_table6298
- GCC_except_table6308
- GCC_except_table6310
- GCC_except_table6312
- GCC_except_table6317
- GCC_except_table6350
- GCC_except_table6454
- GCC_except_table6457
- GCC_except_table6523
- GCC_except_table6597
- GCC_except_table6919
- GCC_except_table7170
- GCC_except_table7171
- GCC_except_table7261
- GCC_except_table7264
- GCC_except_table7269
- GCC_except_table7273
- GCC_except_table7274
- GCC_except_table7282
- GCC_except_table7295
- GCC_except_table7312
- GCC_except_table7366
- GCC_except_table7418
- GCC_except_table7419
- GCC_except_table7420
- GCC_except_table7421
- GCC_except_table7458
- GCC_except_table7526
- GCC_except_table7536
- GCC_except_table7641
- GCC_except_table7694
- GCC_except_table7696
- GCC_except_table7796
- GCC_except_table7804
- GCC_except_table7805
- GCC_except_table7813
- GCC_except_table7820
- GCC_except_table7822
- GCC_except_table7823
- GCC_except_table7824
- GCC_except_table7825
- GCC_except_table7827
- GCC_except_table7885
- GCC_except_table7896
- GCC_except_table791
- GCC_except_table7910
- GCC_except_table7911
- GCC_except_table7912
- GCC_except_table7946
- GCC_except_table7947
- GCC_except_table7951
- GCC_except_table7954
- GCC_except_table8000
- GCC_except_table802
- GCC_except_table812
- GCC_except_table8144
- GCC_except_table8154
- GCC_except_table8162
- GCC_except_table8163
- GCC_except_table8164
- GCC_except_table8165
- GCC_except_table8166
- GCC_except_table8167
- GCC_except_table8210
- GCC_except_table832
- GCC_except_table8396
- GCC_except_table8624
- GCC_except_table8626
- GCC_except_table8627
- GCC_except_table8689
- GCC_except_table8691
- GCC_except_table8693
- GCC_except_table8763
- GCC_except_table879
- GCC_except_table8799
- GCC_except_table8810
- GCC_except_table8819
- GCC_except_table882
- GCC_except_table8822
- GCC_except_table883
- GCC_except_table8833
- GCC_except_table8846
- GCC_except_table8854
- GCC_except_table8855
- GCC_except_table8859
- GCC_except_table8860
- GCC_except_table8868
- GCC_except_table8878
- GCC_except_table8879
- GCC_except_table8882
- GCC_except_table8888
- GCC_except_table8890
- GCC_except_table8891
- GCC_except_table8903
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
- __70+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:completion:]_block_invoke
- __OBJC_$_CLASS_METHODS_PIADMCleanup
- __OBJC_$_CLASS_METHODS_PIADMOutfill
- __OBJC_$_CLASS_METHODS_PICropStraightenAuto_v1
- __OBJC_$_CLASS_METHODS_PIGANCleanup
- __OBJC_$_CLASS_METHODS_PIOutfillPlaceholder
- ___56+[PIObjectRemoval _instancesForGenerativeEditOperation:]_block_invoke
- ___58+[PIObjectRemoval _nonInstancedOperationsFromComposition:]_block_invoke
- ___58+[PIObjectRemoval _nonInstancedOperationsFromComposition:]_block_invoke_2
- ___70+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:completion:]_block_invoke
- ___81-[PIPrivatePhotosPipeline_v0 buildFiltersPipeline:temporality:connections:error:]_block_invoke
- ___81-[PIPrivatePhotosPipeline_v1 buildFiltersPipeline:temporality:connections:error:]_block_invoke
- ___block_descriptor_41_e8_32s_e29_v16?0"<NUMutablePipeline>"8l
- ___block_descriptor_48_e8_32s_e33_B24?0"<NUMutablePipeline>"8^16l
- ___block_descriptor_49_e8_32s40s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8l
- ___block_descriptor_56_e8_32s40s48s_e44_"NUChannelPortRef"16?0"NUChannelPortRef"8l
- _objc_msgSend$_baseLayoutForDisplayContext:ofItem:spatialPhotoEnabled:
- _objc_msgSend$_instancesForGenerativeEditOperation:
- _objc_msgSend$_nonInstancedOperationsFromComposition:
- _objc_msgSend$_tightImageSpaceBoundsForGenerativeEditOperation:composition:error:
- _objc_msgSend$buildFiltersGroupPipeline:temporality:error:
- _objc_msgSend$buildFiltersPipeline:temporality:connections:error:
- _objc_msgSend$defaultNamespace
- _objc_msgSend$ensureLayoutsForAllDisplayContexts:completion:
- _objc_msgSend$gainMapLearnPipeline
- _objc_msgSend$pipelineIdentifier
- _objc_msgSend$renderScaleForInput:geometry:outputScale:
- _objc_msgSend$toneMapPipeline
CStrings:
+ "+[PIObjectRemoval _instancesForGenerativeEditOperation:context:]_block_invoke"
+ "+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:preservesLayout:completion:]"
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
+ "Missing %{public}@ layout configuration, skipping layout property recalculation"
+ "PISensitiveContent: user default set, overriding SafetyRequestFailure to YES"
+ "PI_FORCE_REGIONAL_GUARDRAIL_REQUEST_FAILURE"
+ "PI_GENERATIVE_SEED"
+ "PhotographicStyleV1"
+ "PortraitV1"
+ "Resetting per-display layouts (dynamic config changed: %d, segmentation version changed: %d)"
+ "cleanup"
+ "cropStraightenAuto"
+ "filterEffect"
+ "highResolutionFusion"
+ "landscape"
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
- "+[PISegmentationLoader ensureLayoutsForAllDisplayContexts:completion:]"
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
