## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-234.100.11.0.0
-  __TEXT.__text: 0x1a2ec
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x2150
-  __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x18bb
-  __TEXT.__oslogstring: 0x1d04
-  __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x4218
-  __TEXT.__objc_methtype: 0xbf8
-  __TEXT.__objc_stubs: 0x2ec0
+234.100.14.0.0
+  __TEXT.__text: 0x1ae50
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x21c0
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x1979
+  __TEXT.__oslogstring: 0x1e02
+  __TEXT.__gcc_except_tab: 0x65c
+  __TEXT.__unwind_info: 0xa38
+  __TEXT.__objc_classname: 0x456
+  __TEXT.__objc_methname: 0x43e0
+  __TEXT.__objc_methtype: 0xcab
+  __TEXT.__objc_stubs: 0x2f40
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1148
+  __DATA_CONST.__objc_selrefs: 0x1188
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x2f50
+  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x14e0
+  __AUTH_CONST.__objc_const: 0x2fe8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55F81761-338B-3113-9F60-8100D8E1366F
-  Functions: 881
-  Symbols:   2996
-  CStrings:  1416
+  UUID: 323CCDE5-98F6-30C5-A100-9903C55B952D
+  Functions: 897
+  Symbols:   3042
+  CStrings:  1445
 
Symbols:
+ +[OSIUtilities hasEnoughBatteryDataWithMinimumDays:]
+ -[_OSIBLManager isHighDrainOverAggregatedMedianWithError:].cold.3
+ -[_OSIBLManager setStatModelConsultationThreshold:]
+ -[_OSIBLManager setStatModelDiffThreshold:]
+ -[_OSIBLManager setUseStatModel:]
+ -[_OSIBLManager statModelConsultationThreshold]
+ -[_OSIBLManager statModelDiffThreshold]
+ -[_OSIBLManager useStatModel]
+ -[_OSInactivityPredictionClient recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:]
+ _OBJC_IVAR_$__OSIBLManager._statModelConsultationThreshold
+ _OBJC_IVAR_$__OSIBLManager._statModelDiffThreshold
+ _OBJC_IVAR_$__OSIBLManager._useStatModel
+ ___114-[_OSInactivityPredictionClient longInactivityPredictionResultAtDate:withTimeSinceInactive:withOptions:withError:]_block_invoke.115
+ ___147-[_OSInactivityPredictionClient recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:]_block_invoke
+ ___147-[_OSInactivityPredictionClient recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:]_block_invoke.cold.1
+ ___21-[_OSIBLManager init]_block_invoke.101
+ ___21-[_OSIBLManager init]_block_invoke_2.103
+ ___22-[_OSIBLManager start]_block_invoke.124
+ ___22-[_OSIBLManager start]_block_invoke.127
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.112
+ ___45-[_OSInactivityPredictionClient backedUpData]_block_invoke.133
+ ___46-[_OSInactivityPredictionClient modelMetadata]_block_invoke.100
+ ___47-[_OSInactivityPredictionClient initConnection]_block_invoke.88
+ ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.55
+ ___48-[_OSInactivityPredictionClient fixModelOutput:]_block_invoke.118
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke.59
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.60
+ ___49-[_OSInactivityPredictionClient modelDescription]_block_invoke.96
+ ___49-[_OSInactivityPredictionClient unfixModelOutput]_block_invoke.121
+ ___52+[OSIUtilities hasEnoughBatteryDataWithMinimumDays:]_block_invoke
+ ___52+[OSIUtilities hasEnoughBatteryDataWithMinimumDays:]_block_invoke.72
+ ___52+[OSIUtilities hasEnoughBatteryDataWithMinimumDays:]_block_invoke_2
+ ___52+[OSIUtilities hasEnoughBatteryDataWithMinimumDays:]_block_invoke_2.cold.1
+ ___52-[_OSInactivityPredictionClient recommendedWaitTime]_block_invoke.92
+ ___53-[_OSInactivityPredictionClient deviceUsageDiagnosis]_block_invoke.111
+ ___55-[_OSInactivityPredictionClient restoreInactivityModel]_block_invoke.130
+ ___59-[_OSInactivityPredictionClient hasEnoughInactivityHistory]_block_invoke.104
+ ___59-[_OSInactivityPredictionClient inactivityHistoryDiagnosis]_block_invoke.108
+ ___59-[_OSInactivityPredictionClient restoreRecommendedWaitTime]_block_invoke.127
+ ___63-[_OSInactivityPredictionClient overrideRecommendedWaitTimeTo:]_block_invoke.124
+ ___85-[_OSInactivityPredictionClient longInactivityPredictionResultWithOptions:withError:]_block_invoke.113
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_64_e8_32s40s48r_e22_B16?0"BMStoreEvent"8ls32l8s40l8r48l8
+ ___block_literal_global.103
+ ___block_literal_global.110
+ ___block_literal_global.132
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.140
+ ___block_literal_global.142
+ ___block_literal_global.144
+ ___block_literal_global.146
+ ___block_literal_global.148
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.158
+ ___block_literal_global.58
+ ___block_literal_global.71
+ ___block_literal_global.95
+ ___block_literal_global.99
+ _objc_msgSend$hasEnoughBatteryDataWithMinimumDays:
+ _objc_msgSend$isWeekend:
+ _objc_msgSend$recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:
+ _objc_msgSend$setDecisionMaker:
- ___114-[_OSInactivityPredictionClient longInactivityPredictionResultAtDate:withTimeSinceInactive:withOptions:withError:]_block_invoke.112
- ___21-[_OSIBLManager init]_block_invoke.92
- ___21-[_OSIBLManager init]_block_invoke_2.94
- ___22-[_OSIBLManager start]_block_invoke.115
- ___22-[_OSIBLManager start]_block_invoke.118
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.103
- ___45-[_OSInactivityPredictionClient backedUpData]_block_invoke.130
- ___46-[_OSInactivityPredictionClient modelMetadata]_block_invoke.97
- ___47-[_OSInactivityPredictionClient initConnection]_block_invoke.85
- ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.52
- ___48-[_OSInactivityPredictionClient fixModelOutput:]_block_invoke.115
- ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke.56
- ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.57
- ___49-[_OSInactivityPredictionClient modelDescription]_block_invoke.93
- ___49-[_OSInactivityPredictionClient unfixModelOutput]_block_invoke.118
- ___52-[_OSInactivityPredictionClient recommendedWaitTime]_block_invoke.89
- ___53-[_OSInactivityPredictionClient deviceUsageDiagnosis]_block_invoke.108
- ___55-[_OSInactivityPredictionClient restoreInactivityModel]_block_invoke.127
- ___59-[_OSInactivityPredictionClient hasEnoughInactivityHistory]_block_invoke.101
- ___59-[_OSInactivityPredictionClient inactivityHistoryDiagnosis]_block_invoke.105
- ___59-[_OSInactivityPredictionClient restoreRecommendedWaitTime]_block_invoke.124
- ___63-[_OSInactivityPredictionClient overrideRecommendedWaitTimeTo:]_block_invoke.121
- ___85-[_OSInactivityPredictionClient longInactivityPredictionResultWithOptions:withError:]_block_invoke.110
- ___block_literal_global.100
- ___block_literal_global.104
- ___block_literal_global.141
- ___block_literal_global.143
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.155
- ___block_literal_global.55
- ___block_literal_global.92
- ___block_literal_global.96
- _objc_retain_x26
CStrings:
+ "B24@0:8Q16"
+ "Error in recording engagement: %@"
+ "IBLM_StatModelConsultationThreshold"
+ "IBLM_StatModelDifferenceThreshold"
+ "IBLM_UseStatModel"
+ "Oldest battery event at %@, greater than %lu days"
+ "Prev12Next12Drain Stat Model result: %{public}d Difference: %{public}f"
+ "Seems like device is recently setup and does not have enough history"
+ "TB,N,V_useStatModel"
+ "Td,N,V_statModelConsultationThreshold"
+ "Tq,N,V_statModelDiffThreshold"
+ "Trial: %{public}@:%{public}lu"
+ "_statModelConsultationThreshold"
+ "_statModelDiffThreshold"
+ "_useStatModel"
+ "com.apple.powerui.smartcharging.mlmodelpredictor.queryBatteryEvents"
+ "hasEnoughBatteryDataWithMinimumDays:"
+ "osiutilities.hasEnoughBatteryData"
+ "recordEngagementFrom:to:wasInterrupted:withPredictedMetadata:predictedOutput:withAdditionalParameters:withHandler:"
+ "setStatModelConsultationThreshold:"
+ "setStatModelDiffThreshold:"
+ "setUseStatModel:"
+ "statModelConsultationThreshold"
+ "statModelDiffThreshold"
+ "useStatModel"
+ "v68@0:8@\"NSDate\"16@\"NSDate\"24B32@\"_OSInactivityPredictorMetadata\"36@\"_OSInactivityPredictorOutput\"44@\"NSDictionary\"52@?<v@?B@\"NSError\">60"
+ "v68@0:8@16@24B32@36@44@52@?60"
- ":\"4"

```
