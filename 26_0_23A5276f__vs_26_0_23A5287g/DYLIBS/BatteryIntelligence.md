## BatteryIntelligence

> `/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence`

```diff

-160.0.0.0.0
-  __TEXT.__text: 0x4e44
+167.0.0.0.1
+  __TEXT.__text: 0x5cd8
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__objc_methlist: 0x93c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x61a
-  __TEXT.__oslogstring: 0x3ed
+  __TEXT.__cstring: 0x644
+  __TEXT.__oslogstring: 0x437
   __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x10d7
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__objc_classname: 0x216
+  __TEXT.__objc_methname: 0x1147
   __TEXT.__objc_methtype: 0x360
-  __TEXT.__objc_stubs: 0xd80
+  __TEXT.__objc_stubs: 0xdc0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x1308
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x1628
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x240
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 961542B2-3209-316A-A61E-C26D195FBFC1
-  Functions: 178
-  Symbols:   782
-  CStrings:  392
+  UUID: 55A1EF67-8673-3506-A724-4465BCABD729
+  Functions: 210
+  Symbols:   878
+  CStrings:  405
 
Symbols:
+ +[battery_analysis_ttl_model URLOfModelInThisBundle]
+ +[battery_analysis_ttl_model URLOfModelInThisBundle].cold.1
+ +[battery_analysis_ttl_model loadContentsOfURL:configuration:completionHandler:]
+ +[battery_analysis_ttl_model loadWithConfiguration:completionHandler:]
+ -[battery_analysis_ttl_model .cxx_destruct]
+ -[battery_analysis_ttl_model initWithConfiguration:error:]
+ -[battery_analysis_ttl_model initWithContentsOfURL:configuration:error:]
+ -[battery_analysis_ttl_model initWithContentsOfURL:error:]
+ -[battery_analysis_ttl_model initWithMLModel:]
+ -[battery_analysis_ttl_model init]
+ -[battery_analysis_ttl_model model]
+ -[battery_analysis_ttl_model predictionFromFeatures:completionHandler:]
+ -[battery_analysis_ttl_model predictionFromFeatures:error:]
+ -[battery_analysis_ttl_model predictionFromFeatures:options:completionHandler:]
+ -[battery_analysis_ttl_model predictionFromFeatures:options:error:]
+ -[battery_analysis_ttl_model predictionFromInput_1:error:]
+ -[battery_analysis_ttl_model predictionsFromInputs:options:error:]
+ -[battery_analysis_ttl_modelInput .cxx_destruct]
+ -[battery_analysis_ttl_modelInput featureNames]
+ -[battery_analysis_ttl_modelInput featureValueForName:]
+ -[battery_analysis_ttl_modelInput initWithInput_1:]
+ -[battery_analysis_ttl_modelInput input_1]
+ -[battery_analysis_ttl_modelInput setInput_1:]
+ -[battery_analysis_ttl_modelOutput .cxx_destruct]
+ -[battery_analysis_ttl_modelOutput featureNames]
+ -[battery_analysis_ttl_modelOutput featureValueForName:]
+ -[battery_analysis_ttl_modelOutput initWithTtl_prediction:]
+ -[battery_analysis_ttl_modelOutput setTtl_prediction:]
+ -[battery_analysis_ttl_modelOutput ttl_prediction]
+ _OBJC_CLASS_$_battery_analysis_ttl_model
+ _OBJC_CLASS_$_battery_analysis_ttl_modelInput
+ _OBJC_CLASS_$_battery_analysis_ttl_modelOutput
+ _OBJC_IVAR_$_battery_analysis_ttl_model._model
+ _OBJC_IVAR_$_battery_analysis_ttl_modelInput._input_1
+ _OBJC_IVAR_$_battery_analysis_ttl_modelOutput._ttl_prediction
+ _OBJC_METACLASS_$_battery_analysis_ttl_model
+ _OBJC_METACLASS_$_battery_analysis_ttl_modelInput
+ _OBJC_METACLASS_$_battery_analysis_ttl_modelOutput
+ __OBJC_$_CLASS_METHODS_battery_analysis_ttl_model
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_model
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_modelInput
+ __OBJC_$_INSTANCE_METHODS_battery_analysis_ttl_modelOutput
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_model
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_modelInput
+ __OBJC_$_INSTANCE_VARIABLES_battery_analysis_ttl_modelOutput
+ __OBJC_$_PROP_LIST_battery_analysis_ttl_model
+ __OBJC_$_PROP_LIST_battery_analysis_ttl_modelInput
+ __OBJC_$_PROP_LIST_battery_analysis_ttl_modelOutput
+ __OBJC_CLASS_PROTOCOLS_$_battery_analysis_ttl_modelInput
+ __OBJC_CLASS_PROTOCOLS_$_battery_analysis_ttl_modelOutput
+ __OBJC_CLASS_RO_$_battery_analysis_ttl_model
+ __OBJC_CLASS_RO_$_battery_analysis_ttl_modelInput
+ __OBJC_CLASS_RO_$_battery_analysis_ttl_modelOutput
+ __OBJC_METACLASS_RO_$_battery_analysis_ttl_model
+ __OBJC_METACLASS_RO_$_battery_analysis_ttl_modelInput
+ __OBJC_METACLASS_RO_$_battery_analysis_ttl_modelOutput
+ ___71-[battery_analysis_ttl_model predictionFromFeatures:completionHandler:]_block_invoke
+ ___79-[battery_analysis_ttl_model predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___80+[battery_analysis_ttl_model loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ _objc_msgSend$initWithTtl_prediction:
+ _objc_msgSend$ttl_prediction
CStrings:
+ "Could not load battery_analysis_ttl_model.mlmodelc in the bundle resource"
+ "T@\"MLMultiArray\",&,N,V_ttl_prediction"
+ "_ttl_prediction"
+ "battery_analysis_ttl_model"
+ "battery_analysis_ttl_modelInput"
+ "battery_analysis_ttl_modelOutput"
+ "initWithTtl_prediction:"
+ "setTtl_prediction:"
+ "ttl_prediction"

```
