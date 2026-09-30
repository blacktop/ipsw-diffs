## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0xdaa34
-  __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x8598
-  __TEXT.__const: 0x1828
-  __TEXT.__cstring: 0x38d3e
-  __TEXT.__gcc_except_tab: 0x2af0
-  __TEXT.__oslogstring: 0x765d
-  __TEXT.__unwind_info: 0x2cc8
-  __TEXT.__objc_classname: 0x87e
-  __TEXT.__objc_methname: 0x12b56
-  __TEXT.__objc_methtype: 0x17a1
-  __TEXT.__objc_stubs: 0xf860
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x25b0
-  __DATA_CONST.__objc_classlist: 0x328
+2954.0.0.502.3
+  __TEXT.__text: 0xd9e68
+  __TEXT.__auth_stubs: 0x1ad0
+  __TEXT.__objc_methlist: 0x8840
+  __TEXT.__const: 0x1838
+  __TEXT.__cstring: 0x398c3
+  __TEXT.__oslogstring: 0x756a
+  __TEXT.__gcc_except_tab: 0x28b0
+  __TEXT.__unwind_info: 0x2c98
+  __TEXT.__objc_classname: 0x8a7
+  __TEXT.__objc_methname: 0x12df0
+  __TEXT.__objc_methtype: 0x1890
+  __TEXT.__objc_stubs: 0xf820
+  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f90
+  __DATA_CONST.__objc_selrefs: 0x50b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x38a60
-  __AUTH_CONST.__auth_got: 0xd18
-  __AUTH_CONST.__const: 0x1e20
-  __AUTH_CONST.__cfstring: 0x59940
-  __AUTH_CONST.__objc_const: 0x8f80
-  __AUTH_CONST.__objc_intobj: 0x47a0
-  __AUTH_CONST.__objc_doubleobj: 0x1080
-  __AUTH_CONST.__objc_arrayobj: 0x10c8
-  __AUTH_CONST.__objc_dictobj: 0xe4e8
-  __AUTH.__objc_data: 0x460
+  __DATA_CONST.__objc_arraydata: 0x3a908
+  __AUTH_CONST.__auth_got: 0xd80
+  __AUTH_CONST.__const: 0x2260
+  __AUTH_CONST.__cfstring: 0x5b040
+  __AUTH_CONST.__objc_const: 0x90a0
+  __AUTH_CONST.__objc_intobj: 0x4800
+  __AUTH_CONST.__objc_doubleobj: 0x10c0
+  __AUTH_CONST.__objc_arrayobj: 0x1110
+  __AUTH_CONST.__objc_dictobj: 0xeab0
+  __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x634
-  __DATA.__data: 0x438
-  __DATA.__bss: 0x1b51
+  __DATA.__data: 0x440
+  __DATA.__bss: 0x1739
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xb58
+  __DATA_DIRTY.__objc_data: 0x1b80
+  __DATA_DIRTY.__data: 0x24
+  __DATA_DIRTY.__bss: 0x10c8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
-  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions

   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerlogControl.framework/PowerlogControl

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4823940B-C6E2-3A90-93FE-C3B164796AFA
-  Functions: 4414
-  Symbols:   15653
-  CStrings:  27837
+  UUID: D05E5230-39F9-3023-867E-29EAC02935A5
+  Functions: 4503
+  Symbols:   15788
+  CStrings:  28243
 
