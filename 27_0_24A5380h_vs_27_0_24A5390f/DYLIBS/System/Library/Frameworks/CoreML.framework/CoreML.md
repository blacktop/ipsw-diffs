## CoreML

> `/System/Library/Frameworks/CoreML.framework/CoreML`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.22.1.0.0
-  __TEXT.__text: 0x704550
+3600.25.2.0.0
+  __TEXT.__text: 0x7045f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x10198
   __TEXT.__const: 0x51483
   __TEXT.__dlopen_cstrs: 0x21e
-  __TEXT.__cstring: 0x2e290
+  __TEXT.__cstring: 0x2e28c
   __TEXT.__constg_swiftt: 0x1ec8
   __TEXT.__swift5_typeref: 0x21f0
   __TEXT.__swift5_builtin: 0x1e0

   __TEXT.__swift5_capture: 0xf88
   __TEXT.__swift_as_ret: 0x110
   __TEXT.__oslogstring: 0xb288
-  __TEXT.__gcc_except_tab: 0x3aad0
+  __TEXT.__gcc_except_tab: 0x3aac0
   __TEXT.__ustring: 0x204
   __TEXT.__unwind_info: 0x10470
   __TEXT.__eh_frame: 0x54d4

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 16997
   Symbols:   27243
-  CStrings:  4769
+  CStrings:  4768
 
