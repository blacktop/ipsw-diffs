## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-94.40.1.0.0
-  __TEXT.__text: 0x1da44
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x2360
-  __TEXT.__objc_methlist: 0x1138
-  __TEXT.__cstring: 0x153e
-  __TEXT.__objc_classname: 0x2d5
-  __TEXT.__objc_methtype: 0x506
+97.0.0.0.0
+  __TEXT.__text: 0x1f0b0
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_stubs: 0x2640
+  __TEXT.__objc_methlist: 0x11b0
+  __TEXT.__cstring: 0x17d6
+  __TEXT.__objc_classname: 0x2d7
+  __TEXT.__objc_methtype: 0x54a
   __TEXT.__const: 0x1d8
-  __TEXT.__oslogstring: 0x2baa
-  __TEXT.__objc_methname: 0x2c83
-  __TEXT.__gcc_except_tab: 0x18c
-  __TEXT.__unwind_info: 0x4c8
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x6b8
-  __DATA_CONST.__cfstring: 0x1de0
+  __TEXT.__oslogstring: 0x3035
+  __TEXT.__objc_methname: 0x2f49
+  __TEXT.__gcc_except_tab: 0x184
+  __TEXT.__unwind_info: 0x500
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__cfstring: 0x2020
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__objc_arraydata: 0x378
-  __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA_CONST.__objc_intobj: 0x558
+  __DATA_CONST.__objc_arraydata: 0x390
+  __DATA_CONST.__objc_arrayobj: 0x2a0
+  __DATA_CONST.__objc_intobj: 0x5a0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3b28
-  __DATA.__objc_selrefs: 0xa48
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_const: 0x3b88
+  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x188
   __DATA.__bss: 0x150

   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 565
-  Symbols:   184
-  CStrings:  1171
+  Functions: 592
+  Symbols:   190
+  CStrings:  1243
 
Symbols:
+ _OBJC_CLASS_$__CDClientContext
+ _OBJC_CLASS_$__CDContextQueries
+ _OBJC_CLASS_$__CDContextualChangeRegistration
+ _OBJC_CLASS_$__CDContextualPredicate
+ _PLQueryRegistered
+ _clock_gettime
CStrings:
+ "\x03"
+ "(subsystem == %!@(MISSING) AND category == %!@(MISSING))"
+ "@\"<_CDContext>\""
+ "@\"_CDContextualChangeRegistration\""
+ "@40@0:8@16@24Q32"
+ "CA metrics have been computed once for the current charging session.\n"
+ "Can compute core analytics metrics between:\nplugInMonotonicTimeInSeconds - %!l(MISSING)lu\ncurrentMonotonicTimeInSeconds - %!l(MISSING)lu\ntimeDifferenceInSeconds - %!f(MISSING)"
+ "Cannot compute core analytics metrics as we do not know plugin time:\ncurrentMonotonicTimeInSeconds - %!l(MISSING)lu\npluginMonotonicTimeInSeconds - %!l(MISSING)lu"
+ "Cannot compute core analytics metrics:\ncurrentMonotonicTimeInSeconds - %!l(MISSING)lu\npluginMonotonicTimeInSeconds- %!l(MISSING)lu\ntimeDifferenceInSeconds- %!f(MISSING)"
+ "Computing metrics for event #%!@(MISSING): %!@(MISSING)"
+ "Context store or context store registration not set!"
+ "Deregistering from context store!"
+ "Dictionary sent to CA for event %!@(MISSING): %!@(MISSING)"
+ "Getting data from PPS for the following inputs:\ndateFrom - %!@(MISSING), dateTill - %!@(MISSING), interval - %!@(MISSING)"
+ "Invalid SOC: %!@(MISSING)"
+ "IsWireless"
+ "Not computing CA metrics at plugout. UI SOC at plugout: %!d(MISSING)"
+ "PPS Response length: %!l(MISSING)u"
+ "Registered to context store."
+ "Registration info within CD context store handler: %!@(MISSING), %!@(MISSING)"
+ "SELF.%!@(MISSING).value.externalConnected = %!@(MISSING) AND SELF.%!@(MISSING).value = %!@(MISSING)"
+ "SOC value of %!@(MISSING) is < 0"
+ "SOC value of %!@(MISSING) is > 100"
+ "T@\"<_CDContext>\",&,N,V_context"
+ "T@\"_CDContextualChangeRegistration\",&,N,V_contextStoreRegistration"
+ "Unable to compute the CA metrics as SMC data is not available."
+ "Unable to compute the CA metrics as we did not receive a response from PPS."
+ "XPCCacheFlush"
+ "_context"
+ "_contextStoreRegistration"
+ "binSizeInMinutes should be > 0."
+ "boolForKey:"
+ "caMetricsComputed"
+ "canComputeCoreAnalyticsMetrics"
+ "com.apple.batteryintelligence.timeto80listener"
+ "com.apple.batteryintelligence.tt80-listener"
+ "com.apple.batteryintelligenced.contextstore-registration"
+ "com.apple.batteryintelligenced.tt80listener.contextstore-handler"
+ "com.apple.bi.tt80_predictions"
+ "computeAndSendCoreAnalyticsMetrics"
+ "context"
+ "contextStoreRegistration"
+ "deregisterCallback:"
+ "deregisterFromContextStoreNotification"
+ "duration"
+ "getModelID"
+ "getSOCBin"
+ "getTT80EstimatesFromDate:toDate:limit:"
+ "getTimeIntervalBin"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "is_wireless"
+ "keyPathForBatteryLevel"
+ "keyPathForBatteryStateDataDictionary"
+ "localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
+ "monotonicPluginTimeInSeconds"
+ "numberWithLongLong:"
+ "predicateForKeyPath:withFormat:"
+ "prediction_error_absolute_in_mins"
+ "prediction_error_in_mins"
+ "registerCallback:"
+ "setBool:forKey:"
+ "setContext:"
+ "setContextStoreRegistration:"
+ "setUpContextStoreRegistration"
+ "short_charging_session"
+ "short_charging_session_predicted"
+ "start_soc_bin"
+ "time_of_prediction_offset_bin"
+ "under_predicted"
+ "userContext"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"

```
