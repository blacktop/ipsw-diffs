## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-198.0.0.0.1
-  __TEXT.__text: 0x14bf4
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x1d70
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x12e2
-  __TEXT.__gcc_except_tab: 0x5cc
-  __TEXT.__oslogstring: 0x1585
-  __TEXT.__unwind_info: 0x800
-  __TEXT.__objc_classname: 0x41d
-  __TEXT.__objc_methname: 0x330c
-  __TEXT.__objc_methtype: 0xa8a
-  __TEXT.__objc_stubs: 0x2500
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x760
+206.0.0.0.0
+  __TEXT.__text: 0x16034
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x1e68
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x13b4
+  __TEXT.__gcc_except_tab: 0x5ec
+  __TEXT.__oslogstring: 0x175d
+  __TEXT.__unwind_info: 0x848
+  __TEXT.__objc_classname: 0x41e
+  __TEXT.__objc_methname: 0x3673
+  __TEXT.__objc_methtype: 0xaaa
+  __TEXT.__objc_stubs: 0x2760
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde8
+  __DATA_CONST.__objc_selrefs: 0xeb8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x2b20
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__objc_const: 0x2be0
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_ivar: 0x188
   __DATA.__data: 0x540
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A41601C8-67F0-3C78-8F73-1AB7D3D32C02
-  Functions: 763
-  Symbols:   2568
-  CStrings:  1137
+  UUID: 4937A479-4DA1-31AE-9B23-61CDFCD4551D
+  Functions: 795
+  Symbols:   2668
+  CStrings:  1205
 
