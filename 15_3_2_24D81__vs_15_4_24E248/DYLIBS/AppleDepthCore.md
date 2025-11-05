## AppleDepthCore

> `/System/Library/PrivateFrameworks/AppleDepthCore.framework/Versions/A/AppleDepthCore`

```diff

-132.0.0.0.0
-  __TEXT.__text: 0x5d380
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0x1e6c
-  __TEXT.__const: 0x21b0
-  __TEXT.__gcc_except_tab: 0x5378
-  __TEXT.__oslogstring: 0x183e
-  __TEXT.__cstring: 0x2f4a
-  __TEXT.__unwind_info: 0x1778
-  __TEXT.__objc_classname: 0x43b
-  __TEXT.__objc_methname: 0x50f8
-  __TEXT.__objc_methtype: 0x4155
-  __TEXT.__objc_stubs: 0x31e0
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xf8
-  __DATA_CONST.__objc_classlist: 0x128
+137.3.0.0.0
+  __TEXT.__text: 0x5fcb0
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__objc_methlist: 0x2214
+  __TEXT.__const: 0x21d0
+  __TEXT.__gcc_except_tab: 0x596c
+  __TEXT.__oslogstring: 0x1bb3
+  __TEXT.__cstring: 0x30fb
+  __TEXT.__unwind_info: 0x1880
+  __TEXT.__objc_classname: 0x47f
+  __TEXT.__objc_methname: 0x5577
+  __TEXT.__objc_methtype: 0x3a2f
+  __TEXT.__objc_stubs: 0x3560
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1178
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x160
-  __AUTH_CONST.__auth_got: 0xa28
-  __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x21c0
-  __AUTH_CONST.__objc_const: 0x3ab0
+  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__const: 0x230
+  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__objc_const: 0x3a48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x264
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x2a8
+  __AUTH.__objc_data: 0xc80
+  __DATA.__objc_ivar: 0x294
+  __DATA.__data: 0x210
+  __DATA.__bss: 0x2c8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B5D8978-4803-3AE8-AFDA-3E831B22A79A
-  Functions: 1001
-  Symbols:   2733
-  CStrings:  1940
+  UUID: 780BF63F-D73A-3B22-9765-4A1632C78FE7
+  Functions: 1013
+  Symbols:   2887
+  CStrings:  2041
 
Symbols:
+ +[ADCoreDeviceConfiguration registerVerbosityConfigurationUpdate]
+ +[ADCoreDeviceConfiguration sharedConfiguration]
+ +[ADEspressoRunner espressoRunnerForPath:forEngine:configurationName:]
+ +[ADImageSupportedSize createWithSize:layout:customStrides:]
+ +[ADStreamSync expectedNumberOfFramesForObject:]
+ -[ADCoreDeviceConfiguration init]
+ -[ADEspressoImageDescriptor conformedByPixelBuffer:forLayout:]
+ -[ADEspressoRunnerV2 ops]
+ -[ADImageDescriptor conformedByPixelBuffer:forLayout:]
+ -[ADImageDescriptor customStridesForLayout:]
+ -[ADImageSupportedSize .cxx_destruct]
+ -[ADImageSupportedSize customStrides]
+ -[ADPreferences .cxx_destruct]
+ -[ADPreferences boolForKey:]
+ -[ADPreferences createPropertyForKey:]
+ -[ADPreferences dealloc]
+ -[ADPreferences doubleForKey:]
+ -[ADPreferences floatForKey:]
+ -[ADPreferences initWithDomain:defaultValues:]
+ -[ADPreferences integerForKey:]
+ -[ADPreferences listForKey:]
+ -[ADPreferences numberForKey:]
+ -[ADPreferences observeValueForKeyPath:ofObject:change:context:]
+ -[ADPreferences registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:]
+ -[ADPreferences stringForKey:]
+ -[ADPreferences updateValue:forKey:]
+ -[ADPreferencesObserver .cxx_destruct]
+ -[ADPreferencesObserver dealloc]
+ -[ADPreferencesObserver initForPreferences:updateHandlerBlock:keys:invokeOnInit:]
+ -[ADPreferencesObserver observeValueForKeyPath:ofObject:change:context:]
+ GCC_except_table1004
+ GCC_except_table1006
+ GCC_except_table101
+ GCC_except_table1018
+ GCC_except_table102
+ GCC_except_table1025
+ GCC_except_table1026
+ GCC_except_table1030
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table1037
+ GCC_except_table1048
+ GCC_except_table1049
+ GCC_except_table1050
+ GCC_except_table1051
+ GCC_except_table1052
+ GCC_except_table1055
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1059
+ GCC_except_table106
+ GCC_except_table1060
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1064
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table202
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table235
+ GCC_except_table240
+ GCC_except_table246
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table265
+ GCC_except_table272
+ GCC_except_table276
+ GCC_except_table289
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table368
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table385
+ GCC_except_table393
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table401
+ GCC_except_table402
+ GCC_except_table403
+ GCC_except_table411
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table430
+ GCC_except_table440
+ GCC_except_table441
+ GCC_except_table442
+ GCC_except_table443
+ GCC_except_table444
+ GCC_except_table458
+ GCC_except_table462
+ GCC_except_table466
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table482
+ GCC_except_table491
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table501
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table504
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table537
+ GCC_except_table538
+ GCC_except_table543
+ GCC_except_table545
+ GCC_except_table556
+ GCC_except_table567
+ GCC_except_table569
+ GCC_except_table571
+ GCC_except_table578
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table584
+ GCC_except_table590
+ GCC_except_table601
+ GCC_except_table609
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table613
+ GCC_except_table614
+ GCC_except_table616
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table625
+ GCC_except_table637
+ GCC_except_table645
+ GCC_except_table646
+ GCC_except_table647
+ GCC_except_table648
+ GCC_except_table649
+ GCC_except_table650
+ GCC_except_table654
+ GCC_except_table655
+ GCC_except_table656
+ GCC_except_table658
+ GCC_except_table676
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table693
+ GCC_except_table697
+ GCC_except_table698
+ GCC_except_table700
+ GCC_except_table701
+ GCC_except_table707
+ GCC_except_table708
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table724
+ GCC_except_table725
+ GCC_except_table727
+ GCC_except_table728
+ GCC_except_table729
+ GCC_except_table730
+ GCC_except_table731
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table734
+ GCC_except_table766
+ GCC_except_table779
+ GCC_except_table782
+ GCC_except_table783
+ GCC_except_table784
+ GCC_except_table787
+ GCC_except_table789
+ GCC_except_table79
+ GCC_except_table795
+ GCC_except_table811
+ GCC_except_table812
+ GCC_except_table820
+ GCC_except_table831
+ GCC_except_table84
+ GCC_except_table845
+ GCC_except_table853
+ GCC_except_table854
+ GCC_except_table864
+ GCC_except_table875
+ GCC_except_table876
+ GCC_except_table877
+ GCC_except_table880
+ GCC_except_table881
+ GCC_except_table884
+ GCC_except_table895
+ GCC_except_table896
+ GCC_except_table897
+ GCC_except_table898
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table909
+ GCC_except_table910
+ GCC_except_table914
+ GCC_except_table918
+ GCC_except_table92
+ GCC_except_table923
+ GCC_except_table940
+ GCC_except_table943
+ GCC_except_table944
+ GCC_except_table945
+ GCC_except_table951
+ GCC_except_table960
+ GCC_except_table962
+ GCC_except_table967
+ GCC_except_table968
+ GCC_except_table969
+ GCC_except_table981
+ GCC_except_table982
+ GCC_except_table989
+ GCC_except_table998
+ OBJC_IVAR_$_ADEspressoRunnerV2._ops
+ OBJC_IVAR_$_ADImageSupportedSize._customStrides
+ OBJC_IVAR_$_ADPreferences._currentDefaults
+ OBJC_IVAR_$_ADPreferences._domain
+ OBJC_IVAR_$_ADPreferences._globalUserDefaults
+ OBJC_IVAR_$_ADPreferences._ignoreValueUpdate
+ OBJC_IVAR_$_ADPreferences._originalDefaults
+ OBJC_IVAR_$_ADPreferences._userDefaults
+ OBJC_IVAR_$_ADPreferencesObserver._keys
+ OBJC_IVAR_$_ADPreferencesObserver._preferences
+ OBJC_IVAR_$_ADPreferencesObserver._updateHandlerBlock
+ OBJC_IVAR_$_ADStreamSync._autoAggregation
+ _CVPixelBufferPoolCreate
+ _OBJC_CLASS_$_ADCoreDeviceConfiguration
+ _OBJC_CLASS_$_ADPreferences
+ _OBJC_CLASS_$_ADPreferencesObserver
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_ADCoreDeviceConfiguration
+ _OBJC_METACLASS_$_ADPreferences
+ _OBJC_METACLASS_$_ADPreferencesObserver
+ _PromotedConst.1946
+ _PromotedConst.1947
+ _PromotedConst.1948
+ _PromotedConst.1949
+ _PromotedConst.1950
+ _PromotedConst.1951
+ _ZL15INSTRUMENTS_ENDjyyyy.1040
+ _ZL15INSTRUMENTS_ENDjyyyy.1228
+ _ZL15INSTRUMENTS_ENDjyyyy.1313
+ _ZL15INSTRUMENTS_ENDjyyyy.1319
+ _ZL15INSTRUMENTS_ENDjyyyy.1558
+ _ZL15INSTRUMENTS_ENDjyyyy.1610
+ _ZL15INSTRUMENTS_ENDjyyyy.1810
+ _ZL15INSTRUMENTS_ENDjyyyy.1932
+ _ZL15INSTRUMENTS_ENDjyyyy.306
+ _ZL15INSTRUMENTS_ENDjyyyy.408
+ _ZL15INSTRUMENTS_ENDjyyyy.483
+ _ZL15INSTRUMENTS_ENDjyyyy.489
+ _ZL15INSTRUMENTS_ENDjyyyy.611
+ _ZL15INSTRUMENTS_ENDjyyyy.617
+ _ZL15INSTRUMENTS_ENDjyyyy.704
+ _ZL15INSTRUMENTS_ENDjyyyy.774
+ _ZL15INSTRUMENTS_ENDjyyyy.82
+ _ZL17INSTRUMENTS_EVENTjyyyy.1041
+ _ZL17INSTRUMENTS_EVENTjyyyy.1229
+ _ZL17INSTRUMENTS_EVENTjyyyy.1314
+ _ZL17INSTRUMENTS_EVENTjyyyy.1320
+ _ZL17INSTRUMENTS_EVENTjyyyy.1559
+ _ZL17INSTRUMENTS_EVENTjyyyy.1611
+ _ZL17INSTRUMENTS_EVENTjyyyy.1811
+ _ZL17INSTRUMENTS_EVENTjyyyy.1933
+ _ZL17INSTRUMENTS_EVENTjyyyy.307
+ _ZL17INSTRUMENTS_EVENTjyyyy.409
+ _ZL17INSTRUMENTS_EVENTjyyyy.484
+ _ZL17INSTRUMENTS_EVENTjyyyy.490
+ _ZL17INSTRUMENTS_EVENTjyyyy.612
+ _ZL17INSTRUMENTS_EVENTjyyyy.618
+ _ZL17INSTRUMENTS_EVENTjyyyy.705
+ _ZL17INSTRUMENTS_EVENTjyyyy.775
+ _ZL17INSTRUMENTS_EVENTjyyyy.83
+ _ZL17INSTRUMENTS_STARTjyyyy.1042
+ _ZL17INSTRUMENTS_STARTjyyyy.1230
+ _ZL17INSTRUMENTS_STARTjyyyy.1315
+ _ZL17INSTRUMENTS_STARTjyyyy.1321
+ _ZL17INSTRUMENTS_STARTjyyyy.1560
+ _ZL17INSTRUMENTS_STARTjyyyy.1612
+ _ZL17INSTRUMENTS_STARTjyyyy.1812
+ _ZL17INSTRUMENTS_STARTjyyyy.1934
+ _ZL17INSTRUMENTS_STARTjyyyy.308
+ _ZL17INSTRUMENTS_STARTjyyyy.410
+ _ZL17INSTRUMENTS_STARTjyyyy.485
+ _ZL17INSTRUMENTS_STARTjyyyy.491
+ _ZL17INSTRUMENTS_STARTjyyyy.613
+ _ZL17INSTRUMENTS_STARTjyyyy.619
+ _ZL17INSTRUMENTS_STARTjyyyy.706
+ _ZL17INSTRUMENTS_STARTjyyyy.776
+ _ZL17INSTRUMENTS_STARTjyyyy.84
+ __OBJC_$_CLASS_METHODS_ADCoreDeviceConfiguration
+ __OBJC_$_CLASS_METHODS_ADEspressoRunner
+ __OBJC_$_CLASS_METHODS_ADStreamSync
+ __OBJC_$_INSTANCE_METHODS_ADCoreDeviceConfiguration
+ __OBJC_$_INSTANCE_METHODS_ADPreferences
+ __OBJC_$_INSTANCE_METHODS_ADPreferencesObserver
+ __OBJC_$_INSTANCE_VARIABLES_ADPreferences
+ __OBJC_$_INSTANCE_VARIABLES_ADPreferencesObserver
+ __OBJC_CLASS_RO_$_ADCoreDeviceConfiguration
+ __OBJC_CLASS_RO_$_ADPreferences
+ __OBJC_CLASS_RO_$_ADPreferencesObserver
+ __OBJC_METACLASS_RO_$_ADCoreDeviceConfiguration
+ __OBJC_METACLASS_RO_$_ADPreferences
+ __OBJC_METACLASS_RO_$_ADPreferencesObserver
+ __ZL11getterDummyP11objc_objectP13objc_selector
+ __ZL11setterDummyP11objc_objectP13objc_selectorS0_
+ __ZN16PixelBufferUtils21createPixelBufferPoolE6CGSizejm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne190102ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
+ __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP7ElementNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102ERKS6_S9_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS6_ISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEE5resetB8ne190102EPSD_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP7ElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPP4NodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI21e5rt_surface_format_tNS_6vectorIjNS1_IjEEEEEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE17espresso_buffer_tEEPvEEEEEclB8ne190102EPSC_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPNS_8multisetIP7ElementNSA_14ElementCompareENS1_ISB_EEEEEEPvEEEEEclB8ne190102EPSI_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne190102Ev
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8ne190102ERKSF_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne190102IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne190102IPKjS6_EEvT_T0_l
+ __ZNSt3__1plB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZ48+[ADCoreDeviceConfiguration sharedConfiguration]E8defaults
+ __ZZ48+[ADCoreDeviceConfiguration sharedConfiguration]E9onceToken
+ __ZZ92-[ADPreferences registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:]E13uniqueNameIdx
+ __ZZN27ADJasperPerformanceOverride11getInstanceEvE4once
+ ___48+[ADCoreDeviceConfiguration sharedConfiguration]_block_invoke
+ ___65+[ADCoreDeviceConfiguration registerVerbosityConfigurationUpdate]_block_invoke
+ ___NSArray0__struct
+ ____ZL43registerJasperPointCloudConfigurationUpdateP27ADJasperPerformanceOverride_block_invoke
+ ____ZN27ADJasperPerformanceOverride11getInstanceEv_block_invoke
+ ___block_descriptor_32_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___kCFBooleanFalse
+ __block_literal_global.1350
+ __block_literal_global.201
+ __block_literal_global.215
+ __block_literal_global.217
+ __block_literal_global.605
+ _class_addMethod
+ _class_addProperty
+ _kADCoreDeviceConfigurationKeyJasperPerformanceEmulatedDevice
+ _kADCoreDeviceConfigurationKeyJasperPerformanceOverridePath
+ _kADCoreDeviceConfigurationKeyVerboseLogs
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferWidthKey
+ _objc_destroyWeak
+ _objc_getAssociatedObject
+ _objc_loadWeakRetained
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$boolValue
+ _objc_msgSend$conformedByPixelBuffer:forLayout:
+ _objc_msgSend$createPropertyForKey:
+ _objc_msgSend$createWithSize:layout:customStrides:
+ _objc_msgSend$customStrides
+ _objc_msgSend$customStridesForLayout:
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$espressoRunnerForPath:forEngine:configurationName:
+ _objc_msgSend$expectedNumberOfFramesForObject:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initForPreferences:updateHandlerBlock:keys:invokeOnInit:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$null
+ _objc_msgSend$registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:
+ _objc_msgSend$registerVerbosityConfigurationUpdate
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$sharedConfiguration
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateValue:forKey:
+ _objc_msgSend$willChangeValueForKey:
+ _objc_retainBlock
+ _objc_setAssociatedObject
+ _objc_storeWeak
- -[ADImageDescriptor .cxx_construct]
- GCC_except_table100
- GCC_except_table1008
- GCC_except_table1009
- GCC_except_table1012
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table1020
- GCC_except_table1022
- GCC_except_table1023
- GCC_except_table1024
- GCC_except_table1027
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table116
- GCC_except_table117
- GCC_except_table118
- GCC_except_table124
- GCC_except_table126
- GCC_except_table142
- GCC_except_table143
- GCC_except_table147
- GCC_except_table148
- GCC_except_table149
- GCC_except_table166
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table178
- GCC_except_table182
- GCC_except_table183
- GCC_except_table184
- GCC_except_table190
- GCC_except_table199
- GCC_except_table203
- GCC_except_table204
- GCC_except_table205
- GCC_except_table217
- GCC_except_table218
- GCC_except_table219
- GCC_except_table223
- GCC_except_table224
- GCC_except_table232
- GCC_except_table237
- GCC_except_table242
- GCC_except_table243
- GCC_except_table247
- GCC_except_table249
- GCC_except_table253
- GCC_except_table255
- GCC_except_table257
- GCC_except_table262
- GCC_except_table269
- GCC_except_table273
- GCC_except_table283
- GCC_except_table295
- GCC_except_table317
- GCC_except_table318
- GCC_except_table319
- GCC_except_table320
- GCC_except_table332
- GCC_except_table353
- GCC_except_table357
- GCC_except_table360
- GCC_except_table361
- GCC_except_table363
- GCC_except_table380
- GCC_except_table381
- GCC_except_table382
- GCC_except_table388
- GCC_except_table390
- GCC_except_table394
- GCC_except_table398
- GCC_except_table406
- GCC_except_table407
- GCC_except_table409
- GCC_except_table410
- GCC_except_table425
- GCC_except_table426
- GCC_except_table428
- GCC_except_table434
- GCC_except_table435
- GCC_except_table437
- GCC_except_table451
- GCC_except_table452
- GCC_except_table453
- GCC_except_table454
- GCC_except_table460
- GCC_except_table477
- GCC_except_table486
- GCC_except_table492
- GCC_except_table495
- GCC_except_table496
- GCC_except_table507
- GCC_except_table508
- GCC_except_table510
- GCC_except_table512
- GCC_except_table522
- GCC_except_table524
- GCC_except_table529
- GCC_except_table530
- GCC_except_table532
- GCC_except_table550
- GCC_except_table553
- GCC_except_table554
- GCC_except_table557
- GCC_except_table562
- GCC_except_table565
- GCC_except_table570
- GCC_except_table587
- GCC_except_table588
- GCC_except_table595
- GCC_except_table596
- GCC_except_table597
- GCC_except_table598
- GCC_except_table599
- GCC_except_table600
- GCC_except_table603
- GCC_except_table604
- GCC_except_table606
- GCC_except_table607
- GCC_except_table622
- GCC_except_table626
- GCC_except_table628
- GCC_except_table630
- GCC_except_table631
- GCC_except_table632
- GCC_except_table633
- GCC_except_table634
- GCC_except_table638
- GCC_except_table639
- GCC_except_table640
- GCC_except_table652
- GCC_except_table661
- GCC_except_table662
- GCC_except_table663
- GCC_except_table664
- GCC_except_table665
- GCC_except_table669
- GCC_except_table685
- GCC_except_table691
- GCC_except_table692
- GCC_except_table738
- GCC_except_table739
- GCC_except_table740
- GCC_except_table741
- GCC_except_table742
- GCC_except_table743
- GCC_except_table744
- GCC_except_table747
- GCC_except_table749
- GCC_except_table755
- GCC_except_table77
- GCC_except_table771
- GCC_except_table772
- GCC_except_table773
- GCC_except_table774
- GCC_except_table775
- GCC_except_table776
- GCC_except_table791
- GCC_except_table797
- GCC_except_table805
- GCC_except_table81
- GCC_except_table817
- GCC_except_table819
- GCC_except_table822
- GCC_except_table823
- GCC_except_table824
- GCC_except_table835
- GCC_except_table836
- GCC_except_table840
- GCC_except_table841
- GCC_except_table842
- GCC_except_table843
- GCC_except_table844
- GCC_except_table860
- GCC_except_table869
- GCC_except_table870
- GCC_except_table871
- GCC_except_table874
- GCC_except_table878
- GCC_except_table887
- GCC_except_table890
- GCC_except_table90
- GCC_except_table904
- GCC_except_table905
- GCC_except_table912
- GCC_except_table915
- GCC_except_table916
- GCC_except_table920
- GCC_except_table928
- GCC_except_table929
- GCC_except_table937
- GCC_except_table938
- GCC_except_table941
- GCC_except_table942
- GCC_except_table949
- GCC_except_table953
- GCC_except_table954
- GCC_except_table958
- GCC_except_table964
- GCC_except_table966
- GCC_except_table971
- GCC_except_table985
- GCC_except_table986
- GCC_except_table988
- GCC_except_table99
- GCC_except_table990
- GCC_except_table997
- _PromotedConst.1795
- _PromotedConst.1796
- _PromotedConst.1797
- _PromotedConst.1798
- _PromotedConst.1799
- _PromotedConst.1800
- _ZL15INSTRUMENTS_ENDjyyyy.1159
- _ZL15INSTRUMENTS_ENDjyyyy.1165
- _ZL15INSTRUMENTS_ENDjyyyy.1409
- _ZL15INSTRUMENTS_ENDjyyyy.1462
- _ZL15INSTRUMENTS_ENDjyyyy.1666
- _ZL15INSTRUMENTS_ENDjyyyy.1781
- _ZL15INSTRUMENTS_ENDjyyyy.303
- _ZL15INSTRUMENTS_ENDjyyyy.410
- _ZL15INSTRUMENTS_ENDjyyyy.485
- _ZL15INSTRUMENTS_ENDjyyyy.491
- _ZL15INSTRUMENTS_ENDjyyyy.578
- _ZL15INSTRUMENTS_ENDjyyyy.661
- _ZL15INSTRUMENTS_ENDjyyyy.731
- _ZL15INSTRUMENTS_ENDjyyyy.76
- _ZL15INSTRUMENTS_ENDjyyyy.993
- _ZL17INSTRUMENTS_EVENTjyyyy.1160
- _ZL17INSTRUMENTS_EVENTjyyyy.1166
- _ZL17INSTRUMENTS_EVENTjyyyy.1410
- _ZL17INSTRUMENTS_EVENTjyyyy.1463
- _ZL17INSTRUMENTS_EVENTjyyyy.1667
- _ZL17INSTRUMENTS_EVENTjyyyy.1782
- _ZL17INSTRUMENTS_EVENTjyyyy.304
- _ZL17INSTRUMENTS_EVENTjyyyy.411
- _ZL17INSTRUMENTS_EVENTjyyyy.486
- _ZL17INSTRUMENTS_EVENTjyyyy.492
- _ZL17INSTRUMENTS_EVENTjyyyy.579
- _ZL17INSTRUMENTS_EVENTjyyyy.662
- _ZL17INSTRUMENTS_EVENTjyyyy.732
- _ZL17INSTRUMENTS_EVENTjyyyy.77
- _ZL17INSTRUMENTS_EVENTjyyyy.994
- _ZL17INSTRUMENTS_STARTjyyyy.1161
- _ZL17INSTRUMENTS_STARTjyyyy.1167
- _ZL17INSTRUMENTS_STARTjyyyy.1411
- _ZL17INSTRUMENTS_STARTjyyyy.1464
- _ZL17INSTRUMENTS_STARTjyyyy.1668
- _ZL17INSTRUMENTS_STARTjyyyy.1783
- _ZL17INSTRUMENTS_STARTjyyyy.305
- _ZL17INSTRUMENTS_STARTjyyyy.412
- _ZL17INSTRUMENTS_STARTjyyyy.487
- _ZL17INSTRUMENTS_STARTjyyyy.493
- _ZL17INSTRUMENTS_STARTjyyyy.580
- _ZL17INSTRUMENTS_STARTjyyyy.663
- _ZL17INSTRUMENTS_STARTjyyyy.733
- _ZL17INSTRUMENTS_STARTjyyyy.78
- _ZL17INSTRUMENTS_STARTjyyyy.995
- __ZGVZN27ADJasperPerformanceOverride11getInstanceEvE9singleton
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__113__string_hashIcNS_9allocatorIcEEEclB8ne180100ERKNS_12basic_stringIcNS_11char_traitsIcEES2_EE
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP7ElementNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100ERKS6_S9_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS6_ISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEE5resetB8ne180100EPSD_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE20PixelBufferSharedPtrEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueEEELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI8ADLayout6CGSizeEENS_22__unordered_map_hasherIS2_S4_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE27__node_insert_multi_performEPNS_11__hash_nodeIS4_PvEEPNS_16__hash_node_baseISJ_EE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI8ADLayout6CGSizeEENS_22__unordered_map_hasherIS2_S4_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE27__node_insert_multi_prepareEmRS4_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeI8ADLayout6CGSizeEENS_22__unordered_map_hasherIS2_S4_NS_4hashIS2_EENS_8equal_toIS2_EELb1EEENS_21__unordered_map_equalIS2_S4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP7ElementEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPP4NodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI21e5rt_surface_format_tNS_6vectorIjNS1_IjEEEEEEPvEEEEEclB8ne180100EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE17espresso_buffer_tEEPvEEEEEclB8ne180100EPSC_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEEPS7_EEED2B8ne180100Ev
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN6docopt5valueENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8ne180100ERKSF_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8ne180100IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorIPKN10appledepth16JasperPointCloudENS_9allocatorIS4_EEEC2Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEE18__assign_with_sizeB8ne180100IPKjS6_EEvT_T0_l
- __ZNSt3__1plB8ne180100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __block_literal_global.1196
- __block_literal_global.209
- __block_literal_global.211
CStrings:
+ "!"
+ "%@: (%@)=>(%@)"
+ "%s:%d - ERROR - failed creating pixelBufferPool with error %d"
+ "-[ADImageDescriptor conformedByPixelBuffer:forLayout:]"
+ "/System/AppleInternal/Library/Frameworks/CMCapture.framework/CMCapture"
+ "@\"<ADEspressoRunnerProtocol>\""
+ "@\"ADPreferences\""
+ "@\"NSMutableDictionary\""
+ "@\"NSUserDefaults\""
+ "@\"id\""
+ "@44@0:8@16@?24@32B40"
+ "@48@0:8{CGSize=dd}16Q32@40"
+ "@?"
+ "@@:"
+ "ADCoreDeviceConfiguration"
+ "ADDescriptors.mm"
+ "ADPreferences"
+ "ADPreferencesObserver"
+ "ADStreamSync: stream was initialized with auto aggregation size, but got a non-standard point cloud (%d points)"
+ "B32@0:8^{__CVBuffer=}16Q24"
+ "D"
+ "PixelBuffer has %zu bytes per row in plane %zu, which is not aligned to 64-bytes"
+ "PixelBuffer has %zu bytes per row, which is not aligned to 64-bytes"
+ "PixelBuffer is not backed by IOSurface, so cannot be used as an Espresso buffer"
+ "PixelBuffer with %zu bytes-per-row for plane %zu does not conform to descriptor with bytes-per-row %lu"
+ "PixelBuffer with %zu planes does not conform to descriptor with %lu custom strides"
+ "PixelBuffer with pixel format '%s' does not conform to descriptor with pixel format '%s'"
+ "PixelBuffer with size %dx%d does not conform to descriptor with size %dx%d"
+ "Q24@0:8@16"
+ "Stream sync auto aggregation count set to %zu"
+ "T"
+ "T@\"NSArray\",R,&,N,V_customStrides"
+ "T@\"NSArray\",R,&,N,V_ops"
+ "^B"
+ "__ADPreferencesObserver_%u"
+ "_autoAggregation"
+ "_currentDefaults"
+ "_customStrides"
+ "_domain"
+ "_globalUserDefaults"
+ "_ignoreValueUpdate"
+ "_keys"
+ "_ops"
+ "_originalDefaults"
+ "_preferences"
+ "_updateHandlerBlock"
+ "_userDefaults"
+ "addObserver:forKeyPath:options:context:"
+ "boolForKey:"
+ "boolValue"
+ "cannot set configuration. %{public}@ is set in both global domain and in %@. please only use one."
+ "com.apple.AppleDepthCore"
+ "conformedByPixelBuffer:forLayout:"
+ "createPixelBufferPool"
+ "createPropertyForKey:"
+ "createWithSize:layout:customStrides:"
+ "customStrides"
+ "customStridesForLayout:"
+ "didChangeValueForKey:"
+ "doubleForKey:"
+ "error getting defaults key"
+ "espressoRunnerForPath:forEngine:configurationName:"
+ "expectedNumberOfFramesForObject:"
+ "f24@0:8@16"
+ "failed setting property for configuration key %{public}@"
+ "floatForKey:"
+ "hasPrefix:"
+ "initForPreferences:updateHandlerBlock:keys:invokeOnInit:"
+ "initWithDomain:defaultValues:"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "jasperPerformanceEmulatedDevice"
+ "jasperPerformanceOverridePath"
+ "listForKey:"
+ "null"
+ "numberForKey:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "ops"
+ "planeCount < sizeof(bpps)/sizeof(bpps[0])"
+ "registerUpdateHandlerForKeys:invokeOnRegistration:scopeObject:handlerBlock:"
+ "registerVerbosityConfigurationUpdate"
+ "removeObjectsInRange:"
+ "removeObserver:forKeyPath:context:"
+ "setObject:forKey:"
+ "sharedConfiguration"
+ "standardUserDefaults"
+ "stringByAppendingString:"
+ "stringByReplacingCharactersInRange:withString:"
+ "stringForKey:"
+ "unsignedLongLongValue"
+ "updateValue:forKey:"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8@16@24"
+ "v44@0:8@16B24@28@?36"
+ "v48@0:8@16@24@32^v40"
+ "v@:@"
+ "verboseLogs"
+ "willChangeValueForKey:"
- "@\"NSObject<ADEspressoRunnerProtocol>\""
- "resetting dummy operations for espressoV2 runner"
- "{unordered_map<ADLayout, CGSize, std::hash<ADLayout>, std::equal_to<ADLayout>, std::allocator<std::pair<const ADLayout, CGSize>>>=\"__table_\"{__hash_table<std::__hash_value_type<ADLayout, CGSize>, std::__unordered_map_hasher<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::hash<ADLayout>, std::equal_to<ADLayout>>, std::__unordered_map_equal<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::equal_to<ADLayout>, std::hash<ADLayout>>, std::allocator<std::__hash_value_type<ADLayout, CGSize>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<ADLayout, CGSize>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::hash<ADLayout>, std::equal_to<ADLayout>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<ADLayout, std::__hash_value_type<ADLayout, CGSize>, std::equal_to<ADLayout>, std::hash<ADLayout>>>=\"__value_\"f}}}"

```
