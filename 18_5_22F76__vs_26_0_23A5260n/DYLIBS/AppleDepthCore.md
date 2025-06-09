## AppleDepthCore

> `/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`

```diff

-137.3.0.0.0
-  __TEXT.__text: 0x5d7b0
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__objc_methlist: 0x2214
-  __TEXT.__const: 0x21d0
-  __TEXT.__gcc_except_tab: 0x58e0
-  __TEXT.__oslogstring: 0x1bb3
-  __TEXT.__cstring: 0x30f7
-  __TEXT.__unwind_info: 0x1868
-  __TEXT.__objc_classname: 0x47f
-  __TEXT.__objc_methname: 0x556f
-  __TEXT.__objc_methtype: 0x3a2f
-  __TEXT.__objc_stubs: 0x3560
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__objc_classlist: 0x140
+148.0.0.0.0
+  __TEXT.__text: 0x60198
+  __TEXT.__auth_stubs: 0x1720
+  __TEXT.__objc_methlist: 0x2384
+  __TEXT.__const: 0x21b0
+  __TEXT.__gcc_except_tab: 0x5e50
+  __TEXT.__oslogstring: 0x21fd
+  __TEXT.__cstring: 0x3580
+  __TEXT.__unwind_info: 0x1938
+  __TEXT.__objc_classname: 0x4c1
+  __TEXT.__objc_methname: 0x5b56
+  __TEXT.__objc_methtype: 0x2d8a
+  __TEXT.__objc_stubs: 0x3b00
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1318
+  __DATA_CONST.__objc_selrefs: 0x14a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0xb60
+  __AUTH_CONST.__auth_got: 0xba0
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0x2280
-  __AUTH_CONST.__objc_const: 0x3a48
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x28a0
+  __AUTH_CONST.__objc_const: 0x3e28
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __DATA.__objc_ivar: 0x294
-  __DATA.__data: 0x210
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x2c4
+  __DATA.__data: 0x2f0
   __DATA.__bss: 0x198
-  __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__objc_data: 0xcd0
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7C1EA45-65C2-36F8-860C-9D4845FF4235
-  Functions: 1011
-  Symbols:   3801
-  CStrings:  2041
+  - /usr/lib/libz.1.dylib
+  UUID: BFE0AAC8-D535-38DB-81CF-E35D75371DEC
+  Functions: 1043
+  Symbols:   3985
+  CStrings:  2241
 
Symbols:
+ +[ADImageDimensions imageDimensionsWithWidth:height:]
+ +[ADModelBuilder modelBuilderForModelPath:destinationPath:buildConfigPath:forANE:]
+ +[UtilsForTests areIdenticalPointCloud0:pointCloud1:accuracy:]
+ -[ADAggregatedPointCloudRefiner .cxx_destruct]
+ -[ADAggregatedPointCloudRefiner clear]
+ -[ADAggregatedPointCloudRefiner filter]
+ -[ADAggregatedPointCloudRefiner init]
+ -[ADAggregatedPointCloudRefiner invalidSpotPixel]
+ -[ADAggregatedPointCloudRefiner isSpotPixelOccluded:prevSpotPixel:]
+ -[ADAggregatedPointCloudRefiner pointCloudByRemovingPeridotShortRangeOccludedPoints:]
+ -[ADAggregatedPointCloudRefiner prepareUsingPointCloud:]
+ -[ADAggregatedPointCloudRefiner setFilter:]
+ -[ADEspressoInferenceDescriptor configurationName]
+ -[ADImageDescriptor dimensions]
+ -[ADImageDimensions height]
+ -[ADImageDimensions isEqual:]
+ -[ADImageDimensions setHeight:]
+ -[ADImageDimensions setWidth:]
+ -[ADImageDimensions width]
+ -[ADModelBuilder .cxx_destruct]
+ -[ADModelBuilder createE5MLBundle]
+ -[ADModelBuilder initWithSourcePath:destinationPath:buildConfigPath:forANE:]
+ -[ADModelBuilder makeRunnable]
+ -[ADModelBuilder requiresCompilation]
+ -[ADModelBuilder runnableModelPath]
+ -[ADModelBuilder supportsCompilation]
+ GCC_except_table1000
+ GCC_except_table1005
+ GCC_except_table1007
+ GCC_except_table1008
+ GCC_except_table1015
+ GCC_except_table1016
+ GCC_except_table1020
+ GCC_except_table1027
+ GCC_except_table1036
+ GCC_except_table1042
+ GCC_except_table1044
+ GCC_except_table1056
+ GCC_except_table1064
+ GCC_except_table1068
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1084
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table1087
+ GCC_except_table1088
+ GCC_except_table1091
+ GCC_except_table1092
+ GCC_except_table1093
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1098
+ GCC_except_table1099
+ GCC_except_table1100
+ GCC_except_table1103
+ GCC_except_table1104
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table199
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table254
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table273
+ GCC_except_table277
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table293
+ GCC_except_table297
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table319
+ GCC_except_table34
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table379
+ GCC_except_table38
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table408
+ GCC_except_table41
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table422
+ GCC_except_table423
+ GCC_except_table424
+ GCC_except_table432
+ GCC_except_table435
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table454
+ GCC_except_table460
+ GCC_except_table463
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table505
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table554
+ GCC_except_table557
+ GCC_except_table559
+ GCC_except_table570
+ GCC_except_table572
+ GCC_except_table577
+ GCC_except_table589
+ GCC_except_table598
+ GCC_except_table603
+ GCC_except_table605
+ GCC_except_table624
+ GCC_except_table644
+ GCC_except_table652
+ GCC_except_table659
+ GCC_except_table669
+ GCC_except_table670
+ GCC_except_table671
+ GCC_except_table675
+ GCC_except_table685
+ GCC_except_table687
+ GCC_except_table688
+ GCC_except_table689
+ GCC_except_table705
+ GCC_except_table706
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table719
+ GCC_except_table735
+ GCC_except_table736
+ GCC_except_table737
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table745
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table750
+ GCC_except_table755
+ GCC_except_table757
+ GCC_except_table759
+ GCC_except_table760
+ GCC_except_table761
+ GCC_except_table762
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table765
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table770
+ GCC_except_table771
+ GCC_except_table803
+ GCC_except_table817
+ GCC_except_table819
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table832
+ GCC_except_table849
+ GCC_except_table850
+ GCC_except_table851
+ GCC_except_table852
+ GCC_except_table869
+ GCC_except_table891
+ GCC_except_table892
+ GCC_except_table893
+ GCC_except_table894
+ GCC_except_table913
+ GCC_except_table915
+ GCC_except_table919
+ GCC_except_table920
+ GCC_except_table921
+ GCC_except_table933
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table936
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table941
+ GCC_except_table947
+ GCC_except_table948
+ GCC_except_table949
+ GCC_except_table961
+ GCC_except_table965
+ GCC_except_table983
+ GCC_except_table990
+ _CGRectIsNull
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_ADAggregatedPointCloudRefiner
+ _OBJC_CLASS_$_ADImageDimensions
+ _OBJC_CLASS_$_ADModelBuilder
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSPipe
+ _OBJC_CLASS_$_NSTask
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_ADAggregatedPointCloudRefiner._filter
+ _OBJC_IVAR_$_ADAggregatedPointCloudRefiner._mainIterationCameraAxisIncreasing
+ _OBJC_IVAR_$_ADAggregatedPointCloudRefiner._mainIterationCameraAxisIsY
+ _OBJC_IVAR_$_ADAggregatedPointCloudRefiner._prepared
+ _OBJC_IVAR_$_ADImageDimensions._height
+ _OBJC_IVAR_$_ADImageDimensions._width
+ _OBJC_IVAR_$_ADModelBuilder._buildConfig
+ _OBJC_IVAR_$_ADModelBuilder._buildConfigPath
+ _OBJC_IVAR_$_ADModelBuilder._compiledModelUID
+ _OBJC_IVAR_$_ADModelBuilder._destinationPath
+ _OBJC_IVAR_$_ADModelBuilder._forANE
+ _OBJC_IVAR_$_ADModelBuilder._srcModelPath
+ _OBJC_METACLASS_$_ADAggregatedPointCloudRefiner
+ _OBJC_METACLASS_$_ADImageDimensions
+ _OBJC_METACLASS_$_ADModelBuilder
+ __OBJC_$_CLASS_METHODS_ADImageDimensions
+ __OBJC_$_CLASS_METHODS_ADModelBuilder
+ __OBJC_$_INSTANCE_METHODS_ADAggregatedPointCloudRefiner
+ __OBJC_$_INSTANCE_METHODS_ADImageDimensions
+ __OBJC_$_INSTANCE_METHODS_ADModelBuilder
+ __OBJC_$_INSTANCE_VARIABLES_ADAggregatedPointCloudRefiner
+ __OBJC_$_INSTANCE_VARIABLES_ADImageDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ADModelBuilder
+ __OBJC_$_PROP_LIST_ADAggregatedPointCloudRefiner
+ __OBJC_$_PROP_LIST_ADImageDimensions
+ __OBJC_$_PROP_LIST_ADModelBuilder
+ __OBJC_CLASS_RO_$_ADAggregatedPointCloudRefiner
+ __OBJC_CLASS_RO_$_ADImageDimensions
+ __OBJC_CLASS_RO_$_ADModelBuilder
+ __OBJC_METACLASS_RO_$_ADAggregatedPointCloudRefiner
+ __OBJC_METACLASS_RO_$_ADImageDimensions
+ __OBJC_METACLASS_RO_$_ADModelBuilder
+ __PromotedConst.2161
+ __PromotedConst.2162
+ __PromotedConst.2163
+ __PromotedConst.2164
+ __PromotedConst.2165
+ __PromotedConst.2166
+ __ZL15INSTRUMENTS_ENDjyyyy.1203
+ __ZL15INSTRUMENTS_ENDjyyyy.1413
+ __ZL15INSTRUMENTS_ENDjyyyy.1499
+ __ZL15INSTRUMENTS_ENDjyyyy.1505
+ __ZL15INSTRUMENTS_ENDjyyyy.160
+ __ZL15INSTRUMENTS_ENDjyyyy.1752
+ __ZL15INSTRUMENTS_ENDjyyyy.1805
+ __ZL15INSTRUMENTS_ENDjyyyy.2021
+ __ZL15INSTRUMENTS_ENDjyyyy.2148
+ __ZL15INSTRUMENTS_ENDjyyyy.308
+ __ZL15INSTRUMENTS_ENDjyyyy.405
+ __ZL15INSTRUMENTS_ENDjyyyy.486
+ __ZL15INSTRUMENTS_ENDjyyyy.627
+ __ZL15INSTRUMENTS_ENDjyyyy.633
+ __ZL15INSTRUMENTS_ENDjyyyy.751
+ __ZL15INSTRUMENTS_ENDjyyyy.757
+ __ZL15INSTRUMENTS_ENDjyyyy.77
+ __ZL15INSTRUMENTS_ENDjyyyy.847
+ __ZL15INSTRUMENTS_ENDjyyyy.937
+ __ZL17INSTRUMENTS_EVENTjyyyy.1204
+ __ZL17INSTRUMENTS_EVENTjyyyy.1414
+ __ZL17INSTRUMENTS_EVENTjyyyy.1500
+ __ZL17INSTRUMENTS_EVENTjyyyy.1506
+ __ZL17INSTRUMENTS_EVENTjyyyy.161
+ __ZL17INSTRUMENTS_EVENTjyyyy.1753
+ __ZL17INSTRUMENTS_EVENTjyyyy.1806
+ __ZL17INSTRUMENTS_EVENTjyyyy.2022
+ __ZL17INSTRUMENTS_EVENTjyyyy.2149
+ __ZL17INSTRUMENTS_EVENTjyyyy.309
+ __ZL17INSTRUMENTS_EVENTjyyyy.406
+ __ZL17INSTRUMENTS_EVENTjyyyy.487
+ __ZL17INSTRUMENTS_EVENTjyyyy.628
+ __ZL17INSTRUMENTS_EVENTjyyyy.634
+ __ZL17INSTRUMENTS_EVENTjyyyy.752
+ __ZL17INSTRUMENTS_EVENTjyyyy.758
+ __ZL17INSTRUMENTS_EVENTjyyyy.78
+ __ZL17INSTRUMENTS_EVENTjyyyy.848
+ __ZL17INSTRUMENTS_EVENTjyyyy.938
+ __ZL17INSTRUMENTS_STARTjyyyy.1205
+ __ZL17INSTRUMENTS_STARTjyyyy.1415
+ __ZL17INSTRUMENTS_STARTjyyyy.1501
+ __ZL17INSTRUMENTS_STARTjyyyy.1507
+ __ZL17INSTRUMENTS_STARTjyyyy.162
+ __ZL17INSTRUMENTS_STARTjyyyy.1754
+ __ZL17INSTRUMENTS_STARTjyyyy.1807
+ __ZL17INSTRUMENTS_STARTjyyyy.2023
+ __ZL17INSTRUMENTS_STARTjyyyy.2150
+ __ZL17INSTRUMENTS_STARTjyyyy.310
+ __ZL17INSTRUMENTS_STARTjyyyy.407
+ __ZL17INSTRUMENTS_STARTjyyyy.488
+ __ZL17INSTRUMENTS_STARTjyyyy.629
+ __ZL17INSTRUMENTS_STARTjyyyy.635
+ __ZL17INSTRUMENTS_STARTjyyyy.753
+ __ZL17INSTRUMENTS_STARTjyyyy.759
+ __ZL17INSTRUMENTS_STARTjyyyy.79
+ __ZL17INSTRUMENTS_STARTjyyyy.849
+ __ZL17INSTRUMENTS_STARTjyyyy.939
+ __ZN16PixelBufferUtils17pixelBufferToDataEP10__CVBuffer
+ __ZN16PixelBufferUtils19pixelBufferFromDataEP6NSDataP10__CVBuffer
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBuffer6CGRect
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBufferj
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBufferj6CGRect
+ __ZN16PixelBufferUtils24isSameDimensionAndFormatEP10__CVBufferS1_
+ __ZN23PixelBufferUtilsSession29createCropScaleConvertSessionE6CGSizejS0_j6CGRectS1_
+ __ZN23PixelBufferUtilsSession35createCropScaleConvertRotateSessionE6CGSizejS0_j6CGRectS1_i
+ __ZN23PixelBufferUtilsSessionC1E6CGSizejS0_j6CGRectS1_i33PixelBufferUtilsSessionReflection
+ __ZN23PixelBufferUtilsSessionC2E6CGSizejS0_j6CGRectS1_i33PixelBufferUtilsSessionReflection
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne200100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__119__map_value_compareINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12__value_typeIS6_N6docopt5valueEEENS_4lessIS6_EELb1EEclB8ne200100ERKSA_RKS6_
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS6_ISC_EEEEED1B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__113random_deviceC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZNSt3__113random_deviceD1Ev
+ __ZNSt3__113random_deviceclEv
+ __ZNSt3__114__split_bufferIPP4NodeNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP7ElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPP4NodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE17espresso_buffer_tEEPvEEEEEclB8ne200100EPSC_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN6docopt5valueEEEPvEEEEEclB8ne200100EPSD_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPNS_8multisetIP7ElementNSA_14ElementCompareENS1_ISB_EEEEEEPvEEEEEclB8ne200100EPSI_
+ __ZNSt3__123mersenne_twister_engineIjLm32ELm624ELm397ELm31ELj2567483615ELm11ELj4294967295ELm7ELj2636928640ELm15ELj4022730752ELm18ELj1812433253EEclEv
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne200100Ev
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8ne200100ERKSF_
+ __ZNSt3__16__treeINS_12__value_typeINS_4pairIhhEEmEENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne200100IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP7ElementNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100EOf
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100ERKf
+ __ZNSt3__1plB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ ___34-[ADModelBuilder createE5MLBundle]_block_invoke
+ ____ZL14crc32ForFolderP8NSString_block_invoke
+ ___block_descriptor_40_ea8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_56_ea8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1536
+ ___block_literal_global.216
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.745
+ _crc32
+ _espresso_get_version_string
+ _kCGColorSpaceITUR_709
+ _logf
+ _objc_msgSend$allObjects
+ _objc_msgSend$allValues
+ _objc_msgSend$appendData:
+ _objc_msgSend$code
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createE5MLBundle
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$date
+ _objc_msgSend$emptyFilter
+ _objc_msgSend$enumerateByteRangesUsingBlock:
+ _objc_msgSend$enumeratorAtPath:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$executableURL
+ _objc_msgSend$fileHandleForReading
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$imageDimensionsWithWidth:height:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithSourcePath:destinationPath:buildConfigPath:forANE:
+ _objc_msgSend$invalidSpotPixel
+ _objc_msgSend$isSpotPixelOccluded:prevSpotPixel:
+ _objc_msgSend$launchAndReturnError:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$path
+ _objc_msgSend$pipe
+ _objc_msgSend$prepareUsingPointCloud:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$readDataToEndOfFileAndReturnError:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$requiresCompilation
+ _objc_msgSend$runnableModelPath
+ _objc_msgSend$setArguments:
+ _objc_msgSend$setExecutableURL:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setStandardOutput:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$supportsCompilation
+ _objc_msgSend$terminationStatus
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$waitUntilExit
+ _peridotSensorMap
+ _rmdir
+ _vImageRotate90_CbCr16F
- -[ADEspressoRunnerV2 buildBindFormatsMap]
- GCC_except_table1004
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1018
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1026
- GCC_except_table1028
- GCC_except_table1035
- GCC_except_table1046
- GCC_except_table1047
- GCC_except_table1050
- GCC_except_table1053
- GCC_except_table1054
- GCC_except_table1058
- GCC_except_table1060
- GCC_except_table1065
- GCC_except_table119
- GCC_except_table125
- GCC_except_table127
- GCC_except_table129
- GCC_except_table145
- GCC_except_table146
- GCC_except_table150
- GCC_except_table151
- GCC_except_table152
- GCC_except_table176
- GCC_except_table177
- GCC_except_table186
- GCC_except_table193
- GCC_except_table202
- GCC_except_table206
- GCC_except_table207
- GCC_except_table209
- GCC_except_table210
- GCC_except_table211
- GCC_except_table213
- GCC_except_table220
- GCC_except_table222
- GCC_except_table235
- GCC_except_table250
- GCC_except_table251
- GCC_except_table252
- GCC_except_table256
- GCC_except_table258
- GCC_except_table260
- GCC_except_table276
- GCC_except_table289
- GCC_except_table298
- GCC_except_table300
- GCC_except_table322
- GCC_except_table323
- GCC_except_table324
- GCC_except_table325
- GCC_except_table326
- GCC_except_table327
- GCC_except_table328
- GCC_except_table329
- GCC_except_table334
- GCC_except_table336
- GCC_except_table337
- GCC_except_table35
- GCC_except_table362
- GCC_except_table365
- GCC_except_table366
- GCC_except_table367
- GCC_except_table368
- GCC_except_table371
- GCC_except_table372
- GCC_except_table385
- GCC_except_table39
- GCC_except_table391
- GCC_except_table395
- GCC_except_table396
- GCC_except_table397
- GCC_except_table399
- GCC_except_table400
- GCC_except_table401
- GCC_except_table402
- GCC_except_table403
- GCC_except_table411
- GCC_except_table415
- GCC_except_table42
- GCC_except_table430
- GCC_except_table431
- GCC_except_table438
- GCC_except_table439
- GCC_except_table440
- GCC_except_table441
- GCC_except_table442
- GCC_except_table443
- GCC_except_table444
- GCC_except_table456
- GCC_except_table458
- GCC_except_table466
- GCC_except_table469
- GCC_except_table470
- GCC_except_table497
- GCC_except_table502
- GCC_except_table504
- GCC_except_table520
- GCC_except_table521
- GCC_except_table523
- GCC_except_table542
- GCC_except_table543
- GCC_except_table545
- GCC_except_table556
- GCC_except_table564
- GCC_except_table567
- GCC_except_table568
- GCC_except_table578
- GCC_except_table582
- GCC_except_table584
- GCC_except_table609
- GCC_except_table611
- GCC_except_table614
- GCC_except_table617
- GCC_except_table620
- GCC_except_table621
- GCC_except_table625
- GCC_except_table637
- GCC_except_table641
- GCC_except_table649
- GCC_except_table653
- GCC_except_table656
- GCC_except_table658
- GCC_except_table666
- GCC_except_table667
- GCC_except_table668
- GCC_except_table676
- GCC_except_table678
- GCC_except_table680
- GCC_except_table693
- GCC_except_table698
- GCC_except_table700
- GCC_except_table701
- GCC_except_table720
- GCC_except_table722
- GCC_except_table723
- GCC_except_table724
- GCC_except_table726
- GCC_except_table727
- GCC_except_table729
- GCC_except_table734
- GCC_except_table778
- GCC_except_table779
- GCC_except_table780
- GCC_except_table781
- GCC_except_table782
- GCC_except_table783
- GCC_except_table784
- GCC_except_table787
- GCC_except_table789
- GCC_except_table795
- GCC_except_table811
- GCC_except_table812
- GCC_except_table813
- GCC_except_table814
- GCC_except_table831
- GCC_except_table837
- GCC_except_table845
- GCC_except_table855
- GCC_except_table857
- GCC_except_table861
- GCC_except_table862
- GCC_except_table863
- GCC_except_table864
- GCC_except_table876
- GCC_except_table877
- GCC_except_table880
- GCC_except_table881
- GCC_except_table882
- GCC_except_table884
- GCC_except_table898
- GCC_except_table903
- GCC_except_table909
- GCC_except_table910
- GCC_except_table911
- GCC_except_table923
- GCC_except_table927
- GCC_except_table930
- GCC_except_table943
- GCC_except_table944
- GCC_except_table945
- GCC_except_table951
- GCC_except_table955
- GCC_except_table962
- GCC_except_table967
- GCC_except_table969
- GCC_except_table970
- GCC_except_table979
- GCC_except_table992
- GCC_except_table995
- GCC_except_table996
- __PromotedConst.1946
- __PromotedConst.1947
- __PromotedConst.1948
- __PromotedConst.1949
- __PromotedConst.1950
- __PromotedConst.1951
- __ZL15INSTRUMENTS_ENDjyyyy.1039
- __ZL15INSTRUMENTS_ENDjyyyy.1227
- __ZL15INSTRUMENTS_ENDjyyyy.1312
- __ZL15INSTRUMENTS_ENDjyyyy.1318
- __ZL15INSTRUMENTS_ENDjyyyy.1557
- __ZL15INSTRUMENTS_ENDjyyyy.1609
- __ZL15INSTRUMENTS_ENDjyyyy.1809
- __ZL15INSTRUMENTS_ENDjyyyy.1932
- __ZL15INSTRUMENTS_ENDjyyyy.306
- __ZL15INSTRUMENTS_ENDjyyyy.408
- __ZL15INSTRUMENTS_ENDjyyyy.483
- __ZL15INSTRUMENTS_ENDjyyyy.489
- __ZL15INSTRUMENTS_ENDjyyyy.611
- __ZL15INSTRUMENTS_ENDjyyyy.617
- __ZL15INSTRUMENTS_ENDjyyyy.704
- __ZL15INSTRUMENTS_ENDjyyyy.774
- __ZL15INSTRUMENTS_ENDjyyyy.82
- __ZL17INSTRUMENTS_EVENTjyyyy.1040
- __ZL17INSTRUMENTS_EVENTjyyyy.1228
- __ZL17INSTRUMENTS_EVENTjyyyy.1313
- __ZL17INSTRUMENTS_EVENTjyyyy.1319
- __ZL17INSTRUMENTS_EVENTjyyyy.1558
- __ZL17INSTRUMENTS_EVENTjyyyy.1610
- __ZL17INSTRUMENTS_EVENTjyyyy.1810
- __ZL17INSTRUMENTS_EVENTjyyyy.1933
- __ZL17INSTRUMENTS_EVENTjyyyy.307
- __ZL17INSTRUMENTS_EVENTjyyyy.409
- __ZL17INSTRUMENTS_EVENTjyyyy.484
- __ZL17INSTRUMENTS_EVENTjyyyy.490
- __ZL17INSTRUMENTS_EVENTjyyyy.612
- __ZL17INSTRUMENTS_EVENTjyyyy.618
- __ZL17INSTRUMENTS_EVENTjyyyy.705
- __ZL17INSTRUMENTS_EVENTjyyyy.775
- __ZL17INSTRUMENTS_EVENTjyyyy.83
- __ZL17INSTRUMENTS_STARTjyyyy.1041
- __ZL17INSTRUMENTS_STARTjyyyy.1229
- __ZL17INSTRUMENTS_STARTjyyyy.1314
- __ZL17INSTRUMENTS_STARTjyyyy.1320
- __ZL17INSTRUMENTS_STARTjyyyy.1559
- __ZL17INSTRUMENTS_STARTjyyyy.1611
- __ZL17INSTRUMENTS_STARTjyyyy.1811
- __ZL17INSTRUMENTS_STARTjyyyy.1934
- __ZL17INSTRUMENTS_STARTjyyyy.308
- __ZL17INSTRUMENTS_STARTjyyyy.410
- __ZL17INSTRUMENTS_STARTjyyyy.485
- __ZL17INSTRUMENTS_STARTjyyyy.491
- __ZL17INSTRUMENTS_STARTjyyyy.613
- __ZL17INSTRUMENTS_STARTjyyyy.619
- __ZL17INSTRUMENTS_STARTjyyyy.706
- __ZL17INSTRUMENTS_STARTjyyyy.776
- __ZL17INSTRUMENTS_STARTjyyyy.84
- __ZN16PixelBufferUtils26wrapAsDifferentPixelFormatEP10__CVBufferjPS1_
- __ZN23PixelBufferUtilsSession29createCropScaleConvertSessionE6CGSizejS0_j6CGRect
- __ZN23PixelBufferUtilsSession35createCropScaleConvertRotateSessionE6CGSizejS0_j6CGRecti
- __ZN23PixelBufferUtilsSessionC1E6CGSizejS0_j6CGRecti33PixelBufferUtilsSessionReflection
- __ZN23PixelBufferUtilsSessionC2E6CGSizejS0_j6CGRecti33PixelBufferUtilsSessionReflection
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP7ElementNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS6_ISC_EEEEE5resetB8ne190102EPSC_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEE5resetB8ne190102EPSD_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI21e5rt_surface_format_tNS_6vectorIjNS_9allocatorIjEEEEEENS_22__unordered_map_hasherIS2_S7_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S7_SC_SA_Lb1EEENS4_IS7_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJOS2_EEENSM_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP7ElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPP4NodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI21e5rt_surface_format_tNS_6vectorIjNS1_IjEEEEEEPvEEEEEclB8ne190102EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE17espresso_buffer_tEEPvEEEEEclB8ne190102EPSC_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPNS_8multisetIP7ElementNSA_14ElementCompareENS1_ISB_EEEEEEPvEEEEEclB8ne190102EPSI_
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne190102Ev
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8ne190102ERKSF_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne190102IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEEC2B8ne190102Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne190102IPKjS6_EEvT_T0_l
- __ZNSt3__1plB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___block_literal_global.1349
- ___block_literal_global.201
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.605
CStrings:
+ "%@=%@"
+ "%s:%d - ERROR - Changing pixel format without copying is not supported for formats with different pixel sizes (source=%zu, new=%zu)"
+ "%s:%d - ERROR - Cropping pixel buffer without copying is not supported for multi-planar CVPixelBufferRefs"
+ "*"
+ "-"
+ "--ane-options"
+ "--ane-options-plist"
+ "--e5-compute-units"
+ "--e5-require-ane-resident=strict"
+ "--mil-entry-points"
+ "-i"
+ "-o"
+ "-p"
+ ".N301"
+ "/%@/model.bundle"
+ "/dev/urandom"
+ "/usr/local/bin/espressoc"
+ "/usr/local/bin/zin_ane_dump"
+ "@44@0:8@16@24@32B40"
+ "ADAggregatedPointCloudRefiner"
+ "ADAggregatedPointCloudRefiner cleared point cloud assumptions"
+ "ADAggregatedPointCloudRefiner failed removing short range points"
+ "ADAggregatedPointCloudRefiner picked spots for assumptions adjustment. topLeft (%u,%u,%lu):(%.2f,%.2f) bottomRight (%u,%u,%lu):(%.2f,%.2f) dist(%.2f,%.2f). cameraAxisY=%d, axisIncreasing=%d"
+ "ADAggregatedPointCloudRefiner: filtered %d spots"
+ "ADImageDimensions"
+ "ADModelBuilder"
+ "ANE options: %@"
+ "B36@0:8@16@24f32"
+ "B48@0:8{CGPoint=dd}16{CGPoint=dd}32"
+ "B48@0:8{map<std::string, docopt::value, std::less<std::string>, std::allocator<std::pair<const std::string, docopt::value>>>={__tree<std::__value_type<std::string, docopt::value>, std::__map_value_compare<std::string, std::__value_type<std::string, docopt::value>, std::less<std::string>>, std::allocator<std::__value_type<std::string, docopt::value>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@40"
+ "EnableContextSwitchEvents"
+ "H14G"
+ "Image descriptor contains several sizes. Please use -[sizeForLayout:] instead."
+ "Inference descriptor contains several configurations. Please use -[configurationNameForLayout:] instead."
+ "KernelRewind"
+ "NeFrequency"
+ "Optimize"
+ "ProfileN301iOS"
+ "PstateDCSLevel"
+ "PstateSOCLevel"
+ "ReductionPerf"
+ "ScanWeightsForCompression"
+ "SpatialSplitMode"
+ "T@\"ADImageDimensions\",R,C,N"
+ "T@\"ADJasperPointCloudFilterParameters\",&,N,V_filter"
+ "T@\"NSString\",R,&,N"
+ "T@\"NSString\",R,N"
+ "TB,R,N"
+ "TQ,N,V_height"
+ "TQ,N,V_width"
+ "\\n\\s*--fspatial-split="
+ "\\n\\s*--optimize="
+ "_buildConfig"
+ "_buildConfigPath"
+ "_compiledModelUID"
+ "_destinationPath"
+ "_filter"
+ "_forANE"
+ "_mainIterationCameraAxisIncreasing"
+ "_mainIterationCameraAxisIsY"
+ "_prepared"
+ "_srcModelPath"
+ "allObjects"
+ "allValues"
+ "ane"
+ "appendData:"
+ "areIdenticalPointCloud0:pointCloud1:accuracy:"
+ "build_config.plist"
+ "bundle"
+ "bundleAsEspressoV2"
+ "code"
+ "compiled model flags verification failed"
+ "compiling model %@ info folder %@. forANE:%d. buildConfigPath:%@"
+ "configurationName"
+ "contentsOfDirectoryAtPath:error:"
+ "crc32_%u_isANE_%d_espresso_%s"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createE5MLBundle"
+ "createPixelBufferNoCopy"
+ "custom_options_net.plist"
+ "dataWithContentsOfURL:"
+ "date"
+ "disabled"
+ "enumerateByteRangesUsingBlock:"
+ "enumeratorAtPath:"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "executableURL"
+ "experimentalModelPlatformOverride"
+ "failed to create folder structure needed for compilation. Error: %@"
+ "failed to run %{public}@ with arguments: %{public}@"
+ "fileHandleForReading"
+ "fileSystemRepresentation"
+ "filter"
+ "getResourceValue:forKey:error:"
+ "hwx"
+ "illegal PerformanceOverride csv line, bank ID or spot ID out of range: %s"
+ "illegal PerformanceOverride csv line, should have at least 4 columns: '%s'"
+ "imageDimensionsWithWidth:height:"
+ "initWithData:encoding:"
+ "initWithSourcePath:destinationPath:buildConfigPath:forANE:"
+ "invalidSpotPixel"
+ "isSpotPixelOccluded:prevSpotPixel:"
+ "launchAndReturnError:"
+ "localizedDescription"
+ "makeRunnable"
+ "mismatch in ANE compilation flag Optimize. Expected {reduction-perf} and got {%{public}@}"
+ "mismatch in ANE compilation flag Optimize. Expected {} and got {%{public}@}"
+ "mismatch in ANE compilation flag SpatialSplitMode between {%{public}@} and {%{public}@}"
+ "missing model build config file at %@. unable to compile"
+ "model %@ can be compiled for e5ml"
+ "model already compiled or being compiled, no need to recompile"
+ "model folder found"
+ "model.bundle"
+ "modelBuilderForModelPath:destinationPath:buildConfigPath:forANE:"
+ "moveItemAtPath:toPath:error:"
+ "net"
+ "no ANE found to compile for"
+ "path"
+ "pipe"
+ "pixelBufferFromData"
+ "pixelBufferToData"
+ "platform is %@ but compiling to generic platform instead"
+ "point clouds cameraPixel missmatch for index %i: (%f,%f) != (%f,%f)"
+ "point clouds length do not match: %d != %d"
+ "point clouds xyz missmatch for index %i: (%f,%f,%f) != (%f,%f,%f)"
+ "pointCloudByRemovingPeridotShortRangeOccludedPoints:"
+ "prepareUsingPointCloud:"
+ "rangeOfString:"
+ "rangeOfString:options:"
+ "readDataToEndOfFileAndReturnError:"
+ "reduction-perf"
+ "removeItemAtPath:error:"
+ "requiresCompilation"
+ "runnableModelPath"
+ "running %@ with arguments: %@"
+ "setArguments:"
+ "setExecutableURL:"
+ "setFilter:"
+ "setHeight:"
+ "setStandardOutput:"
+ "setWidth:"
+ "sleepForTimeInterval:"
+ "spatialSplitMode"
+ "stringByDeletingLastPathComponent"
+ "supportsCompilation"
+ "terminationStatus"
+ "timeIntervalSinceDate:"
+ "timed out waiting for model folder. Consider removing folder %@ and try again."
+ "unable to find ANE compilation flag SpatialSplitMode"
+ "universal"
+ "useReductionPerformance"
+ "v40@?0r^v8{_NSRange=QQ}16^B32"
+ "waitUntilExit"
+ "waiting for model folder to appear (timeout: %.0f seconds)"
+ "{JasperPointCloud=\"m_ownedStorage\"{unique_ptr<unsigned char[], std::default_delete<unsigned char[]>>=\"__ptr_\"*}\"m_header\"^{JasperPointCloudDataHeader}\"m_capacity\"Q}"
+ "{deque<Node *, std::allocator<Node *>>=\"__map_\"{__split_buffer<Node **, std::allocator<Node **>>=\"__first_\"^^^{Node}\"__begin_\"^^^{Node}\"__end_\"^^^{Node}\"__cap_\"^^^{Node}}\"__start_\"Q\"__size_\"Q}"
+ "{map<std::string, std::multiset<Element *, Element::ElementCompare> *, std::less<std::string>, std::allocator<std::pair<const std::string, std::multiset<Element *, Element::ElementCompare> *>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, std::__map_value_compare<std::string, std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{unordered_map<e5rt_surface_format_t, std::vector<unsigned int>, std::hash<e5rt_surface_format_t>, std::equal_to<e5rt_surface_format_t>, std::allocator<std::pair<const e5rt_surface_format_t, std::vector<unsigned int>>>>=\"__table_\"{__hash_table<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::__unordered_map_hasher<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::hash<e5rt_surface_format_t>, std::equal_to<e5rt_surface_format_t>>, std::__unordered_map_equal<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::equal_to<e5rt_surface_format_t>, std::hash<e5rt_surface_format_t>>, std::allocator<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<std::string, PixelBufferSharedPtr, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, PixelBufferSharedPtr>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, PixelBufferSharedPtr>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<float, std::allocator<float>>=^f^f^f}24@0:8@16"
- "B48@0:8{map<std::string, docopt::value, std::less<std::string>, std::allocator<std::pair<const std::string, docopt::value>>>={__tree<std::__value_type<std::string, docopt::value>, std::__map_value_compare<std::string, std::__value_type<std::string, docopt::value>, std::less<std::string>>, std::allocator<std::__value_type<std::string, docopt::value>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, docopt::value>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, docopt::value>, std::less<std::string>>>=Q}}}16@40"
- "buildBindFormatsMap"
- "illegal PerformanceOverride csv line, should be 4 columns: '%s'"
- "{JasperPointCloud=\"m_ownedStorage\"{unique_ptr<unsigned char[], std::default_delete<unsigned char[]>>=\"__ptr_\"{__compressed_pair<unsigned char *, std::default_delete<unsigned char[]>>=\"__value_\"*}}\"m_header\"^{JasperPointCloudDataHeader}\"m_capacity\"Q}"
- "{deque<Node *, std::allocator<Node *>>=\"__map_\"{__split_buffer<Node **, std::allocator<Node **>>=\"__first_\"^^^{Node}\"__begin_\"^^^{Node}\"__end_\"^^^{Node}\"__end_cap_\"{__compressed_pair<Node ***, std::allocator<Node **>>=\"__value_\"^^^{Node}}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<Node *>>=\"__value_\"Q}}"
- "{map<std::string, std::multiset<Element *, Element::ElementCompare> *, std::less<std::string>, std::allocator<std::pair<const std::string, std::multiset<Element *, Element::ElementCompare> *>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, std::__map_value_compare<std::string, std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::multiset<Element *, Element::ElementCompare> *>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{unordered_map<e5rt_surface_format_t, std::vector<unsigned int>, std::hash<e5rt_surface_format_t>, std::equal_to<e5rt_surface_format_t>, std::allocator<std::pair<const e5rt_surface_format_t, std::vector<unsigned int>>>>=\"__table_\"{__hash_table<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::__unordered_map_hasher<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::hash<e5rt_surface_format_t>, std::equal_to<e5rt_surface_format_t>>, std::__unordered_map_equal<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::equal_to<e5rt_surface_format_t>, std::hash<e5rt_surface_format_t>>, std::allocator<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::hash<e5rt_surface_format_t>, std::equal_to<e5rt_surface_format_t>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<e5rt_surface_format_t, std::__hash_value_type<e5rt_surface_format_t, std::vector<unsigned int>>, std::equal_to<e5rt_surface_format_t>, std::hash<e5rt_surface_format_t>>>=\"__value_\"f}}}"
- "{unordered_map<std::string, PixelBufferSharedPtr, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, PixelBufferSharedPtr>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, PixelBufferSharedPtr>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, PixelBufferSharedPtr>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, PixelBufferSharedPtr>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}"
- "{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}24@0:8@16"

```
