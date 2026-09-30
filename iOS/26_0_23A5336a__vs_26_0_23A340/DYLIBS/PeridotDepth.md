## PeridotDepth

> `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0x135e20
-  __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x1144
-  __TEXT.__const: 0x18d00
-  __TEXT.__gcc_except_tab: 0x7e5c
-  __TEXT.__cstring: 0x57ad
-  __TEXT.__oslogstring: 0x12ef
-  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__text: 0x137d48
+  __TEXT.__auth_stubs: 0x1870
+  __TEXT.__objc_methlist: 0x133c
+  __TEXT.__const: 0x18d30
+  __TEXT.__gcc_except_tab: 0x7fb8
+  __TEXT.__cstring: 0x590b
+  __TEXT.__oslogstring: 0x133c
+  __TEXT.__unwind_info: 0x1b00
   __TEXT.__eh_frame: 0xc0
-  __TEXT.__objc_classname: 0x1e1
-  __TEXT.__objc_methname: 0x495a
-  __TEXT.__objc_methtype: 0x57e5
-  __TEXT.__objc_stubs: 0x20c0
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__objc_classname: 0x25a
+  __TEXT.__objc_methname: 0x4f6b
+  __TEXT.__objc_methtype: 0x588d
+  __TEXT.__objc_stubs: 0x2540
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda0
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xc40
+  __DATA_CONST.__objc_selrefs: 0xf10
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__auth_got: 0xc48
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0x2a50
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x2df8
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x3c0
+  __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x280
-  __DATA.__data: 0x24df0
-  __DATA.__bss: 0x28a8c4
+  __DATA.__objc_ivar: 0x29c
+  __DATA.__data: 0x24e50
+  __DATA.__bss: 0x28a9c4
   __DATA.__common: 0x2
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 16B27A0D-DE47-348C-82D1-9658E0960CCA
-  Functions: 1454
-  Symbols:   3955
-  CStrings:  2411
+  UUID: 6DE3DAF4-3C7C-31B9-A362-757901CEC8C4
+  Functions: 1494
+  Symbols:   4127
+  CStrings:  2513
 
Symbols:
+ +[main_nyc2d88ffc_44000_V53_V54 URLOfModelInThisBundle]
+ +[main_nyc2d88ffc_44000_V53_V54 loadContentsOfURL:configuration:completionHandler:]
+ +[main_nyc2d88ffc_44000_V53_V54 loadWithConfiguration:completionHandler:]
+ -[main_nyc2d88ffc_44000_V53_V54 .cxx_destruct]
+ -[main_nyc2d88ffc_44000_V53_V54 initWithConfiguration:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 initWithContentsOfURL:configuration:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 initWithContentsOfURL:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 initWithMLModel:]
+ -[main_nyc2d88ffc_44000_V53_V54 init]
+ -[main_nyc2d88ffc_44000_V53_V54 model]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:completionHandler:]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:options:completionHandler:]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:options:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionFromJasper:error:]
+ -[main_nyc2d88ffc_44000_V53_V54 predictionsFromInputs:options:error:]
+ -[main_nyc2d88ffc_44000_V53_V54Input .cxx_destruct]
+ -[main_nyc2d88ffc_44000_V53_V54Input featureNames]
+ -[main_nyc2d88ffc_44000_V53_V54Input featureValueForName:]
+ -[main_nyc2d88ffc_44000_V53_V54Input initWithJasper:]
+ -[main_nyc2d88ffc_44000_V53_V54Input jasper]
+ -[main_nyc2d88ffc_44000_V53_V54Input setJasper:]
+ -[main_nyc2d88ffc_44000_V53_V54Output .cxx_destruct]
+ -[main_nyc2d88ffc_44000_V53_V54Output featureNames]
+ -[main_nyc2d88ffc_44000_V53_V54Output featureValueForName:]
+ -[main_nyc2d88ffc_44000_V53_V54Output initWithOut_argmax_x8:out_prob_class_0:out_prob_class_1:out_prob_class_2:out_spatial_only:]
+ -[main_nyc2d88ffc_44000_V53_V54Output out_argmax_x8]
+ -[main_nyc2d88ffc_44000_V53_V54Output out_prob_class_0]
+ -[main_nyc2d88ffc_44000_V53_V54Output out_prob_class_1]
+ -[main_nyc2d88ffc_44000_V53_V54Output out_prob_class_2]
+ -[main_nyc2d88ffc_44000_V53_V54Output out_spatial_only]
+ -[main_nyc2d88ffc_44000_V53_V54Output setOut_argmax_x8:]
+ -[main_nyc2d88ffc_44000_V53_V54Output setOut_prob_class_0:]
+ -[main_nyc2d88ffc_44000_V53_V54Output setOut_prob_class_1:]
+ -[main_nyc2d88ffc_44000_V53_V54Output setOut_prob_class_2:]
+ -[main_nyc2d88ffc_44000_V53_V54Output setOut_spatial_only:]
+ GCC_except_table1000
+ GCC_except_table1006
+ GCC_except_table1020
+ GCC_except_table1025
+ GCC_except_table1030
+ GCC_except_table1033
+ GCC_except_table1041
+ GCC_except_table1044
+ GCC_except_table1055
+ GCC_except_table1058
+ GCC_except_table106
+ GCC_except_table1061
+ GCC_except_table1064
+ GCC_except_table1068
+ GCC_except_table1072
+ GCC_except_table1078
+ GCC_except_table1086
+ GCC_except_table109
+ GCC_except_table1101
+ GCC_except_table1108
+ GCC_except_table1163
+ GCC_except_table1168
+ GCC_except_table117
+ GCC_except_table1171
+ GCC_except_table1175
+ GCC_except_table122
+ GCC_except_table1222
+ GCC_except_table1228
+ GCC_except_table1229
+ GCC_except_table150
+ GCC_except_table154
+ GCC_except_table161
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table180
+ GCC_except_table190
+ GCC_except_table2
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table219
+ GCC_except_table224
+ GCC_except_table231
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table250
+ GCC_except_table255
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table277
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table317
+ GCC_except_table324
+ GCC_except_table330
+ GCC_except_table338
+ GCC_except_table35
+ GCC_except_table354
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table368
+ GCC_except_table39
+ GCC_except_table391
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table43
+ GCC_except_table442
+ GCC_except_table45
+ GCC_except_table480
+ GCC_except_table506
+ GCC_except_table513
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table533
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table551
+ GCC_except_table556
+ GCC_except_table571
+ GCC_except_table576
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table586
+ GCC_except_table593
+ GCC_except_table607
+ GCC_except_table64
+ GCC_except_table654
+ GCC_except_table665
+ GCC_except_table67
+ GCC_except_table705
+ GCC_except_table708
+ GCC_except_table718
+ GCC_except_table722
+ GCC_except_table73
+ GCC_except_table762
+ GCC_except_table766
+ GCC_except_table774
+ GCC_except_table778
+ GCC_except_table784
+ GCC_except_table786
+ GCC_except_table788
+ GCC_except_table795
+ GCC_except_table806
+ GCC_except_table815
+ GCC_except_table820
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table829
+ GCC_except_table835
+ GCC_except_table837
+ GCC_except_table841
+ GCC_except_table845
+ GCC_except_table849
+ GCC_except_table854
+ GCC_except_table861
+ GCC_except_table865
+ GCC_except_table873
+ GCC_except_table876
+ GCC_except_table888
+ GCC_except_table902
+ GCC_except_table910
+ GCC_except_table912
+ GCC_except_table916
+ GCC_except_table919
+ GCC_except_table93
+ GCC_except_table933
+ GCC_except_table937
+ GCC_except_table944
+ GCC_except_table953
+ GCC_except_table955
+ GCC_except_table958
+ GCC_except_table972
+ GCC_except_table980
+ GCC_except_table992
+ GCC_except_table998
+ _OBJC_CLASS_$_MLArrayBatchProvider
+ _OBJC_CLASS_$_MLFeatureValue
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_MLMultiArray
+ _OBJC_CLASS_$_MLPredictionOptions
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_main_nyc2d88ffc_44000_V53_V54
+ _OBJC_CLASS_$_main_nyc2d88ffc_44000_V53_V54Input
+ _OBJC_CLASS_$_main_nyc2d88ffc_44000_V53_V54Output
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54._model
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Input._jasper
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Output._out_argmax_x8
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Output._out_prob_class_0
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Output._out_prob_class_1
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Output._out_prob_class_2
+ _OBJC_IVAR_$_main_nyc2d88ffc_44000_V53_V54Output._out_spatial_only
+ _OBJC_METACLASS_$_main_nyc2d88ffc_44000_V53_V54
+ _OBJC_METACLASS_$_main_nyc2d88ffc_44000_V53_V54Input
+ _OBJC_METACLASS_$_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_$_CLASS_METHODS_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_$_INSTANCE_METHODS_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_$_INSTANCE_METHODS_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_$_INSTANCE_METHODS_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_$_INSTANCE_VARIABLES_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_$_INSTANCE_VARIABLES_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_$_INSTANCE_VARIABLES_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_$_PROP_LIST_MLFeatureProvider
+ __OBJC_$_PROP_LIST_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_$_PROP_LIST_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_$_PROP_LIST_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MLFeatureProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MLFeatureProvider
+ __OBJC_CLASS_PROTOCOLS_$_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_CLASS_PROTOCOLS_$_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_CLASS_RO_$_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_CLASS_RO_$_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_CLASS_RO_$_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_LABEL_PROTOCOL_$_MLFeatureProvider
+ __OBJC_METACLASS_RO_$_main_nyc2d88ffc_44000_V53_V54
+ __OBJC_METACLASS_RO_$_main_nyc2d88ffc_44000_V53_V54Input
+ __OBJC_METACLASS_RO_$_main_nyc2d88ffc_44000_V53_V54Output
+ __OBJC_PROTOCOL_$_MLFeatureProvider
+ __ZN21InstrumentsTraceGuardD2Ev
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE4R_Vx
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE4cos3
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE4sin3
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE5R_y_3.0
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE5R_y_3.1
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE5R_y_3.2
+ __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE6R_z_90
+ ___74-[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:completionHandler:]_block_invoke
+ ___82-[main_nyc2d88ffc_44000_V53_V54 predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___83+[main_nyc2d88ffc_44000_V53_V54 loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"MLModel"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e41_v24?0"<MLFeatureProvider>"8"NSError"16ls32l8
+ ___block_literal_global.1205
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$URLOfModelInThisBundle
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$dataPointer
+ _objc_msgSend$dataType
+ _objc_msgSend$euclideanDistances
+ _objc_msgSend$featureValueForName:
+ _objc_msgSend$featureValueWithMultiArray:
+ _objc_msgSend$featuresAtIndex:
+ _objc_msgSend$initWithContentsOfURL:configuration:error:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithFeatureProviderArray:
+ _objc_msgSend$initWithJasper:
+ _objc_msgSend$initWithMLModel:
+ _objc_msgSend$initWithOut_argmax_x8:out_prob_class_0:out_prob_class_1:out_prob_class_2:out_spatial_only:
+ _objc_msgSend$initWithShape:dataType:error:
+ _objc_msgSend$jasper
+ _objc_msgSend$loadContentsOfURL:configuration:completionHandler:
+ _objc_msgSend$model
+ _objc_msgSend$modelWithContentsOfURL:configuration:error:
+ _objc_msgSend$modelWithContentsOfURL:error:
+ _objc_msgSend$multiArrayValue
+ _objc_msgSend$out_argmax_x8
+ _objc_msgSend$out_prob_class_0
+ _objc_msgSend$out_prob_class_1
+ _objc_msgSend$out_prob_class_2
+ _objc_msgSend$out_spatial_only
+ _objc_msgSend$pathForResource:ofType:
+ _objc_msgSend$predictionFromFeatures:completionHandler:
+ _objc_msgSend$predictionFromFeatures:error:
+ _objc_msgSend$predictionFromFeatures:options:completionHandler:
+ _objc_msgSend$predictionFromFeatures:options:error:
+ _objc_msgSend$predictionFromJasper:error:
+ _objc_msgSend$predictionsFromBatch:options:error:
+ _objc_msgSend$setWithArray:
+ _objc_retain_x27
- GCC_except_table1004
- GCC_except_table101
- GCC_except_table1019
- GCC_except_table1024
- GCC_except_table1029
- GCC_except_table1032
- GCC_except_table1040
- GCC_except_table1043
- GCC_except_table1054
- GCC_except_table1056
- GCC_except_table1059
- GCC_except_table1063
- GCC_except_table1067
- GCC_except_table1070
- GCC_except_table1077
- GCC_except_table108
- GCC_except_table1083
- GCC_except_table1093
- GCC_except_table11
- GCC_except_table1105
- GCC_except_table116
- GCC_except_table1162
- GCC_except_table1167
- GCC_except_table1170
- GCC_except_table1173
- GCC_except_table118
- GCC_except_table1182
- GCC_except_table1188
- GCC_except_table1189
- GCC_except_table149
- GCC_except_table152
- GCC_except_table159
- GCC_except_table172
- GCC_except_table174
- GCC_except_table179
- GCC_except_table184
- GCC_except_table194
- GCC_except_table207
- GCC_except_table210
- GCC_except_table215
- GCC_except_table218
- GCC_except_table222
- GCC_except_table230
- GCC_except_table237
- GCC_except_table241
- GCC_except_table249
- GCC_except_table252
- GCC_except_table266
- GCC_except_table269
- GCC_except_table275
- GCC_except_table280
- GCC_except_table282
- GCC_except_table290
- GCC_except_table316
- GCC_except_table323
- GCC_except_table327
- GCC_except_table337
- GCC_except_table351
- GCC_except_table356
- GCC_except_table361
- GCC_except_table367
- GCC_except_table38
- GCC_except_table388
- GCC_except_table407
- GCC_except_table410
- GCC_except_table415
- GCC_except_table418
- GCC_except_table44
- GCC_except_table441
- GCC_except_table479
- GCC_except_table505
- GCC_except_table512
- GCC_except_table520
- GCC_except_table524
- GCC_except_table532
- GCC_except_table544
- GCC_except_table546
- GCC_except_table550
- GCC_except_table555
- GCC_except_table570
- GCC_except_table574
- GCC_except_table579
- GCC_except_table581
- GCC_except_table585
- GCC_except_table592
- GCC_except_table606
- GCC_except_table61
- GCC_except_table653
- GCC_except_table663
- GCC_except_table702
- GCC_except_table707
- GCC_except_table715
- GCC_except_table719
- GCC_except_table760
- GCC_except_table765
- GCC_except_table77
- GCC_except_table770
- GCC_except_table777
- GCC_except_table781
- GCC_except_table785
- GCC_except_table787
- GCC_except_table794
- GCC_except_table798
- GCC_except_table812
- GCC_except_table818
- GCC_except_table821
- GCC_except_table826
- GCC_except_table828
- GCC_except_table833
- GCC_except_table836
- GCC_except_table838
- GCC_except_table844
- GCC_except_table846
- GCC_except_table853
- GCC_except_table860
- GCC_except_table863
- GCC_except_table872
- GCC_except_table875
- GCC_except_table884
- GCC_except_table900
- GCC_except_table906
- GCC_except_table911
- GCC_except_table914
- GCC_except_table917
- GCC_except_table92
- GCC_except_table932
- GCC_except_table934
- GCC_except_table943
- GCC_except_table952
- GCC_except_table954
- GCC_except_table956
- GCC_except_table971
- GCC_except_table979
- GCC_except_table989
- GCC_except_table995
- GCC_except_table999
- __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE6R_z_90.0
- __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE6R_z_90.1
- __ZZL20getNominalExtrinsicsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEE6R_z_90.2
- ___block_literal_global.1154
CStrings:
+ "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
+ "@\"MLModel\""
+ "@\"MLMultiArray\""
+ "@\"NSSet\"16@0:8"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "@56@0:8@16@24@32@40@48"
+ "Could not load main_nyc2d88ffc_44000_V53_V54.mlmodelc in the bundle resource"
+ "Error creating MLMultiArray: %@"
+ "Error making prediction: %@"
+ "Error: MLMultiArray data type mismatch. Expected Float32."
+ "MLFeatureProvider"
+ "T@\"MLModel\",R,N,V_model"
+ "T@\"MLMultiArray\",&,N,V_jasper"
+ "T@\"MLMultiArray\",&,N,V_out_argmax_x8"
+ "T@\"MLMultiArray\",&,N,V_out_prob_class_0"
+ "T@\"MLMultiArray\",&,N,V_out_prob_class_1"
+ "T@\"MLMultiArray\",&,N,V_out_prob_class_2"
+ "T@\"MLMultiArray\",&,N,V_out_spatial_only"
+ "T@\"NSSet\",R,N"
+ "URLForResource:withExtension:"
+ "URLOfModelInThisBundle"
+ "_jasper"
+ "_model"
+ "_out_argmax_x8"
+ "_out_prob_class_0"
+ "_out_prob_class_1"
+ "_out_prob_class_2"
+ "_out_spatial_only"
+ "arrayWithObjects:count:"
+ "bundleForClass:"
+ "dataPointer"
+ "dataType"
+ "euclideanDistances"
+ "featureNames"
+ "featureValueForName:"
+ "featureValueWithMultiArray:"
+ "featuresAtIndex:"
+ "initWithConfiguration:error:"
+ "initWithContentsOfURL:configuration:error:"
+ "initWithContentsOfURL:error:"
+ "initWithFeatureProviderArray:"
+ "initWithJasper:"
+ "initWithMLModel:"
+ "initWithOut_argmax_x8:out_prob_class_0:out_prob_class_1:out_prob_class_2:out_spatial_only:"
+ "initWithShape:dataType:error:"
+ "jasper"
+ "loadContentsOfURL:configuration:completionHandler:"
+ "loadWithConfiguration:completionHandler:"
+ "main_nyc2d88ffc_44000-V53-V54"
+ "main_nyc2d88ffc_44000_V53_V54"
+ "main_nyc2d88ffc_44000_V53_V54Input"
+ "main_nyc2d88ffc_44000_V53_V54Output"
+ "mlmodelc"
+ "model"
+ "modelWithContentsOfURL:configuration:error:"
+ "modelWithContentsOfURL:error:"
+ "multiArrayValue"
+ "out_argmax_x8"
+ "out_prob_class_0"
+ "out_prob_class_1"
+ "out_prob_class_2"
+ "out_spatial_only"
+ "pathForResource:ofType:"
+ "predictionFromFeatures:completionHandler:"
+ "predictionFromFeatures:error:"
+ "predictionFromFeatures:options:completionHandler:"
+ "predictionFromFeatures:options:error:"
+ "predictionFromJasper:error:"
+ "predictionsFromBatch:options:error:"
+ "predictionsFromInputs:options:error:"
+ "setJasper:"
+ "setOut_argmax_x8:"
+ "setOut_prob_class_0:"
+ "setOut_prob_class_1:"
+ "setOut_prob_class_2:"
+ "setOut_spatial_only:"
+ "setWithArray:"
+ "v24@?0@\"<MLFeatureProvider>\"8@\"NSError\"16"
+ "v24@?0@\"MLModel\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v40@0:8@16@24@?32"

```
