## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

 30.59.1.9.0
-  __TEXT.__text: 0x3de40
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x4fcc
-  __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x14e4
-  __TEXT.__cstring: 0xb253
-  __TEXT.__unwind_info: 0x1078
-  __TEXT.__objc_classname: 0x63b
-  __TEXT.__objc_methname: 0xab06
-  __TEXT.__objc_methtype: 0x13eb
-  __TEXT.__objc_stubs: 0x56c0
+  __TEXT.__text: 0x3febc
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x5244
+  __TEXT.__const: 0x2a0
+  __TEXT.__gcc_except_tab: 0x1590
+  __TEXT.__cstring: 0xb91e
+  __TEXT.__unwind_info: 0x10b8
+  __TEXT.__objc_classname: 0x63c
+  __TEXT.__objc_methname: 0xb69f
+  __TEXT.__objc_methtype: 0x13ee
+  __TEXT.__objc_stubs: 0x5aa0
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0xe50
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c8
+  __DATA_CONST.__objc_selrefs: 0x2450
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x448
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2160
-  __AUTH_CONST.__objc_const: 0x9110
+  __AUTH_CONST.__cfstring: 0x2460
+  __AUTH_CONST.__objc_const: 0x95c0
   __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x888
-  __DATA.__data: 0xc58
+  __DATA.__objc_ivar: 0x8e0
+  __DATA.__data: 0xd38
   __DATA.__common: 0x8
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6574AC8-02DC-3EF3-AD51-5C79ACFDF771
-  Functions: 2103
-  Symbols:   6378
-  CStrings:  3903
+  UUID: A37D6D8B-BB23-3E41-94BD-CB6770796491
+  Functions: 2167
+  Symbols:   6563
+  CStrings:  4091
 
