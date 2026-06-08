## PerformanceTrace

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0x12af0
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xc4c
+262.0.0.0.0
+  __TEXT.__text: 0x11124
+  __TEXT.__objc_methlist: 0xdbc
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0xd5c
-  __TEXT.__cstring: 0xd25
-  __TEXT.__oslogstring: 0xce5
-  __TEXT.__unwind_info: 0x6a0
-  __TEXT.__objc_classname: 0x158
-  __TEXT.__objc_methname: 0x2463
-  __TEXT.__objc_methtype: 0x6d7
-  __TEXT.__objc_stubs: 0x1be0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__gcc_except_tab: 0x98c
+  __TEXT.__cstring: 0x1409
+  __TEXT.__oslogstring: 0xc30
+  __TEXT.__unwind_info: 0x630
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a8
+  __DATA_CONST.__objc_selrefs: 0xa98
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x250
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x1318
+  __AUTH_CONST.__cfstring: 0x1260
+  __AUTH_CONST.__objc_const: 0x1578
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x168
-  __DATA.__objc_ivar: 0xb0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x208
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x368
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x28

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 294B22C8-2497-37BC-AEAF-B02209FE415C
-  Functions: 341
-  Symbols:   1323
-  CStrings:  829
+  UUID: A1AB2E25-E151-3BA7-89FF-30865644EA16
+  Functions: 362
+  Symbols:   1382
+  CStrings:  393
 
