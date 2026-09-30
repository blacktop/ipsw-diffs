## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0x33fcc
+2954.0.0.502.3
+  __TEXT.__text: 0x3a57c
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2374
+  __TEXT.__objc_methlist: 0x2554
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x328c
-  __TEXT.__oslogstring: 0x12df
+  __TEXT.__cstring: 0x3e52
+  __TEXT.__oslogstring: 0x1354
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__objc_classname: 0x400
-  __TEXT.__objc_methname: 0x2eb8
-  __TEXT.__objc_methtype: 0x508
-  __TEXT.__objc_stubs: 0x33e0
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x180
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__objc_classname: 0x466
+  __TEXT.__objc_methname: 0x3110
+  __TEXT.__objc_methtype: 0x519
+  __TEXT.__objc_stubs: 0x3760
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1018
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_arraydata: 0x1c0
   __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x68c0
-  __AUTH_CONST.__objc_const: 0x3f68
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__const: 0x500
+  __AUTH_CONST.__cfstring: 0x7fe0
+  __AUTH_CONST.__objc_const: 0x4488
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x148
+  __AUTH_CONST.__objc_dictobj: 0x370
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x150
   __DATA.__data: 0x120
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0xe60
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A1696284-17CB-3666-BD54-A486E8A15E98
-  Functions: 921
-  Symbols:   3021
-  CStrings:  2587
+  UUID: 48CB3E3C-12BB-3AFF-B3C7-9D801D389324
+  Functions: 966
+  Symbols:   3183
+  CStrings:  2998
 
