## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2205.1.1.0.0
-  __TEXT.__text: 0xa9070
+2205.2.1.0.0
+  __TEXT.__text: 0xa929c
   __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_methlist: 0x8fa8
   __TEXT.__const: 0x2518
-  __TEXT.__cstring: 0xeb88
+  __TEXT.__cstring: 0xebf5
   __TEXT.__oslogstring: 0xd0ea
   __TEXT.__gcc_except_tab: 0x3dc
   __TEXT.__dlopen_cstrs: 0xa0
   __TEXT.__unwind_info: 0x1738
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1c6a0
+  __TEXT.__objc_methname: 0x1c710
   __TEXT.__objc_methtype: 0x24b9
   __TEXT.__objc_stubs: 0xf2e0
   __DATA_CONST.__got: 0x238

   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xe0c0
-  __AUTH_CONST.__objc_const: 0x16db8
+  __AUTH_CONST.__cfstring: 0xe200
+  __AUTH_CONST.__objc_const: 0x16e78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x209c
+  __DATA.__objc_ivar: 0x20b4
   __DATA.__data: 0x738
   __DATA.__bss: 0x78
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CA2995D1-27C5-33F5-9B53-813A879788D6
+  UUID: 1745E94B-15A1-3C90-B9F1-956062D6D6B8
   Functions: 4107
-  Symbols:   13594
-  CStrings:  9392
+  Symbols:   13600
+  CStrings:  9418
 
Symbols:
+ _OBJC_IVAR_$_VCAggregatorMultiway._dupWRMWaitCount
+ _OBJC_IVAR_$_VCAggregatorMultiway._dupWRMWaitSumMs
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmCachedCount
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmCellExpensiveCount
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmImmediateCount
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmUserMovingCount
Functions:
~ ___47-[VCAggregatorMultiway aggregatedSessionReport]_block_invoke : 12472 -> 12776
~ ___49-[VCAggregatorMultiway updateWRMMetrics:payload:]_block_invoke : 1356 -> 1536
~ ___62-[VCAggregatorMultiway processEventWithCategory:type:payload:]_block_invoke : 8800 -> 8872
CStrings:
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
+ "DUPWRMWT"
+ "DUPWRMWTAVG"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/13BAA429-5F6D-4C5E-96D8-42A952A83E04/TemporaryDirectory.ZDUZuN/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."
+ "WRMCACH"
+ "WRMCACHCNT"
+ "WRMCACHNODUPSTARTCNT"
+ "WRMIMMCNT"
+ "WRMUMOV"
+ "WRMUMOVCNT"
+ "WRMXPNS"
+ "WRMXPNSCNT"
+ "_dupWRMWaitCount"
+ "_dupWRMWaitSumMs"
+ "_wrmCachedCount"
+ "_wrmCellExpensiveCount"
+ "_wrmImmediateCount"
+ "_wrmUserMovingCount"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."

```
