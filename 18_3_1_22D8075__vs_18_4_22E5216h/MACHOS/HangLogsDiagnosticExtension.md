## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0xa468
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x808
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x15cd
-  __TEXT.__oslogstring: 0x1012
-  __TEXT.__objc_methname: 0x324d
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__objc_methtype: 0x688
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x17a0
-  __DATA_CONST.__objc_classlist: 0x20
+354.2.0.0.0
+  __TEXT.__text: 0xb800
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x994
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x1b09
+  __TEXT.__oslogstring: 0x1123
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__objc_methname: 0x3794
+  __TEXT.__objc_methtype: 0x6bd
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x8d8
+  __DATA_CONST.__cfstring: 0x19e0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1688
-  __DATA.__objc_selrefs: 0x7c0
-  __DATA.__objc_ivar: 0x1ac
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x90
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x1b38
+  __DATA.__objc_selrefs: 0x8c8
+  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x98
   __DATA.__bss: 0xa8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 243
-  Symbols:   320
-  CStrings:  809
+  Functions: 321
+  Symbols:   343
+  CStrings:  907
 
Symbols:
+ _NSLog
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_CLASS_$_HangHistoryRecord
+ _OBJC_CLASS_$_HangIntervalRecord
+ _OBJC_CLASS_$_HangQueryInfo
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_METACLASS_$_HangHistoryRecord
+ _OBJC_METACLASS_$_HangIntervalRecord
+ _OBJC_METACLASS_$_HangQueryInfo
+ __os_log_error_impl
+ _dlopen
+ _formattedFloat
+ _getBiomeForegroundDurations
+ _getHangHistoryDescription
+ _getHangHistoryRecords
+ _getHangIntervalsDescription
+ _getHangQueryInfoDescription
+ _htAddAppForegroundDurations
+ _htCompleteHangHistoryInfo
+ _kHTPrefsAugmentSentryTailspinWithSignposts
+ _kHTPrefsConsecutiveHangWaitTimeoutDurationMSec
+ _kPDSEWBClientHangKillSwitch
+ _kPDSEWBClientHangPeriodDays
+ _objc_alloc
+ _processNameForBundleId
- _getHangHistoryInfo
- _kHTPrefsCollectOSSignpostsDeferred
CStrings:
+ "\n%-20s %5s %15s %10s\n"
+ "\n%-20s %5s %15s %10s %10s %10s\n"
+ "\x11"
+ "!"
+ "\""
+ "%-20s %5d %15s %10s\n"
+ "%-20s %5d %15s %10s %10s %10s\n"
+ "%.01f"
+ "%.03f"
+ "%@"
+ "%@\n%@\n%@"
+ "%d"
+ "%s: event->startTime is greater than endTime, shared memory is most likely corrupted."
+ "%s: nil event passed"
+ "-"
+ "."
+ "/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams"
+ "@\"NSDate\""
+ "BundleIdOverride"
+ "HangHistoryRecord"
+ "HangIntervalRecord"
+ "HangQueryInfo"
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "Rate(s/hr)"
+ "SELECT bundleID, sum(duration) FROM (     SELECT *, end_timestamp-start_timestamp AS duration FROM     (         SELECT bundleID,            CASE WHEN starting=1 THEN eventTimestamp ELSE NULL END AS start_timestamp,            CASE WHEN next_starting=0 THEN next_timestamp                  WHEN starting==0 AND previous_starting==0 THEN next_timestamp ELSE NULL END AS end_timestamp         FROM         (             SELECT bundleID, starting, eventTimestamp, lead(eventTimestamp) OVER win AS next_timestamp, lead(starting) OVER win AS next_starting, lag(starting) OVER win AS previous_starting FROM                 \"App.InFocus\"                 where eventTimestamp > unixepoch(\"now\", \"-%d hours\")                 WINDOW win AS (PARTITION BY bundleID ORDER BY eventTimestamp)         )     ) WHERE         start_timestamp IS NOT NULL OR end_timestamp IS NOT NULL     ORDER BY start_timestamp ) GROUP BY bundleID ORDER BY sum(duration) DESC "
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSString\",&,N,V_beginTimestampString"
+ "T@\"NSString\",&,N,V_processName"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,N,V_intervalCount"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Tf,N,V_foregroundDurationHours"
+ "Tf,N,V_hangDuration"
+ "Tf,N,V_intervalDurationMilliseconds"
+ "Tf,N,V_queryTime"
+ "Tf,N,V_windowLookupTime"
+ "Ti,N,V_hangCount"
+ "Ti,N,V_processId"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "Usage(hr)"
+ "_beginTimestampString"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_foregroundDurationHours"
+ "_hangCount"
+ "_hangDuration"
+ "_intervalCount"
+ "_intervalDurationMilliseconds"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_processId"
+ "_processName"
+ "_queryTime"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "_startDate"
+ "_windowLookupTime"
+ "attributes"
+ "beginTimestampString"
+ "biome lookup failed: %@"
+ "bundleID"
+ "checkForHangWithUserMovedAwayAndRecentAssertions"
+ "componentsSeparatedByString:"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "error"
+ "event->bundleID has been corrupted, final char in array is not \\0. bundleID: %s"
+ "event->serviceName has been corrupted, final char in array is not \\0. serviceName: %s"
+ "executeQuery:"
+ "f"
+ "f16@0:8"
+ "foregroundDurationHours"
+ "hangCount"
+ "hangDuration"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "intervalCount"
+ "intervalDurationMilliseconds"
+ "localizedName"
+ "next"
+ "objectAtIndexedSubscript:"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "processId"
+ "q24@0:8@16"
+ "queryTime"
+ "row"
+ "setBeginTimestampString:"
+ "setForegroundDurationHours:"
+ "setHangCount:"
+ "setHangDuration:"
+ "setIntervalCount:"
+ "setIntervalDurationMilliseconds:"
+ "setProcessId:"
+ "setProcessName:"
+ "setQueryTime:"
+ "setStartDate:"
+ "setWindowLookupTime:"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "startDate"
+ "stringWithCString:encoding:"
+ "sum(duration)"
+ "v20@0:8f16"
+ "v24@0:8Q16"
+ "v32@?0@\"NSString\"8@\"HangHistoryRecord\"16^B24"
+ "windowLookupTime"
+ "\xf0\xf0A!&!"
- "\n%-15s %5s %15s %10s\n"
- "%-15s %5d %15.0f %10.0f\n"
- "Retrieval time per window min %@ max %@ mean %@\n"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "numberWithFloat:"
- "objectForKey:"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11&!"

```