Symbols:
+ +[PLAppDeletion iterateMetrics]
+ +[PLGestaltUtilities getBasebandChipset]
+ +[PLGestaltUtilities getBasebandChipset].cold.1
+ +[PLGestaltUtilities getBasebandFirmwareVersion]
+ +[PLGestaltUtilities getBasebandFirmwareVersion].cold.1
+ +[PLGestaltUtilities getBuildVersion]
+ +[PLGestaltUtilities getBuildVersion].cold.1
+ +[PLGestaltUtilities getDeviceClass]
+ +[PLGestaltUtilities getDeviceClass].cold.1
+ +[PLGestaltUtilities getHardwareModel]
+ +[PLGestaltUtilities getHardwareModel].cold.1
+ +[PLGestaltUtilities getHardwarePlatform]
+ +[PLGestaltUtilities getHardwarePlatform].cold.1
+ +[PLGestaltUtilities getInverseDeviceID]
+ +[PLGestaltUtilities getInverseDeviceID].cold.1
+ +[PLGestaltUtilities getNumberOfDCPEXT]
+ +[PLGestaltUtilities getNumberOfDCPEXT].cold.1
+ +[PLGestaltUtilities getProductTypeCode]
+ +[PLGestaltUtilities getProductTypeCode].cold.1
+ +[PLGestaltUtilities getProductType]
+ +[PLGestaltUtilities getProductType].cold.1
+ +[PLGestaltUtilities getUserAssignedDeviceName]
+ +[PLGestaltUtilities getUserAssignedDeviceName].cold.1
+ +[PLGestaltUtilities getWifiChipset]
+ +[PLGestaltUtilities getWifiChipset].cold.1
+ +[PLGestaltUtilities hasANE]
+ +[PLGestaltUtilities hasANE].cold.1
+ +[PLGestaltUtilities hasAOP]
+ +[PLGestaltUtilities hasAOP].cold.1
+ +[PLGestaltUtilities hasAOT]
+ +[PLGestaltUtilities hasAOT].cold.1
+ +[PLGestaltUtilities hasAlwaysListening]
+ +[PLGestaltUtilities hasAlwaysListening].cold.1
+ +[PLGestaltUtilities hasBaseband]
+ +[PLGestaltUtilities hasBaseband].cold.1
+ +[PLGestaltUtilities hasBatteryModuleAuth]
+ +[PLGestaltUtilities hasBatteryModuleAuth].cold.1
+ +[PLGestaltUtilities hasBattery]
+ +[PLGestaltUtilities hasBattery].cold.1
+ +[PLGestaltUtilities hasDCP]
+ +[PLGestaltUtilities hasDCP].cold.1
+ +[PLGestaltUtilities hasDynamicChargingLimit]
+ +[PLGestaltUtilities hasDynamicChargingLimit].cold.1
+ +[PLGestaltUtilities hasFixedChargingLimit]
+ +[PLGestaltUtilities hasFixedChargingLimit].cold.1
+ +[PLGestaltUtilities hasGasGauge]
+ +[PLGestaltUtilities hasGasGauge].cold.1
+ +[PLGestaltUtilities hasInductiveCharging]
+ +[PLGestaltUtilities hasInductiveCharging].cold.1
+ +[PLGestaltUtilities hasLPEM]
+ +[PLGestaltUtilities hasLPEM].cold.1
+ +[PLGestaltUtilities hasLPM]
+ +[PLGestaltUtilities hasLPM].cold.1
+ +[PLGestaltUtilities hasMesa]
+ +[PLGestaltUtilities hasMesa].cold.1
+ +[PLGestaltUtilities hasMessageOnDevice]
+ +[PLGestaltUtilities hasNFC]
+ +[PLGestaltUtilities hasNFC].cold.1
+ +[PLGestaltUtilities hasOrb]
+ +[PLGestaltUtilities hasOrb].cold.1
+ +[PLGestaltUtilities hasPearl]
+ +[PLGestaltUtilities hasPearl].cold.1
+ +[PLGestaltUtilities hasPerseus]
+ +[PLGestaltUtilities hasPerseus].cold.1
+ +[PLGestaltUtilities hasPlatinum]
+ +[PLGestaltUtilities hasPlatinum].cold.1
+ +[PLGestaltUtilities hasRearALS]
+ +[PLGestaltUtilities hasRearALS].cold.1
+ +[PLGestaltUtilities hasSleepMedia]
+ +[PLGestaltUtilities hasWirelessCharger]
+ +[PLGestaltUtilities hasWirelessCharger].cold.1
+ +[PLGestaltUtilities hasWristTemperature]
+ +[PLGestaltUtilities hasWristTemperature].cold.1
+ +[PLGestaltUtilities is64Bit]
+ +[PLGestaltUtilities is64Bit].cold.1
+ +[PLGestaltUtilities isAppleTV]
+ +[PLGestaltUtilities isAppleVision]
+ +[PLGestaltUtilities isComputeModule]
+ +[PLGestaltUtilities isDevBoard]
+ +[PLGestaltUtilities isDevBoard].cold.1
+ +[PLGestaltUtilities isHomePod]
+ +[PLGestaltUtilities isMac]
+ +[PLGestaltUtilities isVirtualDevice]
+ +[PLGestaltUtilities isVirtualDevice].cold.1
+ +[PLGestaltUtilities isWatch]
+ +[PLGestaltUtilities isiPad]
+ +[PLGestaltUtilities isiPhone]
+ +[PLGestaltUtilities isiPod]
+ +[PLMetricdLifecycleManager sharedManager]
+ +[PLMetricdLifecycleManager sharedManager].cold.1
+ +[PLModelingUtilities criticalBatteryLevel]
+ +[PLOSMetricsUtilities addCounter:withValue:]
+ +[PLOSMetricsUtilities addDimensions:withKey:withValue:]
+ +[PLOSMetricsUtilities addDimensions:withKey:withValue:].cold.1
+ +[PLOSMetricsUtilities createCounter:withLabel:]
+ +[PLOSMetricsUtilities createCounter:withLabel:withDimensions:withFlags:]
+ +[PLOSMetricsUtilities createDimensions:]
+ +[PLOSMetricsUtilities createGauge:withLabel:]
+ +[PLOSMetricsUtilities createGauge:withLabel:withDimensions:withLevel:withFlags:]
+ +[PLOSMetricsUtilities createHistogram:withLabel:withBins:withInterval:]
+ +[PLOSMetricsUtilities createHistogram:withLabel:withDimensions:withLevel:withBins:withInterval:withFlags:]
+ +[PLOSMetricsUtilities createMetricGroup:withDimensions:]
+ +[PLOSMetricsUtilities setGauge:withValue:]
+ +[PLOSMetricsUtilities setHistogram:withValue:]
+ +[PLOSMetricsUtilities subtractCounter:withValue:]
+ +[PLPlatform hasAOP2]
+ +[PLPlatform hasAOP2].cold.1
+ +[PLPlatform hasAOP]
+ +[PLPlatform hasAOP].cold.1
+ +[PLPlatform isUsingAnOlderWifiChip]
+ +[PLPlatform isUsingAnOlderWifiChip].cold.1
+ +[PLUtilities dateFromnSecEpoch:]
+ +[PLUtilities experimentGroup]
+ +[PLUtilities experimentGroup].cold.1
+ +[PLUtilities hasInternalKey:]
+ +[PLUtilities hasInternalKey:].cold.1
+ +[PLUtilities hasInternalKey:].cold.2
+ +[PLUtilities hasInternalKey]
+ +[PLUtilities hasInternalKey].cold.1
+ +[PLUtilities isPerfPowerMetricd]
+ +[PLUtilities isPerfPowerMetricd].cold.1
+ +[PLUtilities isPowerexceptionsd]
+ +[PLUtilities isPowerexceptionsd].cold.1
+ +[PLUtilities machTimeFromSeconds:]
+ +[PLUtilities machTimeFromSeconds:].cold.1
+ +[PLUtilities machTimeFromSeconds:].cold.2
+ +[PLUtilities machTimeFromSeconds:].cold.3
+ +[PLUtilities machTimeFromSeconds:].cold.4
+ +[PLUtilities pUUIDForPid:]
+ +[PPSEntryKey allAppIdentiferKeysForEntryKey:]
+ +[PPSEntryKey hasAppIdentiferKeys:]
+ +[PPSFileUtilities containerPath]
+ +[PPSFileUtilities containerPath].cold.1
+ +[PPSFileUtilities(APFS) _debugStringForPurgeableLabel:]
+ +[PPSFileUtilities(APFS) _purgeableLabelWithUrgency:startDate:]
+ +[PPSFileUtilities(APFS) markAsPurgeable:label:]
+ +[PPSFileUtilities(APFS) markAsPurgeable:urgency:startDate:]
+ +[PPSFileUtilities(APFS) supportsEnhancedAPFS]
+ +[PPSFileUtilities(APFS) supportsEnhancedAPFS].cold.1
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:]
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.1
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.2
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.3
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.4
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.5
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.6
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.7
+ -[PLABMClient triggerPeriodicMetrics:andprofileId:].cold.8
+ -[PLCoreStorage init].cold.6
+ -[PLMetricdLifecycleManager init]
+ -[PLMetricdLifecycleManager isActive]
+ -[PLMetricdLifecycleManager setIsActive:]
+ -[PLMetricdLifecycleManager signalActive]
+ -[PLMetricdLifecycleManager signalInactive]
+ -[PLMetricdLifecycleManager stopMetricd]
+ -[PLSubmissionFileBG copyAndPrepareLog].cold.10
+ -[PLSubmissionFileBG copyAndPrepareLog].cold.11
+ -[PLSubmissionFileBG copyAndPrepareLog].cold.9
+ -[PPSSQLStorage setupDBConnections].cold.6
+ GCC_except_table165
+ GCC_except_table29
+ _IORegistryEntryFromPath
+ _MGGetProductType
+ _MGGetSInt32Answer
+ _MGGetStringAnswer
+ _MobileGestalt_copy_hwModelDescriptionForPowerPerf_obj
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _OBJC_CLASS_$_PLGestaltUtilities
+ _OBJC_CLASS_$_PLMetricdLifecycleManager
+ _OBJC_CLASS_$_PLOSMetricsUtilities
+ _OBJC_IVAR_$_PLMetricdLifecycleManager._isActive
+ _OBJC_METACLASS_$_PLGestaltUtilities
+ _OBJC_METACLASS_$_PLMetricdLifecycleManager
+ _OBJC_METACLASS_$_PLOSMetricsUtilities
+ _OBJC_METACLASS_$_PPSFileUtilities
+ _PLLogMetricdLifecycleManager
+ _PLLogMetricdLifecycleManager.cold.1
+ _PLLogMetricdLifecycleManager.log
+ _PLLogMetricdLifecycleManager.onceToken
+ _PLLogOSMetrics
+ _PLLogOSMetrics.__logObj
+ _PLLogOSMetrics.cold.1
+ _PLLogOSMetrics.onceToken
+ __OBJC_$_CLASS_METHODS_PLGestaltUtilities
+ __OBJC_$_CLASS_METHODS_PLMetricdLifecycleManager
+ __OBJC_$_CLASS_METHODS_PLOSMetricsUtilities
+ __OBJC_$_CLASS_METHODS_PPSFileUtilities(APFS)
+ __OBJC_$_INSTANCE_METHODS_PLMetricdLifecycleManager
+ __OBJC_$_INSTANCE_VARIABLES_PLMetricdLifecycleManager
+ __OBJC_$_PROP_LIST_PLMetricdLifecycleManager
+ __OBJC_CLASS_RO_$_PLGestaltUtilities
+ __OBJC_CLASS_RO_$_PLMetricdLifecycleManager
+ __OBJC_CLASS_RO_$_PLOSMetricsUtilities
+ __OBJC_CLASS_RO_$_PPSFileUtilities
+ __OBJC_METACLASS_RO_$_PLGestaltUtilities
+ __OBJC_METACLASS_RO_$_PLMetricdLifecycleManager
+ __OBJC_METACLASS_RO_$_PLOSMetricsUtilities
+ __OBJC_METACLASS_RO_$_PPSFileUtilities
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZnwmSt19__type_descriptor_t
+ ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.843
+ ___20+[PLPlatform hasAOP]_block_invoke
+ ___21+[PLPlatform hasAOP2]_block_invoke
+ ___21-[PLCoreStorage init]_block_invoke.103
+ ___27-[PLArchiveManager migrate]_block_invoke.530
+ ___28+[PLGestaltUtilities hasANE]_block_invoke
+ ___28+[PLGestaltUtilities hasAOP]_block_invoke
+ ___28+[PLGestaltUtilities hasAOT]_block_invoke
+ ___28+[PLGestaltUtilities hasDCP]_block_invoke
+ ___28+[PLGestaltUtilities hasLPM]_block_invoke
+ ___28+[PLGestaltUtilities hasNFC]_block_invoke
+ ___28+[PLGestaltUtilities hasOrb]_block_invoke
+ ___29+[PLGestaltUtilities hasLPEM]_block_invoke
+ ___29+[PLGestaltUtilities hasMesa]_block_invoke
+ ___29+[PLGestaltUtilities is64Bit]_block_invoke
+ ___29+[PLUtilities deviceBootUUID]_block_invoke.118
+ ___29+[PLUtilities hasInternalKey]_block_invoke
+ ___30+[PLGestaltUtilities hasPearl]_block_invoke
+ ___30+[PLUtilities experimentGroup]_block_invoke
+ ___32+[PLGestaltUtilities hasBattery]_block_invoke
+ ___32+[PLGestaltUtilities hasPerseus]_block_invoke
+ ___32+[PLGestaltUtilities hasRearALS]_block_invoke
+ ___32+[PLGestaltUtilities isDevBoard]_block_invoke
+ ___33+[PLGestaltUtilities hasBaseband]_block_invoke
+ ___33+[PLGestaltUtilities hasGasGauge]_block_invoke
+ ___33+[PLGestaltUtilities hasPlatinum]_block_invoke
+ ___33+[PLUtilities isPerfPowerMetricd]_block_invoke
+ ___33+[PLUtilities isPowerexceptionsd]_block_invoke
+ ___33+[PPSFileUtilities containerPath]_block_invoke
+ ___33+[PPSFileUtilities containerPath]_block_invoke.cold.1
+ ___33-[PLABMClient regTriggerListener]_block_invoke.cold.1
+ ___33-[PLABMClient regTriggerListener]_block_invoke.cold.2
+ ___35+[PPSEntryKey hasAppIdentiferKeys:]_block_invoke
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.514
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.414
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.414.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.420
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.425
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.425.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.426
+ ___36+[PLGestaltUtilities getDeviceClass]_block_invoke
+ ___36+[PLGestaltUtilities getProductType]_block_invoke
+ ___36+[PLGestaltUtilities getWifiChipset]_block_invoke
+ ___36+[PLPlatform isUsingAnOlderWifiChip]_block_invoke
+ ___37+[PLAppDeletion populateIdentifiers:]_block_invoke_2
+ ___37+[PLGestaltUtilities getBuildVersion]_block_invoke
+ ___37+[PLGestaltUtilities isVirtualDevice]_block_invoke
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke.179
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.746
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.752
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.759
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.765
+ ___38+[PLGestaltUtilities getHardwareModel]_block_invoke
+ ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.490
+ ___39+[PLAppDeletion constructUpdateQueries]_block_invoke.109
+ ___39+[PLGestaltUtilities getNumberOfDCPEXT]_block_invoke
+ ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.162
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.657
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.659
+ ___40+[PLGestaltUtilities getBasebandChipset]_block_invoke
+ ___40+[PLGestaltUtilities getInverseDeviceID]_block_invoke
+ ___40+[PLGestaltUtilities getProductTypeCode]_block_invoke
+ ___40+[PLGestaltUtilities hasAlwaysListening]_block_invoke
+ ___40+[PLGestaltUtilities hasWirelessCharger]_block_invoke
+ ___41+[PLGestaltUtilities getHardwarePlatform]_block_invoke
+ ___41+[PLGestaltUtilities hasWristTemperature]_block_invoke
+ ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.129
+ ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.308
+ ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.317
+ ___42+[PLGestaltUtilities hasBatteryModuleAuth]_block_invoke
+ ___42+[PLGestaltUtilities hasInductiveCharging]_block_invoke
+ ___42+[PLMetricdLifecycleManager sharedManager]_block_invoke
+ ___43+[PLGestaltUtilities hasFixedChargingLimit]_block_invoke
+ ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.147
+ ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.150
+ ___43-[PLMetricdLifecycleManager signalInactive]_block_invoke
+ ___45+[PLGestaltUtilities hasDynamicChargingLimit]_block_invoke
+ ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.138
+ ___46+[PPSEntryKey allAppIdentiferKeysForEntryKey:]_block_invoke
+ ___46+[PPSEntryKey allAppIdentiferKeysForEntryKey:]_block_invoke_2
+ ___46+[PPSFileUtilities(APFS) supportsEnhancedAPFS]_block_invoke
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.491
+ ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.169
+ ___47+[PLGestaltUtilities getUserAssignedDeviceName]_block_invoke
+ ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.185
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.492
+ ___48+[PLGestaltUtilities getBasebandFirmwareVersion]_block_invoke
+ ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.727
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.697
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.697.cold.1
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.703
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.194
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.203
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.218
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.248
+ ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.257
+ ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.684
+ ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.889
+ ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.788
+ ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.137
+ ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.551
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.1
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.2
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.3
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87.cold.1
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.736
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.742
+ ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.120
+ ___Block_byref_object_copy_.722
+ ___Block_byref_object_dispose_.723
+ ___PLLogMetricdLifecycleManager_block_invoke
+ ___PLLogOSMetrics_block_invoke
+ ___block_descriptor_48_ea8_32s_e131_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e36_v32?0"NSString"8"PPSMetric"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32r40r_e131_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40lr32l8r40l8
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.118
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.13
+ ___block_literal_global.131
+ ___block_literal_global.136
+ ___block_literal_global.142
+ ___block_literal_global.146
+ ___block_literal_global.151
+ ___block_literal_global.156
+ ___block_literal_global.161
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.173
+ ___block_literal_global.178
+ ___block_literal_global.18
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.199
+ ___block_literal_global.210
+ ___block_literal_global.217
+ ___block_literal_global.23
+ ___block_literal_global.235
+ ___block_literal_global.271
+ ___block_literal_global.284
+ ___block_literal_global.289
+ ___block_literal_global.3
+ ___block_literal_global.307
+ ___block_literal_global.319
+ ___block_literal_global.325
+ ___block_literal_global.328
+ ___block_literal_global.340
+ ___block_literal_global.352
+ ___block_literal_global.361
+ ___block_literal_global.369
+ ___block_literal_global.381
+ ___block_literal_global.405
+ ___block_literal_global.411
+ ___block_literal_global.413
+ ___block_literal_global.418
+ ___block_literal_global.423
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.439
+ ___block_literal_global.44
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.453
+ ___block_literal_global.458
+ ___block_literal_global.467
+ ___block_literal_global.475
+ ___block_literal_global.48
+ ___block_literal_global.484
+ ___block_literal_global.488
+ ___block_literal_global.528
+ ___block_literal_global.530
+ ___block_literal_global.535
+ ___block_literal_global.540
+ ___block_literal_global.545
+ ___block_literal_global.550
+ ___block_literal_global.555
+ ___block_literal_global.560
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.575
+ ___block_literal_global.585
+ ___block_literal_global.587
+ ___block_literal_global.589
+ ___block_literal_global.591
+ ___block_literal_global.593
+ ___block_literal_global.595
+ ___block_literal_global.597
+ ___block_literal_global.599
+ ___block_literal_global.601
+ ___block_literal_global.609
+ ___block_literal_global.611
+ ___block_literal_global.613
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.619
+ ___block_literal_global.621
+ ___block_literal_global.63
+ ___block_literal_global.647
+ ___block_literal_global.68
+ ___block_literal_global.712
+ ___block_literal_global.714
+ ___block_literal_global.717
+ ___block_literal_global.724
+ ___block_literal_global.727
+ ___block_literal_global.730
+ ___block_literal_global.75
+ ___block_literal_global.78
+ ___block_literal_global.8
+ ___block_literal_global.823
+ ___block_literal_global.83
+ ___block_literal_global.846
+ ___block_literal_global.86
+ ___block_literal_global.866
+ ___block_literal_global.89
+ ___block_literal_global.927
+ ___block_literal_global.93
+ ___block_literal_global.99
+ __os_metric_double_create_impl
+ __os_metric_double_op_impl
+ __os_metric_uint64_create_impl
+ __os_metric_uint64_op_impl
+ _blockingFlushCachesWithReason:timeout:.classDebugEnabled.683
+ _blockingFlushCachesWithReason:timeout:.defaultOnce.682
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.692
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.702
+ _blockingFlushQueues:withTimeout:.defaultOnce.691
+ _blockingFlushQueues:withTimeout:.defaultOnce.701
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.193
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.202
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.217
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.247
+ _decodeIPPacket:encryptedPath:.classDebugEnabled.256
+ _decodeIPPacket:encryptedPath:.defaultOnce.192
+ _decodeIPPacket:encryptedPath:.defaultOnce.201
+ _decodeIPPacket:encryptedPath:.defaultOnce.216
+ _decodeIPPacket:encryptedPath:.defaultOnce.246
+ _decodeIPPacket:encryptedPath:.defaultOnce.255
+ _deviceBootUUID.classDebugEnabled.117
+ _deviceBootUUID.defaultOnce.116
+ _experimentGroup.expGroup
+ _experimentGroup.onceToken
+ _flushCachesWithReason:.defaultOnce.658
+ _getBasebandChipset.onceToken
+ _getBasebandChipset.ret
+ _getBasebandFirmwareVersion.onceToken
+ _getBasebandFirmwareVersion.ret
+ _getBuildVersion.onceToken
+ _getBuildVersion.ret
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.136
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.135
+ _getDeviceClass.onceToken
+ _getDeviceClass.ret
+ _getHardwareModel.onceToken
+ _getHardwareModel.ret
+ _getHardwarePlatform.onceToken
+ _getHardwarePlatform.ret
+ _getInverseDeviceID.onceToken
+ _getInverseDeviceID.ret
+ _getNetworkWakeInfo:.classDebugEnabled.128
+ _getNetworkWakeInfo:.defaultOnce.127
+ _getNormalizedIPV6Address:.classDebugEnabled.184
+ _getNormalizedIPV6Address:.defaultOnce.183
+ _getNumberOfDCPEXT.onceToken
+ _getProductType.onceToken
+ _getProductType.ret
+ _getProductTypeCode.onceToken
+ _getProductTypeCode.ret
+ _getUnattributedWakeInfo:.classDebugEnabled.137
+ _getUnattributedWakeInfo:.defaultOnce.136
+ _getUserAssignedDeviceName.onceToken
+ _getUserAssignedDeviceName.ret
+ _getWifiChipset.onceToken
+ _getWifiChipset.ret
+ _handleIPSecEvent:.classDebugEnabled.161
+ _handleIPSecEvent:.defaultOnce.160
+ _handlePowerWakeEvent:.classDebugEnabled.146
+ _handlePowerWakeEvent:.classDebugEnabled.149
+ _handlePowerWakeEvent:.defaultOnce.145
+ _handlePowerWakeEvent:.defaultOnce.148
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.550
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.549
+ _hasANE.ret
+ _hasAOP.hasAOP
+ _hasAOP.onceToken
+ _hasAOP.ret
+ _hasAOP2.hasAOP2
+ _hasAOP2.onceToken
+ _hasAOT.ret
+ _hasAlwaysListening.onceToken
+ _hasAlwaysListening.ret
+ _hasBaseband.onceToken
+ _hasBaseband.ret
+ _hasBattery.ret
+ _hasBatteryModuleAuth.onceToken
+ _hasBatteryModuleAuth.ret
+ _hasDCP.ret
+ _hasDynamicChargingLimit.onceToken
+ _hasDynamicChargingLimit.ret
+ _hasFixedChargingLimit.onceToken
+ _hasFixedChargingLimit.ret
+ _hasGasGauge.ret
+ _hasInductiveCharging.onceToken
+ _hasInductiveCharging.ret
+ _hasInternalKey._hasInternalAccount
+ _hasInternalKey.onceToken
+ _hasLPEM.ret
+ _hasLPM.onceToken
+ _hasLPM.ret
+ _hasMesa.onceToken
+ _hasMesa.ret
+ _hasNFC.ret
+ _hasOrb.onceToken
+ _hasOrb.ret
+ _hasPearl.onceToken
+ _hasPearl.ret
+ _hasPerseus.onceToken
+ _hasPerseus.ret
+ _hasPlatinum.onceToken
+ _hasPlatinum.ret
+ _hasRearALS.onceToken
+ _hasRearALS.ret
+ _hasWirelessCharger.onceToken
+ _hasWirelessCharger.ret
+ _hasWristTemperature.onceToken
+ _hasWristTemperature.ret
+ _is64Bit.ret
+ _isDevBoard.onceToken
+ _isDevBoard.ret
+ _isESPPacket:offset:.classDebugEnabled.307
+ _isESPPacket:offset:.defaultOnce.306
+ _isPerfPowerMetricd.isPerfPowerMetricd
+ _isPerfPowerMetricd.onceToken
+ _isPowerexceptionsd.isPowerexceptionsd
+ _isPowerexceptionsd.onceToken
+ _isUsingAnOlderWifiChip.onceToken
+ _isUsingAnOlderWifiChip.result
+ _isVirtualDevice.ret
+ _kIOMainPortDefault
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.751
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.758
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.764
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.750
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.757
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.763
+ _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.888
+ _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.887
+ _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.938
+ _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.939
+ _migrateArchive:.classDebugEnabled.513
+ _migrateArchive:.defaultOnce.512
+ _objc_msgSend$_debugStringForPurgeableLabel:
+ _objc_msgSend$_purgeableLabelWithUrgency:startDate:
+ _objc_msgSend$appIdentifier
+ _objc_msgSend$experimentGroup
+ _objc_msgSend$getDeviceClass
+ _objc_msgSend$getHardwareModel
+ _objc_msgSend$getProductType
+ _objc_msgSend$hasAOP
+ _objc_msgSend$hasAOP2
+ _objc_msgSend$hasAppIdentiferKeys:
+ _objc_msgSend$hasInternalKey:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$internalKey
+ _objc_msgSend$isActive
+ _objc_msgSend$isPerfPowerMetricd
+ _objc_msgSend$isPowerexceptionsd
+ _objc_msgSend$iterateMetrics
+ _objc_msgSend$kPLWiFiClassIsOneOf:
+ _objc_msgSend$markAsPurgeable:label:
+ _objc_msgSend$markAsPurgeable:urgency:startDate:
+ _objc_msgSend$setIsActive:
+ _objc_msgSend$stopMetricd
+ _objc_msgSend$supportsEnhancedAPFS
+ _os_metric_dimensions_add
+ _os_metric_dimensions_create
+ _os_metric_group_create
+ _registerDailyTasks.classDebugEnabled.419
+ _registerDailyTasks.defaultOnce.418
+ _sharedManager.metricdLifecycleManagerInstance
+ _supportsEnhancedAPFS.onceToken
+ _supportsEnhancedAPFS.result
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.735
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.741
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.734
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.740
- +[PLCacheDeleteUtility enforceRetentionForDirectory:withMaxDays:]
- +[PLCacheDeleteUtility enforceRetentionForDirectory:withMaxDays:].cold.1
- +[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]
- +[PLCacheDeleteUtility enforceRetentionForVersionDirectory:].cold.1
- +[PLCacheDeleteUtility periodicPurgeBlockWithInfo:withUrgency:]
- +[PLCacheDeleteUtility periodicPurgeBlockWithInfo:withUrgency:].cold.1
- +[PLCacheDeleteUtility periodicPurgeBlockWithInfo:withUrgency:].cold.2
- +[PLCacheDeleteUtility purgeBlockWithInfo:withUrgency:]
- +[PLCacheDeleteUtility purgeBlockWithInfo:withUrgency:].cold.1
- +[PLCacheDeleteUtility purgeBlockWithInfo:withUrgency:].cold.2
- +[PLCacheDeleteUtility purgeBlockWithInfo:withUrgency:].cold.3
- +[PLCacheDeleteUtility purgeBuildDirectory:]
- +[PLCacheDeleteUtility purgeBuildDirectory:].cold.1
- +[PLCacheDeleteUtility purgeVersionDirectory:]
- +[PLCacheDeleteUtility purgeVersionDirectory:].cold.1
- +[PLCacheDeleteUtility purgeableBlockWithInfo:withUrgency:]
- +[PLCacheDeleteUtility purgeableBlockWithInfo:withUrgency:].cold.1
- +[PLCacheDeleteUtility purgeableBlockWithInfo:withUrgency:].cold.2
- +[PLCacheDeleteUtility purgeableSizeForBuildDirectory:]
- +[PLCacheDeleteUtility purgeableSizeForBuildDirectory:].cold.1
- +[PLCacheDeleteUtility purgeableSizeForVersionDirectory:]
- +[PLCacheDeleteUtility purgeableSizeForVersionDirectory:].cold.1
- +[PLCacheDeleteUtility registerCacheDeleteFull]
- +[PLCacheDeleteUtility registerCacheDelete]
- +[PLCacheDeleteUtility traverseBuildDirectory:withBlock:]
- +[PLCacheDeleteUtility traverseBuildDirectory:withBlock:].cold.1
- +[PLCacheDeleteUtility traverseVersionDirectory:withBlock:]
- +[PLHelperdLifecycleManager sharedManager]
- +[PLHelperdLifecycleManager sharedManager].cold.1
- +[PLPlatform isVirtualDevice]
- +[PLPlatform isVirtualDevice].cold.1
- +[PLUtilities devBoardDevice]
- +[PLUtilities devBoardDevice].cold.1
- +[PLUtilities getDeviceSoC]
- +[PLUtilities getDeviceSoC].cold.1
- +[PLUtilities hardwareModelSMC:]
- +[PLUtilities hardwareModel]
- +[PLUtilities hardwareModel].cold.1
- +[PLUtilities markFileAsPurgeable:withUrgency:]
- +[PLUtilities markFileAsPurgeable:withUrgency:].cold.1
- +[PLUtilities markFilesAsPurgeable:withUrgency:]
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:]
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.1
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.2
- +[PLUtilities productType]
- +[PLUtilities productType].cold.1
- +[PowerlogCore isAudioAccessory]
- +[PowerlogCore isAudioAccessory].cold.1
- +[PowerlogCore shouldSetupCore]
- -[PLABMClient triggerPeriodicMetrics:]
- -[PLABMClient triggerPeriodicMetrics:].cold.1
- -[PLABMClient triggerPeriodicMetrics:].cold.2
- -[PLABMClient triggerPeriodicMetrics:].cold.3
- -[PLABMClient triggerPeriodicMetrics:].cold.4
- -[PLABMClient triggerPeriodicMetrics:].cold.5
- -[PLABMClient triggerPeriodicMetrics:].cold.6
- -[PLABMClient triggerPeriodicMetrics:].cold.7
- -[PLABMClient triggerPeriodicMetrics:].cold.8
- -[PLArchiveManager deprecateTablesBGSQL].cold.1
- -[PLArchiveManager trimBackgroundProcessingLog].cold.1
- -[PLHelperdLifecycleManager .cxx_destruct]
- -[PLHelperdLifecycleManager activeServices]
- -[PLHelperdLifecycleManager init]
- -[PLHelperdLifecycleManager isServiceActive:]
- -[PLHelperdLifecycleManager serviceNameFor:]
- -[PLHelperdLifecycleManager setActiveServices:]
- -[PLHelperdLifecycleManager signalServiceActive:]
- -[PLHelperdLifecycleManager signalServiceActive:].cold.1
- -[PLHelperdLifecycleManager signalServiceInactive:]
- -[PLHelperdLifecycleManager signalServiceInactive:].cold.1
- -[PLHelperdLifecycleManager signalServiceInactive:].cold.2
- -[PLHelperdLifecycleManager stopPowerlogHelperd]
- GCC_except_table36
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table47
- GCC_except_table65
- GCC_except_table69
- _CacheDeleteRegisterInfoCallbacks
- _NSURLContentModificationDateKey
- _NSURLFileSizeKey
- _OBJC_CLASS_$_PLCacheDeleteUtility
- _OBJC_CLASS_$_PLHelperdLifecycleManager
- _OBJC_IVAR_$_PLHelperdLifecycleManager._activeServices
- _OBJC_METACLASS_$_PLCacheDeleteUtility
- _OBJC_METACLASS_$_PLHelperdLifecycleManager
- _PLLogPowerlogHelperdLifecycleManager
- _PLLogPowerlogHelperdLifecycleManager.cold.1
- _PLLogPowerlogHelperdLifecycleManager.log
- _PLLogPowerlogHelperdLifecycleManager.onceToken
- _PLServiceTypeBatteryGaugeName
- _PLServiceTypeMetricMonitorName
- _PLServiceTypeXPCName
- __OBJC_$_CLASS_METHODS_PLCacheDeleteUtility
- __OBJC_$_CLASS_METHODS_PLHelperdLifecycleManager
- __OBJC_$_INSTANCE_METHODS_PLHelperdLifecycleManager
- __OBJC_$_INSTANCE_VARIABLES_PLHelperdLifecycleManager
- __OBJC_$_PROP_LIST_PLHelperdLifecycleManager
- __OBJC_CLASS_RO_$_PLCacheDeleteUtility
- __OBJC_CLASS_RO_$_PLHelperdLifecycleManager
- __OBJC_METACLASS_RO_$_PLCacheDeleteUtility
- __OBJC_METACLASS_RO_$_PLHelperdLifecycleManager
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZZ29-[PLABMClient startListening]E11defaultOnce
- __ZZ29-[PLABMClient startListening]E17classDebugEnabled
- __ZZ33-[PLABMClient removeDeviceConfig]E11defaultOnce
- __ZZ33-[PLABMClient removeDeviceConfig]E11defaultOnce_0
- __ZZ33-[PLABMClient removeDeviceConfig]E17classDebugEnabled
- __ZZ33-[PLABMClient removeDeviceConfig]E17classDebugEnabled_0
- __ZZ35-[PLABMClient getBasebandBootState]E11defaultOnce_0
- __ZZ35-[PLABMClient getBasebandBootState]E11defaultOnce_1
- __ZZ35-[PLABMClient getBasebandBootState]E17classDebugEnabled_0
- __ZZ35-[PLABMClient getBasebandBootState]E17classDebugEnabled_1
- __ZZ38-[PLABMClient triggerPeriodicMetrics:]E11defaultOnce
- __ZZ38-[PLABMClient triggerPeriodicMetrics:]E11defaultOnce_0
- __ZZ38-[PLABMClient triggerPeriodicMetrics:]E17classDebugEnabled
- __ZZ38-[PLABMClient triggerPeriodicMetrics:]E17classDebugEnabled_0
- __ZZ39-[PLABMClient sendMetricToLoggerUsing:]E11defaultOnce
- __ZZ39-[PLABMClient sendMetricToLoggerUsing:]E17classDebugEnabled
- __ZZ40-[PLABMClient sendTriggerToLoggerUsing:]E11defaultOnce
- __ZZ40-[PLABMClient sendTriggerToLoggerUsing:]E17classDebugEnabled
- __ZZ41-[PLABMClient sendWakeInfoToLoggerUsing:]E11defaultOnce
- __ZZ41-[PLABMClient sendWakeInfoToLoggerUsing:]E17classDebugEnabled
- __ZZ51-[PLABMClient sendBootStateChangInfoToLoggerUsing:]E11defaultOnce
- __ZZ51-[PLABMClient sendBootStateChangInfoToLoggerUsing:]E17classDebugEnabled
- __ZZ54-[PLABMClient addDeviceConfigWith:andConfigExtension:]E11defaultOnce
- __ZZ54-[PLABMClient addDeviceConfigWith:andConfigExtension:]E17classDebugEnabled
- __ZZZ32-[PLABMClient regBBWakeListener]EUb2_E11defaultOnce
- __ZZZ32-[PLABMClient regBBWakeListener]EUb2_E17classDebugEnabled
- __ZZZ32-[PLABMClient regMetricListener]EUb1_E11defaultOnce
- __ZZZ32-[PLABMClient regMetricListener]EUb1_E17classDebugEnabled
- __ZZZ33-[PLABMClient regTriggerListener]EUb0_E11defaultOnce
- __ZZZ33-[PLABMClient regTriggerListener]EUb0_E17classDebugEnabled
- __ZZZ35-[PLABMClient regBootStateListener]EUb_E11defaultOnce
- __ZZZ35-[PLABMClient regBootStateListener]EUb_E17classDebugEnabled
- __Znwm
- ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.839
- ___21-[PLCoreStorage init]_block_invoke.100
- ___26+[PLUtilities productType]_block_invoke
- ___27+[PLUtilities getDeviceSoC]_block_invoke
- ___27-[PLArchiveManager migrate]_block_invoke.499
- ___28+[PLUtilities hardwareModel]_block_invoke
- ___28+[PLUtilities hardwareModel]_block_invoke.cold.1
- ___28+[PLUtilities hardwareModel]_block_invoke.cold.2
- ___29+[PLPlatform isVirtualDevice]_block_invoke
- ___29+[PLUtilities devBoardDevice]_block_invoke
- ___29+[PLUtilities devBoardDevice]_block_invoke.cold.1
- ___29+[PLUtilities deviceBootUUID]_block_invoke.117
- ___29-[PLABMClient startListening]_block_invoke
- ___32+[PowerlogCore isAudioAccessory]_block_invoke
- ___32-[PLABMClient regBBWakeListener]_block_invoke.83
- ___32-[PLABMClient regMetricListener]_block_invoke.79
- ___33-[PLABMClient regTriggerListener]_block_invoke_2
- ___33-[PLABMClient removeDeviceConfig]_block_invoke
- ___33-[PLABMClient removeDeviceConfig]_block_invoke.93
- ___35-[PLABMClient getBasebandBootState]_block_invoke.156
- ___35-[PLABMClient getBasebandBootState]_block_invoke.160
- ___35-[PLABMClient regBootStateListener]_block_invoke.71
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.483
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.410
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.410.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.416
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.421
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.421.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.422
- ___37+[PLUtilities exitWithReason:action:]_block_invoke.178
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.742
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.748
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.755
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.761
- ___38-[PLABMClient triggerPeriodicMetrics:]_block_invoke
- ___38-[PLABMClient triggerPeriodicMetrics:]_block_invoke.100
- ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.459
- ___39+[PLAppDeletion constructUpdateQueries]_block_invoke.101
- ___39+[PLNetworkUtilities handleIPSecEvent:]_block_invoke.150
- ___39-[PLABMClient sendMetricToLoggerUsing:]_block_invoke
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.653
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.655
- ___40-[PLABMClient sendTriggerToLoggerUsing:]_block_invoke
- ___41+[PLNetworkUtilities getNetworkWakeInfo:]_block_invoke.123
- ___41+[PLNetworkUtilities isESPPacket:offset:]_block_invoke.296
- ___41-[PLABMClient sendWakeInfoToLoggerUsing:]_block_invoke
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.312
- ___42+[PLHelperdLifecycleManager sharedManager]_block_invoke
- ___43+[PLCacheDeleteUtility registerCacheDelete]_block_invoke
- ___43+[PLCacheDeleteUtility registerCacheDelete]_block_invoke_2
- ___43+[PLCacheDeleteUtility registerCacheDelete]_block_invoke_3
- ___43+[PLCacheDeleteUtility registerCacheDelete]_block_invoke_4
- ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.141
- ___43+[PLNetworkUtilities handlePowerWakeEvent:]_block_invoke.144
- ___44+[PLCacheDeleteUtility purgeBuildDirectory:]_block_invoke
- ___44+[PLCacheDeleteUtility purgeBuildDirectory:]_block_invoke_2
- ___44+[PLCacheDeleteUtility purgeBuildDirectory:]_block_invoke_2.cold.1
- ___46+[PLCacheDeleteUtility purgeVersionDirectory:]_block_invoke
- ___46+[PLNetworkUtilities getUnattributedWakeInfo:]_block_invoke.132
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.460
- ___46-[PPSSQLStorage handleSchemaMismatchForTable:]_block_invoke.167
- ___47+[PLCacheDeleteUtility registerCacheDeleteFull]_block_invoke
- ___47+[PLCacheDeleteUtility registerCacheDeleteFull]_block_invoke_2
- ___47+[PLCacheDeleteUtility registerCacheDeleteFull]_block_invoke_3
- ___47+[PLCacheDeleteUtility registerCacheDeleteFull]_block_invoke_4
- ___47+[PLNetworkUtilities getNormalizedIPV6Address:]_block_invoke.179
- ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.461
- ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.723
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.689
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.693.cold.1
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.699
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.188
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.197
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.206
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.230
- ___51+[PLNetworkUtilities decodeIPPacket:encryptedPath:]_block_invoke.251
- ___51-[PLABMClient sendBootStateChangInfoToLoggerUsing:]_block_invoke
- ___51-[PLHelperdLifecycleManager signalServiceInactive:]_block_invoke
- ___54-[PLABMClient addDeviceConfigWith:andConfigExtension:]_block_invoke
- ___55+[PLCacheDeleteUtility purgeableSizeForBuildDirectory:]_block_invoke
- ___55+[PLCacheDeleteUtility purgeableSizeForBuildDirectory:]_block_invoke_2
- ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.680
- ___57+[PLCacheDeleteUtility purgeableSizeForVersionDirectory:]_block_invoke
- ___57+[PLCacheDeleteUtility traverseBuildDirectory:withBlock:]_block_invoke
- ___57+[PLCacheDeleteUtility traverseBuildDirectory:withBlock:]_block_invoke_2
- ___59+[PLCacheDeleteUtility traverseVersionDirectory:withBlock:]_block_invoke
- ___60+[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]_block_invoke
- ___60+[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]_block_invoke_2
- ___60+[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]_block_invoke_3
- ___60+[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]_block_invoke_3.cold.1
- ___60+[PLCacheDeleteUtility enforceRetentionForVersionDirectory:]_block_invoke_3.cold.2
- ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.885
- ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.784
- ___65+[PLCacheDeleteUtility enforceRetentionForDirectory:withMaxDays:]_block_invoke
- ___65+[PLCacheDeleteUtility enforceRetentionForDirectory:withMaxDays:]_block_invoke.cold.1
- ___65+[PLCacheDeleteUtility enforceRetentionForDirectory:withMaxDays:]_block_invoke.cold.2
- ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.136
- ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.547
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.1
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.2
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.3
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86.cold.1
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.732
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.738
- ___93-[PLEnhancedTaskingAgent logAggregatedDataFromSignpostWithPayload:withStartDate:withEndDate:]_block_invoke.119
- ___Block_byref_object_copy_.718
- ___Block_byref_object_dispose_.719
- ___PLLogPowerlogHelperdLifecycleManager_block_invoke
- ___block_descriptor_32_e45_^{__CFDictionary=}20?0i8^{__CFDictionary=}12l
- ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8lr32l8
- ___block_descriptor_48_e8_32r_e21_B24?0"NSString"8Q16lr32l8
- ___block_descriptor_48_e8_32s40bs_e22_v32?0"NSURL"8Q16^B24ls40l8s32l8
- ___block_descriptor_48_ea8_32s_e209_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40ls32l8
- ___block_descriptor_56_e8_32s40r_e18_v16?0"NSString"8ls32l8r40l8
- ___block_descriptor_56_e8_32s40r_e21_B24?0"NSString"8Q16ls32l8r40l8
- ___block_descriptor_56_ea8_32r40r_e209_v48?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40lr32l8r40l8
- ___block_descriptor_80_e8_32s40r48r56r64r_e22_v32?0"NSURL"8Q16^B24lr40l8r48l8r56l8s32l8r64l8
- ___block_literal_global.102
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.122
- ___block_literal_global.195
- ___block_literal_global.207
- ___block_literal_global.216
- ___block_literal_global.234
- ___block_literal_global.252
- ___block_literal_global.269
- ___block_literal_global.281
- ___block_literal_global.288
- ___block_literal_global.306
- ___block_literal_global.314
- ___block_literal_global.323
- ___block_literal_global.324
- ___block_literal_global.335
- ___block_literal_global.347
- ___block_literal_global.356
- ___block_literal_global.368
- ___block_literal_global.380
- ___block_literal_global.404
- ___block_literal_global.409
- ___block_literal_global.410
- ___block_literal_global.412
- ___block_literal_global.417
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.437
- ___block_literal_global.447
- ___block_literal_global.456
- ___block_literal_global.457
- ___block_literal_global.464
- ___block_literal_global.47
- ___block_literal_global.473
- ___block_literal_global.51
- ___block_literal_global.513
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.551
- ___block_literal_global.553
- ___block_literal_global.558
- ___block_literal_global.563
- ___block_literal_global.568
- ___block_literal_global.57
- ___block_literal_global.573
- ___block_literal_global.578
- ___block_literal_global.582
- ___block_literal_global.584
- ___block_literal_global.586
- ___block_literal_global.588
- ___block_literal_global.590
- ___block_literal_global.592
- ___block_literal_global.594
- ___block_literal_global.602
- ___block_literal_global.604
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.61
- ___block_literal_global.610
- ___block_literal_global.612
- ___block_literal_global.614
- ___block_literal_global.628
- ___block_literal_global.693
- ___block_literal_global.695
- ___block_literal_global.706
- ___block_literal_global.708
- ___block_literal_global.713
- ___block_literal_global.718
- ___block_literal_global.725
- ___block_literal_global.728
- ___block_literal_global.731
- ___block_literal_global.734
- ___block_literal_global.81
- ___block_literal_global.819
- ___block_literal_global.842
- ___block_literal_global.85
- ___block_literal_global.862
- ___block_literal_global.932
- _blockingFlushCachesWithReason:timeout:.classDebugEnabled.679
- _blockingFlushCachesWithReason:timeout:.defaultOnce.678
- _blockingFlushQueues:withTimeout:.classDebugEnabled.688
- _blockingFlushQueues:withTimeout:.classDebugEnabled.698
- _blockingFlushQueues:withTimeout:.defaultOnce.687
- _blockingFlushQueues:withTimeout:.defaultOnce.697
- _decodeIPPacket:encryptedPath:.classDebugEnabled.187
- _decodeIPPacket:encryptedPath:.classDebugEnabled.196
- _decodeIPPacket:encryptedPath:.classDebugEnabled.205
- _decodeIPPacket:encryptedPath:.classDebugEnabled.229
- _decodeIPPacket:encryptedPath:.classDebugEnabled.250
- _decodeIPPacket:encryptedPath:.defaultOnce.186
- _decodeIPPacket:encryptedPath:.defaultOnce.195
- _decodeIPPacket:encryptedPath:.defaultOnce.204
- _decodeIPPacket:encryptedPath:.defaultOnce.228
- _decodeIPPacket:encryptedPath:.defaultOnce.249
- _devBoardDevice._devBoard
- _devBoardDevice.onceToken
- _deviceBootUUID.classDebugEnabled.116
- _deviceBootUUID.defaultOnce.115
- _enforceRetentionForVersionDirectory:.defaultOnce
- _enforceRetentionForVersionDirectory:.objectForKey
- _flushCachesWithReason:.defaultOnce.654
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.135
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.134
- _getDeviceSoC._soc
- _getDeviceSoC.onceToken
- _getNetworkWakeInfo:.classDebugEnabled.122
- _getNetworkWakeInfo:.defaultOnce.121
- _getNormalizedIPV6Address:.classDebugEnabled.178
- _getNormalizedIPV6Address:.defaultOnce.177
- _getUnattributedWakeInfo:.classDebugEnabled.131
- _getUnattributedWakeInfo:.defaultOnce.130
- _handleIPSecEvent:.classDebugEnabled.149
- _handleIPSecEvent:.defaultOnce.148
- _handlePowerWakeEvent:.classDebugEnabled.140
- _handlePowerWakeEvent:.classDebugEnabled.143
- _handlePowerWakeEvent:.defaultOnce.139
- _handlePowerWakeEvent:.defaultOnce.142
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.546
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.545
- _hardwareModel._hardwareModel
- _hardwareModel.onceToken
- _isAudioAccessory.__isAudioAccessory
- _isAudioAccessory.onceToken
- _isESPPacket:offset:.classDebugEnabled.295
- _isESPPacket:offset:.defaultOnce.294
- _isVirtualDevice.isVirtualDevice
- _kPLHelperdLifecycleManagerServiceIsActiveNotification
- _kPLHelperdLifecycleManagerServiceIsInactiveNotification
- _kPLHelperdLifecycleManagerServiceKey
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.747
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.754
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.760
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.746
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.753
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.759
- _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.884
- _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.883
- _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.934
- _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.935
- _migrateArchive:.classDebugEnabled.482
- _migrateArchive:.defaultOnce.481
- _objc_msgSend$absoluteString
- _objc_msgSend$activeServices
- _objc_msgSend$compareFilesByKey:file1:file2:sortAscending:
- _objc_msgSend$directorySize:
- _objc_msgSend$enforceRetentionForDirectory:withMaxDays:
- _objc_msgSend$enforceRetentionForVersionDirectory:
- _objc_msgSend$fileCreationDate
- _objc_msgSend$hardwareModel
- _objc_msgSend$hardwareModelSMC:
- _objc_msgSend$markFileAsPurgeable:withUrgency:
- _objc_msgSend$periodicPurgeBlockWithInfo:withUrgency:
- _objc_msgSend$productType
- _objc_msgSend$purgeBlockWithInfo:withUrgency:
- _objc_msgSend$purgeBuildDirectory:
- _objc_msgSend$purgeVersionDirectory:
- _objc_msgSend$purgeableBlockWithInfo:withUrgency:
- _objc_msgSend$purgeableSizeForBuildDirectory:
- _objc_msgSend$purgeableSizeForVersionDirectory:
- _objc_msgSend$registerCacheDelete
- _objc_msgSend$registerCacheDeleteFull
- _objc_msgSend$serviceNameFor:
- _objc_msgSend$setActiveServices:
- _objc_msgSend$shouldSetupCore
- _objc_msgSend$stopPowerlogHelperd
- _objc_msgSend$traverseBuildDirectory:withBlock:
- _productType._productType
- _productType.onceToken
- _purgeBuildDirectory:.defaultOnce
- _purgeBuildDirectory:.objectForKey
- _purgeableSizeForBuildDirectory:.defaultOnce
- _purgeableSizeForBuildDirectory:.objectForKey
- _registerDailyTasks.classDebugEnabled.415
- _registerDailyTasks.defaultOnce.414
- _sharedManager.helperdLifecycleManagerInstance
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.731
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.737
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.730
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.736
CStrings:
+ "%@_%@_%@_%@"
+ "1hz_bic_accum_count"
+ "1hz_flipbook_frame_count"
+ "1hz_frame_miss_count"
+ "1oMPwMsqxTa9BJxUs8v06w"
+ "64-bit"
+ "8S7ydMJ4DlCUF38/hI/fJA"
+ "@20@0:8C16"
+ "@40@0:8@16@24C32I36"
+ "@44@0:8@16@24@32C40"
+ "@48@0:8@16@24@32C40C44"
+ "@56@0:8@16@24@32C40C44I48C52"
+ "@64@0:8{apfs_label_purgeable_request=QQQQQQ}16"
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
+ "ABM Client: triggerPeriodicMetrics with trigger id %d profile:%d"
+ "ADGOnly"
+ "ANCTotalDuration"
+ "AOP2Performance"
+ "APFS"
+ "AccessoryUsageSummary"
+ "AccumulatedKeyValues"
+ "AccumulatedLookUpTable"
+ "ActiveClients"
+ "AdaptiveTotalDuration"
+ "Address"
+ "AllocatedRuntime"
+ "AppIcons"
+ "Arkit"
+ "Attempted to convert negative seconds (%f) to mach time. Returning 0."
+ "Attempted to stop perfpowermetricd but metric monitor is still active"
+ "AudioDropCount"
+ "AudioDropOverWaitCount"
+ "AudioDropPoorRSSICount"
+ "AugmentedBatteryHealthWeekly"
+ "B40@0:8@16Q24@32"
+ "B72@0:8@16{apfs_label_purgeable_request=QQQQQQ}24"
+ "BasebandChipset"
+ "BasebandFirmwareVersion"
+ "BasebandMetrics_TelephonyActivity_1_2"
+ "BasebandMetrics_TelephonyRegistration_1_2"
+ "BilledEnergy"
+ "BluetoothWakeTrace"
+ "BothBudTotalDuration"
+ "CM-VIDEOPLAYBACK"
+ "CPMPowerTargets"
+ "CPMS"
+ "CPUCycleConsumed"
+ "CPUPressure"
+ "CPUTimeConsumed"
+ "CafeSwellDaily"
+ "Capability18"
+ "Capability19"
+ "Capability20"
+ "Capability21"
+ "Capability22"
+ "CaptureTimestamp"
+ "CoalitionName"
+ "ConnectionError1Count"
+ "ConnectionError2Count"
+ "ConnectionError3Count"
+ "ConnectionError4Count"
+ "ConnectionErrorGeneralCount"
+ "CoreLocation"
+ "CustomCheckpoint"
+ "CustomTintColor"
+ "CycleCountDiff"
+ "D6/BMDrlb8V3WSiqL8gL+w"
+ "DataConsumed"
+ "DebugEnabled"
+ "Default"
+ "DeviceSupports80ChargeLimit"
+ "DeviceSupportsAOP"
+ "DeviceSupportsAOP2"
+ "DeviceSupportsCorrectedTemperature"
+ "DeviceSupportsDynamicEndOfCharge"
+ "DisconnectionError1Count"
+ "DisconnectionError2Count"
+ "DisconnectionError3Count"
+ "DisconnectionError4Count"
+ "DisconnectionGeneralCount"
+ "DiskIOConsumed"
+ "DisplayPower"
+ "DisplayPredictiveSysCap_mW"
+ "DynFilteredCurrentRc3_mA"
+ "DynFilteredCurrentRc4_mA"
+ "ErrorString"
+ "ExpectedValue"
+ "ExperimentGroup"
+ "ExtendedBatteryMode"
+ "F0St"
+ "F0TE"
+ "FEna"
+ "Failed to mark file '%@' as purgeable with label: '%@' (error %d = '%s')"
+ "Failed to open file handle for '%@' to apply purgeable status: '%@' (error %d = '%s')"
+ "FeatureEngagementState"
+ "FilterType"
+ "ForceMitigationSuggestion"
+ "GameTotalDuration"
+ "GdXjx1ixZYvN9Gg8iSf68A"
+ "GeofenceTrigger"
+ "HCIRawData"
+ "HFPTotalDuration"
+ "HV7WDiidgMf7lwAu++Lk5w"
+ "HasBaseband"
+ "HasInternalKey"
+ "HealthKitQuery"
+ "IBLMFeatureEngagement"
+ "IBLMFeatureState"
+ "INSERT INTO %@ (TaskEndTime, Reason) VALUES ('%@', '%@')"
+ "IODeviceTree:/filesystems"
+ "IOPortPredictiveSysCap_mW"
+ "IdlePhysFootprint"
+ "IndeedCPUIntensive"
+ "IndeedIntensive"
+ "IndeedMemoryIntensive"
+ "InstantAmperage_mA"
+ "InterfaceName"
+ "ItemCount"
+ "ItemsCompleted"
+ "LiveTranslatedMessage"
+ "LongLook"
+ "MXClientsAvailable"
+ "Mach time calculation overflowed for %f seconds. Clamping to UINT64_MAX."
+ "Mach time calculation resulted in negative value (%f) for %f seconds. Returning 0."
+ "Mach time ratio is zero, cannot convert seconds (%f) to mach time. Returning 0."
+ "Maps"
+ "Marked file '%@' as purgeable with label: '%@'"
+ "MetricKitD"
+ "Mitigation"
+ "MitigationDecisionReason"
+ "MitigationDecisionType"
+ "MitigationSuggestion"
+ "MitigationSuggestionReason"
+ "ModeChange"
+ "NSProcessInfoInteractionTracking"
+ "OCV_mV"
+ "OPTICAL_POWER_HE1_25"
+ "OPTICAL_POWER_HE1_25_Transitions"
+ "OPTICAL_POWER_HE2_25"
+ "OPTICAL_POWER_HE2_25_Transitions"
+ "OPTICAL_POWER_HE4_25"
+ "OPTICAL_POWER_HE4_25_Transitions"
+ "OPTICAL_POWER_SC1_HE"
+ "OPTICAL_POWER_SC1_HE_Transitions"
+ "OPTICAL_POWER_SC2_HE"
+ "OPTICAL_POWER_SC2_HE_Transitions"
+ "OPTICAL_POWER_SC4_HE"
+ "OPTICAL_POWER_SC4_HE_Transitions"
+ "OSIPrediction"
+ "OutputPp_mW"
+ "OutputPs_mW"
+ "OutputPu_mW"
+ "Overridden"
+ "PLApplicationAgent_EventForward_RBSApplication"
+ "PLBluetoothAgent_EventBackward_HCITrace"
+ "PLGestaltUtilities"
+ "PLHealthKitAgent_EventPoint_HealthKitQuery"
+ "PLMetricdLifecycleManager"
+ "PLOSMetricsUtilities"
+ "PLPushAgent_Aggregate_SentKeepAlive"
+ "PLSleepWakeAgent_EventPoint_CoSocPower"
+ "PLVideoAgent_EventBackward_CMVideoPlayback"
+ "PMUMetrics"
+ "PPSFileUtilities"
+ "PUUID"
+ "PairingCount"
+ "PairingError1Count"
+ "PairingError2Count"
+ "PairingError3Count"
+ "PairingError4Count"
+ "PairingErrorGeneralCount"
+ "PlaybackType"
+ "PluginPrediction"
+ "PmaxCurrent_mA"
+ "PmaxState"
+ "PmaxVoltage_mV"
+ "PowerExceptionsDetection"
+ "PpmzzBVLpZVubmP0tCIymg"
+ "PredictionDate"
+ "PredictionDuration"
+ "PredictionWindowID"
+ "Progress"
+ "PsCutoffVoltage_mV"
+ "QoS"
+ "Rail"
+ "RailEnergy"
+ "Rcp0"
+ "Rcu0"
+ "ReallocatedDuration"
+ "RearALSCapability"
+ "RebootEvents"
+ "RequestsImmediateRuntime"
+ "RuleID"
+ "ShadowPolicyEvaluation"
+ "SingleBudTotalDuration"
+ "SpatialTotalDuration"
+ "SpringfieldUsage"
+ "StartedInIdle"
+ "StartedOnBattery"
+ "StatusKitAgent"
+ "Stopping perfpowermetricd"
+ "StrobePredictiveSysCap_mW"
+ "TB,V_isActive"
+ "TVMx"
+ "TaskEndTime"
+ "TaskID"
+ "TaskInstanceData"
+ "TaskInstanceID"
+ "TaskInstanceStore"
+ "TaskMetadata"
+ "TaskRuntimeAllocation"
+ "TaskThroughput"
+ "The BGSQL insertion query failed"
+ "The BGSQL tasking open database failed"
+ "The epoch time for BGSQL copy log is %f"
+ "The payload for BGSQL Tasking log is %@"
+ "The table name for BGSQL Tasking log is %@"
+ "ThermalLevelElevated"
+ "TimeOfCaptureEvent"
+ "TimeSinceBoot"
+ "TotalItemCount"
+ "TransparencyTotalDuration"
+ "Trial"
+ "TrialDeploymentID"
+ "TrialEndDate"
+ "TrialExperimentID"
+ "TrialStartDate"
+ "TrialTreatmentID"
+ "TriggerEvents"
+ "TriggeredDetection"
+ "Unable to add metrics dimensions"
+ "UserAssignedDeviceName"
+ "UtilizedRuntime"
+ "VCafe"
+ "VDroop_mV"
+ "Variant"
+ "Voltage_mV"
+ "WiFiNonInfra"
+ "WifiChipset"
+ "Will attempt to stop perfpowermetricd after %d seconds"
+ "XPCMetrics_GroupActivities_1_2"
+ "XPCMetrics_PowerExceptionsDetection_1_2"
+ "XPCMetrics_TriggerEvents_1_2"
+ "_debugStringForPurgeableLabel:"
+ "_isActive"
+ "_purgeableLabelWithUrgency:startDate:"
+ "addCounter:withValue:"
+ "addDimensions:withKey:withValue:"
+ "allAppIdentiferKeysForEntryKey:"
+ "appIdentifier"
+ "augmentedNCC"
+ "augmentedQmax"
+ "augmentedRdc"
+ "com.apple.Foundation"
+ "com.apple.powerlog.perfpowermetricd"
+ "computeEmbeddingsForQuery"
+ "createCounter:withLabel:"
+ "createCounter:withLabel:withDimensions:withFlags:"
+ "createDimensions:"
+ "createGauge:withLabel:"
+ "createGauge:withLabel:withDimensions:withLevel:withFlags:"
+ "createHistogram:withLabel:withBins:withInterval:"
+ "createHistogram:withLabel:withDimensions:withLevel:withBins:withInterval:withFlags:"
+ "createMetricGroup:withDimensions:"
+ "criticalBatteryLevel"
+ "dateFromnSecEpoch:"
+ "deltaNCC"
+ "deltaQmax"
+ "deltaRdc"
+ "e-apfs"
+ "eQd5mlz0BN0amTp/2ccMoA"
+ "error checking for internal key, %@"
+ "errorFrameCount"
+ "experimentGroup"
+ "f+PE44W6AO2UENJk3p2s5A"
+ "flags=%llu, startTime=%llu"
+ "getBasebandChipset"
+ "getBasebandFirmwareVersion"
+ "getBuildVersion"
+ "getDeviceClass"
+ "getHardwareModel"
+ "getHardwarePlatform"
+ "getInverseDeviceID"
+ "getNumberOfDCPEXT"
+ "getProductType"
+ "getProductTypeCode"
+ "getUserAssignedDeviceName"
+ "getWifiChipset"
+ "hands"
+ "hasAOP"
+ "hasAOP2"
+ "hasAlwaysListening"
+ "hasAppIdentiferKeys:"
+ "hasBatteryModuleAuth"
+ "hasDynamicChargingLimit"
+ "hasFixedChargingLimit"
+ "hasInductiveCharging"
+ "hasInternalKey"
+ "hasInternalKey:"
+ "hasLPM"
+ "hasMesa"
+ "hasMessageOnDevice"
+ "hasPearl"
+ "hasPerseus"
+ "hasPlatinum"
+ "hasRearALS"
+ "hasWirelessCharger"
+ "hasWristTemperature"
+ "idleConnectionWake"
+ "initWithUUIDBytes:"
+ "internalKey"
+ "invalid internal key: %{private}@ resulting in %lu components"
+ "isANEIntensive"
+ "isBackgroundQuery"
+ "isCPUIntensive"
+ "isComputeModule"
+ "isDiskIntensive"
+ "isGPUIntensive"
+ "isMemoryIntensive"
+ "isPerfPowerMetricd"
+ "isPowerexceptionsd"
+ "isSPR"
+ "isUsingAnOlderWifiChip"
+ "iterateMetrics"
+ "longevityPredict"
+ "lpwProcessedWake"
+ "mCafe"
+ "machTimeFromSeconds:"
+ "markAsPurgeable:label:"
+ "markAsPurgeable:urgency:startDate:"
+ "megaBytesDownloaded"
+ "metric monitor became active"
+ "metric monitor became inactive"
+ "mlPm"
+ "mlpR"
+ "option"
+ "osmetrics"
+ "pUUIDForPid:"
+ "peFK_ID"
+ "peProcess"
+ "peReason"
+ "perfpowermetricd"
+ "perfpowermetricdLifecycleManager"
+ "powerexceptionsd"
+ "queryID"
+ "queryType"
+ "rxCellularBytes"
+ "rxWifiBytes"
+ "rxWiredBytes"
+ "s7nuHoZIYNoOHCqT9iyZkQ"
+ "setGauge:withValue:"
+ "setHistogram:withValue:"
+ "setIsActive:"
+ "signalActive"
+ "signalInactive"
+ "stopMetricd"
+ "subtractCounter:withValue:"
+ "supportsEnhancedAPFS"
+ "totalDuration"
+ "triggerPeriodicMetrics:andprofileId:"
+ "triggered"
+ "txCellularBytes"
+ "txWifiBytes"
+ "txWiredBytes"
+ "v32@0:8@16Q24"
+ "v32@0:8@16d24"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40"
+ "voBi"
+ "voKi"
+ "voPk"
+ "voPs"
+ "voSi"
+ "voWi"
+ "{apfs_label_purgeable_request=QQQQQQ}32@0:8Q16@24"
- "%@ became active"
- "%@ became inactive"
- "*** unable to metric info to bbagent"
- "*** unable to send boot state change to bbagent"
- "*** unable to send trigger info to bbagent"
- "*** unable to send wake info to bbagent"
- "/Library/BatteryLife/UpgradeLogs"
- "/private/var"
- "@24@0:8q16"
- "ABM Client: triggerPeriodicMetrics with trigger id %d"
- "AnimatedStickerScoring"
- "Attempted to stop powerlogHelperd when %lu services are active; keeping powerlogHelperd alive"
- "B24@?0@\"NSString\"8Q16"
- "B32@0:8@16Q24"
- "B40@0:8@16@24Q32"
- "Background Processing dB disabled"
- "BaselineSysCap"
- "Bdg"
- "Build directory: %@ numContents: %lu"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_VOLUME"
- "CM-CRABS"
- "CM-FILE"
- "CM-HLS"
- "Car"
- "Currently active services: %@"
- "DroopCtrlEff"
- "DurationOfPreUVLODown"
- "Failed query command"
- "Failed to get contents of directory at %@ with error: %@"
- "Failed to mark %@ purgeable - can't open error: %s"
- "Failed to mark %@ purgeable - flags 0x%llx returned %d (%s)"
- "Failed to mark files in directory %@ purgeable -- error when retrieving contents of directory: '%@'"
- "Failed to mark files in directory %@ purgeable -- path is not directory"
- "Failed to remove file at path: %@ with error: %@"
- "Failed to retreive attributes for file: %@ with error: %@"
- "GroupActivities"
- "HeartBeatStatus"
- "IBR"
- "Idx"
- "IsOnDemand"
- "Marked %@ purgeable with urgency: %llu"
- "MaxFileRetentionInDays"
- "MaxFilesPostPurge"
- "ModeledSysCap"
- "MomentsDeferredProcessing"
- "NetSysCap"
- "No active services; stopping powerlogHelperd"
- "Occurences of PreUVLO Downs"
- "OverrideSysCap"
- "PLArchiveManager::trimBGSQL: disabled"
- "PLBatteryGaugeService"
- "PLCacheDeleteUtility"
- "PLHealthSensorAgent_EventPoint_Escalation"
- "PLHelperdLifecycleManager"
- "PLHelperdLifecycleManager.serviceIsActive"
- "PLHelperdLifecycleManager.serviceIsInactive"
- "PLPowerMetricMonitorService"
- "PLXPCAgent_EventForward_SosSoundTrigger"
- "Pb"
- "Periodic purge request with info: %@ urgency: %d"
- "Periodic purge result: %@"
- "Pp"
- "PreUVLODownOccurences"
- "ProactiveSysCap"
- "ProcessedAssetCount"
- "ProcessingType"
- "ProductType"
- "Ps"
- "Purge request with info: %@ urgency: %d"
- "Purge result: %@"
- "Purgeable %lu bytes for build directory: %@"
- "Purgeable %lu bytes for version directory: %@"
- "Purgeable request with info: %@ urgency: %d"
- "Purgeable result: %@"
- "Purged %lu bytes for build directory: %@"
- "Purged %lu bytes for version directory: %@"
- "Pwr"
- "Q32@0:8@16Q24"
- "R0"
- "R1"
- "R2"
- "R3"
- "Received BB wake info: \n %@"
- "Received event metric: \n %@"
- "RequestedAssetCount"
- "Signaled service inactive for %@ which is not currently active."
- "Skipping %@ for marking as purgeable -- file is of type '%@' & doesn't not match given extension filter."
- "SosSoundTrigger"
- "SoundD"
- "StaticStickerScoring"
- "StickerScoringAssetCount"
- "Successfully executed query command"
- "T@\"NSMutableSet\",&,V_activeServices"
- "TStamp"
- "TotalDemandAdj"
- "TotalDemandRaw"
- "Vgg"
- "VisualSearchAssetCount"
- "VoicemailDuration"
- "Will attempt to stop powerlogHelperd after %d seconds"
- "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
- "_activeServices"
- "absoluteString"
- "activeServices"
- "avgRdcRatio"
- "avgRunningPwr"
- "background_processing_db"
- "baselineR0"
- "baselineR1"
- "baselineR2"
- "baselineR3"
- "bytesDownloaded"
- "com.apple.powerlog.CacheDelete"
- "devBoardDevice"
- "devBoardDevice: returning %d"
- "enforceRetentionForDirectory:withMaxDays:"
- "enforceRetentionForVersionDirectory:"
- "fileCreationDate"
- "getDeviceSoC"
- "hardwareModel"
- "hardwareModel: HWModelStr = %@"
- "hardwareModel: returning %@"
- "hardwareModelSMC:"
- "isAudioAccessory"
- "isServiceActive:"
- "mPb"
- "mPp"
- "markFileAsPurgeable:withUrgency:"
- "markFilesAsPurgeable:withUrgency:"
- "markFilesInDirectoryAsPurgeable:ofType:withUrgency:"
- "outputFlag"
- "periodicPurgeBlockWithInfo:withUrgency:"
- "powerlogHelperdLifecycleManager"
- "productType"
- "purgeBlockWithInfo:withUrgency:"
- "purgeBuildDirectory:"
- "purgeVersionDirectory:"
- "purgeableBlockWithInfo:withUrgency:"
- "purgeableSizeForBuildDirectory:"
- "purgeableSizeForVersionDirectory:"
- "registerCacheDelete"
- "registerCacheDeleteFull"
- "reqBdg"
- "serviceNameFor:"
- "session"
- "setActiveServices:"
- "shouldSetupCore"
- "signalServiceActive:"
- "signalServiceInactive:"
- "stopPowerlogHelperd"
- "traverseBuildDirectory:withBlock:"
- "triggerPeriodicMetrics:"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40"

```
