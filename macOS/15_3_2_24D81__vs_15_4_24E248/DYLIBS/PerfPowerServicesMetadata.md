## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/Versions/A/PerfPowerServicesMetadata`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0x2e354
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x2004
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x255d
+2423.100.232.0.0
+  __TEXT.__text: 0x34b5c
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_methlist: 0x229c
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x2d5b
   __TEXT.__oslogstring: 0x129a
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x740
-  __TEXT.__objc_classname: 0x3d0
-  __TEXT.__objc_methname: 0x2b93
+  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__objc_classname: 0x3e7
+  __TEXT.__objc_methname: 0x2d43
   __TEXT.__objc_methtype: 0x508
-  __TEXT.__objc_stubs: 0x2e00
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__objc_stubs: 0x30c0
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe70
+  __DATA_CONST.__objc_selrefs: 0xf98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__objc_arraydata: 0x128
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0x3fd0
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__cfstring: 0x5de0
+  __AUTH_CONST.__objc_const: 0x3e78
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__objc_dictobj: 0x1b8
-  __AUTH.__objc_data: 0x1090
+  __AUTH_CONST.__objc_dictobj: 0x230
+  __AUTH.__objc_data: 0x10e0
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x120
   __DATA.__bss: 0x288

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1063973D-9C52-3253-9E08-45634641ED2F
-  Functions: 841
-  Symbols:   1945
-  CStrings:  2097
+  UUID: A5679C55-980A-3635-8AAB-5E20D7DE5EDF
+  Functions: 908
+  Symbols:   2035
+  CStrings:  2394
 
