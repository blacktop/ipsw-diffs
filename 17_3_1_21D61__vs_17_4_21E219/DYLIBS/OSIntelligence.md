## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-126.0.0.0.0
-  __TEXT.__text: 0x7474
+131.0.0.0.0
+  __TEXT.__text: 0x7564
   __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x8fc
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x6ea
   __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__oslogstring: 0x91a
-  __TEXT.__unwind_info: 0x388
-  __TEXT.__objc_classname: 0x23b
-  __TEXT.__objc_methname: 0x1760
+  __TEXT.__oslogstring: 0x932
+  __TEXT.__unwind_info: 0x380
+  __TEXT.__objc_classname: 0x23c
+  __TEXT.__objc_methname: 0x1772
   __TEXT.__objc_methtype: 0x4f8
   __TEXT.__objc_stubs: 0x1000
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x310
+  __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1230
   __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__auth_got: 0x1a8
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__objc_superrefs: 0x48
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x300
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 298
-  Symbols:   1061
-  CStrings:  475
+  Functions: 300
+  Symbols:   1064
+  CStrings:  476
 
Symbols:
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ___27-[_OSBatteryPredictor init]_block_invoke.49
+ ___27-[_OSBatteryPredictor init]_block_invoke.49.cold.1
+ ___28-[_OSChargingPredictor init]_block_invoke.55
+ ___28-[_OSChargingPredictor init]_block_invoke.55.cold.1
+ ___37-[_OSInactivityPredictionClient init]_block_invoke.85
+ ___37-[_OSInactivityPredictionClient init]_block_invoke.85.cold.1
+ ___39-[_OSChargingPredictor fixModelOutput:]_block_invoke.61
+ ___40-[_OSChargingPredictor unfixModelOutput]_block_invoke.63
+ ___46-[_OSInactivityPredictionClient modelMetadata]_block_invoke.97
+ ___49-[_OSBatteryPredictor lowSOCPredictionWithError:]_block_invoke.53
+ ___49-[_OSBatteryPredictor lowSOCPredictionWithError:]_block_invoke.53.cold.1
+ ___49-[_OSInactivityPredictionClient modelDescription]_block_invoke.93
+ ___52-[_OSInactivityPredictionClient recommendedWaitTime]_block_invoke.89
+ ___53-[_OSInactivityPredictionClient deviceUsageDiagnosis]_block_invoke.108
+ ___59-[_OSInactivityPredictionClient hasEnoughInactivityHistory]_block_invoke.101
+ ___59-[_OSInactivityPredictionClient inactivityHistoryDiagnosis]_block_invoke.105
+ ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.59
+ ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.59.cold.1
+ ___block_descriptor_40_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_literal_global.100
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.92
+ ___block_literal_global.96
- ___27-[_OSBatteryPredictor init]_block_invoke.48
- ___27-[_OSBatteryPredictor init]_block_invoke.48.cold.1
- ___28-[_OSChargingPredictor init]_block_invoke.54
- ___28-[_OSChargingPredictor init]_block_invoke.54.cold.1
- ___37-[_OSInactivityPredictionClient init]_block_invoke.84
- ___37-[_OSInactivityPredictionClient init]_block_invoke.84.cold.1
- ___39-[_OSChargingPredictor fixModelOutput:]_block_invoke.60
- ___40-[_OSChargingPredictor unfixModelOutput]_block_invoke.62
- ___46-[_OSInactivityPredictionClient modelMetadata]_block_invoke.96
- ___49-[_OSBatteryPredictor lowSOCPredictionWithError:]_block_invoke.52
- ___49-[_OSBatteryPredictor lowSOCPredictionWithError:]_block_invoke.52.cold.1
- ___49-[_OSInactivityPredictionClient modelDescription]_block_invoke.92
- ___52-[_OSInactivityPredictionClient recommendedWaitTime]_block_invoke.88
- ___53-[_OSInactivityPredictionClient deviceUsageDiagnosis]_block_invoke.107
- ___59-[_OSInactivityPredictionClient hasEnoughInactivityHistory]_block_invoke.100
- ___59-[_OSInactivityPredictionClient inactivityHistoryDiagnosis]_block_invoke.104
- ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.58
- ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.58.cold.1
- ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_literal_global.103
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.157
- ___block_literal_global.91
- ___block_literal_global.95
- ___block_literal_global.99
CStrings:
+ "(%ld) Error in getting long inactivity prediction at date %@ with time since inactive %.2f synchronously: %@"
+ "(%ld) Error in getting long inactivity prediction at date %@ with time since inactive %.2f: %@"
+ "(%ld) Error in getting long inactivity prediction synchronously: %@"
+ "(%ld) Error in getting long inactivity prediction: %@"
+ "T@\"NSString\",?,R,C"
- "Error in getting long inactivity prediction at date %@ with time since inactive %.2f synchronously: %@"
- "Error in getting long inactivity prediction at date %@ with time since inactive %.2f: %@"
- "Error in getting long inactivity prediction synchronously: %@"
- "Error in getting long inactivity prediction: %@"

```
