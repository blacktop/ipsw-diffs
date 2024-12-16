## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2090.17.2.0.0
-  __TEXT.__text: 0x9ea04
+2100.3.1.0.0
+  __TEXT.__text: 0x9fde8
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x8114
-  __TEXT.__const: 0x2208
-  __TEXT.__cstring: 0xcb9e
-  __TEXT.__oslogstring: 0xb3a2
+  __TEXT.__objc_methlist: 0x820c
+  __TEXT.__const: 0x2278
+  __TEXT.__cstring: 0xcde5
+  __TEXT.__oslogstring: 0xb4ef
   __TEXT.__gcc_except_tab: 0x350
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1300
+  __TEXT.__unwind_info: 0x1328
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x196f6
-  __TEXT.__objc_methtype: 0x20bb
-  __TEXT.__objc_stubs: 0xd980
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xd18
+  __TEXT.__objc_methname: 0x19b53
+  __TEXT.__objc_methtype: 0x2100
+  __TEXT.__objc_stubs: 0xdd00
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xd20
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ce0
+  __DATA_CONST.__objc_selrefs: 0x3dc0
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x200
   __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xcc00
-  __AUTH_CONST.__objc_const: 0x156c8
+  __AUTH_CONST.__cfstring: 0xcdc0
+  __AUTH_CONST.__objc_const: 0x158e8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0x1de0
+  __DATA.__objc_ivar: 0x1e18
   __DATA.__data: 0x638
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3479
-  Symbols:   3876
-  CStrings:  6856
+  Functions: 3506
+  Symbols:   3906
+  CStrings:  6932
 
