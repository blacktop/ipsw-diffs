## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-206.0.0.0.0
-  __TEXT.__text: 0x16034
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x1e68
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x13b4
-  __TEXT.__gcc_except_tab: 0x5ec
-  __TEXT.__oslogstring: 0x175d
-  __TEXT.__unwind_info: 0x848
-  __TEXT.__objc_classname: 0x41e
-  __TEXT.__objc_methname: 0x3673
-  __TEXT.__objc_methtype: 0xaaa
-  __TEXT.__objc_stubs: 0x2760
+213.0.0.502.1
+  __TEXT.__text: 0x16a60
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x1ed0
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x1435
+  __TEXT.__gcc_except_tab: 0x5f8
+  __TEXT.__oslogstring: 0x18d7
+  __TEXT.__unwind_info: 0x888
+  __TEXT.__objc_classname: 0x41c
+  __TEXT.__objc_methname: 0x37e1
+  __TEXT.__objc_methtype: 0xab8
+  __TEXT.__objc_stubs: 0x27e0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeb8
+  __DATA_CONST.__objc_selrefs: 0xf00
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x2f0
-  __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x10c0
-  __AUTH_CONST.__objc_const: 0x2be0
+  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__const: 0x760
+  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__objc_const: 0x2c70
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x194
   __DATA.__data: 0x540
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4937A479-4DA1-31AE-9B23-61CDFCD4551D
-  Functions: 795
-  Symbols:   2668
-  CStrings:  1205
+  UUID: FF3E3DA1-EF1C-3A1D-9514-2DDBABA1EB5D
+  Functions: 813
+  Symbols:   2718
+  CStrings:  1234
 
Symbols:
+ -[_OSBatteryDrainPredictor didReachEngagementThresholds]
+ -[_OSBatteryDrainPredictor firstBatteryLevelDate]
+ -[_OSBatteryDrainPredictor recordIntelligentLPMThreshold:threshold:]
+ -[_OSIBLManager alreadyStarted]
+ -[_OSIBLManager managerStartStopQueue]
+ -[_OSIBLManager setAlreadyStarted:]
+ -[_OSIBLManager setManagerStartStopQueue:]
+ -[_OSIBatteryLifeManager registerForDrainLevelPredictionForClient:withithUpdateHandler:].cold.1
+ -[_OSICLPCInterface mitigationOption]
+ -[_OSICLPCInterface setMitigationOption:]
+ -[_OSICLPCInterface stop]
+ -[_OSICLPCInterface stop].cold.1
+ -[_OSICLPCInterface updatePerformanceControlWithMitigation:]
+ _OBJC_IVAR_$__OSIBLManager._alreadyStarted
+ _OBJC_IVAR_$__OSIBLManager._managerStartStopQueue
+ _OBJC_IVAR_$__OSICLPCInterface._mitigationOption
+ ___21-[_OSIBLManager init]_block_invoke.73
+ ___21-[_OSIBLManager init]_block_invoke_2.75
+ ___22-[_OSIBLManager start]_block_invoke.92
+ ___22-[_OSIBLManager start]_block_invoke.95
+ ___38-[_OSIBLManager handleFeatureDisabled]_block_invoke
+ ___44-[_OSIBLManager currentMitigationWithError:]_block_invoke
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke.61
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke_2
+ ___49-[_OSBatteryDrainPredictor firstBatteryLevelDate]_block_invoke_2.cold.1
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.62
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.1
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.2
+ ___68-[_OSBatteryDrainPredictor recordIntelligentLPMThreshold:threshold:]_block_invoke
+ ___block_descriptor_40_e8_32r_e22_B16?0"BMStoreEvent"8lr32l8
+ ___block_descriptor_48_e19_"NSDictionary"8?0l
+ ___block_literal_global.60
+ _notify_cancel
+ _objc_msgSend$didReachEngagementThresholds
+ _objc_msgSend$firstBatteryLevelDate
+ _objc_msgSend$recordIntelligentLPMThreshold:threshold:
+ _objc_msgSend$refresh
+ _objc_msgSend$setMitigationOption:
+ _objc_msgSend$sinkWithCompletion:shouldContinue:
+ _objc_msgSend$updatePerformanceControlWithMitigation:
- -[_OSBatteryDrainPredictor didLastChargingSessionFinish]
- -[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]
- ___21-[_OSIBLManager init]_block_invoke.71
- ___21-[_OSIBLManager init]_block_invoke_2.74
- ___21-[_OSIBLManager init]_block_invoke_3
- ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.59
- ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke
- ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke.cold.1
- ___76-[_OSICLPCInterface updatePerformanceControlWithMitigation:withOptionValue:]_block_invoke.cold.2
- ___block_literal_global.101
- _objc_msgSend$didLastChargingSessionFinish
- _objc_msgSend$minute
- _objc_msgSend$updatePerformanceControlWithMitigation:withOptionValue:
CStrings:
+ "Error getting battery level biome events in firstBatteryLevelDate %@"
+ "Error getting battery stream in lastBatteryLevelValue: %s"
+ "IBLM Manager already started. Skipping start"
+ "Sending Intelligent LPM CA event: %ld"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_managerStartStopQueue"
+ "TB,N,V_alreadyStarted"
+ "Tq,N,V_mitigationOption"
+ "Using cached result %@"
+ "_alreadyStarted"
+ "_managerStartStopQueue"
+ "_mitigationOption"
+ "alreadyStarted"
+ "batteryLevel"
+ "com.apple.osintelligence.OSIBLManager.managerStartStop"
+ "com.apple.osintelligence.intelligent_lpm_threshold"
+ "didReachEngagementThresholds"
+ "firstBatteryLevelDate"
+ "highBatteryDrainComparedtoHourlyAggregate failed error: %@ lastValue: %ld lastDate: %@"
+ "highBatteryDrainComparedtoHourlyAggregate lastBatteryLevelValue: %ld currentDelta: %ld resultArray: %@"
+ "managerStartStopQueue"
+ "mitigationOption"
+ "recordIntelligentLPMThreshold:threshold:"
+ "refresh"
+ "setAlreadyStarted:"
+ "setManagerStartStopQueue:"
+ "setMitigationOption:"
+ "sinkWithCompletion:shouldContinue:"
+ "threshold"
+ "updatePerformanceControlWithMitigation:"
+ "v32@0:8q16q24"
- "CLPC option overide set via Trial. Value %ld"
- "didLastChargingSessionFinish"
- "minute"
- "updatePerformanceControlWithMitigation:withOptionValue:"

```
