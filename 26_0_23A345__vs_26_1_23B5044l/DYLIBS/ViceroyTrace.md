## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2145.62.1.2.0
-  __TEXT.__text: 0xad33c
+2175.9.2.0.0
+  __TEXT.__text: 0xadf78
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8cf8
-  __TEXT.__const: 0x2478
-  __TEXT.__cstring: 0xe904
-  __TEXT.__oslogstring: 0xc5ce
+  __TEXT.__objc_methlist: 0x8d60
+  __TEXT.__const: 0x24a8
+  __TEXT.__cstring: 0xea60
+  __TEXT.__oslogstring: 0xc712
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1bb43
-  __TEXT.__objc_methtype: 0x2441
-  __TEXT.__objc_stubs: 0xed80
+  __TEXT.__objc_methname: 0x1bd0c
+  __TEXT.__objc_methtype: 0x244f
+  __TEXT.__objc_stubs: 0xee60
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xd88
+  __DATA_CONST.__const: 0xd98
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42c0
+  __DATA_CONST.__objc_selrefs: 0x42f8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdd80
-  __AUTH_CONST.__objc_const: 0x167d8
+  __AUTH_CONST.__cfstring: 0xde60
+  __AUTH_CONST.__objc_const: 0x16898
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x200c
+  __DATA.__objc_ivar: 0x2020
   __DATA.__data: 0x738
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x80
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0xaa
+  __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x22
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F0D9BDE7-1171-39D2-9029-D14F6092F4E9
-  Functions: 3957
-  Symbols:   13029
-  CStrings:  9237
+  UUID: EFBC49D3-A981-3FFF-A6CF-684DBC76A2BF
+  Functions: 3968
+  Symbols:   13065
+  CStrings:  9274
 
