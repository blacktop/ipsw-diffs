## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-920.7.110.0.0
-  __TEXT.__text: 0x2a356c
+920.12.210.0.0
+  __TEXT.__text: 0x2ab218
   __TEXT.__delay_helper: 0x22c
-  __TEXT.__objc_methlist: 0x17c10
-  __TEXT.__const: 0x8e00
+  __TEXT.__objc_methlist: 0x17e10
+  __TEXT.__const: 0x8e30
   __TEXT.__dlopen_cstrs: 0x2a2
-  __TEXT.__swift5_typeref: 0x3ba
+  __TEXT.__swift5_typeref: 0x414
   __TEXT.__constg_swiftt: 0x250
   __TEXT.__swift5_reflstr: 0x556
   __TEXT.__swift5_fieldmd: 0x50c
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__cstring: 0x4b793
+  __TEXT.__cstring: 0x4bc8f
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x38
-  __TEXT.__oslogstring: 0x845f
-  __TEXT.__swift5_capture: 0x354
+  __TEXT.__oslogstring: 0x857b
+  __TEXT.__swift5_capture: 0x390
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift_as_entry: 0x1c
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift_as_cont: 0x34
-  __TEXT.__gcc_except_tab: 0x5038
+  __TEXT.__gcc_except_tab: 0x504c
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x7288
-  __TEXT.__eh_frame: 0xc80
+  __TEXT.__unwind_info: 0x73f0
+  __TEXT.__eh_frame: 0xd80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x46f8
-  __DATA_CONST.__objc_classlist: 0x1228
+  __DATA_CONST.__const: 0x4910
+  __DATA_CONST.__objc_classlist: 0x1230
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc040
+  __DATA_CONST.__objc_selrefs: 0xc218
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x788
-  __DATA_CONST.__objc_arraydata: 0x8fe0
-  __DATA_CONST.__got: 0x28d8
-  __AUTH_CONST.__const: 0x6140
-  __AUTH_CONST.__cfstring: 0x2a340
-  __AUTH_CONST.__objc_const: 0x2b0a8
+  __DATA_CONST.__objc_superrefs: 0x7b0
+  __DATA_CONST.__objc_arraydata: 0x8fb8
+  __DATA_CONST.__got: 0x2980
+  __AUTH_CONST.__const: 0x62e0
+  __AUTH_CONST.__cfstring: 0x2a1a0
+  __AUTH_CONST.__objc_const: 0x2afd8
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_doubleobj: 0xe10
-  __AUTH_CONST.__objc_intobj: 0x1530
-  __AUTH_CONST.__objc_arrayobj: 0x750
+  __AUTH_CONST.__objc_doubleobj: 0xdc0
+  __AUTH_CONST.__objc_intobj: 0x15d8
+  __AUTH_CONST.__objc_arrayobj: 0x720
   __AUTH_CONST.__objc_floatobj: 0xb0
-  __AUTH_CONST.__objc_dictobj: 0x56b8
-  __AUTH_CONST.__auth_got: 0x1728
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x165c
-  __DATA.__data: 0x494
-  __DATA_DIRTY.__objc_data: 0xb2f0
+  __AUTH_CONST.__objc_dictobj: 0x5780
+  __AUTH_CONST.__auth_got: 0x1790
+  __AUTH.__objc_data: 0x5c0
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x1654
+  __DATA.__data: 0x49c
+  __DATA_DIRTY.__objc_data: 0xb250
   __DATA_DIRTY.__data: 0x15f8
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AutoLoop.framework/AutoLoop
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
+  - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/InertiaCam.framework/InertiaCam
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9889
-  Symbols:   16814
-  CStrings:  7704
+  Functions: 9992
+  Symbols:   16935
+  CStrings:  7728
 
