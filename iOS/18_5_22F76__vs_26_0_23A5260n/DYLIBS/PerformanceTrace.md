## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-218.2.0.0.0
-  __TEXT.__text: 0x4ae0
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x6b8
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__cstring: 0x8c6
-  __TEXT.__oslogstring: 0x24c
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methname: 0x13b2
-  __TEXT.__objc_methtype: 0x348
-  __TEXT.__objc_stubs: 0x11a0
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0x10
+234.0.0.0.0
+  __TEXT.__text: 0x11d70
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0xc4c
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0xc78
+  __TEXT.__cstring: 0xd39
+  __TEXT.__oslogstring: 0xce5
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__objc_classname: 0x158
+  __TEXT.__objc_methname: 0x2463
+  __TEXT.__objc_methtype: 0x6d7
+  __TEXT.__objc_stubs: 0x1be0
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xa80
-  __AUTH_CONST.__objc_const: 0xa88
+  __DATA_CONST.__objc_selrefs: 0x9a8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__objc_const: 0x1318
   __AUTH_CONST.__objc_intobj: 0x90
-  __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x2a0
-  __DATA_DIRTY.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x168
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__data: 0x368
+  __DATA.__bss: 0xd0
+  __DATA_DIRTY.__objc_data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2DBFF2B-64D6-3F6F-984B-B39F2B69DBE1
-  Functions: 126
-  Symbols:   595
-  CStrings:  507
+  UUID: 8A885FA9-230E-3F0E-9ACD-1CDBF55FF0D6
+  Functions: 334
+  Symbols:   1301
+  CStrings:  831
 