Symbols:
+ +[VCAggregator firstOrientation:matchesSecondOrientation:]
+ -[MultiwayCall currentRemoteOrientation]
+ -[MultiwayCall matchedOrientationDurations]
+ -[MultiwayCall setCurrentRemoteOrientation:]
+ -[VCAggregator finalizeSession]
+ -[VCAggregator setPeriodicAggregationOccurredHandler:]
+ -[VCAggregatorMultiway finalizeSession]
+ -[VCAggregatorMultiway processDeviceOrientation:]
+ -[VCSymptomReporter reportVideoReceiverEnqueueFrameRateTooHighWithOptionalDictionary:]
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table54
+ GCC_except_table78
+ _OBJC_IVAR_$_MultiwayCall._currentRemoteOrientation
+ _OBJC_IVAR_$_MultiwayCall._matchedOrientationDurations
+ _OBJC_IVAR_$_VCAggregator._periodicAggregationOccurredHandler
+ _OBJC_IVAR_$_VCAggregatorMultiway._currentLocalOrientation
+ _OBJC_IVAR_$_VCAggregatorMultiway._localOrientationChangeCount
+ _OBJC_IVAR_$_VCAggregatorMultiway._localOrientationDurations
+ __MergedGlobals.1003
+ __VRTraceIsInternalOSInstalled
+ __VRTraceIsInternalOSInstalled.hasChecked
+ __VRTraceIsInternalOSInstalled.isInternal
+ __VRTraceIsInternalOSInstalled.simulateCustomerBuild
+ ___39-[VCAggregatorMultiway finalizeSession]_block_invoke
+ ___54-[VCAggregator setPeriodicAggregationOccurredHandler:]_block_invoke
+ ___VRTraceReset__block_invoke.31
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.32
+ ___block_literal_global.29
+ ___block_literal_global.34
+ ___reportingSetPeriodicAggregationOccurredHandler_block_invoke
+ __reportingVCRunOnce.cold.2
+ _matchedOrientation
+ _objc_msgSend$currentRemoteOrientation
+ _objc_msgSend$finalizeSession
+ _objc_msgSend$firstOrientation:matchesSecondOrientation:
+ _objc_msgSend$matchedOrientationDurations
+ _objc_msgSend$processDeviceOrientation:
+ _objc_msgSend$reportVideoReceiverEnqueueFrameRateTooHighWithOptionalDictionary:
+ _objc_msgSend$setCurrentRemoteOrientation:
+ _objc_msgSend$setPeriodicAggregationOccurredHandler:
+ _orientationType
+ _reportingSetPeriodicAggregationOccurredHandler
+ _reportingSetPeriodicAggregationOccurredHandler.cold.1
+ _sRTCReportingAPI_RelaxSessionLimit
- -[VCAggregator setPeriodicAggregationOccuredHandler:]
- GCC_except_table126
- GCC_except_table128
- GCC_except_table230
- GCC_except_table231
- GCC_except_table239
- GCC_except_table53
- GCC_except_table77
- _OBJC_IVAR_$_VCAggregator._periodicAggregationOccuredHandler
- _VRTraceIsInternalOSInstalled.hasChecked
- _VRTraceIsInternalOSInstalled.isInternal
- __MergedGlobals.1002
- ___53-[VCAggregator setPeriodicAggregationOccuredHandler:]_block_invoke
- ___VRTraceReset__block_invoke.28
- ___block_descriptor_tmp.24
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.7
- ___block_literal_global.26
- ___block_literal_global.31
- ___reportingSetPeriodicAggregationOccuredHandler_block_invoke
- _objc_msgSend$setPeriodicAggregationOccuredHandler:
- _reportingSetPeriodicAggregationOccuredHandler
- _reportingSetPeriodicAggregationOccuredHandler.cold.1
CStrings:
+ " [%s] %s:%d SymptomReporter: reporting symptom on VideoReceiverEnqueueFrameRateTooHigh optionalDictionary=%@"
+ " [%s] %s:%d lastReceivedVideoStallTime value=%f was transferred to the new DownlinkSegment for participantID=%@, streamGroupID=%@"
+ " [%s] %s:%d totalDecodedVideoFrameEnqueueCounter=%u (%@); Frame rate is higher than %d FPS"
+ "-[VCAggregatorMultiway addStreamGroupTelemetryForCall:callReport:]"
+ "-[VCSymptomReporter reportVideoReceiverEnqueueFrameRateTooHighWithOptionalDictionary:]"
+ "B24@0:8C16C20"
+ "ORTNChangeCount"
+ "ORTNDurs"
+ "ORTNLocal"
+ "ORTNMatchedDurs"
+ "ORTNRemote"
+ "RTC_relaxSessions"
+ "ReportingVC [%s] %s:%d Failed to resolve SPI RelaxSessionLimit"
+ "ReportingVC [%s] %s:%d Timeout occurred during Periodic Task"
+ "ReportingVC [%s] %s:%d Timeout occurred during Periodic Task collection scheduling"
+ "ReportingVC [%s] %s:%d Timeout occurred during Periodic Task update scheduling"
+ "T@\"VCDurationHistogram\",R,V_matchedOrientationDurations"
+ "TC,V_currentRemoteOrientation"
+ "VRTraceSimulateCustomerBuild"
+ "VideoReceiverEnqueueFrameRateTooHigh"
+ "[80B]"
+ "_VCReporting_SetCustomConcurrentSessionLimit"
+ "_VRTraceIsInternalOSInstalled: Simulating customer build"
+ "_currentLocalOrientation"
+ "_currentRemoteOrientation"
+ "_localOrientationChangeCount"
+ "_localOrientationDurations"
+ "_matchedOrientationDurations"
+ "_periodicAggregationOccurredHandler"
+ "currentRemoteOrientation"
+ "finalizeSession"
+ "firstOrientation:matchesSecondOrientation:"
+ "matchedOrientationDurations"
+ "processDeviceOrientation:"
+ "reportVideoReceiverEnqueueFrameRateTooHighWithOptionalDictionary:"
+ "reportingSetPeriodicAggregationOccurredHandler"
+ "setCurrentRemoteOrientation:"
+ "setPeriodicAggregationOccurredHandler:"
+ "void reportingSetPeriodicAggregationOccurredHandler(RTCReportingRef, RTCPeriodicAggregationOccurredHandler)"
- " [%s] %s:%d lastReceivedVideoStallTime value=%f was transfered to the new DownlinkSegment for participantID=%@, streamGroupID=%@"
- "ReportingVC [%s] %s:%d Timeout occured during Periodic Task"
- "ReportingVC [%s] %s:%d Timeout occured during Periodic Task collection scheduling"
- "ReportingVC [%s] %s:%d Timeout occured during Periodic Task update scheduling"
- "[79B]"
- "_periodicAggregationOccuredHandler"
- "reportingSetPeriodicAggregationOccuredHandler"
- "setPeriodicAggregationOccuredHandler:"
- "void reportingSetPeriodicAggregationOccuredHandler(RTCReportingRef, RTCPeriodicAggregationOccuredHandler)"

```