Symbols:
+ +[OSIUtilities isWeekend:]
+ -[_OSBatteryDrainPredictor didLastChargingSessionFinish]
+ -[_OSDayDrainResult batteryDifference]
+ -[_OSDayDrainResult setBatteryDifference:]
+ -[_OSIBLMAnalyticsHandler modelStringForModel:]
+ -[_OSIBLMAnalyticsHandler reportDrainResult:forModel:]
+ -[_OSIBLMAnalyticsHandler reportNewMitigation:]
+ -[_OSIBLManager dateFormatter]
+ -[_OSIBLManager dateFormatter].cold.1
+ -[_OSIBLManager drainResultWithModel:withError:]
+ -[_OSIBLManager drainResultWithModel:withError:].cold.1
+ -[_OSIBLManager handleCallback:]
+ -[_OSIBLManager hasVariationForMedianLevels:]
+ -[_OSIBLManager hasVariationForMedianLevels:].cold.1
+ -[_OSIBLManager isHighDrainOverAggregatedMedianWithError:]
+ -[_OSIBLManager isHighDrainOverAggregatedMedianWithError:].cold.1
+ -[_OSIBLManager isHighDrainOverAggregatedMedianWithError:].cold.2
+ -[_OSIBLManager lastPredictionDate]
+ -[_OSIBLManager lastPrediction]
+ -[_OSIBLManager setLastPrediction:]
+ -[_OSIBLManager setLastPredictionDate:]
+ -[_OSIBLManager setTrialClientOSI:]
+ -[_OSIBLManager setTrialClientPXP:]
+ -[_OSIBLManager setTrialPerformanceMitigationOption:]
+ -[_OSIBLManager shadowEvaluateForModels:]
+ -[_OSIBLManager shadowEvaluateForModels:].cold.1
+ -[_OSIBLManager trialClientOSI]
+ -[_OSIBLManager trialClientPXP]
+ -[_OSIBLManager trialPerformanceMitigationOption]
+ -[_OSIBLManager updateTrialOSIParameters]
+ -[_OSIBLManager updateTrialPXPParameters]
+ -[_OSICLPCInterface optionFromValue:]
+ -[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSError
+ _OBJC_IVAR_$__OSDayDrainResult._batteryDifference
+ _OBJC_IVAR_$__OSIBLManager._lastPrediction
+ _OBJC_IVAR_$__OSIBLManager._lastPredictionDate
+ _OBJC_IVAR_$__OSIBLManager._trialClientOSI
+ _OBJC_IVAR_$__OSIBLManager._trialClientPXP
+ _OBJC_IVAR_$__OSIBLManager._trialPerformanceMitigationOption
+ ___21-[_OSIBLManager init]_block_invoke.71
+ ___21-[_OSIBLManager init]_block_invoke_2.74
+ ___21-[_OSIBLManager init]_block_invoke_3
+ ___30-[_OSIBLManager dateFormatter]_block_invoke
+ ___32-[_OSIBLManager handleCallback:]_block_invoke
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.80
+ ___41-[_OSIBLManager updateTrialPXPParameters]_block_invoke
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.92
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.96
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.97
+ ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke
+ ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke.cold.1
+ ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke.cold.2
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.101
+ ___block_literal_global.109
+ __xpc_event_key_name
+ _kMedianBatteryModelDomain
+ _objc_autorelease
+ _objc_msgSend$batteryDifference
+ _objc_msgSend$batteryRawExternalConnectedKey
+ _objc_msgSend$didLastChargingSessionFinish
+ _objc_msgSend$drainResultWithModel:withError:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$hasVariationForMedianLevels:
+ _objc_msgSend$isDateInWeekend:
+ _objc_msgSend$isHighDrainOverAggregatedMedianWithError:
+ _objc_msgSend$longValue
+ _objc_msgSend$modelStringForModel:
+ _objc_msgSend$objectForContextualKeyPath:
+ _objc_msgSend$optionFromValue:
+ _objc_msgSend$reportDrainResult:forModel:
+ _objc_msgSend$reportNewMitigation:
+ _objc_msgSend$setBatteryDifference:
+ _objc_msgSend$setIsHighDrain:
+ _objc_msgSend$shadowEvaluateForModels:
+ _objc_msgSend$updatePerformanceControlWithMitigation:withOptionValue:
+ _objc_msgSend$updateTrialOSIParameters
+ _objc_msgSend$updateTrialPXPParameters
+ _objc_msgSend$valueForKey:
+ _objc_retain_x26
+ _strcmp
+ _xpc_dictionary_get_string
- -[_OSIBLManager lastEvaluateDate]
- -[_OSIBLManager setLastEvaluateDate:]
- -[_OSIBLManager setTrialClient:]
- -[_OSIBLManager trialClient]
- -[_OSIBLManager updateTrialParameters]
- -[_OSICLPCInterface updatePerformanceControlWithMitigation:]
- _OBJC_IVAR_$__OSIBLManager._lastEvaluateDate
- _OBJC_IVAR_$__OSIBLManager._trialClient
- ___21-[_OSIBLManager init]_block_invoke.53
- ___21-[_OSIBLManager init]_block_invoke_2.56
- ___38-[_OSIBLManager updateTrialParameters]_block_invoke
- ___38-[_OSIBLManager updateTrialParameters]_block_invoke.62
- ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.89
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.93
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.94
- ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke
- ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.1
- ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.2
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.106
- _objc_msgSend$updatePerformanceControlWithMitigation:
- _objc_msgSend$updateTrialParameters
CStrings:
+ "@\"_OSDayDrainResult\""
+ "CLPC option overide set via Trial. Value %ld"
+ "CLPC_IBLMOption"
+ "COREOS_POWER_EXPERIENCE_POWER_TUNING"
+ "Decision"
+ "Device currently plugged in. Skipping shadow evaluation for drain prediction"
+ "IBLMPredictionAlgorithmOutput"
+ "LPM on. Skipping shadow evaluation for drain prediction"
+ "MLP12N12"
+ "Not enough variation in the values. Min %@, Max %@"
+ "Q24@0:8q16"
+ "Received notification: %s"
+ "Returning because of error %@"
+ "Shadow evaluating for Drain prediction"
+ "Shadow evaluating for Drain prediction failed. Error %@"
+ "StatMedian"
+ "StatMedian Reference %@, Current %@"
+ "T@\"NSDate\",&,N,V_lastPredictionDate"
+ "T@\"TRIClient\",&,N,V_trialClientOSI"
+ "T@\"TRIClient\",&,N,V_trialClientPXP"
+ "T@\"_OSDayDrainResult\",&,N,V_lastPrediction"
+ "Td,N,V_batteryDifference"
+ "Tq,N,V_trialPerformanceMitigationOption"
+ "Trial: %@:%@:%ld"
+ "Unsupported option"
+ "Using StatMedian %@"
+ "Value"
+ "_batteryDifference"
+ "_lastPrediction"
+ "_lastPredictionDate"
+ "_trialClientOSI"
+ "_trialClientPXP"
+ "_trialPerformanceMitigationOption"
+ "batteryDifference"
+ "batteryRawExternalConnectedKey"
+ "com.apple.osintelligence.medianBatteryLevelsModel"
+ "didLastChargingSessionFinish"
+ "drainResultWithModel:withError:"
+ "errorWithDomain:code:userInfo:"
+ "handleCallback:"
+ "hasVariationForMedianLevels:"
+ "isDateInWeekend:"
+ "isHighDrainOverAggregatedMedianWithError:"
+ "isWeekend:"
+ "kLastIBLMPredictionFetchDate"
+ "lastPrediction"
+ "lastPredictionDate"
+ "longValue"
+ "medianLevels"
+ "modelStringForModel:"
+ "objectForContextualKeyPath:"
+ "optionFromValue:"
+ "reportDrainResult:forModel:"
+ "reportNewMitigation:"
+ "setBatteryDifference:"
+ "setLastPrediction:"
+ "setLastPredictionDate:"
+ "setTrialClientOSI:"
+ "setTrialClientPXP:"
+ "setTrialPerformanceMitigationOption:"
+ "shadowEvaluateForModels:"
+ "trialClientOSI"
+ "trialClientPXP"
+ "trialPerformanceMitigationOption"
+ "updatePerformanceControlWithMitigation:withOptionValue:"
+ "updateTrialOSIParameters"
+ "updateTrialPXPParameters"
+ "valueForKey:"
- "T@\"NSDate\",&,N,V_lastEvaluateDate"
- "T@\"TRIClient\",&,N,V_trialClient"
- "_lastEvaluateDate"
- "_trialClient"
- "lastEvaluateDate"
- "setLastEvaluateDate:"
- "setTrialClient:"
- "trialClient"
- "updatePerformanceControlWithMitigation:"
- "updateTrialParameters"

```
