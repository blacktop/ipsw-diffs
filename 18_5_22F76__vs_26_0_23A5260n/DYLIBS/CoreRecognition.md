## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

```diff

-404.0.0.0.0
-  __TEXT.__text: 0x4b9c4
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x207c
-  __TEXT.__const: 0x800
-  __TEXT.__cstring: 0x3695
+418.100.0.0.0
+  __TEXT.__text: 0x52868
+  __TEXT.__auth_stubs: 0x13e0
+  __TEXT.__objc_methlist: 0x2214
+  __TEXT.__const: 0x830
+  __TEXT.__cstring: 0x38c2
   __TEXT.__ustring: 0x1282
-  __TEXT.__gcc_except_tab: 0x7c94
+  __TEXT.__gcc_except_tab: 0x80cc
   __TEXT.__oslogstring: 0x52
-  __TEXT.__unwind_info: 0x11f8
+  __TEXT.__unwind_info: 0x1380
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x2d6
-  __TEXT.__objc_methname: 0x72eb
-  __TEXT.__objc_methtype: 0x178c
-  __TEXT.__objc_stubs: 0x6ec0
-  __DATA_CONST.__got: 0x5a8
+  __TEXT.__objc_classname: 0x2f1
+  __TEXT.__objc_methname: 0x78d6
+  __TEXT.__objc_methtype: 0x1745
+  __TEXT.__objc_stubs: 0x7380
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__const: 0xa18
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e20
+  __DATA_CONST.__objc_selrefs: 0x1f70
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x3dc0
-  __AUTH_CONST.__auth_got: 0xa30
-  __AUTH_CONST.__const: 0x908
-  __AUTH_CONST.__cfstring: 0xfa60
-  __AUTH_CONST.__objc_const: 0x32b8
+  __AUTH_CONST.__auth_got: 0xa08
+  __AUTH_CONST.__const: 0x990
+  __AUTH_CONST.__cfstring: 0xfc00
+  __AUTH_CONST.__objc_const: 0x35a8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1f8
-  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x90
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x26c
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH.__objc_data: 0x780
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x240
   __DATA.__bss: 0x98
-  __DATA.__common: 0x50
+  __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
+  - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D0BAB929-4F5A-3BB5-AE3F-DEB522764B5F
-  Functions: 986
-  Symbols:   4123
-  CStrings:  4688
+  UUID: 4E71FEAC-EE68-3D37-AF02-695E3DCA142F
+  Functions: 1064
+  Symbols:   4380
+  CStrings:  4791
 
Symbols:
+ +[CRCameraReader capturedCardHeightForTargetWidth:]
+ +[CRCameraReader extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:]
+ +[CRCameraReader perspectiveCorrectedImage:p1:p2:p3:p4:]
+ +[CRCameraReader platformImageFromCIImage:]
+ +[CRCameraReader scaledImage:width:height:]
+ -[CRCameraReader enableUnpaddedIDCapture]
+ -[CRCameraReader getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:unpaddedCardImage:]
+ -[CRCameraReader outputCapturedImageHeight]
+ -[CRCameraReader outputCapturedImageWidth]
+ -[CRCameraReader setEnableUnpaddedIDCapture:]
+ -[CRCameraReader setOutputCapturedImageWidth:]
+ -[CRCameraReaderOutputIDCard unpaddedImageValue]
+ -[CRCameraReaderOutputInternal setUnpaddedImageValue:]
+ -[CRCameraReaderOutputInternal unpaddedImageValue]
+ -[CRMLModel .cxx_destruct]
+ -[CRMLModel classCount]
+ -[CRMLModel codeMap]
+ -[CRMLModel cpuBatchSize]
+ -[CRMLModel gpuBatchSize]
+ -[CRMLModel initRestrictingToCPU:]
+ -[CRMLModel initWithURL:error:]
+ -[CRMLModel initWithURL:restrictToCPU:error:]
+ -[CRMLModel init]
+ -[CRMLModel inputHeight]
+ -[CRMLModel inputWidth]
+ -[CRMLModel modelName]
+ -[CRMLModel modelShape]
+ -[CRMLModel predict:error:]
+ -[CRMLModel setCpuBatchSize:]
+ -[CRMLModel setGpuBatchSize:]
+ -[CRMLModel setModelShape:]
+ -[CRMLModel(Activations) activationsFromImage:]
+ -[CRMLModel(Activations) decodeActivations:]
+ -[CRMLModel(Activations) decodeActivations:blank:ctcAllowGarbage:numResultNeeded:]
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table147
+ GCC_except_table153
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table28
+ GCC_except_table41
+ GCC_except_table53
+ GCC_except_table58
+ GCC_except_table90
+ GCC_except_table94
+ GCC_except_table97
+ _.str
+ _CGRectZero
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_MLDictionaryFeatureProvider
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_MLModelConfiguration
+ _OBJC_CLASS_$_MLMultiArray
+ _OBJC_CLASS_$_NSException
+ _OBJC_IVAR_$_CRCameraReader._enableUnpaddedIDCapture
+ _OBJC_IVAR_$_CRCameraReaderOutputInternal._unpaddedImageValue
+ _OBJC_IVAR_$_CRMLModel._classCount
+ _OBJC_IVAR_$_CRMLModel._codeMap
+ _OBJC_IVAR_$_CRMLModel._cpuBatchSize
+ _OBJC_IVAR_$_CRMLModel._gpuBatchSize
+ _OBJC_IVAR_$_CRMLModel._modelHeight
+ _OBJC_IVAR_$_CRMLModel._modelShape
+ _OBJC_IVAR_$_CRMLModel._modelWidth
+ _OBJC_IVAR_$_CRMLModel.model
+ __OBJC_$_INSTANCE_METHODS_CRMLModel(Activations)
+ __OBJC_$_INSTANCE_VARIABLES_CRMLModel
+ __OBJC_$_PROP_LIST_CRMLModel
+ __OBJC_CLASS_RO_$_CRMLModel
+ __OBJC_METACLASS_RO_$_CRMLModel
+ __ZL13indexGroupingNSt3__16vectorIiNS_9allocatorIiEEEERNS0_IS3_NS1_IS3_EEEEi
+ __ZL6logAddff
+ __ZN6MatrixIfED0Ev
+ __ZN6MatrixIfED1Ev
+ __ZN6MatrixIfEaSEPKf
+ __ZN6MatrixIfEaSERKS0_
+ __ZN6MatrixIfEeqERKS0_
+ __ZN6MatrixIfEpLERKS0_
+ __ZN8CTCLayer23computeForwardVariablesEv
+ __ZN8CTCLayerC2Ev
+ __ZN8CTCLayerD2Ev
+ __ZNK6MatrixIfEmlERKS0_
+ __ZNK6MatrixIfEmlERKf
+ __ZNK6MatrixIfEplERKS0_
+ __ZNKSt3__119__map_value_compareINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12__value_typeIS6_jEENS_4lessIS6_EELb1EEclB8ne200100ERKS6_RKS8_
+ __ZNKSt3__119__map_value_compareINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12__value_typeIS6_jEENS_4lessIS6_EELb1EEclB8ne200100ERKS8_RKS6_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_EclB8ne200100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_EclB8ne200100Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIfiEEEEEELb0EEEvT1_SC_T0_NS_15iterator_traitsISC_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZL33returnIndiciesOfSortedFloatVectorRKNS_6vectorIfNS_9allocatorIfEEEEE3$_0PiLb0EEEvT1_SB_T0_NS_15iterator_traitsISB_E15difference_typeEb
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_6vectorINS1_IfNS_9allocatorIfEEEENS2_IS4_EEEERNS2_IS6_EEE5clearB8ne200100Ev
+ __ZNSt3__114__split_bufferINS_6vectorINS1_IfNS_9allocatorIfEEEENS2_IS4_EEEERNS2_IS6_EEED2Ev
+ __ZNSt3__114__split_bufferINS_6vectorIfNS_9allocatorIfEEEERNS2_IS4_EEE17__destruct_at_endB8ne200100EPS4_
+ __ZNSt3__114__split_bufferINS_6vectorIiNS_9allocatorIiEEEERNS2_IS4_EEE17__destruct_at_endB8ne200100EPS4_
+ __ZNSt3__114__split_bufferINS_6vectorIiNS_9allocatorIiEEEERNS2_IS4_EEED2Ev
+ __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIffEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIfiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_6vectorIiNS1_IiEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP5LayerIfffEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeIjNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIfiEEEEEEEEbT1_SC_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_EEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_EEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERZL33returnIndiciesOfSortedFloatVectorRKNS_6vectorIfNS_9allocatorIfEEEEE3$_0PiEEbT1_SB_T0_
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne200100Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16__sortIRNS_6__lessIiiEEPiEEvT0_S5_T_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__16__treeINS_12__value_typeIiiEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSE_SE_
+ __ZNSt3__16__treeINS_12__value_typeIiiEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIiJRKNS_21piecewise_construct_tENS_5tupleIJOiEEENSE_IJEEEEEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIiiEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIiJRKNS_21piecewise_construct_tENS_5tupleIJRKiEEENSE_IJEEEEEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIiiEENS_19__map_value_compareIiS2_NS_4lessIiEELb1EEENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIjNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareIjS8_NS_4lessIjEELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__16__treeIiNS_4lessIiEENS_9allocatorIiEEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSA_SA_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI6matrixIfENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI6matrixIfENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI6matrixIjENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne200100IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE6resizeEm
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE8__appendEm
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorINS_4pairIffEENS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIffEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIffEENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorINS_4pairIfiEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIfiEENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIP15LayerParametersNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP15LayerParametersNS_9allocatorIS2_EEE9push_backB8ne200100ERKS2_
+ __ZNSt3__16vectorIP5LayerIfffENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP5LayerIfffENS_9allocatorIS3_EEE9push_backB8ne200100EOS3_
+ __ZNSt3__16vectorIP5LayerIfffENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorIP6matrixIfENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB8ne200100EOd
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne200100Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne200100EmRKd
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100EOf
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100EmRKh
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne200100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE18__assign_with_sizeB8ne200100IPiS5_EEvT_T0_l
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100ERKi
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100EmRKi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8ne200100EOj
+ __ZNSt3__17__sort3B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIfiEEEEEELi0EEEbT1_SC_SC_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_Li0EEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_Li0EEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIfiEEEEEELi0EEEvT1_SC_SC_SC_SC_T0_
+ __ZNSt3__17__sort5B8ne200100INS_17_ClassicAlgPolicyERZL33returnIndiciesOfSortedFloatVectorRKNS_6vectorIfNS_9allocatorIfEEEEE3$_0PiLi0EEEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17getlineB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
+ __ZNSt3__19__reverseB8ne200100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPNS_6vectorIfNS_9allocatorIfEEEEEES8_EEvT0_T1_
+ __ZNSt3__1rsB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTI6MatrixIfE
+ __ZTS6MatrixIfE
+ __ZTV6MatrixIfE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZZL7logZerovE8slogZero
+ __ZZL7logZerovE9onceToken
+ __ZdlPvSt11align_val_t
+ __ZnwmSt11align_val_t
+ ____ZL7logZerov_block_invoke
+ ___block_literal_global.328
+ ___block_literal_global.330
+ ___block_literal_global.333
+ ___block_literal_global.417
+ ___block_literal_global.419
+ ___block_literal_global.456
+ ___block_literal_global.458
+ ___block_literal_global.478
+ ___block_literal_global.483
+ ___block_literal_global.488
+ ___block_literal_global.520
+ ___block_literal_global.528
+ ___block_literal_global.530
+ _deviceHasAppleNeuralEngine
+ _expf
+ _memset_pattern16
+ _objc_exception_throw
+ _objc_msgSend$capturedCardHeightForTargetWidth:
+ _objc_msgSend$cpuBatchSize
+ _objc_msgSend$dataPointer
+ _objc_msgSend$defaultConfiguration
+ _objc_msgSend$doesNotRecognizeSelector:
+ _objc_msgSend$enableUnpaddedIDCapture
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:
+ _objc_msgSend$featureValueForName:
+ _objc_msgSend$getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:unpaddedCardImage:
+ _objc_msgSend$gpuBatchSize
+ _objc_msgSend$initWithDictionary:error:
+ _objc_msgSend$initWithShape:dataType:error:
+ _objc_msgSend$initWithURL:error:
+ _objc_msgSend$initWithURL:restrictToCPU:error:
+ _objc_msgSend$inputDescriptionsByName
+ _objc_msgSend$modelDescription
+ _objc_msgSend$modelName
+ _objc_msgSend$modelShape
+ _objc_msgSend$modelWithContentsOfURL:configuration:error:
+ _objc_msgSend$multiArrayConstraint
+ _objc_msgSend$multiArrayValue
+ _objc_msgSend$outputCapturedImageHeight
+ _objc_msgSend$outputCapturedImageWidth
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$perspectiveCorrectedImage:p1:p2:p3:p4:
+ _objc_msgSend$platformImageFromCIImage:
+ _objc_msgSend$predict:error:
+ _objc_msgSend$predictionFromFeatures:error:
+ _objc_msgSend$scaledImage:width:height:
+ _objc_msgSend$setAllowBackgroundGPUCompute:
+ _objc_msgSend$setComputeUnits:
+ _objc_msgSend$setCpuBatchSize:
+ _objc_msgSend$setEnableUnpaddedIDCapture:
+ _objc_msgSend$setGpuBatchSize:
+ _objc_msgSend$setModelShape:
+ _objc_msgSend$setUnpaddedImageValue:
+ _objc_msgSend$shape
+ _objc_msgSend$unpaddedImageValue
+ _objc_release_x10
- -[CRCameraReader getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:]
- -[CRMLCCModel init]
- GCC_except_table109
- GCC_except_table110
- GCC_except_table112
- GCC_except_table115
- GCC_except_table118
- GCC_except_table123
- GCC_except_table131
- GCC_except_table148
- GCC_except_table154
- GCC_except_table161
- GCC_except_table163
- GCC_except_table164
- GCC_except_table168
- GCC_except_table35
- GCC_except_table67
- GCC_except_table68
- GCC_except_table69
- GCC_except_table91
- GCC_except_table95
- GCC_except_table98
- OBJC_IVAR_$_CRMLModel._modelHeight
- OBJC_IVAR_$_CRMLModel._modelWidth
- _CRImageReaderRecognitionMethod
- _CRImageReaderRecognitionMethodSingleChar
- __ZN15LayerParametersC2Ev
- __ZN8CTCLayerC1Ev
- __ZN8CTCLayerD1Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_EclB8ne190102Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_EclB8ne190102Ev
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNKSt3__16vectorI6matrixIfENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIffEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP15LayerParametersNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP5LayerIfffENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP6matrixIfENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__114__split_bufferINS_6vectorIfNS_9allocatorIfEEEERNS2_IS4_EEE17__destruct_at_endB8ne190102EPS4_
- __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIiNS1_IiEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15LayerParametersEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP5LayerIfffEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEjEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeIjNS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_EEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_EEbT1_SA_T0_
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne190102Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEjEENS_19__map_value_compareIS7_S8_NS_4lessIS7_EELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__16__treeINS_12__value_typeIjNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareIjS8_NS_4lessIjEELb1EEENS5_IS8_EEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__16vectorI6matrixIfENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI6matrixIjENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne190102IPS5_S9_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIffEENS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102EmRKd
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne190102IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102Em
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_EEjT1_SA_SA_T0_
- __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_EEjT1_SA_SA_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_EEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_EEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIdjES5_EPS3_EEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERPFbRK8HeapPairIjjES5_EPS3_EEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__17getlineB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
- __ZNSt3__19__reverseB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPNS_6vectorIfNS_9allocatorIfEEEEEES8_EEvT0_T1_
- __ZNSt3__1rsB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.351
- ___block_literal_global.435
- ___block_literal_global.437
- ___block_literal_global.474
- ___block_literal_global.476
- ___block_literal_global.496
- ___block_literal_global.501
- ___block_literal_global.506
- ___block_literal_global.525
- ___block_literal_global.538
- ___block_literal_global.546
- ___block_literal_global.548
- _objc_msgSend$getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:
CStrings:
+ "%@"
+ "@\"MLModel\""
+ "@132@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128"
+ "@136@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128S132"
+ "@148@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128{CGSize=dd}132"
+ "@152@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128{CGSize=dd}132S148"
+ "@20@0:8B16"
+ "@32@0:8@16^@24"
+ "@36@0:8@16B24^@28"
+ "@40@0:8@16d24d32"
+ "@40@0:8^v16S24B28q32"
+ "@44@0:8@16^{__CVBuffer=}24I32^@36"
+ "@72@0:8@16^{__CVBuffer=}24^{__CVBuffer=}32@40@48f56i60^@64"
+ "@88@0:8@16{CGPoint=dd}24{CGPoint=dd}40{CGPoint=dd}56{CGPoint=dd}72"
+ "Activations"
+ "Attempt to recognize image (%zu,%zu) incompatible with model input dimensions (%i,%i)"
+ "CRMLModel"
+ "Codemap size doesn't match model output class"
+ "CoreRecognition: result %@ size %@ is smaller than batch size %li"
+ "Ignoring attempt to set CameraReader output image width to %ld, below minimum width of %d."
+ "Q24@0:8Q16"
+ "T@\"NSArray\",&,V_modelShape"
+ "T@\"UIImage\",&,V_unpaddedImageValue"
+ "TB,V_enableUnpaddedIDCapture"
+ "TQ,R,V_outputCapturedImageHeight"
+ "TQ,V_outputCapturedImageWidth"
+ "Ti,R"
+ "Ti,R,V_classCount"
+ "Tq,V_cpuBatchSize"
+ "Tq,V_gpuBatchSize"
+ "Tr^i,R,V_codeMap"
+ "Using custom cpu batch size of %li"
+ "Using custom gpu batch size of %li"
+ "_classCount"
+ "_codeMap"
+ "_cpuBatchSize"
+ "_enableUnpaddedIDCapture"
+ "_gpuBatchSize"
+ "_modelHeight"
+ "_modelShape"
+ "_modelWidth"
+ "_outputCapturedImageHeight"
+ "_outputCapturedImageWidth"
+ "_unpaddedImageValue"
+ "bundle"
+ "capturedCardHeightForTargetWidth:"
+ "com.apple.CoreRecognition.cpu_batch_size"
+ "com.apple.CoreRecognition.gpu_batch_size"
+ "cpuBatchSize"
+ "dataPointer"
+ "decodeActivations must be overridden in subclass"
+ "decodeActivations:blank:ctcAllowGarbage:numResultNeeded:"
+ "defaultConfiguration"
+ "doesNotRecognizeSelector:"
+ "enableUnpaddedIDCapture"
+ "exceptionWithName:reason:userInfo:"
+ "extractCardImage:fromPixelBuffer:withCardBuffer:withPoints:cameraIntrinsicData:padding:inputOrientation:unpaddedCardImage:"
+ "featureValueForName:"
+ "getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:unpaddedCardImage:"
+ "gpuBatchSize"
+ "initRestrictingToCPU:"
+ "initWithDictionary:error:"
+ "initWithShape:dataType:error:"
+ "initWithURL:error:"
+ "initWithURL:restrictToCPU:error:"
+ "inputDescriptionsByName"
+ "inputHeight"
+ "inputWidth"
+ "model"
+ "modelDescription"
+ "modelName must be overridden in subclass"
+ "modelShape"
+ "modelWithContentsOfURL:configuration:error:"
+ "multiArrayConstraint"
+ "multiArrayValue"
+ "outputCapturedImageHeight"
+ "outputCapturedImageWidth"
+ "pathForResource:ofType:"
+ "perspectiveCorrectedImage:p1:p2:p3:p4:"
+ "platformImageFromCIImage:"
+ "predict:error:"
+ "predictionFromFeatures:error:"
+ "r^i"
+ "scaledImage:width:height:"
+ "setAllowBackgroundGPUCompute:"
+ "setComputeUnits:"
+ "setCpuBatchSize:"
+ "setEnableUnpaddedIDCapture:"
+ "setGpuBatchSize:"
+ "setModelShape:"
+ "setOutputCapturedImageWidth:"
+ "setUnpaddedImageValue:"
+ "shape"
+ "softmax_output"
+ "unpaddedImageValue"
+ "{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}24@0:8@16"
- "@132@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{__compressed_pair<std::vector<std::vector<float>> *, std::allocator<std::vector<std::vector<float>>>>=^v}}104B128"
- "@136@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{__compressed_pair<std::vector<std::vector<float>> *, std::allocator<std::vector<std::vector<float>>>>=^v}}104B128S132"
- "@148@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{__compressed_pair<std::vector<std::vector<float>> *, std::allocator<std::vector<std::vector<float>>>>=^v}}104B128{CGSize=dd}132"
- "@152@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{__compressed_pair<std::vector<std::vector<float>> *, std::allocator<std::vector<std::vector<float>>>>=^v}}104B128{CGSize=dd}132S148"
- "@36@0:8@16^{__CVBuffer=}24I32"
- "Layer"
- "getCorrectedIDImageFromAuxiliaryPoints:fromPixelBuffer:orientation:"

```