Symbols:
+ +[PTPassiveDataSourceConfig _configFromDictionary:errorOut:]
+ -[PTPassiveCollectionConfig .cxx_destruct]
+ -[PTPassiveCollectionConfig _hasLoggingCategory:]
+ -[PTPassiveCollectionConfig _setLoggingCategory:enabled:]
+ -[PTPassiveCollectionConfig addDataSource:dataCategory:]
+ -[PTPassiveCollectionConfig collectAppInFocus]
+ -[PTPassiveCollectionConfig collectLoggingAppLaunch]
+ -[PTPassiveCollectionConfig collectLoggingHangs]
+ -[PTPassiveCollectionConfig collectLoggingInteractionTracking]
+ -[PTPassiveCollectionConfig collectLoggingMetalFramePacing]
+ -[PTPassiveCollectionConfig collectLoggingMetricKit]
+ -[PTPassiveCollectionConfig collectLoggingPerfPowerMetrics]
+ -[PTPassiveCollectionConfig collectLoggingPointsOfInterest]
+ -[PTPassiveCollectionConfig collectLoggingScrolling]
+ -[PTPassiveCollectionConfig collectLoggingStateReporting]
+ -[PTPassiveCollectionConfig collectMicrostackshot]
+ -[PTPassiveCollectionConfig configForDataSource:]
+ -[PTPassiveCollectionConfig copyWithZone:]
+ -[PTPassiveCollectionConfig dictionaryRepresentation]
+ -[PTPassiveCollectionConfig initWithDictionary:]
+ -[PTPassiveCollectionConfig removeDataSource:dataCategory:]
+ -[PTPassiveCollectionConfig setCollectAppInFocus:]
+ -[PTPassiveCollectionConfig setCollectLoggingAppLaunch:]
+ -[PTPassiveCollectionConfig setCollectLoggingHangs:]
+ -[PTPassiveCollectionConfig setCollectLoggingInteractionTracking:]
+ -[PTPassiveCollectionConfig setCollectLoggingMetalFramePacing:]
+ -[PTPassiveCollectionConfig setCollectLoggingMetricKit:]
+ -[PTPassiveCollectionConfig setCollectLoggingPerfPowerMetrics:]
+ -[PTPassiveCollectionConfig setCollectLoggingPointsOfInterest:]
+ -[PTPassiveCollectionConfig setCollectLoggingScrolling:]
+ -[PTPassiveCollectionConfig setCollectLoggingStateReporting:]
+ -[PTPassiveCollectionConfig setCollectMicrostackshot:]
+ -[PTPassiveCollectionConfig setCollectionConfig:forDataSource:]
+ -[PTPassiveDataSourceConfig .cxx_destruct]
+ -[PTPassiveDataSourceConfig _dictionaryRepresentation]
+ -[PTPassiveDataSourceConfig copyWithZone:]
+ -[PTPassiveDataSourceConfig dataCategories]
+ -[PTPassiveDataSourceConfig initWithDataCategories:options:errorOut:]
+ -[PTPassiveDataSourceConfig options]
+ -[PTPassiveTraceConfig fetchCollectionConfiguration:]
+ -[PTPassiveTraceConfig updateCollectionConfiguration:]
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table54
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table95
+ _OBJC_CLASS_$_PTPassiveCollectionConfig
+ _OBJC_CLASS_$_PTPassiveDataSourceConfig
+ _OBJC_IVAR_$_PTPassiveCollectionConfig._backing
+ _OBJC_IVAR_$_PTPassiveDataSourceConfig._dataCategories
+ _OBJC_IVAR_$_PTPassiveDataSourceConfig._options
+ _OBJC_METACLASS_$_PTPassiveCollectionConfig
+ _OBJC_METACLASS_$_PTPassiveDataSourceConfig
+ _PTCValidateCollectionConfigurationDict
+ _PTCValidateDataSourceConfigDict
+ _PTCValidateDataSourceConfigFields
+ _PTPassiveDataSourceNameAppInFocus
+ _PTPassiveDataSourceNameLogging
+ _PTPassiveDataSourceNameMicrostackshot
+ __OBJC_$_CLASS_METHODS_PTPassiveDataSourceConfig
+ __OBJC_$_INSTANCE_METHODS_PTPassiveCollectionConfig
+ __OBJC_$_INSTANCE_METHODS_PTPassiveDataSourceConfig
+ __OBJC_$_INSTANCE_VARIABLES_PTPassiveCollectionConfig
+ __OBJC_$_INSTANCE_VARIABLES_PTPassiveDataSourceConfig
+ __OBJC_$_PROP_LIST_PTPassiveCollectionConfig
+ __OBJC_$_PROP_LIST_PTPassiveDataSourceConfig
+ __OBJC_CLASS_PROTOCOLS_$_PTPassiveCollectionConfig
+ __OBJC_CLASS_PROTOCOLS_$_PTPassiveDataSourceConfig
+ __OBJC_CLASS_RO_$_PTPassiveCollectionConfig
+ __OBJC_CLASS_RO_$_PTPassiveDataSourceConfig
+ __OBJC_METACLASS_RO_$_PTPassiveCollectionConfig
+ __OBJC_METACLASS_RO_$_PTPassiveDataSourceConfig
+ ___29-[PTPassiveTraceConfig init:]_block_invoke.214
+ ___29-[PTPassiveTraceConfig init:]_block_invoke.215
+ ___53-[PTPassiveTraceConfig fetchCollectionConfiguration:]_block_invoke
+ ___53-[PTPassiveTraceConfig fetchCollectionConfiguration:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectionConfiguration:]_block_invoke
+ ___54-[PTPassiveTraceConfig updateCollectionConfiguration:]_block_invoke_2
+ ___54-[PTPassiveTraceConfig updateCollectionConfiguration:]_block_invoke_3
+ ___block_descriptor_56_e8_32r40r48r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_literal_global.199
+ ___block_literal_global.213
+ ___block_literal_global.379
+ ___block_literal_global.383
+ ___block_literal_global.386
+ ___block_literal_global.392
+ ___block_literal_global.416
+ ___block_literal_global.77
+ ___block_literal_global.80
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_configFromDictionary:errorOut:
+ _objc_msgSend$_dictionaryRepresentation
+ _objc_msgSend$_hasLoggingCategory:
+ _objc_msgSend$_setLoggingCategory:enabled:
+ _objc_msgSend$addDataSource:dataCategory:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$dataCategories
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$getCollectionConfiguration:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithDataCategories:options:errorOut:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$options
+ _objc_msgSend$removeDataSource:dataCategory:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resetCollectionConfiguration:
+ _objc_msgSend$setCollectionConfiguration:callback:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table105
- GCC_except_table108
- GCC_except_table11
- GCC_except_table111
- GCC_except_table114
- GCC_except_table117
- GCC_except_table120
- GCC_except_table123
- GCC_except_table126
- GCC_except_table129
- GCC_except_table132
- GCC_except_table135
- GCC_except_table18
- GCC_except_table21
- GCC_except_table22
- GCC_except_table24
- GCC_except_table25
- GCC_except_table28
- GCC_except_table29
- GCC_except_table31
- GCC_except_table32
- GCC_except_table35
- GCC_except_table36
- GCC_except_table38
- GCC_except_table39
- GCC_except_table42
- GCC_except_table43
- GCC_except_table45
- GCC_except_table46
- GCC_except_table49
- GCC_except_table52
- GCC_except_table53
- GCC_except_table56
- GCC_except_table59
- GCC_except_table63
- GCC_except_table66
- GCC_except_table67
- GCC_except_table70
- GCC_except_table71
- GCC_except_table74
- GCC_except_table78
- GCC_except_table87
- GCC_except_table90
- GCC_except_table91
- GCC_except_table94
- GCC_except_table97
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ___29-[PTPassiveTraceConfig init:]_block_invoke.97
- ___29-[PTPassiveTraceConfig init:]_block_invoke.98
- ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke
- ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke_2
- ___41-[PTPassiveTraceConfig updateCollectMSS:]_block_invoke_3
- ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke
- ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke_2
- ___48-[PTPassiveTraceConfig updateCollectAppInFocus:]_block_invoke_3
- ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke
- ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke_2
- ___50-[PTPassiveTraceConfig updateCollectLoggingHangs:]_block_invoke_3
- ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke
- ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke_2
- ___54-[PTPassiveTraceConfig updateCollectLoggingAppLaunch:]_block_invoke_3
- ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke
- ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke_2
- ___54-[PTPassiveTraceConfig updateCollectLoggingScrolling:]_block_invoke_3
- ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke
- ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke_2
- ___60-[PTPassiveTraceConfig updateCollectLoggingUserInteraction:]_block_invoke_3
- ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke
- ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke_2
- ___61-[PTPassiveTraceConfig updateCollectLoggingMetalFramePacing:]_block_invoke_3
- ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke
- ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke_2
- ___61-[PTPassiveTraceConfig updateCollectLoggingPerfPowerMetrics:]_block_invoke_3
- ___block_literal_global.200
- ___block_literal_global.229
- ___block_literal_global.233
- ___block_literal_global.236
- ___block_literal_global.243
- ___block_literal_global.417
- ___block_literal_global.78
- ___block_literal_global.81
- ___block_literal_global.96
- _objc_msgSend$resetCollectAppInFocus:
- _objc_msgSend$resetCollectLoggingAppLaunch:
- _objc_msgSend$resetCollectLoggingHangs:
- _objc_msgSend$resetCollectLoggingMetalFramePacing:
- _objc_msgSend$resetCollectLoggingPerfPowerMetrics:
- _objc_msgSend$resetCollectLoggingScrolling:
- _objc_msgSend$resetCollectLoggingUserInteraction:
- _objc_msgSend$resetCollectMSS:
- _objc_msgSend$setCollectAppInFocus:callback:
- _objc_msgSend$setCollectLoggingAppLaunch:callback:
- _objc_msgSend$setCollectLoggingHangs:callback:
- _objc_msgSend$setCollectLoggingMetalFramePacing:callback:
- _objc_msgSend$setCollectLoggingPerfPowerMetrics:callback:
- _objc_msgSend$setCollectLoggingScrolling:callback:
- _objc_msgSend$setCollectLoggingUserInteraction:callback:
- _objc_msgSend$setCollectMSS:callback:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "'dataCategories' must be an array"
+ "'dataCategories' must contain only strings"
+ "'options' keys must be strings"
+ "'options' must be a dictionary"
+ "'options' value for key '%@' must be an array"
+ "'options' value for key '%@' must contain only strings"
+ "AppInFocus"
+ "AppLaunch"
+ "Collection configuration dictionary must not be nil"
+ "Collection configuration must contain at least one data source"
+ "Data source configuration dictionary must not be nil"
+ "Data source configuration must be a non-nil dictionary"
+ "DataCategories"
+ "Hangs"
+ "InteractionTracking"
+ "Invalid configuration for data source '%@': %@"
+ "Logging"
+ "MetalFramePacing"
+ "MetricKit"
+ "Microstackshot"
+ "Non-string key in collection configuration dictionary"
+ "Options"
+ "PerfPowerMetrics"
+ "PointsOfInterest"
+ "Scrolling"
+ "Service returned nil collection configuration"
+ "StateReporting"
+ "Value for data source '%@' must be a dictionary"
+ "updateCollectAppInFocus deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingAppLaunch deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingHangs deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingMetalFramePacing deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingPerfPowerMetrics deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingScrolling deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectLoggingUserInteraction deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "updateCollectMSS deprecated. Use -[PTPassiveTraceConfig updateCollectionConfiguration:] instead."
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PTPCPassiveCollectionConfigurationInterface>\""
- "@\"<PTTraceSessionDelegate>\""
- "@\"NSArray\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"PTTraceConfig\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@36@0:8@16B24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "@52@0:8@16@24@32B40^@44"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PTGlobalStateChangeMonitor"
- "PTPCPassiveCollectionClientDelegate"
- "PTPCPassiveCollectionConfigurationInterface"
- "PTPassiveTraceArchiveHandle"
- "PTPassiveTraceConfig"
- "PTServiceInterface"
- "PTTraceConfig"
- "PTTraceSession"
- "PTTraceSessionDelegate"
- "PTTraceSessionDelegatePrivate"
- "PerformanceTrace"
- "Q16@0:8"
- "T#,R"
- "T@\"<PTPCPassiveCollectionConfigurationInterface>\",R,N,V_syncRemoteProxy"
- "T@\"<PTTraceSessionDelegate>\",&,N,V_delegate"
- "T@\"NSArray\",&,N,V_traceRecordArgs"
- "T@\"NSError\",&,N,V_proxyError"
- "T@\"NSMutableArray\",&,N,V_traceGroups"
- "T@\"NSNumber\",R,N,V_notify_token"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_targetQueue"
- "T@\"NSObject<OS_os_transaction>\",&,N,V_tracingActiveTransaction"
- "T@\"NSString\",&,N,V_ownerName"
- "T@\"NSString\",&,N,V_planNameOrPath"
- "T@\"NSString\",&,N,V_traceName"
- "T@\"NSString\",&,N,V_traceRecordEndNotificationName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_aarPath"
- "T@\"NSURL\",&,N,V_traceDirectoryURL"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"NSXPCConnection\",R,N,V_connection"
- "T@\"PTTraceConfig\",&,N,V_config"
- "T@?,R,N,V_stateChangeBlock"
- "TB,N,V_compressWhenFinished"
- "TB,N,V_enableSwiftUITracing"
- "TB,N,V_includeKernelStacks"
- "TB,N,V_includeOSLogs"
- "TB,N,V_includeOSSignposts"
- "TB,N,V_overrideIncludeOSLogs"
- "TB,N,V_overrideIncludeOSSignposts"
- "TB,N,V_overrideSymbolicate"
- "TB,N,V_skipNotification"
- "TB,N,V_symbolicate"
- "TB,N,V_useTraceRecord"
- "TB,R"
- "TB,R,N,V_connectionInvalidated"
- "TB,R,N,V_isValid"
- "TI,N,V_kernelBufferDrainQoS"
- "TQ,N,V_callstackSamplingRateMS"
- "TQ,N,V_kernelBufferDrainRateMS"
- "TQ,N,V_kernelBufferSizeMB"
- "TQ,N,V_source"
- "TQ,N,V_traceDurationSecs"
- "TQ,N,V_traceTimeoutS"
- "TQ,N,V_traceType"
- "TQ,R"
- "Ti,N,V_ownerPID"
- "Tq,R,N,V_sandboxToken"
- "URL"
- "URLHostAllowedCharacterSet"
- "UTF8String"
- "UpdateAppInFocus"
- "UpdateLoggingAppLaunch"
- "UpdateLoggingHangs"
- "UpdateLoggingMetalFramePacing"
- "UpdateLoggingPerfPowerMetrics"
- "UpdateLoggingScrolling"
- "UpdateLoggingUserInteraction"
- "UpdateMSS"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_aarPath"
- "_callstackSamplingRateMS"
- "_compressWhenFinished"
- "_config"
- "_connection"
- "_connectionInvalidated"
- "_defaultTraceRecordConfig"
- "_delegate"
- "_didPingService:"
- "_enableSwiftUITracing"
- "_getRemoteObjectProxy"
- "_includeKernelStacks"
- "_includeOSLogs"
- "_includeOSSignposts"
- "_initConnection"
- "_invalidateSession"
- "_isValid"
- "_kernelBufferDrainQoS"
- "_kernelBufferDrainRateMS"
- "_kernelBufferSizeMB"
- "_notify_token"
- "_overrideIncludeOSLogs"
- "_overrideIncludeOSSignposts"
- "_overrideSymbolicate"
- "_ownerName"
- "_ownerPID"
- "_ping:"
- "_planNameOrPath"
- "_proxyError"
- "_queue"
- "_sandboxToken"
- "_skipNotification"
- "_source"
- "_stateChangeBlock"
- "_symbolicate"
- "_syncLock"
- "_syncRemoteProxy"
- "_targetQueue"
- "_traceDirectoryURL"
- "_traceDurationSecs"
- "_traceGroups"
- "_traceName"
- "_traceRecordArgs"
- "_traceRecordEndNotificationName"
- "_traceTimeoutS"
- "_traceType"
- "_tracingActiveTransaction"
- "_useTraceRecord"
- "aarPath"
- "absoluteString"
- "addObject:"
- "addObjectsFromArray:"
- "appendFormat:"
- "appendString:"
- "applyConfig:withError:"
- "applyPresetSettings:callback:"
- "applySetting:"
- "array"
- "arrayWithArray:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "autorelease"
- "availableTracePlanNames"
- "boolValue"
- "cancelCurrentSettingWithoutCollecting"
- "class"
- "clearCurrentPresetSettings:"
- "collectAndClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:callback:"
- "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:callback:"
- "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:"
- "collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:"
- "collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:callback:"
- "collectWithStartDate:endDate:traceNamePrefix:triggerUserNotification:errorOut:"
- "componentsJoinedByString:"
- "config"
- "configWithDictionary:"
- "configWithTemplate:"
- "configWithTracePlanName:"
- "configWithTracePlanURL:"
- "conformsToProtocol:"
- "connection"
- "connectionInvalidated"
- "containsObject:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "defaultWorkspace"
- "delegate"
- "description"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "displayNameForTracePlanName:"
- "displayTraceCompletedAlertWithTraceFileURL:additionalInfo:notificationTimeoutSecs:completionHandler:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error:description:"
- "error:description:underlyingError:"
- "errorWithDomain:code:userInfo:"
- "fetchCollectAppInFocus:"
- "fetchCollectLoggingAppLaunch:"
- "fetchCollectLoggingHangs:"
- "fetchCollectLoggingMetalFramePacing:"
- "fetchCollectLoggingPerfPowerMetrics:"
- "fetchCollectLoggingScrolling:"
- "fetchCollectLoggingUserInteraction:"
- "fetchCollectLookbackInterval:"
- "fetchCollectMSS:"
- "fetchCurrentSetting:"
- "fetchMSSPMICycleInterval:"
- "fetchMetalPerDrawableSignpostsEnabled:"
- "fetchPerfPowerMetricMonitorEnabled:"
- "fetchPerfPowerMetricMonitoredProcesses:"
- "fetchRecordingStartDate:"
- "fileExistsAtPath:isDirectory:"
- "fileURLWithPath:"
- "firstObject"
- "getCollectAppInFocus:"
- "getCollectLoggingAppLaunch:"
- "getCollectLoggingHangs:"
- "getCollectLoggingMetalFramePacing:"
- "getCollectLoggingPerfPowerMetrics:"
- "getCollectLoggingScrolling:"
- "getCollectLoggingUserInteraction:"
- "getCollectLookbackInterval:"
- "getCollectMSS:"
- "getCurrentConfig"
- "getCurrentPresetSettings:"
- "getCurrentStoredConfig:"
- "getImitationRecordStartDate:"
- "getInstrumentationConfigIsLocked:"
- "getMetalPerDrawableSignpostsEnabled:"
- "getMetricMonitoredAppProcessNames:"
- "getMetricMonitoringEnabled:"
- "getMssPmiCycleInterval:"
- "globalSettingsAreLocked"
- "hasDirectoryPath"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "init:"
- "initFileURLWithPath:"
- "initWithAarPath:sandboxExtension:"
- "initWithCoder:"
- "initWithConfig:"
- "initWithMachServiceName:options:"
- "initWithQueue:stateChangeBlock:"
- "initWithServiceName:"
- "initWithSuiteName:"
- "instrumentationConfigLocked:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isControlCenterModuleAvailable"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToString:"
- "isInRecordingWorkflow"
- "isInRecordingWorkflow:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isValid"
- "lastPathComponent"
- "localizedDescription"
- "notify_token"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openURL:configuration:error:"
- "passiveTraceError:description:"
- "path"
- "pathExtension"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performanceTraceDidComplete:withToken:withError:"
- "performanceTraceDidStart:"
- "performanceTraceDidStop:"
- "pingService:"
- "pingService:callback:"
- "pingService:errorOut:"
- "proxyError"
- "q"
- "q16@0:8"
- "queryItemWithName:value:"
- "raise:format:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "resetCollectAppInFocus:"
- "resetCollectLoggingAppLaunch:"
- "resetCollectLoggingHangs:"
- "resetCollectLoggingMetalFramePacing:"
- "resetCollectLoggingPerfPowerMetrics:"
- "resetCollectLoggingScrolling:"
- "resetCollectLoggingUserInteraction:"
- "resetCollectLookbackInterval:"
- "resetCollectMSS:"
- "resetConfig"
- "resetConfig:"
- "resetPassiveCollectionSettings:"
- "resetSettings:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "sandboxToken"
- "self"
- "setBool:forKey:"
- "setCallstackSamplingRateMS:"
- "setCollectAppInFocus:callback:"
- "setCollectLoggingAppLaunch:callback:"
- "setCollectLoggingHangs:callback:"
- "setCollectLoggingMetalFramePacing:callback:"
- "setCollectLoggingPerfPowerMetrics:callback:"
- "setCollectLoggingScrolling:callback:"
- "setCollectLoggingUserInteraction:callback:"
- "setCollectLookbackInterval:callback:"
- "setCollectMSS:callback:"
- "setCompressWhenFinished:"
- "setConfig:"
- "setConnection:"
- "setControlCenterModuleAvailable:"
- "setDelegate:"
- "setEnableSwiftUITracing:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHost:"
- "setImitationRecordStartDate:callback:"
- "setIncludeKernelStacks:"
- "setIncludeOSLogs:"
- "setIncludeOSSignposts:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setKernelBufferDrainQoS:"
- "setKernelBufferDrainRateMS:"
- "setKernelBufferSizeMB:"
- "setMetalPerDrawableSignpostsEnabled:callback:"
- "setMetricMonitoredAppProcessNames:callback:"
- "setMetricMonitoringEnabled:callback:"
- "setMssPmiCycleInterval:callback:"
- "setObject:forKey:"
- "setOverrideIncludeOSLogs:"
- "setOverrideIncludeOSSignposts:"
- "setOverrideSymbolicate:"
- "setOwnerName:"
- "setOwnerPID:"
- "setPlanNameOrPath:"
- "setProxyError:"
- "setQueryItems:"
- "setRemoteObjectInterface:"
- "setScheme:"
- "setSkipNotification:"
- "setSource:"
- "setSymbolicate:"
- "setTraceDirectoryURL:"
- "setTraceDurationSecs:"
- "setTraceGroups:"
- "setTraceName:"
- "setTraceRecordArgs:"
- "setTraceRecordEndNotificationName:"
- "setTraceTimeoutS:"
- "setTraceType:"
- "setTracingActiveTransaction:"
- "setUseTraceRecord:"
- "setUserSelectedTracePlanName:"
- "setUserSpecifiedCustomTracePlanArguments:"
- "setValue:forKey:"
- "setWithObjects:"
- "sharedConfig:"
- "smallMSSPMIInterval"
- "startPerformanceTrace"
- "startPerformanceTrace:"
- "stateChangeBlock"
- "stopPerformanceTrace"
- "storeConfig"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingString:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithString:"
- "superclass"
- "supportsSecureCoding"
- "syncRemoteProxy"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "targetQueue"
- "traceRecordEndNotificationName"
- "tracingActiveTransaction"
- "unsignedIntValue"
- "unsignedLongValue"
- "updateCollectAppInFocus:"
- "updateCollectLoggingAppLaunch:"
- "updateCollectLoggingHangs:"
- "updateCollectLoggingMetalFramePacing:"
- "updateCollectLoggingPerfPowerMetrics:"
- "updateCollectLoggingScrolling:"
- "updateCollectLoggingUserInteraction:"
- "updateCollectLookbackInterval:"
- "updateCollectMSS:"
- "updateMSSPMICycleInterval:"
- "updateMetalPerDrawableSignpostsEnabled:"
- "updatePerfPowerMetricMonitorEnabled:"
- "updatePerfPowerMetricMonitoredProcesses:"
- "updateRecordingStartDate:"
- "userSelectedTracePlanName"
- "userSpecifiedCustomTracePlanArguments"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"PTTraceConfig\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDate\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\"@\"PTTraceConfig\">16"
- "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?d>16"
- "v24@0:8Q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDate\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"PTTraceConfig\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8d16@?24"
- "v32@0:8d16@?<v@?@\"NSError\">24"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v48@0:8@16@24@32@?40"
- "v52@0:8@\"NSDate\"16@\"NSDate\"24@\"NSString\"32B40@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "validateConfig"
- "valueForKey:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
