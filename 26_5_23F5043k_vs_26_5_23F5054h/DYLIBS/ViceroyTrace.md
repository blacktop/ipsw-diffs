## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2195.5.1.0.0
-  __TEXT.__text: 0xa8790
+2205.1.1.0.0
+  __TEXT.__text: 0xa9070
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8eb8
-  __TEXT.__const: 0x24e8
-  __TEXT.__cstring: 0xeb43
+  __TEXT.__objc_methlist: 0x8fa8
+  __TEXT.__const: 0x2518
+  __TEXT.__cstring: 0xeb88
   __TEXT.__oslogstring: 0xd0ea
   __TEXT.__gcc_except_tab: 0x3dc
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1730
+  __TEXT.__unwind_info: 0x1738
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1c2ec
+  __TEXT.__objc_methname: 0x1c6a0
   __TEXT.__objc_methtype: 0x24b9
-  __TEXT.__objc_stubs: 0xf0c0
+  __TEXT.__objc_stubs: 0xf2e0
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xdc8
+  __DATA_CONST.__const: 0xdd0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43b8
+  __DATA_CONST.__objc_selrefs: 0x4440
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdfc0
-  __AUTH_CONST.__objc_const: 0x16b08
+  __AUTH_CONST.__cfstring: 0xe0c0
+  __AUTH_CONST.__objc_const: 0x16db8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x205c
+  __DATA.__objc_ivar: 0x209c
   __DATA.__data: 0x738
   __DATA.__bss: 0x78
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 36474F09-EE32-3A25-BE33-70EE2BF35A37
-  Functions: 4083
-  Symbols:   13512
-  CStrings:  9342
+  UUID: CA2995D1-27C5-33F5-9B53-813A879788D6
+  Functions: 4107
+  Symbols:   13594
+  CStrings:  9392
 
