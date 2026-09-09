## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

 3486.2.4.0.0
-  __TEXT.__text: 0x1dc330
-  __TEXT.__objc_methlist: 0x10ae0
+  __TEXT.__text: 0x1e6bb8
+  __TEXT.__objc_methlist: 0x111c8
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x2641e
-  __TEXT.__oslogstring: 0x14c39
-  __TEXT.__gcc_except_tab: 0x258c
+  __TEXT.__cstring: 0x2694b
+  __TEXT.__oslogstring: 0x15b6e
+  __TEXT.__gcc_except_tab: 0x2598
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3b88
+  __TEXT.__unwind_info: 0x3c58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4480
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__const: 0x4580
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad78
+  __DATA_CONST.__objc_selrefs: 0xb208
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2c8
-  __DATA_CONST.__objc_arraydata: 0x159f0
-  __DATA_CONST.__got: 0xf70
+  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_arraydata: 0x163c8
+  __DATA_CONST.__got: 0xf80
   __AUTH_CONST.__const: 0x1a40
-  __AUTH_CONST.__cfstring: 0x33740
-  __AUTH_CONST.__objc_const: 0x15dd0
+  __AUTH_CONST.__cfstring: 0x33f80
+  __AUTH_CONST.__objc_const: 0x168c0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x28b0
-  __AUTH_CONST.__objc_dictobj: 0x3a70
+  __AUTH_CONST.__objc_intobj: 0x28c8
+  __AUTH_CONST.__objc_dictobj: 0x3ac0
   __AUTH_CONST.__objc_doubleobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x2e38
-  __AUTH_CONST.__auth_got: 0xdf8
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x15f8
+  __AUTH_CONST.__objc_arrayobj: 0x2fa0
+  __AUTH_CONST.__auth_got: 0xe00
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x16c8
   __DATA.__data: 0x580
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8612
-  Symbols:   16110
-  CStrings:  8944
+  Functions: 8831
+  Symbols:   16484
+  CStrings:  9088
 