Symbols:
+ +[NSError(PerformanceTrace) passiveTraceError:description:]
+ +[PTPassiveTraceConfig sharedConfig:]
+ +[PTPassiveTraceConfig sharedConfig:].cold.1
+ +[PTPassiveTraceConfig smallMSSPMIInterval]
+ +[PTTraceConfig isInRecordingWorkflow]
+ +[PTTraceConfig(ControlCenter) availableTracePlanNames]
+ +[PTTraceConfig(ControlCenter) availableTracePlanNames].cold.1
+ +[PTTraceConfig(ControlCenter) displayNameForTracePlanName:]
+ +[PTTraceConfig(ControlCenter) displayNameForTracePlanName:].cold.1
+ +[PTTraceConfig(ControlCenter) displayNameForTracePlanName:].cold.2
+ +[PTTraceConfig(ControlCenter) globalSettingsAreLocked]
+ +[PTTraceConfig(ControlCenter) globalSettingsAreLocked].cold.1
+ +[PTTraceConfig(ControlCenter) isControlCenterModuleAvailable]
+ +[PTTraceConfig(ControlCenter) setControlCenterModuleAvailable:]
+ +[PTTraceConfig(ControlCenter) setUserSelectedTracePlanName:]
+ +[PTTraceConfig(ControlCenter) setUserSelectedTracePlanName:].cold.1
+ +[PTTraceConfig(ControlCenter) setUserSpecifiedCustomTracePlanArguments:]
+ +[PTTraceConfig(ControlCenter) userSelectedTracePlanName]
+ +[PTTraceConfig(ControlCenter) userSelectedTracePlanName].cold.1
+ +[PTTraceConfig(ControlCenter) userSpecifiedCustomTracePlanArguments]
+ -[PTGlobalStateChangeMonitor .cxx_destruct]
+ -[PTGlobalStateChangeMonitor dealloc]
+ -[PTGlobalStateChangeMonitor dealloc].cold.1
+ -[PTGlobalStateChangeMonitor initWithQueue:stateChangeBlock:]
+ -[PTGlobalStateChangeMonitor initWithQueue:stateChangeBlock:].cold.1
+ -[PTGlobalStateChangeMonitor notify_token]
+ -[PTGlobalStateChangeMonitor stateChangeBlock]
+ -[PTGlobalStateChangeMonitor targetQueue]
+ -[PTPassiveTraceArchiveHandle .cxx_destruct]
+ -[PTPassiveTraceArchiveHandle aarPath]
+ -[PTPassiveTraceArchiveHandle dealloc]
+ -[PTPassiveTraceArchiveHandle initWithAarPath:sandboxExtension:]
+ -[PTPassiveTraceArchiveHandle sandboxToken]
+ -[PTPassiveTraceConfig .cxx_destruct]
+ -[PTPassiveTraceConfig applySetting:]
+ -[PTPassiveTraceConfig cancelCurrentSettingWithoutCollecting]
+ -[PTPassiveTraceConfig collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:]
+ -[PTPassiveTraceConfig collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:]
+ -[PTPassiveTraceConfig collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:errorOut:]
+ -[PTPassiveTraceConfig connectionInvalidated]
+ -[PTPassiveTraceConfig connection]
+ -[PTPassiveTraceConfig fetchCollectAppInFocus:]
+ -[PTPassiveTraceConfig fetchCollectLoggingAppLaunch:]
+ -[PTPassiveTraceConfig fetchCollectLoggingHangs:]
+ -[PTPassiveTraceConfig fetchCollectLoggingMetalFramePacing:]
+ -[PTPassiveTraceConfig fetchCollectLoggingPerfPowerMetrics:]
+ -[PTPassiveTraceConfig fetchCollectLoggingScrolling:]
+ -[PTPassiveTraceConfig fetchCollectLoggingUserInteraction:]
+ -[PTPassiveTraceConfig fetchCollectLookbackInterval:]
+ -[PTPassiveTraceConfig fetchCollectMSS:]
+ -[PTPassiveTraceConfig fetchCurrentSetting:]
+ -[PTPassiveTraceConfig fetchMSSPMICycleInterval:]
+ -[PTPassiveTraceConfig fetchMetalPerDrawableSignpostsEnabled:]
+ -[PTPassiveTraceConfig fetchPerfPowerMetricMonitorEnabled:]
+ -[PTPassiveTraceConfig fetchPerfPowerMetricMonitoredProcesses:]
+ -[PTPassiveTraceConfig fetchRecordingStartDate:]
+ -[PTPassiveTraceConfig init:]
+ -[PTPassiveTraceConfig instrumentationConfigLocked:]
+ -[PTPassiveTraceConfig pingService:errorOut:]
+ -[PTPassiveTraceConfig proxyError]
+ -[PTPassiveTraceConfig resetPassiveCollectionSettings:]
+ -[PTPassiveTraceConfig setProxyError:]
+ -[PTPassiveTraceConfig syncRemoteProxy]
+ -[PTPassiveTraceConfig updateCollectAppInFocus:]
+ -[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]
+ -[PTPassiveTraceConfig updateCollectLoggingHangs:]
+ -[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]
+ -[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]
+ -[PTPassiveTraceConfig updateCollectLoggingScrolling:]
+ -[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]
+ -[PTPassiveTraceConfig updateCollectLookbackInterval:]
+ -[PTPassiveTraceConfig updateCollectMSS:]
+ -[PTPassiveTraceConfig updateMSSPMICycleInterval:]
+ -[PTPassiveTraceConfig updateMetalPerDrawableSignpostsEnabled:]
+ -[PTPassiveTraceConfig updatePerfPowerMetricMonitorEnabled:]
+ -[PTPassiveTraceConfig updatePerfPowerMetricMonitoredProcesses:]
+ -[PTPassiveTraceConfig updateRecordingStartDate:]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table11
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table13
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table9
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table97
+ GCC_except_table99
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PTGlobalStateChangeMonitor
+ _OBJC_CLASS_$_PTPassiveTraceArchiveHandle
+ _OBJC_CLASS_$_PTPassiveTraceConfig
+ _OBJC_IVAR_$_PTGlobalStateChangeMonitor._notify_token
+ _OBJC_IVAR_$_PTGlobalStateChangeMonitor._stateChangeBlock
+ _OBJC_IVAR_$_PTGlobalStateChangeMonitor._targetQueue
+ _OBJC_IVAR_$_PTPassiveTraceArchiveHandle._aarPath
+ _OBJC_IVAR_$_PTPassiveTraceArchiveHandle._sandboxToken
+ _OBJC_IVAR_$_PTPassiveTraceConfig._connection
+ _OBJC_IVAR_$_PTPassiveTraceConfig._connectionInvalidated
+ _OBJC_IVAR_$_PTPassiveTraceConfig._proxyError
+ _OBJC_IVAR_$_PTPassiveTraceConfig._syncLock
+ _OBJC_IVAR_$_PTPassiveTraceConfig._syncRemoteProxy
+ _OBJC_METACLASS_$_PTGlobalStateChangeMonitor
+ _OBJC_METACLASS_$_PTPassiveTraceArchiveHandle
+ _OBJC_METACLASS_$_PTPassiveTraceConfig
+ _OUTLINED_FUNCTION_1
+ _PTDefaultTraceDirectoryAvailableTraceFileURLs
+ _PTServicesPostStateDidChangeNotification
+ _PTServicesPostStateDidChangeNotification.cold.1
+ __OBJC_$_CLASS_METHODS_PTPassiveTraceConfig
+ __OBJC_$_CLASS_METHODS_PTTraceConfig(ControlCenter)
+ __OBJC_$_INSTANCE_METHODS_PTGlobalStateChangeMonitor
+ __OBJC_$_INSTANCE_METHODS_PTPassiveTraceArchiveHandle
+ __OBJC_$_INSTANCE_METHODS_PTPassiveTraceConfig
+ __OBJC_$_INSTANCE_VARIABLES_PTGlobalStateChangeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_PTPassiveTraceArchiveHandle
+ __OBJC_$_INSTANCE_VARIABLES_PTPassiveTraceConfig
+ __OBJC_$_PROP_LIST_PTGlobalStateChangeMonitor
+ __OBJC_$_PROP_LIST_PTPassiveTraceArchiveHandle
+ __OBJC_$_PROP_LIST_PTPassiveTraceConfig
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PTPCPassiveCollectionConfigurationInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PTPCPassiveCollectionConfigurationInterface
+ __OBJC_$_PROTOCOL_REFS_PTPCPassiveCollectionClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PTPassiveTraceConfig
+ __OBJC_CLASS_RO_$_PTGlobalStateChangeMonitor
+ __OBJC_CLASS_RO_$_PTPassiveTraceArchiveHandle
+ __OBJC_CLASS_RO_$_PTPassiveTraceConfig
+ __OBJC_LABEL_PROTOCOL_$_PTPCPassiveCollectionClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_PTPCPassiveCollectionConfigurationInterface
+ __OBJC_METACLASS_RO_$_PTGlobalStateChangeMonitor
+ __OBJC_METACLASS_RO_$_PTPassiveTraceArchiveHandle
+ __OBJC_METACLASS_RO_$_PTPassiveTraceConfig
+ __OBJC_PROTOCOL_$_PTPCPassiveCollectionClientDelegate
+ __OBJC_PROTOCOL_$_PTPCPassiveCollectionConfigurationInterface
+ __OBJC_PROTOCOL_REFERENCE_$_PTPCPassiveCollectionConfigurationInterface
+ ___100-[PTPassiveTraceConfig collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:]_block_invoke
+ ___100-[PTPassiveTraceConfig collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:]_block_invoke_2
+ ___102-[PTPassiveTraceConfig collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:errorOut:]_block_invoke
+ ___102-[PTPassiveTraceConfig collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:errorOut:]_block_invoke_2
+ ___107-[PTPassiveTraceConfig collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:]_block_invoke
+ ___107-[PTPassiveTraceConfig collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:]_block_invoke_2
+ ___29-[PTPassiveTraceConfig init:]_block_invoke
+ ___29-[PTPassiveTraceConfig init:]_block_invoke.97
+ ___29-[PTPassiveTraceConfig init:]_block_invoke.98
+ ___32-[PTTraceConfig _initConnection]_block_invoke.184
+ ___32-[PTTraceConfig _initConnection]_block_invoke.184.cold.1
+ ___33-[PTTraceSession _initConnection]_block_invoke.31
+ ___33-[PTTraceSession _initConnection]_block_invoke.31.cold.1
+ ___37+[PTPassiveTraceConfig sharedConfig:]_block_invoke
+ ___37-[PTPassiveTraceConfig applySetting:]_block_invoke
+ ___37-[PTPassiveTraceConfig applySetting:]_block_invoke_2
+ ___38+[PTTraceConfig isInRecordingWorkflow]_block_invoke
+ ___38+[PTTraceConfig isInRecordingWorkflow]_block_invoke.cold.1
+ ___40-[PTPassiveTraceConfig fetchCollectMSS:]_block_invoke
+ ___40-[PTPassiveTraceConfig fetchCollectMSS:]_block_invoke_2
+ ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke
+ ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke_2
+ ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke_3
+ ___44-[PTPassiveTraceConfig fetchCurrentSetting:]_block_invoke
+ ___44-[PTPassiveTraceConfig fetchCurrentSetting:]_block_invoke_2
+ ___45-[PTPassiveTraceConfig pingService:errorOut:]_block_invoke
+ ___45-[PTPassiveTraceConfig pingService:errorOut:]_block_invoke_2
+ ___47-[PTPassiveTraceConfig fetchCollectAppInFocus:]_block_invoke
+ ___47-[PTPassiveTraceConfig fetchCollectAppInFocus:]_block_invoke_2
+ ___48-[PTPassiveTraceConfig fetchRecordingStartDate:]_block_invoke
+ ___48-[PTPassiveTraceConfig fetchRecordingStartDate:]_block_invoke_2
+ ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke
+ ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke_2
+ ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke_3
+ ___49-[PTPassiveTraceConfig fetchCollectLoggingHangs:]_block_invoke
+ ___49-[PTPassiveTraceConfig fetchCollectLoggingHangs:]_block_invoke_2
+ ___49-[PTPassiveTraceConfig fetchMSSPMICycleInterval:]_block_invoke
+ ___49-[PTPassiveTraceConfig fetchMSSPMICycleInterval:]_block_invoke_2
+ ___49-[PTPassiveTraceConfig updateRecordingStartDate:]_block_invoke
+ ___49-[PTPassiveTraceConfig updateRecordingStartDate:]_block_invoke_2
+ ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke
+ ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke_2
+ ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke_3
+ ___50-[PTPassiveTraceConfig updateMSSPMICycleInterval:]_block_invoke
+ ___50-[PTPassiveTraceConfig updateMSSPMICycleInterval:]_block_invoke_2
+ ___52-[PTPassiveTraceConfig instrumentationConfigLocked:]_block_invoke
+ ___52-[PTPassiveTraceConfig instrumentationConfigLocked:]_block_invoke_2
+ ___53-[PTPassiveTraceConfig fetchCollectLoggingAppLaunch:]_block_invoke
+ ___53-[PTPassiveTraceConfig fetchCollectLoggingAppLaunch:]_block_invoke_2
+ ___53-[PTPassiveTraceConfig fetchCollectLoggingScrolling:]_block_invoke
+ ___53-[PTPassiveTraceConfig fetchCollectLoggingScrolling:]_block_invoke_2
+ ___53-[PTPassiveTraceConfig fetchCollectLookbackInterval:]_block_invoke
+ ___53-[PTPassiveTraceConfig fetchCollectLookbackInterval:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke
+ ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke_3
+ ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke
+ ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke_3
+ ___54-[PTPassiveTraceConfig updateCollectLookbackInterval:]_block_invoke
+ ___54-[PTPassiveTraceConfig updateCollectLookbackInterval:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectLookbackInterval:]_block_invoke_3
+ ___55+[PTTraceConfig(ControlCenter) availableTracePlanNames]_block_invoke
+ ___55+[PTTraceConfig(ControlCenter) availableTracePlanNames]_block_invoke.cold.1
+ ___55-[PTPassiveTraceConfig resetPassiveCollectionSettings:]_block_invoke
+ ___55-[PTPassiveTraceConfig resetPassiveCollectionSettings:]_block_invoke_2
+ ___59-[PTPassiveTraceConfig fetchCollectLoggingUserInteraction:]_block_invoke
+ ___59-[PTPassiveTraceConfig fetchCollectLoggingUserInteraction:]_block_invoke_2
+ ___59-[PTPassiveTraceConfig fetchPerfPowerMetricMonitorEnabled:]_block_invoke
+ ___59-[PTPassiveTraceConfig fetchPerfPowerMetricMonitorEnabled:]_block_invoke_2
+ ___60+[PTTraceConfig(ControlCenter) displayNameForTracePlanName:]_block_invoke
+ ___60-[PTPassiveTraceConfig fetchCollectLoggingMetalFramePacing:]_block_invoke
+ ___60-[PTPassiveTraceConfig fetchCollectLoggingMetalFramePacing:]_block_invoke_2
+ ___60-[PTPassiveTraceConfig fetchCollectLoggingPerfPowerMetrics:]_block_invoke
+ ___60-[PTPassiveTraceConfig fetchCollectLoggingPerfPowerMetrics:]_block_invoke_2
+ ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke
+ ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke_2
+ ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke_3
+ ___60-[PTPassiveTraceConfig updatePerfPowerMetricMonitorEnabled:]_block_invoke
+ ___60-[PTPassiveTraceConfig updatePerfPowerMetricMonitorEnabled:]_block_invoke_2
+ ___61-[PTGlobalStateChangeMonitor initWithQueue:stateChangeBlock:]_block_invoke
+ ___61-[PTPassiveTraceConfig cancelCurrentSettingWithoutCollecting]_block_invoke
+ ___61-[PTPassiveTraceConfig cancelCurrentSettingWithoutCollecting]_block_invoke_2
+ ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke
+ ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke_2
+ ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke_3
+ ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke
+ ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke_2
+ ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke_3
+ ___62-[PTPassiveTraceConfig fetchMetalPerDrawableSignpostsEnabled:]_block_invoke
+ ___62-[PTPassiveTraceConfig fetchMetalPerDrawableSignpostsEnabled:]_block_invoke_2
+ ___63-[PTPassiveTraceConfig fetchPerfPowerMetricMonitoredProcesses:]_block_invoke
+ ___63-[PTPassiveTraceConfig fetchPerfPowerMetricMonitoredProcesses:]_block_invoke_2
+ ___63-[PTPassiveTraceConfig updateMetalPerDrawableSignpostsEnabled:]_block_invoke
+ ___63-[PTPassiveTraceConfig updateMetalPerDrawableSignpostsEnabled:]_block_invoke_2
+ ___64-[PTPassiveTraceConfig updatePerfPowerMetricMonitoredProcesses:]_block_invoke
+ ___64-[PTPassiveTraceConfig updatePerfPowerMetricMonitoredProcesses:]_block_invoke_2
+ ___NSArray0__struct
+ ____clientLogHandle_block_invoke
+ ____clientPassiveErrorHandle_block_invoke
+ ____clientPassiveHandle_block_invoke
+ ____controlCenterHandle_block_invoke
+ ____passiveArchiveHandleErrorHandle_block_invoke
+ ____passiveArchiveHandleHandle_block_invoke
+ ____stateChangeMonitorHandle_block_invoke
+ ____stateChangeNotificationHandle_block_invoke
+ ____traceSessionClientHandle_block_invoke
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_48_e8_32r40r_e16_v16?0"NSDate"8lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e30_v24?0"NSNumber"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e8_v12?0B8lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e8_v16?0d8lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32r40r48r56r_e43_v32?0"NSString"8"NSString"16"NSError"24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_65_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_literal_global.11
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.200
+ ___block_literal_global.229
+ ___block_literal_global.233
+ ___block_literal_global.236
+ ___block_literal_global.243
+ ___block_literal_global.420
+ ___block_literal_global.78
+ ___block_literal_global.8
+ ___block_literal_global.81
+ ___block_literal_global.89
+ ___block_literal_global.96
+ ___error
+ ___isAppleInternal_block_invoke
+ __clientLogHandle
+ __clientLogHandle.cold.1
+ __clientLogHandle.handle
+ __clientLogHandle.onceToken
+ __clientPassiveErrorHandle
+ __clientPassiveErrorHandle.cold.1
+ __clientPassiveErrorHandle.handle
+ __clientPassiveErrorHandle.onceToken
+ __clientPassiveHandle
+ __clientPassiveHandle.cold.1
+ __clientPassiveHandle.handle
+ __clientPassiveHandle.onceToken
+ __controlCenterHandle
+ __controlCenterHandle.cold.1
+ __controlCenterHandle.handle
+ __controlCenterHandle.onceToken
+ __os_signpost_emit_with_name_impl
+ __passiveArchiveHandleErrorHandle
+ __passiveArchiveHandleErrorHandle.cold.1
+ __passiveArchiveHandleErrorHandle.handle
+ __passiveArchiveHandleErrorHandle.onceToken
+ __passiveArchiveHandleHandle
+ __passiveArchiveHandleHandle.cold.1
+ __passiveArchiveHandleHandle.handle
+ __passiveArchiveHandleHandle.onceToken
+ __stateChangeMonitorHandle
+ __stateChangeMonitorHandle.cold.1
+ __stateChangeMonitorHandle.handle
+ __stateChangeMonitorHandle.onceToken
+ __stateChangeNotificationHandle
+ __stateChangeNotificationHandle.cold.1
+ __stateChangeNotificationHandle.handle
+ __stateChangeNotificationHandle.onceToken
+ __traceSessionClientHandle
+ __traceSessionClientHandle.cold.1
+ __traceSessionClientHandle.handle
+ __traceSessionClientHandle.onceToken
+ _availableTracePlanNames.availablePlans
+ _availableTracePlanNames.onceToken
+ _dispatch_once
+ _displayNameForTracePlanName:.onceToken
+ _displayNameForTracePlanName:.tracePlanNameToDisplayNameMap
+ _isAppleInternal
+ _isAppleInternal.cold.1
+ _isAppleInternal.isAppleInternal
+ _isAppleInternal.pred
+ _kPTControlCenterModulePrefsDomainName
+ _kPTControlCenterPrefsAvailableKeyName
+ _kPTControlCenterPrefsCustomTracePlanArgumentsPreferenceKeyName
+ _kPTControlCenterPrefsDomainName
+ _kPTControlCenterPrefsSelectedTracePlanNamePreferenceKeyName
+ _kPTPassiveTracePlanNameLightweightPowerMetrics
+ _kPTPassiveTracePlanNamePassive
+ _kPTTracePlanNameCustom
+ _kPTTracePlanNameDefault
+ _kPTTracePlanNameProfile
+ _notify_cancel
+ _notify_post
+ _notify_register_dispatch
+ _objc_autorelease
+ _objc_msgSend$UTF8String
+ _objc_msgSend$aarPath
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$applyPresetSettings:callback:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$availableTracePlanNames
+ _objc_msgSend$clearCurrentPresetSettings:
+ _objc_msgSend$collectAndClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:callback:
+ _objc_msgSend$collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:callback:
+ _objc_msgSend$collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:callback:
+ _objc_msgSend$connectionInvalidated
+ _objc_msgSend$containsObject:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$getCollectAppInFocus:
+ _objc_msgSend$getCollectLoggingAppLaunch:
+ _objc_msgSend$getCollectLoggingHangs:
+ _objc_msgSend$getCollectLoggingMetalFramePacing:
+ _objc_msgSend$getCollectLoggingPerfPowerMetrics:
+ _objc_msgSend$getCollectLoggingScrolling:
+ _objc_msgSend$getCollectLoggingUserInteraction:
+ _objc_msgSend$getCollectLookbackInterval:
+ _objc_msgSend$getCollectMSS:
+ _objc_msgSend$getCurrentPresetSettings:
+ _objc_msgSend$getImitationRecordStartDate:
+ _objc_msgSend$getInstrumentationConfigIsLocked:
+ _objc_msgSend$getMetalPerDrawableSignpostsEnabled:
+ _objc_msgSend$getMetricMonitoredAppProcessNames:
+ _objc_msgSend$getMetricMonitoringEnabled:
+ _objc_msgSend$getMssPmiCycleInterval:
+ _objc_msgSend$hasDirectoryPath
+ _objc_msgSend$init:
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithAarPath:sandboxExtension:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$instrumentationConfigLocked:
+ _objc_msgSend$intValue
+ _objc_msgSend$isControlCenterModuleAvailable
+ _objc_msgSend$isInRecordingWorkflow
+ _objc_msgSend$isInRecordingWorkflow:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$notify_token
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$passiveTraceError:description:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pingService:callback:
+ _objc_msgSend$proxyError
+ _objc_msgSend$resetCollectAppInFocus:
+ _objc_msgSend$resetCollectLoggingAppLaunch:
+ _objc_msgSend$resetCollectLoggingHangs:
+ _objc_msgSend$resetCollectLoggingMetalFramePacing:
+ _objc_msgSend$resetCollectLoggingPerfPowerMetrics:
+ _objc_msgSend$resetCollectLoggingScrolling:
+ _objc_msgSend$resetCollectLoggingUserInteraction:
+ _objc_msgSend$resetCollectLookbackInterval:
+ _objc_msgSend$resetCollectMSS:
+ _objc_msgSend$resetSettings:
+ _objc_msgSend$sandboxToken
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setCollectAppInFocus:callback:
+ _objc_msgSend$setCollectLoggingAppLaunch:callback:
+ _objc_msgSend$setCollectLoggingHangs:callback:
+ _objc_msgSend$setCollectLoggingMetalFramePacing:callback:
+ _objc_msgSend$setCollectLoggingPerfPowerMetrics:callback:
+ _objc_msgSend$setCollectLoggingScrolling:callback:
+ _objc_msgSend$setCollectLoggingUserInteraction:callback:
+ _objc_msgSend$setCollectLookbackInterval:callback:
+ _objc_msgSend$setCollectMSS:callback:
+ _objc_msgSend$setImitationRecordStartDate:callback:
+ _objc_msgSend$setMetalPerDrawableSignpostsEnabled:callback:
+ _objc_msgSend$setMetricMonitoredAppProcessNames:callback:
+ _objc_msgSend$setMetricMonitoringEnabled:callback:
+ _objc_msgSend$setMssPmiCycleInterval:callback:
+ _objc_msgSend$setProxyError:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$sharedConfig:
+ _objc_msgSend$stateChangeBlock
+ _objc_msgSend$syncRemoteProxy
+ _objc_msgSend$targetQueue
+ _objc_msgSend$userSelectedTracePlanName
+ _objc_release_x1
+ _objc_retainAutorelease
+ _objc_retainBlock
+ _objc_retain_x10
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x9
+ _os_log_create
+ _os_signpost_enabled
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _os_variant_has_internal_diagnostics
+ _sandbox_extension_consume
+ _sandbox_extension_release
+ _sharedConfig:.allocError
+ _sharedConfig:.onceToken
+ _sharedConfig:.shared
+ _strerror
- GCC_except_table12
- GCC_except_table5
- GCC_except_table8
- __OBJC_$_CLASS_METHODS_PTTraceConfig
- ___32-[PTTraceConfig _initConnection]_block_invoke.175
- ___32-[PTTraceConfig _initConnection]_block_invoke.175.cold.1
- ___33-[PTTraceSession _initConnection]_block_invoke.29
- ___33-[PTTraceSession _initConnection]_block_invoke.29.cold.1
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.87
- __os_log_default
CStrings:
+ "%{public}@"
+ "%{public}@ is already the selected trace plan"
+ "%{public}@ isn't a valid trace plan name"
+ "-"
+ "@\"<PTPCPassiveCollectionConfigurationInterface>\""
+ "@\"NSError\""
+ "@\"NSNumber\""
+ "@24@0:8^@16"
+ "@32@0:8@16@24"
+ "@32@0:8@16@?24"
+ "@32@0:8@16^@24"
+ "@36@0:8@16B24^@28"
+ "@52@0:8@16@24@32B40^@44"
+ "@?"
+ "@?16@0:8"
+ "An error occurred getting recording state."
+ "B24@0:8^@16"
+ "Client"
+ "Client process could not establish connection to the backing mach service"
+ "ClientPassiveConfiguration"
+ "ClientPassiveConfigurationError"
+ "Connection to passive collection service invalidated. Client process will no longer attempt to communicate with service and all functionality will error out."
+ "Control Center module availability status from preferences : %{public}@"
+ "ControlCenter"
+ "ControlCenter module is already available"
+ "ControlCenterPerformanceTraceCustomTracePlanArguments"
+ "ControlCenterPerformanceTraceIsAvailable"
+ "ControlCenterPerformanceTraceSelectedTracePlanName"
+ "CouldNotGetRemoteObjectProxy"
+ "Custom (Apple Internal)"
+ "Custom trace plan arguments from preferences: %{public}@"
+ "Encountered error: %{public}@"
+ "ExtensionConsumptionFailed"
+ "Failed to consume sandbox extension for '%{public}@' due to error: %{public}s"
+ "Failed to create query item for key: %{public}@, value: %{public}@"
+ "Failed to get global settings, so defaulting to unlocked. Passive config error: %{public}@"
+ "Failed to post notification for new global state change. Status: %{public}#x"
+ "Failed to register from global state change notifications with status: %#x"
+ "Failed to release sandbox extension for %{public}@ due to error: %{public}s"
+ "Failed to reset due to error: %{public}@"
+ "Failed to unregister from global state change notifications with status: %#x"
+ "Failed with error: %{public}@"
+ "FailedToAllocateSharedInstance"
+ "Falling back to trace plan named %{public}@"
+ "FetchAppInFocus"
+ "FetchLoggingAppLaunch"
+ "FetchLoggingHangs"
+ "FetchLoggingMetalFramePacing"
+ "FetchLoggingPerfPowerMetrics"
+ "FetchLoggingScrolling"
+ "FetchLoggingUserInteraction"
+ "FetchLookbackInterval"
+ "FetchMSS"
+ "Fired notification handler block"
+ "Getting recording state config"
+ "Global settings are %{public}@ due to passive instrumentation locked setting"
+ "Global settings are locked since we are in recording workflow"
+ "GlobalStateChangeMonitor"
+ "Got recording state: %{public}@"
+ "Lookback Collection"
+ "Not Recording"
+ "PTGlobalStateChangeMonitor"
+ "PTPCPassiveCollectionClientDelegate"
+ "PTPCPassiveCollectionConfigurationInterface"
+ "PTPassiveTraceArchiveHandle"
+ "PTPassiveTraceConfig"
+ "PassiveArchiveHandle"
+ "PassiveArchiveHandleError"
+ "PassiveTraceArchiveHandleCreation"
+ "PassiveTraceArchiveHandleExtensionRelease"
+ "PassiveTraceArchiveHandleExtensionReleaseFailure"
+ "Posted global state change notification"
+ "Power Profiler"
+ "Recording"
+ "Reset configuration to default"
+ "ResetError"
+ "ResetSuccess"
+ "SBIconVisibility"
+ "Selected trace plan name from preferences (%{public}@) is either invalid or not available for this build variant/configuration"
+ "Selected trace plan name from preferences: %{public}@"
+ "Sending Ping: %{public}@"
+ "ServiceConnectionInterrupted"
+ "ServiceConnectionInvalidated"
+ "StateChangeNotification"
+ "Successfully created an archive handle for '%{public}@'"
+ "Successfully released the sandbox extension for %{public}@"
+ "SynchronousRemoteObjectProxyError"
+ "System Activity (Detailed)"
+ "System Activity (Summary)"
+ "T@\"<PTPCPassiveCollectionConfigurationInterface>\",R,N,V_syncRemoteProxy"
+ "T@\"NSError\",&,N,V_proxyError"
+ "T@\"NSNumber\",R,N,V_notify_token"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_targetQueue"
+ "T@\"NSString\",R,N,V_aarPath"
+ "T@\"NSXPCConnection\",R,N,V_connection"
+ "T@?,R,N,V_stateChangeBlock"
+ "TB,R,N,V_connectionInvalidated"
+ "Tq,R,N,V_sandboxToken"
+ "Trace completed with URL: %{public}@, error: %{public}@"
+ "Trace directory is not a directory"
+ "TraceSessionClient"
+ "UTF8String"
+ "Unknown"
+ "UpdateAppInFocus"
+ "UpdateLoggingAppLaunch"
+ "UpdateLoggingHangs"
+ "UpdateLoggingMetalFramePacing"
+ "UpdateLoggingPerfPowerMetrics"
+ "UpdateLoggingScrolling"
+ "UpdateLoggingUserInteraction"
+ "UpdateLookbackInterval"
+ "UpdateMSS"
+ "Value: %{public}@"
+ "Writing Control Center module availability status to preferences : %{BOOL}d"
+ "Writing custom trace plan arguments to preferences: %{public}@"
+ "Writing selected trace plan name to preferences: %{public}@"
+ "_aarPath"
+ "_connectionInvalidated"
+ "_notify_token"
+ "_proxyError"
+ "_sandboxToken"
+ "_stateChangeBlock"
+ "_syncLock"
+ "_syncRemoteProxy"
+ "_targetQueue"
+ "aar"
+ "aarPath"
+ "addObjectsFromArray:"
+ "applyPresetSettings:callback:"
+ "applySetting:"
+ "arrayWithObjects:count:"
+ "atrc"
+ "availableTracePlanNames"
+ "cancelCurrentSettingWithoutCollecting"
+ "clearCurrentPresetSettings:"
+ "collectAndClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:callback:"
+ "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:callback:"
+ "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:"
+ "collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:"
+ "collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:callback:"
+ "collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:errorOut:"
+ "com.apple.PerformanceTrace"
+ "com.apple.PerformanceTrace.ControlCenterPrefs"
+ "com.apple.PerformanceTrace.ptpassivecollectiond.collectionconfig"
+ "com.apple.control-center.PerformanceTraceModule"
+ "com.apple.performancetrace.global_state_did_change"
+ "connectionInvalidated"
+ "containsObject:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "custom"
+ "dealloc"
+ "default"
+ "displayNameForTracePlanName:"
+ "fetchCollectAppInFocus:"
+ "fetchCollectLoggingAppLaunch:"
+ "fetchCollectLoggingHangs:"
+ "fetchCollectLoggingMetalFramePacing:"
+ "fetchCollectLoggingPerfPowerMetrics:"
+ "fetchCollectLoggingScrolling:"
+ "fetchCollectLoggingUserInteraction:"
+ "fetchCollectLookbackInterval:"
+ "fetchCollectMSS:"
+ "fetchCurrentSetting:"
+ "fetchMSSPMICycleInterval:"
+ "fetchMetalPerDrawableSignpostsEnabled:"
+ "fetchPerfPowerMetricMonitorEnabled:"
+ "fetchPerfPowerMetricMonitoredProcesses:"
+ "fetchRecordingStartDate:"
+ "getCollectAppInFocus:"
+ "getCollectLoggingAppLaunch:"
+ "getCollectLoggingHangs:"
+ "getCollectLoggingMetalFramePacing:"
+ "getCollectLoggingPerfPowerMetrics:"
+ "getCollectLoggingScrolling:"
+ "getCollectLoggingUserInteraction:"
+ "getCollectLookbackInterval:"
+ "getCollectMSS:"
+ "getCurrentPresetSettings:"
+ "getImitationRecordStartDate:"
+ "getInstrumentationConfigIsLocked:"
+ "getMetalPerDrawableSignpostsEnabled:"
+ "getMetricMonitoredAppProcessNames:"
+ "getMetricMonitoringEnabled:"
+ "getMssPmiCycleInterval:"
+ "globalSettingsAreLocked"
+ "hasDirectoryPath"
+ "init:"
+ "initFileURLWithPath:"
+ "initWithAarPath:sandboxExtension:"
+ "initWithMachServiceName:options:"
+ "initWithQueue:stateChangeBlock:"
+ "initWithSuiteName:"
+ "instrumentationConfigLocked:"
+ "intValue"
+ "isControlCenterModuleAvailable"
+ "isInRecordingWorkflow"
+ "isInRecordingWorkflow:"
+ "lightweight power metrics"
+ "localizedDescription"
+ "locked"
+ "not locked"
+ "notify_token"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "passive"
+ "passiveTraceError:description:"
+ "pathExtension"
+ "pingService:callback:"
+ "pingService:errorOut:"
+ "profile"
+ "proxyError"
+ "q"
+ "q16@0:8"
+ "resetCollectAppInFocus:"
+ "resetCollectLoggingAppLaunch:"
+ "resetCollectLoggingHangs:"
+ "resetCollectLoggingMetalFramePacing:"
+ "resetCollectLoggingPerfPowerMetrics:"
+ "resetCollectLoggingScrolling:"
+ "resetCollectLoggingUserInteraction:"
+ "resetCollectLookbackInterval:"
+ "resetCollectMSS:"
+ "resetPassiveCollectionSettings:"
+ "resetSettings:"
+ "sandboxToken"
+ "setBool:forKey:"
+ "setCollectAppInFocus:callback:"
+ "setCollectLoggingAppLaunch:callback:"
+ "setCollectLoggingHangs:callback:"
+ "setCollectLoggingMetalFramePacing:callback:"
+ "setCollectLoggingPerfPowerMetrics:callback:"
+ "setCollectLoggingScrolling:callback:"
+ "setCollectLoggingUserInteraction:callback:"
+ "setCollectLookbackInterval:callback:"
+ "setCollectMSS:callback:"
+ "setControlCenterModuleAvailable:"
+ "setImitationRecordStartDate:callback:"
+ "setMetalPerDrawableSignpostsEnabled:callback:"
+ "setMetricMonitoredAppProcessNames:callback:"
+ "setMetricMonitoringEnabled:callback:"
+ "setMssPmiCycleInterval:callback:"
+ "setProxyError:"
+ "setUserSelectedTracePlanName:"
+ "setUserSpecifiedCustomTracePlanArguments:"
+ "setValue:forKey:"
+ "sharedConfig:"
+ "smallMSSPMIInterval"
+ "stateChangeBlock"
+ "syncRemoteProxy"
+ "targetQueue"
+ "tgz"
+ "updateCollectAppInFocus:"
+ "updateCollectLoggingAppLaunch:"
+ "updateCollectLoggingHangs:"
+ "updateCollectLoggingMetalFramePacing:"
+ "updateCollectLoggingPerfPowerMetrics:"
+ "updateCollectLoggingScrolling:"
+ "updateCollectLoggingUserInteraction:"
+ "updateCollectLookbackInterval:"
+ "updateCollectMSS:"
+ "updateMSSPMICycleInterval:"
+ "updateMetalPerDrawableSignpostsEnabled:"
+ "updatePerfPowerMetricMonitorEnabled:"
+ "updatePerfPowerMetricMonitoredProcesses:"
+ "updateRecordingStartDate:"
+ "userSelectedTracePlanName"
+ "userSpecifiedCustomTracePlanArguments"
+ "v12@?0B8"
+ "v12@?0i8"
+ "v16@?0@\"NSDate\"8"
+ "v16@?0d8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDate\">16"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8@?<v@?d>16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSDate\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?@\"NSError\">24"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSError\"24"
+ "v36@0:8@\"NSString\"16B24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">28"
+ "v36@0:8@16B24@?28"
+ "v52@0:8@\"NSDate\"16@\"NSDate\"24@\"NSString\"32B40@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%@"
- "Failed to create query item for key: %@, value: %@"
- "Sending Ping: %@"

```
