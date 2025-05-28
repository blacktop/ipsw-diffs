## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-104.0.1.0.0
-  __TEXT.__text: 0x2bf54
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x2d90
-  __TEXT.__cstring: 0x140d
-  __TEXT.__oslogstring: 0x5e85
-  __TEXT.__gcc_except_tab: 0x208
+104.0.6.0.0
+  __TEXT.__text: 0x2cb08
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x2dc8
+  __TEXT.__cstring: 0x148c
+  __TEXT.__oslogstring: 0x61cd
+  __TEXT.__gcc_except_tab: 0x1f8
   __TEXT.__const: 0x68
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__eh_frame: 0x38
+  __TEXT.__unwind_info: 0x7b0
   __TEXT.__objc_classname: 0x58f
-  __TEXT.__objc_methname: 0x8739
-  __TEXT.__objc_methtype: 0x10f9
-  __TEXT.__objc_stubs: 0x61c0
+  __TEXT.__objc_methname: 0x8883
+  __TEXT.__objc_methtype: 0x1107
+  __TEXT.__objc_stubs: 0x6240
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4f88
-  __DATA_CONST.__objc_selrefs: 0x1be0
-  __AUTH_CONST.__cfstring: 0x1f20
+  __DATA_CONST.__objc_const: 0x4fb8
+  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_classrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __AUTH_CONST.__cfstring: 0x2020
   __AUTH_CONST.__objc_const: 0xe00
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x1c8
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x8
-  __DATA.__objc_classrefs: 0x270
-  __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x3f0
+  __DATA.__objc_ivar: 0x3f4
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 980
-  Symbols:   3585
-  CStrings:  2114
+  Functions: 983
+  Symbols:   3593
+  CStrings:  2137
 
Symbols:
+ -[SAMonitoringSession lastAlertDateInCurrentTravelingSession]
+ -[SAMonitoringSession setLastAlertDateInCurrentTravelingSession:]
+ -[SAMonitoringSessionManager checkIfAlertWasTriggeredAtHome:isEarlyVehicularTrigger:]
+ -[SAMonitoringSessionManager checkIfCloseToAnySafeLocations:leftBehindLocation:]
+ -[SAMonitoringSessionManager shouldSuppressDueToRepeatedAlertsInOneTravelingSession:context:]
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table41
+ _OBJC_IVAR_$_SAMonitoringSession._lastAlertDateInCurrentTravelingSession
+ __ZNKSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__117__floyd_sift_downB8ue170006INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__19__sift_upB8ue170006INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ _objc_msgSend$boolValue
+ _objc_msgSend$checkIfAlertWasTriggeredAtHome:isEarlyVehicularTrigger:
+ _objc_msgSend$checkIfCloseToAnySafeLocations:leftBehindLocation:
+ _objc_msgSend$lastAlertDateInCurrentTravelingSession
+ _objc_msgSend$setLastAlertDateInCurrentTravelingSession:
+ _objc_msgSend$shouldSuppressDueToRepeatedAlertsInOneTravelingSession:context:
- GCC_except_table32
- GCC_except_table37
- GCC_except_table42
- GCC_except_table43
- __ZNKSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__117__floyd_sift_downB7v160006INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIU8__strongP11SAAlarmTaskEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIU8__strongP11SAAlarmTaskNS_9allocatorIS3_EEED2B7v160006Ev
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyER19SAAlarmClassCompareNS_11__wrap_iterIPU8__strongP11SAAlarmTaskEEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- __ZSt9terminatev
- ___clang_call_terminate
- ___cxa_begin_catch
- _objc_msgSend$initWithTimestamp:latitude:longitude:horizontalAccuracy:
- _objc_msgSend$setCaLastAlertDate:
CStrings:
+ "\x12)"
+ "B28@0:8@16B24"
+ "Error"
+ "SetupComplete"
+ "T@\"CLCircularRegion\",C,N,V_lastWithYouLocation"
+ "T@\"NSDate\",&,N,V_lastAlertDateInCurrentTravelingSession"
+ "T@\"NSMutableDictionary\",&,N,V_caLastAlertDate"
+ "T@\"NSString\",?,R,C"
+ "_lastAlertDateInCurrentTravelingSession"
+ "boolValue"
+ "checkIfAlertWasTriggeredAtHome:isEarlyVehicularTrigger:"
+ "checkIfCloseToAnySafeLocations:leftBehindLocation:"
+ "closeToAnySafeLocations"
+ "hasSurfacedInCurrentTravelingSession"
+ "isHome"
+ "lastAlertDateInCurrentTravelingSession"
+ "lastAlertRssiValue"
+ "setLastAlertDateInCurrentTravelingSession:"
+ "shouldSuppressDueToRepeatedAlertsInOneTravelingSession:context:"
+ "tSincePriorAlert"
+ "timeSinceLastAlert"
+ "travelingSuppressed"
+ "triggeredAtHome"
+ "unknown"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager checking if alert was triggered at home\", \"location\":\"%{private}@\", \"isEarlyVehicularTrigger\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager checking if close to any safe locations before surfacing the alert\", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager end current traveling session\", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager gating number of alerts in one traveling session \", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager suppressing alerts due to related device alert in current traveling session\", \"uuid\":\"%{private}@\", \"relatedDeviceUUID\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager suppressing alerts due to repeated alerts in one traveling session\", \"uuid\":\"%{private}@\"}"
- "\x12("
- "T@\"NSDate\",&,N,V_caLastAlertDate"
- "T@\"TALocationLite\",C,N,V_lastWithYouLocation"
- "gpsAvailable"
- "initWithTimestamp:latitude:longitude:horizontalAccuracy:"
- "passcodeLocked"
- "reachability"
- "tSincePriorOverallAlert"
- "wifiAvailable"

```