Symbols:
+ +[NUAssetCapability(PISlowMotion) slowMotion]
+ +[PIAudioMix_v1 dialogMixBiasDescriptor]
+ +[PIAudioMix_v1 renderingStyleDescriptor]
+ +[PILivePhotoEffect_v1 availableOptions]
+ +[PILivePhotoKeyFrame_v1 adjustmentDescriptorForAsset:]
+ +[PILivePhotoKeyFrame_v1 captureKeyFrameTimeForAsset:]
+ +[PIModularPhotosPipeline buildPhotosPipelineVersion:forAsset:options:error:]
+ +[PIModularPhotosPipeline withPhotosPipelineForComposition:options:block:error:]
+ +[PIModularPhotosPipeline(Common) controlDataWithAdjustment:format:]
+ +[PIModularPhotosPipeline(Common) controlDataWithAudioMixAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithCropStraightenAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithCurvesAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithDepthEffectAdjustment:descriptor:]
+ +[PIModularPhotosPipeline(Common) controlDataWithEffect3DAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithEffectAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithLevelsAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithLivePhotoKeyFrameAdjustment:descriptor:]
+ +[PIModularPhotosPipeline(Common) controlDataWithMuteAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithOrientationAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithPortraitEffectAdjustment:descriptor:]
+ +[PIModularPhotosPipeline(Common) controlDataWithPortraitVideoAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithSelectiveColorAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithSemanticStyleAdjustment:descriptor:]
+ +[PIModularPhotosPipeline(Common) controlDataWithSloMoAdjustment:]
+ +[PIModularPhotosPipeline(Common) controlDataWithTrimAdjustment:]
+ +[PIModularPhotosPipeline(Common) disabledControlDataWithDescriptor:]
+ +[PIModularPhotosPipeline(Common) mediaDataWithInpaintMasks:error:]
+ +[PIPhotographicStyle defaultSettingsForAsset:]
+ +[PISignedMetadata _developmentSignedBoxForRequest:identity:error:]
+ +[PISignedMetadata _developmentSigningIdentityWithError:]
+ +[PISignedMetadata _errorWithStatus:reason:object:]
+ +[PISignedMetadata _hasDevelopmentSigningIdentity]
+ +[PISignedMetadata _insertBox:intoImageAtURL:error:]
+ +[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]
+ +[PISignedMetadata _signingRequestForImageAtURL:error:]
+ +[PISignedMetadata _signingServiceAvailable]
+ +[PISignedMetadata canSignFileType:]
+ +[PISignedMetadata developmentOperationsOverride]
+ +[PISignedMetadata developmentSigningIdentityURL]
+ +[PISignedMetadata operationsForComposition:]
+ +[PISignedMetadata setDevelopmentOperationsOverride:]
+ +[PISignedMetadata setDevelopmentSigningIdentityURL:]
+ +[PISignedMetadata signImageAtURL:completion:]
+ +[PISignedMetadata signingRequiredForComposition:]
+ +[PITextureStyle grainIdentifier]
+ -[NUGlobalSettings(PIGlobalSettings) setSignedMetadataEnabled:]
+ -[NUGlobalSettings(PIGlobalSettings) signedMetadataEnabled]
+ -[PICinematicVideo initWithOptions:]
+ -[PICinematicVideo inputChannels]
+ -[PICinematicVideo outputChannels]
+ -[PICinematicVideoTimedFocusDisparityProcessor _generationOfCinematographyState:]
+ -[PICinematicVideoTimedFocusDisparityProcessor cinematographySnapshotDictionaryForVideoURLString:cinematographyState:error:]
+ -[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:controlData:error:]
+ -[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForDictionaryRepresentation:videoURLString:perform:]
+ -[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForVideoURLString:cinematographyState:error:perform:]
+ -[PICompositionExportResult didEmbedSignedMetadata]
+ -[PICompositionExportResult setDidEmbedSignedMetadata:]
+ -[PICompositionExporterAuxiliaryOptions embedSignedMetadata]
+ -[PICompositionExporterAuxiliaryOptions setEmbedSignedMetadata:]
+ -[PICompositionExporterImageOptions embedSignedMetadata]
+ -[PICompositionExporterImageOptions setEmbedSignedMetadata:]
+ -[PIDepthEffectApertureAutoCalculator resultWithPipeline:asset:error:]
+ -[PIGlobalSettings setSignedMetadataEnabled:]
+ -[PIGlobalSettings signedMetadataEnabled]
+ -[PILivePhotoEffect_v1 includesAudio]
+ -[PILivePhotoEffect_v1 mediaFormatWithAudioChannel:]
+ -[PILivePhotoEffect_v1 mediaFormat]
+ -[PILivePhotoEffect_v1 outputMediaFormat]
+ -[PILivePhotoKeyFrame_v1 .cxx_destruct]
+ -[PILivePhotoKeyFrame_v1 asset]
+ -[PILivePhotoKeyFrame_v1 initWithAsset:]
+ -[PILivePhotoKeyFrame_v1 initWithOptions:]
+ -[PIModularAutoCalculator controlFormatForPipeline:input:error:]
+ -[PIModularAutoCalculator pipelineInput]
+ -[PIModularAutoCalculator resultWithPipeline:asset:error:]
+ -[PIModularPhotosPipelineCache _cacheEntryForSource:options:error:]
+ -[PIModularPhotosPipelineCache _newCacheEntryForSource:options:session:error:]
+ -[PIModularPhotosPipelineCacheEntry asset]
+ -[PIModularPhotosPipelineCacheEntry initWithPipeline:asset:options:session:]
+ -[PIParallaxSegmentationItem hasUnarchivedChanges]
+ -[PIPhotographicStyle initWithOptions:]
+ -[PIPhotosPipeline addInputChannels:error:]
+ -[PIPhotosPipeline addOutputChannels:error:]
+ -[PIPhotosPipeline imageOutputFormatWithInputFormat:error:]
+ -[PIPhotosPipeline inputChannels:]
+ -[PIPhotosPipeline livePhotoOutputFormatWithInputFormat:error:]
+ -[PIPhotosPipeline outputChannels:]
+ -[PIPhotosPipeline outputMediaFormat:]
+ -[PIPhotosPipeline videoOutputFormatWithInputFormat:error:]
+ -[PIPhotosPipeline_v0 inputChannels:]
+ -[PIPhotosPipeline_v0 outputChannels:]
+ -[PIPhotosPipeline_v1 _addComponentGroup:name:module:containerFormat:componentFormat:componentChannel:error:]
+ -[PIPhotosPipeline_v1 buildTemporalGeometryPipeline:format:input:error:]
+ -[PIPhotosPipeline_v1 inputChannels:]
+ -[PIPhotosPipeline_v1 outputChannels:]
+ -[PIPortrait initWithOptions:]
+ -[PIPortrait inputChannels]
+ -[PIPortrait outputChannels]
+ -[PIPortraitAutoCalculator _settingsWithPortraitSettings:]
+ -[PIPortraitAutoCalculator resultWithPipeline:asset:error:]
+ -[PIPrivatePhotosPipeline .cxx_destruct]
+ -[PIPrivatePhotosPipeline basePipeline]
+ -[PIPrivatePhotosPipeline buildPipeline:error:]
+ -[PIPrivatePhotosPipeline initWithPipelineDescriptor:]
+ -[PIPrivatePhotosPipeline initWithPipelineDescriptor:basePipeline:]
+ -[PIPrivatePhotosPipeline inputChannels:]
+ -[PIPrivatePhotosPipeline outputChannels:]
+ -[PIPrivatePhotosPipeline updateInputChannels:error:]
+ -[PIPrivatePhotosPipeline updateOutputChannels:error:]
+ -[PIPrivatePhotosPipeline_v0 addPipelineFilterInputChannels:]
+ -[PIPrivatePhotosPipeline_v0 inputChannels:]
+ -[PIPrivatePhotosPipeline_v0 outputChannels:]
+ -[PIPrivatePhotosPipeline_v1 inputChannels:]
+ -[PIPrivatePhotosPipeline_v1 outputChannels:]
+ -[PISemanticStyleAutoCalculator pipelineInput]
+ -[PISignedMetadataDevelopmentIdentity .cxx_destruct]
+ -[PISignedMetadataDevelopmentIdentity certificate]
+ -[PISignedMetadataDevelopmentIdentity keyData]
+ -[PISignedMetadataDevelopmentIdentity setCertificate:]
+ -[PISignedMetadataDevelopmentIdentity setKeyData:]
+ -[PISignedMetadataSigningRequest .cxx_destruct]
+ -[PISignedMetadataSigningRequest contentHash]
+ -[PISignedMetadataSigningRequest listedItemIDs]
+ -[PISignedMetadataSigningRequest setContentHash:]
+ -[PISignedMetadataSigningRequest setListedItemIDs:]
+ -[PISlowMotion_v1 initWithAsset:]
+ -[PISlowMotion_v1 initWithOptions:]
+ -[PITextureStyleAutoCalculator pipelineInput]
+ -[_PISlowMotionCapability evaluateForAsset:]
+ GCC_except_table1033
+ GCC_except_table1367
+ GCC_except_table1403
+ GCC_except_table1406
+ GCC_except_table1407
+ GCC_except_table161
+ GCC_except_table1639
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table1741
+ GCC_except_table1742
+ GCC_except_table1746
+ GCC_except_table1747
+ GCC_except_table1748
+ GCC_except_table175
+ GCC_except_table1753
+ GCC_except_table1761
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table2057
+ GCC_except_table2097
+ GCC_except_table2632
+ GCC_except_table2639
+ GCC_except_table2642
+ GCC_except_table2653
+ GCC_except_table2660
+ GCC_except_table2739
+ GCC_except_table2741
+ GCC_except_table3015
+ GCC_except_table3017
+ GCC_except_table3019
+ GCC_except_table303
+ GCC_except_table3121
+ GCC_except_table314
+ GCC_except_table3148
+ GCC_except_table3187
+ GCC_except_table333
+ GCC_except_table3341
+ GCC_except_table3350
+ GCC_except_table3378
+ GCC_except_table339
+ GCC_except_table3404
+ GCC_except_table341
+ GCC_except_table3472
+ GCC_except_table3494
+ GCC_except_table3499
+ GCC_except_table3500
+ GCC_except_table3510
+ GCC_except_table3512
+ GCC_except_table3544
+ GCC_except_table365
+ GCC_except_table3666
+ GCC_except_table3836
+ GCC_except_table3841
+ GCC_except_table3851
+ GCC_except_table387
+ GCC_except_table4055
+ GCC_except_table4186
+ GCC_except_table4448
+ GCC_except_table4452
+ GCC_except_table4557
+ GCC_except_table4565
+ GCC_except_table457
+ GCC_except_table4771
+ GCC_except_table5232
+ GCC_except_table5243
+ GCC_except_table5253
+ GCC_except_table5297
+ GCC_except_table5386
+ GCC_except_table5388
+ GCC_except_table5520
+ GCC_except_table5560
+ GCC_except_table5581
+ GCC_except_table5677
+ GCC_except_table5724
+ GCC_except_table5868
+ GCC_except_table5968
+ GCC_except_table5972
+ GCC_except_table5975
+ GCC_except_table5977
+ GCC_except_table5979
+ GCC_except_table5981
+ GCC_except_table5987
+ GCC_except_table5992
+ GCC_except_table6001
+ GCC_except_table6077
+ GCC_except_table6162
+ GCC_except_table6287
+ GCC_except_table6297
+ GCC_except_table6305
+ GCC_except_table6306
+ GCC_except_table6307
+ GCC_except_table6308
+ GCC_except_table6309
+ GCC_except_table6310
+ GCC_except_table6345
+ GCC_except_table6351
+ GCC_except_table6359
+ GCC_except_table6366
+ GCC_except_table6374
+ GCC_except_table6422
+ GCC_except_table6432
+ GCC_except_table6516
+ GCC_except_table6524
+ GCC_except_table6538
+ GCC_except_table6539
+ GCC_except_table6540
+ GCC_except_table6622
+ GCC_except_table6623
+ GCC_except_table6813
+ GCC_except_table6827
+ GCC_except_table6889
+ GCC_except_table6890
+ GCC_except_table6982
+ GCC_except_table6985
+ GCC_except_table6989
+ GCC_except_table6990
+ GCC_except_table6994
+ GCC_except_table6995
+ GCC_except_table6997
+ GCC_except_table7003
+ GCC_except_table7012
+ GCC_except_table7028
+ GCC_except_table7079
+ GCC_except_table7132
+ GCC_except_table7133
+ GCC_except_table7134
+ GCC_except_table7135
+ GCC_except_table7170
+ GCC_except_table726
+ GCC_except_table7419
+ GCC_except_table7452
+ GCC_except_table7510
+ GCC_except_table7545
+ GCC_except_table7572
+ GCC_except_table7683
+ GCC_except_table7685
+ GCC_except_table7686
+ GCC_except_table7687
+ GCC_except_table7689
+ GCC_except_table7691
+ GCC_except_table7693
+ GCC_except_table7696
+ GCC_except_table7699
+ GCC_except_table7701
+ GCC_except_table7702
+ GCC_except_table7703
+ GCC_except_table7704
+ GCC_except_table7706
+ GCC_except_table7711
+ GCC_except_table773
+ GCC_except_table7835
+ GCC_except_table7837
+ GCC_except_table7838
+ GCC_except_table7869
+ GCC_except_table7879
+ GCC_except_table7882
+ GCC_except_table7883
+ GCC_except_table7895
+ GCC_except_table806
+ GCC_except_table8247
+ GCC_except_table837
+ GCC_except_table8388
+ GCC_except_table844
+ GCC_except_table8477
+ GCC_except_table8496
+ GCC_except_table8497
+ GCC_except_table8503
+ GCC_except_table8637
+ GCC_except_table8821
+ GCC_except_table8826
+ GCC_except_table8841
+ GCC_except_table8857
+ GCC_except_table8862
+ GCC_except_table8868
+ GCC_except_table8930
+ GCC_except_table8941
+ GCC_except_table8946
+ GCC_except_table8954
+ GCC_except_table8955
+ GCC_except_table8956
+ GCC_except_table8959
+ GCC_except_table8961
+ GCC_except_table8965
+ GCC_except_table8967
+ GCC_except_table8986
+ GCC_except_table8990
+ GCC_except_table8994
+ GCC_except_table8995
+ GCC_except_table9003
+ GCC_except_table9007
+ GCC_except_table9033
+ GCC_except_table9034
+ GCC_except_table9035
+ GCC_except_table9047
+ _CMPhotoAIMarkerCopyFileAndInsertAIMarker
+ _CMPhotoAIMarkerCreateBox
+ _CMPhotoAIMarkerCreateContentHash
+ _CMPhotoAIMarkerModifyBoxSignature
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NUChannelGenericMediaFormat
+ _OBJC_CLASS_$_NUChannelOptionalFormat
+ _OBJC_CLASS_$_PISignedMetadata
+ _OBJC_CLASS_$_PISignedMetadataDevelopmentIdentity
+ _OBJC_CLASS_$_PISignedMetadataSigningRequest
+ _OBJC_CLASS_$_PISignedMetadataSigningService
+ _OBJC_CLASS_$__PISlowMotionCapability
+ _OBJC_IVAR_$_PICompositionExportResult._didEmbedSignedMetadata
+ _OBJC_IVAR_$_PICompositionExporterAuxiliaryOptions._embedSignedMetadata
+ _OBJC_IVAR_$_PICompositionExporterImageOptions._embedSignedMetadata
+ _OBJC_IVAR_$_PILivePhotoKeyFrame_v1._asset
+ _OBJC_IVAR_$_PIModularPhotosPipelineCacheEntry._asset
+ _OBJC_IVAR_$_PIParallaxSegmentationItem._hasUnarchivedChanges
+ _OBJC_IVAR_$_PIPrivatePhotosPipeline._basePipeline
+ _OBJC_IVAR_$_PISegmentationLoader._reusedCachedSegmentationForNewLayout
+ _OBJC_IVAR_$_PISignedMetadataDevelopmentIdentity._certificate
+ _OBJC_IVAR_$_PISignedMetadataDevelopmentIdentity._keyData
+ _OBJC_IVAR_$_PISignedMetadataSigningRequest._contentHash
+ _OBJC_IVAR_$_PISignedMetadataSigningRequest._listedItemIDs
+ _OBJC_METACLASS_$_PISignedMetadata
+ _OBJC_METACLASS_$_PISignedMetadataDevelopmentIdentity
+ _OBJC_METACLASS_$_PISignedMetadataSigningRequest
+ _OBJC_METACLASS_$_PISignedMetadataSigningService
+ _OBJC_METACLASS_$__PISlowMotionCapability
+ _PFGenerativeEditsOperationIdentifierCleanUpPrefix
+ _PFGenerativeEditsOperationIdentifierOutfill
+ _PFGenerativeEditsOperationIdentifierSpatialReframe
+ _PILivePhotoEffectNoAudio
+ _SecKeyCreateSignature
+ _SecKeyCreateWithData
+ _UTTypeHEIC
+ _UTTypeHEIF
+ __CLASS_METHODS_PISignedMetadataSigningService
+ __DATA_PISignedMetadataSigningService
+ __INSTANCE_METHODS_PISignedMetadataSigningService
+ __METACLASS_DATA_PISignedMetadataSigningService
+ __OBJC_$_CLASS_METHODS_NUAssetCapability(PIAudioMix|PICinematicVideo|PIPhotographicStyle|PIPortrait|PISlowMotion)
+ __OBJC_$_CLASS_METHODS_PIModularPhotosPipeline(Common)
+ __OBJC_$_CLASS_METHODS_PISignedMetadata
+ __OBJC_$_CLASS_PROP_LIST_PISignedMetadata
+ __OBJC_$_INSTANCE_METHODS_PISignedMetadataDevelopmentIdentity
+ __OBJC_$_INSTANCE_METHODS_PISignedMetadataSigningRequest
+ __OBJC_$_INSTANCE_METHODS__PISlowMotionCapability
+ __OBJC_$_INSTANCE_VARIABLES_PILivePhotoKeyFrame_v1
+ __OBJC_$_INSTANCE_VARIABLES_PIPrivatePhotosPipeline
+ __OBJC_$_INSTANCE_VARIABLES_PISignedMetadataDevelopmentIdentity
+ __OBJC_$_INSTANCE_VARIABLES_PISignedMetadataSigningRequest
+ __OBJC_$_PROP_LIST_PILivePhotoKeyFrame_v1
+ __OBJC_$_PROP_LIST_PISignedMetadataDevelopmentIdentity
+ __OBJC_$_PROP_LIST_PISignedMetadataSigningRequest
+ __OBJC_CLASS_RO_$_PISignedMetadata
+ __OBJC_CLASS_RO_$_PISignedMetadataDevelopmentIdentity
+ __OBJC_CLASS_RO_$_PISignedMetadataSigningRequest
+ __OBJC_CLASS_RO_$__PISlowMotionCapability
+ __OBJC_METACLASS_RO_$_PISignedMetadata
+ __OBJC_METACLASS_RO_$_PISignedMetadataDevelopmentIdentity
+ __OBJC_METACLASS_RO_$_PISignedMetadataSigningRequest
+ __OBJC_METACLASS_RO_$__PISlowMotionCapability
+ ___109-[PIPhotosPipeline_v1 _addComponentGroup:name:module:containerFormat:componentFormat:componentChannel:error:]_block_invoke
+ ___109-[PIPhotosPipeline_v1 _addComponentGroup:name:module:containerFormat:componentFormat:componentChannel:error:]_block_invoke_2
+ ___124-[PICinematicVideoTimedFocusDisparityProcessor cinematographySnapshotDictionaryForVideoURLString:cinematographyState:error:]_block_invoke
+ ___138-[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForDictionaryRepresentation:videoURLString:perform:]_block_invoke
+ ___139-[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForVideoURLString:cinematographyState:error:perform:]_block_invoke
+ ___34-[PIModularAutoCalculator submit:]_block_invoke_5
+ ___34-[PIModularAutoCalculator submit:]_block_invoke_6
+ ___34-[PIModularAutoCalculator submit:]_block_invoke_7
+ ___43-[PICropStraighten_v1 buildPipeline:error:]_block_invoke_2
+ ___45-[PIPrivatePhotosPipeline_v0 outputChannels:]_block_invoke
+ ___45-[PIPrivatePhotosPipeline_v1 outputChannels:]_block_invoke
+ ___46+[PISignedMetadata signImageAtURL:completion:]_block_invoke
+ ___46+[PISignedMetadata signImageAtURL:completion:]_block_invoke_2
+ ___58-[PIPortraitAutoCalculator _settingsWithPortraitSettings:]_block_invoke
+ ___59-[NUGlobalSettings(PIGlobalSettings) signedMetadataEnabled]_block_invoke
+ ___67+[PIModularPhotosPipeline(Common) controlDataWithCurvesAdjustment:]_block_invoke
+ ___67-[PIPhotosPipeline_v1 buildPipeline:assetMedia:outputFormat:error:]_block_invoke_2
+ ___67-[PIPhotosPipeline_v1 buildPipeline:assetMedia:outputFormat:error:]_block_invoke_3
+ ___73-[PICompositionExporter exportImageToURL:composition:options:completion:]_block_invoke_2
+ ___74+[PIModularPhotosPipeline(Common) controlDataWithPortraitVideoAdjustment:]_block_invoke_2
+ ___75+[PIModularPhotosPipeline(Common) controlDataWithCropStraightenAdjustment:]_block_invoke
+ ___75+[PIModularPhotosPipeline(Common) controlDataWithSelectiveColorAdjustment:]_block_invoke
+ ___75+[PIModularPhotosPipeline(Common) controlDataWithSelectiveColorAdjustment:]_block_invoke_2
+ ___77-[PIPhotosPipeline_v1 buildSpatialGeometryPipeline:format:connections:error:]_block_invoke_2
+ ___77-[PIPhotosPipeline_v1 buildSpatialGeometryPipeline:format:connections:error:]_block_invoke_3
+ ___77-[PIPhotosPipeline_v1 buildSpatialGeometryPipeline:format:connections:error:]_block_invoke_4
+ ___82+[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]_block_invoke
+ ___82+[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]_block_invoke_2
+ ___82+[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]_block_invoke_3
+ ___82+[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]_block_invoke_4
+ ___82+[PISignedMetadata _requestSignedBoxForRequest:identity:timeout:queue:completion:]_block_invoke_5
+ ___88-[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:controlData:error:]_block_invoke
+ ___88-[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:controlData:error:]_block_invoke_2
+ ___block_descriptor_32_e19_B16?0"NUChannel"8l
+ ___block_descriptor_32_e80_"NUChannelPortRef"32?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24l
+ ___block_descriptor_32_e84_"NUChannelPortRef"40?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24^32l
+ ___block_descriptor_40_e22_B16?0"NSDictionary"8l
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e40_B32?0"<NUPipeline>"8"<NUAsset>"16^24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e84_"NUChannelPortRef"40?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24^32ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40bs_e59_v24?0"PFPosterOrientedLayout"8"PFPosterOrientedLayout"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e84_"NUChannelPortRef"40?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24^32ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32bs40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e84_"NUChannelPortRef"40?0"<NUMutablePipeline>"8"NUChannelPortRef"16"NSArray"24^32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e40_B32?0"<NUPipeline>"8"<NUAsset>"16^24lr56l8u64l8s32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48bs_e20_v16?0"NUResponse"8ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e33_B24?0"<NUMutablePipeline>"8^16ls32l8s40l8s48l8s56l8s64l8s72l8
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _dispatch_queue_attr_make_with_qos_class
+ _kCMPhotoAIMarkerBoxOption_CertificateChain
+ _kCMPhotoAIMarkerBoxOption_Description
+ _kCMPhotoAIMarkerBoxOption_PlaceholderSignature
+ _kCMPhotoAIMarkerBoxOption_SignatureAlgorithm
+ _kCMPhotoAIMarkerSignatureAlgorithm_ECDSAP256SHA384
+ _kSecAttrKeyClass
+ _kSecAttrKeyClassPrivate
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecKeyAlgorithmECDSASignatureDigestX962SHA384
+ _os_signpost_id_generate
+ _sDevelopmentOperationsOverride
+ _sDevelopmentSigningIdentityURL
+ _swift_retain
+ _swift_retain_x2
+ _symbolic Say_____GSg s6UInt32V
+ _symbolic So6NSDataCSgSo7NSErrorCSgIeyBhyy_
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____Sg______pSgIeghgg_ 10Foundation4DataV s5ErrorP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s6UInt32V
- +[PIAudioMix_v1 adjustmentFormat]
- +[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForDictionaryRepresentation:perform:]
- +[PICinematicVideo_v1 adjustmentFormat]
- +[PICinematicVideo_v2 adjustmentFormat]
- +[PIDefinition_v1 defaultAdjustmentData]
- +[PIFilterEffect_v1 adjustmentFormat]
- +[PILivePhotoEffect_v1 mediaFormat]
- +[PILivePhotoKeyFrame_v1 adjustmentDescriptor]
- +[PILivePhotoKeyFrame_v1 adjustmentFormat]
- +[PIModularPhotosPipeline buildPhotosPipelineVersion:forSource:options:error:]
- +[PIModularPhotosPipeline_v0 controlDataWithAdjustment:format:]
- +[PIModularPhotosPipeline_v0 controlDataWithAudioMixAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithCropStraightenAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithCurvesAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithDepthEffectAdjustment:descriptor:]
- +[PIModularPhotosPipeline_v0 controlDataWithEffect3DAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithEffectAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithLevelsAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithLivePhotoKeyFrameAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithMuteAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithOrientationAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithPortraitEffectAdjustment:descriptor:]
- +[PIModularPhotosPipeline_v0 controlDataWithPortraitVideoAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithSelectiveColorAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithSemanticStyleAdjustment:descriptor:]
- +[PIModularPhotosPipeline_v0 controlDataWithSloMoAdjustment:]
- +[PIModularPhotosPipeline_v0 controlDataWithTrimAdjustment:]
- +[PIModularPhotosPipeline_v0 mediaDataWithInpaintMasks:error:]
- +[PIMute_v1 adjustmentFormat]
- +[PINoiseReduction_v1 defaultAdjustmentData]
- +[PIOrientation_v1 adjustmentFormat]
- +[PIPhotographicStyle adjustmentDescriptorForVersion:capturedSettings:]
- +[PIPhotographicStyle adjustmentFormat]
- +[PIPortrait portraitSettingsDescriptorForAsset:]
- +[PIPortraitAutoCalculator portraitSettingsWithExifProperties:makerNote:disparityMetadata:depthData:error:]
- +[PIPortrait_v1 portraitSettingsAdjustmentDescriptor]
- +[PIPortrait_v1 portraitSettingsAdjustmentFormat]
- +[PIPortrait_v1 portraitSettingsExpressionFunctionClass]
- +[PIPortrait_v2 portraitSettingsAdjustmentDescriptor]
- +[PIPortrait_v2 portraitSettingsExpressionFunctionClass]
- +[PISharpen_v1 defaultAdjustmentData]
- +[PISlowMotion_v1 adjustmentFormat]
- +[PITrim_v1 adjustmentFormat]
- +[PIVignette_v1 defaultAdjustmentData]
- -[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:settings:error:]
- -[PIDepthEffectApertureAutoCalculator pipelineOutput]
- -[PIDepthEffectApertureAutoCalculator processComputedData:error:]
- -[PIModularPhotosPipelineCache _photosPipelineForSource:options:error:]
- -[PIModularPhotosPipelineCacheEntry initWithPipeline:options:session:]
- -[PIPhotographicStyle init]
- -[PIPhotographicStyle options]
- -[PIPhotosPipeline_v0 addAdjustmentInputChannels:error:]
- -[PIPhotosPipeline_v0 addAutoAdjustmentOuputChannels:error:]
- -[PIPhotosPipeline_v0 addPipelineFilterInputChannels:error:]
- -[PIPhotosPipeline_v1 _buildPostGeometryPipeline:media:error:]
- -[PIPhotosPipeline_v1 addAdjustmentInputChannels:error:]
- -[PIPhotosPipeline_v1 addAutoAdjustmentOuputChannels:error:]
- -[PIPhotosPipeline_v1 addPipelineFilterInputChannels:error:]
- -[PIPhotosPipeline_v1 buildTemporalGeometryPipeline:format:connections:error:]
- -[PIPortrait hasOption:]
- -[PIPortrait options]
- -[PIPortraitAutoCalculator pipelineOutput]
- -[PIPortraitAutoCalculator processComputedData:error:]
- -[PIPortraitSettings .cxx_destruct]
- -[PIPortraitSettings canAdjustAperture]
- -[PIPortraitSettings canAdjustFocusRect]
- -[PIPortraitSettings canAdjustPortraitLightingIntensity]
- -[PIPortraitSettings defaultAperture]
- -[PIPortraitSettings defaultFocusRect]
- -[PIPortraitSettings defaultPortraitLightingIntensity]
- -[PIPortraitSettings depthEnabledAtCapture]
- -[PIPortraitSettings initWithValuesAtCapture:]
- -[PIPortraitSettings maximumAperture]
- -[PIPortraitSettings minimumAperture]
- -[PIPortraitSettings renderingVersion]
- -[PIPortraitSettings supportedPortraitLightingEffects]
- -[PIPortraitSettings supportsPortraitLightingEffect]
- -[PIPortraitSettingsExpressionFunction evaluateWithArguments:error:]
- -[PIPortraitSettingsExpressionFunction format]
- -[PIPortraitSettingsExpressionFunction_v2 format]
- -[PIPortrait_v1 buildPortraitSettings:]
- -[PIPrivatePhotosPipeline_v0 addPipelineFilterInputChannels:error:]
- -[PIPrivatePhotosPipeline_v1 addAdjustmentInputsAndOutputs:]
- -[PIPrivatePhotosPipeline_v1 addPipelineFilterInputsAndOutputs:]
- -[PISemanticStyleAutoCalculator pipelineOutput]
- -[PITextureStyleAutoCalculator pipelineOutput]
- -[_PIPhotographicStyleSettingsExpressionFunction evaluateWithArguments:error:]
- -[_PIPhotographicStyleSettingsExpressionFunction format]
- GCC_except_table1024
- GCC_except_table1352
- GCC_except_table1387
- GCC_except_table1390
- GCC_except_table1391
- GCC_except_table160
- GCC_except_table1623
- GCC_except_table166
- GCC_except_table169
- GCC_except_table171
- GCC_except_table1724
- GCC_except_table1725
- GCC_except_table1729
- GCC_except_table1730
- GCC_except_table1731
- GCC_except_table1736
- GCC_except_table1744
- GCC_except_table176
- GCC_except_table179
- GCC_except_table184
- GCC_except_table187
- GCC_except_table2042
- GCC_except_table2082
- GCC_except_table2612
- GCC_except_table2619
- GCC_except_table2622
- GCC_except_table2633
- GCC_except_table2640
- GCC_except_table2719
- GCC_except_table2721
- GCC_except_table2995
- GCC_except_table2997
- GCC_except_table2999
- GCC_except_table302
- GCC_except_table3091
- GCC_except_table3115
- GCC_except_table313
- GCC_except_table3151
- GCC_except_table3303
- GCC_except_table3312
- GCC_except_table332
- GCC_except_table3340
- GCC_except_table3366
- GCC_except_table338
- GCC_except_table340
- GCC_except_table3435
- GCC_except_table3438
- GCC_except_table3457
- GCC_except_table3462
- GCC_except_table3463
- GCC_except_table3473
- GCC_except_table3507
- GCC_except_table3629
- GCC_except_table364
- GCC_except_table3799
- GCC_except_table3804
- GCC_except_table3814
- GCC_except_table386
- GCC_except_table4018
- GCC_except_table4149
- GCC_except_table4411
- GCC_except_table4415
- GCC_except_table4520
- GCC_except_table4528
- GCC_except_table456
- GCC_except_table4734
- GCC_except_table5190
- GCC_except_table5201
- GCC_except_table5211
- GCC_except_table5260
- GCC_except_table5352
- GCC_except_table5354
- GCC_except_table5502
- GCC_except_table5542
- GCC_except_table5563
- GCC_except_table5659
- GCC_except_table5706
- GCC_except_table5850
- GCC_except_table5950
- GCC_except_table5954
- GCC_except_table5956
- GCC_except_table5957
- GCC_except_table5959
- GCC_except_table5961
- GCC_except_table5963
- GCC_except_table5969
- GCC_except_table5983
- GCC_except_table6052
- GCC_except_table6134
- GCC_except_table6256
- GCC_except_table6266
- GCC_except_table6273
- GCC_except_table6274
- GCC_except_table6275
- GCC_except_table6276
- GCC_except_table6277
- GCC_except_table6278
- GCC_except_table6279
- GCC_except_table6314
- GCC_except_table6320
- GCC_except_table6328
- GCC_except_table6343
- GCC_except_table6391
- GCC_except_table6401
- GCC_except_table6485
- GCC_except_table6493
- GCC_except_table6507
- GCC_except_table6508
- GCC_except_table6509
- GCC_except_table6591
- GCC_except_table6592
- GCC_except_table6782
- GCC_except_table6796
- GCC_except_table6857
- GCC_except_table6858
- GCC_except_table6950
- GCC_except_table6953
- GCC_except_table6957
- GCC_except_table6958
- GCC_except_table6962
- GCC_except_table6963
- GCC_except_table6965
- GCC_except_table6971
- GCC_except_table6980
- GCC_except_table6996
- GCC_except_table7047
- GCC_except_table7100
- GCC_except_table7101
- GCC_except_table7102
- GCC_except_table7103
- GCC_except_table7138
- GCC_except_table724
- GCC_except_table7387
- GCC_except_table7420
- GCC_except_table7476
- GCC_except_table7503
- GCC_except_table7611
- GCC_except_table7613
- GCC_except_table7614
- GCC_except_table7615
- GCC_except_table7617
- GCC_except_table7619
- GCC_except_table7621
- GCC_except_table7624
- GCC_except_table7627
- GCC_except_table7629
- GCC_except_table7630
- GCC_except_table7631
- GCC_except_table7632
- GCC_except_table7634
- GCC_except_table7639
- GCC_except_table764
- GCC_except_table7763
- GCC_except_table7765
- GCC_except_table7766
- GCC_except_table7797
- GCC_except_table7807
- GCC_except_table7810
- GCC_except_table7811
- GCC_except_table7823
- GCC_except_table797
- GCC_except_table8175
- GCC_except_table828
- GCC_except_table8315
- GCC_except_table835
- GCC_except_table8404
- GCC_except_table8423
- GCC_except_table8424
- GCC_except_table8430
- GCC_except_table8565
- GCC_except_table8750
- GCC_except_table8755
- GCC_except_table8770
- GCC_except_table8786
- GCC_except_table8791
- GCC_except_table8797
- GCC_except_table8859
- GCC_except_table8870
- GCC_except_table8875
- GCC_except_table8883
- GCC_except_table8884
- GCC_except_table8885
- GCC_except_table8888
- GCC_except_table8890
- GCC_except_table8894
- GCC_except_table8896
- GCC_except_table8915
- GCC_except_table8919
- GCC_except_table8923
- GCC_except_table8924
- GCC_except_table8932
- GCC_except_table8936
- GCC_except_table8962
- GCC_except_table8963
- GCC_except_table8964
- GCC_except_table8976
- _NUChannelNamePortraitSettings
- _OBJC_CLASS_$_NUMediaGeometryExpression
- _OBJC_CLASS_$_PIPortraitSettings
- _OBJC_CLASS_$_PIPortraitSettingsExpressionFunction
- _OBJC_CLASS_$_PIPortraitSettingsExpressionFunction_v2
- _OBJC_CLASS_$__PIPhotographicStyleSettingsExpressionFunction
- _OBJC_IVAR_$_PIPhotographicStyle._options
- _OBJC_IVAR_$_PIPortrait._options
- _OBJC_IVAR_$_PIPortraitSettings._canAdjustAperture
- _OBJC_IVAR_$_PIPortraitSettings._canAdjustFocusRect
- _OBJC_IVAR_$_PIPortraitSettings._canAdjustPortraitLightingIntensity
- _OBJC_IVAR_$_PIPortraitSettings._defaultAperture
- _OBJC_IVAR_$_PIPortraitSettings._defaultFocusRect
- _OBJC_IVAR_$_PIPortraitSettings._defaultPortraitLightingIntensity
- _OBJC_IVAR_$_PIPortraitSettings._depthEnabledAtCapture
- _OBJC_IVAR_$_PIPortraitSettings._maximumAperture
- _OBJC_IVAR_$_PIPortraitSettings._minimumAperture
- _OBJC_IVAR_$_PIPortraitSettings._renderingVersion
- _OBJC_IVAR_$_PIPortraitSettings._supportedPortraitLightingEffects
- _OBJC_IVAR_$_PIPortraitSettings._supportsPortraitLightingEffect
- _OBJC_METACLASS_$_PIPortraitSettings
- _OBJC_METACLASS_$_PIPortraitSettingsExpressionFunction
- _OBJC_METACLASS_$_PIPortraitSettingsExpressionFunction_v2
- _OBJC_METACLASS_$__PIPhotographicStyleSettingsExpressionFunction
- __OBJC_$_CLASS_METHODS_NUAssetCapability(PIAudioMix|PICinematicVideo|PIPhotographicStyle|PIPortrait)
- __OBJC_$_CLASS_METHODS_PICinematicVideoTimedFocusDisparityProcessor
- __OBJC_$_CLASS_METHODS_PIModularPhotosPipeline
- __OBJC_$_INSTANCE_METHODS_PIPortraitSettings
- __OBJC_$_INSTANCE_METHODS_PIPortraitSettingsExpressionFunction
- __OBJC_$_INSTANCE_METHODS_PIPortraitSettingsExpressionFunction_v2
- __OBJC_$_INSTANCE_METHODS__PIPhotographicStyleSettingsExpressionFunction
- __OBJC_$_INSTANCE_VARIABLES_PIPortraitSettings
- __OBJC_$_PROP_LIST_PIPortraitSettings
- __OBJC_CLASS_PROTOCOLS_$_PICinematicVideo
- __OBJC_CLASS_PROTOCOLS_$_PIPhotographicStyle
- __OBJC_CLASS_PROTOCOLS_$_PIPortrait
- __OBJC_CLASS_RO_$_PIPortraitSettings
- __OBJC_CLASS_RO_$_PIPortraitSettingsExpressionFunction
- __OBJC_CLASS_RO_$_PIPortraitSettingsExpressionFunction_v2
- __OBJC_CLASS_RO_$__PIPhotographicStyleSettingsExpressionFunction
- __OBJC_METACLASS_RO_$_PIPortraitSettings
- __OBJC_METACLASS_RO_$_PIPortraitSettingsExpressionFunction
- __OBJC_METACLASS_RO_$_PIPortraitSettingsExpressionFunction_v2
- __OBJC_METACLASS_RO_$__PIPhotographicStyleSettingsExpressionFunction
- ___123+[PICinematicVideoTimedFocusDisparityProcessor usingSharedCinematographyScriptSnapshotForDictionaryRepresentation:perform:]_block_invoke
- ___54-[PIPortraitAutoCalculator processComputedData:error:]_block_invoke
- ___55-[PIPhotosPipeline_v1 buildAudioPipeline:format:error:]_block_invoke_2
- ___55-[PIPhotosPipeline_v1 buildAudioPipeline:format:error:]_block_invoke_3
- ___62+[PIModularPhotosPipeline_v0 controlDataWithCurvesAdjustment:]_block_invoke
- ___69+[PIModularPhotosPipeline_v0 controlDataWithPortraitVideoAdjustment:]_block_invoke_2
- ___70+[PIModularPhotosPipeline_v0 controlDataWithCropStraightenAdjustment:]_block_invoke
- ___70+[PIModularPhotosPipeline_v0 controlDataWithSelectiveColorAdjustment:]_block_invoke
- ___70+[PIModularPhotosPipeline_v0 controlDataWithSelectiveColorAdjustment:]_block_invoke_2
- ___78-[PIPhotosPipeline_v1 buildTemporalGeometryPipeline:format:connections:error:]_block_invoke
- ___85-[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:settings:error:]_block_invoke
- ___block_descriptor_32_e72_"NUChannelPortRef"32?0"<NUMutablePipeline>"8"NUChannelPortRef"16^24l
- ___block_descriptor_56_e8_32s40bs_e59_v24?0"PFPosterOrientedLayout"8"PFPosterOrientedLayout"16ls32l8s40l8
- ___block_descriptor_56_ea8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40bs_e20_v16?0"NUResponse"8ls40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56r_e26_B24?0"<NUPipeline>"8^16lr56l8u64l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e72_"NUChannelPortRef"32?0"<NUMutablePipeline>"8"NUChannelPortRef"16^24ls32l8s40l8s48l8s56l8s64l8
CStrings:
+ "+[PILivePhotoKeyFrame_v1 adjustmentDescriptorForAsset:]"
+ "+[PIModularPhotosPipeline buildPhotosPipelineVersion:forAsset:options:error:]"
+ "+[PIModularPhotosPipeline withPhotosPipelineForComposition:options:block:error:]"
+ "+[PISignedMetadata _developmentSignedBoxForRequest:identity:error:]"
+ "+[PISignedMetadata _developmentSigningIdentityWithError:]"
+ "+[PISignedMetadata _insertBox:intoImageAtURL:error:]"
+ "+[PISignedMetadata _signingRequestForImageAtURL:error:]"
+ "+[PISignedMetadata signImageAtURL:completion:]"
+ "-[PICinematicVideo initWithOptions:]"
+ "-[PICinematicVideo inputChannels]"
+ "-[PICinematicVideoTimedFocusDisparityProcessor cinematographySnapshotDictionaryForVideoURLString:cinematographyState:error:]"
+ "-[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:controlData:error:]"
+ "-[PILivePhotoEffect_v1 mediaFormatWithAudioChannel:]"
+ "-[PILivePhotoKeyFrame_v1 initWithAsset:]"
+ "-[PILivePhotoKeyFrame_v1 initWithOptions:]"
+ "-[PILivePhotoKeyFrame_v1 inputChannels]"
+ "-[PIModularAutoCalculator controlFormatForPipeline:input:error:]"
+ "-[PIModularAutoCalculator resultWithPipeline:asset:error:]"
+ "-[PIModularPhotosPipelineCache _cacheEntryForSource:options:error:]"
+ "-[PIModularPhotosPipelineCacheEntry initWithPipeline:asset:options:session:]"
+ "-[PIPhotographicStyle initWithOptions:]"
+ "-[PIPhotosPipeline imageOutputFormatWithInputFormat:error:]"
+ "-[PIPhotosPipeline livePhotoOutputFormatWithInputFormat:error:]"
+ "-[PIPhotosPipeline videoOutputFormatWithInputFormat:error:]"
+ "-[PIPortrait initWithOptions:]"
+ "-[PIPortrait inputChannels]"
+ "-[PIPrivatePhotosPipeline buildPipeline:error:]"
+ "-[PIPrivatePhotosPipeline initWithPipelineDescriptor:]"
+ "-[PISlowMotion_v1 initWithAsset:]"
+ "-[PISlowMotion_v1 initWithOptions:]"
+ "..:<"
+ "..:<adjustment"
+ "..:<applyAsMetadata"
+ "/:adjustment.grain.enabled"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Pipeline/API/PILivePhotoKeyFrame.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PISignedMetadata.m"
+ ":<adjustment.effect"
+ ":<adjustment.rect"
+ ":<gainMap"
+ ":>adjustment.enabled"
+ ":lightingAdjustment.effect"
+ "@\"NUChannelPortRef\"32@?0@\"<NUMutablePipeline>\"8@\"NUChannelPortRef\"16@\"NSArray\"24"
+ "@\"NUChannelPortRef\"40@?0@\"<NUMutablePipeline>\"8@\"NUChannelPortRef\"16@\"NSArray\"24^@32"
+ "B16@?0@\"NUChannel\"8"
+ "B32@?0@\"<NUPipeline>\"8@\"<NUAsset>\"16^@24"
+ "CinSnapshot.LoadScriptFromVideo"
+ "CinSnapshot.Shared"
+ "Cinematography snapshot and videoURL are both missing from control data"
+ "Exported %@ without signed metadata: %@"
+ "Failed to add input channels"
+ "Failed to add output channels"
+ "Failed to add photographicStyleApply pipeline"
+ "Failed to add the signature to the AI Marker Box"
+ "Failed to build photos pipeline from source"
+ "Failed to build the AI Marker Box"
+ "Failed to compute the Content Hash of the exported image"
+ "Failed to connect temporal output to geometry pipeline"
+ "Failed to customize Photos pipeline"
+ "Failed to generate adjustment descriptor"
+ "Failed to generate output media format"
+ "Failed to insert the AI Marker Box"
+ "Failed to load the development signing key"
+ "Failed to read the development signing identity"
+ "Failed to sign the AI Marker Box"
+ "Failed to update input channels"
+ "Failed to update output channels"
+ "Failed to write the signed image"
+ "Input has no default data"
+ "Missing pipeline input"
+ "Not a control data input"
+ "PISignedMetadata.signing"
+ "PISignedMetadataDevelopmentSigningCertificate"
+ "PISignedMetadataDevelopmentSigningDelay"
+ "PISignedMetadataDevelopmentSigningIdentity"
+ "PISignedMetadataDevelopmentSigningKey"
+ "PI_SIGNED_METADATA_ENABLED"
+ "Signed metadata: leaving %{public}@ unsigned, no signing service in this build"
+ "Signed metadata: leaving %{public}@ unsigned, signing is turned off"
+ "Signed metadata: signed %{public}@ with %{public}s (listed items: %lu, box: %lu bytes)"
+ "Signing request timed out"
+ "Subclass must specify a pipeline input or override this method"
+ "TextureStyleGrain"
+ "The development signing identity defaults are not valid base64"
+ "[asset hasCapability:NUAssetCapability.cinematicVideo]"
+ "[asset hasCapability:NUAssetCapability.slowMotion]"
+ "asset.type == NUAssetTypeLivePhoto"
+ "autoCropStraighten:>auto.enabled"
+ "certificate.der"
+ "cinematographyScriptSnapshot#%@"
+ "cinematographyScriptSnapshotFromAdjustment#%@"
+ "cinematographySnapshotDictionary#%@"
+ "edit"
+ "generation=%lu"
+ "generation=%lu result=%{public}s"
+ "inputName != nil"
+ "key.bin"
+ "livePhotoEffectNoAudio"
+ "map"
+ "maxPixelCount"
+ "media:>output.audio!"
+ "poolHit"
+ "poolMiss"
+ "the development identity"
+ "the signing service"
+ "timedFocusDisparityProcessor:<cinematographyState"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "vignette:<media"
+ "vignette:>media"
- "%@/noiseReduction:>default"
- "+[PILivePhotoEffect_v1 mediaFormat]"
- "+[PIModularPhotosPipeline buildPhotosPipelineVersion:forSource:options:error:]"
- "+[PIPortraitAutoCalculator portraitSettingsWithExifProperties:makerNote:disparityMetadata:depthData:error:]"
- "-[PICinematicVideoTimedFocusDisparityProcessor computeDataWithInputs:settings:error:]"
- "-[PIModularAutoCalculator pipelineOutput]"
- "-[PIModularPhotosPipelineCache _photosPipelineForSource:options:error:]"
- "-[PIModularPhotosPipelineCacheEntry initWithPipeline:options:session:]"
- "-[PIPhotographicStyle init]"
- "-[PIPortraitSettings initWithValuesAtCapture:]"
- "-[PIPortraitSettingsExpressionFunction evaluateWithArguments:error:]"
- "-[_PIPhotographicStyleSettingsExpressionFunction evaluateWithArguments:error:]"
- "..:<media.gainMap"
- "/:<photographicStyle"
- "/:>defaultDefinition"
- "/:>defaultNoiseReduction"
- "/:>defaultPhotographicStyle"
- "/:>defaultSharpen"
- "/:>defaultVignette"
- "/:>portraitSettings"
- "/:adjustment.grainIntensity"
- "/:default"
- "/:defaultPhotographicStyle"
- "/asset:>media.image.disparity"
- ":>default"
- ":>settings"
- "Asset has no cinematic video capability"
- "Asset is not a valid portrait"
- "B24@?0@\"<NUPipeline>\"8^@16"
- "CinEverywhere: Created cinematography snapshot with generation %lu from the source asset"
- "Cinematography snapshot is missing from settings"
- "Failed to add PIPhotographicStyleApplyV1 pipeline"
- "Failed to add auto adjustment inputs"
- "Failed to add image output media channel"
- "Failed to add inputs"
- "Failed to add live photo output media channel"
- "Failed to add pipeline filter inputs"
- "Failed to add pipeline filters output"
- "Failed to add pipeline local filters output"
- "Failed to add video output media channel"
- "Failed to assign auto adjustment port"
- "Failed to generate image output container format"
- "Failed to generate live-photo output container format"
- "Failed to generate video output container format"
- "Failed to setup style revert pipeline"
- "Invalid MakerNote metadata"
- "Missing MakerNote metadata"
- "Missing default style output"
- "_PIPhotographicStyleSettingsExpressionFunction"
- "adjust/definition:>default"
- "adjust/sharpen:>default"
- "arguments.count == 4"
- "arguments[2].format.channelType == NUChannelTypeMetadata"
- "arguments[3].format.channelType == NUChannelTypeControl"
- "canAdjustAperture"
- "cinematographyScriptSnapshot"
- "defaultAdjustment != nil"
- "defaultAdjustmentPort != nil"
- "defaultDefinition"
- "defaultNoiseReduction"
- "defaultPhotographicStyle"
- "defaultSharpen"
- "defaultVignette"
- "image/adjust/definition:>default"
- "image/adjust/sharpen:>default"
- "image/post-geometry/vignette:>default"
- "photograhicStyleRevertBypass"
- "photographicStyleApply:<adjustment"
- "photographicStyleApply:<style"
- "photographicStyleLearn:<adjustment"
- "photographicStyleLearn:<linearThumbnail"
- "photographicStyleLearn:<portraitMatte"
- "photographicStyleLearn:<primary"
- "photographicStyleLearn:<skinMatte"
- "photographicStyleLearn:<skyMatte"
- "photographicStyleLearn:>default"
- "photographicStyleLearn:default"
- "portrait:>settings"
- "portraitSettings"
- "portraitSettings:<disparity"
- "portraitSettings:<primary"
- "portraitSettings:>settings"
- "post-geometry/vignette:>default"
- "resetOrientation:applyAsMetadata"
```
