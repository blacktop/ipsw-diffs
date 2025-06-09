## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`

```diff

-8.0.78.0.0
-  __TEXT.__text: 0x2d0a8
+9.0.23.0.0
+  __TEXT.__text: 0x2e834
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x27ac
+  __TEXT.__objc_methlist: 0x28ac
   __TEXT.__const: 0x114
-  __TEXT.__dlopen_cstrs: 0x190
-  __TEXT.__gcc_except_tab: 0x26c0
-  __TEXT.__cstring: 0x3571
+  __TEXT.__dlopen_cstrs: 0x1dc
+  __TEXT.__gcc_except_tab: 0x27b0
+  __TEXT.__cstring: 0x360f
   __TEXT.__oslogstring: 0x1d5
-  __TEXT.__unwind_info: 0xf40
-  __TEXT.__objc_classname: 0xa5a
-  __TEXT.__objc_methname: 0x77ac
-  __TEXT.__objc_methtype: 0x212c
-  __TEXT.__objc_stubs: 0x3ec0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x658
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__unwind_info: 0xfe8
+  __TEXT.__objc_classname: 0xac6
+  __TEXT.__objc_methname: 0x7aa0
+  __TEXT.__objc_methtype: 0x1c53
+  __TEXT.__objc_stubs: 0x4000
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1670
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_selrefs: 0x16e0
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x3700
-  __AUTH_CONST.__objc_const: 0x5210
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__cfstring: 0x37c0
+  __AUTH_CONST.__objc_const: 0x5400
+  __AUTH_CONST.__objc_intobj: 0x408
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x3c8
-  __DATA.__bss: 0x160
-  __DATA_DIRTY.__objc_data: 0x1220
-  __DATA_DIRTY.__bss: 0x88
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x310
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x178
+  __DATA_DIRTY.__objc_data: 0x1130
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3B58D17F-DE9D-374B-9028-610B2BD9BD8F
-  Functions: 917
-  Symbols:   3691
-  CStrings:  2325
+  UUID: DBC3C114-D4F8-31BB-BE44-34B1DD605114
+  Functions: 944
+  Symbols:   3799
+  CStrings:  2363
 
Symbols:
+ +[VisionCoreISPInferenceNetworkDescriptor _configurationForIdentifier:]
+ +[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectClassesDetectionStatusIndexesV7]
+ +[VisionCoreSmudgeInferenceNetworkDescriptor _createDescriptorWithError:]
+ +[VisionCoreSmudgeInferenceNetworkDescriptor modelFileURLForModelVersion:error:]
+ +[VisionCoreSmudgeInferenceNetworkDescriptor smudgeDetectionNetworkForModelVersion:error:]
+ +[VisionCoreSmudgeInferenceNetworkDescriptor supportedANEGenerationLowerBoundForModelFileName:]
+ +[VisionCoreSmudgeInferenceNetworkDescriptor supportedFullANEResidencyGenerationLowerBoundForModelFileName:]
+ +[VisionCoreVideoSegmentationE5NetworkDescriptor _configurationForIdentifier:]
+ +[VisionCoreVideoSegmentationE5NetworkDescriptor descriptorForIdentifier:version:error:]
+ +[VisionCoreVideoSegmentationInferenceNetworkDescriptor _configurationForIdentifier:version:]
+ +[VisionCoreVideoSegmentationInferenceNetworkDescriptor supportedIdentifiersForVersion:]
+ -[VisionCoreANSTInferenceNetworkDescriptor initWithDescriptor:version:identifier:]
+ -[VisionCoreE5RTFunction(VideoSegmentation) requiresPostProcessing]
+ -[VisionCoreE5RTProgramLibraryCompilationOptions milEntryPoints]
+ -[VisionCoreE5RTProgramLibraryCompilationOptions setMilEntryPoints:]
+ -[VisionCoreISPInferenceNetworkDescriptor initWithDescriptor:identifier:error:]
+ -[VisionCoreSmudgeInferenceNetworkDescriptor isEqual:]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor .cxx_destruct]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor URL]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor descriptorForConfig:identifier:error:]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor functionForIdentifier:error:]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor initWithSpecifier:url:]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor postProcessUpdateFrameForInferenceOutputKeyBuffer:inferenceOutputValueBuffer:postProcessingOutputKeyBuffer:postProcessingOutputValueBuffer:error:]
+ -[VisionCoreVideoSegmentationE5NetworkDescriptor postProcessingOutputDescriptorsForFunction:]
+ GCC_except_table102
+ GCC_except_table122
+ GCC_except_table13
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table15
+ GCC_except_table153
+ GCC_except_table159
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table18
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table21
+ GCC_except_table224
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table240
+ GCC_except_table242
+ GCC_except_table248
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table285
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table396
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table423
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table445
+ GCC_except_table446
+ GCC_except_table452
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table548
+ GCC_except_table550
+ GCC_except_table551
+ GCC_except_table570
+ GCC_except_table611
+ GCC_except_table612
+ GCC_except_table615
+ GCC_except_table625
+ GCC_except_table633
+ GCC_except_table640
+ GCC_except_table641
+ GCC_except_table642
+ GCC_except_table659
+ GCC_except_table680
+ GCC_except_table687
+ GCC_except_table689
+ GCC_except_table692
+ GCC_except_table693
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table696
+ GCC_except_table697
+ GCC_except_table712
+ GCC_except_table716
+ GCC_except_table777
+ GCC_except_table781
+ GCC_except_table793
+ GCC_except_table794
+ GCC_except_table795
+ GCC_except_table803
+ GCC_except_table806
+ GCC_except_table820
+ GCC_except_table888
+ GCC_except_table899
+ GCC_except_table900
+ GCC_except_table901
+ GCC_except_table924
+ GCC_except_table932
+ GCC_except_table933
+ _ANSTKitLibrary.1095
+ _ANSTKitLibrary.1263
+ _ANSTKitLibrary.2528
+ _ANSTKitLibrary.2829
+ _ANSTKitLibraryCore.frameworkLibrary.1098
+ _ANSTKitLibraryCore.frameworkLibrary.1266
+ _ANSTKitLibraryCore.frameworkLibrary.2531
+ _ANSTKitLibraryCore.frameworkLibrary.2832
+ _OBJC_CLASS_$_VisionCoreSmudgeInferenceNetworkDescriptor
+ _OBJC_CLASS_$_VisionCoreVideoSegmentationE5NetworkDescriptor
+ _OBJC_IVAR_$_VisionCoreE5RTProgramLibraryCompilationOptions._milEntryPoints
+ _OBJC_IVAR_$_VisionCoreVideoSegmentationE5NetworkDescriptor._URL
+ _OBJC_IVAR_$_VisionCoreVideoSegmentationE5NetworkDescriptor._anstUpdateFramePostProcessor
+ _OBJC_IVAR_$_VisionCoreVideoSegmentationE5NetworkDescriptor._currentANSTDescriptor
+ _OBJC_IVAR_$_VisionCoreVideoSegmentationE5NetworkDescriptor._programLibrary
+ _OBJC_METACLASS_$_VisionCoreSmudgeInferenceNetworkDescriptor
+ _OBJC_METACLASS_$_VisionCoreVideoSegmentationE5NetworkDescriptor
+ _VisionCoreInferenceNetworkIdentifierSmudgeDetector
+ _VisionCoreVideoSegmentationE5InferenceNetworkIdentifier
+ __OBJC_$_CLASS_METHODS_VisionCoreSmudgeInferenceNetworkDescriptor
+ __OBJC_$_CLASS_METHODS_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __OBJC_$_INSTANCE_METHODS_VisionCoreE5RTFunction(VideoSegmentation)
+ __OBJC_$_INSTANCE_METHODS_VisionCoreSmudgeInferenceNetworkDescriptor
+ __OBJC_$_INSTANCE_METHODS_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __OBJC_$_PROP_LIST_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __OBJC_CLASS_RO_$_VisionCoreSmudgeInferenceNetworkDescriptor
+ __OBJC_CLASS_RO_$_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __OBJC_METACLASS_RO_$_VisionCoreSmudgeInferenceNetworkDescriptor
+ __OBJC_METACLASS_RO_$_VisionCoreVideoSegmentationE5NetworkDescriptor
+ __ZNKSt3__111__copy_implclB8ne200100IPDhS2_NS_20back_insert_iteratorINS_6vectorIDhNS_9allocatorIDhEEEEEEEENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__111__copy_implclB8ne200100IPmS2_NS_20back_insert_iteratorINS_6vectorImNS_9allocatorImEEEEEEEENS_4pairIT_T1_EESA_T0_SB_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI30VisionCoreValueConfidencePointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIDhEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERZ57-[VisionCoreValueConfidenceCurve _finalizeInitialization]E3$_0P30VisionCoreValueConfidencePointEEbT1_S6_T0_
+ __ZNSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEEC2B8ne200100EmRKS1_
+ __ZNSt3__16vectorI30VisionCoreValueConfidencePointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI30VisionCoreValueConfidencePointNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIDhNS_9allocatorIDhEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIDhNS_9allocatorIDhEEE18__assign_with_sizeB8ne200100IPDhS5_EEvT_T0_l
+ __ZNSt3__16vectorIDhNS_9allocatorIDhEEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPDhEES7_EES7_NS5_IPKDhEET_T0_l
+ __ZNSt3__16vectorIDhNS_9allocatorIDhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDhNS_9allocatorIDhEEEC2B8ne200100Em
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPKfS6_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne200100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100EmRKi
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8ne200100IPmS5_EEvT_T0_l
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8ne200100EOm
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8ne200100ERKm
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERZ57-[VisionCoreValueConfidenceCurve _finalizeInitialization]E3$_0P30VisionCoreValueConfidencePointLi0EEEvT1_S6_S6_S6_S6_T0_
+ __ZNSt3__1ssB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___114+[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectClassesDetectionStatusIndexesV7]_block_invoke
+ ___96+[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectOutputNamesV7]_block_invoke
+ ___ANSTKitLibraryCore_block_invoke.1099
+ ___ANSTKitLibraryCore_block_invoke.1267
+ ___ANSTKitLibraryCore_block_invoke.2532
+ ___ANSTKitLibraryCore_block_invoke.2833
+ ___block_literal_global.1056
+ ___block_literal_global.1176
+ ___block_literal_global.119
+ ___block_literal_global.1333
+ ___block_literal_global.139
+ ___block_literal_global.1461
+ ___block_literal_global.152
+ ___block_literal_global.1866
+ ___block_literal_global.1926
+ ___block_literal_global.2231
+ ___block_literal_global.2600
+ ___block_literal_global.2787
+ ___block_literal_global.3370
+ ___block_literal_global.3445
+ ___block_literal_global.3454
+ ___block_literal_global.421
+ ___block_literal_global.871
+ ___getANSTViSegHQInferenceConfigurationClass_block_invoke.2870
+ ___getANSTViSegHQInitialFrameInferenceDescriptorClass_block_invoke.2841
+ ___getANSTViSegHQRegularFrameInferenceDescriptorClass_block_invoke.2838
+ ___getANSTViSegHQUpdateFrameInferenceDescriptorClass_block_invoke.2828
+ ___getANSTViSegHQUpdateFramePostProcessorClass_block_invoke
+ __objectClassIDsToObjectClassesDetectionStatusIndexesV7.objectClassIDsToObjectClassesDetectionStatusIndexes
+ __objectClassIDsToObjectClassesDetectionStatusIndexesV7.onceToken
+ __objectClassIDsToObjectOutputNamesV7.objectClassIDsToObjectClassOutputNames
+ __objectClassIDsToObjectOutputNamesV7.onceToken
+ _audit_stringANSTKit.1102
+ _audit_stringANSTKit.1270
+ _audit_stringANSTKit.2535
+ _audit_stringANSTKit.2836
+ _e5rt_e5_compiler_options_set_mil_entry_points
+ _getANSTViSegHQInferenceConfigurationClass.softClass.2869
+ _getANSTViSegHQInitialFrameInferenceDescriptorClass
+ _getANSTViSegHQInitialFrameInferenceDescriptorClass.softClass.2840
+ _getANSTViSegHQRegularFrameInferenceDescriptorClass.2821
+ _getANSTViSegHQRegularFrameInferenceDescriptorClass.softClass.2837
+ _getANSTViSegHQUpdateFrameInferenceDescriptorClass.2822
+ _getANSTViSegHQUpdateFrameInferenceDescriptorClass.softClass.2827
+ _getANSTViSegHQUpdateFramePostProcessorClass.softClass
+ _objc_msgSend$_configurationForIdentifier:
+ _objc_msgSend$_configurationForIdentifier:version:
+ _objc_msgSend$_createDescriptorWithError:
+ _objc_msgSend$e5FunctionName
+ _objc_msgSend$initWithDescriptor:identifier:error:
+ _objc_msgSend$initWithDescriptor:version:identifier:
+ _objc_msgSend$initWithSpecifier:url:
+ _objc_msgSend$milEntryPoints
+ _objc_msgSend$processKeyTensorWithSrcBaseAddress:dstBaseAddress:error:
+ _objc_msgSend$processValueTensorWithSrcBaseAddress:dstBaseAddress:error:
+ _objc_msgSend$requiresPostProcessing
+ _objc_msgSend$requiresPostprocessing
+ _objc_msgSend$setMilEntryPoints:
+ _objc_msgSend$supportedANEGenerationLowerBoundForModelFileName:
+ _objc_msgSend$supportedFullANEResidencyGenerationLowerBoundForModelFileName:
+ _objc_msgSend$supportedIdentifiersForVersion:
+ _sgelqf$NEWLAPACK
+ _sgesvd$NEWLAPACK
+ _sormlq$NEWLAPACK
- +[VisionCoreFaceprintInferenceNetworkDescriptor FPrev3_1FArev1_3_MD2AndReturnError:]
- +[VisionCoreFaceprintInferenceNetworkDescriptor faceAttributesV1_3]
- +[VisionCoreFaceprintInferenceNetworkDescriptor faceprintInferenceNetworkDescriptorForIndentifier:modelName:aneModelName:pixelFotmatType:faceAnalyzerDetectorVersion:faceprintVersion:faceattributesVersion:error:]
- +[VisionCoreISPInferenceNetworkDescriptor _configurationForIdentifer:]
- +[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectClassesDetectionStatusIndexesV6]
- +[VisionCoreVideoSegmentationInferenceNetworkDescriptor _configurationForIdentifer:version:]
- +[VisionCoreVideoSegmentationInferenceNetworkDescriptor supportedIdentifersForVersion:]
- -[VisionCoreANSTInferenceNetworkDescriptor initWithDescriptor:identifer:]
- -[VisionCoreISPInferenceNetworkDescriptor initWithDescriptor:identifer:error:]
- GCC_except_table114
- GCC_except_table12
- GCC_except_table121
- GCC_except_table126
- GCC_except_table136
- GCC_except_table139
- GCC_except_table14
- GCC_except_table141
- GCC_except_table144
- GCC_except_table16
- GCC_except_table160
- GCC_except_table161
- GCC_except_table162
- GCC_except_table164
- GCC_except_table165
- GCC_except_table166
- GCC_except_table167
- GCC_except_table168
- GCC_except_table181
- GCC_except_table184
- GCC_except_table186
- GCC_except_table187
- GCC_except_table188
- GCC_except_table19
- GCC_except_table192
- GCC_except_table215
- GCC_except_table216
- GCC_except_table217
- GCC_except_table218
- GCC_except_table219
- GCC_except_table22
- GCC_except_table220
- GCC_except_table221
- GCC_except_table222
- GCC_except_table223
- GCC_except_table233
- GCC_except_table24
- GCC_except_table276
- GCC_except_table286
- GCC_except_table289
- GCC_except_table320
- GCC_except_table321
- GCC_except_table357
- GCC_except_table364
- GCC_except_table367
- GCC_except_table369
- GCC_except_table370
- GCC_except_table371
- GCC_except_table372
- GCC_except_table374
- GCC_except_table386
- GCC_except_table387
- GCC_except_table389
- GCC_except_table390
- GCC_except_table391
- GCC_except_table392
- GCC_except_table393
- GCC_except_table397
- GCC_except_table408
- GCC_except_table409
- GCC_except_table414
- GCC_except_table430
- GCC_except_table431
- GCC_except_table434
- GCC_except_table436
- GCC_except_table437
- GCC_except_table447
- GCC_except_table451
- GCC_except_table453
- GCC_except_table457
- GCC_except_table465
- GCC_except_table473
- GCC_except_table539
- GCC_except_table541
- GCC_except_table542
- GCC_except_table564
- GCC_except_table603
- GCC_except_table605
- GCC_except_table606
- GCC_except_table607
- GCC_except_table623
- GCC_except_table627
- GCC_except_table630
- GCC_except_table634
- GCC_except_table653
- GCC_except_table672
- GCC_except_table678
- GCC_except_table686
- GCC_except_table702
- GCC_except_table706
- GCC_except_table767
- GCC_except_table771
- GCC_except_table791
- GCC_except_table859
- GCC_except_table870
- GCC_except_table871
- GCC_except_table872
- GCC_except_table895
- GCC_except_table903
- GCC_except_table904
- GCC_except_table94
- _ANSTKitLibrary.1042
- _ANSTKitLibrary.1208
- _ANSTKitLibrary.2454
- _ANSTKitLibraryCore.frameworkLibrary.1045
- _ANSTKitLibraryCore.frameworkLibrary.1211
- _ANSTKitLibraryCore.frameworkLibrary.2457
- __OBJC_$_INSTANCE_METHODS_VisionCoreE5RTFunction
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI30VisionCoreValueConfidencePointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDhNS_9allocatorIDhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI30VisionCoreValueConfidencePointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDhEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__120back_insert_iteratorINS_6vectorIDhNS_9allocatorIDhEEEEEaSB8ne190102ERKDh
- __ZNSt3__120back_insert_iteratorINS_6vectorImNS_9allocatorImEEEEEaSB8ne190102ERKm
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZ57-[VisionCoreValueConfidenceCurve _finalizeInitialization]E3$_0P30VisionCoreValueConfidencePointEEbT1_S6_T0_
- __ZNSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI20VisionCoreHomographyNS_9allocatorIS1_EEEC2B8ne190102EmRKS1_
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorIDhNS_9allocatorIDhEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIDhNS_9allocatorIDhEEE18__assign_with_sizeB8ne190102IPDhS5_EEvT_T0_l
- __ZNSt3__16vectorIDhNS_9allocatorIDhEEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPDhEES7_EES7_NS5_IPKDhEET_T0_l
- __ZNSt3__16vectorIDhNS_9allocatorIDhEEEC2B8ne190102Em
- __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne190102IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102EmRKi
- __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8ne190102IPmS5_EEvT_T0_l
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZ57-[VisionCoreValueConfidenceCurve _finalizeInitialization]E3$_0P30VisionCoreValueConfidencePointEEjT1_S6_S6_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZ57-[VisionCoreValueConfidenceCurve _finalizeInitialization]E3$_0P30VisionCoreValueConfidencePointEEvT1_S6_S6_S6_T0_
- __ZNSt3__1ssB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___114+[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectClassesDetectionStatusIndexesV6]_block_invoke
- ___96+[VisionCoreSemanticSegmentationInferenceNetworkDescriptor _objectClassIDsToObjectOutputNamesV6]_block_invoke
- ___ANSTKitLibraryCore_block_invoke.1046
- ___ANSTKitLibraryCore_block_invoke.1212
- ___ANSTKitLibraryCore_block_invoke.2458
- ___block_literal_global.1004
- ___block_literal_global.111
- ___block_literal_global.1121
- ___block_literal_global.124
- ___block_literal_global.1277
- ___block_literal_global.1404
- ___block_literal_global.1805
- ___block_literal_global.1863
- ___block_literal_global.2167
- ___block_literal_global.2529
- ___block_literal_global.2713
- ___block_literal_global.3205
- ___block_literal_global.3279
- ___block_literal_global.3288
- ___block_literal_global.375
- ___block_literal_global.828
- ___block_literal_global.97
- __objectClassIDsToObjectClassesDetectionStatusIndexesV6.objectClassIDsToObjectClassesDetectionStatusIndexes
- __objectClassIDsToObjectClassesDetectionStatusIndexesV6.onceToken
- __objectClassIDsToObjectOutputNamesV6.objectClassIDsToObjectClassOutputNames
- __objectClassIDsToObjectOutputNamesV6.onceToken
- _audit_stringANSTKit.1049
- _audit_stringANSTKit.1215
- _audit_stringANSTKit.2461
- _objc_msgSend$_configurationForIdentifer:
- _objc_msgSend$_configurationForIdentifer:version:
- _objc_msgSend$initWithDescriptor:identifer:
- _objc_msgSend$initWithDescriptor:identifer:error:
- _objc_msgSend$initWithMajor:
- _objc_msgSend$supportedIdentifersForVersion:
- _sgelqf_
- _sgesvd_
- _sormlq_
CStrings:
+ "*"
+ "@\"ANSTViSegHQUpdateFramePostProcessor\""
+ "@152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}16"
+ "@160@0:8@16{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}24"
+ "ANSTViSegHQUpdateFramePostProcessor"
+ "B56@0:8r^v16r^v24^v32^v40^@48"
+ "Invalid ptr to destination or source buffer"
+ "T@\"NSArray\",N,V_milEntryPoints"
+ "T@\"NSURL\",R,N,V_URL"
+ "Undefined model version"
+ "Unknown smudge model"
+ "VideoSegmentation"
+ "VisionCoreInferenceNetworkIdentifierSmudgeDetector"
+ "VisionCoreSmudgeInferenceNetworkDescriptor"
+ "VisionCoreVideoSegmentationE5InferenceNetworkIdentifier"
+ "VisionCoreVideoSegmentationE5NetworkDescriptor"
+ "_URL"
+ "_anstUpdateFramePostProcessor"
+ "_configurationForIdentifier:"
+ "_configurationForIdentifier:version:"
+ "_createDescriptorWithError:"
+ "_currentANSTDescriptor"
+ "_milEntryPoints"
+ "descriptorForConfig:identifier:error:"
+ "e5FunctionName"
+ "functionForIdentifier:error:"
+ "i44@0:8i16{vector<int, std::allocator<int>>=^i^i^i}20"
+ "initWithDescriptor:identifier:error:"
+ "initWithDescriptor:version:identifier:"
+ "initWithSpecifier:url:"
+ "milEntryPoints"
+ "personsemantics-v7"
+ "personsemantics-v7.bundle/personsemantics-v7.mil"
+ "postProcessUpdateFrameForInferenceOutputKeyBuffer:inferenceOutputValueBuffer:postProcessingOutputKeyBuffer:postProcessingOutputValueBuffer:error:"
+ "postProcessingOutputDescriptorsForFunction:"
+ "processKeyTensorWithSrcBaseAddress:dstBaseAddress:error:"
+ "processValueTensorWithSrcBaseAddress:dstBaseAddress:error:"
+ "requiresPostprocessing"
+ "setMilEntryPoints:"
+ "smudgeDetectionNetworkForModelVersion:error:"
+ "smudge_probabilities"
+ "smudgenet-v1.E5"
+ "smudgenet-v1.E5.bundle/smudgenet-v1.E5.mil"
+ "supportedANEGenerationLowerBoundForModelFileName:"
+ "supportedFullANEResidencyGenerationLowerBoundForModelFileName:"
+ "supportedIdentifiersForVersion:"
+ "update"
+ "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}16"
+ "{?=[3]}152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}16"
+ "{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f^f}{vector<bool, std::allocator<bool>>=^QQQ}{vector<float, std::allocator<float>>=^f^f^f}{_RANSAC_Parameters_=ifif}}36@0:8^v16^v24f32"
+ "{vector<VisionCoreHomography, std::allocator<VisionCoreHomography>>=^{VisionCoreHomography}^{VisionCoreHomography}^{VisionCoreHomography}}60@0:8^{__CVBuffer=}16B24@28^@36^v44@52"
+ "{vector<VisionCoreValueConfidencePoint, std::allocator<VisionCoreValueConfidencePoint>>=\"__begin_\"^{VisionCoreValueConfidencePoint}\"__end_\"^{VisionCoreValueConfidencePoint}\"__cap_\"^{VisionCoreValueConfidencePoint}}"
+ "{vector<__fp16, std::allocator<__fp16>>=\"__begin_\"^ \"__end_\"^ \"__cap_\"^ }"
+ "{vector<__fp16, std::allocator<__fp16>>=^ ^ ^ }24@0:8f16i20"
+ "{vector<int, std::allocator<int>>=^i^i^i}32@0:8^v16^v24"
+ "{vector<long, std::allocator<long>>=\"__begin_\"^q\"__end_\"^q\"__cap_\"^q}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
- "@152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{_RANSAC_Parameters_=ifif}}16"
- "@160@0:8@16{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{_RANSAC_Parameters_=ifif}}24"
- "FPrev3_1FArev1_3_MD2"
- "FPrev3_1FArev1_3_MD2AndReturnError:"
- "Unkknown person instance model"
- "_configurationForIdentifer:"
- "_configurationForIdentifer:version:"
- "camalgoseg.flows.lowres-s2h6ysbnuy_82500"
- "camalgoseg.flows.lowres-s2h6ysbnuy_82500.bundle/camalgoseg.flows.lowres-s2h6ysbnuy_82500.mil"
- "facerec_fp3.1_fa1.3.espresso"
- "handheld_object"
- "i44@0:8i16{vector<int, std::allocator<int>>=^i^i{__compressed_pair<int *, std::allocator<int>>=^i}}20"
- "initWithDescriptor:identifer:"
- "initWithDescriptor:identifer:error:"
- "supportedIdentifersForVersion:"
- "v40@0:8{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}16"
- "{?=[3]}152@0:8{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{_RANSAC_Parameters_=ifif}}16"
- "{VisionCoreHomography={Geometry2D_cart2D=^f^fi}{Geometry2D_cart2D=^f^fi}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{vector<bool, std::allocator<bool>>=^QQ{__compressed_pair<unsigned long, std::allocator<unsigned long>>=Q}}{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}{_RANSAC_Parameters_=ifif}}36@0:8^v16^v24f32"
- "{vector<VisionCoreHomography, std::allocator<VisionCoreHomography>>=^{VisionCoreHomography}^{VisionCoreHomography}{__compressed_pair<VisionCoreHomography *, std::allocator<VisionCoreHomography>>=^{VisionCoreHomography}}}60@0:8^{__CVBuffer=}16B24@28^@36^v44@52"
- "{vector<VisionCoreValueConfidencePoint, std::allocator<VisionCoreValueConfidencePoint>>=\"__begin_\"^{VisionCoreValueConfidencePoint}\"__end_\"^{VisionCoreValueConfidencePoint}\"__end_cap_\"{__compressed_pair<VisionCoreValueConfidencePoint *, std::allocator<VisionCoreValueConfidencePoint>>=\"__value_\"^{VisionCoreValueConfidencePoint}}}"
- "{vector<__fp16, std::allocator<__fp16>>=\"__begin_\"^ \"__end_\"^ \"__end_cap_\"{__compressed_pair<__fp16 *, std::allocator<__fp16>>=\"__value_\"^ }}"
- "{vector<__fp16, std::allocator<__fp16>>=^ ^ {__compressed_pair<__fp16 *, std::allocator<__fp16>>=^ }}24@0:8f16i20"
- "{vector<int, std::allocator<int>>=^i^i{__compressed_pair<int *, std::allocator<int>>=^i}}32@0:8^v16^v24"
- "{vector<long, std::allocator<long>>=\"__begin_\"^q\"__end_\"^q\"__end_cap_\"{__compressed_pair<long *, std::allocator<long>>=\"__value_\"^q}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}"

```