Functions:
~ -[MLModelConfiguration copyWithZone:] : 776 -> 768
~ ___101-[MLE5ProgramLibrary createOperationForFunctionName:forceRespecialization:hasRangeShapeInputs:error:]_block_invoke : 2844 -> 2820
~ ___60-[MLModelAssetResourceFactory modelWithConfiguration:error:]_block_invoke : 172 -> 164
~ +[MLPredictionOptions defaultOptions] : 60 -> 68
~ -[MLPipeline predictionFromFeatures:options:error:] : 688 -> 712
~ -[MLPredictionOptions setE5rtStreamReuseExpectation:] : 40 -> 16
~ __ZN12_GLOBAL__N_127makeProgramWithMemoryLayoutENSt3__110shared_ptrIKN3MIL9IRProgramEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP18MLModelDescriptionPU15__autoreleasingP7NSError : 3636 -> 3628
~ __ZN8IArchive13nestedArchiveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 544 -> 520
~ -[MLRegressor predictionFromFeatures:options:error:] : 180 -> 172
~ -[MLFeatureVectorizer predictionTypeForKTrace] : 24 -> 32
~ -[MLModel predictionFromFeatures:error:] : 268 -> 260
~ -[MLPredictionOptions init] : 8 -> 16
~ -[MLMultiArray .cxx_construct] : 24 -> 16
~ -[MLPredictionOptions copyWithZone:] : 396 -> 404
~ -[MLFeatureDescription initWithName:type:optional:contraints:] : 732 -> 756
~ +[MLModelIOUtils populateConstraintsForFeatureDescription:] : 1148 -> 1124
~ -[MLModelDescription initFromModelDescriptionSpecification:] : 904 -> 896
~ __ZN6google8protobuf3MapINSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEES8_E8InnerMap6insertIRS8_EENS2_4pairINSA_13iterator_baseINS0_7MapPairIS8_S8_EEEEbEEOT_ : 316 -> 292
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm : 96 -> 88
~ __ZN6google8protobuf8internal16InternalMetadataD2Ev : 484 -> 492
~ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEC1EPKcj : 456 -> 448
~ __ZNK8Archiver17_IArchiveDiskImpl10createBlobERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 2876 -> 2884
~ __ZN8Archiver17_IArchiveDiskImplC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_10FileFormatE : 2336 -> 2112
~ +[MLLoader _loadModelFromAssetAtURL:configuration:loaderEvent:error:] : 684 -> 676
~ __ZNK8IArchive16hasNestedArchiveERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 144 -> 152
~ __ZN6google8protobuf8internal14ArenaStringPtr22DestroyNoArenaSlowPathEv : 108 -> 100
~ __ZN6CoreML13Specification18FeatureDescriptionD0Ev : 80 -> 56
~ +[MLModelDescription metadataWithFormat:] : 788 -> 780
~ -[MLLayerPath init] : 20 -> 28
~ _MLLoggingGetCoreChannel : 108 -> 100
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification16ModelDescriptionENS_9allocatorIS3_EEE16__on_zero_sharedEv : 28 -> 36
~ __ZN6google8protobuf16RepeatedPtrFieldIN6CoreML13Specification18FeatureDescriptionEED2Ev : 80 -> 72
~ -[MLPredictionEvent init] : 184 -> 192
~ -[MLModelAssetDescription .cxx_destruct] : 80 -> 104
~ __ZN6CoreML13Specification18FeatureDescriptionD2Ev : 212 -> 220
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase13DestroyProtosEv : 128 -> 152
~ __ZN6CoreML13Specification11FeatureType10clear_TypeEv : 536 -> 544
~ -[MLModel(ModelAsset) initInterfaceAndMetadataWithCompiledArchive:error:] : 300 -> 324
~ __ZN6CoreML13Specification21DictionaryFeatureType13clear_KeyTypeEv : 168 -> 176
~ -[MLMultiArray(ScopedBufferAccess) getMutableBytesWithHandler:] : 344 -> 336
~ -[MLPredictionOptions .cxx_destruct] : 164 -> 140
~ -[MLFeatureValue doubleValue] : 52 -> 44
~ ___60-[MLFeatureVectorizer predictionFromFeatures:options:error:]_block_invoke : 32 -> 40
~ __ZNSt3__120__shared_ptr_pointerIPhZN6CoreML16MultiArrayBufferC1ES1_RKNS_6vectorImNS_9allocatorImEEEES9_NS2_10ScalarTypeEE3$_0NS5_IhEEE21__on_zero_shared_weakEv : 8 -> 32
~ -[MLFeatureVectorizer predictionFromFeatures:options:error:] : 1796 -> 1804
~ ___63+[MLMultiArray(ConvenientConstruction) doubleVectorWithValues:]_block_invoke_2 : 124 -> 116
~ -[MLModelEngine modelDescription] : 8 -> 16
~ __ZNSt3__120__shared_ptr_pointerIPN8Archiver11MMappedFileENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE16__on_zero_sharedEv : 48 -> 40
~ __ZN8Archiver11MMappedFileD0Ev : 60 -> 68
~ ___52-[MLMultiArrayShapeConstraint isAllowedShape:error:]_block_invoke : 356 -> 348
~ +[MLState emptyState] : 88 -> 96
~ -[MLMultiArray numberAtOffset:] : 292 -> 284
~ -[MLE5ProgramLibrary modelConfiguration] : 12 -> 20
~ -[MLModelAssetResourceFactoryOnDiskImpl initWithModelURL:error:] : 152 -> 144
~ -[MLModelAssetModelStructureVendor initWithResourceFactory:] : 140 -> 148
~ -[MLModelConfiguration setComputeUnits:] : 12 -> 36
~ -[MLE5ExecutionStreamOperation functionName] : 28 -> 36
~ +[MLArchivingUtils codedObjectURLFromInputArchiver:] : 300 -> 292
~ __ZrsR8IArchiveR11MLModelType : 240 -> 248
~ +[MLArchivingUtils parseModelArchive:modelType:compilerVersion:modelVersion:error:] : 700 -> 692
~ __ZrsR8IArchiveRx : 232 -> 240
~ -[MLModelDescription(RawModelDescription) initFromRawCompiledModelArchive:error:] : 200 -> 192
~ __ZN8Archiver11MMappedFileD2Ev : 272 -> 280
~ -[MLModelDescription .cxx_destruct] : 276 -> 268
~ -[MLLayerPath .cxx_destruct] : 68 -> 76
~ -[MLFeatureDescription .cxx_destruct] : 136 -> 128
~ -[MLPredictionEvent .cxx_destruct] : 136 -> 144
~ -[MLPredictionEventMetric .cxx_destruct] : 92 -> 116
~ +[MLModelIOUtils deserializeInterfaceFormat:archive:error:] : 1272 -> 1280
~ __ZN6google8protobuf11MessageLite20ParseFromCodedStreamEPNS0_2io16CodedInputStreamE : 1144 -> 1136
~ __ZN6CoreML13Specification16ModelDescription14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 1348 -> 1356
~ ___MLLoggingGetCoreChannel_block_invoke : 156 -> 148
~ +[MLModelIOUtils deserializeVersionInfoFromArchive:error:] : 268 -> 276
~ __ZN6google8protobuf24ZeroCopyCodedInputStream4NextEPPKvPi : 152 -> 176
~ __ZN6google8protobuf8internal18EpsCopyInputStream13DoneWithCheckEPPKci : 140 -> 148
~ ___37+[MLModelTypeRegistry sharedInstance]_block_invoke : 76 -> 68
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification18FeatureDescriptionEJEEEPT_PS1_DpOT0_ : 140 -> 148
~ __ZN6google8protobuf8internal12ParseContext28ReadSizeAndPushLimitAndDepthEPKcPi : 140 -> 164
~ __ZN6CoreML13Specification18FeatureDescription14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 564 -> 572
~ __ZN6google8protobuf8internal23IsStructurallyValidUTF8EPKci : 712 -> 704
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification16ArrayFeatureTypeEJEEEPT_PS1_DpOT0_ : 196 -> 204
~ __ZN6google8protobuf13RepeatedFieldIyE7ReserveEi : 292 -> 284
~ __ZN6CoreML6ResultC1Ev : 176 -> 152
~ __ZN8Archiver14_IDataBlobImplD1Ev : 32 -> 24
~ __ZNSt3__120__shared_ptr_emplaceIN8Archiver14_IDataBlobImplENS_9allocatorIS2_EEE16__on_zero_sharedEv : 56 -> 32
~ -[MLOptimizationHints setReshapeFrequency:] : 20 -> 12
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification16ModelDescriptionENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 24 -> 32
~ __ZNK8Archiver17_IArchiveDiskImpl11storageTypeEv : 36 -> 28
~ __ZrsR8IArchiveRNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 380 -> 356
~ +[MLLoader _loadModelFromArchive:configuration:modelVersion:compilerVersion:loaderEvent:useUpdatableModelLoaders:loadingClasses:error:] : 1888 -> 1880
~ __ZNSt3__120__shared_ptr_emplaceIN8Archiver14_IDataBlobImplENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 8 -> 16
~ -[MLLoaderEvent .cxx_destruct] : 320 -> 312
~ -[MLModelAssetModelVendor setCachedConfiguration:] : 16 -> 24
~ -[MLModelAsset .cxx_destruct] : 136 -> 128
~ -[MLModelAssetDescriptionVendor .cxx_destruct] : 92 -> 68
~ __ZNK8IArchive4blobERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 136 -> 128
~ __ZNK8Archiver17_IArchiveDiskImpl7getBlobERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 236 -> 244
~ __ZN8Archiver14_IDataBlobImpl13asMMappedFileEv : 536 -> 528
~ __ZNK8Archiver11MMappedFile4dataEv : 24 -> 32
~ -[MLModelDescription inputDescriptionsByName] : 16 -> 8
~ __ZN6CoreML13Specification16ArrayFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 964 -> 972
~ __ZN6google8protobuf8internal17PackedInt64ParserEPvPKcPNS1_12ParseContextE : 336 -> 360
~ __ZN6google8protobuf8internal12MapEntryImplIN6CoreML13Specification7MILSpec43Function_BlockSpecializationsEntry_DoNotUseENS0_11MessageLiteENSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEENS5_5BlockELNS1_14WireFormatLite9FieldTypeE9ELSH_11EE6ParserINS1_12MapFieldLiteIS6_SE_SF_LSH_9ELSH_11EEENS0_3MapISE_SF_EEED2Ev : 144 -> 120
~ __ZN6google8protobuf8internal18EpsCopyInputStream12DoneFallbackEii : 808 -> 832
~ __ZNK6CoreML13Specification16ModelDescription13IsInitializedEv : 28 -> 36
~ __ZN6google8protobuf2io25CopyingInputStreamAdaptorD2Ev : 148 -> 172
~ __ZN6CoreML13Specification16ArrayFeatureTypeD2Ev : 184 -> 192
~ ___22+[MLReporter reporter]_block_invoke : 64 -> 88
~ -[MLModelAssetModelVendor cachedConfiguration] : 8 -> 16
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_10shared_ptrIKN3MIL7IRValueEEES6_EENS_22__unordered_map_hasherIS6_NS_4pairIKS6_S6_EENS3_16IRValueMapHasherENS3_12IRValueMapEqEEENS_21__unordered_map_equalIS6_SB_SD_SC_EENS_9allocatorISB_EEED2Ev : 112 -> 104
~ -[MLE5ExecutionStreamOperation _newArrayOfInputPorts:featureDescriptionsByName:error:] : 800 -> 808
~ -[MLE5InputPortBinder initWithPort:featureDescription:] : 160 -> 152
~ -[MLE5ExecutionStreamOperation pixelBufferPool] : 24 -> 32
~ -[MLE5InputPortBinder setPixelBufferPool:] : 24 -> 16
~ -[MLE5OutputPort initWithPortHandle:name:featureDescription:] : 248 -> 256
~ -[MLE5OutputPortBinder initWithPort:featureDescription:] : 184 -> 176
~ -[MLE5OutputPort binder] : 36 -> 12
~ -[MLE5OutputPortBinder setPixelBufferPool:] : 12 -> 36
~ -[MLE5ExecutionStreamOperation setOutputPorts:] : 12 -> 20
~ -[MLDelegateModel predictionTypeForKTrace] : 100 -> 92
~ -[MLE5ExecutionStreamOperation modelDescription] : 24 -> 32
~ __ZN6CoreML24addMemoryLayoutToProgramENSt3__110shared_ptrIKN3MIL9IRProgramEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEP12NSDictionaryIP8NSStringP20MLFeatureDescriptionESK_ : 7352 -> 7376
~ -[MLE5ExecutionStreamOperation outputPorts] : 32 -> 8
~ __ZNSt3__120__shared_ptr_pointerIPN3MIL9IRProgramENS_14default_deleteIS2_EENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 12 -> 4
~ -[MLModelAssetModelVendor setCachedModel:] : 32 -> 40
~ -[MLOptimizationHints isEqual:] : 204 -> 196
~ -[MLModelAssetModelVendor cachedModel] : 16 -> 24
~ -[MLOutputBackingsVerifier .cxx_destruct] : 32 -> 24
~ -[MLMultiArrayConstraint .cxx_destruct] : 100 -> 108
~ -[MLGLMRegression .cxx_destruct] : 152 -> 144
~ __ZN6CoreML13Specification5ModelD2Ev : 184 -> 192
~ __ZNSt3__120__shared_ptr_emplaceIN6CoreML13Specification5ModelENS_9allocatorIS3_EEE16__on_zero_sharedEv : 36 -> 28
~ __ZN6CoreML13Specification8Int64SetD2Ev : 140 -> 148
~ -[MLModelAsset modelVendor] : 8 -> 32
~ -[MLModelAssetModelVendor resourceFactory] : 16 -> 24
~ +[MLNeuralNetworkContainer containerFromCompiledArchiveCommon:filename:modelVersionInfo:compilerVersionInfo:configuration:error:] : 1152 -> 1176
~ -[MLMultiArrayConstraint initWithShape:dataType:shapeConstraint:defaultOptionalValue:] : 376 -> 384
~ -[MLMultiArrayShapeConstraint initWithEnumeratedShapes:] : 1692 -> 1684
~ +[MLModelIOUtils outputDescriptionFromInterface:] : 12 -> 20
~ -[MLMultiArrayShapeConstraint initUnspecified] : 128 -> 152
~ +[MLModelIOUtils stateDescriptionFromInterface:] : 20 -> 28
~ -[MLModelAssetDescription usesMultiFunctionSyntax] : 88 -> 80
~ -[MLLayerPath initWithScopedModelAndLayerName:layerName:] : 184 -> 192
~ -[MLModelDescription(RawModelDescription) initFromRawModelDescriptionSpecification:] : 4 -> 28
~ +[MLModelIOUtils defaultFunctionNameFromDescriptionSpecification:] : 120 -> 128
~ -[MLMultiArray initWithDataPointer:shape:dataType:strides:deallocator:error:] : 56 -> 48
~ -[MLPredictionOptions initWithUsesCPUOnly:] : 208 -> 216
~ -[MLNeuralNetworkEngine recordsPredictionEvent] : 132 -> 156
~ -[MLPredictionOptions outputBackings] : 36 -> 12
~ -[MLModelDescription outputDescriptionsByName] : 12 -> 36
~ -[MLPredictionOptions aneQoS] : 36 -> 12
~ -[MLNeuralNetworkEngine predictionTypeForKTrace] : 16 -> 8
~ -[MLPredictionOptions parentSignpostID] : 16 -> 24
~ -[MLNeuralNetworkEngine predictionFromFeatures:options:error:] : 468 -> 460
~ -[MLModelEngine configuration] : 24 -> 32
~ -[MLNeuralNetworkEngine priority] : 36 -> 28
~ -[MLMultiArrayConstraint isAllowedValue:isNeuralNetworkInputOrOutput:usingRank5Mapping:featureName:error:] : 888 -> 896
~ -[MLNeuralNetworkEngine plan] : 32 -> 24
~ -[MLPredictionOptions inputDirectBindingExpectations] : 20 -> 28
~ -[MLNeuralNetworkEngine classLabels] : 32 -> 24
~ -[MLPredictionOptions automaticOutputBackingMode] : 28 -> 36
~ -[MLFeatureValue isUndefined] : 20 -> 12
~ -[MLMultiArrayConstraint isAllowedShape:error:] : 108 -> 116
~ -[MLNeuralNetworkEngine populateMultiArrayShape:strides:forEbuf:featureDescription:ndArrayInterpretation:] : 2488 -> 2480
~ -[MLMultiArrayConstraint shapeConstraint] : 12 -> 20
~ -[MLModelAsset setLastConfiguration:] : 28 -> 20
~ -[MLPredictionOptions outputDirectBindingExpectations] : 12 -> 20
~ -[MLNeuralNetworkEngine releaseBuffer:] : 172 -> 164
~ -[MLPredictionEvent maybeLogPredictionEvent:] : 124 -> 132
~ -[MLNeuralNetworkFunctionInfo initWithCompiledModelArchive:compilerVersionInfo:error:] : 972 -> 964
~ -[MLPredictionEvent modelType] : 8 -> 16
~ -[MLModelDescription copyWithZone:] : 876 -> 868
~ -[MLLayerPath scopedModelNames] : 12 -> 20
~ -[MLNeuralNetworkEngine initWithContainer:configuration:error:] : 1156 -> 1148
~ -[MLModelEngine initWithDescription:configuration:] : 240 -> 248
~ -[MLNeuralNetworkEngine network] : 36 -> 28
~ __ZN6CoreML13Specification17StringFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 312 -> 320
~ -[MLNeuralNetworkEngine copyImagePreprocessingParametersTo:error:] : 1420 -> 1412
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN6CoreML13Specification21DictionaryFeatureTypeEJEEEPT_PS1_DpOT0_ : 120 -> 128
~ -[MLNeuralNetworkEngine isEspressoBiasPreprocessingShared] : 36 -> 28
~ __ZN6CoreML13Specification21DictionaryFeatureType14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 484 -> 492
~ -[MLDelegateModel initWithEngine:error:] : 828 -> 852
~ -[MLModelEngine supportsConcurrentSubmissions] : 36 -> 12
~ -[MLLoaderEvent setProcessName:] : 24 -> 16
~ -[MLPredictionEvent setBundleIdentifier:] : 32 -> 8
~ __ZN12_GLOBAL__N_125loadProgramDefaultOptionsEP5NSURLPU15__autoreleasingP7NSError : 1492 -> 1484
~ +[MLAllComputeDeviceRegistry sharedRegistry] : 180 -> 188
~ __ZL22get_ANEDeviceInfoClassv : 232 -> 224
~ ___44+[MLAllComputeDeviceRegistry sharedRegistry]_block_invoke : 276 -> 252
~ -[MLE5ProgramLibraryOnDeviceAOTCompilationImpl .cxx_construct] : 12 -> 36
~ -[MLAllComputeDeviceRegistry deviceRegistries] : 12 -> 20
~ -[MLE5Engine _conformInputFeatures:error:] : 408 -> 400
~ -[MLE5ExecutionStream _reusableForInputFeatures:options:] : 508 -> 484
~ ___34-[MLE5ExecutionStreamPool takeOut]_block_invoke : 304 -> 328
~ ___41-[MLE5ExecutionStream cancelPendingReset]_block_invoke : 20 -> 28
~ __Z26MLE5PortSupportsBufferTypeP12e5rt_io_port25e5rt_buffer_object_type_t : 304 -> 328
~ __ZN12_GLOBAL__N_122dependentEventsBoundToEP31e5rt_execution_stream_operation : 688 -> 696
~ -[MLE5Engine _cleanUpAndReconfigureStream:forInputFeatures:error:] : 168 -> 192
~ -[MLE5ExecutionStreamOperation setAsyncSubmissionError:] : 24 -> 32
~ -[MLE5InputPortBinder dealloc] : 144 -> 136
~ -[MLE5ProgramLibrary .cxx_destruct] : 108 -> 116
~ __Z30MLE5MultiArrayStridesForTensorP16e5rt_tensor_desc : 780 -> 772
~ -[MLE5ExecutionStreamOperation _bindOutputPortsWithOptions:error:] : 576 -> 552
~ _MLE5TypeOfBufferObject : 240 -> 264
~ ___46-[MLE5ExecutionStreamOperation outputFeatures]_block_invoke : 44 -> 52
~ ____ZN6CoreMLL18copyMultiArrayBNNSIfiEEbRKNS_16MultiArrayBufferERS1__block_invoke_2 : 80 -> 72
~ -[MLE5OutputPort name] : 16 -> 24
~ ___55-[MLE5StaticShapeExecutionStreamOperationPool putBack:]_block_invoke : 24 -> 16
~ -[MLE5ExecutionStream setOperationPool:] : 16 -> 24
~ -[MLE5Engine _predictionFromFeatures:stream:options:error:] : 452 -> 444
~ -[MLE5ExecutionStream _prepareForInputFeatures:options:error:] : 824 -> 832
~ __ZN6CoreMLL19vectorizeMultiArrayIfDF16_EEbRKNS_16MultiArrayBufferENS_12StorageOrderERS1_ : 452 -> 444
~ -[MLE5ExecutionStreamOperation state] : 24 -> 32
~ _MLE5OutputMultiArrayFeatureValueByRetainingTensor : 132 -> 156
~ -[MLE5ExecutionStreamOperation outputFeatures] : 1116 -> 1124
~ __ZNSt3__16__treeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4lessIS6_EENS4_IS6_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSF_SF_ : 96 -> 88
~ -[MLE5ProgramLibrary prepareAndReturnError:] : 384 -> 392
~ -[MLGPUComputeDeviceRegistry registerGPUDevices] : 736 -> 728
~ +[MLGPUComputeDevice deviceWithMetalDevice:] : 104 -> 112
~ -[MLCPUComputeDeviceRegistry initWithCpuDevice:] : 124 -> 116
~ -[MLAllComputeDeviceRegistry registeredComputeDevices] : 316 -> 324
~ -[MLGPUComputeDeviceRegistry pendingChanges] : 8 -> 32
~ -[MLE5ExecutionStream operations] : 8 -> 16
~ -[MLE5InputPort name] : 28 -> 20
~ -[MLE5OutputPort featureValue] : 100 -> 108
~ -[MLE5InputPortBinder setBindingMode:] : 20 -> 12
~ -[MLE5ExecutionStreamOperation operationHandle] : 20 -> 28
~ -[MLE5ExecutionStreamPool pool] : 28 -> 20
~ -[MLE5ExecutionStreamOperation setWaitSharedEventsBoundToESOP:] : 24 -> 32
~ -[MLGPUComputeDeviceRegistry setObservationToken:] : 12 -> 36
~ -[MLGPUComputeDevice initWithMetalDevice:] : 152 -> 160
~ ___36+[MLCPUComputeDevice physicalDevice]_block_invoke : 68 -> 60
~ -[MLAllComputeDeviceRegistry initWithDeviceRegistries:] : 128 -> 136
~ -[MLE5OutputPortBinder featureDescription] : 16 -> 40
~ -[MLE5ExecutionStream operationPool] : 24 -> 32
~ -[MLE5InputPortBinder bindingMode] : 12 -> 36
~ -[MLPredictionOptions inferenceFrameDataSerialization] : 36 -> 12
~ -[MLE5ExecutionStreamPool takeOut] : 328 -> 320
~ -[MLE5ExecutionStream setState:] : 20 -> 28
~ -[MLE5Engine inputFeatureConformer] : 16 -> 40
~ -[MLE5ExecutionStream resetQueue] : 20 -> 28
~ sub_195b23038 -> sub_195c710d8 : 52 -> 44
~ -[MLModelEngine recordsPredictionEvent] : 8 -> 16
~ -[MLPipeline predictionTypeForKTrace] : 36 -> 28
~ -[MLPredictionOptions setInferenceFrameDataSerialization:] : 28 -> 36
~ sub_195d8990c -> sub_195ed79ac : 184 -> 176
~ sub_195d89b7c -> sub_195ed7c14 : 20 -> 28
~ __ZNK8Archiver17_IArchiveDiskImpl9getObjectERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 104 -> 96
~ __ZN6google8protobuf8internal15ThreadSafeArena23AllocateAlignedFallbackEmPKSt9type_info : 244 -> 252
~ __ZN6google8protobuf5Arena26AllocateAlignedWithCleanupEmPKSt9type_info : 200 -> 192
~ __ZN6google8protobuf8internal18ThreadLocalStorageINS1_15ThreadSafeArena11ThreadCacheEE6DeleteEPv : 16 -> 24
~ ___Block_byref_object_dispose_.21946 : 20 -> 12
~ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEED2Ev : 204 -> 212
~ __ZN8Archiver13_OArchiveImplD0Ev : 24 -> 16
~ ___56+[MLBackgroundWatchdog watchdogWithTimeout:label:queue:]_block_invoke : 216 -> 224
CStrings:
+ " is not a valid .mlmodelc file because the first word is not recognizable. "
+ "3600.25.2"
- " is not a valid .mlmodelc file because the first word ("
- ") is not recognizable. "
- "3600.22.1"
```
