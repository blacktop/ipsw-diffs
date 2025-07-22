## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-167.0.0.0.1
-  __TEXT.__text: 0x5cd8
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x93c
+174.0.0.0.0
+  __TEXT.__text: 0x401c
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x644
-  __TEXT.__oslogstring: 0x437
-  __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x216
-  __TEXT.__objc_methname: 0x1147
-  __TEXT.__objc_methtype: 0x360
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x30
+  __TEXT.__cstring: 0x595
+  __TEXT.__oslogstring: 0x3e1
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_classname: 0x149
+  __TEXT.__objc_methname: 0xccb
+  __TEXT.__objc_methtype: 0x2cf
+  __TEXT.__objc_stubs: 0xa00
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x1628
+  __AUTH_CONST.__cfstring: 0x3a0
+  __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x240
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x6c
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55A1EF67-8673-3506-A724-4465BCABD729
-  Functions: 210
-  Symbols:   878
-  CStrings:  405
+  UUID: C36B8A5F-1729-367E-971D-FAB7AC087513
+  Functions: 146
+  Symbols:   641
+  CStrings:  327
 
Symbols:
- +[battery_analysis_tt80_model URLOfModelInThisBundle]
- +[battery_analysis_tt80_model URLOfModelInThisBundle].cold.1
- +[battery_analysis_tt80_model loadContentsOfURL:configuration:completionHandler:]
- +[battery_analysis_tt80_model loadWithConfiguration:completionHandler:]
- +[battery_analysis_ttl_model URLOfModelInThisBundle]
- +[battery_analysis_ttl_model URLOfModelInThisBundle].cold.1
- +[battery_analysis_ttl_model loadContentsOfURL:configuration:completionHandler:]
- +[battery_analysis_ttl_model loadWithConfiguration:completionHandler:]
- -[battery_analysis_tt80_model .cxx_destruct]
- -[battery_analysis_tt80_model initWithConfiguration:error:]
- -[battery_analysis_tt80_model initWithContentsOfURL:configuration:error:]
- -[battery_analysis_tt80_model initWithContentsOfURL:error:]
- -[battery_analysis_tt80_model initWithMLModel:]
- -[battery_analysis_tt80_model init]
- -[battery_analysis_tt80_model model]
- -[battery_analysis_tt80_model predictionFromFeatures:completionHandler:]
- -[battery_analysis_tt80_model predictionFromFeatures:error:]
- -[battery_analysis_tt80_model predictionFromFeatures:options:completionHandler:]
- -[battery_analysis_tt80_model predictionFromFeatures:options:error:]
- -[battery_analysis_tt80_model predictionFromInput_1:error:]
- -[battery_analysis_tt80_model predictionsFromInputs:options:error:]
- -[battery_analysis_tt80_modelInput .cxx_destruct]
- -[battery_analysis_tt80_modelInput featureNames]
- -[battery_analysis_tt80_modelInput featureValueForName:]
- -[battery_analysis_tt80_modelInput initWithInput_1:]
- -[battery_analysis_tt80_modelInput input_1]
- -[battery_analysis_tt80_modelInput setInput_1:]
- -[battery_analysis_tt80_modelOutput .cxx_destruct]
- -[battery_analysis_tt80_modelOutput featureNames]
- -[battery_analysis_tt80_modelOutput featureValueForName:]
- -[battery_analysis_tt80_modelOutput initWithTt80_prediction:]
- -[battery_analysis_tt80_modelOutput setTt80_prediction:]
- -[battery_analysis_tt80_modelOutput tt80_prediction]
- -[battery_analysis_ttl_model .cxx_destruct]
- -[battery_analysis_ttl_model initWithConfiguration:error:]
- -[battery_analysis_ttl_model initWithContentsOfURL:configuration:error:]
- -[battery_analysis_ttl_model initWithContentsOfURL:error:]
- -[battery_analysis_ttl_model initWithMLModel:]
- -[battery_analysis_ttl_model init]
- -[battery_analysis_ttl_model model]
- -[battery_analysis_ttl_model predictionFromFeatures:completionHandler:]
- -[battery_analysis_ttl_model predictionFromFeatures:error:]
- -[battery_analysis_ttl_model predictionFromFeatures:options:completionHandler:]
- -[battery_analysis_ttl_model predictionFromFeatures:options:error:]
- -[battery_analysis_ttl_model predictionFromInput_1:error:]
- -[battery_analysis_ttl_model predictionsFromInputs:options:error:]
- -[battery_analysis_ttl_modelInput .cxx_destruct]
- -[battery_analysis_ttl_modelInput featureNames]
- -[battery_analysis_ttl_modelInput featureValueForName:]
- -[battery_analysis_ttl_modelInput initWithInput_1:]
- -[battery_analysis_ttl_modelInput input_1]
- -[battery_analysis_ttl_modelInput setInput_1:]
- -[battery_analysis_ttl_modelOutput .cxx_destruct]
- -[battery_analysis_ttl_modelOutput featureNames]
- -[battery_analysis_ttl_modelOutput featureValueForName:]
- -[battery_analysis_ttl_modelOutput initWithTtl_prediction:]
- -[battery_analysis_ttl_modelOutput setTtl_prediction:]
- -[battery_analysis_ttl_modelOutput ttl_prediction]
- _OBJC_CLASS_$_MLArrayBatchProvider
- _OBJC_CLASS_$_MLFeatureValue
- _OBJC_CLASS_$_MLModel
- _OBJC_CLASS_$_MLPredictionOptions
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_battery_analysis_tt80_model
- _OBJC_CLASS_$_battery_analysis_tt80_modelInput
- _OBJC_CLASS_$_battery_analysis_tt80_modelOutput
- _OBJC_CLASS_$_battery_analysis_ttl_model
- _OBJC_CLASS_$_battery_analysis_ttl_modelInput
- _OBJC_CLASS_$_battery_analysis_ttl_modelOutput
- _OBJC_IVAR_$_battery_analysis_tt80_model._model
- _OBJC_IVAR_$_battery_analysis_tt80_modelInput._input_1
- _OBJC_IVAR_$_battery_analysis_tt80_modelOutput._tt80_prediction
- _OBJC_IVAR_$_battery_analysis_ttl_model._model
- _OBJC_IVAR_$_battery_analysis_ttl_modelInput._input_1
- _OBJC_IVAR_$_battery_analysis_ttl_modelOutput._ttl_prediction
- _OBJC_METACLASS_$_battery_analysis_tt80_model
- _OBJC_METACLASS_$_battery_analysis_tt80_modelInput
- _OBJC_METACLASS_$_battery_analysis_tt80_modelOutput
- _OBJC_METACLASS_$_battery_analysis_ttl_model
- _OBJC_METACLASS_$_battery_analysis_ttl_modelInput
- _OBJC_METACLASS_$_battery_analysis_ttl_modelOutput
- __OBJC_$_CLASS_METHODS_battery_analysis_tt80_model
- __OBJC_$_CLASS_METHODS_battery_analysis_ttl_model
- __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_model
- __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_modelInput
- __OBJC_$_INSTANCE_METHODS_battery_analysis_tt80_modelOutput
- __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_model
- __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_modelInput
- __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_modelOutput
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_model
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_modelInput
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_tt80_modelOutput
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_model
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_modelInput
- __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_modelOutput
- __OBJC_$_PROP_LIST_MLFeatureProvider
- __OBJC_$_PROP_LIST_battery_analysis_tt80_model
- __OBJC_$_PROP_LIST_battery_analysis_tt80_modelInput
- __OBJC_$_PROP_LIST_battery_analysis_tt80_modelOutput
- __OBJC_$_PROP_LIST_battery_analysis_ttl_model
- __OBJC_$_PROP_LIST_battery_analysis_ttl_modelInput
- __OBJC_$_PROP_LIST_battery_analysis_ttl_modelOutput
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MLFeatureProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_MLFeatureProvider
- __OBJC_CLASS_PROTOCOLS_$_battery_analysis_tt80_modelInput
- __OBJC_CLASS_PROTOCOLS_$_battery_analysis_tt80_modelOutput
- __OBJC_CLASS_PROTOCOLS_$_battery_analysis_ttl_modelInput
- __OBJC_CLASS_PROTOCOLS_$_battery_analysis_ttl_modelOutput
- __OBJC_CLASS_RO_$_battery_analysis_tt80_model
- __OBJC_CLASS_RO_$_battery_analysis_tt80_modelInput
- __OBJC_CLASS_RO_$_battery_analysis_tt80_modelOutput
- __OBJC_CLASS_RO_$_battery_analysis_ttl_model
- __OBJC_CLASS_RO_$_battery_analysis_ttl_modelInput
- __OBJC_CLASS_RO_$_battery_analysis_ttl_modelOutput
- __OBJC_LABEL_PROTOCOL_$_MLFeatureProvider
- __OBJC_METACLASS_RO_$_battery_analysis_tt80_model
- __OBJC_METACLASS_RO_$_battery_analysis_tt80_modelInput
- __OBJC_METACLASS_RO_$_battery_analysis_tt80_modelOutput
- __OBJC_METACLASS_RO_$_battery_analysis_ttl_model
- __OBJC_METACLASS_RO_$_battery_analysis_ttl_modelInput
- __OBJC_METACLASS_RO_$_battery_analysis_ttl_modelOutput
- __OBJC_PROTOCOL_$_MLFeatureProvider
- ___71-[battery_analysis_ttl_model predictionFromFeatures:completionHandler:]_block_invoke
- ___72-[battery_analysis_tt80_model predictionFromFeatures:completionHandler:]_block_invoke
- ___79-[battery_analysis_ttl_model predictionFromFeatures:options:completionHandler:]_block_invoke
- ___80+[battery_analysis_ttl_model loadContentsOfURL:configuration:completionHandler:]_block_invoke
- ___80-[battery_analysis_tt80_model predictionFromFeatures:options:completionHandler:]_block_invoke
- ___81+[battery_analysis_tt80_model loadContentsOfURL:configuration:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e29_v24?0"MLModel"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e41_v24?0"<MLFeatureProvider>"8"NSError"16ls32l8
- __os_log_default
- _objc_msgSend$URLOfModelInThisBundle
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$count
- _objc_msgSend$featureValueForName:
- _objc_msgSend$featureValueWithMultiArray:
- _objc_msgSend$featuresAtIndex:
- _objc_msgSend$fileURLWithPath:
- _objc_msgSend$initWithContentsOfURL:configuration:error:
- _objc_msgSend$initWithContentsOfURL:error:
- _objc_msgSend$initWithFeatureProviderArray:
- _objc_msgSend$initWithInput_1:
- _objc_msgSend$initWithMLModel:
- _objc_msgSend$initWithTt80_prediction:
- _objc_msgSend$initWithTtl_prediction:
- _objc_msgSend$input_1
- _objc_msgSend$isEqualToString:
- _objc_msgSend$loadContentsOfURL:configuration:completionHandler:
- _objc_msgSend$model
- _objc_msgSend$modelWithContentsOfURL:configuration:error:
- _objc_msgSend$modelWithContentsOfURL:error:
- _objc_msgSend$multiArrayValue
- _objc_msgSend$pathForResource:ofType:
- _objc_msgSend$predictionFromFeatures:completionHandler:
- _objc_msgSend$predictionFromFeatures:error:
- _objc_msgSend$predictionFromFeatures:options:completionHandler:
- _objc_msgSend$predictionFromFeatures:options:error:
- _objc_msgSend$predictionsFromBatch:options:error:
- _objc_msgSend$setWithArray:
- _objc_msgSend$tt80_prediction
- _objc_msgSend$ttl_prediction
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "Client output for %@ - additional information: %@, output: %@"
+ "Estimate updated for %@ target - output: %@, additional information: %@"
- "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
- "@\"MLModel\""
- "@\"MLMultiArray\""
- "@\"NSSet\"16@0:8"
- "@32@0:8@16^@24"
- "@40@0:8@16@24^@32"
- "Client output:%@"
- "Could not load battery_analysis_tt80_model.mlmodelc in the bundle resource"
- "Could not load battery_analysis_ttl_model.mlmodelc in the bundle resource"
- "Estimate updated for %@ target with client output: %@"
- "MLFeatureProvider"
- "T@\"MLModel\",R,N,V_model"
- "T@\"MLMultiArray\",&,N,V_input_1"
- "T@\"MLMultiArray\",&,N,V_tt80_prediction"
- "T@\"MLMultiArray\",&,N,V_ttl_prediction"
- "T@\"NSSet\",R,N"
- "URLOfModelInThisBundle"
- "_input_1"
- "_model"
- "_tt80_prediction"
- "_ttl_prediction"
- "arrayWithCapacity:"
- "battery_analysis_tt80_model"
- "battery_analysis_tt80_modelInput"
- "battery_analysis_tt80_modelOutput"
- "battery_analysis_ttl_model"
- "battery_analysis_ttl_modelInput"
- "battery_analysis_ttl_modelOutput"
- "count"
- "featureNames"
- "featureValueForName:"
- "featureValueWithMultiArray:"
- "featuresAtIndex:"
- "fileURLWithPath:"
- "initWithConfiguration:error:"
- "initWithContentsOfURL:configuration:error:"
- "initWithContentsOfURL:error:"
- "initWithFeatureProviderArray:"
- "initWithInput_1:"
- "initWithMLModel:"
- "initWithTt80_prediction:"
- "initWithTtl_prediction:"
- "input_1"
- "isEqualToString:"
- "loadContentsOfURL:configuration:completionHandler:"
- "loadWithConfiguration:completionHandler:"
- "mlmodelc"
- "model"
- "modelWithContentsOfURL:configuration:error:"
- "modelWithContentsOfURL:error:"
- "multiArrayValue"
- "pathForResource:ofType:"
- "predictionFromFeatures:completionHandler:"
- "predictionFromFeatures:error:"
- "predictionFromFeatures:options:completionHandler:"
- "predictionFromFeatures:options:error:"
- "predictionFromInput_1:error:"
- "predictionsFromBatch:options:error:"
- "predictionsFromInputs:options:error:"
- "setInput_1:"
- "setTt80_prediction:"
- "setTtl_prediction:"
- "setWithArray:"
- "tt80_prediction"
- "ttl_prediction"
- "v24@?0@\"<MLFeatureProvider>\"8@\"NSError\"16"
- "v24@?0@\"MLModel\"8@\"NSError\"16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"

```
