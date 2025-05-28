## LighthouseCoreMLFeatureStore

> `/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`

```diff

-2.1.6.0.0
-  __TEXT.__text: 0xb9a0
-  __TEXT.__auth_stubs: 0x430
+2.2.1.0.0
+  __TEXT.__text: 0xba88
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0xa2c
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x6ed
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x6fc
   __TEXT.__oslogstring: 0x1eb
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x244
-  __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x2114
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_classname: 0x297
+  __TEXT.__objc_methname: 0x2102
   __TEXT.__objc_methtype: 0x2ef
   __TEXT.__objc_stubs: 0x1820
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1948
+  __DATA_CONST.__objc_const: 0x1928
   __DATA_CONST.__objc_selrefs: 0x740
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__cfstring: 0x7c0

   __AUTH_CONST.__objc_const: 0x798
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_classrefs: 0x120
   __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0xe8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 236
-  Symbols:   1062
+  Functions: 238
+  Symbols:   1066
   CStrings:  537
 
Symbols:
+ -[LCFELShadowEvaluationPrediction init:predictedFeatureSet:outputLabelFeatureName:]
+ -[LCFELShadowEvaluationPrediction probability]
+ GCC_except_table0
+ _OBJC_IVAR_$_LCFELShadowEvaluationPrediction._probability
+ __Block_object_dispose
+ ___124+[LCFCoreMLFeatureProviderUtils toMultiArrayTypeFeatureProvider:srcFeatureNames:srcLabelName:destFeatureName:destLabelName:]_block_invoke.53
+ ___block_descriptor_40_e8_32r_e9_v16?0^v8lr32l8
+ ___block_descriptor_48_e8_32r40r_e13_v24?0r^v8q16lr32l8r40l8
+ _objc_msgSend$getBytesWithHandler:
- -[LCFELShadowEvaluationPrediction init:predictedFeatureSet:outputLabelFeaturName:]
- -[LCFELShadowEvaluationPrediction probablity]
- _OBJC_IVAR_$_LCFELShadowEvaluationPrediction._probablity
- _OBJC_IVAR_$_LCFFeatureValue._valueInString
- ___block_descriptor_40_e9_v16?0^v8l
- _objc_msgSend$mutableBytes
CStrings:
+ "\x16"
+ "T@\"NSNumber\",R,N,V_probability"
+ "T@\"NSString\",R,N"
+ "_probability"
+ "classProbability"
+ "getBytesWithHandler:"
+ "init:predictedFeatureSet:outputLabelFeatureName:"
+ "probability"
+ "v24@?0r^v8q16"
- "\x17"
- "T@\"NSNumber\",R,N,V_probablity"
- "T@\"NSString\",R,N,V_valueInString"
- "_probablity"
- "_valueInString"
- "classProbablity"
- "init:predictedFeatureSet:outputLabelFeaturName:"
- "mutableBytes"
- "probablity"

```