Symbols:
+ -[AABattery chargingDEOC]
+ -[AAController _personalTranslationMessageReceived:fromDevice:]
+ -[AAController personalTranslationMessageHandler]
+ -[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:]
+ -[AAController setPersonalTranslationMessageHandler:]
+ -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:chargingDEOC:]
+ -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:chargingDEOC:].cold.1
+ -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:chargingDEOC:].cold.2
+ -[AADeviceBatteryInfo dynamicEndOfChargeCapability]
+ -[AADeviceBatteryInfo setDynamicEndOfChargeCapability:]
+ -[AADeviceConfig changeDynamicEndOfChargeState]
+ -[AADeviceConfig enableHearingProtectionPPE]
+ -[AADeviceConfig hearingAidV2SourceRegionSupport]
+ -[AADeviceConfig setChangeDynamicEndOfChargeState:]
+ -[AADeviceConfig setEnableHearingProtectionPPE:]
+ -[AADeviceConfig setHearingAidV2SourceRegionSupport:]
+ -[AAOVADSensorInfo update:].cold.1
+ -[AAOVADSensorInfo update:].cold.2
+ -[AAProxCardsInfo dynamicEndOfChargeNotificationVersion]
+ -[AAProxCardsInfo personalTranslatorVersion]
+ -[AAProxCardsInfo setDynamicEndOfChargeNotificationVersion:]
+ -[AAProxCardsInfo setPersonalTranslatorVersion:]
+ -[AAProximityPairingAccessoryStatusPayload chargingDEOC]
+ -[AAProximityPairingStatusPayloadGeneral chargingDEOCSupported]
+ -[AAProximityPairingStatusPayloadGeneral chargingDEOC]
+ -[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:].cold.2
+ -[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:].cold.1
+ -[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:].cold.2
+ -[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:].cold.3
+ -[AASystemStateMonitor activeHRMDeviceChangedHandler]
+ -[AASystemStateMonitor setActiveHRMDeviceChangedHandler:]
+ -[AudioAccessoryDevice computePersonalTranslatorCapability]
+ -[AudioAccessoryDevice computePersonalTranslatorCapability].cold.1
+ -[AudioAccessoryDevice computePersonalTranslatorCapability].cold.2
+ -[AudioAccessoryDevice dynamicEndOfChargeCapability]
+ -[AudioAccessoryDevice dynamicEndOfChargeEnabled]
+ -[AudioAccessoryDevice dynamicEndOfChargeState]
+ -[AudioAccessoryDevice dynamicEndOfChargeTempDisabled]
+ -[AudioAccessoryDevice hearingAidV2Capability]
+ -[AudioAccessoryDevice hearingProtectionPPECapLevel]
+ -[AudioAccessoryDevice hearingProtectionPPECapability]
+ -[AudioAccessoryDevice hearingProtectionPPEEnabled]
+ -[AudioAccessoryDevice heartRateMonitorCapabilityChanged]
+ -[AudioAccessoryDevice heartRateMonitorCapabilityValueOriginatedFromDevice]
+ -[AudioAccessoryDevice heartRateMonitorCapability]
+ -[AudioAccessoryDevice personalTranslatorCapability]
+ -[AudioAccessoryDevice setDynamicEndOfChargeCapability:]
+ -[AudioAccessoryDevice setDynamicEndOfChargeEnabled:]
+ -[AudioAccessoryDevice setDynamicEndOfChargeState:]
+ -[AudioAccessoryDevice setDynamicEndOfChargeTempDisabled:]
+ -[AudioAccessoryDevice setHearingAidV2Capability:]
+ -[AudioAccessoryDevice setHearingProtectionPPECapLevel:]
+ -[AudioAccessoryDevice setHearingProtectionPPECapability:]
+ -[AudioAccessoryDevice setHearingProtectionPPEEnabled:]
+ -[AudioAccessoryDevice setHeartRateMonitorCapability:]
+ -[AudioAccessoryDevice setHeartRateMonitorCapabilityChanged:]
+ -[AudioAccessoryDevice setHeartRateMonitorCapabilityValueOriginatedFromDevice:]
+ -[AudioAccessoryDevice setPersonalTranslatorCapability:]
+ -[HMDeviceCloudRecordInfo haRegionStatusV2]
+ -[HMDeviceCloudRecordInfo hpPPERegionStatus]
+ -[HMDeviceCloudRecordInfo setHaRegionStatusV2:]
+ -[HMDeviceCloudRecordInfo setHpPPERegionStatus:]
+ GCC_except_table21
+ _OBJC_IVAR_$_AAController._personalTranslationMessageHandler
+ _OBJC_IVAR_$_AADeviceBatteryInfo._dynamicEndOfChargeCapability
+ _OBJC_IVAR_$_AADeviceConfig._changeDynamicEndOfChargeState
+ _OBJC_IVAR_$_AADeviceConfig._enableHearingProtectionPPE
+ _OBJC_IVAR_$_AADeviceConfig._hearingAidV2SourceRegionSupport
+ _OBJC_IVAR_$_AAProxCardsInfo._dynamicEndOfChargeNotificationVersion
+ _OBJC_IVAR_$_AAProxCardsInfo._personalTranslatorVersion
+ _OBJC_IVAR_$_AASystemStateMonitor._activeHRMDeviceChangedHandler
+ _OBJC_IVAR_$_AudioAccessoryDevice._dynamicEndOfChargeCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._dynamicEndOfChargeEnabled
+ _OBJC_IVAR_$_AudioAccessoryDevice._dynamicEndOfChargeState
+ _OBJC_IVAR_$_AudioAccessoryDevice._dynamicEndOfChargeTempDisabled
+ _OBJC_IVAR_$_AudioAccessoryDevice._hearingAidV2Capability
+ _OBJC_IVAR_$_AudioAccessoryDevice._hearingProtectionPPECapLevel
+ _OBJC_IVAR_$_AudioAccessoryDevice._hearingProtectionPPECapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._hearingProtectionPPEEnabled
+ _OBJC_IVAR_$_AudioAccessoryDevice._heartRateMonitorCapability
+ _OBJC_IVAR_$_AudioAccessoryDevice._heartRateMonitorCapabilityChanged
+ _OBJC_IVAR_$_AudioAccessoryDevice._heartRateMonitorCapabilityValueOriginatedFromDevice
+ _OBJC_IVAR_$_AudioAccessoryDevice._personalTranslatorCapability
+ _OBJC_IVAR_$_HMDeviceCloudRecordInfo._haRegionStatusV2
+ _OBJC_IVAR_$_HMDeviceCloudRecordInfo._hpPPERegionStatus
+ ___63-[AAController _personalTranslationMessageReceived:fromDevice:]_block_invoke
+ ___91-[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:]_block_invoke
+ ___91-[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:]_block_invoke.cold.1
+ ___block_literal_global.133
+ ___block_literal_global.136
+ _gLogCategory_AudioAccessoryDevice
+ _objc_msgSend$_batteryStateFromCharging:chargingOBC:chargingDEOC:
+ _objc_msgSend$_personalTranslationMessageReceived:fromDevice:
+ _objc_msgSend$activeHRMDeviceChanged:withSREnabled:
+ _objc_msgSend$changeDynamicEndOfChargeState
+ _objc_msgSend$chargingDEOC
+ _objc_msgSend$chargingDEOCSupported
+ _objc_msgSend$computePersonalTranslatorCapability
+ _objc_msgSend$dynamicEndOfChargeCapability
+ _objc_msgSend$dynamicEndOfChargeEnabled
+ _objc_msgSend$dynamicEndOfChargeState
+ _objc_msgSend$dynamicEndOfChargeTempDisabled
+ _objc_msgSend$enableHearingProtectionPPE
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$hearingAidV2Capability
+ _objc_msgSend$hearingProtectionPPECapLevel
+ _objc_msgSend$hearingProtectionPPECapability
+ _objc_msgSend$hearingProtectionPPECapabilityLevel
+ _objc_msgSend$hearingProtectionPPEEnabled
+ _objc_msgSend$heartRateMonitorCapability
+ _objc_msgSend$personalTranslatorCapability
+ _objc_msgSend$setDynamicEndOfChargeCapability:
+ _objc_msgSend$setDynamicEndOfChargeEnabled:
+ _objc_msgSend$setDynamicEndOfChargeState:
+ _objc_msgSend$setDynamicEndOfChargeTempDisabled:
+ _objc_msgSend$setHearingAidV2Capability:
+ _objc_msgSend$setHearingProtectionPPECapLevel:
+ _objc_msgSend$setHearingProtectionPPECapability:
+ _objc_msgSend$setHearingProtectionPPEEnabled:
+ _objc_msgSend$setHeartRateMonitorCapability:
+ _objc_msgSend$setHeartRateMonitorCapabilityChanged:
+ _objc_msgSend$setHeartRateMonitorCapabilityValueOriginatedFromDevice:
+ _objc_msgSend$setPersonalTranslatorCapability:
+ _os_eligibility_get_domain_answer
- -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:]
- -[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:].cold.1
- GCC_except_table16
- GCC_except_table29
- GCC_except_table30
- ___block_literal_global.129
- ___block_literal_global.132
- _objc_msgSend$_batteryStateFromCharging:chargingOBC:
CStrings:
+ "### XPC receive Personal Translation message failed: %@"
+ "%s event is deprecated"
+ ", DEOC"
+ ", DEOC %s"
+ ", DEOC N %llu"
+ ", DEOC on: %s"
+ ", En HPPPE %s"
+ ", Fit Ed N %llu"
+ ", HA v2 rgn St %d"
+ ", HAv2 Rg %s"
+ ", HP PPE rgn St %d"
+ ", Ps Tr %llu"
+ "-[AAController _personalTranslationMessageReceived:fromDevice:]"
+ "-[AAController _personalTranslationMessageReceived:fromDevice:]_block_invoke"
+ "-[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:]_block_invoke"
+ "-[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:chargingDEOC:]"
+ "-[AAOVADSensorInfo update:]"
+ "-[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:]"
+ "-[AudioAccessoryDevice computePersonalTranslatorCapability]"
+ "Absent"
+ "Bad source BT address: %@"
+ "BatteryDEOC"
+ "Calling HRM capable device route changed handler with device %@"
+ "Calling active HRM changed handler with device %@, HID Device to use %s"
+ "Calling active HRM changed handler with no device"
+ "Charging DEOC"
+ "Charging OBC"
+ "DEOC"
+ "DEOC: "
+ "DualBudLongPress"
+ "DynamicEndOfCharge"
+ "HearingAidV2"
+ "HearingProtectionPPE"
+ "HeartRate"
+ "Incorrect packet subtype: %d"
+ "Invalid Battery status, not charging, but DEOC engaged."
+ "Invalid packetData"
+ "Local"
+ "NO"
+ "No HRM device changed handler"
+ "PPE: "
+ "Personal Translation message received: source %@, data <%@>"
+ "Present"
+ "Registered change in OVAD status: %s -> %s"
+ "T@?,C,N,V_personalTranslationMessageHandler"
+ "T@?,C,V_activeHRMDeviceChangedHandler"
+ "TB,N,V_heartRateMonitorCapabilityChanged"
+ "TB,N,V_heartRateMonitorCapabilityValueOriginatedFromDevice"
+ "TC,N,V_dynamicEndOfChargeCapability"
+ "TC,N,V_hearingAidV2Capability"
+ "TC,N,V_hearingProtectionPPECapability"
+ "TC,N,V_heartRateMonitorCapability"
+ "TC,N,V_personalTranslatorCapability"
+ "TC,V_haRegionStatusV2"
+ "TC,V_hpPPERegionStatus"
+ "TI,N,V_hearingProtectionPPECapLevel"
+ "TQ,V_dynamicEndOfChargeNotificationVersion"
+ "TQ,V_personalTranslatorVersion"
+ "Tc,N,V_changeDynamicEndOfChargeState"
+ "Tc,N,V_dynamicEndOfChargeEnabled"
+ "Tc,N,V_dynamicEndOfChargeState"
+ "Tc,N,V_dynamicEndOfChargeTempDisabled"
+ "Tc,N,V_enableHearingProtectionPPE"
+ "Tc,N,V_hearingAidV2SourceRegionSupport"
+ "Tc,N,V_hearingProtectionPPEEnabled"
+ "Virtual"
+ "YES"
+ "_activeHRMDeviceChangedHandler"
+ "_batteryStateFromCharging:chargingOBC:chargingDEOC:"
+ "_changeDynamicEndOfChargeState"
+ "_dynamicEndOfChargeCapability"
+ "_dynamicEndOfChargeEnabled"
+ "_dynamicEndOfChargeNotificationVersion"
+ "_dynamicEndOfChargeState"
+ "_dynamicEndOfChargeTempDisabled"
+ "_enableHearingProtectionPPE"
+ "_haRegionStatusV2"
+ "_hearingAidV2Capability"
+ "_hearingAidV2SourceRegionSupport"
+ "_hearingProtectionPPECapLevel"
+ "_hearingProtectionPPECapability"
+ "_hearingProtectionPPEEnabled"
+ "_heartRateMonitorCapability"
+ "_heartRateMonitorCapabilityChanged"
+ "_heartRateMonitorCapabilityValueOriginatedFromDevice"
+ "_hpPPERegionStatus"
+ "_personalTranslationMessageHandler"
+ "_personalTranslationMessageReceived:fromDevice:"
+ "_personalTranslatorCapability"
+ "_personalTranslatorVersion"
+ "activeHRMDeviceChangedHandler"
+ "cDEC"
+ "changeDynamicEndOfChargeState"
+ "chargingDEOC"
+ "chargingDEOCSupported"
+ "computePersonalTranslatorCapability"
+ "computePersonalTranslatorCapability isPersonalTranslationEligible %@, Computed: %@, Forced: %@"
+ "computePersonalTranslatorCapability to return unsupported due to airpods capability check failure"
+ "computePersonalTranslatorCapability: Unable to determine eligibility due to error %d"
+ "dcTD"
+ "decC"
+ "decN"
+ "decc"
+ "deoE"
+ "deoS"
+ "dynamicEndOfChargeCapability"
+ "dynamicEndOfChargeEnabled"
+ "dynamicEndOfChargeNotificationVersion"
+ "dynamicEndOfChargeState"
+ "dynamicEndOfChargeTempDisabled"
+ "enableHearingProtectionPPE"
+ "fitEdN"
+ "getBytes:length:"
+ "hV2R"
+ "haR2"
+ "haRegionStatusV2"
+ "haV2"
+ "hearingAidV2Capability"
+ "hearingAidV2SourceRegionSupport"
+ "hearingProtectionPPECapLevel"
+ "hearingProtectionPPECapability"
+ "hearingProtectionPPECapabilityLevel"
+ "hearingProtectionPPEEnabled"
+ "heartRateMonitorCapability"
+ "heartRateMonitorCapabilityChanged"
+ "heartRateMonitorCapabilityValueOriginatedFromDevice"
+ "hk wr %s"
+ "hpPPERegionStatus"
+ "hpPR"
+ "hrCp"
+ "lvl %u, "
+ "personalTranslationMessageHandler"
+ "personalTranslatorCapability"
+ "personalTranslatorVersion"
+ "ppeC"
+ "ppeE"
+ "ppeL"
+ "prT"
+ "pt %s, "
+ "ptCP"
+ "q28@0:8B16B20B24"
+ "send DEOCTempDisableInterval message to destination %@"
+ "sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:"
+ "setActiveHRMDeviceChangedHandler:"
+ "setChangeDynamicEndOfChargeState:"
+ "setDynamicEndOfChargeCapability:"
+ "setDynamicEndOfChargeEnabled:"
+ "setDynamicEndOfChargeNotificationVersion:"
+ "setDynamicEndOfChargeState:"
+ "setDynamicEndOfChargeTempDisabled:"
+ "setEnableHearingProtectionPPE:"
+ "setHaRegionStatusV2:"
+ "setHearingAidV2Capability:"
+ "setHearingAidV2SourceRegionSupport:"
+ "setHearingProtectionPPECapLevel:"
+ "setHearingProtectionPPECapability:"
+ "setHearingProtectionPPEEnabled:"
+ "setHeartRateMonitorCapability:"
+ "setHeartRateMonitorCapabilityChanged:"
+ "setHeartRateMonitorCapabilityValueOriginatedFromDevice:"
+ "setHpPPERegionStatus:"
+ "setPersonalTranslationMessageHandler:"
+ "setPersonalTranslatorCapability:"
+ "setPersonalTranslatorVersion:"
+ "st %s, "
+ "v2 cap %s, "
+ "\x82"
+ "\xf0."
- "-[AADeviceBatteryInfo _batteryStateFromCharging:chargingOBC:]"
- "_batteryStateFromCharging:chargingOBC:"
- "q24@0:8B16B20"
- "r"
- "\xfe"

```