Symbols:
+ _OBJC_CLASS_$_NSCalendar
CStrings:
+ " [%s] %s:%d Already reported"
+ " [%s] %s:%d Supplied status has no value"
+ " [%s] %s:%d SymptomReporter: reporting symptom on connection Slice status for callID=%u symptomID=%d"
+ "+[VCDiskUtils createDefaultDirectoryIfNeeded:]"
+ "-[RTCReportingAgent directoryPathForWeeklyIDCache]"
+ "-[RTCReportingAgent setAndSaveWeeklyID:currentWeek:currentYear:cachePath:]"
+ "-[RTCReportingAgent setUpWeeklyRotatingID]"
+ "-[VCAggregatorMultiway calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:]"
+ "-[VCAggregatorMultiway checkSliceStatus:hasValuesOnlyForStatus:]"
+ "-[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]"
+ "-[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]"
+ "-[VCSymptomReporter reportConnectionSliceStatus:]"
+ "@28@0:8i16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}20"
+ "@32@0:8@16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}24"
+ "ABBDP"
+ "APBBD"
+ "B28@0:8@16i24"
+ "B40@0:8@16q24q32"
+ "BBNOTENW"
+ "BBNWP"
+ "DUID"
+ "PTM"
+ "RMUSE"
+ "ReportingVC [%s] %s:%d Could not create directory"
+ "ReportingVC [%s] %s:%d Could not create directory=%@"
+ "ReportingVC [%s] %s:%d Could not get calendar"
+ "ReportingVC [%s] %s:%d Could not save ID value to cache error=%@"
+ "ReportingWeeklyID"
+ "ReportingWeeklyIDValidityWeek"
+ "ReportingWeeklyIDValidityYear"
+ "SliceInterfaceFailed"
+ "SliceInterfaceNotReceived"
+ "T@\"NSString\",C,V_weeklyDUID"
+ "TI,V_audioBasebandDropPacketCount"
+ "TI,V_audioFlushPacketCount"
+ "TQ,V_videoBasebandDropPacketCount"
+ "T{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}},V_persistentSettings"
+ "URLByAppendingPathComponent:"
+ "UUID"
+ "VBBDP"
+ "VPBBD"
+ "[72B]"
+ "_audioBasebandDropPacketCount"
+ "_deviceUniqueID"
+ "_hasReportedSliceStatusFailedSymptom"
+ "_hasReportedSliceStatusNotReceivedSymptom"
+ "_jbJumpSpikeCount"
+ "_jbSlopeSpikeCount"
+ "_jbSpikeSizeDelta"
+ "_jbUnclippedTarget"
+ "_pTime"
+ "_rateControlBasebandNotificationNWCount"
+ "_remoteMicPacketLossRateAccumulator"
+ "_remoteMicUseCase"
+ "_videoBasebandDropPacketCount"
+ "_weeklyDUID"
+ "aggregateJitterBufferMetricsToReportDictionary:"
+ "audioBasebandDropPacketCount"
+ "calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:"
+ "checkIfWeeklyIDIsExpired:currentWeek:currentYear:"
+ "checkSliceStatus:hasValuesOnlyForStatus:"
+ "components:fromDate:"
+ "createDefaultCacheDirectoryIfNeeded"
+ "createDefaultDirectoryIfNeeded:"
+ "currentCalendar"
+ "directoryPathForWeeklyIDCache"
+ "fileURLWithPath:isDirectory:"
+ "i20@0:8I16"
+ "initCallWithRemoteParticipantID:andWeeklyID:"
+ "initWithContentsOfURL:"
+ "numberWithUnsignedInteger:"
+ "processCallStart:"
+ "processSegmentRateControllerTelemetry:"
+ "processSliceStatusABCSymptoms:"
+ "processSliceStatusFailedABCSymptom:"
+ "processSliceStatusNotReceivedABCSymptom:"
+ "reportConnectionSliceStatus:"
+ "reporting_weeklyID_config.plist"
+ "setAndSaveWeeklyID:currentWeek:currentYear:cachePath:"
+ "setAudioBasebandDropPacketCount:"
+ "setUpWeeklyRotatingID"
+ "setVideoBasebandDropPacketCount:"
+ "setWeeklyDUID:"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}16"
+ "v24@0:8^{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
+ "v40@0:8@16^I24^I32"
+ "v40@0:8{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
+ "v48@0:8@16Q24Q32@40"
+ "videoBasebandDropPacketCount"
+ "weekOfYear"
+ "weeklyDUID"
+ "writeToURL:error:"
+ "yearForWeekOfYear"
+ "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B}}"
+ "{tagVCReportingClientSettingsPersist=cccccccQ{tagVCReportingClientExperimentSettings=BB}}16@0:8"
- " [%s] %s:%d totalAudioPacketsFlushed must no be nil"
- "+[VCDiskUtils createDefaultLogDirectoryIfNeeded]"
- "-[VCAggregatorMultiway calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:totalAudioPacketsFlushed:]"
- "@28@0:8i16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}20"
- "@32@0:8@16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}24"
- "BGRCCFENB"
- "Tc,N,V_backgroundReplacementContinuityCameraStatus"
- "T{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BB}},V_persistentSettings"
- "[70B]"
- "_backgroundReplacementContinuityCameraStatus"
- "backgroundReplacementContinuityCameraStatus"
- "calculateStreamTelemetry:totalReceiveRate:audioPacketsSent:totalAudioPacketsFlushed:"
- "initCallWithRemoteParticipantID:"
- "setBackgroundReplacementContinuityCameraStatus:"
- "v24@0:8^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}16"
- "v24@0:8^{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
- "v40@0:8{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BB}}16"
- "v48@0:8@16^I24^I32^I40"
- "{tagVCReportingClientSettingsPersist=\"eyeContactStatus\"c\"mlEnhanceStatus\"c\"centerStageStatus\"c\"portraitModeStatus\"c\"studioLightStatus\"c\"reactionsStatus\"c\"backgroundReplacementStatus\"c\"backgroundReplacementContinuityCameraStatus\"c\"switches\"Q\"experimentSettings\"{tagVCReportingClientExperimentSettings=\"networkConditionMonitoringClientExperimentEnabled\"B\"motionBasedDuplicationClientExperimentEnabled\"B}}"
- "{tagVCReportingClientSettingsPersist=ccccccccQ{tagVCReportingClientExperimentSettings=BB}}16@0:8"

```
