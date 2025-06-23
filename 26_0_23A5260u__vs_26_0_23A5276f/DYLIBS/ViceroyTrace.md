## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2145.45.1.11.2
-  __TEXT.__text: 0xabac0
+2145.50.1.0.0
+  __TEXT.__text: 0xacb24
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x8bf0
+  __TEXT.__objc_methlist: 0x8ca8
   __TEXT.__const: 0x2478
-  __TEXT.__cstring: 0xe5de
-  __TEXT.__oslogstring: 0xc421
+  __TEXT.__cstring: 0xe7ea
+  __TEXT.__oslogstring: 0xc59e
   __TEXT.__gcc_except_tab: 0x3b4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1668
+  __TEXT.__unwind_info: 0x1688
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1b640
-  __TEXT.__objc_methtype: 0x23c3
-  __TEXT.__objc_stubs: 0xeac0
+  __TEXT.__objc_methname: 0x1b8a7
+  __TEXT.__objc_methtype: 0x240f
+  __TEXT.__objc_stubs: 0xec60
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xd68
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4200
+  __DATA_CONST.__objc_selrefs: 0x4278
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdbe0
-  __AUTH_CONST.__objc_const: 0x16640
+  __AUTH_CONST.__cfstring: 0xdc80
+  __AUTH_CONST.__objc_const: 0x166e8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1fe0
+  __DATA.__objc_ivar: 0x1ff0
   __DATA.__data: 0x698
   __DATA.__bss: 0x70
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7C75EE57-C7AF-30F3-9EB4-A85FEB39E498
-  Functions: 3914
-  Symbols:   12905
-  CStrings:  9151
+  UUID: 3AF4B7F7-43DB-3F58-ABD6-71407F6E34AD
+  Functions: 3933
+  Symbols:   12963
+  CStrings:  9199
 
Symbols:
+ +[VCAggregatorUtils safeRoundOffNumber:toSignificantDigits:maxAllowedValue:]
+ +[VCAggregatorUtils safeRoundOffNumber:toSignificantDigits:maxAllowedValue:].cold.1
+ -[MultiwaySegment isP2PTLEABTestEnabled]
+ -[MultiwaySegment setIsP2PTLEABTestEnabled:]
+ -[VCAggregatorMultiway HDCaptureDurationsMsec]
+ -[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:]
+ -[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:].cold.1
+ -[VCAggregatorMultiway markHDCaptureStartWithTimestamp:]
+ -[VCAggregatorMultiway markHDCaptureStopWithTimestamp:]
+ -[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:]
+ -[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:].cold.1
+ -[VCAggregatorMultiway processSliceStatusABCSymptoms:currentSegmentName:]
+ -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]
+ -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:].cold.1
+ -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]
+ -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:].cold.1
+ -[VCAggregatorMultiway setHDCaptureDurationsMsec:]
+ -[VCSymptomReporter reportConnectionSliceStatus:]
+ GCC_except_table77
+ _OBJC_IVAR_$_MultiwaySegment._isP2PTLEABTestEnabled
+ _OBJC_IVAR_$_VCAggregator._isP2PTLEABTestEnabled
+ _OBJC_IVAR_$_VCAggregatorMultiway._hdCaptureDurationsMsec
+ _OBJC_IVAR_$_VCAggregatorMultiway._hdCaptureStartTime
+ _OBJC_IVAR_$_VCAggregatorVideoStream._averageRxFrameRateSum
+ _OBJC_IVAR_$_VCCaptionsDataCollector._languageCodeDict
+ ___reportingScreenCaptureEvent_block_invoke
+ _objc_msgSend$checkSliceStatus:hasValuesOnlyForStatus:
+ _objc_msgSend$compare:
+ _objc_msgSend$isP2PTLEABTestEnabled
+ _objc_msgSend$markHDCaptureStartWithTimestamp:
+ _objc_msgSend$markHDCaptureStopWithTimestamp:
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$processHDCaptureEnabledWithType:withTimestamp:
+ _objc_msgSend$processSliceStatusABCSymptoms:currentSegmentName:
+ _objc_msgSend$processSliceStatusFailedABCSymptom:
+ _objc_msgSend$processSliceStatusNotReceivedABCSymptom:
+ _objc_msgSend$reportConnectionSliceStatus:
+ _objc_msgSend$safeRoundOffNumber:toSignificantDigits:maxAllowedValue:
+ _objc_msgSend$setIsP2PTLEABTestEnabled:
+ _reportingScreenCaptureEvent
- GCC_except_table76
- _OBJC_IVAR_$_VCAggregatorVideoStream._averageRxFramerateSum
- _OBJC_IVAR_$_VCCaptionsDataCollector._detectedLanguageCodeHistogram
- _OUTLINED_FUNCTION_76
CStrings:
+ " [%s] %s:%d Already reported"
+ " [%s] %s:%d Supplied status has no value"
+ " [%s] %s:%d SymptomReporter: reporting symptom on connection Slice status for callID=%u symptomID=%d"
+ " [%s] %s:%d VCAggregatorMultiway: hdCapture invalid type=%hu"
+ "+[VCAggregatorUtils safeRoundOffNumber:toSignificantDigits:maxAllowedValue:]"
+ "-[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:]"
+ "-[VCAggregatorMultiway processHDCaptureEnabledWithType:withTimestamp:]"
+ "-[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]"
+ "-[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]"
+ "-[VCSymptomReporter reportConnectionSliceStatus:]"
+ "@36@0:8@16C24@28"
+ "B28@0:8@16i24"
+ "HDCaptureDurationsMsec"
+ "PTLE"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
+ "SliceInterfaceFailed"
+ "SliceInterfaceNotReceived"
+ "T@\"NSMutableArray\",V_hdCaptureDurationsMsec"
+ "TB,V_isP2PTLEABTestEnabled"
+ "VTSCD"
+ "[77B]"
+ "_averageRxFrameRateSum"
+ "_hdCaptureDurationsMsec"
+ "_hdCaptureStartTime"
+ "_isP2PTLEABTestEnabled"
+ "_languageCodeDict"
+ "checkSliceStatus:hasValuesOnlyForStatus:"
+ "compare:"
+ "i20@0:8I16"
+ "isP2PTLEABTestEnabled"
+ "markHDCaptureStartWithTimestamp:"
+ "markHDCaptureStopWithTimestamp:"
+ "numberFromString:"
+ "p2pTLE"
+ "processHDCaptureEnabledWithType:withTimestamp:"
+ "processSliceStatusABCSymptoms:currentSegmentName:"
+ "processSliceStatusFailedABCSymptom:"
+ "processSliceStatusNotReceivedABCSymptom:"
+ "reportConnectionSliceStatus:"
+ "reportingScreenCaptureEvent"
+ "reportingScreenCaptureEvent_block_invoke"
+ "safeRoundOffNumber:toSignificantDigits:maxAllowedValue:"
+ "setHDCaptureDurationsMsec:"
+ "setIsP2PTLEABTestEnabled:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@16^{tagVCAggregatorFaceTimeSegmentStatsBytes=QQQQQQQQ}24"
+ "v32@0:8^{tagVCAggregatorFaceTimeSegmentStatsBytes=QQQQQQQQ}16@24"
- "[75B]"
- "_averageRxFramerateSum"
- "_detectedLanguageCodeHistogram"
- "v32@0:8@16^{tagVCAggregatorFaceTimeSegmentStatsBytes=QQQQIIII}24"
- "v32@0:8^{tagVCAggregatorFaceTimeSegmentStatsBytes=QQQQIIII}16@24"

```