Symbols:
+ -[DownlinkSegment _processAltVideoStallStreamData:streamGroupStats:]
+ -[DownlinkSegment averagePercentageOfDTX]
+ -[DownlinkSegment percentageOfDTX]
+ -[DownlinkSegment processPercentageOfDTXValue:]
+ -[DownlinkSegment setAveragePercentageOfDTX:]
+ -[MultiwayStream _processAltVideoStallPayload:]
+ -[MultiwayStream averagePercentageOfDTXCounter]
+ -[MultiwayStream averagePercentageOfDTXSum]
+ -[MultiwayStream currentStallTimeAlt]
+ -[MultiwayStream maxVideoStallCountAlt]
+ -[MultiwayStream percentageOfDTX]
+ -[MultiwayStream totalVideoStallTimeAlt]
+ -[StreamGroupStats currentStallTimeAlt]
+ -[StreamGroupStats lastReceivedVideoStallTimeAlt]
+ -[StreamGroupStats maxVideoStallCountAlt]
+ -[StreamGroupStats setCurrentStallTimeAlt:]
+ -[StreamGroupStats setLastReceivedVideoStallTimeAlt:]
+ -[StreamGroupStats setMaxVideoStallCountAlt:]
+ -[StreamGroupStats setVideoStalledTotalTimeAlt:]
+ -[StreamGroupStats videoStalledTotalTimeAlt]
+ GCC_except_table1307
+ _OBJC_IVAR_$_DownlinkSegment._averagePercentageOfDTX
+ _OBJC_IVAR_$_DownlinkSegment._averagePercentageOfDTXCounter
+ _OBJC_IVAR_$_DownlinkSegment._averagePercentageOfDTXSum
+ _OBJC_IVAR_$_DownlinkSegment._percentageOfDTX
+ _OBJC_IVAR_$_MultiwayStream._averagePercentageOfDTXCounter
+ _OBJC_IVAR_$_MultiwayStream._averagePercentageOfDTXSum
+ _OBJC_IVAR_$_MultiwayStream._currentStallTimeAlt
+ _OBJC_IVAR_$_MultiwayStream._lastReceivedVideoStallTimeAlt
+ _OBJC_IVAR_$_MultiwayStream._maxVideoStallCountAlt
+ _OBJC_IVAR_$_MultiwayStream._percentageOfDTX
+ _OBJC_IVAR_$_MultiwayStream._totalVideoStallTimeAlt
+ _OBJC_IVAR_$_StreamGroupStats._currentStallTimeAlt
+ _OBJC_IVAR_$_StreamGroupStats._lastReceivedVideoStallTimeAlt
+ _OBJC_IVAR_$_StreamGroupStats._maxVideoStallCountAlt
+ _OBJC_IVAR_$_StreamGroupStats._videoStalledTotalTimeAlt
+ _OBJC_IVAR_$_VCAggregator._averagePercentageOfDTX
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _objc_msgSend$_processAltVideoStallPayload:
+ _objc_msgSend$_processAltVideoStallStreamData:streamGroupStats:
+ _objc_msgSend$averagePercentageOfDTX
+ _objc_msgSend$averagePercentageOfDTXCounter
+ _objc_msgSend$averagePercentageOfDTXSum
+ _objc_msgSend$currentStallTimeAlt
+ _objc_msgSend$lastReceivedVideoStallTimeAlt
+ _objc_msgSend$maxVideoStallCountAlt
+ _objc_msgSend$percentageOfDTX
+ _objc_msgSend$processPercentageOfDTXValue:
+ _objc_msgSend$setAveragePercentageOfDTX:
+ _objc_msgSend$setCurrentStallTimeAlt:
+ _objc_msgSend$setLastReceivedVideoStallTimeAlt:
+ _objc_msgSend$setMaxVideoStallCountAlt:
+ _objc_msgSend$setVideoStalledTotalTimeAlt:
+ _objc_msgSend$totalVideoStallTimeAlt
+ _objc_msgSend$videoStalledTotalTimeAlt
+ _percentageBucketRanges
- GCC_except_table1287
CStrings:
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
+ "AVPEROFDTX"
+ "PODTX"
+ "PercentageOfDTX"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/7142D0D5-BB9C-4809-A6C8-307A41E450B7/TemporaryDirectory.ovE73p/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."
+ "SAPODTX"
+ "T@\"VCReportingHistogram\",R,V_percentageOfDTX"
+ "TI,V_maxVideoStallCountAlt"
+ "TQ,R,V_averagePercentageOfDTXCounter"
+ "TQ,V_averagePercentageOfDTX"
+ "TVST_A"
+ "Td,R,V_averagePercentageOfDTXSum"
+ "Td,V_currentStallTimeAlt"
+ "Td,V_lastReceivedVideoStallTimeAlt"
+ "Td,V_videoStalledTotalTimeAlt"
+ "VSP_A"
+ "VSTCNT_A"
+ "VST_A"
+ "_averagePercentageOfDTX"
+ "_averagePercentageOfDTXCounter"
+ "_averagePercentageOfDTXSum"
+ "_currentStallTimeAlt"
+ "_lastReceivedVideoStallTimeAlt"
+ "_maxVideoStallCountAlt"
+ "_percentageOfDTX"
+ "_processAltVideoStallPayload:"
+ "_processAltVideoStallStreamData:streamGroupStats:"
+ "_totalVideoStallTimeAlt"
+ "_videoStalledTotalTimeAlt"
+ "averagePercentageOfDTX"
+ "averagePercentageOfDTXCounter"
+ "averagePercentageOfDTXSum"
+ "currentStallTimeAlt"
+ "lastReceivedVideoStallTimeAlt"
+ "maxVideoStallCountAlt"
+ "percentageOfDTX"
+ "processPercentageOfDTXValue:"
+ "setAveragePercentageOfDTX:"
+ "setCurrentStallTimeAlt:"
+ "setLastReceivedVideoStallTimeAlt:"
+ "setMaxVideoStallCountAlt:"
+ "setVideoStalledTotalTimeAlt:"
+ "totalVideoStallTimeAlt"
+ "videoStalledTotalTimeAlt"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
- " [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType=%d error code=%d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
- "ReportingVC [%s] %s:%d /Library/Caches/com.apple.xbs/2689C490-EFFF-40F7-8514-5303DEA24BAA/TemporaryDirectory.hZYyrW/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."

```
