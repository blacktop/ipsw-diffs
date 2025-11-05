## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/Versions/A/ViceroyTrace`

```diff

-2100.5.1.0.0
-  __TEXT.__text: 0x9f3bc
+2105.10.1.0.0
+  __TEXT.__text: 0xa1330
   __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0x8204
-  __TEXT.__const: 0x21b8
-  __TEXT.__cstring: 0xcc2c
-  __TEXT.__oslogstring: 0xbeac
-  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__objc_methlist: 0x85a0
+  __TEXT.__const: 0x21a0
+  __TEXT.__cstring: 0xccd7
+  __TEXT.__oslogstring: 0xc169
+  __TEXT.__gcc_except_tab: 0x354
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__unwind_info: 0x14e8
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x19b49
-  __TEXT.__objc_methtype: 0x20e3
-  __TEXT.__objc_stubs: 0xdd20
+  __TEXT.__objc_methname: 0x19c3b
+  __TEXT.__objc_methtype: 0x20f0
+  __TEXT.__objc_stubs: 0xdda0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__const: 0x4c0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3dc0
+  __DATA_CONST.__objc_selrefs: 0x3e58
   __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0x200
+  __DATA_CONST.__objc_arraydata: 0x210
   __AUTH_CONST.__auth_got: 0x618
   __AUTH_CONST.__const: 0xb30
-  __AUTH_CONST.__cfstring: 0xcc60
-  __AUTH_CONST.__objc_const: 0x158c8
+  __AUTH_CONST.__cfstring: 0xcd40
+  __AUTH_CONST.__objc_const: 0x15360
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1090
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x1e14
-  __DATA.__data: 0x618
+  __DATA.__objc_ivar: 0x1e28
+  __DATA.__data: 0x628
   __DATA.__bss: 0xb8
   __DATA.__common: 0x23
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D4EFCE40-E002-3F76-857D-32DF7D273086
-  Functions: 3517
-  Symbols:   8236
-  CStrings:  8543
+  UUID: 9AC48F1D-9FFA-3CE6-B800-B22EB8CC0B91
+  Functions: 3729
+  Symbols:   8512
+  CStrings:  8580
 
Symbols:
+ -[RTCReportingAgent collectTelemetryForService:payload:lock:].cold.2
+ -[RTCReportingAgent collectTelemetryForService:payload:lock:].cold.3
+ -[RTCReportingAgent collectTelemetryForService:payload:lock:].cold.4
+ -[RTCReportingAgent createSecondAggregatorWithOptions:].cold.2
+ -[RTCReportingAgent createSecondAggregatorWithOptions:].cold.3
+ -[RTCReportingAgent getUserInfoFromReportingConfiguration:].cold.1
+ -[RTCReportingAgent registerPeriodicTaskForModule:needToUpdate:needToReport:serviceBlock:].cold.1
+ -[RTCReportingAgent reportPeriodicTelemetryWithCategory:type:payload:lock:].cold.1
+ -[RTCReportingAgent reportPeriodicTelemetryWithCategory:type:payload:lock:].cold.2
+ -[RTCReportingAgent setUpWeeklyRotatingID].cold.3
+ -[RTCReportingAgent telemetryUpdate:updateTimeout:].cold.3
+ -[RTCReportingAgent telemetryUpdate:updateTimeout:].cold.4
+ -[UplinkSegment segmentReportingMode]
+ -[UplinkSegment setSegmentReportingMode:]
+ -[VCAggregator isApplePersonalHotspotAndUpdatePhyMode].cold.4
+ -[VCAggregator isApplePersonalHotspotAndUpdatePhyMode].cold.5
+ -[VCAggregator phyModeFromWifiInterface:].cold.1
+ -[VCAggregator phyModeFromWifiInterface:].cold.2
+ -[VCAggregatorAirPlay aggregatedSessionReport]
+ -[VCAggregatorAudioStream aggregatedCallReport].cold.1
+ -[VCAggregatorMultiway addSessionOperatingModeForCallReport:]
+ -[VCAggregatorMultiway processSliceStatusABCSymptoms:currentSegmentName:]
+ -[VCAggregatorMultiway updateOperatingMode:]
+ -[VCAggregatorMultiway updateOperatingMode:].cold.1
+ -[VCAlgosStreamingScorer addCallFailureWithTime:detailedErrorCode:].cold.1
+ -[VCAlgosStreamingScorer addLargeGapErasureWithTime:largeGapErasureRate:].cold.1
+ -[VCAlgosStreamingScorer addStreamTierSwitchWithTime:].cold.1
+ -[VCAlgosStreamingScorer addVideoStallWithStartTime:endStallTime:].cold.1
+ -[VCAlgosStreamingScorer endWithTime:streamType:].cold.1
+ -[VCAlgosStreamingScorer endWithTime:streamType:].cold.2
+ -[VCAlgosStreamingScorer scoreStreaming].cold.1
+ -[VCAlgosStreamingScorer startWithTime:streamType:].cold.1
+ -[VCAlgosStreamingScorer startWithTime:streamType:].cold.2
+ -[VCAlgosStreamingScorer stopWithTime:streamType:].cold.1
+ -[VCAlgosStreamingScorer stopWithTime:streamType:].cold.2
+ -[VCAlgosStreamingScorer stopWithTime:streamType:].cold.3
+ -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.12
+ -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.13
+ -[VCPersistentDataStore initWithIdentifier:dataCollectionEnabled:].cold.14
+ -[VCSymptomReporter reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary:]
+ GCC_except_table223
+ GCC_except_table224
+ OBJC_IVAR_$_UplinkSegment._segmentReportingMode
+ OBJC_IVAR_$_VCAggregatorHomeKitVideo._connectionType
+ OBJC_IVAR_$_VCAggregatorMultiway._audioOnlyModeDuration
+ OBJC_IVAR_$_VCAggregatorMultiway._callStartReportingMode
+ OBJC_IVAR_$_VCAggregatorMultiway._currentReportingMode
+ VCDiskUtils_FileZipToFile.cold.1
+ VCDiskUtils_FileZipToFile.cold.2
+ VCDiskUtils_FileZipToFile.cold.3
+ VRTraceSetErrorLogLevel.cold.1
+ VRTraceSetErrorLogLevelForModule.cold.1
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _VCPersistentDataStore_BindAndExecute.cold.10
+ _VCPersistentDataStore_BindAndExecute.cold.11
+ _VCPersistentDataStore_BindAndExecute.cold.12
+ _VCPersistentDataStore_BindAndExecute.cold.13
+ _VCPersistentDataStore_BindAndExecute.cold.14
+ _VCPersistentDataStore_BindAndExecute.cold.15
+ _VCPersistentDataStore_BindAndExecute.cold.16
+ _VCPersistentDataStore_BindAndExecute.cold.17
+ _VCPersistentDataStore_BindAndExecute.cold.18
+ _VCPersistentDataStore_BindAndExecute.cold.19
+ _VCPersistentDataStore_BindAndExecute.cold.20
+ _VCPersistentDataStore_BindAndExecute.cold.21
+ _VCPersistentDataStore_BindAndExecute.cold.22
+ _VCPersistentDataStore_BindAndExecute.cold.23
+ _VCPersistentDataStore_BindAndExecute.cold.24
+ _VCPersistentDataStore_BindAndExecute.cold.25
+ _VCPersistentDataStore_BindAndExecute.cold.26
+ _VCPersistentDataStore_BindAndExecute.cold.27
+ _VCPersistentDataStore_BindAndExecute.cold.28
+ _VCPersistentDataStore_BindAndExecute.cold.29
+ _VCPersistentDataStore_BindAndExecute.cold.30
+ _VCPersistentDataStore_BindAndExecute.cold.31
+ _VCPersistentDataStore_BindAndExecute.cold.32
+ _VCPersistentDataStore_BindAndExecute.cold.33
+ _VCPersistentDataStore_BindAndExecute.cold.34
+ _VCPersistentDataStore_BindAndExecute.cold.35
+ _VCPersistentDataStore_BindAndExecute.cold.36
+ _VCPersistentDataStore_BindAndExecute.cold.37
+ _VCPersistentDataStore_BindAndExecute.cold.38
+ _VCPersistentDataStore_BindAndExecute.cold.39
+ _VCPersistentDataStore_BindAndExecute.cold.40
+ _VCPersistentDataStore_BindAndExecute.cold.41
+ _VCPersistentDataStore_BindAndExecute.cold.42
+ _VCPersistentDataStore_BindAndExecute.cold.43
+ _VCPersistentDataStore_BindAndExecute.cold.44
+ _VCPersistentDataStore_BindAndExecute.cold.45
+ _VCPersistentDataStore_BindAndExecute.cold.46
+ _VCPersistentDataStore_BindAndExecute.cold.47
+ _VCPersistentDataStore_BindAndExecute.cold.48
+ _VCPersistentDataStore_BindAndExecute.cold.49
+ _VCPersistentDataStore_BindAndExecute.cold.50
+ _VCPersistentDataStore_BindAndExecute.cold.51
+ _VCPersistentDataStore_BindAndExecute.cold.52
+ _VCPersistentDataStore_BindAndExecute.cold.53
+ _VCPersistentDataStore_BindAndExecute.cold.54
+ _VCPersistentDataStore_BindAndExecute.cold.55
+ _VCPersistentDataStore_BindAndExecute.cold.56
+ _VCPersistentDataStore_BindAndExecute.cold.57
+ _VCPersistentDataStore_BindAndExecute.cold.58
+ _VCPersistentDataStore_BindAndExecute.cold.59
+ _VCPersistentDataStore_BindAndExecute.cold.6
+ _VCPersistentDataStore_BindAndExecute.cold.60
+ _VCPersistentDataStore_BindAndExecute.cold.61
+ _VCPersistentDataStore_BindAndExecute.cold.62
+ _VCPersistentDataStore_BindAndExecute.cold.63
+ _VCPersistentDataStore_BindAndExecute.cold.64
+ _VCPersistentDataStore_BindAndExecute.cold.65
+ _VCPersistentDataStore_BindAndExecute.cold.66
+ _VCPersistentDataStore_BindAndExecute.cold.67
+ _VCPersistentDataStore_BindAndExecute.cold.68
+ _VCPersistentDataStore_BindAndExecute.cold.69
+ _VCPersistentDataStore_BindAndExecute.cold.7
+ _VCPersistentDataStore_BindAndExecute.cold.70
+ _VCPersistentDataStore_BindAndExecute.cold.71
+ _VCPersistentDataStore_BindAndExecute.cold.72
+ _VCPersistentDataStore_BindAndExecute.cold.73
+ _VCPersistentDataStore_BindAndExecute.cold.74
+ _VCPersistentDataStore_BindAndExecute.cold.75
+ _VCPersistentDataStore_BindAndExecute.cold.76
+ _VCPersistentDataStore_BindAndExecute.cold.77
+ _VCPersistentDataStore_BindAndExecute.cold.78
+ _VCPersistentDataStore_BindAndExecute.cold.79
+ _VCPersistentDataStore_BindAndExecute.cold.8
+ _VCPersistentDataStore_BindAndExecute.cold.80
+ _VCPersistentDataStore_BindAndExecute.cold.81
+ _VCPersistentDataStore_BindAndExecute.cold.82
+ _VCPersistentDataStore_BindAndExecute.cold.83
+ _VCPersistentDataStore_BindAndExecute.cold.84
+ _VCPersistentDataStore_BindAndExecute.cold.85
+ _VCPersistentDataStore_BindAndExecute.cold.86
+ _VCPersistentDataStore_BindAndExecute.cold.87
+ _VCPersistentDataStore_BindAndExecute.cold.9
+ __51-[RTCReportingAgent unregisterPeriodTaskForModule:]_block_invoke.cold.1
+ __64-[VCAggregatorMultiway processSessionInitWithPayload:timestamp:]_block_invoke.5350
+ __81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.166
+ __81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.cold.2
+ __MergedGlobals
+ __OBJC_$_INSTANCE_VARIABLES_VCAggregatorHomeKitVideo
+ ___76-[VCAggregatorHomeKitVideo dispatchedProcessEventWithCategory:type:payload:]_block_invoke
+ __block_literal_global.453
+ __block_literal_global.463
+ __block_literal_global.555
+ __reportingSetUserInfo_block_invoke.459
+ __reportingSetUserInfo_block_invoke.460
+ __reportingSetUserInfo_block_invoke.460.cold.1
+ _objc_msgSend$addSessionOperatingModeForCallReport:
+ _objc_msgSend$processSliceStatusABCSymptoms:currentSegmentName:
+ _objc_msgSend$reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary:
+ _objc_msgSend$segmentReportingMode
+ _objc_msgSend$setSegmentReportingMode:
+ _objc_msgSend$updateOperatingMode:
+ _reportingSessionModeFromOperatingMode
+ _sRTCReportingSafeViewScreenSharingClientName
+ _sRTCReportingSafeViewSystemAudioSharingClientName
+ machTimeScale.cold.1
+ reportingSessionModeFromOperatingMode.cold.1
- -[MultiwayCall incrementCallDuration].cold.1
- -[VCAggregatorFaceTime updateAudioTxStatsWithPayload:].cold.1
- -[VCAggregatorHomeKitAudio initWithDelegate:].cold.3
- -[VCAggregatorMultiway calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:].cold.1
- -[VCAggregatorMultiway calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:].cold.2
- -[VCAggregatorMultiway processSliceStatusABCSymptoms:]
- -[VCAggregatorMultiway updateAudioCodecAndMediaBitrate:currentTime:].cold.1
- -[VCAggregatorMultiway updateNetworkCapabilities:type:].cold.1
- -[VCAggregatorMultiway updateNetworkCapabilities:type:].cold.2
- -[VCAggregatorMultiway updateNetworkCapabilities:type:].cold.3
- -[VCAggregatorMultiway updateTotalConnectionTime:].cold.1
- -[VCDataMLEnhance init].cold.4
- -[VCReportingCommon init].cold.3
- -[VCReportingDeltaDistribution initWithSignedHistogramType:reportingKeys:].cold.2
- -[VCSignedHistogram initWithType:bucketValues:].cold.3
- -[VCSymptomReporter reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary]
- __64-[VCAggregatorMultiway processSessionInitWithPayload:timestamp:]_block_invoke.5336
- __81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.163
- __block_literal_global.450
- __block_literal_global.460
- __block_literal_global.552
- __reportingSetUserInfo_block_invoke.456
- __reportingSetUserInfo_block_invoke.457
- __reportingSetUserInfo_block_invoke.457.cold.1
- _objc_msgSend$processSliceStatusABCSymptoms:
- _objc_msgSend$reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary
- machTimeScale.did_init
- machTimeScale.timeScale
CStrings:
+ " [%s] %s:%d %@(%p) Changed reportingMode=%d"
+ " [%s] %s:%d %@(%p) Created database file with databasePath=%@"
+ " [%s] %s:%d %@(%p) Deleted database with databasePath=%@"
+ " [%s] %s:%d %@(%p) Failed to initialize SQLite database with path=%@"
+ " [%s] %s:%d %@(%p) Received operatingMode=%d which is not a valid VCSessionReportingMode"
+ " [%s] %s:%d %@(%p) Starting reportingMode=%d"
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
+ " [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
+ " [%s] %s:%d Changed reportingMode=%d"
+ " [%s] %s:%d Created database file with databasePath=%@"
+ " [%s] %s:%d Deleted database with databasePath=%@"
+ " [%s] %s:%d Failed to initialize SQLite database with path=%@"
+ " [%s] %s:%d Received operatingMode=%d which is not a valid VCSessionReportingMode"
+ " [%s] %s:%d Starting reportingMode=%d"
+ "-[VCAggregatorMultiway updateOperatingMode:]"
+ "-[VCSymptomReporter reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary:]"
+ "ADRTN"
+ "CallConnectionTime"
+ "HKCT"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
+ "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."
+ "ReportingVC [%s] %s:%d Could not find directory path"
+ "ReportingVC [%s] %s:%d Invalid operating mode for VCSession=%d"
+ "SEOPMODE"
+ "SSOPMODE"
+ "SafeViewScreenShare"
+ "TC,V_segmentReportingMode"
+ "VCMSConnectionType"
+ "_audioOnlyModeDuration"
+ "_callStartReportingMode"
+ "_currentReportingMode"
+ "_segmentReportingMode"
+ "addSessionOperatingModeForCallReport:"
+ "processSliceStatusABCSymptoms:currentSegmentName:"
+ "reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary:"
+ "reportingSessionModeFromOperatingMode"
+ "segmentReportingMode"
+ "setSegmentReportingMode:"
+ "updateOperatingMode:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
- " [%s] %s:%d %@(%p) Failed to initialize SQLite database"
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending deflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error ending inflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing deflate."
- " [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/Utilities/CompressionUtils.c:%d: Error initializing inflate."
- " [%s] %s:%d Failed to initialize SQLite database"
- "-[VCSymptomReporter reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary]"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: %s: CFBundleVersion for RTCReporting class returned nil. Defaulting it to 'Unknown'"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Agent is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: Init time userInfo=%@"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(%s): agent is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC(_validateClassAndSymbols): class or symbol don't exist."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: ReportingVC: error code=%d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: SymptomReporter: Couldn't find group symptomID, message=%@"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: _reportingVCRunOnce: can't load framework."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: algosScoreDictionary is nil"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: eventType:%d error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: flushMessages: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: recipientUUID == NULL"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingAWDCallStart: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingCancelLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnecting: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingConnectionType: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final DTX stats"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingDisconnected: error code %d while sending final call stats"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingError: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingGetDefaults: pointers can't be NULL"
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingHandoverResult: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLocalAndRemoteInterface: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingModeRoleTransportLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingMomentsEvents: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingPerfTimes: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingRemoteFrameSize: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingThermal: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingTierLog: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoPaused: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVideoProp: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingVisualRectangle: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallEnd: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogCallStart: error code %d."
- "ReportingVC [%s] %s:%d /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVConference/ViceroyTrace.subproj/Sources/ReportingVC.m:%d: reportingWiFiCallingLogMetricSample: error code %d."
- "processSliceStatusABCSymptoms:"
- "reportNoVideoDisplayedFailSafeFIRWithOptionalDictionary"
- "v24@0:8@\"NSString\"16"

```
