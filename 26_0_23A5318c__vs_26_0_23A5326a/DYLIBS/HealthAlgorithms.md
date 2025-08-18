## HealthAlgorithms

> `/System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms`

```diff

 135.0.0.0.0
-  __TEXT.__text: 0x3fc68
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x11dc
-  __TEXT.__const: 0xb899
-  __TEXT.__cstring: 0x1778
-  __TEXT.__oslogstring: 0x413
-  __TEXT.__gcc_except_tab: 0x42a0
-  __TEXT.__unwind_info: 0x1348
-  __TEXT.__objc_classname: 0x380
-  __TEXT.__objc_methname: 0x37db
-  __TEXT.__objc_methtype: 0xda8
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0x40
+  __TEXT.__text: 0x40f90
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x133c
+  __TEXT.__const: 0xb8c9
+  __TEXT.__gcc_except_tab: 0x4308
+  __TEXT.__oslogstring: 0x529
+  __TEXT.__cstring: 0x1b2a
+  __TEXT.__dlopen_cstrs: 0x4e
+  __TEXT.__unwind_info: 0x13c0
+  __TEXT.__objc_classname: 0x3cc
+  __TEXT.__objc_methname: 0x3d26
+  __TEXT.__objc_methtype: 0x108c
+  __TEXT.__objc_stubs: 0x1020
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b8
+  __DATA_CONST.__objc_selrefs: 0xae0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0xe80
-  __AUTH_CONST.__objc_const: 0x2da8
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x220
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_arraydata: 0xd8
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0xd30
+  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__objc_const: 0x3100
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x248
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 615252DA-A66F-340E-81C6-5B13472D3C6A
-  Functions: 1228
-  Symbols:   3618
-  CStrings:  1125
+  UUID: 2F4E134D-E39E-356D-A796-25D3927F02FF
+  Functions: 1263
+  Symbols:   3769
+  CStrings:  1268
 
Symbols:
+ +[HABloodOxygenCalculator analyzeBloodOxygenFromRawData:withPressureInKilopascals:]
+ +[HABloodOxygenCalculator calculateBloodOxygenFromRawData:]
+ -[HABloodOxygenCalculator .cxx_destruct]
+ -[HABloodOxygenCalculator calculateBloodOxygenFromRawData:]
+ -[HABloodOxygenCalculator finalizeAnalytics:timestamp:]
+ -[HABloodOxygenCalculator finalizeAnalytics:timestamp:].cold.1
+ -[HABloodOxygenCalculator finalizeAnalytics:timestamp:].cold.2
+ -[HABloodOxygenCalculator handleAbort:withAnalytics:atTimestamp:]
+ -[HABloodOxygenCalculator handleAbort:withAnalytics:atTimestamp:].cold.1
+ -[HABloodOxygenCalculator handleMotionStatusChange:atTimestamp:]
+ -[HABloodOxygenCalculator handlePostureStatusChange:atTimestamp:]
+ -[HABloodOxygenCalculator handleResult:withAnalytics:atTimestamp:]
+ -[HABloodOxygenCalculator handleResult:withAnalytics:atTimestamp:].cold.1
+ -[HABloodOxygenCalculator runBloodOxygenAnalysisFromRawData:withPressureInKilopascals:]
+ -[HABloodOxygenCalculator runBloodOxygenAnalysisFromRawData:withPressureInKilopascals:].cold.1
+ -[HABloodOxygenCalculator windbreakerSessionDidCompleteSuccessfullyWithRawData:atTimestamp:]
+ -[HABloodOxygenCalculator windbreakerSessionDidCompleteWithRawDataRecorded:atTimestamp:]
+ -[HABloodOxygenMeasurement .cxx_destruct]
+ -[HABloodOxygenMeasurement averageHeartRate]
+ -[HABloodOxygenMeasurement background]
+ -[HABloodOxygenMeasurement date]
+ -[HABloodOxygenMeasurement oxygenSaturationPercentage]
+ -[HABloodOxygenMeasurement setAverageHeartRate:]
+ -[HABloodOxygenMeasurement setBackground:]
+ -[HABloodOxygenMeasurement setDate:]
+ -[HABloodOxygenMeasurement setOxygenSaturationPercentage:]
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_HABloodOxygenCalculator
+ _OBJC_CLASS_$_HABloodOxygenMeasurement
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_IVAR_$_HABloodOxygenCalculator._analysis
+ _OBJC_IVAR_$_HABloodOxygenCalculator._bootTime
+ _OBJC_IVAR_$_HABloodOxygenCalculator._measurement
+ _OBJC_IVAR_$_HABloodOxygenCalculator._pressure
+ _OBJC_IVAR_$_HABloodOxygenCalculator._scandiumProcessor
+ _OBJC_IVAR_$_HABloodOxygenCalculator._ticksPerSecond
+ _OBJC_IVAR_$_HABloodOxygenMeasurement._averageHeartRate
+ _OBJC_IVAR_$_HABloodOxygenMeasurement._background
+ _OBJC_IVAR_$_HABloodOxygenMeasurement._date
+ _OBJC_IVAR_$_HABloodOxygenMeasurement._oxygenSaturationPercentage
+ _OBJC_METACLASS_$_HABloodOxygenCalculator
+ _OBJC_METACLASS_$_HABloodOxygenMeasurement
+ _ScandiumLibraryCore
+ _ScandiumLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_HABloodOxygenCalculator
+ __OBJC_$_INSTANCE_METHODS_HABloodOxygenCalculator
+ __OBJC_$_INSTANCE_METHODS_HABloodOxygenMeasurement
+ __OBJC_$_INSTANCE_VARIABLES_HABloodOxygenCalculator
+ __OBJC_$_INSTANCE_VARIABLES_HABloodOxygenMeasurement
+ __OBJC_$_PROP_LIST_HABloodOxygenCalculator
+ __OBJC_$_PROP_LIST_HABloodOxygenMeasurement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCProcessorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCProcessorDelegate
+ __OBJC_$_PROTOCOL_REFS_SCProcessorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HABloodOxygenCalculator
+ __OBJC_CLASS_RO_$_HABloodOxygenCalculator
+ __OBJC_CLASS_RO_$_HABloodOxygenMeasurement
+ __OBJC_LABEL_PROTOCOL_$_SCProcessorDelegate
+ __OBJC_METACLASS_RO_$_HABloodOxygenCalculator
+ __OBJC_METACLASS_RO_$_HABloodOxygenMeasurement
+ __OBJC_PROTOCOL_$_SCProcessorDelegate
+ ___ScandiumLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___destructor_8_s0_s16
+ ___getSCProcessorClass_block_invoke
+ ___getSCProcessorClass_block_invoke.cold.1
+ ___ha_diagnostic_log_block_invoke
+ ___objc_personality_v0
+ __os_log_debug_impl
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringScandium
+ _free
+ _getSCProcessorClass.softClass
+ _ha_diagnostic_log
+ _ha_diagnostic_log.cold.1
+ _ha_diagnostic_log.log
+ _ha_diagnostic_log.onceToken
+ _objc_enumerationMutation
+ _objc_getClass
+ _objc_msgSend$calculateBloodOxygenFromRawData:
+ _objc_msgSend$component:fromDate:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dictionaryForAnalytics:sessionDuration:systemInterface:
+ _objc_msgSend$finalizeAnalytics:timestamp:
+ _objc_msgSend$forBackground
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithStartPacket:ofLength:delegate:withSignalQualityMetricsEnabled:bypassingAlgorithms:forWindbreaker:bootDate:hardwareModel:
+ _objc_msgSend$intValue
+ _objc_msgSend$isHealthDataSubmissionAllowed
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$processPacket:ofLength:
+ _objc_msgSend$runBloodOxygenAnalysisFromRawData:withPressureInKilopascals:
+ _objc_msgSend$setAverageHeartRate:
+ _objc_msgSend$setBackground:
+ _objc_msgSend$setDate:
+ _objc_msgSend$setOxygenSaturationPercentage:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$subdataWithRange:
+ _objc_retainAutorelease
CStrings:
+ "!"
+ "%s"
+ "+[HABloodOxygenCalculator analyzeBloodOxygenFromRawData:withPressureInKilopascals:]"
+ "+[HABloodOxygenCalculator calculateBloodOxygenFromRawData:]"
+ "-[HABloodOxygenCalculator handleAbort:withAnalytics:atTimestamp:]"
+ "-[HABloodOxygenCalculator handleResult:withAnalytics:atTimestamp:]"
+ "@\"HABloodOxygenMeasurement\""
+ "@\"SCProcessor\""
+ "CFAbsoluteTimeRounded"
+ "HABloodOxygenCalculator"
+ "HABloodOxygenMeasurement"
+ "LP5 ID %u: %zu bytes"
+ "SCProcessor"
+ "SCProcessorDelegate"
+ "T@\"NSDate\",&,N,V_date"
+ "TB,N,V_background"
+ "Tf,N,V_averageHeartRate"
+ "Tf,N,V_oxygenSaturationPercentage"
+ "Unable to find class %s"
+ "_analysis"
+ "_averageHeartRate"
+ "_background"
+ "_bootTime"
+ "_date"
+ "_measurement"
+ "_oxygenSaturationPercentage"
+ "_pressure"
+ "_scandiumProcessor"
+ "_ticksPerSecond"
+ "agcOpcGreenSampRate256Hz"
+ "agcOpcNumConverged"
+ "agcOpcNumRetries"
+ "analyzeBloodOxygenFromRawData:withPressureInKilopascals:"
+ "averageHeartRate"
+ "background"
+ "barometricPressure"
+ "bootTime: %f, sessionStartTime %llu, ticksPerSecond: %d, sessionDuration: %f"
+ "calculateBloodOxygenFromRawData:"
+ "component:fromDate:"
+ "coreAnalytics is nil. analytics->is_complete: %{public}@ self.processor.forBackground: %{public}s"
+ "countByEnumeratingWithState:objects:count:"
+ "date"
+ "dictionaryForAnalytics:sessionDuration:systemInterface:"
+ "finalizeAnalytics:timestamp:"
+ "forBackground"
+ "foreground"
+ "handleAbort:withAnalytics:atTimestamp:"
+ "handleMotionStatusChange:atTimestamp:"
+ "handlePostureStatusChange:atTimestamp:"
+ "handleResult:withAnalytics:atTimestamp:"
+ "hourOfDay"
+ "i"
+ "incompleteReason"
+ "initWithCalendarIdentifier:"
+ "initWithData:encoding:"
+ "initWithStartPacket:ofLength:delegate:withSignalQualityMetricsEnabled:bypassingAlgorithms:forWindbreaker:bootDate:hardwareModel:"
+ "intValue"
+ "isHealthDataSubmissionAllowed"
+ "localTimeZone"
+ "meanPerfusionIndexGreenShort"
+ "meanPerfusionIndexIrLong"
+ "meanPerfusionIndexIrShort"
+ "meanPerfusionIndexRedLong"
+ "meanPerfusionIndexRedShort"
+ "meanSpO2Long"
+ "meanSpO2ShortIR"
+ "meanSpO2ShortRed"
+ "mutableCopy"
+ "notApplicable"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "numberWithLong:"
+ "oxygenSaturationPercentage"
+ "postedHeartRate"
+ "postedHeartRateRounded"
+ "postedSpO2Rounded"
+ "pressureInKilopascals: %{public}@"
+ "processPacket:ofLength:"
+ "rawSpO2"
+ "rawSpO2NoConfidenceGate"
+ "rawSpO2NoConfidenceGateWindow0"
+ "rawSpO2NoConfidenceGateWindow1"
+ "rawSpO2NoConfidenceGateWindow2"
+ "rawSpO2Window0"
+ "rawSpO2Window1"
+ "rawSpO2Window2"
+ "realTimeMaxMAV"
+ "realTimeMedianMAV"
+ "realTimeMinMAV"
+ "runBloodOxygenAnalysisFromRawData:withPressureInKilopascals:"
+ "scandium"
+ "sessionEndTime: %f, sessionEndDate:  %{public}@"
+ "setAverageHeartRate:"
+ "setBackground:"
+ "setDate:"
+ "setOxygenSaturationPercentage:"
+ "setTimeZone:"
+ "sharedConnection"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Scandium.framework/Scandium"
+ "startTimestamp"
+ "subdataWithRange:"
+ "v20@0:8f16"
+ "v28@0:8B16d20"
+ "v32@0:8@\"NSData\"16d24"
+ "v32@0:8@16d24"
+ "v32@0:8r^{SCAnalytics=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}16d24"
+ "v36@0:8C16r^{SCAnalytics=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}20d28"
+ "v40@0:8r^{SCResult=ff}16r^{SCAnalytics=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}24d32"
+ "windbreakerSessionDidCompleteSuccessfullyWithRawData:atTimestamp:"
+ "windbreakerSessionDidCompleteWithRawDataRecorded:atTimestamp:"
+ "{HABloodOxygenAnalysis=\"measurement\"@\"HABloodOxygenMeasurement\"\"background\"B\"coreAnalytics\"@\"NSDictionary\"}"
+ "{HABloodOxygenAnalysis=@B@}32@0:8@16@24"

```
