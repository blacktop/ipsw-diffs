## ospredictiond

> `/usr/libexec/ospredictiond`

```diff

-232.0.0.0.0
-  __TEXT.__text: 0x5b754
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x8680
-  __TEXT.__objc_methlist: 0x8670
+234.40.3.0.0
+  __TEXT.__text: 0x5cd34
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x8a00
+  __TEXT.__objc_methlist: 0x89c0
   __TEXT.__const: 0x2f8
-  __TEXT.__cstring: 0x48b7
-  __TEXT.__objc_methname: 0x135b9
-  __TEXT.__oslogstring: 0x5445
-  __TEXT.__objc_classname: 0xcfa
-  __TEXT.__objc_methtype: 0x221a
+  __TEXT.__cstring: 0x49ed
+  __TEXT.__objc_methname: 0x13d19
+  __TEXT.__oslogstring: 0x54eb
+  __TEXT.__objc_classname: 0xd53
+  __TEXT.__objc_methtype: 0x225b
   __TEXT.__gcc_except_tab: 0xa7c
-  __TEXT.__unwind_info: 0x1228
-  __DATA_CONST.__auth_got: 0x410
+  __TEXT.__unwind_info: 0x1290
+  __DATA_CONST.__auth_got: 0x418
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__const: 0xf28
-  __DATA_CONST.__cfstring: 0x5520
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__cfstring: 0x56a0
+  __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x300
-  __DATA_CONST.__objc_intobj: 0x1b0
-  __DATA_CONST.__objc_arraydata: 0x1370
+  __DATA_CONST.__objc_superrefs: 0x330
+  __DATA_CONST.__objc_intobj: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x13a8
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__objc_arrayobj: 0x408
+  __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xf048
-  __DATA.__objc_selrefs: 0x3730
-  __DATA.__objc_ivar: 0xcd0
-  __DATA.__objc_data: 0x2300
+  __DATA.__objc_const: 0xf7b8
+  __DATA.__objc_selrefs: 0x3870
+  __DATA.__objc_ivar: 0xd18
+  __DATA.__objc_data: 0x24e0
   __DATA.__data: 0x720
   __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BB35C87-A7F0-381F-A4AA-AAFE340F1200
-  Functions: 2985
-  Symbols:   255
-  CStrings:  5042
+  UUID: 34BC6FA5-9918-39DD-8722-B80D25350757
+  Functions: 3052
+  Symbols:   256
+  CStrings:  5150
 
Symbols:
+ _PLQueryRegistered
CStrings:
+ "(subsystem == 'BatteryDataCollection' AND category == 'BDC_OBC')"
+ "(subsystem == 'BatteryDataCollection' AND category == 'BDC_SBC')"
+ "@40@0:8@16@24d32"
+ "@72@0:8d16d24d32d40d48d56d64"
+ "@80@0:8d16d24d32d40d48d56d64^@72"
+ "Could not load tte_v1.mlmodelc in the bundle resource"
+ "Curr_SoC_10th_Percentile"
+ "Curr_SoC_90th_Percentile"
+ "Curr_SoC_IQ1"
+ "Curr_SoC_IQ3"
+ "Curr_SoC_Median"
+ "Curr_SoC_SD"
+ "Current SoC 10: %@"
+ "Current SoC 90: %@"
+ "Current SoC IQ1: %@"
+ "Current SoC IQ3: %@"
+ "Current SoC Median: %@"
+ "Current SoC Std Dev: %@"
+ "Done with mlInputFeatures, returning it. inputDict: %@"
+ "ETA model raw output %@"
+ "Error from PPSGetData for OBC %@"
+ "Error from PPSGetData for SBC %@"
+ "ExternalConnected"
+ "FQ"
+ "Not enough history to make prediction : %{public}lf days"
+ "Prediction input %{public}@ : %{public}lf"
+ "Prev12Next12Drain result  %{public}@"
+ "StateOfCharge"
+ "T@\"NSDate\",&,N,V_timestamp"
+ "T@\"NSMutableArray\",&,N,V_dischargeEvents"
+ "T@\"NSNumber\",&,N,V_currentCapacity"
+ "T@\"NSNumber\",&,N,V_endSoC"
+ "T@\"NSNumber\",&,N,V_soc"
+ "T@\"NSNumber\",&,N,V_startSoC"
+ "Td,N,V_Curr_SoC_10th_Percentile"
+ "Td,N,V_Curr_SoC_90th_Percentile"
+ "Td,N,V_Curr_SoC_IQ1"
+ "Td,N,V_Curr_SoC_IQ3"
+ "Td,N,V_Curr_SoC_Median"
+ "Td,N,V_Curr_SoC_SD"
+ "Td,N,V_StateOfCharge"
+ "Td,N,V_durationToDischarge"
+ "Td,N,V_tte"
+ "Ti,N,V_rarelyUsedTimeRestrictionEarlyHourForSleepSuppression"
+ "Ti,N,V_rarelyUsedTimeRestrictionLateHourForSleepSuppression"
+ "Total Discharge Cycles: %@"
+ "Total Discharge Intervals: %@"
+ "XPCCacheFlush"
+ "_Curr_SoC_10th_Percentile"
+ "_Curr_SoC_90th_Percentile"
+ "_Curr_SoC_IQ1"
+ "_Curr_SoC_IQ3"
+ "_Curr_SoC_Median"
+ "_Curr_SoC_SD"
+ "_OSDischargeCycle"
+ "_OSDischargeEvent"
+ "_OSDischargeInterval"
+ "_StateOfCharge"
+ "_currentCapacity"
+ "_dischargeEvents"
+ "_durationToDischarge"
+ "_rarelyUsedTimeRestrictionEarlyHourForSleepSuppression"
+ "_rarelyUsedTimeRestrictionLateHourForSleepSuppression"
+ "_soc"
+ "_timestamp"
+ "_tte"
+ "addEvent:"
+ "currentCapacity"
+ "dischargeEvents"
+ "durationToDischarge"
+ "findEventWithCurrentCapacity:"
+ "getInputFeatures"
+ "getLastEvent"
+ "initWithSoC:andCurrrentCapacity:andTimestamp:"
+ "initWithStartSoC:andEndSoC:andDurationToDischarge:"
+ "initWithStateOfCharge:Curr_SoC_Median:Curr_SoC_SD:Curr_SoC_10th_Percentile:Curr_SoC_IQ1:Curr_SoC_IQ3:Curr_SoC_90th_Percentile:"
+ "initWithTte:"
+ "isEqualToNumber:"
+ "mergeWithTimeSeries:"
+ "monotonicTimestamp"
+ "predictionFromStateOfCharge:Curr_SoC_Median:Curr_SoC_SD:Curr_SoC_10th_Percentile:Curr_SoC_IQ1:Curr_SoC_IQ3:Curr_SoC_90th_Percentile:error:"
+ "rarelyUsedTimeRestrictionEarlyHourForSleepSuppression"
+ "rarelyUsedTimeRestrictionLateHourForSleepSuppression"
+ "setCurr_SoC_10th_Percentile:"
+ "setCurr_SoC_90th_Percentile:"
+ "setCurr_SoC_IQ1:"
+ "setCurr_SoC_IQ3:"
+ "setCurr_SoC_Median:"
+ "setCurr_SoC_SD:"
+ "setDischargeEvents:"
+ "setDurationToDischarge:"
+ "setEndSoC:"
+ "setRarelyUsedTimeRestrictionEarlyHourForSleepSuppression:"
+ "setRarelyUsedTimeRestrictionLateHourForSleepSuppression:"
+ "setSoc:"
+ "setStartSoC:"
+ "setStateOfCharge:"
+ "setTimestamp:"
+ "setTte:"
+ "signalsTimeRestrictionEarlyHourForSleepSuppression"
+ "signalsTimeRestrictionLateHourForSleepSuppression"
+ "soc"
+ "tte"
+ "tte_v1"
+ "tte_v1Input"
+ "tte_v1Output"
+ "unsignedIntValue"
- "6Q"
- "Adding current duration %@"
- "Amperage"
- "Discharge ETA prediction output %@ for model %@"
- "Getting on-device PPS Data"
- "Median duration untill discharge %@"
- "Not enough history to make prediction : %lf days"
- "PPS Response is %lu objects"
- "Prediction input %@ : %lf"
- "Prev12Next12Drain result  %@"
- "Result is %@"
- "Returning fixed prediction result %@"
- "Returning prediction result %@"
- "Temperature"
- "Voltage"
- "com.apple.osintelligence.timeTillDischarge.dataFetch"
- "d32@0:8q16q24"
- "instantaneousTemperatureAndAmperage"
- "orPredicateWithSubpredicates:"
- "timeUntilSOC:fromCurrent:"

```