Symbols:
+ +[PPSBGProcessingCommonMetrics AppResumeInferredCarryMetrics]
+ +[PPSBGProcessingCommonMetrics BuddyDataMetrics]
+ +[PPSBGProcessingCommonMetrics FeatureFlagMetrics]
+ +[PPSBGProcessingCommonMetrics allDeclMetrics]
+ +[PPSBGProcessingCommonMetrics configMetrics]
+ +[PPSBGProcessingCommonMetrics localeMetrics]
+ +[PPSBGProcessingCommonMetrics optInMetrics]
+ +[PPSBGProcessingCommonMetrics subsystem]
+ +[PPSBGProcessingCommonMetrics timeOffsetCadence]
+ +[PPSBGProcessingCommonMetrics timeOffsetMetrics]
+ +[PPSBGProcessingCommonMetrics timezoneLoggingCadence]
+ +[PPSBasebandMetrics BBMessageLite]
+ +[PPSBasebandMetrics BBMsgAll]
+ +[PPSBasebandMetrics BBReport]
+ +[PPSBasebandMetrics SleepWakeABM]
+ +[PPSBasebandMetrics SmartDataMode]
+ +[PPSBasebandMetrics allDeclMetrics]
+ +[PPSBasebandMetrics eventMetrics]
+ +[PPSBasebandMetrics histogramMetrics]
+ +[PPSBasebandMetrics messageMetricDump]
+ +[PPSBasebandMetrics messageTriggerDump]
+ +[PPSBasebandMetrics subsystem]
+ +[PPSBasebandMetrics telephonyActivity]
+ +[PPSBasebandMetrics telephonyRegistration]
+ +[PPSCadence cadenceEventSBC].cold.1
+ +[PPSCadence cadenceEventSBC_EventScreenStateChange].cold.1
+ +[PPSCadence cadenceInit].cold.1
+ +[PPSCadence cadenceInit_EventSBC].cold.1
+ +[PPSIOReportMetrics ans2Msp0Metrics]
+ +[PPSIOReportMetrics dcpScanoutStatsMetrics]
+ +[PPSIOReportMetrics ispIspEventsMetrics]
+ +[PPSMessageMetrics messageTranscriptForegroundMetrics]
+ +[PPSMetadataStore sharedStore].cold.1
+ +[PPSMetricManager metricDeclMap].cold.2
+ +[PPSMetricType absoluteMeasure].cold.1
+ +[PPSMetricType accumulatedNegativeMeasure].cold.1
+ +[PPSMetricType accumulatedPositiveMeasure].cold.1
+ +[PPSMetricType deltaMeasure].cold.1
+ +[PPSMetricType genericDimension].cold.1
+ +[PPSMetricType stateDimension].cold.1
+ +[PPSRounding roundDown].cold.1
+ +[PPSRounding roundNearest].cold.1
+ +[PPSRounding roundUp].cold.1
+ +[PPSSMCMetrics smcInstantKeyValueMetrics]
+ +[PPSSMCMetrics smcInstantLookUpMetrics]
+ +[PPSSMCMetrics smcPowerDeliveryCLVRMetrics]
+ +[PPSSleepMetrics allDeclMetrics]
+ +[PPSSleepMetrics subsystem]
+ +[PPSUnit bytes].cold.1
+ +[PPSUnit celsius].cold.1
+ +[PPSUnit dimensionless].cold.1
+ +[PPSUnit grams].cold.1
+ +[PPSUnit kilobytes].cold.1
+ +[PPSUnit megabytes].cold.1
+ +[PPSUnit microWattHours].cold.1
+ +[PPSUnit microseconds].cold.1
+ +[PPSUnit milliAmpereHours].cold.1
+ +[PPSUnit milliAmperes].cold.1
+ +[PPSUnit milliVolts].cold.1
+ +[PPSUnit milliseconds].cold.1
+ +[PPSUnit nanoseconds].cold.1
+ +[PPSUnit seconds].cold.1
+ +[PPSUnit volts].cold.1
+ +[PPSXPCMetrics mailCategorizationEnabledMetrics]
+ +[PPSXPCMetrics mailCategorizationMetrics]
+ PPSClientInterfaceLog.cold.1
+ PPSMetricLog.cold.1
+ PPSSQLStoreLog.cold.1
+ PPSStorageLog.cold.1
+ PPSStoreLog.cold.1
+ _OBJC_CLASS_$_PPSBGProcessingCommonMetrics
+ _OBJC_CLASS_$_PPSBasebandMetrics
+ _OBJC_CLASS_$_PPSSleepMetrics
+ _OBJC_METACLASS_$_PPSBGProcessingCommonMetrics
+ _OBJC_METACLASS_$_PPSBasebandMetrics
+ _OBJC_METACLASS_$_PPSSleepMetrics
+ __OBJC_$_CLASS_METHODS_PPSBGProcessingCommonMetrics
+ __OBJC_$_CLASS_METHODS_PPSBasebandMetrics
+ __OBJC_$_CLASS_METHODS_PPSSleepMetrics
+ __OBJC_$_PROP_LIST_PPSBGProcessingCommonMetrics
+ __OBJC_$_PROP_LIST_PPSBasebandMetrics
+ __OBJC_$_PROP_LIST_PPSSleepMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSBGProcessingCommonMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSBasebandMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSSleepMetrics
+ __OBJC_CLASS_RO_$_PPSBGProcessingCommonMetrics
+ __OBJC_CLASS_RO_$_PPSBasebandMetrics
+ __OBJC_CLASS_RO_$_PPSSleepMetrics
+ __OBJC_METACLASS_RO_$_PPSBGProcessingCommonMetrics
+ __OBJC_METACLASS_RO_$_PPSBasebandMetrics
+ __OBJC_METACLASS_RO_$_PPSSleepMetrics
+ _objc_msgSend$AppResumeInferredCarryMetrics
+ _objc_msgSend$BBMessageLite
+ _objc_msgSend$BBMsgAll
+ _objc_msgSend$BBReport
+ _objc_msgSend$BuddyDataMetrics
+ _objc_msgSend$FeatureFlagMetrics
+ _objc_msgSend$SleepWakeABM
+ _objc_msgSend$SmartDataMode
+ _objc_msgSend$ans2Msp0Metrics
+ _objc_msgSend$dcpScanoutStatsMetrics
+ _objc_msgSend$eventMetrics
+ _objc_msgSend$histogramMetrics
+ _objc_msgSend$ispIspEventsMetrics
+ _objc_msgSend$localeMetrics
+ _objc_msgSend$mailCategorizationEnabledMetrics
+ _objc_msgSend$mailCategorizationMetrics
+ _objc_msgSend$messageMetricDump
+ _objc_msgSend$messageTranscriptForegroundMetrics
+ _objc_msgSend$messageTriggerDump
+ _objc_msgSend$smcInstantKeyValueMetrics
+ _objc_msgSend$smcInstantLookUpMetrics
+ _objc_msgSend$smcPowerDeliveryCLVRMetrics
+ _objc_msgSend$telephonyActivity
+ _objc_msgSend$telephonyRegistration
+ _objc_msgSend$timeOffsetCadence
+ logHandle.cold.1
- +[PPSButtonMetrics allDeclMetrics]
- +[PPSButtonMetrics captureButtonAction]
- +[PPSButtonMetrics captureButtonConfig]
- +[PPSButtonMetrics subsystem]
- +[PPSCameraCaptureMetrics allDeclMetrics]
- +[PPSCameraCaptureMetrics cameraInPocketDecision]
- +[PPSCameraCaptureMetrics subsystem]
- _OBJC_CLASS_$_PPSButtonMetrics
- _OBJC_CLASS_$_PPSCameraCaptureMetrics
- _OBJC_METACLASS_$_PPSButtonMetrics
- _OBJC_METACLASS_$_PPSCameraCaptureMetrics
- _OUTLINED_FUNCTION_9
- __OBJC_$_CLASS_METHODS_PPSButtonMetrics
- __OBJC_$_CLASS_METHODS_PPSCameraCaptureMetrics
- __OBJC_$_PROP_LIST_PPSButtonMetrics
- __OBJC_$_PROP_LIST_PPSCameraCaptureMetrics
- __OBJC_CLASS_PROTOCOLS_$_PPSButtonMetrics
- __OBJC_CLASS_PROTOCOLS_$_PPSCameraCaptureMetrics
- __OBJC_CLASS_RO_$_PPSButtonMetrics
- __OBJC_CLASS_RO_$_PPSCameraCaptureMetrics
- __OBJC_METACLASS_RO_$_PPSButtonMetrics
- __OBJC_METACLASS_RO_$_PPSCameraCaptureMetrics
- ___kCFBooleanFalse
- _fmod
- _objc_msgSend$cameraInPocketDecision
- _objc_msgSend$captureButtonAction
- _objc_msgSend$captureButtonConfig
CStrings:
+ "%@%d"
+ "ANS2MSP0"
+ "AppResumeInferredCarry"
+ "AppResumeInferredCarryMetrics"
+ "AriGroupID"
+ "AriLength"
+ "AriMsgID"
+ "AriMsgName"
+ "AriSeqNum"
+ "AutomatedDeviceGroup"
+ "BBMessageLite"
+ "BBMsgAll"
+ "BBReport"
+ "BackgroundProcessing"
+ "Backlog"
+ "BasebandMetrics"
+ "Begin"
+ "BuddyDataMetrics"
+ "CarryType"
+ "ClientAction"
+ "ClientName"
+ "CustomerOS"
+ "DCPscanoutstats"
+ "DPE_AISP_BAYERPROC_PIPE_BayerProc High"
+ "DPE_AISP_BAYERPROC_PIPE_BayerProc Low"
+ "DPE_AISP_DEMPROC_PIPE_DemProc High"
+ "DPE_AISP_DEMPROC_PIPE_DemProc Low"
+ "DPE_AISP_MSBEPROC_PIPE_MsProcBE High"
+ "DPE_AISP_MSBEPROC_PIPE_MsProcBE Low"
+ "DPE_AISP_SIFFE_PIPE0_IspPipeSIfFE High"
+ "DPE_AISP_SIFFE_PIPE0_IspPipeSIfFE Low"
+ "DPE_AISP_SIFFE_PIPE1_IspPipeSIfFE High"
+ "DPE_AISP_SIFFE_PIPE1_IspPipeSIfFE Low"
+ "DPE_AISP_SIFFE_PIPE2_IspPipeSIfFE High"
+ "DPE_AISP_SIFFE_PIPE2_IspPipeSIfFE Low"
+ "DPE_AISP_SIFFE_PIPE3_IspPipeSIfFE High"
+ "DPE_AISP_SIFFE_PIPE3_IspPipeSIfFE Low"
+ "DPE_CVD_LaccMatchWrap High"
+ "DPE_CVD_LaccMatchWrap Low"
+ "DeviceDiskSize"
+ "Device_SoC"
+ "Domain"
+ "Empty-Mail-Thread"
+ "Erase install"
+ "Events"
+ "Fast-Pass"
+ "FeatureFlag"
+ "FeatureFlagMetrics"
+ "FeatureName"
+ "Foreground"
+ "GenerativeFunctionMetricsOptIn"
+ "Histogram"
+ "ISPISPEvents"
+ "InstallType"
+ "InstantKeyValues"
+ "InstantLookUpTable"
+ "IpDst"
+ "IpDstPort"
+ "IpProto"
+ "IpSrc"
+ "IpSrcPort"
+ "IpVer"
+ "IsCmas"
+ "Key0"
+ "KeyIndex"
+ "KeyName"
+ "LastBuild"
+ "LastUpgradeSystemTimestamp"
+ "LastUpgradeTimestamp"
+ "Mail-Summarization-Disabled"
+ "MailCategorization"
+ "MailCategorizationEnabled"
+ "MailCategorizationEvent"
+ "Major upgrade install"
+ "Message-Summarization-Disabled"
+ "MessageAll"
+ "MessageLite"
+ "Minor upgrade install"
+ "MsgMetricDump"
+ "MsgTriggerDump"
+ "New-Message"
+ "Notes-Summarization-Disabled"
+ "OSVariant"
+ "PID"
+ "PPSBGProcessingCommonMetrics"
+ "PPSBasebandMetrics"
+ "PPSSleepMetrics"
+ "Payload"
+ "PowerDeliveryCLVRKeys"
+ "ProcessName"
+ "RailMode"
+ "Report"
+ "RootInstalled"
+ "SDMState"
+ "SeqNum"
+ "Sleep"
+ "SleepWakeABM"
+ "SmartDataMode"
+ "State"
+ "SupplementalBuild"
+ "TargetRelease"
+ "TelephonyActivity"
+ "TelephonyRegistration"
+ "Temperature(0)"
+ "TranscriptForeground"
+ "TranscriptVisibilityState"
+ "Type"
+ "WakeChannel"
+ "WakeData"
+ "WakeDataParsed"
+ "WakeSubType"
+ "WakeType"
+ "activeBand"
+ "airplaneMode"
+ "ambient"
+ "ans2Msp0Metrics"
+ "appId"
+ "bbtimestamp"
+ "callStatus"
+ "campedRat"
+ "cellId"
+ "currentRat"
+ "dataActive"
+ "dataAttached"
+ "dataInd"
+ "dataStatus"
+ "dcpScanoutStatsMetrics"
+ "duration_exp"
+ "end_time"
+ "eventMetrics"
+ "genpipe_one_sca"
+ "genpipe_two_sca"
+ "histogramMetrics"
+ "home"
+ "ispIspEventsMetrics"
+ "lac"
+ "localeMetrics"
+ "mailCategorizationEnabledMetrics"
+ "mailCategorizationMetrics"
+ "messageMetricDump"
+ "messageTranscriptForegroundMetrics"
+ "messageTriggerDump"
+ "metricPayload"
+ "metricProfileId"
+ "metricTriggerRef"
+ "mid"
+ "one_genpipe"
+ "operator"
+ "pdc"
+ "prc"
+ "preferredRat"
+ "serviceOpt"
+ "signalBars"
+ "signalStrength"
+ "simStatus"
+ "smcInstantKeyValueMetrics"
+ "smcInstantLookUpMetrics"
+ "smcPowerDeliveryCLVRMetrics"
+ "spi"
+ "start_time"
+ "subsId"
+ "telephonyActivity"
+ "telephonyRegistration"
+ "timeOffsetCadence"
+ "timestampLogged"
+ "triggerCnt"
+ "triggerId"
+ "triggerRef"
+ "triggerTime"
+ "triggerType"
+ "two_genpipe"
+ "value_enabled"
+ "value_history"
- "Button"
- "CameraCapture"
- "CaptureButtonAction"
- "CaptureButtonConfig"
- "DetectionSessionStartTime"
- "DetectionSessionStopTime"
- "FullPress"
- "HalfPress"
- "InPocketDecision"
- "PPSButtonMetrics"
- "PPSCameraCaptureMetrics"
- "PocketDetection"
- "Touch"
- "TouchTimeInterval"
- "cameraInPocketDecision"
- "captureButtonAction"
- "captureButtonConfig"

```
