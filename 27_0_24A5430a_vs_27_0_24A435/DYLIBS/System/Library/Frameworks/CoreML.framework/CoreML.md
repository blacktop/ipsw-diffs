## CoreML

> `/System/Library/Frameworks/CoreML.framework/CoreML`

```diff

 3600.25.2.0.0
-  __TEXT.__text: 0x704650
+  __TEXT.__text: 0x70467c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x10198
+  __TEXT.__objc_methlist: 0x10200
   __TEXT.__const: 0x51483
   __TEXT.__dlopen_cstrs: 0x21e
   __TEXT.__cstring: 0x2e28c

   __TEXT.__swift5_capture: 0xf88
   __TEXT.__swift_as_ret: 0x110
   __TEXT.__oslogstring: 0xb288
-  __TEXT.__gcc_except_tab: 0x3aac0
+  __TEXT.__gcc_except_tab: 0x3aab0
   __TEXT.__ustring: 0x204
-  __TEXT.__unwind_info: 0x10540
+  __TEXT.__unwind_info: 0x10538
   __TEXT.__eh_frame: 0x54d4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x74c8
+  __DATA_CONST.__objc_selrefs: 0x7510
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_arraydata: 0x160
   __DATA_CONST.__got: 0x11a0
   __AUTH_CONST.__const: 0x20f88
   __AUTH_CONST.__cfstring: 0xd360
-  __AUTH_CONST.__objc_const: 0x22f30
+  __AUTH_CONST.__objc_const: 0x22ff8
   __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x978
Functions:
~ __GLOBAL__I_000102 : 144 -> 148
~ __ZNSt3__16vectorINS_4pairIPFvPKvES3_EENS_9allocatorIS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_ : 228 -> 244
~ -[MLModelConfiguration init] : 8 -> 16
~ -[MLOptimizationHints init] : 84 -> 88
~ -[MLModelAssetResourceFactory initWithImpl:] : 300 -> 288
~ -[MLModelConfiguration copyWithZone:] : 768 -> 780
~ +[MLModel modelWithContentsOfURL:error:] : 252 -> 240
~ -[MLModelConfiguration .cxx_destruct] : 184 -> 164
~ ___60-[MLModelAssetResourceFactory modelWithConfiguration:error:]_block_invoke : 164 -> 160
~ +[MLPredictionOptions defaultOptions] : 68 -> 72
~ -[MLModel nextPredictionRequestID] : 16 -> 44
~ -[MLPredictionOptions setE5rtStreamReuseExpectation:] : 16 -> 40
~ -[MLOutputBackingsVerifier verifyOutputBackings:predictionUsesBatch:error:] : 768 -> 748
~ __ZN12_GLOBAL__N_127makeProgramWithMemoryLayoutENSt3__110shared_ptrIKN3MIL9IRProgramEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP18MLModelDescriptionPU15__autoreleasingP7NSError : 3628 -> 3624
~ __ZN8IArchive13nestedArchiveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 520 -> 524
~ __ZNK8Archiver17_IArchiveDiskImpl16getNestedArchiveERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 324 -> 316
~ -[MLTreeEnsembleClassifier classify:options:error:] : 764 -> 772
~ ___24-[MLReporter logMetric:]_block_invoke : 16 -> 36
~ __ZNSt3__16vectorImNS_9allocatorImEEE7reserveEm : 180 -> 176
~ __ZN6CoreML16MultiArrayBuffer24stridesForConiguousArrayERKNSt3__16vectorImNS1_9allocatorImEEEENS_12StorageOrderE : 220 -> 224
~ __ZNK6CoreML14SafeMultipliesImEclERKmS3_ : 136 -> 132
~ __ZN6CoreML16MultiArrayBufferC2ERKNSt3__16vectorImNS1_9allocatorImEEEES7_NS_10ScalarTypeEm : 1128 -> 1132
~ __ZN14StorageManager14mutableStorageEv : 904 -> 892
~ +[MLFeatureTypeUtils featureTypeForObject:] : 468 -> 484
~ +[MLFeatureValue featureValueOfType:fromObject:error:] : 592 -> 596
~ -[MLDictionaryFeatureProvider featureValueForName:] : 28 -> 8
~ -[MLRegressor predictionFromFeatures:options:error:] : 172 -> 192
~ -[MLPredictionOptions setAneQoS:] : 16 -> 20
~ -[MLFeatureVectorizer predictionTypeForKTrace] : 32 -> 20
~ -[MLMultiArray(Attributes) mutableBytes] : 112 -> 120
~ -[MLDictionaryFeatureProvider initWithDictionary:error:] : 584 -> 588
~ -[MLModel predictionFromFeatures:error:] : 260 -> 256
~ -[MLPipelineRegressor regress:options:error:] : 372 -> 380
~ __ZN19ElapsedTimeRecorderC2EP17MLPredictionEventyyyy : 192 -> 208
~ -[MLMultiArray .cxx_construct] : 16 -> 24
~ -[MLFeatureDescription initWithName:type:optional:contraints:] : 756 -> 760
~ +[MLModelIOUtils populateConstraintsForFeatureDescription:] : 1124 -> 1120
~ -[MLFeatureDescription name] : 32 -> 24
~ -[MLModelDescription initFromModelDescriptionSpecification:] : 896 -> 912
~ __ZN29_MLModelMetadataSpecificationC1ERKN6CoreML13Specification8MetadataE : 172 -> 148
~ __ZN6CoreML13Specification8MetadataC2ERKS1_ : 496 -> 520
~ __ZN6google8protobuf5Arena20CreateInArenaStorageINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEJRS9_EEEvPT_PS1_DpOT0_ : 144 -> 168
~ __ZN6google8protobuf8internal16InternalMetadataD2Ev : 492 -> 480
~ +[MLLogging coreChannel] : 8 -> 20
~ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEC1EPKcj : 448 -> 452
~ __ZNK8Archiver17_IArchiveDiskImpl10createBlobERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 2884 -> 2880
~ __ZN8Archiver14_IDataBlobImplC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 132 -> 136
~ -[MLLoaderEvent extractAndSetModelDetailsFromArchive:] : 3096 -> 3084
~ __ZN8Archiver14_IDataBlobImpl8asStreamEv : 472 -> 464
~ -[MLModelAssetDescription initWithRawModelDescription:] : 1008 -> 984
~ -[MLModelConfiguration setParentModelName:] : 24 -> 32
~ -[MLOptimizationHints copyWithZone:] : 136 -> 112
~ __ZN8IArchiveC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN8Archiver10FileFormatE : 224 -> 220
~ __ZN8Archiver17_IArchiveDiskImplC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_10FileFormatE : 2112 -> 2108
~ __ZNK8IArchive16hasNestedArchiveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 152 -> 156
~ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEC1ERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj : 476 -> 480
~ __ZN6google8protobuf8internal14ArenaStringPtr22DestroyNoArenaSlowPathEv : 100 -> 108
~ __ZN6CoreML13Specification18FeatureDescriptionD0Ev : 56 -> 80
~ __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap12InsertUniqueEmPNSA_4NodeE : 268 -> 252
~ +[MLModelDescription metadataWithFormat:] : 780 -> 764
~ __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap5clearEv : 268 -> 276
~ __ZN6CoreML13Specification8MetadataD2Ev : 208 -> 232
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification8MetadataENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 28 -> 24
~ -[MLLayerPath init] : 28 -> 48
~ __ZL26conformedStateDescriptionsP12NSDictionaryIP8NSStringP20MLFeatureDescriptionES5_ : 480 -> 456
~ -[MLFeatureDescription type] : 8 -> 32
~ __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap13iterator_baseIKNS0_7MapPairIS8_S8_EEEppEv : 304 -> 300
~ _MLLoggingGetCoreChannel : 100 -> 96
~ __ZN6CoreML13Specification16ModelDescriptionD2Ev : 288 -> 276
~ __ZN6google8protobuf16RepeatedPtrFieldIN6CoreML13Specification18FeatureDescriptionEED2Ev : 72 -> 84
~ __ZN6google8protobuf16RepeatedPtrFieldIN6CoreML13Specification19FunctionDescriptionEED2Ev : 80 -> 64
~ -[MLPredictionEvent init] : 192 -> 176
~ __ZN6CoreML13Specification18FeatureDescriptionD2Ev : 220 -> 240
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase13DestroyProtosEv : 152 -> 128
~ __ZN6CoreML13Specification11FeatureTypeD2Ev : 148 -> 136
~ __ZN6CoreML13Specification9SizeRangeD2Ev : 116 -> 128
~ __ZN6CoreML13Specification11FeatureType10clear_TypeEv : 544 -> 560
~ -[MLModel(ModelAsset) initInterfaceAndMetadataWithCompiledArchive:error:] : 324 -> 308
~ __ZN6CoreML13Specification21DictionaryFeatureType13clear_KeyTypeEv : 176 -> 188
~ -[MLMultiArray objectAtIndexedSubscript:] : 140 -> 120
~ -[MLDelegateModel _predictionFromFeatures:usingState:options:error:] : 1092 -> 1112
~ ___56-[MLMultiArray(ScopedBufferAccess) getBytesWithHandler:]_block_invoke : 36 -> 32
~ __ZNK6CoreML16MultiArrayBuffer14offsetForIndexExNS_12StorageOrderE : 164 -> 152
~ __ZN19ElapsedTimeRecorderD2Ev : 112 -> 128
~ __ZNK6CoreML16MultiArrayBuffer10loadBufferEv : 764 -> 760
~ __ZN6CoreML16MultiArrayBufferD2Ev : 140 -> 144
~ __ZNK14StorageManager7storageEv : 128 -> 124
~ __ZN6CoreML16MultiArrayBufferD1Ev : 32 -> 4
~ -[MLMultiArray .cxx_destruct] : 84 -> 80
~ __ZNSt3__120__shared_ptr_pointerIPhZN6CoreML16MultiArrayBufferC1ERKNS_6vectorImNS_9allocatorImEEEES9_NS2_10ScalarTypeEmE3$_1NS5_IhEEE21__on_zero_shared_weakEv : 16 -> 20
~ -[MLMultiArray(ScopedBufferAccess) getMutableBytesWithHandler:] : 336 -> 344
~ -[MLDictionaryFeatureProvider .cxx_destruct] : 84 -> 80
~ -[MLFeatureValue .cxx_destruct] : 92 -> 88
~ -[MLMultiArray(Attributes) bytes] : 136 -> 124
~ __ZN6CoreML13TreeEnsembles8Internal7predictEPdPKhPKd : 45488 -> 45484
~ __ZN6CoreML13TreeEnsembles8InternalL30apply_postevaluation_transformEPdNS_16TreeEnsembleBase23PostEvaluationTransformEm : 408 -> 416
~ __ZN6CoreML8Archiver21MMappedContentManagerD2Ev : 160 -> 140
~ -[MLFeatureValue doubleValue] : 44 -> 48
~ ___45-[MLPredictionEvent maybeLogPredictionEvent:]_block_invoke : 464 -> 468
~ ___60-[MLFeatureVectorizer predictionFromFeatures:options:error:]_block_invoke : 40 -> 32
~ -[MLTreeEnsembleRegressor regress:options:error:] : 1120 -> 1116
~ -[MLMultiArray count] : 92 -> 96
~ +[MLFeatureProviderUtils _vectorizeWithoutSizeCheckFeatureValues:intoDoubleVector:stride:error:] : 844 -> 840
~ -[MLMultiArray(RawAccess) multiArrayBuffer] : 88 -> 84
~ __ZNSt3__120__shared_ptr_pointerIPhZN6CoreML16MultiArrayBufferC1ES1_RKNS_6vectorImNS_9allocatorImEEEES9_NS2_10ScalarTypeEE3$_0NS5_IhEEE21__on_zero_shared_weakEv : 32 -> 16
~ __ZNK6CoreML16MultiArrayBuffer13vectorizeIntoERS0_NS_12StorageOrderE : 916 -> 940
~ ___49-[MLTreeEnsembleRegressor regress:options:error:]_block_invoke : 28 -> 44
~ -[MLRegressorResult .cxx_destruct] : 84 -> 68
~ -[MLLazyUnionFeatureProvider .cxx_destruct] : 84 -> 80
~ ___63+[MLMultiArray(ConvenientConstruction) doubleVectorWithValues:]_block_invoke_2 : 116 -> 128
~ -[MLModelEngine modelDescription] : 16 -> 20
~ -[MLNeuralNetworkEngine bindOutputBuffers:outputBackings:automaticOutputBackingMode:directlyBoundOutputFeatureNames:error:] : 2332 -> 2328
~ __ZN6CoreMLL19vectorizeMultiArrayIffEEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 452 -> 456
~ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbNS_4lessIS6_EENS4_INS_4pairIKS6_bEEEEEixERSA_ : 212 -> 192
~ __ZNK6CoreML16MultiArrayBuffer8copyIntoERS0_ : 13844 -> 13848
~ -[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:deallocator:mutableShapedBufferProvider:error:] : 1592 -> 1608
~ -[MLNeuralNetworkEngine populateOutputs:outputBackings:directlyBoundOutputFeatureNames:error:] : 2132 -> 2116
~ -[MLNeuralNetworkEngine resetSizesNoAutoRelease:error:] : 5392 -> 5376
~ -[MLNeuralNetworkEngine verifyInputs:error:] : 392 -> 408
~ -[MLMultiArray setObject:atIndexedSubscript:] : 180 -> 164
~ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEP17espresso_buffer_tNS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEixEOS6_ : 204 -> 188
~ __ZNSt3__120__shared_ptr_pointerIPhZ105-[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:deallocator:mutableShapedBufferProvider:error:]E3$_0NS_9allocatorIhEEE16__on_zero_sharedEv : 88 -> 104
~ ___44-[MLNeuralNetworkEngine verifyInputs:error:]_block_invoke : 40 -> 56
~ __ZNSt3__120__shared_ptr_pointerIPhZ105-[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:deallocator:mutableShapedBufferProvider:error:]E3$_0NS_9allocatorIhEEE21__on_zero_shared_weakEv : 16 -> 32
~ ___67-[MLNeuralNetworkEngine evaluateInputs:options:verifyInputs:error:]_block_invoke.182 : 84 -> 104
~ -[MLFeatureValue type] : 20 -> 36
~ -[MLPredictionEventMetric dictionaryRepresentation] : 428 -> 412
~ -[MLTreeEnsembleClassifier .cxx_destruct] : 180 -> 184
~ __ZNSt3__120__shared_ptr_pointerIPN8Archiver11MMappedFileENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE16__on_zero_sharedEv : 40 -> 44
~ __ZN8Archiver11MMappedFileD0Ev : 68 -> 60
~ ___51-[MLTreeEnsembleClassifier classify:options:error:]_block_invoke : 44 -> 40
~ +[MLMultiArray(ConvenientConstruction) doubleVectorWithValues:] : 424 -> 428
~ -[MLLazyUnionFeatureProvider initWithFeaturesFrom:addedToFeaturesFrom:] : 188 -> 196
~ -[MLModel(Utilities) vectorizeInput:error:] : 196 -> 188
~ +[MLFeatureProviderUtils _featureValuesForNames:providedBy:error:] : 388 -> 384
~ ___52-[MLMultiArrayShapeConstraint isAllowedShape:error:]_block_invoke : 348 -> 352
~ +[MLState emptyState] : 96 -> 92
~ -[MLMultiArray setObject:forKeyedSubscript:] : 228 -> 212
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE7reserveEm : 196 -> 180
~ -[MLMultiArray numberAtOffset:] : 284 -> 296
~ -[MLE5ProgramLibrary modelConfiguration] : 20 -> 12
~ +[MLModelAsset modelAssetWithURL:error:] : 180 -> 176
~ -[MLModelConfiguration initWithComputeUnits:] : 404 -> 416
~ +[MLModelAssetResourceFactory resourceFactoryWithModelURL:error:] : 168 -> 172
~ -[MLModelAssetResourceFactoryOnDiskImpl initWithModelURL:error:] : 144 -> 136
~ -[MLModelAssetModelVendor initWithResourceFactory:] : 176 -> 184
~ -[MLModelAssetModelStructureVendor initWithResourceFactory:] : 148 -> 132
~ -[MLModelConfiguration setComputeUnits:] : 36 -> 16
~ -[MLE5ExecutionStreamOperation functionName] : 36 -> 24
~ -[MLModelConfiguration(E5RT) setE5rtMutableMILWeightURLs:] : 92 -> 68
~ -[MLOptimizationHints reshapeFrequency] : 8 -> 28
~ _MLLoggingAllowsInstrumentation : 588 -> 596
~ +[MLArchivingUtils codedObjectURLFromInputArchiver:] : 292 -> 296
~ __ZrsR8IArchiveR11MLModelType : 248 -> 244
~ +[MLArchivingUtils parseModelArchive:modelType:compilerVersion:modelVersion:error:] : 692 -> 696
~ +[MLLoader _loadWithModelLoaderFromArchive:configuration:loaderEvent:useUpdatableModelLoaders:error:] : 968 -> 972
~ __ZNK8Archiver17_IArchiveDiskImpl12isENMLFormatEv : 32 -> 28
~ __ZN8IArchive6rewindEv : 204 -> 188
~ -[MLModelAssetDescription initWithCompiledModelArchive:error:] : 172 -> 180
~ -[MLModelDescription(RawModelDescription) initFromRawCompiledModelArchive:error:] : 192 -> 204
~ __ZN8Archiver11MMappedFileD2Ev : 280 -> 276
~ __ZNSt3__120__shared_ptr_pointerIPN8Archiver11MMappedFileENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 24 -> 28
~ -[MLModel .cxx_destruct] : 136 -> 124
~ -[MLModelDescription .cxx_destruct] : 268 -> 248
~ -[MLLayerPath .cxx_destruct] : 76 -> 72
~ -[MLPredictionEvent .cxx_destruct] : 144 -> 124
~ -[MLPredictionEventMetric .cxx_destruct] : 116 -> 108
~ +[MLModelIOUtils deserializeInterfaceFormat:archive:error:] : 1280 -> 1284
~ __ZN6google8protobuf11MessageLite20ParseFromCodedStreamEPNS0_2io16CodedInputStreamE : 1136 -> 1144
~ __ZN6CoreML13Specification16ModelDescription14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 1356 -> 1344
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase14InternalExtendEi : 256 -> 228
~ __ZN6google8protobuf8internal12ParseContext12ParseMessageEPNS0_11MessageLiteEPKc : 168 -> 188
~ -[MLModelTypeRegistry init] : 68 -> 72
~ -[MLOptimizationHints hotHandDuration] : 24 -> 12
~ ___MLLoggingGetCoreChannel_block_invoke : 148 -> 164
~ +[MLModelIOUtils deserializeVersionInfoFromArchive:error:] : 276 -> 280
~ __ZN6google8protobuf24ZeroCopyCodedInputStream4NextEPPKvPi : 176 -> 152
~ __ZN6CoreML13Specification16ModelDescription5ClearEv : 584 -> 600
~ __ZN6google8protobuf8internal18EpsCopyInputStream13DoneWithCheckEPPKci : 148 -> 120
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase18AddOutOfLineHelperEPv : 128 -> 120
~ ___37+[MLModelTypeRegistry sharedInstance]_block_invoke : 68 -> 56
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification18FeatureDescriptionEJEEEPT_PS1_DpOT0_ : 148 -> 140
~ __ZN6google8protobuf8internal12ParseContext28ReadSizeAndPushLimitAndDepthEPKcPi : 164 -> 140
~ __ZN6CoreML13Specification18FeatureDescription14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 572 -> 564
~ __ZN6google8protobuf8internal10VerifyUTF8ENS0_20stringpiece_internal11StringPieceEPKc : 88 -> 84
~ __ZN6google8protobuf8internal23IsStructurallyValidUTF8EPKci : 704 -> 712
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification16ArrayFeatureTypeEJEEEPT_PS1_DpOT0_ : 204 -> 176
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIyLb0EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 192 -> 184
~ __ZN6google8protobuf13RepeatedFieldIyE7ReserveEi : 284 -> 288
~ __ZN6CoreML13Specification17DoubleFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 308 -> 312
~ __ZN6CoreML13Specification8Metadata14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 1672 -> 1668
~ __ZN6CoreML6ResultC1Ev : 152 -> 180
~ __ZN6google8protobuf2io16CodedInputStreamD1Ev : 152 -> 160
~ -[MLModelAssetDescription defaultFunctionNameOrEmptyString] : 12 -> 32
~ +[MLModel generateSignpostId] : 92 -> 84
~ +[MLTreeEnsembleRegressor loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 780 -> 788
~ -[MLModel predictionTypeForKTrace] : 16 -> 12
~ __ZNSt3__120__shared_ptr_pointerIPNS_14basic_ifstreamIcNS_11char_traitsIcEEEENS_10shared_ptrINS_13basic_istreamIcS3_EEE27__shared_ptr_default_deleteIS8_S4_EENS_9allocatorIS4_EEE16__on_zero_sharedEv : 40 -> 64
~ __ZN8Archiver14_IDataBlobImplD2Ev : 104 -> 112
~ __ZN8Archiver14_IDataBlobImplD1Ev : 24 -> 28
~ __ZNSt3__120__shared_ptr_emplaceIN8Archiver14_IDataBlobImplENS_9allocatorIS2_EEE16__on_zero_sharedEv : 32 -> 36
~ __ZNSt3__120__shared_ptr_emplaceIN8Archiver17_IArchiveDiskImplENS_9allocatorIS2_EEE16__on_zero_sharedEv : 32 -> 24
~ -[MLOptimizationHints setReshapeFrequency:] : 12 -> 16
~ __ZNK8Archiver17_IArchiveDiskImpl11storageTypeEv : 28 -> 24
~ +[MLLoader _loadModelFromArchive:configuration:modelVersion:compilerVersion:loaderEvent:useUpdatableModelLoaders:loadingClasses:error:] : 1880 -> 1884
~ -[MLLoaderEvent .cxx_destruct] : 312 -> 308
~ +[MLTreeEnsembleClassifier loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 1736 -> 1744
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6resizeEm : 412 -> 428
~ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEED2Ev : 56 -> 72
~ __ZrsIxER8IArchiveS1_RNSt3__16vectorIT_NS2_9allocatorIS4_EEEE : 168 -> 160
~ __ZNSt3__120__shared_ptr_pointerIPNS_14basic_ifstreamIcNS_11char_traitsIcEEEENS_10shared_ptrINS_13basic_istreamIcS3_EEE27__shared_ptr_default_deleteIS8_S4_EENS_9allocatorIS4_EEE21__on_zero_shared_weakEv : 20 -> 28
~ __ZNSt3__120__shared_ptr_emplaceIN8Archiver17_IArchiveDiskImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 12 -> 8
~ -[MLModel modelDescription] : 28 -> 8
~ __ZNSt3__16vectorIxNS_9allocatorIxEEE6resizeEm : 288 -> 304
~ -[MLVersionInfo .cxx_destruct] : 20 -> 16
~ -[MLModelAsset .cxx_destruct] : 128 -> 140
~ -[MLModelAssetModelStructureVendor .cxx_destruct] : 76 -> 68
~ -[MLModelAssetDescriptionVendor .cxx_destruct] : 68 -> 72
~ -[MLModelAssetResourceFactory .cxx_destruct] : 100 -> 104
~ __ZNK8IArchive4blobERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 128 -> 124
~ __ZNK8Archiver17_IArchiveDiskImpl7getBlobERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 244 -> 240
~ __ZN8Archiver14_IDataBlobImpl13asMMappedFileEv : 528 -> 532
~ __ZNK8Archiver11MMappedFile4dataEv : 32 -> 20
~ -[MLModelDescription inputDescriptionsByName] : 8 -> 28
~ __ZN6google8protobuf8internal17PackedInt64ParserEPvPKcPNS1_12ParseContextE : 360 -> 356
~ __ZN6google8protobuf8internal11VarintParseIyEEPKcS4_PT_ : 148 -> 124
~ __ZN6google8protobuf8internal18EpsCopyInputStream10ReadStringEPKciPNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE : 352 -> 348
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification17DoubleFeatureTypeEJEEEPT_PS1_DpOT0_ : 144 -> 148
~ __ZN6google8protobuf8internal12MapEntryImplIN6CoreML13Specification7MILSpec43Function_BlockSpecializationsEntry_DoNotUseENS0_11MessageLiteENSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEENS5_5BlockELNS1_14WireFormatLite9FieldTypeE9ELSH_11EE6ParserINS1_12MapFieldLiteIS6_SE_SF_LSH_9ELSH_11EEENS0_3MapISE_SF_EEED2Ev : 120 -> 144
~ __ZN6google8protobuf8internal18EpsCopyInputStream12DoneFallbackEii : 832 -> 808
~ __ZNK6CoreML13Specification16ModelDescription13IsInitializedEv : 36 -> 28
~ __ZN6google8protobuf2io25CopyingInputStreamAdaptorD2Ev : 172 -> 168
~ __ZN6CoreML18numericArrayToObjCIN6google8protobuf13RepeatedFieldIxEExEEP7NSArrayIP8NSNumberERKT_ : 184 -> 192
~ __ZN6CoreML13Specification16ArrayFeatureTypeD2Ev : 192 -> 176
~ -[MLTreeEnsembleRegressor .cxx_construct] : 48 -> 36
~ -[MLModelAssetDescription modelDescriptionsByFunctionName] : 28 -> 16
~ -[MLModel initWithDescription:configuration:] : 312 -> 328
~ ___MLLoggingGetInstrumentsActiveChannel_block_invoke : 168 -> 152
~ ___22+[MLReporter reporter]_block_invoke : 88 -> 84
~ -[MLModelAssetModelVendor cachedConfiguration] : 16 -> 8
~ -[MLModelConfiguration isEqualToModelConfiguration:] : 1736 -> 1748
~ __ZNSt3__120__shared_ptr_pointerIPN3MIL9IRProgramENS_14default_deleteIS2_EENS_9allocatorIS2_EEE16__on_zero_sharedEv : 60 -> 48
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_10shared_ptrIKN3MIL7IRValueEEES6_EENS_22__unordered_map_hasherIS6_NS_4pairIKS6_S6_EENS3_16IRValueMapHasherENS3_12IRValueMapEqEEENS_21__unordered_map_equalIS6_SB_SD_SC_EENS_9allocatorISB_EEED2Ev : 104 -> 116
~ -[MLE5ExecutionStreamOperation _inputPortNames] : 696 -> 700
~ -[MLE5InputPortBinder initWithPort:featureDescription:] : 152 -> 148
~ -[MLE5ExecutionStreamOperation pixelBufferPool] : 32 -> 36
~ -[MLE5InputPortBinder setPixelBufferPool:] : 16 -> 12
~ -[MLE5ExecutionStreamOperation _inoutPortNames] : 700 -> 672
~ -[MLE5ExecutionStreamOperation _newArrayOfInoutPorts:featureDescriptionsByName:error:] : 820 -> 816
~ -[MLE5ExecutionStreamOperation _outputPortNames] : 672 -> 676
~ -[MLE5ExecutionStreamOperation _newArrayOfOutputPorts:featureDescriptionsByName:error:] : 808 -> 800
~ -[MLE5OutputPort initWithPortHandle:name:featureDescription:] : 256 -> 244
~ -[MLE5OutputPortBinder initWithPort:featureDescription:] : 176 -> 188
~ -[MLE5OutputPort binder] : 12 -> 32
~ -[MLE5OutputPortBinder setPixelBufferPool:] : 36 -> 20
~ -[MLE5ProgramLibraryOnDeviceAOTCompilationImpl createProgramLibraryHandleWithRespecialization:error:] : 7840 -> 7844
~ __ZN6CoreML24addMemoryLayoutToProgramENSt3__110shared_ptrIKN3MIL9IRProgramEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP12NSDictionaryIP8NSStringP20MLFeatureDescriptionESK_ : 7376 -> 7372
~ -[MLE5StaticShapeExecutionStreamOperationPool _putBack:] : 164 -> 152
~ -[MLOutputBackingsVerifier initWithOutputDescriptions:] : 148 -> 160
~ __ZNSt3__120__shared_ptr_pointerIPN3MIL9IRProgramENS_14default_deleteIS2_EENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 4 -> 32
~ -[MLPipeline .cxx_destruct] : 84 -> 88
~ -[MLDelegateModel .cxx_destruct] : 172 -> 160
~ -[MLOutputBackingsVerifier .cxx_destruct] : 24 -> 36
~ -[MLModelEngine .cxx_destruct] : 88 -> 80
~ -[MLMultiArrayConstraint .cxx_destruct] : 108 -> 104
~ -[MLMultiArrayShapeConstraint .cxx_destruct] : 88 -> 80
~ __ZN6CoreML13Specification5ModelD2Ev : 192 -> 196
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification5ModelENS_9allocatorIS3_EEE16__on_zero_sharedEv : 28 -> 24
~ __ZN6CoreML13Specification5Model10clear_TypeEv : 2388 -> 2416
~ __ZN6CoreML13Specification24GLMRegressor_DoubleArrayD0Ev : 80 -> 76
~ __ZN6CoreML13Specification8Int64SetD2Ev : 148 -> 160
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification5ModelENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 8 -> 20
~ +[MLLoader loadModelFromAssetAtURL:configuration:error:] : 396 -> 400
~ +[MLModel modelWithContentsOfURL:configuration:error:] : 720 -> 728
~ +[MLNeuralNetworkV1Engine containerClass] : 36 -> 24
~ +[_OnDiskArchiveReader modelShapeFileName] : 100 -> 128
~ -[MLModelTypeRegistry loadNeuralNetworkClasses:trainWithMLCompute:] : 196 -> 204
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220106Em : 164 -> 156
~ -[MLModelAsset initWithResourceFactory:configuration:] : 388 -> 416
~ +[MLNeuralNetworkContainer containerFromCompiledArchiveCommon:filename:modelVersionInfo:compilerVersionInfo:configuration:error:] : 1180 -> 1156
~ -[_NNLayerInfo initWithType:concatenatedInputNames:bidirectional:] : 196 -> 188
~ +[MLNeuralNetworkEngine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 348 -> 356
~ +[_OnDiskArchiveReader modelNetFileName] : 100 -> 124
~ -[MLNeuralNetworkContainer modelDescription] : 16 -> 32
~ -[MLNeuralNetworkEngine initWithContainer:configuration:error:] : 1160 -> 1144
~ -[MLNeuralNetworkContainer inputLayerNames] : 20 -> 32
~ -[MLModelEngine initWithDescription:configuration:] : 248 -> 252
~ -[MLNeuralNetworkEngine collectParametersFromContainer:configuration:error:] : 5376 -> 5296
~ -[MLNeuralNetworkContainer compilerOutput] : 12 -> 28
~ -[MLNeuralNetworkEngine _espressoDeviceForConfiguration:error:] : 8 -> 24
~ -[MLNeuralNetworkEngine modelIsEncrypted] : 24 -> 40
~ -[MLNeuralNetworkEngine _addNetworkToPlan:error:] : 612 -> 596
~ -[MLModelConfiguration optimizationHints] : 12 -> 20
~ -[MLOptimizationHints specializationStrategy] : 12 -> 36
~ -[MLModelConfiguration setOptimizationHints:] : 28 -> 36
~ -[MLOptimizationHints setHotHandDuration:] : 20 -> 16
~ -[MLModelTypeRegistry classesForLoadingModelType:configuration:isUpdatable:isEncrypted:] : 1612 -> 1592
~ __ZNSt3__1plB9fqe220106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_ : 164 -> 180
~ -[MLModelConfiguration(E5RT) setExperimentalMLProgramEncryptedCacheUsage:] : 28 -> 36
~ -[MLOptimizationHints setSpecializationStrategy:] : 24 -> 16
~ -[MLModelConfiguration(E5RT) setSpecializationUsesMPSGraphExecutable:] : 24 -> 28
~ -[MLModelAsset modelVendor] : 32 -> 36
~ -[MLModelAssetModelVendor resourceFactory] : 20 -> 24
~ -[MLModelAssetResourceFactory impl] : 20 -> 24
~ -[MLModelAssetResourceFactoryOnDiskImpl modelURL] : 16 -> 36
~ -[MLModelAsset modelWithConfiguration:error:] : 536 -> 544
~ -[MLModelAssetResourceFactory modelWithConfiguration:error:] : 492 -> 496
~ -[MLModelAssetResourceFactoryOnDiskImpl compiledModelURL] : 32 -> 24
~ +[MLLoader _createDecryptSessionForModelAtURL:configuration:decryptSession:loaderEvent:error:] : 276 -> 280
~ -[MLLoaderEvent setModelIsEncrypted:] : 16 -> 8
~ -[MLModelTypeRegistry classesForLoadingModelType:] : 152 -> 148
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_19__map_value_compareIS7_NS_4pairIKS7_S7_EENS_4lessIS7_EEEENS5_ISC_EEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeIS8_PvEE : 104 -> 88
~ __ZNSt3__127__tree_balance_after_insertB9fqe220106IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 456 -> 484
~ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220106Ev : 104 -> 124
~ __ZNSt3__16__treeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS6_EENS4_IS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSF_SF_ : 112 -> 88
~ +[_OnDiskArchiveReader parseCompiledNetworkBlobWithName:archive:error:] : 664 -> 672
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE8IArchiveEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeIS9_PvEE : 120 -> 116
~ -[MLLoaderEvent setContainsCustomLayer:] : 28 -> 16
~ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES8_EEPvEENS_22__tree_node_destructorINS6_ISB_EEEEED1B9fqe220106Ev : 104 -> 84
~ -[MLLoaderEvent setModelHash:] : 8 -> 36
~ +[MLLoader _findCodedObjectURLInModelArchive:] : 208 -> 212
~ -[MLLoaderEvent numberFromCString:] : 416 -> 404
~ __ZNSt3__19allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS0_IcEEEES6_EEE7destroyB9fqe220106EPS7_ : 112 -> 92
~ -[MLLoaderEvent setModelType:] : 36 -> 32
~ -[MLVersionInfo versionNumberString] : 76 -> 80
~ -[MLLoaderEvent setModelVersion:] : 8 -> 36
~ -[MLVersionInfo initWithMajor:minor:patch:variant:] : 168 -> 172
~ -[MLModelEngine signpostID] : 20 -> 8
~ +[MLMultiArray(Attributes) cppStorageOrder:] : 28 -> 12
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9fqe220106Em : 92 -> 76
~ -[MLMultiArray initWithShape:dataType:error:] : 36 -> 20
~ __ZNSt3__16vectorImNS_9allocatorImEEEC2B9fqe220106EmRKm : 128 -> 144
~ __ZNSt3__110unique_ptrI14StorageManagerNS_14default_deleteIS1_EEE5resetB9fqe220106EPS1_ : 120 -> 136
~ __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPmS6_EEvT0_T1_l : 288 -> 284
~ -[MLModelEngine configuration] : 20 -> 8
~ -[MLNeuralNetworkEngine rebuildPlan:error:] : 2080 -> 2064
~ -[MLNeuralNetworkEngine _handleAddNetworkToPlanStatus:error:] : 936 -> 920
~ -[MLNeuralNetworkEngine network] : 20 -> 32
~ -[MLModelEngine supportsConcurrentSubmissions] : 20 -> 8
~ -[MLNeuralNetworkEngine isEspressoBiasPreprocessingShared] : 36 -> 44
~ +[MLLoader _loadModelWithClass:fromArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 1256 -> 1232
~ __ZN6google8protobuf8internal18TransparentSupportINSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEE6EqualsIS9_S9_EEbRKT_RKT0_ : 128 -> 144
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16allocator_traitsIS7_EEEENS_19__allocation_resultINT0_7pointerENSB_9size_typeEEERT_m : 116 -> 100
~ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiNS_4lessIS6_EENS4_INS_4pairIKS6_iEEEEEixERSA_ : 236 -> 228
~ -[_OnDiskArchiveReader transformParams] : 104 -> 128
~ -[MLNeuralNetworkContainer initWithFeatureDescriptions:modelDescription:outputLayerNames:classScoreVectorName:classLabels:isEncrypted:modelVersionInfo:compilerVersionInfo:] : 652 -> 636
~ __ZNSt3__116__pad_and_outputB9fqe220106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_ : 396 -> 388
~ -[MLVersionInfo majorVersion] : 20 -> 28
~ __ZNSt3__124__put_character_sequenceB9fqe220106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 432 -> 424
~ -[_OnDiskArchiveReader modelPath] : 32 -> 36
~ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqe220106Ev : 276 -> 272
~ -[_OnDiskArchiveReader initWithNetJson:shapeJson:modelPath:] : 804 -> 796
~ -[MLModelDescription(RawModelDescription) initFromRawModelDescriptionSpecification:] : 28 -> 8
~ +[MLModelIOUtils featureDescriptionsFromProto:] : 372 -> 376
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqe220106EPKvm : 1116 -> 1104
~ -[MLFeatureValue isUndefined] : 28 -> 32
~ -[MLPredictionEvent maybeLogPredictionEvent:] : 120 -> 124
~ -[MLDelegateModel predictionFromFeatures:options:error:] : 292 -> 288
~ -[MLDictionaryFeatureProvider featureNames] : 8 -> 4
~ -[MLFeatureValue multiArrayValue] : 108 -> 104
~ __ZNSt3__111atomic_loadB9fqe220106IhEENS_10shared_ptrIT_EEPKS3_ : 132 -> 112
~ -[MLReporter logMetric:] : 232 -> 228
~ -[MLPredictionEvent modelType] : 16 -> 8
~ -[MLMultiArray shape] : 20 -> 32
~ +[MLInternalSettings globalSettings] : 96 -> 84
~ -[MLMultiArrayShapeConstraint type] : 24 -> 8
~ __ZNSt3__16vectorImNS_9allocatorImEEE16__init_with_sizeB9fqe220106IPmS5_EEvT_T0_m : 124 -> 140
~ __ZNSt3__110unique_ptrINS_3mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE10_BlobShapeNS_4lessIS7_EENS5_INS_4pairIKS7_S8_EEEEEENS_14default_deleteISF_EEE5resetB9fqe220106EPSF_ : 120 -> 104
~ -[MLNeuralNetworkEngine inputBindStateForFeatureValue:error:] : 1460 -> 1476
~ -[MLNeuralNetworkEngine pixelBufferFromOutputBacking:forFeature:] : 504 -> 520
~ -[MLNeuralNetworkEngine releaseBuffer:] : 152 -> 168
~ -[MLNeuralNetworkEngine classLabels] : 44 -> 48
~ -[MLMultiArrayConstraint shapeConstraint] : 20 -> 28
~ -[MLInternalSettings restrictNeuralNetworksToUseCPUOnly] : 16 -> 36
~ -[MLNeuralNetworkEngine predictionFromFeatures:options:error:] : 448 -> 464
~ -[MLNeuralNetworkEngine evaluateInputs:options:error:] : 284 -> 268
~ -[MLNeuralNetworkEngine recordsPredictionEvent] : 152 -> 136
~ -[MLNeuralNetworkEngine resetSizes:error:] : 368 -> 352
~ -[MLNeuralNetworkEngine usingEspressoConfigurations] : 36 -> 52
~ -[MLNeuralNetworkEngine evaluateInputs:options:verifyInputs:error:] : 660 -> 676
~ __ZNSt3__128__exception_guard_exceptionsIZNS_10shared_ptrIhEC1B9fqe220106IhZ105-[MLMultiArray initWithBytesNoCopy:shape:dataType:strides:deallocator:mutableShapedBufferProvider:error:]E3$_0Li0EEEPT_T0_EUlvE_ED1B9fqe220106Ev : 80 -> 88
~ -[MLFeatureDescription imageConstraint] : 28 -> 24
~ +[MLFeatureValue featureValueWithMultiArray:] : 100 -> 104
~ -[MLPredictionOptions hasDirectBindingExpectations] : 124 -> 120
~ -[MLMultiArrayConstraint isAllowedShape:error:] : 116 -> 112
~ -[MLMultiArrayShapeConstraint isAllowedShape:error:] : 816 -> 832
~ -[MLNeuralNetworkEngine tryToSetOutputBacking:forFeatureName:toEbuf:reportPointerFlags:error:] : 988 -> 1004
~ -[MLNeuralNetworkEngine submitSemaphore] : 16 -> 32
~ -[MLNeuralNetworkEngine multiArrayFeatureValueFromEbuf:backingMultiArray:description:outputName:error:] : 1336 -> 1352
~ -[MLNeuralNetworkEngine modelVersionInfo] : 20 -> 40
~ +[MLDataConversionUtils stridesForShape:] : 312 -> 304
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIyEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m : 72 -> 76
~ -[MLNeuralNetworkEngine _deallocContextAndPlan] : 88 -> 104
~ -[MLNeuralNetworkEngine .cxx_destruct] : 704 -> 700
~ -[MLPixelBufferPool .cxx_destruct] : 32 -> 20
~ -[MLFeatureProviderConformer .cxx_destruct] : 80 -> 96
~ -[MLMultiArray objectForKeyedSubscript:] : 200 -> 220
~ -[MLPredictionEventMetric featuresPredictionCountSoFar] : 12 -> 28
~ -[MLState initWithBackings:] : 136 -> 144
~ -[MLInternalSettings init] : 72 -> 68
~ -[MLFeatureDescription multiArrayConstraint] : 32 -> 28
~ -[MLMultiArrayConstraint dataType] : 8 -> 36
~ -[MLModelDescription outputDescriptionsByName] : 8 -> 20
~ -[MLLoaderEvent setModelLoadError:] : 28 -> 20
~ -[MLMultiArrayConstraint shape] : 20 -> 28
~ -[MLLoaderEvent setModelOrigin:] : 32 -> 20
~ -[MLNeuralNetworkContainer .cxx_destruct] : 328 -> 308
~ -[MLLoaderEvent setProcessName:] : 32 -> 28
~ -[MLPredictionEvent setModelType:] : 28 -> 20
~ -[MLModelDescription setModelURL:] : 32 -> 40
~ +[MLLoader _populateLoaderAndPredictionEvent:model:configuration:loadTimeDuration:] : 1076 -> 1080
~ -[MLLoaderEvent setComputeUnits:] : 16 -> 12
~ -[MLPredictionEvent setModelName:] : 24 -> 28
~ -[MLLoaderEvent setBundleIdentifier:] : 12 -> 32
~ -[MLModelDescription setIsUpdatable:] : 28 -> 8
~ -[MLLoaderEvent bundleIdentifier] : 8 -> 36
~ -[MLPredictionEvent setBundleIdentifier:] : 8 -> 12
~ -[MLLoaderEvent modelHash] : 32 -> 24
~ -[MLModelAsset setLastConfiguration:] : 16 -> 24
~ -[MLLoaderEvent processName] : 16 -> 12
~ -[_OnDiskArchiveReader loadUpdatableParams:] : 364 -> 388
~ -[MLNeuralNetworkContainer setOptionalInputDefaultValues:] : 16 -> 24
~ -[_OnDiskArchiveReader copyLayerShapesToContainer:] : 880 -> 904
~ -[MLNeuralNetworkContainer setCompilerOutput:] : 20 -> 28
~ -[_NNLayerInfo .cxx_destruct] : 80 -> 72
~ -[MLNeuralNetworkContainer imagePreprocessingParams] : 24 -> 32
~ -[MLVersionInfo olderThan:] : 216 -> 192
~ +[MLModelIOUtils functionDescriptionsFromDescriptionSpecification:] : 600 -> 596
~ -[MLLayerPath copyWithZone:] : 172 -> 192
~ -[MLMultiArrayShapeConstraint initWithEnumeratedShapes:] : 1684 -> 1696
~ +[MLModelIOUtils orderedNamesFromProto:] : 216 -> 236
~ -[MLMultiArrayShapeConstraint initUnspecified] : 148 -> 128
~ +[MLModelIOUtils orderedOutputFeatureNamesFromInterface:] : 16 -> 40
~ -[MLMultiArrayConstraint initWithShape:dataType:shapeConstraint:defaultOptionalValue:] : 392 -> 368
~ -[MLLayerPath initWithScopedModelAndLayerName:layerName:] : 196 -> 184
~ -[MLModelDescription functionDescriptions] : 12 -> 36
~ -[MLModelAssetDescription usesMultiFunctionSyntax] : 100 -> 80
~ -[MLNeuralNetworkFunctionInfo initWithCompiledModelArchive:compilerVersionInfo:error:] : 956 -> 952
~ __ZN6CoreML17stringArrayToObjCERKNSt3__16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEE : 204 -> 196
~ -[MLModelAssetDescription functionNames] : 36 -> 16
~ -[MLNeuralNetworkFunctionInfo classLabels] : 8 -> 16
~ -[MLLayerPath layerName] : 12 -> 32
~ -[MLModelDescription copyWithZone:] : 892 -> 872
~ -[MLLayerPath setScopedModelNames:] : 28 -> 16
~ -[MLModelDescription setClassLabels:] : 28 -> 12
~ +[MLModelIOUtils defaultFunctionNameFromDescriptionSpecification:] : 148 -> 132
~ -[MLModelDescription defaultFunctionName] : 8 -> 20
~ -[MLLayerPath scopedModelNames] : 32 -> 24
~ -[MLNeuralNetworkFunctionInfo outputNames] : 36 -> 32
~ -[MLModelDescription stateDescriptionsByName] : 16 -> 32
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB9fqe220106Ev : 104 -> 88
~ -[MLNeuralNetworkContainer .cxx_construct] : 84 -> 88
~ -[MLNeuralNetworkFunctionInfo .cxx_destruct] : 80 -> 108
~ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB9fqe220106EPS6_ : 108 -> 100
~ -[MLModelAssetDescription assetDescriptionBySettingClassLabels:] : 160 -> 144
~ -[_OnDiskArchiveReader netJson] : 32 -> 24
~ __ZNSt3__16vectorINS_3mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEP17espresso_buffer_tNS_4lessIS7_EENS5_INS_4pairIKS7_S9_EEEEEENS5_ISG_EEE6resizeEm : 464 -> 460
~ -[MLPixelBufferPool init] : 132 -> 152
~ -[MLFeatureProviderConformer initWithFeatureDescriptions:defaultValues:usingRank5Mapping:optionalInputTypes:passthroughStateFeatures:] : 288 -> 284
~ -[MLE5ExecutionStream _reset] : 572 -> 576
~ -[MLE5ExecutionStreamOperation reset] : 1060 -> 1056
~ -[MLE5ExecutionStreamOperation operationHandle] : 36 -> 8
~ -[MLE5InputPortBinder setDirectlyBoundFeatureValue:] : 16 -> 12
~ -[MLModelEngine recordsPredictionEvent] : 28 -> 24
~ -[MLPredictionOptions inferenceFrameDataSerialization] : 32 -> 28
~ +[MLFeatureProviderUtils(MLNewProviderConstruction) providerWithSubsetOfFeaturesNamed:providedBy:] : 524 -> 496
~ -[MLPredictionOptions setInferenceFrameDataSerialization:] : 36 -> 28
~ -[MLCustomModelWrapper predictionFromFeatures:options:error:] : 316 -> 320
~ ___swift_closure_destructor.24 : 64 -> 76
~ -[MLE5InputPortBinder setBindingMode:] : 28 -> 20
~ -[MLE5OutputPort reset] : 308 -> 296
~ -[MLE5OutputPortBinder reset] : 112 -> 132
~ ___68+[MLMultiArray(MLE5Utils) multiArrayOwningBufferObjectOfPort:error:]_block_invoke : 88 -> 100
~ -[MLE5OutputPortBinder setOutputBackingWasDirectlyBound:] : 24 -> 8
~ -[MLE5ExecutionStream operations] : 20 -> 36
~ _MLE5PortTraitOf : 468 -> 484
~ +[MLE5Engine loadModelFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 960 -> 952
~ -[MLProgramE5Container initWithCompiledArchive:modelVersionInfo:compilerVersionInfo:error:] : 2072 -> 2096
~ __Z22MLE5TensorDescriptorOfP12e5rt_io_port : 280 -> 264
~ -[MLE5ExecutionStreamOperation state] : 32 -> 28
~ -[MLE5OutputPort featureValue] : 104 -> 92
~ -[MLE5OutputPortBinder _makeFeatureValueFromPort:featureDescription:error:] : 1888 -> 1892
~ __Z31MLE5MultiArrayDataTypeForTensorP16e5rt_tensor_desc : 864 -> 848
~ +[MLMultiArray(MLE5Utils) multiArrayOwningBufferObjectOfPort:error:] : 1156 -> 1136
~ _MLE5TypeOfBufferObject : 256 -> 264
~ sub_195a6a50c -> sub_195b60504 : 584 -> 592
~ -[MLModel newRequestWithInputFeatures:usingState:options:error:] : 412 -> 404
~ -[MLGenericPredictionRequest model] : 16 -> 24
~ -[MLModel submitPredictionRequest:completionHandler:] : 320 -> 312
~ -[MLGenericPredictionRequest predictionOptions] : 32 -> 8
~ ___65-[MLClassifier predictionFromFeatures:options:completionHandler:]_block_invoke : 176 -> 172
~ -[MLPredictionOptions classifyTopK] : 24 -> 20
~ _block_copy_helper : 16 -> 40
~ +[MLClassifier(Utilities) predictionFromFeatures:classifier:options:error:] : 244 -> 220
~ -[MLTreeEnsembleClassifier prepareInput:error:] : 556 -> 584
~ -[MLModelDescription inputFeatureNames] : 24 -> 12
~ -[MLClassifierResult initWithIntClassProbability:classFeatureType:additionalFeatures:] : 556 -> 540
~ +[MLFeatureValue featureValueWithInt64:] : 116 -> 112
~ -[MLModelDescription predictedProbabilitiesName] : 16 -> 12
~ -[MLClassifierResult(Utilities) asFeatureDictionaryWithPredictedClassDescription:classProbabilityDescription:] : 612 -> 604
~ -[MLClassifierResult predictedClass] : 12 -> 32
~ -[MLTreeEnsembleClassifier modelData] : 68 -> 52
~ __ZNSt3__16__treeIyNS_4lessIyEENS_9allocatorIyEEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeIyPvEE : 88 -> 68
~ -[MLTreeEnsembleClassifier _buildClassificationClasses:topk:error:] : 3492 -> 3488
~ -[MLModelDescription classProbabilityFeatureDescription] : 160 -> 180
~ -[MLClassifierResult predictedClassFeatureType] : 16 -> 32
~ _block_destroy_helper : 24 -> 20
~ -[MLModelDescription predictedClassFeatureDescription] : 176 -> 164
~ sub_195a6d3ec -> sub_195b633b4 : 172 -> 168
~ -[MLE5ExecutionStreamOperation outputFeatures] : 1100 -> 1112
~ -[MLE5OutputPortBinder featureDescription] : 28 -> 40
~ _MLE5DirectOutputModeTensorToMultiArray : 340 -> 332
~ __Z28MLE5MultiArrayShapeForTensorP16e5rt_tensor_desc : 412 -> 420
~ _MLE5OutputMultiArrayFeatureValueByRetainingTensor : 144 -> 148
~ -[MLE5ExecutionStreamOperation asyncSubmissionError] : 36 -> 20
~ _MLE5DataPointerOfBufferObject : 244 -> 256
~ -[MLE5OutputPort name] : 20 -> 28
~ ___46-[MLE5ExecutionStreamOperation outputFeatures]_block_invoke : 40 -> 36
~ -[MLE5Engine _predictionFromFeatures:usingState:options:error:] : 572 -> 568
~ -[MLPredictionOptions usesCPUOnly] : 8 -> 12
~ ___42-[MLE5Engine _conformInputFeatures:error:]_block_invoke : 44 -> 48
~ -[MLImageSize pixelsWide] : 12 -> 24
~ _MLE5BindEmptyMemoryObjectToPort : 2568 -> 2552
~ _MLE5BindInputBufferObjectByRetainingMultiArrayMemory : 892 -> 896
~ -[MLE5InputPortBinder bindMemoryObjectForFeatureValue:error:] : 500 -> 512
~ _MLE5FeatureTraitOf : 156 -> 172
~ _MLE5DirectModeFromMultiArrayMemoryToTensor : 216 -> 200
~ _MLE5CompareTensorAndMultiArrayMemoryLayout : 816 -> 820
~ -[MLMultiArray backingPixelBufferWasLocked] : 80 -> 92
~ _MLE5InputReusabilityTensorPortHasSameMultiArrayMemory : 140 -> 144
~ -[MLE5InputPortBinder copyFeatureValue:error:] : 364 -> 368
~ __ZN6CoreML13Specification16ImageFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 904 -> 900
~ __ZN6google8protobuf8internal16ReadSizeFallbackEPKcj : 144 -> 140
~ +[MLModelIOUtils populateConstraintsForImageFeatureDescription:] : 1624 -> 1628
~ -[MLImageSize initWithPixelsWide:pixelsHigh:] : 96 -> 84
~ -[MLImageSizeConstraint initWithEnumeratedImageSizes:] : 680 -> 660
~ -[MLImageSize pixelsHigh] : 16 -> 36
~ -[MLImageConstraint initWithPixelsWide:pixelsHigh:pixelType:sizeConstraint:] : 156 -> 168
~ __ZN6google8protobuf8internal14ArenaStringPtr3SetEPKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERSA_PNS0_5ArenaE : 312 -> 316
~ __ZN6CoreML13Specification16ImageFeatureTypeD2Ev : 144 -> 164
~ __ZrsR8IArchiveRf : 240 -> 232
~ +[MLNeuralNetworkEngine gpuEngine] : 8 -> 20
~ -[MLNeuralEngineComputeDeviceRegistry neuralEngineDevice] : 12 -> 32
~ -[MLModelConfiguration allowBackgroundGPUCompute] : 16 -> 28
~ -[MLInternalSettings restrictNeuralNetworksFromUsingANE] : 32 -> 24
~ -[MLImageConstraint pixelFormatType] : 72 -> 68
~ ___swift_memcpy16_8 : 28 -> 12
~ sub_195a73d38 -> sub_195b69d5c : 120 -> 136
~ sub_195a741ec -> sub_195b6a220 : 72 -> 84
~ __ZNSt3__110unique_ptrI18e5rt_buffer_object17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 64 -> 80
~ __Z24MLE5NewBufferObjectUsingP11__IOSurface : 248 -> 268
~ -[MLE5InputPortBinder featureDescription] : 12 -> 40
~ -[MLE5ExecutionStreamOperation _copyInputFeatures:error:] : 712 -> 684
~ -[MLE5InputPort boundFeatureDirectly] : 100 -> 96
~ _MLE5BindInputBufferObjectByCopyingMultiArray : 696 -> 692
~ _MLE5FeatureTraitOfBackingObject : 184 -> 172
~ __Z23MLE5BufferObjectBoundToP12e5rt_io_port : 284 -> 268
~ -[MLE5ExecutionStreamOperation _bindOutputPortsWithOptions:error:] : 556 -> 552
~ -[MLE5OutputPort prepareWithOptions:error:] : 268 -> 256
~ -[MLE5OutputPortBinder setOutputBacking:] : 28 -> 12
~ ___57-[MLE5ExecutionStreamOperation _copyInputFeatures:error:]_block_invoke : 32 -> 28
~ _MLE5DirectOutputBackingModeFromTensorToMultiArraySurface : 156 -> 176
~ -[MLE5OutputPortBinder _directlyBindOutputBacking:error:] : 876 -> 888
~ _MLE5BindMultiArrayOutputBackingToTensorPort : 344 -> 364
~ _MLE5GetShapeFromTensorDescriptor : 240 -> 248
~ __ZN35MLE5PixelBufferAndTensorStrategyKeyC1EjP16e5rt_tensor_desc : 144 -> 168
~ __ZN12_GLOBAL__N_143tensorUsesSameMemoryLayoutAsPixelFormatTypeEP16e5rt_tensor_descj : 368 -> 372
~ __ZNSt3__110unique_ptrI22e5rt_tensor_desc_dtype17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 64 -> 60
~ -[PixelBufferPoolKey copyWithZone:] : 8 -> 20
~ -[MLPredictionOptions completionSyncPoint] : 28 -> 32
~ -[MLE5Engine classLabels] : 108 -> 96
~ -[MLModelDescription classLabels] : 16 -> 28
~ -[MLE5Engine streamPool] : 36 -> 24
~ -[MLE5ExecutionStreamPool modelConfiguration] : 32 -> 12
~ -[MLE5ExecutionStream setResetTimer:] : 28 -> 16
~ ___35-[MLE5ExecutionStreamPool putBack:]_block_invoke : 124 -> 120
~ __ZN6CoreML16MultiArrayBufferC2EP10__CVBufferRKNSt3__16vectorImNS3_9allocatorImEEEES9_ : 380 -> 384
~ -[MLMultiArray initWithMultiArrayBuffer:] : 144 -> 128
~ -[MLE5InputPortBinder reusableForFeatureValue:willBindDirectly:] : 732 -> 744
~ _MLE5PortCompatibilityMultiArrayAndTensor : 236 -> 240
~ -[MLMultiArray initWithMultiArrayBuffer:mutableShapedBufferProvider:] : 348 -> 364
~ __ZNSt3__16vectorImNS_9allocatorImEEEC2B9fqe220106Em : 124 -> 108
~ ___42-[MLMultiArray initWithPixelBuffer:shape:]_block_invoke : 176 -> 172
~ __ZN6CoreML12scalarTypeOfEP10__CVBuffer : 180 -> 164
~ -[MLE5ExecutionStream _prepareForInputFeatures:options:error:] : 844 -> 848
~ -[MLE5ExecutionStreamOperation preloadAndReturnError:] : 580 -> 564
~ -[MLOutputBackingsVerifier _verifyMultiArrayOutputBacking:forFeature:error:] : 1100 -> 1080
~ -[MLE5ExecutionStream _reusableForInputFeatures:options:] : 500 -> 504
~ -[MLE5InputPortBinder pixelBufferPool] : 24 -> 20
~ __ZNSt3__110unique_ptrI42e5rt_precompiled_compute_op_create_options17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 76 -> 60
~ _MLE5FeatureTraitOfMultiArray : 92 -> 108
~ _MLE5FindInputBindFunction : 948 -> 952
~ -[MLE5InputPort copyFeatureValue:error:] : 136 -> 148
~ -[MLE5OutputPortBinder _reusableForDirectlyBoundOutputBacking:] : 1260 -> 1272
~ _MLE5OutputReusabilityTensorPortHasSameMultiArray : 316 -> 304
~ __Z20MLE5TensorDataTypeOfP16e5rt_tensor_desc : 260 -> 268
~ __ZN35MLE5PixelBufferAndTensorStrategyKey19componentDataTypeOfEP22e5rt_tensor_desc_dtype : 256 -> 248
~ -[MLPixelBufferPool createPixelBufferWithSize:pixelFormatType:error:] : 560 -> 564
~ -[MLOutputBackingsVerifier _verifyOutputBacking:forFeature:error:] : 672 -> 652
~ -[MLE5Engine _predictionFromFeatures:options:error:] : 560 -> 548
~ -[MLE5ExecutionStreamPool takeOut] : 336 -> 320
~ -[MLE5InputPort reusableForFeatureValue:willBindDirectly:] : 140 -> 152
~ -[PixelBufferPoolKey isEqual:] : 260 -> 248
~ -[MLE5ExecutionStreamOperation _prepareInputPortsForFeatures:error:] : 1632 -> 1636
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification9SizeRangeEJEEEPT_PS1_DpOT0_ : 136 -> 152
~ -[MLFeatureValue description] : 144 -> 160
~ __ZN6CoreML13Specification9SizeRange14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 596 -> 588
~ +[MLModelIOUtils rangeFromAllowedSizeRangeProtoMessage:] : 52 -> 40
~ -[MLMultiArrayShapeConstraint initWithSizeRangeForDimension:] : 168 -> 156
~ __ZN6CoreML13Specification9SizeRangeD0Ev : 76 -> 72
~ -[MLE5InputPort name] : 12 -> 24
~ _MLE5BindSurfaceBackedMultiArrayToTensorPort : 496 -> 512
~ -[MLE5ExecutionStreamOperation _bindCompletionSyncPointDirectlyIfPossible:] : 392 -> 376
~ -[MLE5OutputPortBinder _makeFeatureValueFromOutputBacking:error:] : 512 -> 528
~ __ZNSt3__110unique_ptrI21e5rt_program_function17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 68 -> 72
~ -[MLE5InputPortBinder bindingMode] : 16 -> 12
~ __ZN6CoreMLL19vectorizeMultiArrayIDF16_DF16_EEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 432 -> 448
~ -[PixelBufferPoolKey pixelFormatType] : 36 -> 24
~ -[MLE5InputPortBinder directlyBoundFeatureValue] : 36 -> 24
~ __ZN35MLE5PixelBufferAndTensorStrategyKey15componentPackOfEP22e5rt_tensor_desc_dtype : 248 -> 256
~ ___81-[MLE5StaticShapeExecutionStreamOperationPool takeOutOperationForFeatures:error:]_block_invoke : 84 -> 104
~ ___34-[MLE5ExecutionStreamPool takeOut]_block_invoke : 308 -> 324
~ -[MLE5InputPortBinder portHandle] : 24 -> 36
~ -[MLPixelBufferPool pixelBufferPoolCache] : 16 -> 20
~ -[MLMultiArray dataPointer] : 128 -> 120
~ __ZN6CoreML13Specification19FunctionDescriptionD0Ev : 64 -> 72
~ -[MLModelDescription parameterDescriptionsByKey] : 12 -> 36
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification19FunctionDescriptionEJEEEPT_PS1_DpOT0_ : 192 -> 200
~ -[MLModelDescription modelURL] : 32 -> 12
~ -[MLE5Engine initWithContainer:configuration:error:] : 684 -> 676
~ +[MLProgramE5Container deduceFunctionNameToCompute:modelDescription:fromConfiguration:modelAssetDescription:error:] : 1476 -> 1464
~ -[MLModelAssetDescription modelDescriptionOfFunctionNamed:] : 496 -> 484
~ -[MLE5ProgramLibrary initWithContainer:configuration:error:] : 1260 -> 1252
~ -[MLProgramE5Container URLOfMILText] : 12 -> 24
~ -[MLE5ProgramLibraryE5BundleImpl initWithE5BundleAtURL:configuration:] : 184 -> 180
~ ___44-[MLE5ProgramLibrary prepareAndReturnError:]_block_invoke : 116 -> 120
~ -[MLE5ProgramLibraryE5BundleImpl e5BundleURL] : 12 -> 32
~ -[MLProgramE5Container compilerVersionInfo] : 36 -> 24
~ __ZN6CoreML13Specification19FunctionDescriptionD2Ev : 208 -> 216
~ -[MLModelDescription modelPath] : 20 -> 32
~ -[MLE5ProgramLibrary prepareAndReturnError:] : 392 -> 384
~ -[MLProgramE5Container optionalInputDefaultValuesForFunctionNamed:] : 704 -> 680
~ ___64-[MLE5Engine _predictionFromFeatures:options:completionHandler:]_block_invoke : 580 -> 568
~ -[MLE5ExecutionStreamPool initWithModelConfiguration:modelSignpostId:] : 244 -> 252
~ +[MLE5ExecutionStreamOperationPoolFactory createPoolFromLibrary:functionName:modelDescription:modelConfiguration:modelSignpostId:compilerVersionInfo:] : 288 -> 284
~ -[MLModelDescription(Utilities) hasEnumeratedShapeInputs] : 428 -> 424
~ -[MLMultiArrayShapeConstraint enumeratedShapes] : 8 -> 20
~ ___Block_byref_object_dispose_.22410 : 60 -> 48
~ -[MLArrayBatchProvider initWithFeatureProviderArray:] : 120 -> 132
~ ___55-[MLDelegateModel _predictionsFromBatch:options:error:]_block_invoke : 24 -> 44
~ sub_195a81e10 -> sub_195b77e64 : 432 -> 412
~ sub_195a82c1c -> sub_195b78c5c : 20 -> 16
~ sub_195a82ec4 -> sub_195b78f00 : 376 -> 356
~ sub_195a83558 -> sub_195b79580 : 104 -> 84
~ sub_195a83678 -> sub_195b7968c : 84 -> 96
~ -[MLE5Engine initWithProgramLibrary:modelDescription:configuration:functionName:classProbabilitiesFeatureName:optionalInputDefaultValues:compilerVersionInfo:] : 996 -> 1016
~ ___swift_memcpy48_8 : 32 -> 20
~ __ZN6CoreML13Specification22ArrayFeatureType_ShapeD0Ev : 72 -> 84
~ __ZN6CoreML21numericVectorFromObjCImEENSt3__16vectorIT_NS1_9allocatorIS3_EEEEP7NSArrayIP8NSNumberE : 428 -> 420
~ __ZN6CoreML22MultiArrayBufferLayoutC2ENSt3__16vectorImNS1_9allocatorImEEEES5_NS_12StorageOrderE : 548 -> 544
~ -[MLMultiArrayBufferLayout offsetOfScalarAtIndex:contiguousScalars:] : 152 -> 156
~ __ZNK6CoreML22MultiArrayBufferLayout9getOffsetEmPm : 284 -> 280
~ -[MLMultiArrayBufferLayout .cxx_destruct] : 20 -> 12
~ -[MLE5ExecutionStream init] : 412 -> 400
~ -[MLE5ExecutionStreamPool modelSignpostId] : 24 -> 36
~ ___35-[MLE5ProgramLibrary functionNames]_block_invoke : 1192 -> 1180
~ __ZN12_GLOBAL__N_18ToVectorIiiEENSt3__16vectorIT_NS1_9allocatorIS3_EEEERKN8Espresso11layer_shapeE : 304 -> 280
~ -[MLFeatureDescription valueConstraints] : 20 -> 12
~ __ZN6CoreML24MLNeuralNetworkUtilities35hashVectorShapesToConfigurationNameERKNSt3__13mapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_6vectorIiNS6_IiEEEENS1_4lessIS8_EENS6_INS1_4pairIKS8_SB_EEEEEE : 476 -> 452
~ -[MLFeatureDescription encodeWithCoder:] : 228 -> 220
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIiNS5_IiEEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SA_EENS_4lessIS7_EEEENS5_ISF_EEE14__tree_deleterclB9fqe220106EPNS_11__tree_nodeISB_PvEE : 80 -> 88
~ +[MLFeatureDescription supportsSecureCoding] : 20 -> 12
~ __ZN12_GLOBAL__N_128computeE5ProgramFunctionNameEP8NSStringP5NSSetIS1_ERKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEEP13MLVersionInfo : 456 -> 460
~ +[MLNeuralNetworkCompiler iOS18CompilerVersionInfo] : 100 -> 96
~ __ZN6CoreML24MLNeuralNetworkUtilities38hashFeatureProviderToConfigurationNameEPU28objcproto17MLFeatureProvider11objc_objectbP13MLVersionInfo : 1724 -> 1708
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIjEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m : 92 -> 76
~ ___85-[MLE5EnumeratedShapeExecutionStreamOperationPool takeOutOperationForFeatures:error:]_block_invoke : 136 -> 120
~ -[MLE5ProgramLibraryE5BundleImpl configuration] : 8 -> 24
~ -[MLE5EnumeratedShapeExecutionStreamOperationPool functionNameToPoolMap] : 16 -> 28
~ -[MLE5ExecutionStreamOperation .cxx_construct] : 24 -> 12
~ -[MLE5EnumeratedShapeExecutionStreamOperationPool modelSignpostId] : 36 -> 20
~ -[MLE5ExecutionStreamOperation initWithProgramLibrary:functionName:modelDescription:configuration:debugLabel:modelSignpostId:] : 604 -> 600
~ sub_195a883b8 -> sub_195b7e358 : 216 -> 220
~ -[MLE5ExecutionStreamOperation _createOperationAndReturnError:] : 20 -> 16
~ __ZNSt3__110unique_ptrI16e5rt_e5_compiler17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 64 -> 68
~ -[MLE5ExecutionStreamOperation _createOperationWithRetryCount:error:] : 456 -> 476
~ sub_195a88864 -> sub_195b7e81c : 100 -> 76
~ -[MLE5ProgramLibrary container] : 28 -> 20
~ sub_195a8960c -> sub_195b7f5a4 : 112 -> 84
~ -[MLDictionaryFeatureProvider objectForKeyedSubscript:] : 24 -> 16
~ -[MLE5EnumeratedShapeExecutionStreamOperationPool _putBack:] : 436 -> 448
~ -[MLE5ProgramLibraryOnDeviceAOTCompilationImpl configuration] : 8 -> 36
~ -[MLE5OutputPort .cxx_destruct] : 104 -> 92
~ -[MLE5OutputPortBinder .cxx_destruct] : 132 -> 120
~ -[MLE5InputPortBinder .cxx_destruct] : 92 -> 88
~ __ZNSt3__110unique_ptrI16e5rt_async_event17MLE5ObjectDeleterIS1_EE5resetB9fqe220106EPS1_ : 68 -> 64
~ -[MLE5OutputPort dealloc] : 140 -> 160
~ -[MLE5OutputPortBinder dealloc] : 140 -> 128
~ -[MLE5InputPortBinder dealloc] : 128 -> 144
~ ___59-[MLE5EnumeratedShapeExecutionStreamOperationPool putBack:]_block_invoke : 12 -> 16
~ ___51+[MLNeuralNetworkCompiler iOS18CompilerVersionInfo]_block_invoke : 108 -> 88
~ -[MLE5ExecutionStreamOperation dealloc] : 144 -> 140
~ ___Block_byref_object_copy_.17087 : 24 -> 44
~ -[MLMultiArray(PrivateConstruction) initWithBytesNoCopy:shape:dataType:strides:mutableShapedBufferProvider:] : 68 -> 48
~ -[MLE5ExecutionStream prepareAsyncSubmissionForInputFeatures:options:error:] : 828 -> 832
~ sub_195a8da54 -> sub_195b839d8 : 32 -> 24
~ __ZN6CoreMLL19vectorizeMultiArrayIdfEEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 452 -> 456
~ __ZN6CoreMLL19vectorizeMultiArrayIfdEEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 444 -> 460
~ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI23MLE5PortBindStrategyKeyPFbP14MLFeatureValueP12e5rt_io_portEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S8_EENS2_4hashENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SD_SG_SE_EENS_9allocatorISD_EEE16__emplace_uniqueB9fqe220106IJRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSR_IJEEEEEENSB_INS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEEDpOT_ENKUlRSC_SQ_OST_OSU_E_clES15_SQ_S16_S17_ : 1068 -> 1052
~ -[MLE5ProgramLibrary .cxx_destruct] : 92 -> 116
~ -[MLProgramE5Container .cxx_destruct] : 140 -> 120
~ -[MLE5ProgramLibraryE5BundleImpl .cxx_destruct] : 92 -> 76
~ -[MLE5ExecutionStreamPool .cxx_destruct] : 100 -> 112
~ -[MLE5ExecutionStream .cxx_destruct] : 104 -> 92
~ -[MLE5EnumeratedShapeExecutionStreamOperationPool .cxx_destruct] : 140 -> 144
~ -[MLTreeEnsembleClassifier .cxx_construct] : 80 -> 64
~ __ZN6CoreML13Specification21DictionaryFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 492 -> 496
~ -[MLModelAssetDescription initFromModelDescriptionSpecification:] : 156 -> 148
~ -[MLDictionaryConstraint initWithKeyType:] : 84 -> 80
~ +[MLAllComputeDeviceRegistry sharedRegistry] : 188 -> 160
~ __ZN12_GLOBAL__N_140overheadBytesFromRowAlignmentIsTolerableEmN3MIL10IRDataTypeE : 184 -> 208
~ __ZN12_GLOBAL__N_126makeTensorBufferFromTensorEPKN3MIL17IRTensorValueTypeERNS0_10MILContextE : 260 -> 268
~ __ZN12_GLOBAL__N_123tensorInputOutputRenameERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 136 -> 132
~ sub_195a90cb4 -> sub_195b86c14 : 84 -> 72
~ __ZL22get_ANEDeviceInfoClassv : 224 -> 236
~ -[MLCPUComputeDeviceRegistry cpuDevice] : 8 -> 12
~ -[MLE5ExecutionStreamOperation _reusableForWaitSyncPoints:allInputsUseDirectBinding:] : 696 -> 692
~ __ZN12_GLOBAL__N_122dependentEventsBoundToEP31e5rt_execution_stream_operation : 696 -> 680
~ -[MLE5OutputPortBinder reusableForOutputBacking:willBindDirectly:] : 184 -> 200
~ __ZN6CoreMLL19vectorizeMultiArrayIfDF16_EEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 456 -> 444
~ -[MLNeuralEngineComputeDevice initWithTotalCoreCount:] : 84 -> 96
~ -[MLGPUComputeDeviceRegistry registerGPUDevices] : 728 -> 732
~ +[MLGPUComputeDevice deviceWithMetalDevice:] : 112 -> 108
~ -[MLGPUComputeDeviceRegistry setObservationToken:] : 36 -> 40
~ -[MLGPUComputeDevice initWithMetalDevice:] : 160 -> 148
~ ___36+[MLCPUComputeDevice physicalDevice]_block_invoke : 60 -> 68
~ -[MLAllComputeDeviceRegistry initWithDeviceRegistries:] : 132 -> 116
~ __ZNK6CoreML16MultiArrayBuffer7squeezeEv : 760 -> 776
~ __ZN6CoreMLL18copyMultiArrayBNNSIDF16_DF16_EEbRKNS_16MultiArrayBufferERS1_ : 596 -> 612
~ __ZN6CoreMLL12initVIBufferERKNS_16MultiArrayBufferEP13vImage_Buffer : 364 -> 348
~ sub_195cf957c -> sub_195def4dc : 64 -> 52
~ sub_195cf95bc -> sub_195def510 : 116 -> 108
~ sub_195cf9630 -> sub_195def57c : 92 -> 84
~ sub_195cf973c -> sub_195def680 : 56 -> 80
~ sub_195cf9774 -> sub_195def6d0 : 104 -> 116
~ sub_195cf98f4 -> sub_195def85c : 28 -> 20
~ __ZN5Cache10swap_indexEii : 348 -> 356
~ __ZN6Kernel10k_functionEPK8svm_nodeS2_RK13svm_parameter : 572 -> 564
~ __ZL4infoPKcz : 132 -> 140
~ __ZN6Solver5SolveEiRK7QMatrixPKdPKaPddddPNS_12SolutionInfoEi : 2684 -> 2676
~ __ZN9Solver_NU13calculate_rhoEv : 388 -> 396
~ _svm_train : 5248 -> 5252
~ __ZL13svm_train_onePK11svm_problemPK13svm_parameterdd : 2760 -> 2764
~ __ZL17svm_group_classesPK11svm_problemPiPS2_S3_S3_S2_ : 784 -> 780
~ _svm_cross_validation : 1568 -> 1560
~ _svm_get_svr_probability : 104 -> 116
~ _svm_predict_values : 788 -> 776
~ __ZL8readlineP7__sFILE : 192 -> 204
~ _svm_free_model_content : 224 -> 244
~ _svm_set_print_string_function : 60 -> 56
~ __ZN5SVC_QD1Ev : 12 -> 28
~ __ZN5SVC_QC2ERK11svm_problemRK13svm_parameterPKa : 424 -> 440
~ __ZN5SVC_QD0Ev : 64 -> 84
~ __ZN5SVC_QD2Ev : 184 -> 192
~ __ZN11ONE_CLASS_QD0Ev : 72 -> 64
~ __ZN11ONE_CLASS_QD2Ev : 144 -> 148
~ __ZN5SVR_QD1Ev : 28 -> 24
~ __ZN5SVR_QC2ERK11svm_problemRK13svm_parameter : 592 -> 596
~ __ZN5SVR_QD2Ev : 232 -> 244
~ __ZNSt3__110unique_ptrIN3MIL10Attributes17FlexibleShapeInfoENS_14default_deleteIS3_EEED1B9fqe220106Ev : 72 -> 88
~ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIPKN3MIL11IRDimensionENS6_ISD_EEEEEEPvEENS_22__hash_node_destructorINS6_ISI_EEEEED1B9fqe220106Ev : 92 -> 76
~ __ZNSt3__16vectorIPKN3MIL11IRDimensionENS_9allocatorIS4_EEE16__init_with_sizeB9fqe220106IPS4_S9_EEvT_T0_m : 156 -> 172
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIPKN3MIL11IRDimensionENS5_ISC_EEEEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SE_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SJ_SN_SL_EENS5_ISJ_EEED2Ev : 124 -> 100
~ __ZNSt3__16vectorIPKN3MIL11IRDimensionENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_ : 188 -> 196
~ __ZN12_GLOBAL__N_115getOperatorTypeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKN3MIL7IROpsetE : 380 -> 364
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS_22__unordered_map_hasherIS7_NS_4pairIKS7_S7_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SC_SG_SE_EENS5_ISC_EEED2Ev : 124 -> 108
~ __ZNSt3__112__hash_tableINS_10shared_ptrIN3MIL7Builder16OperationBuilderEEENS_4hashIS5_EENS_8equal_toIS5_EENS_9allocatorIS5_EEED2Ev : 116 -> 100
~ __ZNSt3__15dequeINS_4pairIU8__strongP7NSArraymEENS_9allocatorIS5_EEE9push_backEOS5_ : 1240 -> 1268
~ __ZNSt3__114__split_bufferIPNS_4pairIU8__strongP7NSArraymEENS_9allocatorIS6_EEE12emplace_backIJRS6_EEEvDpOT_ : 248 -> 252
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIPNS_4pairIU8__strongP7NSArraymEEEENS_16allocator_traitsIS8_EEEENS_19__allocation_resultINT0_7pointerENSC_9size_typeEEERT_m : 92 -> 76
~ __ZNSt3__15dequeINS_4pairIU8__strongP7NSArraymEENS_9allocatorIS5_EEED2B9fqe220106Ev : 360 -> 344
~ -[MLRegressor(Utilities) regressorResultFromOutputFeatures:error:] : 816 -> 820
~ -[MLSVREngine deallocSVMNodeVector:] : 36 -> 32
~ -[MLSVREngine setFreeModelOnDealloc:] : 20 -> 24
~ +[MLModelErrorUtils programEvaluationErrorWithUnderlyingError:format:] : 84 -> 80
~ +[MLNeuralNetworkCompiler collectNNModelDetailsFromArchive:spec:error:] : 848 -> 852
~ ___51+[MLNeuralNetworkCompiler iOS17CompilerVersionInfo]_block_invoke : 100 -> 96
~ +[MLNeuralNetworkEngine loadModelAssetDescriptionFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 284 -> 300
~ -[MLNeuralNetworkEngine setEspressoBlobShapes:widths:heights:ks:batches:sequences:ranks:error:] : 1180 -> 1164
~ -[MLNeuralNetworkEngine setActiveFunction:] : 40 -> 24
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE10_BlobShapeEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEE21__construct_from_treeB9fqe220106IZNSI_21__copy_construct_treeB9fqe220106EPNS_11__tree_nodeIS9_PvEEEUlRKSD_E_EESN_SN_T_ : 292 -> 276
~ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 196 -> 180
~ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIPKcEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m : 84 -> 92
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE24__emplace_back_slow_pathIJRKiEEEPiDpOT_ : 180 -> 204
~ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJRKmEEEPmDpOT_ : 224 -> 208
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE10_BlobShapeEENS_19__map_value_compareIS7_NS_4pairIKS7_S8_EENS_4lessIS7_EEEENS5_ISD_EEEC2ERKSI_ : 132 -> 124
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJjEEEPjDpOT_ : 192 -> 200
~ -[MLErfActivationBrick size] : 20 -> 36
~ -[MLItemSimilarityRecommender _itemForIndex:error:] : 212 -> 220
~ -[MLItemSimilarityRecommender _mapItemSequence:dest:error:] : 1092 -> 1100
~ -[MLItemSimilarityRecommender predictionFromFeatures:options:error:] : 6384 -> 6376
~ ___68-[MLItemSimilarityRecommender predictionFromFeatures:options:error:]_block_invoke : 44 -> 52
~ -[MLItemSimilarityRecommender .cxx_construct] : 156 -> 172
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_ : 280 -> 288
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERZ68-[MLItemSimilarityRecommender predictionFromFeatures:options:error:]E3$_0PNS_4pairIydEEEEbT1_S7_T0_ : 944 -> 928
~ __ZN6CoreML13TreeEnsembles8Internal30buildTreeEnsembleModelFromSpecENSt3__110shared_ptrINS0_13_TreeEnsembleEEERKNS2_3mapINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEESC_NS2_4lessISC_EENSA_INS2_4pairIKSC_SC_EEEEEE : 32000 -> 31984
~ -[MLModelAssetDescription description] : 716 -> 696
~ -[MLSVMEngine deallocSVMNodeVector:] : 36 -> 32
~ -[MLSVMEngine predict:] : 668 -> 700
~ -[MLSVMEngine predictProbabilities:probabilities:] : 284 -> 276
~ -[MLSVMEngine .cxx_destruct] : 32 -> 12
~ -[MLArrayDictionaryFeatureProvider .cxx_destruct] : 36 -> 40
~ -[MLTreeEnsembleClassifier _setSingleArrayLookupField] : 324 -> 320
~ __ZNSt3__16vectorImNS_9allocatorImEEE6resizeEm : 304 -> 308
~ __ZNSt3__16vectorIxNS_9allocatorIxEEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPxS6_EEvT0_T1_l : 288 -> 284
~ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B9fqe220106Em : 132 -> 136
~ -[MLFeatureDescription sequenceConstraintCached] : 24 -> 20
~ -[MLNearestNeighborsLinearIndex initWithDataset:numberOfDimensions:] : 272 -> 296
~ -[MLNearestNeighborsLinearIndex findNearestNeighbors:toIndex:] : 732 -> 744
~ -[MLNearestNeighborsLinearIndex .cxx_construct] : 40 -> 28
~ __ZNSt3__111__sift_downB9fqe220106INS_17_ClassicAlgPolicyELb0ERN6CoreML25CompareIndexDistancePairsENS_11__wrap_iterIPNS_4pairImfEEEEEEvT2_OT1_NS_15iterator_traitsISA_E15difference_typeESF_ : 220 -> 252
~ __ZNSt3__16vectorINS_4pairImfEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 200 -> 184
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKfEES9_EENS6_IPfEES9_T0_T1_l : 588 -> 584
~ __ZN6CoreML10NNCompiler8Frontend3MIL5ParseENSt3__110shared_ptrIN3MIL10MILContextEEERKNS_13Specification5ModelERKNS3_13unordered_mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS4_IKNS5_4Blob11StorageDataEEENS3_4hashISI_EENS3_8equal_toISI_EENSG_INS3_4pairIKSI_SM_EEEEEESI_ : 10172 -> 10176
~ __ZNSt3__16vectorImNS_9allocatorImEEE6insertENS_11__wrap_iterIPKmEEOm : 560 -> 564
~ __ZN11BrickLayers4TileERKNSt3__16vectorImNS0_9allocatorImEEEEPKfS6_PfRS4_ : 720 -> 728
~ __ZN11BrickLayers30SlidingWindowsShapeComputationExxxRKNSt3__16vectorImNS0_9allocatorImEEEERS4_ : 424 -> 416
~ __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B9fqe220106Em : 108 -> 116
~ -[MLSupportVectorRegressor .cxx_destruct] : 24 -> 28
~ +[MLGLMRegression loadModelFromSpecification:configuration:error:] : 132 -> 128
~ -[MLGLMRegression .cxx_construct] : 72 -> 76
~ __ZN6CoreMLL18copyMultiArrayBNNSIddEEbRKNS_16MultiArrayBufferERS1_ : 288 -> 292
~ __ZN6CoreML18MultiArrayIteratorIdEppEv : 208 -> 216
~ __ZN6CoreML18MultiArrayIteratorIiED1Ev : 68 -> 88
~ ____ZN6CoreMLL16copyMultiArrayVIIddEEbRKNS_16MultiArrayBufferERS1__block_invoke : 236 -> 252
~ ___Block_byref_object_dispose_.39 : 20 -> 4
~ __ZN6CoreML18MultiArrayIteratorIdEC2ERKNS_16MultiArrayBufferENS_12StorageOrderEb : 388 -> 404
~ __ZNSt3__16vectorImNS_9allocatorImEEE6resizeEmRKm : 284 -> 280
~ __ZN6CoreMLL18copyMultiArrayBNNSIdfEEbRKNS_16MultiArrayBufferERS1_ : 368 -> 372
~ __ZN6CoreML18MultiArrayIteratorIiEppEv : 232 -> 228
~ __ZN6CoreML18MultiArrayIteratorIfEC2ERKNS_16MultiArrayBufferENS_12StorageOrderEb : 396 -> 408
~ __ZN6CoreML18MultiArrayIteratorIiEC2ERKNS_16MultiArrayBufferENS_12StorageOrderEb : 396 -> 408
~ __ZN6CoreMLL18copyMultiArrayBNNSIdDF16_EEbRKNS_16MultiArrayBufferERS1_ : 368 -> 372
~ __ZN6CoreML18MultiArrayIteratorIDF16_EppEv : 232 -> 228
~ __ZN6CoreML18MultiArrayIteratorIDF16_EC2ERKNS_16MultiArrayBufferENS_12StorageOrderEb : 396 -> 408
~ +[MLReporterUtils archiveModelDetails:withName:toArchive:error:] : 520 -> 532
~ -[MLSliceNDBrick hasGPUSupport] : 24 -> 12
~ -[MLSliceNDBrick computeOnCPUWithInputTensors:outputTensors:] : 3128 -> 3160
~ -[MLSliceNDBrick .cxx_destruct] : 160 -> 172
~ __ZN6CoreML22MultiArrayBufferLayoutC2ERKS0_ : 260 -> 264
~ __ZNKSt3__112__hash_tableINS_17__hash_value_typeIyN6CoreML24BayesianProbitRegression8GaussianEEENS_22__unordered_map_hasherIyNS_4pairIKyS4_EENS3_11SuperHasherESA_EENS_21__unordered_map_equalIyS9_SA_SA_EENS_9allocatorIS9_EEE4findIyEENS_21__hash_const_iteratorIPNS_11__hash_nodeIS5_PvEEEERKT_ : 172 -> 188
~ ___79-[MLE5RangeShapeExecutionStreamOperationPool prepareWithInitialPoolSize:error:]_block_invoke : 732 -> 716
~ __ZN12_GLOBAL__N_123computeDefaultShapeHashEP18MLModelDescriptionP13MLVersionInfo : 184 -> 168
~ -[MLE5RangeShapeExecutionStreamOperationPool _makeAndPreloadOperationForFunction:error:] : 424 -> 408
~ __ZN12_GLOBAL__N_129InputNameAndOperandDescVectorD1Ev : 152 -> 144
~ __ZNSt3__16vectorIP17e5rt_operand_descNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_ : 208 -> 200
~ __ZNK6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEN6CoreML13Specification7MILSpec8FunctionEE8InnerMap10FindHelperIS8_EENS2_4pairINSE_13iterator_baseIKNS0_7MapPairIS8_SC_EEEEmEERKT_PNS2_14__map_iteratorINS2_15__tree_iteratorINS2_12__value_typeINS2_17reference_wrapperIKS8_EEPvEEPNS2_11__tree_nodeISX_SW_EElEEEE : 292 -> 296
~ __ZNSt3__110__function6__funcIZN12_GLOBAL__N_169ModelSpecificationDataByResolvingBlobFileReferencesIntoInMemoryValuesERN6CoreML13Specification5ModelEP5NSURLPU15__autoreleasingP7NSErrorE3$_0FvRNS4_7MILSpec5ValueEEE18destroy_deallocateEv : 60 -> 56
~ __ZNSt3__110unique_ptrIN3MIL4Blob13StorageReaderENS_14default_deleteIS3_EEED1B9fqe220106Ev : 96 -> 100
~ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IN3MIL4Blob13StorageReaderENS_14default_deleteISB_EEEEEEPvEENS_22__hash_node_destructorINS6_ISH_EEEEED1B9fqe220106Ev : 92 -> 88
~ __ZNSt3__112__destroy_atB9fqe220106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN3MIL4Blob13StorageReaderENS_14default_deleteISC_EEEEEEEEvPT_ : 108 -> 80
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB9fqe220106IPKdS6_EEvT_T0_m : 148 -> 144
~ __ZNKSt3__110__function6__funcIZN12_GLOBAL__N_132LoadBlobFileReferencesIntoMemoryERN6CoreML13Specification5ModelEP5NSURLPU15__autoreleasingP7NSErrorE3$_0FvRNS4_7MILSpec5ValueEEE11target_typeEv : 36 -> 12
~ -[MLTreeEnsembleXGBoostClassifier featureProviderFromXGboostResults:length:error:] : 224 -> 252
~ -[MLTreeEnsembleXGBoostClassifier .cxx_destruct] : 116 -> 120
~ ____ZL28getXGBoosterPredictSymbolLocv_block_invoke : 80 -> 108
~ ____ZL25getXGBoosterFreeSymbolLocv_block_invoke : 84 -> 88
~ +[MLNNLayerComputeUnitSelectionUtils undoLastHintUpdate:error:] : 296 -> 292
~ __ZN6CoreML10NNCompiler8Frontend3MIL4Util24ValidateSpecIsConsistentERKN3MIL9IRProgramERKNS0_11MLModelInfoERKNS_13Specification16ModelDescriptionE : 10216 -> 10276
~ -[InternalCustomTileLike .cxx_construct] : 24 -> 20
~ +[MLProgramContainer populateInputNameToShapeMap:fromContainer:forFunction:program:withValidation:error:] : 5600 -> 5568
~ +[MLProgramContainer containerFromCompiledArchive:modelVersionInfo:compilerVersionInfo:configuration:error:] : 1652 -> 1664
~ __ZN6CoreML10NNCompiler7Backend3MIL10Ios16Train17Ios16TrainBackend7CompileER8OArchive : 2004 -> 2000
~ -[_KDNode partitionDataPoints:indices:numDimensions:] : 604 -> 608
~ -[MLNearestNeighborsSingleKdTreeIndex calculateDistancesForNodesBetweenLeft:andRight:toQueryPoint:] : 1028 -> 1024
~ -[MLNearestNeighborsSingleKdTreeIndex findK:nearestNeighbors:toQueryPoint:inTree:] : 1096 -> 1100
~ +[MLNearestNeighborsSingleKdTreeIndex supportsSecureCoding] : 32 -> 28
~ __ZNSt3__111__sift_downB9fqe220106INS_17_ClassicAlgPolicyELb0ERN6CoreML25CompareIndexDistancePairsEPNS_4pairImfEEEEvT2_OT1_NS_15iterator_traitsIS8_E15difference_typeESD_ : 228 -> 232
~ __ZNSt3__125__independent_bits_engineINS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEmE6__evalENS_17integral_constantIbLb1EEE : 296 -> 312
~ -[MLNonMaximumSuppressionParameters .cxx_destruct] : 132 -> 140
~ -[MLNonMaximumSuppression initWithParameters:modelDescription:configuration:error:] : 168 -> 192
~ -[MLNonMaximumSuppression .cxx_destruct] : 24 -> 32
~ __ZN6CoreML10NNCompiler7Backend3MIL5Ios1520Ios15LayerTranslatorD0Ev : 56 -> 84
~ -[MLNeuralNetworkMLComputeGraph lossInputsFromUpdateParams:] : 332 -> 336
~ -[MLNeuralNetworkMLComputeGraph .cxx_destruct] : 188 -> 184
~ +[MLBatchProviderUtils(MLBatchCopyToMultiArray) vectorizeFeaturesNamed:fromBatch:intoRowsOfDoubleMatrix:error:] : 836 -> 840
~ __ZN6CoreML13TreeEnsembles30buildTreeEnsembleModelFromSpecENSt3__110shared_ptrINS0_13_TreeEnsembleEEERKNS1_3mapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEESB_NS1_4lessISB_EENS9_INS1_4pairIKSB_SB_EEEEEE : 168 -> 140
~ -[MLE5ExecutionStreamOperation _bindNewWaitEventsDirectlyWithWaitSyncPoints:] : 1496 -> 1492
~ -[MLE5ExecutionStreamOperation completionSharedEventBoundToESOP] : 8 -> 12
~ __ZNSt3__114__split_bufferINS_10unique_ptrI16e5rt_async_event17MLE5ObjectDeleterIS2_EEERNS_9allocatorIS5_EEED2Ev : 108 -> 104
~ __ZNSt3__16vectorINS_10unique_ptrI16e5rt_async_event17MLE5ObjectDeleterIS2_EEENS_9allocatorIS5_EEE16__destroy_vectorclB9fqe220106Ev : 132 -> 136
~ __ZNSt3__15dequeINS_4pairINS_10shared_ptrIN8Espresso16abstract_contextEEENS3_12compute_pathEEENS_9allocatorIS7_EEED2B9fqe220106Ev : 388 -> 384
~ +[MLModelIOUtils specificationURLFromModelAtURL:error:] : 992 -> 964
~ +[MLModelIOUtils orderedFeatureNamesFromInterface:forInput:] : 84 -> 80
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification16ModelDescriptionENS_9allocatorIS3_EEED0Ev : 112 -> 84
~ +[MLGLMClassification loadModelFromSpecification:configuration:error:] : 132 -> 128
~ -[MLGLMClassification .cxx_construct] : 80 -> 84
~ __ZN6CoreML10NNCompiler7Backend3MIL16MILMetadataUtils26SetFlexibleShapesAttributeERN3MIL10MILContextERNS4_10IRFunctionERKNSt3__13mapINS9_12basic_stringIcNS9_11char_traitsIcEENS9_9allocatorIcEEEENS9_6vectorIiNSE_IiEEEENS9_4lessISG_EENSE_INS9_4pairIKSG_SJ_EEEEEERKNSA_ISG_N8Espresso17net_configurationESL_NSE_INSM_ISN_SU_EEEEEERKNSA_ISG_NS0_12MLRangeShapeESL_NSE_INSM_ISN_S10_EEEEEE : 3056 -> 3052
~ __ZN6CoreML10NNCompiler7Backend3MIL16MILMetadataUtilsL14GetRangeShapesERKNS0_14MLFunctionInfoE : 828 -> 804
~ __ZZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_6vectorIPKN3MIL11IRDimensionENS5_ISC_EEEEEENS_22__unordered_map_hasherIS7_NS_4pairIKS7_SE_EENS_4hashIS7_EENS_8equal_toIS7_EEEENS_21__unordered_map_equalIS7_SJ_SN_SL_EENS5_ISJ_EEE16__emplace_uniqueB9fqe220106IJRKNS_21piecewise_construct_tENS_5tupleIJRSI_EEENSX_IJEEEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeISF_PvEEEEbEEDpOT_ENKUlSY_SW_OSZ_OS10_E_clESY_SW_S1B_S1C_ : 1088 -> 1080
~ -[MLLayerPath hash] : 348 -> 340
~ __ZN6CoreML10NNCompiler7Backend13NeuralNetwork40UpdatableNeuralNetworkEspressoNetBackendD0Ev : 68 -> 76
~ __ZL21compileUpdatableModelRKN6CoreML10NNCompiler13NeuralNetwork22NeuralNetworkSpecProxyERKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEER8OArchiveRU8__strongP7NSError : 6560 -> 6552
~ sub_195e74d0c -> sub_195f6ad04 : 900 -> 896
~ sub_195e75090 -> sub_195f6b084 : 952 -> 936
~ sub_195e75448 -> sub_195f6b42c : 952 -> 936
~ sub_195e75b74 -> sub_195f6bb48 : 952 -> 936
~ sub_195e90360 -> sub_195f86324 : 552 -> 556
~ sub_195e9081c -> sub_195f867e4 : 352 -> 364
~ sub_195e9097c -> sub_195f86950 : 628 -> 604
~ sub_195e91000 -> sub_195f86fbc : 624 -> 628
~ sub_195e96314 -> sub_195f8c2d4 : 244 -> 248
~ sub_195e96408 -> sub_195f8c3cc : 236 -> 240
~ sub_195e96914 -> sub_195f8c8dc : 168 -> 172
~ sub_195ea41d8 -> sub_195f9a1a4 : 1316 -> 1252
~ sub_195ebb100 -> sub_195fb108c : 2848 -> 2856
~ sub_195ed2054 -> sub_195fc7fe8 : 7732 -> 7724
~ sub_195ed9628 -> sub_195fcf5b4 : 7672 -> 7684
~ sub_195efecf8 -> sub_195ff4c90 : 724 -> 732
~ sub_195effdb0 -> sub_195ff5d50 : 816 -> 792
~ sub_195f00350 -> sub_195ff62d8 : 940 -> 948
~ sub_195f058d4 -> sub_195ffb864 : 400 -> 404
~ sub_195f06374 -> sub_195ffc308 : 356 -> 360
~ sub_195f067e0 -> sub_195ffc778 : 364 -> 368
~ sub_195f071bc -> sub_195ffd158 : 232 -> 224
~ sub_195f072a4 -> sub_195ffd238 : 272 -> 264
~ sub_195f073b4 -> sub_195ffd340 : 276 -> 256
~ sub_195f074c8 -> sub_195ffd440 : 284 -> 288
~ sub_195f075e4 -> sub_195ffd560 : 248 -> 244
~ sub_195f076dc -> sub_195ffd654 : 268 -> 264
~ sub_195f077e8 -> sub_195ffd75c : 264 -> 260
~ sub_195f083a8 -> sub_195ffe318 : 1456 -> 1464
~ sub_195f17954 -> sub_19600d8cc : 1804 -> 1816
~ sub_195f1a3e4 -> sub_196010368 : 1804 -> 1816
~ sub_195f30630 -> sub_1960265c0 : 1792 -> 1788
~ sub_195f475ac -> sub_19603d538 : 1800 -> 1804
~ sub_195f48814 -> sub_19603e7a4 : 1972 -> 1980
~ sub_195f49380 -> sub_19603f318 : 584 -> 576
~ sub_195f515e4 -> sub_196047574 : 60736 -> 61008
~ sub_195f68fb8 -> sub_19605f058 : 472 -> 476
~ sub_195f6ecd8 -> sub_196064d7c : 436 -> 408
~ sub_195f6f1ac -> sub_196065234 : 680 -> 676
~ sub_195f6fa20 -> sub_196065aa4 : 384 -> 380
~ sub_195f6fd08 -> sub_196065d88 : 404 -> 376
~ sub_195f6fe9c -> sub_196065f00 : 708 -> 704
~ sub_195f70374 -> sub_1960663d4 : 1464 -> 1472
~ sub_195f7092c -> sub_196066994 : 1464 -> 1472
~ sub_195f70ee4 -> sub_196066f54 : 1448 -> 1456
~ sub_195f71a34 -> sub_196067aac : 1468 -> 1480
~ ___swift_closure_destructor.8 : 16 -> 4
~ __ZN15LayerTranslator6addMaxERKN6CoreML13Specification18NeuralNetworkLayerE : 1952 -> 1956
~ __ZN15LayerTranslator10addAverageERKN6CoreML13Specification18NeuralNetworkLayerE : 3000 -> 3004
~ __ZN15LayerTranslator6addAddERKN6CoreML13Specification18NeuralNetworkLayerE : 2112 -> 2116
~ __ZN15LayerTranslator6addMinERKN6CoreML13Specification18NeuralNetworkLayerE : 1952 -> 1956
~ __ZN15LayerTranslator11addReduceL1ERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator11addReduceL2ERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator12addReduceMaxERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator12addReduceMinERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator13addReduceProdERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator13addReduceMeanERKN6CoreML13Specification18NeuralNetworkLayerE : 3896 -> 3876
~ __ZN15LayerTranslator18addReduceLogSumExpERKN6CoreML13Specification18NeuralNetworkLayerE : 4976 -> 4984
~ __ZN15LayerTranslator11addMultiplyERKN6CoreML13Specification18NeuralNetworkLayerE : 2128 -> 2132
~ __Z30validateUpdatableNeuralNetworkIN6CoreML13Specification13NeuralNetworkEENS0_6ResultERKT_ : 4140 -> 4156
~ __Z30validateUpdatableNeuralNetworkIN6CoreML13Specification23NeuralNetworkClassifierEENS0_6ResultERKT_ : 4148 -> 4132
~ __ZL37validateOtherTopLevelUpdateParametersRKN6CoreML13Specification23NetworkUpdateParametersE : 544 -> 524
~ __ZNK6CoreML27NeuralNetworkValidatorGraph15getNodeFromNameENSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 124 -> 128
~ __ZNSt3__116allocator_traitsINS_9allocatorIN6CoreML9LayerNodeEEEE9constructB9fqe220106IS3_JS3_ELi0EEEvRS4_PT_DpOT0_ : 180 -> 176
~ __ZNSt3__116allocator_traitsINS_9allocatorIN6CoreML9LayerNodeEEEE7destroyB9fqe220106IS3_Li0EEEvRS4_PT_ : 148 -> 120
~ __ZNSt3__16vectorIN6CoreML9LayerNodeENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 300 -> 316
~ __ZN6CoreML9LayerNodeC2EPKNS_13Specification18NeuralNetworkLayerE : 744 -> 760
~ __ZNSt3__16vectorIPN6CoreML9LayerNodeENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_ : 232 -> 248
~ __ZNSt3__15dequeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backERKS6_ : 1296 -> 1308
~ __ZNSt3__16vectorIN6CoreML9LayerNodeENS_9allocatorIS2_EEE16__destroy_vectorclB9fqe220106Ev : 136 -> 140
~ __ZN6CoreML26NeuralNetworkSpecValidator16validateGRULayerERKNS_13Specification18NeuralNetworkLayerE : 5088 -> 5080
~ __ZN6CoreML26NeuralNetworkSpecValidator23validateFailUnknownTypeERKNS_13Specification18NeuralNetworkLayerE : 552 -> 560
~ __ZL39MLActivationParamsNonlinearityType_Name34MLActivationParamsNonlinearityType : 324 -> 316
~ __ZN6CoreML24validateModelDescriptionERKNS_13Specification16ModelDescriptionEiRKNS_16ValidationPolicyE : 3500 -> 3492
~ __ZN6CoreML8validateIL11MLModelType403EEENS_6ResultERKNS_13Specification5ModelE : 5164 -> 5192
~ __ZN6CoreML8validateIL11MLModelType303EEENS_6ResultERKNS_13Specification5ModelE : 3328 -> 3336
~ __ZN6CoreML8validateIL11MLModelType500EEENS_6ResultERKNS_13Specification5ModelE : 4048 -> 4044
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SC_EESA_EENS5_ISH_EEE21__construct_from_treeB9fqe220106IZNSK_21__copy_construct_treeB9fqe220106EPNS_11__tree_nodeISD_PvEEEUlRKSH_E_EESP_SP_T_ : 360 -> 356
~ __ZN6CoreML21validateTensorMessageERKNS_13Specification6TensorERKNS0_18NeuralNetworkLayerE : 400 -> 376
~ __ZN6CoreML26NeuralNetworkSpecValidator21validateNeuralNetworkINS_13Specification22NeuralNetworkRegressorEEENS_6ResultERKT_ : 4580 -> 4552
~ __ZN6CoreMLL8validateERKNS_13Specification5ModelERKNS0_8PipelineE : 3836 -> 3828
~ __ZN6CoreML8validateIL11MLModelType2002EEENS_6ResultERKNS_13Specification5ModelE : 2792 -> 2816
~ __ZN6CoreML13TreeEnsembles40constructAndValidateTreeEnsembleFromSpecERKNS_13Specification5ModelE : 10412 -> 10492
~ __ZN6CoreML11Recommender53constructAndValidateItemSimilarityRecommenderFromSpecERKNS_13Specification5ModelE : 6812 -> 6844
~ __ZNSt3__16__treeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS6_EENS4_IS6_EEE16__construct_nodeIJRS6_EEENS_10unique_ptrINS_11__tree_nodeIS6_PvEENS_22__tree_node_destructorINS4_ISG_EEEEEEDpOT_ : 160 -> 164
~ __ZN6google8protobuf8internal15ThreadSafeArena23AllocateAlignedFallbackEmPKSt9type_info : 252 -> 244
~ __ZN6google8protobuf5Arena26AllocateAlignedWithCleanupEmPKSt9type_info : 192 -> 200
~ __ZN6google8protobuf8internal18ThreadLocalStorageINS1_15ThreadSafeArena11ThreadCacheEE6DeleteEPv : 24 -> 16
~ __ZN6google8protobuf20stringpiece_internal11StringPiece18LogFatalSizeTooBigEmPKc : 292 -> 296
~ __ZN6google8protobuf8internal17PackedInt32ParserEPvPKcPNS1_12ParseContextE : 360 -> 336
~ __ZN6google8protobuf8internal18PackedUInt64ParserEPvPKcPNS1_12ParseContextE : 340 -> 344
~ __ZN6google8protobuf8internal16PackedBoolParserEPvPKcPNS1_12ParseContextE : 348 -> 352
~ __ZN6google8protobuf8internal11FieldParserINS1_28UnknownFieldLiteParserHelperEEEPKcyRT_S5_PNS1_12ParseContextE : 1604 -> 1592
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIiLb0EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 188 -> 168
~ __ZN8nlohmann6detail9dtoa_impl36get_cached_power_for_binary_exponentEi : 184 -> 188
~ _OUTLINED_FUNCTION_0 : 48 -> 56
~ ___Block_byref_object_dispose_ : 12 -> 16
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendB9fqe220106IPKcLi0EEERS5_T_SA_ : 400 -> 384
~ ___Block_byref_object_dispose_.5492 : 32 -> 8
~ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEC1EPKcj : 460 -> 444
~ __ZNSt3__113__tree_removeB9fqe220106IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 972 -> 984
~ ___Block_byref_object_dispose_.9965 : 8 -> 16
~ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqe220106ERKNS_12basic_stringIcS2_S4_EEj : 224 -> 240
~ ___Block_byref_object_dispose_.12693 : 20 -> 4
~ ___Block_byref_object_dispose_.13695 : 8 -> 24
~ ___Block_byref_object_dispose_.16435 : 24 -> 8
~ ___Block_byref_object_dispose_.17857 : 28 -> 32
~ ____ZL27getXGBoosterCreateSymbolLocv_block_invoke : 92 -> 96
~ ____ZL34getXGDMatrixCreateFromMatSymbolLocv_block_invoke : 100 -> 88
~ ___Block_byref_object_dispose_.19836 : 20 -> 32
~ ___Block_byref_object_dispose_.20260 : 16 -> 8
~ ___Block_byref_object_dispose_.21946 : 32 -> 28
~ ___Block_byref_object_dispose_.23569 : 8 -> 12
~ ___Block_byref_object_dispose_.28475 : 32 -> 24
~ ___Block_byref_object_dispose_.28868 : 36 -> 16
~ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEED2Ev : 212 -> 208
~ __ZN6KernelD0Ev : 16 -> 20
~ __ZN8Archiver13_IArchiveImplD0Ev : 8 -> 24
~ __ZN8Archiver13_OArchiveImplD0Ev : 16 -> 20
~ ___56+[MLBackgroundWatchdog watchdogWithTimeout:label:queue:]_block_invoke : 224 -> 204
~ __ZN8nlohmann6detail5lexerINS_10basic_jsonINSt3__13mapENS3_6vectorENS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEbxydS9_NS_14adl_serializerENS5_IhNS9_IhEEEEEENS0_20input_stream_adapterEE18next_byte_in_rangeESt16initializer_listIiE.cold.1 : 156 -> 164
```