Symbols:
+ +[PLBatteryAgent entryEventBackwardDefinitionShelfLifeModeAutoEntry]
+ +[PLBatteryAgent entryEventBackwardDefinitionShelfLifeModeExitCounters]
+ +[PLDisplayAgent entryEventBackwardDefinitionAPLStatsX]
+ +[PLDisplayAgent entryEventForwardDefinitionDisplayX]
+ +[PLDisplayAgent entryEventPointDefinitionDisplayX]
+ +[PLDisplayAgent secondaryCADisplay]
+ +[PLEventBackwardBatteryEntry entryKeyPack0]
+ +[PLEventBackwardBatteryEntry entryKeyPack1]
+ +[PLScreenStateAgent entryEventBackwardDefinitionBacklightStateChangeX]
+ +[PLScreenStateAgent entryEventForwardScreenStateX]
+ -[PLAppTimeService displayCallbackX]
+ -[PLAppTimeService screenstateCallbackX]
+ -[PLAppTimeService setDisplayCallbackX:]
+ -[PLAppTimeService setScreenstateCallbackX:]
+ -[PLBatteryAgent batteryPackConfigDataLogged]
+ -[PLBatteryAgent logEventBackwardRebalanceWithRawData:hwBypassByChargerID:]
+ -[PLBatteryAgent logShelfLifeModeFromBatteryData:autoEntryTableName:exitCountersTableName:]
+ -[PLBatteryAgent logShelfLifeModeWithRawData:]
+ -[PLBatteryAgent logTrustedBatteryHealthForPack:toTableName:]
+ -[PLBatteryAgent serialNumber2]
+ -[PLBatteryAgent setBatteryPackConfigDataLogged:]
+ -[PLBatteryAgent setSerialNumber2:]
+ -[PLBatteryAgent setShelfLifeModeLogged:]
+ -[PLBatteryAgent shelfLifeModeLogged]
+ -[PLDisplayAgent ApplicationNotificationX]
+ -[PLDisplayAgent HDRHeadroomX]
+ -[PLDisplayAgent afkEndpointsX]
+ -[PLDisplayAgent afkRoleForService:properties:]
+ -[PLDisplayAgent afkRoleIsDCPSEC:]
+ -[PLDisplayAgent backlightFilterTimerX]
+ -[PLDisplayAgent cbDisplayClientX]
+ -[PLDisplayAgent cleanUpAFKInterfacesX]
+ -[PLDisplayAgent copyCoreBrightnessPropertyForKeyX:]
+ -[PLDisplayAgent displayIdentifierX]
+ -[PLDisplayAgent displayIdentifier]
+ -[PLDisplayAgent displayLuxX]
+ -[PLDisplayAgent displaymNitsX]
+ -[PLDisplayAgent fillInBuiltinDisplayBrightnessParametersX:]
+ -[PLDisplayAgent handleAFKInterfaceIOServiceCallbackX:]
+ -[PLDisplayAgent handleAFKInterfaceMsgX:]
+ -[PLDisplayAgent handleBrightnessClientNotificationX:withValue:]
+ -[PLDisplayAgent iokitBacklightDCPSEC]
+ -[PLDisplayAgent isDisplayOnNowX]
+ -[PLDisplayAgent isSecondaryDisplayIdentifier:]
+ -[PLDisplayAgent lastBuiltinDisplayBrightnessX]
+ -[PLDisplayAgent lastBuiltinDisplayLuxX]
+ -[PLDisplayAgent lastBuiltinDisplaySliderValueX]
+ -[PLDisplayAgent lastBuiltinDisplayTimeX]
+ -[PLDisplayAgent lastForegroundAppAPLX]
+ -[PLDisplayAgent lastScreenStateDisplayX]
+ -[PLDisplayAgent lastmNitsValueX]
+ -[PLDisplayAgent logDisplayAPLX]
+ -[PLDisplayAgent logEventForwardDisplayXWithRawData:withDate:]
+ -[PLDisplayAgent modernDisplayObserverX]
+ -[PLDisplayAgent pendingBacklightEntryDateX]
+ -[PLDisplayAgent pendingBacklightEntryX]
+ -[PLDisplayAgent secondaryBacklightKey]
+ -[PLDisplayAgent secondaryDisplayRef]
+ -[PLDisplayAgent setAfkEndpointsX:]
+ -[PLDisplayAgent setApplicationNotificationX:]
+ -[PLDisplayAgent setBacklightFilterTimerX:]
+ -[PLDisplayAgent setCbDisplayClientX:]
+ -[PLDisplayAgent setDisplayIdentifier:]
+ -[PLDisplayAgent setDisplayIdentifierX:]
+ -[PLDisplayAgent setDisplayLuxX:]
+ -[PLDisplayAgent setDisplaymNitsX:]
+ -[PLDisplayAgent setHDRHeadroomX:]
+ -[PLDisplayAgent setIsDisplayOnNowX:]
+ -[PLDisplayAgent setLastBuiltinDisplayBrightnessX:]
+ -[PLDisplayAgent setLastBuiltinDisplayLuxX:]
+ -[PLDisplayAgent setLastBuiltinDisplaySliderValueX:]
+ -[PLDisplayAgent setLastBuiltinDisplayTimeX:]
+ -[PLDisplayAgent setLastForegroundAppAPLX:]
+ -[PLDisplayAgent setLastScreenStateDisplayX:]
+ -[PLDisplayAgent setLastmNitsValueX:]
+ -[PLDisplayAgent setModernDisplayObserverX:]
+ -[PLDisplayAgent setPendingBacklightEntryDateX:]
+ -[PLDisplayAgent setPendingBacklightEntryX:]
+ -[PLDisplayAgent setSecondaryBacklightKey:]
+ -[PLDisplayAgent setSecondaryDisplayRef:]
+ -[PLDisplayAgent setUAmpsEntryX:]
+ -[PLDisplayAgent setUAmpsFilterTimerX:]
+ -[PLDisplayAgent setupModernCoreBrightnessClientXForCADisplay:]
+ -[PLDisplayAgent uAmpsEntryX]
+ -[PLDisplayAgent uAmpsFilterTimerX]
+ -[PLDisplayAgent updateLastForegroundAppAPLX:]
+ -[PLDisplayIOReportAODStatsX init]
+ -[PLDisplayIOReportStatsX init]
+ -[PLPowerMetricMonitorService _cacheDisplayHWIDs]
+ -[PLPowerMetricMonitorService _parseDisplayAPLXMetricsFromEntry:cacheMetrics:]
+ -[PLPowerMetricMonitorService _setupBrightnessClientX]
+ -[PLPowerMetricMonitorService brightnessPercentX]
+ -[PLPowerMetricMonitorService brightnessPercentageX]
+ -[PLPowerMetricMonitorService brightnessSumX]
+ -[PLPowerMetricMonitorService brightnessX]
+ -[PLPowerMetricMonitorService cbClient]
+ -[PLPowerMetricMonitorService cbDisplayClientX]
+ -[PLPowerMetricMonitorService dcpDisplayStatsX]
+ -[PLPowerMetricMonitorService dcpScanoutStatsX]
+ -[PLPowerMetricMonitorService dcpSwapStatsX]
+ -[PLPowerMetricMonitorService isV68]
+ -[PLPowerMetricMonitorService primaryDisplayHWID]
+ -[PLPowerMetricMonitorService screenStateX]
+ -[PLPowerMetricMonitorService secondaryDisplayHWID]
+ -[PLPowerMetricMonitorService setBrightnessPercentageX:]
+ -[PLPowerMetricMonitorService setBrightnessSumX:]
+ -[PLPowerMetricMonitorService setBrightnessX:]
+ -[PLPowerMetricMonitorService setCbClient:]
+ -[PLPowerMetricMonitorService setCbDisplayClientX:]
+ -[PLPowerMetricMonitorService setDcpDisplayStatsX:]
+ -[PLPowerMetricMonitorService setDcpScanoutStatsX:]
+ -[PLPowerMetricMonitorService setDcpSwapStatsX:]
+ -[PLPowerMetricMonitorService setPrimaryDisplayHWID:]
+ -[PLPowerMetricMonitorService setScreenStateX:]
+ -[PLPowerMetricMonitorService setSecondaryDisplayHWID:]
+ -[PLScreenStateAgent accountForegroundWithMainPrecedence]
+ -[PLScreenStateAgent displayCallbackX]
+ -[PLScreenStateAgent displayStateX]
+ -[PLScreenStateAgent displayValueForLayout:]
+ -[PLScreenStateAgent handleDisplayCallbackX:]
+ -[PLScreenStateAgent isSecondaryDisplay:]
+ -[PLScreenStateAgent lastDisplayLayoutContainsLockScreenX]
+ -[PLScreenStateAgent lastDisplayLayoutX]
+ -[PLScreenStateAgent lastDisplayXLayoutEntries]
+ -[PLScreenStateAgent lastLayoutMonitorEntriesX]
+ -[PLScreenStateAgent lastMainLayoutEntries]
+ -[PLScreenStateAgent lastScreenStateEntriesX]
+ -[PLScreenStateAgent logEventBackwardBacklightStateChangeX:]
+ -[PLScreenStateAgent logEventForwardScreenStateX:]
+ -[PLScreenStateAgent primaryDisplayHWID]
+ -[PLScreenStateAgent secondaryDisplayHWID]
+ -[PLScreenStateAgent setDisplayCallbackX:]
+ -[PLScreenStateAgent setDisplayStateX:]
+ -[PLScreenStateAgent setLastDisplayLayoutContainsLockScreenX:]
+ -[PLScreenStateAgent setLastDisplayLayoutX:]
+ -[PLScreenStateAgent setLastDisplayXLayoutEntries:]
+ -[PLScreenStateAgent setLastLayoutMonitorEntriesX:]
+ -[PLScreenStateAgent setLastMainLayoutEntries:]
+ -[PLScreenStateAgent setLastScreenStateEntriesX:]
+ -[PLScreenStateAgent setPrimaryDisplayHWID:]
+ -[PLScreenStateAgent setSecondaryDisplayHWID:]
+ -[_PLDisplayCBPropertyObserver forDisplayX]
+ -[_PLDisplayCBPropertyObserver setForDisplayX:]
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table154
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table226
+ GCC_except_table228
+ GCC_except_table261
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table275
+ GCC_except_table281
+ GCC_except_table287
+ GCC_except_table298
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table337
+ GCC_except_table62
+ _IORegistryEntryGetName
+ _OBJC_CLASS_$_PLDisplayIOReportAODStatsX
+ _OBJC_CLASS_$_PLDisplayIOReportStatsX
+ _OBJC_IVAR_$_PLAppTimeService._displayCallbackX
+ _OBJC_IVAR_$_PLAppTimeService._screenstateCallbackX
+ _OBJC_IVAR_$_PLBatteryAgent._batteryPackConfigDataLogged
+ _OBJC_IVAR_$_PLBatteryAgent._serialNumber2
+ _OBJC_IVAR_$_PLBatteryAgent._shelfLifeModeLogged
+ _OBJC_IVAR_$_PLDisplayAgent._ApplicationNotificationX
+ _OBJC_IVAR_$_PLDisplayAgent._HDRHeadroomX
+ _OBJC_IVAR_$_PLDisplayAgent._afkEndpointsX
+ _OBJC_IVAR_$_PLDisplayAgent._backlightFilterTimerX
+ _OBJC_IVAR_$_PLDisplayAgent._cbDisplayClientX
+ _OBJC_IVAR_$_PLDisplayAgent._displayIdentifier
+ _OBJC_IVAR_$_PLDisplayAgent._displayIdentifierX
+ _OBJC_IVAR_$_PLDisplayAgent._displayLuxX
+ _OBJC_IVAR_$_PLDisplayAgent._displaymNitsX
+ _OBJC_IVAR_$_PLDisplayAgent._iokitBacklightDCPSEC
+ _OBJC_IVAR_$_PLDisplayAgent._isDisplayOnNowX
+ _OBJC_IVAR_$_PLDisplayAgent._lastBuiltinDisplayBrightnessX
+ _OBJC_IVAR_$_PLDisplayAgent._lastBuiltinDisplayLuxX
+ _OBJC_IVAR_$_PLDisplayAgent._lastBuiltinDisplaySliderValueX
+ _OBJC_IVAR_$_PLDisplayAgent._lastBuiltinDisplayTimeX
+ _OBJC_IVAR_$_PLDisplayAgent._lastForegroundAppAPLX
+ _OBJC_IVAR_$_PLDisplayAgent._lastScreenStateDisplayX
+ _OBJC_IVAR_$_PLDisplayAgent._lastmNitsValueX
+ _OBJC_IVAR_$_PLDisplayAgent._modernDisplayObserverX
+ _OBJC_IVAR_$_PLDisplayAgent._pendingBacklightEntryDateX
+ _OBJC_IVAR_$_PLDisplayAgent._pendingBacklightEntryX
+ _OBJC_IVAR_$_PLDisplayAgent._secondaryBacklightKey
+ _OBJC_IVAR_$_PLDisplayAgent._secondaryDisplayRef
+ _OBJC_IVAR_$_PLDisplayAgent._uAmpsEntryX
+ _OBJC_IVAR_$_PLDisplayAgent._uAmpsFilterTimerX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._brightnessPercentageX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._brightnessSumX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._brightnessX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._cbClient
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._cbDisplayClientX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._dcpDisplayStatsX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._dcpScanoutStatsX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._dcpSwapStatsX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._primaryDisplayHWID
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._screenStateX
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._secondaryDisplayHWID
+ _OBJC_IVAR_$_PLScreenStateAgent._displayCallbackX
+ _OBJC_IVAR_$_PLScreenStateAgent._displayStateX
+ _OBJC_IVAR_$_PLScreenStateAgent._lastDisplayLayoutContainsLockScreenX
+ _OBJC_IVAR_$_PLScreenStateAgent._lastDisplayLayoutX
+ _OBJC_IVAR_$_PLScreenStateAgent._lastDisplayXLayoutEntries
+ _OBJC_IVAR_$_PLScreenStateAgent._lastLayoutMonitorEntriesX
+ _OBJC_IVAR_$_PLScreenStateAgent._lastMainLayoutEntries
+ _OBJC_IVAR_$_PLScreenStateAgent._lastScreenStateEntriesX
+ _OBJC_IVAR_$_PLScreenStateAgent._primaryDisplayHWID
+ _OBJC_IVAR_$_PLScreenStateAgent._secondaryDisplayHWID
+ _OBJC_IVAR_$__PLDisplayCBPropertyObserver._forDisplayX
+ _OBJC_METACLASS_$_PLDisplayIOReportAODStatsX
+ _OBJC_METACLASS_$_PLDisplayIOReportStatsX
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ __OBJC_$_INSTANCE_METHODS_PLDisplayIOReportAODStatsX
+ __OBJC_$_INSTANCE_METHODS_PLDisplayIOReportStatsX
+ __OBJC_CLASS_RO_$_PLDisplayIOReportAODStatsX
+ __OBJC_CLASS_RO_$_PLDisplayIOReportStatsX
+ __OBJC_METACLASS_RO_$_PLDisplayIOReportAODStatsX
+ __OBJC_METACLASS_RO_$_PLDisplayIOReportStatsX
+ ___22-[PLDisplayAgent init]_block_invoke_4
+ ___43-[PLPowerMetricMonitorService _setUpAgents]_block_invoke_10
+ ___44-[PLAppTimeService initOperatorDependancies]_block_invoke_8
+ ___50-[PLScreenStateAgent logEventForwardScreenStateX:]_block_invoke
+ ___55-[PLDisplayAgent handleAFKInterfaceIOServiceCallbackX:]_block_invoke
+ ___64-[PLDisplayAgent handleBrightnessClientNotificationX:withValue:]_block_invoke
+ ___75-[PLBatteryAgent logEventBackwardRebalanceWithRawData:hwBypassByChargerID:]_block_invoke
+ ___78-[PLPowerMetricMonitorService _parseDisplayAPLXMetricsFromEntry:cacheMetrics:]_block_invoke
+ ___78-[PLPowerMetricMonitorService _parseDisplayAPLXMetricsFromEntry:cacheMetrics:]_block_invoke_2
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8s32l8r56l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ _displaySync_block_invoke_2.screenStateEntriesCounterX
+ _kPLBB25
+ _kPLBatteryAgentEventBackwardNameBatteryPack0
+ _kPLBatteryAgentEventBackwardNameBatteryPack1
+ _kPLBatteryAgentEventBackwardNameChargerData1
+ _kPLBatteryAgentEventBackwardNameRebalance
+ _kPLBatteryAgentEventBackwardNameShelfLifeModeAutoEntry
+ _kPLBatteryAgentEventBackwardNameShelfLifeModeAutoEntryX
+ _kPLBatteryAgentEventBackwardNameShelfLifeModeExitCounters
+ _kPLBatteryAgentEventBackwardNameShelfLifeModeExitCountersX
+ _kPLBatteryAgentEventBackwardNameTrustedBatteryHealth0
+ _kPLBatteryAgentEventBackwardNameTrustedBatteryHealth1
+ _kPLBatteryAgentEventNoneBatteryConfigPack0
+ _kPLBatteryAgentEventNoneBatteryConfigPack1
+ _kPLBatteryAgentEventPointNameBatteryShutdownPack1
+ _kPLBatteryAgentStringLastShutdownSystemTimestamp1
+ _kPLDisplayAgentEventBackwardNameAPLStatsX
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke.classDebugEnabled
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke.defaultOnce
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke_2.classDebugEnabled
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke_2.defaultOnce
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke_3.classDebugEnabled
+ _kPLDisplayAgentEventBackwardNameDCPAODstatsX_block_invoke_3.defaultOnce
+ _kPLDisplayAgentEventForwardNameDisplayX
+ _kPLDisplayAgentEventPointNameDisplayX
+ _kPLScreenStateAgentEventBackwardNameBacklightStateChangeX
+ _kPLScreenStateAgentEventForwardNameScreenStateX
+ _objc_msgSend$HDRHeadroomX
+ _objc_msgSend$_cacheDisplayHWIDs
+ _objc_msgSend$_parseDisplayAPLXMetricsFromEntry:cacheMetrics:
+ _objc_msgSend$_setupBrightnessClientX
+ _objc_msgSend$accountForegroundWithMainPrecedence
+ _objc_msgSend$afkEndpointsX
+ _objc_msgSend$afkRoleForService:properties:
+ _objc_msgSend$backlightFilterTimerX
+ _objc_msgSend$batteryPackConfigDataLogged
+ _objc_msgSend$brightnessPercentageX
+ _objc_msgSend$brightnessSumX
+ _objc_msgSend$brightnessX
+ _objc_msgSend$cbDisplayClientX
+ _objc_msgSend$cleanUpAFKInterfacesX
+ _objc_msgSend$copyCoreBrightnessPropertyForKeyX:
+ _objc_msgSend$dcpDisplayStatsX
+ _objc_msgSend$dcpScanoutStatsX
+ _objc_msgSend$dcpSwapStatsX
+ _objc_msgSend$displayConfiguration
+ _objc_msgSend$displayIdentifierX
+ _objc_msgSend$displayPowerX
+ _objc_msgSend$displayStateX
+ _objc_msgSend$displayValueForLayout:
+ _objc_msgSend$enrichedSnapshotFromChargerService:
+ _objc_msgSend$enrichedSnapshotFromPackService:
+ _objc_msgSend$entryEventBackwardDefinitionAPLStatsX
+ _objc_msgSend$entryEventBackwardDefinitionBacklightStateChangeX
+ _objc_msgSend$entryEventBackwardDefinitionRebalance
+ _objc_msgSend$entryEventBackwardDefinitionShelfLifeModeAutoEntry
+ _objc_msgSend$entryEventBackwardDefinitionShelfLifeModeExitCounters
+ _objc_msgSend$entryEventForwardDefinitionDisplayX
+ _objc_msgSend$entryEventForwardScreenStateX
+ _objc_msgSend$entryEventPointDefinitionDisplayX
+ _objc_msgSend$entryKeyPack0
+ _objc_msgSend$entryKeyPack1
+ _objc_msgSend$fillInBuiltinDisplayBrightnessParametersX:
+ _objc_msgSend$forDisplayX
+ _objc_msgSend$fusePackCurrentAccumulators:fusedAccumulator:fusedCount:
+ _objc_msgSend$handleAFKInterfaceIOServiceCallbackX:
+ _objc_msgSend$handleAFKInterfaceMsgX:
+ _objc_msgSend$handleBrightnessClientNotificationX:withValue:
+ _objc_msgSend$handleDisplayCallbackX:
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$iokitBacklightDCPSEC
+ _objc_msgSend$isSecondaryDisplay:
+ _objc_msgSend$isSecondaryDisplayIdentifier:
+ _objc_msgSend$isV68
+ _objc_msgSend$lastBuiltinDisplayBrightnessX
+ _objc_msgSend$lastBuiltinDisplayLuxX
+ _objc_msgSend$lastBuiltinDisplaySliderValueX
+ _objc_msgSend$lastBuiltinDisplayTimeX
+ _objc_msgSend$lastDisplayLayoutContainsLockScreenX
+ _objc_msgSend$lastDisplayLayoutX
+ _objc_msgSend$lastDisplayXLayoutEntries
+ _objc_msgSend$lastLayoutMonitorEntriesX
+ _objc_msgSend$lastMainLayoutEntries
+ _objc_msgSend$lastScreenStateDisplay
+ _objc_msgSend$lastScreenStateDisplayX
+ _objc_msgSend$lastScreenStateEntriesX
+ _objc_msgSend$logDisplayAPLX
+ _objc_msgSend$logEventBackwardBacklightStateChangeX:
+ _objc_msgSend$logEventBackwardRebalanceWithRawData:hwBypassByChargerID:
+ _objc_msgSend$logEventForwardDisplayXWithRawData:withDate:
+ _objc_msgSend$logEventForwardScreenStateX:
+ _objc_msgSend$logShelfLifeModeFromBatteryData:autoEntryTableName:exitCountersTableName:
+ _objc_msgSend$logShelfLifeModeWithRawData:
+ _objc_msgSend$logTrustedBatteryHealthForPack:toTableName:
+ _objc_msgSend$modernDisplayObserverX
+ _objc_msgSend$operators
+ _objc_msgSend$pendingBacklightEntryDateX
+ _objc_msgSend$pendingBacklightEntryX
+ _objc_msgSend$prevRebalanceErrorFlags
+ _objc_msgSend$prevRebalanceNotRebalancingReason
+ _objc_msgSend$primaryDisplayHWID
+ _objc_msgSend$screenStateX
+ _objc_msgSend$secondaryCADisplay
+ _objc_msgSend$secondaryDisplayHWID
+ _objc_msgSend$secondaryDisplayRef
+ _objc_msgSend$serialNumber2
+ _objc_msgSend$setAfkEndpointsX:
+ _objc_msgSend$setApplicationNotificationX:
+ _objc_msgSend$setBacklightFilterTimerX:
+ _objc_msgSend$setBatteryPackConfigDataLogged:
+ _objc_msgSend$setBrightnessPercentageX:
+ _objc_msgSend$setBrightnessSumX:
+ _objc_msgSend$setBrightnessX:
+ _objc_msgSend$setCbDisplayClientX:
+ _objc_msgSend$setDcpDisplayStatsX:
+ _objc_msgSend$setDcpScanoutStatsX:
+ _objc_msgSend$setDcpSwapStatsX:
+ _objc_msgSend$setDisplayAPLX:
+ _objc_msgSend$setDisplayCallbackX:
+ _objc_msgSend$setDisplayCostX:
+ _objc_msgSend$setDisplayEnergyX:
+ _objc_msgSend$setDisplayFPSX:
+ _objc_msgSend$setDisplayIdentifier:
+ _objc_msgSend$setDisplayIdentifierX:
+ _objc_msgSend$setDisplayLuxX:
+ _objc_msgSend$setDisplayPowerX:
+ _objc_msgSend$setDisplayStateX:
+ _objc_msgSend$setDisplaymNitsX:
+ _objc_msgSend$setForDisplayX:
+ _objc_msgSend$setHDRHeadroomX:
+ _objc_msgSend$setIsDisplayOnNowX:
+ _objc_msgSend$setLastBuiltinDisplayBrightnessX:
+ _objc_msgSend$setLastBuiltinDisplayLuxX:
+ _objc_msgSend$setLastBuiltinDisplaySliderValueX:
+ _objc_msgSend$setLastBuiltinDisplayTimeX:
+ _objc_msgSend$setLastDisplayLayoutContainsLockScreenX:
+ _objc_msgSend$setLastDisplayLayoutX:
+ _objc_msgSend$setLastDisplayXLayoutEntries:
+ _objc_msgSend$setLastForegroundAppAPLX:
+ _objc_msgSend$setLastLayoutMonitorEntriesX:
+ _objc_msgSend$setLastMainLayoutEntries:
+ _objc_msgSend$setLastScreenStateDisplay:
+ _objc_msgSend$setLastScreenStateDisplayX:
+ _objc_msgSend$setLastScreenStateEntriesX:
+ _objc_msgSend$setModernDisplayObserverX:
+ _objc_msgSend$setPendingBacklightEntryDateX:
+ _objc_msgSend$setPendingBacklightEntryX:
+ _objc_msgSend$setPrevRebalanceErrorFlags:
+ _objc_msgSend$setPrevRebalanceNotRebalancingReason:
+ _objc_msgSend$setPrimaryDisplayHWID:
+ _objc_msgSend$setScanoutFPSX:
+ _objc_msgSend$setScreenStateX:
+ _objc_msgSend$setScreenstateCallbackX:
+ _objc_msgSend$setSecondaryDisplayHWID:
+ _objc_msgSend$setSecondaryDisplayRef:
+ _objc_msgSend$setSerialNumber2:
+ _objc_msgSend$setShelfLifeModeLogged:
+ _objc_msgSend$setWeightOnScreenX:
+ _objc_msgSend$setupModernCoreBrightnessClientXForCADisplay:
+ _objc_msgSend$sharedBacklightForDisplay:
+ _objc_msgSend$shelfLifeModeLogged
+ _objc_msgSend$uniqueId
+ _objc_msgSend$updateLastForegroundAppAPLX:
- GCC_except_table136
- GCC_except_table140
- GCC_except_table141
- GCC_except_table153
- GCC_except_table158
- GCC_except_table167
- GCC_except_table172
- GCC_except_table175
- GCC_except_table187
- GCC_except_table193
- GCC_except_table211
- GCC_except_table220
- GCC_except_table248
- GCC_except_table257
- GCC_except_table260
- GCC_except_table262
- GCC_except_table271
- GCC_except_table277
- GCC_except_table278
- GCC_except_table325
- GCC_except_table328
- GCC_except_table332
- GCC_except_table54
- ___26-[PLScreenStateAgent init]_block_invoke_5
- ___51-[PLBatteryAgent logCurrentAccumulatorWithRawData:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- _kPRearNits_block_invoke.classDebugEnabled
- _kPRearNits_block_invoke.defaultOnce
- _kPRearNits_block_invoke_2.classDebugEnabled
- _kPRearNits_block_invoke_2.defaultOnce
- _kPRearNits_block_invoke_3.classDebugEnabled
- _kPRearNits_block_invoke_3.defaultOnce
CStrings:
+ "#"
+ "%@-%llx"
+ "/\n"
+ "1946944"
+ "APLStatsX"
+ "AutoEntryCounterCase2"
+ "AutoEntryCounterCase3"
+ "BacklightStateChangeX"
+ "BatteryConfigPack0"
+ "BatteryConfigPack1"
+ "BatteryLife"
+ "BatteryPack0"
+ "BatteryPack1"
+ "BatteryShutdownPack1"
+ "BrightnessClientX created, displayId=%u"
+ "BrightnessClientX setup: CBClient activate failed: %{public}@"
+ "BrightnessClientX setup: CBClient init failed"
+ "BrightnessClientX setup: newDisplayClientForID:%u failed: %{public}@"
+ "ButtonPressExitCounter"
+ "CACHED_CSI_DUAL_ANTENNA_DURATION"
+ "CACHED_CSI_ENABLED_DURATION"
+ "CACHED_CSI_MAC_ACTIVE_DURATION"
+ "CBDisplayClient created for DisplayX, displayId=%u"
+ "CBDisplayClient: no CADisplay provided for DisplayX"
+ "CBDisplayClient: primary cbClient not yet initialized; DisplayX setup deferred"
+ "CSIDualAntennaDuration"
+ "CSIEnabledDuration"
+ "CSIMacActiveDuration"
+ "Cached display HWIDs — primary=%{public}@ secondary=%{public}@"
+ "ChargerConnectExitCounter"
+ "ChargerData1"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "CurrentAccumulator: expected %u packs, gathered %lu; skipping sample"
+ "CurrentAccumulator: failed to match AppleSmartBatteryPack %x"
+ "DCPAODstatsX"
+ "DCPSEC"
+ "Detected aggregate display reference (ID: 0x%llx, name: %@), using primary display"
+ "Display reference matches known display but not in map: %@"
+ "DisplayDynamicX"
+ "DisplayX"
+ "DisplayX AFK Data: %@"
+ "DisplayX AFK Registry ID: %llu"
+ "DisplayX AFK input buffer is empty"
+ "DisplayX AFK match: registryID=%llu role='%{public}@'"
+ "DisplayX AFK matched role '%{public}@'"
+ "DisplayX AFK msg is not a dictionary"
+ "DisplayX AFK unserialize error: %@"
+ "DisplayX AFKInterface activated"
+ "DisplayX CBDisplayClient observer registered for %lu keys"
+ "DisplayX CBDisplayClient registerObserver failed: %{public}@; tearing down"
+ "DisplayX Reported mNits:%f brightness:%f %%:%f"
+ "DisplayX entry: %@"
+ "DisplayX final data to log: %@"
+ "DisplayX flush: writing pending entry: %@ date: %@"
+ "DisplayX received AFK msg at timestamp: %llu"
+ "DisplayX setup skipped: secondaryCADisplay returned the same displayId (%u) as the primary; refusing to double-bind"
+ "DisplayX: IO object property is not dictionary"
+ "DisplayX: Not logging brightness value: %{public}@"
+ "DisplayX: error getting AFK interface"
+ "DisplayX: error getting IO object properties"
+ "DisplayX: ignoring CB key %{public}@"
+ "DisplayX: received Brightness Notification: %@"
+ "EPRole"
+ "EndpointName"
+ "Erronous spot that we find sth other than primary and secondary display"
+ "Failed to create reference for primary display"
+ "Failed to create reference for secondary display"
+ "Failed to get backlight for primary display"
+ "Failed to get backlight for secondary display"
+ "Failed to retrieve battery trusted dictionary for pack"
+ "Failed to subscribe to IOReport DCP display stats"
+ "Failed to subscribe to IOReport DCP scanout"
+ "Failed to subscribe to IOReport DCP swap"
+ "Found %lu integrated displays"
+ "INSTANT_CSI_DUAL_ANTENNA_DURATION"
+ "INSTANT_CSI_ENABLED_DURATION"
+ "INSTANT_CSI_MAC_ACTIVE_DURATION"
+ "LastSLMExitType"
+ "LastShutdownSystemTimestamp1"
+ "Layout HWID: %{public}@ (primary: %{public}@, secondary: %{public}@)"
+ "MULTI_BATTERY: Failed to get AppleChargerData with result=%x"
+ "MULTI_BATTERY: Failed to get AppleSmartBatteryPack data with result=%x"
+ "MULTI_BATTERY: Logging rebalance entry %@"
+ "MULTI_BATTERY: This device has %d batteries"
+ "MULTI_BATTERY: This device has %d chargers"
+ "MULTI_BATTERY: rawDataMultiBattery=%@"
+ "Primary AFK match: registryID=%llu role='%{public}@'"
+ "Primary HWID: %{public}@, Secondary HWID: %{public}@"
+ "Primary display: %@, last state: %d"
+ "RebalanceData"
+ "RebalanceEnableStatus"
+ "RebalanceErrorFlags"
+ "RebalanceHWBypassFETStatus"
+ "RebalanceHWBypassFETStatus0"
+ "RebalanceHWBypassFETStatus1"
+ "RebalanceInrushCurrentDebug"
+ "RebalanceNotRebalancingReason"
+ "RebalanceOutputStruct"
+ "RebalanceTimeSeconds"
+ "Role"
+ "Routing to PRIMARY display logging"
+ "Routing to SECONDARY display logging"
+ "SECONDARY Display callback - userInfo=%@"
+ "SECONDARY: Display callback - userInfo=%@"
+ "SECONDARY: FBSDisplayLayoutElement currentEntry bundleID: %@"
+ "SECONDARY: LayoutEntries is empty"
+ "SECONDARY: LayoutEntries: %@"
+ "SECONDARY: Logged %d FBSDisplayLayoutElement entries"
+ "SECONDARY: Relogging screen state - displayStateX=%d, containsLockScreen=%d"
+ "SECONDARY: Screen State element's bundleID/identifier is nil"
+ "SECONDARY: calling logEventForwardScreenStateX with displayLayout=%@"
+ "SECONDARY: current FBSDisplayLayoutElement entry was already logged, skipping"
+ "SECONDARY: dts runtime ff enabled=%d, [PLPlatform hasAOD]=%d]"
+ "SECONDARY: element bundleID=%@, entry=%@, displayStateX=%d"
+ "SECONDARY: entry after transformation = %@"
+ "SECONDARY: self.displayStateX=%d, self.lastDisplayLayoutContainsLockScreenX=%d,  self.lastDisplayLayoutX=%@"
+ "ScreenStateX"
+ "Secondary display: %@, last state: %d"
+ "ShelfLifeMode: failed to match AppleSmartBatteryPack %x"
+ "ShelfLifeModeAutoEntry"
+ "ShelfLifeModeAutoEntryX"
+ "ShelfLifeModeExitCounters"
+ "ShelfLifeModeExitCountersX"
+ "Single integrated display, primary HWID: %{public}@"
+ "TrustedBatteryHealth0"
+ "TrustedBatteryHealth1"
+ "Unexpected integrated display count: %lu"
+ "Unexpected number of integrated displays: %d"
+ "V68 SW"
+ "bb25"
+ "com.apple.battery.RebalanceData"
+ "displayIdentifier"
+ "endpoint-name"
+ "logDisplayAPLX"
+ "newDisplayClientForID:%u failed for DisplayX: %{public}@"
+ "rebalance_enable_status"
+ "rebalance_error_flags"
+ "rebalance_hw_bypass_fet_status_0"
+ "rebalance_hw_bypass_fet_status_1"
+ "rebalance_not_rebalancing_reason"
+ "rebalance_time_seconds"
+ "role"
```