Symbols:
+ +[PPSAccessoryUsageSummaryMetrics allDeclMetrics]
+ +[PPSAccessoryUsageSummaryMetrics audioAccessoryMetrics]
+ +[PPSAccessoryUsageSummaryMetrics subsystem]
+ +[PPSApplicationMetrics appiconMetrics]
+ +[PPSBGProcessingCommonMetrics RebootEventsMetrics]
+ +[PPSBGProcessingCommonMetrics TimeOfCaptureEventMetrics]
+ +[PPSBasebandMetrics modeChange]
+ +[PPSCadence cadencePeriodic:]
+ +[PPSCoreLocation allDeclMetrics]
+ +[PPSCoreLocation geoFenceTriggerMetrics]
+ +[PPSCoreLocation subsystem]
+ +[PPSIOReportMetrics aop2PerformanceMetrics]
+ +[PPSMapsMetrics allDeclMetrics]
+ +[PPSMapsMetrics springfieldUsageMetrics]
+ +[PPSMapsMetrics subsystem]
+ +[PPSMetric isValidAppIdentifier:]
+ +[PPSMetric isValidAppIdentifier:].cold.1
+ +[PPSMetric isValidAppIdentifier:].cold.2
+ +[PPSMetric(JSON) isValidMetricJSON:].cold.24
+ +[PPSPMUMetrics allDeclMetrics]
+ +[PPSPMUMetrics railEnergyPMUMetrics]
+ +[PPSPMUMetrics subsystem]
+ +[PPSSMCMetrics smcAccumulatedKeyValueMetrics]
+ +[PPSSMCMetrics smcAccumulatedLookUpMetrics]
+ +[PPSSMCMetrics smcOLEDDisplayPowerMetrics]
+ +[PPSStatusKitAgentMetrics aggregatedPushesMetrics]
+ +[PPSStatusKitAgentMetrics allDeclMetrics]
+ +[PPSStatusKitAgentMetrics subsystem]
+ +[PPSUnit milliWatts]
+ +[PPSUnit milliWatts].cold.1
+ +[PPSUnit minutes]
+ +[PPSUnit minutes].cold.1
+ +[PPSUnit watts]
+ +[PPSUnit watts].cold.1
+ +[PPSXPCMetrics powerExceptionsDetectionMetrics]
+ +[PPSXPCMetrics triggerEventMetrics]
+ -[PPSMetric addAppIdentifier:]
+ -[PPSMetric appIdentifier]
+ -[PPSPBMetric appIdentifier]
+ -[PPSPBMetric hasAppIdentifier]
+ -[PPSPBMetric setAppIdentifier:]
+ -[PPSPBMetric setHasAppIdentifier:]
+ GCC_except_table35
+ GCC_except_table61
+ GCC_except_table93
+ OBJC_IVAR_$_PPSPBMetric._appIdentifier
+ _OBJC_CLASS_$_NSUnitPower
+ _OBJC_CLASS_$_PPSAccessoryUsageSummaryMetrics
+ _OBJC_CLASS_$_PPSCoreLocation
+ _OBJC_CLASS_$_PPSMapsMetrics
+ _OBJC_CLASS_$_PPSPMUMetrics
+ _OBJC_CLASS_$_PPSStatusKitAgentMetrics
+ _OBJC_IVAR_$_PPSMetric._appIdentifier
+ _OBJC_METACLASS_$_PPSAccessoryUsageSummaryMetrics
+ _OBJC_METACLASS_$_PPSCoreLocation
+ _OBJC_METACLASS_$_PPSMapsMetrics
+ _OBJC_METACLASS_$_PPSPMUMetrics
+ _OBJC_METACLASS_$_PPSStatusKitAgentMetrics
+ __OBJC_$_CLASS_METHODS_PPSAccessoryUsageSummaryMetrics
+ __OBJC_$_CLASS_METHODS_PPSCoreLocation
+ __OBJC_$_CLASS_METHODS_PPSMapsMetrics
+ __OBJC_$_CLASS_METHODS_PPSPMUMetrics
+ __OBJC_$_CLASS_METHODS_PPSStatusKitAgentMetrics
+ __OBJC_$_PROP_LIST_PPSAccessoryUsageSummaryMetrics
+ __OBJC_$_PROP_LIST_PPSCoreLocation
+ __OBJC_$_PROP_LIST_PPSMapsMetrics
+ __OBJC_$_PROP_LIST_PPSPMUMetrics
+ __OBJC_$_PROP_LIST_PPSStatusKitAgentMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSAccessoryUsageSummaryMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSCoreLocation
+ __OBJC_CLASS_PROTOCOLS_$_PPSMapsMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSPMUMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PPSStatusKitAgentMetrics
+ __OBJC_CLASS_RO_$_PPSAccessoryUsageSummaryMetrics
+ __OBJC_CLASS_RO_$_PPSCoreLocation
+ __OBJC_CLASS_RO_$_PPSMapsMetrics
+ __OBJC_CLASS_RO_$_PPSPMUMetrics
+ __OBJC_CLASS_RO_$_PPSStatusKitAgentMetrics
+ __OBJC_METACLASS_RO_$_PPSAccessoryUsageSummaryMetrics
+ __OBJC_METACLASS_RO_$_PPSCoreLocation
+ __OBJC_METACLASS_RO_$_PPSMapsMetrics
+ __OBJC_METACLASS_RO_$_PPSPMUMetrics
+ __OBJC_METACLASS_RO_$_PPSStatusKitAgentMetrics
+ ___16+[PPSUnit watts]_block_invoke
+ ___18+[PPSUnit minutes]_block_invoke
+ ___21+[PPSUnit milliWatts]_block_invoke
+ ___30+[PPSCadence cadencePeriodic:]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_literal_global.26
+ ___block_literal_global.29
+ ___block_literal_global.34
+ ___block_literal_global.37
+ ___block_literal_global.39
+ ___block_literal_global.42
+ ___block_literal_global.45
+ ___block_literal_global.47
+ _cadencePeriodic:._cadences
+ _cadencePeriodic:.onceToken
+ _milliWatts._unitMilliWatts
+ _milliWatts.onceToken
+ _minutes._unitMinutes
+ _minutes.onceToken
+ _objc_msgSend$RebootEventsMetrics
+ _objc_msgSend$TimeOfCaptureEventMetrics
+ _objc_msgSend$_setError
+ _objc_msgSend$addAppIdentifier:
+ _objc_msgSend$aggregatedPushesMetrics
+ _objc_msgSend$aop2PerformanceMetrics
+ _objc_msgSend$appIdentifier
+ _objc_msgSend$appiconMetrics
+ _objc_msgSend$audioAccessoryMetrics
+ _objc_msgSend$cadencePeriodic:
+ _objc_msgSend$geoFenceTriggerMetrics
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$isValidAppIdentifier:
+ _objc_msgSend$milliWatts
+ _objc_msgSend$milliwatts
+ _objc_msgSend$minutes
+ _objc_msgSend$modeChange
+ _objc_msgSend$position
+ _objc_msgSend$powerExceptionsDetectionMetrics
+ _objc_msgSend$railEnergyPMUMetrics
+ _objc_msgSend$setAppIdentifier:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$smcAccumulatedKeyValueMetrics
+ _objc_msgSend$smcAccumulatedLookUpMetrics
+ _objc_msgSend$smcOLEDDisplayPowerMetrics
+ _objc_msgSend$springfieldUsageMetrics
+ _objc_msgSend$triggerEventMetrics
+ _objc_msgSend$watts
+ _watts._unitWatts
+ _watts.onceToken
- +[PPSXPCMetrics groupActivitiesMetrics]
- GCC_except_table33
- GCC_except_table60
- GCC_except_table88
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___block_literal_global.16
- ___block_literal_global.21
- ___block_literal_global.24
- ___block_literal_global.27
- ___block_literal_global.32
- ___block_literal_global.35
- ___block_literal_global.38
- ___block_literal_global.40
- _objc_msgSend$groupActivitiesMetrics
CStrings:
+ "A2DPRSSIHigh"
+ "A2DPRSSIMiddle"
+ "A2DPRSSIPoor"
+ "A2DPRetransHigh"
+ "A2DPRetransLow"
+ "A2DPRetransMiddle"
+ "A2DPSNRHigh"
+ "A2DPSNRLow"
+ "A2DPSNRMiddle"
+ "A2DPTotalDuration"
+ "ANCTotalDuration"
+ "AOP2Performance"
+ "AP_HIBERNATE"
+ "AP_PANIC"
+ "AP_RESTART"
+ "AP_SHUTDOWN"
+ "AP_SYSTEM_RESET"
+ "AP_VIRTUAL_SLEEP_LL"
+ "AP_WATCHDOG_EXPIRY"
+ "Accent"
+ "AccessoryUsageSummary"
+ "AccumulatedKeyValues"
+ "AccumulatedLookUpTable"
+ "AdaptiveTotalDuration"
+ "Address"
+ "AggregatedPushes"
+ "AirplaneMode"
+ "Already BackgroundQoS"
+ "AppIcons"
+ "AppIdentifier"
+ "AssertedPresence"
+ "AudioDropCount"
+ "AudioDropOverWaitCount"
+ "AudioDropPoorRSSICount"
+ "Auto"
+ "Background QoS Disabled"
+ "Background QoS Enabled"
+ "BackgroundQoS Failed"
+ "BothBudTotalDuration"
+ "Cell2Wifi"
+ "ChannelType"
+ "ClientID"
+ "CoalitionID"
+ "CoalitionName"
+ "Color"
+ "CompanionConnectionUpdate"
+ "ConnectionCount"
+ "ConnectionError1Count"
+ "ConnectionError2Count"
+ "ConnectionError3Count"
+ "ConnectionError4Count"
+ "ConnectionErrorGeneralCount"
+ "ContinousTrackingTimer"
+ "CopyLog"
+ "CoreLocation"
+ "CreatedChannel"
+ "CustomTintColor"
+ "CycleCountDiff"
+ "Dark"
+ "DelayedTriggerTimer"
+ "DisconnectionError1Count"
+ "DisconnectionError2Count"
+ "DisconnectionError3Count"
+ "DisconnectionError4Count"
+ "DisconnectionGeneralCount"
+ "DisplayPower"
+ "ENTER_REM"
+ "ENTER_REM_DEVELOPMENT"
+ "EpnoEntry"
+ "EpnoExit"
+ "ErrorString"
+ "EstimatedEnergy"
+ "EventName"
+ "Exempted DAS Activity"
+ "Exempted Plugged In"
+ "Exempted Root Daemon"
+ "Exempted due to coalition name"
+ "Exempted from cpu mon"
+ "False"
+ "Fatal Skipped"
+ "FilterType"
+ "ForceMitigationSuggestion"
+ "Forced Migitation"
+ "GameTotalDuration"
+ "GeofenceTrigger"
+ "HFPTotalDuration"
+ "IDS"
+ "IDSMessage"
+ "Invalid Argument"
+ "Invalid appIdentifier %llu"
+ "Kill Failed"
+ "Known Violation"
+ "Large"
+ "LaunchdName"
+ "Light"
+ "MEMORY_MAINTENANCE"
+ "Maps"
+ "Metadata"
+ "Metric json property 'appIdentifier' is not a %@"
+ "MitigationDecisionReason"
+ "MitigationDecisionType"
+ "MitigationSuggestion"
+ "MitigationSuggestionReason"
+ "ModeChange"
+ "More than one processes"
+ "MotionActivityAlarm"
+ "No Process Data"
+ "No Process Identifier"
+ "No Process Name"
+ "No pids found that match coalition ID"
+ "No process"
+ "Not daemon"
+ "NumIncoming"
+ "NumOutgoing"
+ "Off Charger"
+ "Overridden"
+ "Overridden By Other Rules"
+ "PDEP"
+ "PDLP"
+ "PMUMetrics"
+ "PPSAccessoryUsageSummaryMetrics"
+ "PPSCoreLocation"
+ "PPSMapsMetrics"
+ "PPSPMUMetrics"
+ "PPSStatusKitAgentMetrics"
+ "PairingCount"
+ "PairingError1Count"
+ "PairingError2Count"
+ "PairingError3Count"
+ "PairingError4Count"
+ "PairingErrorGeneralCount"
+ "Partial Mitigation"
+ "Pending Background QoS"
+ "Pending BackgroundQoS"
+ "PolledForPresence"
+ "PosterName"
+ "Power"
+ "Power Exceptions relaunched"
+ "PowerExceptionsDetection"
+ "Presence"
+ "PresenceManagement"
+ "Process Not Running"
+ "Process relaunched"
+ "ProductID"
+ "ProvisionedPayload"
+ "PublishedStatus"
+ "REBOOTEVENT_SYSTEM"
+ "REBOOTEVENT_USERSPACE"
+ "RESTORE_FROM_BACKUP"
+ "Rail"
+ "RailEnergy"
+ "Reason"
+ "RebootEvents"
+ "RebootEventsMetrics"
+ "ReceivedPayload"
+ "RefreshVisibleAPs"
+ "RuleID"
+ "SMC_DARK_WAKE_THERMAL_CRITICAL"
+ "SMC_REMOTE_MANAGEMENT"
+ "SMC_THERMAL_CRITICAL"
+ "SingleBudTotalDuration"
+ "Size"
+ "Small"
+ "SpatialTotalDuration"
+ "SpringfieldUsage"
+ "Status"
+ "StatusKitAgent"
+ "Subscribed"
+ "Sysdiagnose"
+ "TaskEndTime"
+ "Tasking"
+ "Ti,N,V_appIdentifier"
+ "Ti,R,V_appIdentifier"
+ "Time Limit Expired"
+ "TimeOfCaptureEvent"
+ "TimeOfCaptureEventMetrics"
+ "TimeSinceBoot"
+ "TransparencyTotalDuration"
+ "TriggerEvents"
+ "TriggeredDetection"
+ "True"
+ "UNKNOWN"
+ "USER_SWITCH"
+ "UnassertedPresence"
+ "Unsubscribed"
+ "Variant"
+ "Wake"
+ "WiFiConnected"
+ "WiFiDisassociation"
+ "WiFiDisconnected"
+ "WiFiPower"
+ "_appIdentifier"
+ "_setError"
+ "addAppIdentifier:"
+ "aggregatedPushesMetrics"
+ "aop2PerformanceMetrics"
+ "appIdentifier"
+ "appIdentifier not a NSNumber type %@[%@]"
+ "appiconMetrics"
+ "audioAccessoryMetrics"
+ "cadencePeriodic:"
+ "geoFenceTriggerMetrics"
+ "getBytes:range:"
+ "hasAppIdentifier"
+ "hasError"
+ "isSPR"
+ "isValidAppIdentifier:"
+ "kCTRadioBasebandOperatingModeKey"
+ "kCTRadioBasebandOperatingModeReasonKey"
+ "kCTRadioBasebandReasonKey"
+ "kCTRadioBasebandTelephonyReasonKey"
+ "megaBytesDownloaded"
+ "milliWatts"
+ "milliwatts"
+ "minutes"
+ "modeChange"
+ "position"
+ "powerExceptionsDetectionMetrics"
+ "railEnergyPMUMetrics"
+ "setAppIdentifier:"
+ "setHasAppIdentifier:"
+ "setPosition:"
+ "smcAccumulatedKeyValueMetrics"
+ "smcAccumulatedLookUpMetrics"
+ "smcOLEDDisplayPowerMetrics"
+ "springfieldUsageMetrics"
+ "timestampStart"
+ "triggerEventMetrics"
+ "watts"
+ "{?=\"version\"b1\"appIdentifier\"b1\"auxiliaryType\"b1\"datatype\"b1\"deviceCapability\"b1\"directionality\"b1\"enabledPopulation\"b1\"fixedArraySize\"b1\"mode\"b1\"obfuscation\"b1\"privacyClassification\"b1\"storage\"b1\"timeToLive\"b1\"dmaCompliant\"b1\"filterEntryLogging\"b1}"
- "GroupActivities"
- "Max CPU Usage Limit"
- "bytesDownloaded"
- "groupActivitiesMetrics"
- "{?=\"version\"b1\"auxiliaryType\"b1\"datatype\"b1\"deviceCapability\"b1\"directionality\"b1\"enabledPopulation\"b1\"fixedArraySize\"b1\"mode\"b1\"obfuscation\"b1\"privacyClassification\"b1\"storage\"b1\"timeToLive\"b1\"dmaCompliant\"b1\"filterEntryLogging\"b1}"

```
