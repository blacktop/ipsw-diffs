## ARKitDaemon

> `/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon`

```diff

-746.100.4.0.0
-  __TEXT.__text: 0xea10
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x12ac
+779.0.0.0.5
+  __TEXT.__text: 0xe078
+  __TEXT.__objc_methlist: 0x144c
   __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x20dd
-  __TEXT.__cstring: 0x713
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__unwind_info: 0x4f8
-  __TEXT.__objc_classname: 0x390
-  __TEXT.__objc_methname: 0x2aee
-  __TEXT.__objc_methtype: 0xc41
-  __TEXT.__objc_stubs: 0x1ea0
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__gcc_except_tab: 0x4b8
+  __TEXT.__cstring: 0x712
+  __TEXT.__oslogstring: 0x213c
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0xb28
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH_CONST.__const: 0x380
+  __DATA_CONST.__got: 0x1f0
+  __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x4410
+  __AUTH_CONST.__objc_const: 0x4a70
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x124
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
-  - /System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
   - /System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization
+  - /System/Library/SubFrameworks/ARKitCore.framework/ARKitCore
+  - /System/Library/SubFrameworks/ARKitFoundation.framework/ARKitFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE47DED2-62C8-3846-865D-5DC4C9E432E7
-  Functions: 363
-  Symbols:   1713
-  CStrings:  884
+  UUID: BF6BF30B-9B99-38A6-9B4C-C79684BB903D
+  Functions: 387
+  Symbols:   1822
+  CStrings:  263
 
Symbols:
+ +[ARBaseDaemonControl controlInterface]
+ +[ARBaseDaemonControl controlProxyInterface]
+ +[ARBaseDaemonControl serviceName]
+ +[ARDaemon createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:]
+ +[ARDaemon createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:serviceRestrictions:]
+ +[ARDaemon createAnonymousListenerDaemonWithServiceRestrictions:]
+ +[ARDaemonControl controlInterface]
+ +[ARDaemonControl controlProxyInterface]
+ +[ARDaemonServiceRestrictions noRestrictions]
+ +[ARDaemonServiceRestrictions restrictionsWithAllowedServiceNames:]
+ +[ARDaemonServiceRestrictions restrictionsWithAllowedServices:disallowedServices:]
+ +[ARSystemStatusSnapshot snapshotWithProcessName:processIdentifier:spawnTime:]
+ -[ARBaseDaemonControl .cxx_destruct]
+ -[ARBaseDaemonControl connectionDidInterrupt]
+ -[ARBaseDaemonControl connectionDidInvalidate]
+ -[ARBaseDaemonControl connection]
+ -[ARBaseDaemonControl initWithConnection:]
+ -[ARBaseDaemonControl server]
+ -[ARBaseDaemonControl setConnection:]
+ -[ARBaseDaemonControl setServer:]
+ -[ARBaseDaemonControl setStatusLogger:]
+ -[ARBaseDaemonControl statusLogger]
+ -[ARControlListener _acceptConnectionForContext:connection:]
+ -[ARControlListener _acceptConnectionForContext:connection:].cold.1
+ -[ARControlListener _createContextForControlClass:controlType:isInProcess:]
+ -[ARControlListener _createListenerForServiceName:isInProcess:]
+ -[ARControlListener _invalidateContext:]
+ -[ARControlListener endpointForServiceName:]
+ -[ARDaemon _initializeAlgorithmSupportWithGraphScheduler:watchdogMonitor:]
+ -[ARDaemon _initializeServerWithExecutionManager:watchdogMonitor:]
+ -[ARDaemonService minimumChannelBufferSize]
+ -[ARDaemonService minimumDispatchChannelBufferSize]
+ -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:serviceRestrictions:]
+ -[ARDaemonServiceRestrictions .cxx_destruct]
+ -[ARDaemonServiceRestrictions allowsService:]
+ -[ARDaemonServiceRestrictions initWithAllowedServices:disallowedServices:]
+ -[ARInProcessDaemonConfiguration .cxx_destruct]
+ -[ARInProcessDaemonConfiguration initWithServiceRestrictions:]
+ -[ARInProcessDaemonConfiguration init]
+ -[ARInProcessDaemonConfiguration serviceRestrictions]
+ -[ARMainDaemonConfiguration serviceRestrictions]
+ -[ARServer controlListener]
+ -[ARSystemStatusSnapshot .cxx_destruct]
+ -[ARSystemStatusSnapshot toDictionary]
+ -[ARSystemStatusSnapshot toString]
+ GCC_except_table10
+ GCC_except_table18
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table7
+ GCC_except_table8
+ _OBJC_CLASS_$_ARBaseDaemonControl
+ _OBJC_CLASS_$_ARDaemonServiceRestrictions
+ _OBJC_CLASS_$_ARSystemStatusSnapshot
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_ARBaseDaemonControl._connection
+ _OBJC_IVAR_$_ARBaseDaemonControl._server
+ _OBJC_IVAR_$_ARBaseDaemonControl._statusLogger
+ _OBJC_IVAR_$_ARControlListener._control
+ _OBJC_IVAR_$_ARDaemonServiceRestrictions._allowedServices
+ _OBJC_IVAR_$_ARDaemonServiceRestrictions._disallowedServices
+ _OBJC_IVAR_$_ARInProcessDaemonConfiguration._serviceRestrictions
+ _OBJC_IVAR_$_ARServer._batchedServicesTransitionCompleted
+ _OBJC_IVAR_$_ARServer._batchedServicesTransitionCondition
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._processIdentifier
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._processName
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._processUpTimeIncludingSleepAndDriftCorrectionString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._processUpTimeIncludingSleepString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._processUpTimeString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._spawnTime
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._spawnTimeString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._systemBootTimeString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._systemUpTimeIncludingSleepAndDriftCorrectionString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._systemUpTimeIncludingSleepString
+ _OBJC_IVAR_$_ARSystemStatusSnapshot._systemUpTimeString
+ _OBJC_METACLASS_$_ARBaseDaemonControl
+ _OBJC_METACLASS_$_ARDaemonServiceRestrictions
+ _OBJC_METACLASS_$_ARSystemStatusSnapshot
+ __OBJC_$_CLASS_METHODS_ARBaseDaemonControl
+ __OBJC_$_CLASS_METHODS_ARDaemonServiceRestrictions
+ __OBJC_$_CLASS_METHODS_ARSystemStatusSnapshot
+ __OBJC_$_CLASS_PROP_LIST_ARBaseDaemonControl
+ __OBJC_$_CLASS_PROP_LIST_ARDaemonControlProviding
+ __OBJC_$_INSTANCE_METHODS_ARBaseDaemonControl
+ __OBJC_$_INSTANCE_METHODS_ARDaemonServiceRestrictions
+ __OBJC_$_INSTANCE_METHODS_ARSystemStatusSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_ARBaseDaemonControl
+ __OBJC_$_INSTANCE_VARIABLES_ARDaemonServiceRestrictions
+ __OBJC_$_INSTANCE_VARIABLES_ARInProcessDaemonConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ARSystemStatusSnapshot
+ __OBJC_$_PROP_LIST_ARBaseDaemonControl
+ __OBJC_$_PROP_LIST_ARDaemonControlProviding
+ __OBJC_$_PROTOCOL_CLASS_METHODS_ARDaemonControlProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARDaemonControlProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARDaemonControlProviding
+ __OBJC_$_PROTOCOL_REFS_ARDaemonControlProviding
+ __OBJC_CLASS_PROTOCOLS_$_ARBaseDaemonControl
+ __OBJC_CLASS_RO_$_ARBaseDaemonControl
+ __OBJC_CLASS_RO_$_ARDaemonServiceRestrictions
+ __OBJC_CLASS_RO_$_ARSystemStatusSnapshot
+ __OBJC_LABEL_PROTOCOL_$_ARDaemonControlProviding
+ __OBJC_METACLASS_RO_$_ARBaseDaemonControl
+ __OBJC_METACLASS_RO_$_ARDaemonServiceRestrictions
+ __OBJC_METACLASS_RO_$_ARSystemStatusSnapshot
+ __OBJC_PROTOCOL_$_ARDaemonControlProviding
+ ___42-[ARBaseDaemonControl initWithConnection:]_block_invoke
+ ___42-[ARBaseDaemonControl initWithConnection:]_block_invoke_2
+ ___42-[ARServer _configureServiceForExecution:]_block_invoke.44
+ ___42-[ARServer _configureServiceForExecution:]_block_invoke.45
+ ___90-[ARDaemon initWithConfiguration:spawnTime:watchdogMonitor:graphScheduler:replayDelegate:]_block_invoke.6
+ ___92-[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:serviceRestrictions:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_64_e8_32s40r48w_e5_v8?0lr40l8w48l8s32l8u56l8
+ ___block_literal_global.103
+ ___block_literal_global.134
+ ___block_literal_global.138
+ ___block_literal_global.195
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.21
+ ___block_literal_global.83
+ ___block_literal_global.88
+ ___block_literal_global.93
+ ___destructor_8_s8_s16_s24
+ ___move_assignment_8_8_t0w8_s8_s16_s24
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_acceptConnectionForContext:connection:
+ _objc_msgSend$_createContextForControlClass:controlType:isInProcess:
+ _objc_msgSend$_createListenerForServiceName:isInProcess:
+ _objc_msgSend$_initializeAlgorithmSupportWithGraphScheduler:watchdogMonitor:
+ _objc_msgSend$_initializeServerWithExecutionManager:watchdogMonitor:
+ _objc_msgSend$_invalidateContext:
+ _objc_msgSend$_startServiceSynchronous:
+ _objc_msgSend$allowsService:
+ _objc_msgSend$broadcast
+ _objc_msgSend$connectionDidInterrupt
+ _objc_msgSend$connectionDidInvalidate
+ _objc_msgSend$controlListener
+ _objc_msgSend$createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:
+ _objc_msgSend$createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:serviceRestrictions:
+ _objc_msgSend$doesNotRecognizeSelector:
+ _objc_msgSend$endpointForServiceName:
+ _objc_msgSend$initWithAllowedServices:disallowedServices:
+ _objc_msgSend$initWithDelegate:watchdogMonitor:isInProcess:serviceRestrictions:
+ _objc_msgSend$initWithServiceRestrictions:
+ _objc_msgSend$lock
+ _objc_msgSend$minimumChannelBufferSize
+ _objc_msgSend$minimumDispatchChannelBufferSize
+ _objc_msgSend$noRestrictions
+ _objc_msgSend$serviceRestrictions
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$snapshotWithProcessName:processIdentifier:spawnTime:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$toDictionary
+ _objc_msgSend$toString
+ _objc_msgSend$unlock
+ _objc_msgSend$wait
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x5
- +[ARDaemon createAnonymousListenerDaemonWithReplayURL:deterministic:replayDelegate:]
- +[ARDaemon createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:isDryRun:]
- -[ARDaemon runningRemoteServices]
- -[ARDaemonControl .cxx_destruct]
- -[ARDaemonControl interruptionHandler]
- -[ARDaemonControl invalidationHandler]
- -[ARDaemonControl server]
- -[ARDaemonControl setServer:]
- -[ARDaemonControl setStatusLogger:]
- -[ARDaemonControl statusLogger]
- -[ARDaemonService channelDataSize]
- -[ARDaemonService dispatchChannelDataSize]
- -[ARDaemonService isDataAccessAllowed]
- -[ARDaemonService isHidFocused]
- -[ARDaemonService minimumChannelQueueSize]
- -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:ignoredServiceNames:]
- -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:]
- -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:]
- -[ARServer _setupLiteHUDIntegrator]
- -[ARServer listenerEndPointForServiceNamed:]
- -[ARTechniqueService requiredTimeIntervalWithReply:]
- GCC_except_table1
- GCC_except_table22
- GCC_except_table25
- GCC_except_table28
- GCC_except_table33
- GCC_except_table35
- GCC_except_table40
- GCC_except_table41
- GCC_except_table5
- _OBJC_CLASS_$_ARServiceUpdateParameters
- _OBJC_IVAR_$_ARControlListener._controlClass
- _OBJC_IVAR_$_ARControlListener._listener
- _OBJC_IVAR_$_ARDaemon._runningRemoteServices
- _OBJC_IVAR_$_ARDaemonControl._connection
- _OBJC_IVAR_$_ARDaemonControl._server
- _OBJC_IVAR_$_ARDaemonControl._statusLogger
- _OBJC_IVAR_$_ARDaemonService._dataAccessAllowed
- _OBJC_IVAR_$_ARDaemonService._hidFocused
- _OBJC_METACLASS_$_ARServiceUpdateParameters
- __OBJC_$_CLASS_PROP_LIST_ARDaemonControl
- __OBJC_$_INSTANCE_VARIABLES_ARDaemonControl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARLoggingFullDescription
- __OBJC_$_PROTOCOL_METHOD_TYPES_ARLoggingFullDescription
- __OBJC_$_PROTOCOL_REFS_ARLoggingFullDescription
- __OBJC_CLASS_RO_$_ARServiceUpdateParameters
- __OBJC_LABEL_PROTOCOL_$_ARLoggingFullDescription
- __OBJC_METACLASS_RO_$_ARServiceUpdateParameters
- __OBJC_PROTOCOL_$_ARLoggingFullDescription
- ___113-[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:]_block_invoke
- ___30-[ARDaemon startWithServices:]_block_invoke
- ___38-[ARDaemonControl initWithConnection:]_block_invoke
- ___38-[ARDaemonControl initWithConnection:]_block_invoke_2
- ___42-[ARServer _configureServiceForExecution:]_block_invoke.103
- ___42-[ARServer _configureServiceForExecution:]_block_invoke.104
- ___90-[ARDaemon initWithConfiguration:spawnTime:watchdogMonitor:graphScheduler:replayDelegate:]_block_invoke.3
- ___block_descriptor_32_e39_v16?0"<ARDaemonServiceBaseProtocol>"8l
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8u56l8
- ___block_literal_global.106
- ___block_literal_global.140
- ___block_literal_global.144
- ___block_literal_global.19
- ___block_literal_global.22
- ___block_literal_global.259
- ___block_literal_global.263
- ___block_literal_global.266
- ___block_literal_global.81
- ___block_literal_global.86
- ___block_literal_global.94
- _kARDispatchChannelMessageSizeKey
- _objc_msgSend$_startService
- _objc_msgSend$channelDataSize
- _objc_msgSend$createAnonymousListenerDaemonWithReplayURL:deterministic:replayDelegate:
- _objc_msgSend$createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:isDryRun:
- _objc_msgSend$dispatchChannelDataSize
- _objc_msgSend$initWithDelegate:watchdogMonitor:isInProcess:
- _objc_msgSend$initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:
- _objc_msgSend$listenerEndPointForServiceNamed:
- _objc_msgSend$minimumChannelQueueSize
- _objc_msgSend$requiredTimeInterval
- _objc_msgSend$syncServiceWithTimeout:callback:
- _objc_release_x2
- _objc_retain_x28
- _xpc_dictionary_set_uint64
CStrings:
+ "!"
+ "%{public}@ <%p>: Accepted connection for %{public}@."
+ "%{public}@ <%p>: Failed to create %{public}@."
+ "%{public}@ <%p>: Listener received request for %{public}@"
+ "%{public}@ <%p>: Unknown listener: %@"
+ "0@P`"
+ "Error: %{public}@ <%p>: Failed to create %{public}@."
+ "Error: %{public}@ <%p>: Unknown listener: %@"
+ "a"
+ "b"
+ "control"
- "#"
- "#16@0:8"
- "%{public}@ <%p>: Accepted connection for control."
- "%{public}@ <%p>: Failed to create control."
- "%{public}@ <%p>: Listener received request for control"
- ".cxx_destruct"
- "1@`"
- "@\"<ARControlListenerDelegate>\""
- "@\"<ARDaemonConfiguration>\""
- "@\"<ARDaemonServiceDataSource>\""
- "@\"<ARDaemonServiceDataSource>\"16@0:8"
- "@\"<ARDaemonServiceDelegate>\""
- "@\"<ARDaemonServiceDelegate>\"16@0:8"
- "@\"<ARDaemonServiceListenerDelegate>\""
- "@\"<ARMemoryPressureMonitorDelegate>\""
- "@\"<ARRemoteSensorClient>\""
- "@\"<ARRemoteServiceBaseProtocol>\""
- "@\"<ARRemoteTechniqueClient>\""
- "@\"<ARSensor>\""
- "@\"<ARServerStatusLogging>\""
- "@\"<ARServiceType>\"32@0:8@\"<ARServiceType>\"16#24"
- "@\"ARControlListener\""
- "@\"ARDaemonService\""
- "@\"ARDaemonServiceListener\""
- "@\"ARDaemonStatusLogger\""
- "@\"ARDeviceOrientationData\""
- "@\"ARLocationData\""
- "@\"ARMemoryPressureMonitor\""
- "@\"ARRemoteService\""
- "@\"ARServer\""
- "@\"ARSystemTimeSnapshot\""
- "@\"ARTechnique\""
- "@\"ARUserProfile\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\"20@0:8B16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_channel_rt>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_activity>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"20@0:8B16"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"NSXPCListenerEndpoint\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16#24"
- "@36@0:8@\"NSURL\"16B24@\"<ARDaemonReplayDelegate>\"28"
- "@36@0:8@16#24B32"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16B24B28@32B40"
- "@52@0:8@16@24B32@36@44"
- "@56@0:8@16@24@32@40@48"
- "ARAdditions"
- "ARControlListener"
- "ARControlListenerDelegate"
- "ARControlProtocol"
- "ARDaemon"
- "ARDaemonConfiguration"
- "ARDaemonControl"
- "ARDaemonMetrics"
- "ARDaemonService"
- "ARDaemonServiceBaseProtocol"
- "ARDaemonServiceDataSource"
- "ARDaemonServiceDelegate"
- "ARDaemonServiceListener"
- "ARDaemonServiceListenerDelegate"
- "ARExecutionManager"
- "ARGeoTrackingTechniqueService"
- "ARInProcessDaemonConfiguration"
- "ARLocalDaemon"
- "ARLocationSensorService"
- "ARLoggingFullDescription"
- "ARMainDaemonConfiguration"
- "ARMemoryPressureMonitor"
- "ARMemoryPressureMonitorDelegate"
- "ARNamedService"
- "ARRemoteGeoTrackingTechniqueService"
- "ARRemoteLocationSensorService"
- "ARRemoteSensorClient"
- "ARRemoteSensorService"
- "ARRemoteTechniqueClient"
- "ARRemoteTechniqueService"
- "ARSensorDelegate"
- "ARSensorService"
- "ARServer"
- "ARServerStatusLogging"
- "ARServiceType"
- "ARServiceUpdateParameters"
- "ARTechniqueDelegate"
- "ARTechniqueService"
- "ARWatchdogMonitor"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8#16i24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16#24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "Error: %{public}@ <%p>: Failed to create control."
- "NSObject"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "Server: %@\n"
- "T#,R"
- "T#,R,N"
- "T@\"<ARControlListenerDelegate>\",W,N,V_delegate"
- "T@\"<ARDaemonServiceDataSource>\",W,N"
- "T@\"<ARDaemonServiceDataSource>\",W,N,V_dataSource"
- "T@\"<ARDaemonServiceDelegate>\",W,N"
- "T@\"<ARDaemonServiceDelegate>\",W,N,V_delegate"
- "T@\"<ARDaemonServiceListenerDelegate>\",R,W,N,V_delegate"
- "T@\"<ARMemoryPressureMonitorDelegate>\",W,N,V_delegate"
- "T@\"<ARRemoteSensorClient>\",&,N,V_clientProxy"
- "T@\"<ARRemoteServiceBaseProtocol>\",R,V_clientService"
- "T@\"<ARRemoteTechniqueClient>\",&,N,V_clientProxy"
- "T@\"<ARSensor>\",&,N,V_sensor"
- "T@\"<ARServerStatusLogging>\",W,N,V_statusLogger"
- "T@\"ARDaemonService\",&,V_serviceBeingRemoved"
- "T@\"ARDaemonServiceListener\",R,N,V_listener"
- "T@\"ARRemoteService\",&,V_remoteService"
- "T@\"ARServer\",R,N,V_server"
- "T@\"ARServer\",W,N,V_server"
- "T@\"ARTechnique\",&,N,V_technique"
- "T@\"ARUserProfile\",&,N,V_userProfile"
- "T@\"NSArray\",&,V_servicesBeingAdded"
- "T@\"NSArray\",R,N,V_runningRemoteServices"
- "T@\"NSDate\",&,V_lastDonTime"
- "T@\"NSObject<OS_channel_rt>\",&,N,V_channel"
- "T@\"NSObject<OS_channel_rt>\",&,V_dispatchChannel"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_clientBundleIdentifier"
- "T@\"NSString\",R,N,V_clientProcessName"
- "T@\"NSXPCConnection\",&,V_connection"
- "T@\"NSXPCListenerEndpoint\",R"
- "TB,N,GisActive"
- "TB,N,GisActive,V_active"
- "TB,N,GisDryRun,V_dryRun"
- "TB,R,N"
- "TB,R,N,V_isReplay"
- "TB,V_isKeybagUnlocked"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_state"
- "Ti,R,N"
- "Ti,R,N,V_clientProcessIdentifier"
- "Tq,R,N"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_active"
- "_activeServiceCountPerClient"
- "_addServiceForClient:serviceName:"
- "_addServices:"
- "_allServicesUsedPerClient"
- "_authorized"
- "_batchedServices"
- "_batchedServicesConfiguredSemaphore"
- "_batchedServicesLock"
- "_channel"
- "_clientBundleIdentifier"
- "_clientProcessIdentifier"
- "_clientProcessName"
- "_clientProxy"
- "_clientService"
- "_commonInitWithProcessName:processIdentifier:bundleIdentifier:"
- "_concurrentConnectionTargetQueue"
- "_configuration"
- "_configureServiceForExecution:"
- "_connection"
- "_controlClass"
- "_controlListener"
- "_createLocalServices"
- "_daemonConfiguration"
- "_daemonServiceActivity"
- "_dataAccessAllowed"
- "_dataSource"
- "_delegate"
- "_dispatchChannel"
- "_dryRun"
- "_fullDescription"
- "_getActiveServiceCountPerClient"
- "_getAllServicesUsedPerClient"
- "_getPeakMemoryUsageInMegabytes"
- "_heartbeat"
- "_heartbeatTimer"
- "_hidFocused"
- "_initCommon:"
- "_isInProcess"
- "_isKeybagUnlocked"
- "_isReplay"
- "_lastDaemonHeartbeatEventReportedTimestamp"
- "_lastDonTime"
- "_lastProcessedDeviceOrientationData"
- "_lastProcessedLocationData"
- "_listener"
- "_listenerQueue"
- "_logDaemonStatus"
- "_memoryPressureEventSource"
- "_memoryPressureMonitor"
- "_numServicesToBatchCommit"
- "_peakMemoryUsageInMegabytes"
- "_peerServicesOfService:"
- "_remoteService"
- "_removeService:"
- "_removeServiceForClient:serviceName:"
- "_removeServiceFromServicesByClass:"
- "_reportCoreAnalyticsDaemonEventWithServiceName:clientBundleIdentifier:isServiceRemoved:isDisconnectingClient:"
- "_reportDaemonHeartbeatForSessionUUID:daemonUpTimeExcludingSleepMinutes:daemonUpTimeIncludingSleepMinutes:systemUpTimeMinutes:memoryFootprintInBytes:"
- "_reportingQueue"
- "_runningDaemons"
- "_runningRemoteServices"
- "_sensor"
- "_server"
- "_serviceBeingRemoved"
- "_serviceClasses"
- "_serviceQueue"
- "_services"
- "_servicesBeingAdded"
- "_servicesByClass"
- "_servicesByPID"
- "_servicesLock"
- "_sessionUUID"
- "_setQueue:"
- "_setupLiteHUDIntegrator"
- "_setupUserProfile"
- "_shortenedServiceNameForLogging"
- "_shouldAddService:forPID:"
- "_spawnTime"
- "_startService"
- "_state"
- "_statusLogger"
- "_technique"
- "_transaction"
- "_updateAlgorithmConfigurationWithServices:"
- "_updateServicesByPID"
- "_updateWithServices:error:"
- "_userProfile"
- "_xpcListeners"
- "active"
- "addEntriesFromDictionary:"
- "addObject:"
- "addPointer:"
- "addQueue:hangPolicy:"
- "addServiceByName:serviceClass:"
- "addServiceWithQueueByName:serviceClass:"
- "allKeys"
- "allObjects"
- "altitude"
- "anonymousListener"
- "appendFormat:"
- "ar_booleanValueForEntitlement:"
- "ar_compactZeroedWeakPointers"
- "ar_entitlementsArray"
- "ar_firstObjectPassingTest:"
- "ar_hasPrivateAREntitlement:"
- "ar_hoursMinutesSecondsWithTimeInterval:"
- "ar_map:"
- "ar_processBundleIdentifier"
- "ar_processName"
- "ar_remoteProcessIdentifier"
- "ar_timestampWithDate:"
- "ar_valueForEntitlement:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "auditToken"
- "autorelease"
- "beginDispatchChannelCreation"
- "beginRTChannelCreation"
- "boolValue"
- "bundleIdentifier"
- "captureBehavior"
- "captureBehaviorWithReply:"
- "caseInsensitiveCompare:"
- "channel"
- "channelDataSize"
- "class"
- "clientBundleIdentifier"
- "clientProcessIdentifier"
- "clientProcessName"
- "clientProxy"
- "clientService"
- "commitServices:"
- "compare:"
- "componentsJoinedByString:"
- "configureForReplay"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "controlClass"
- "controlInterface"
- "controlProxyInterface"
- "coordinate"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAnonymousListenerDaemon"
- "createAnonymousListenerDaemonWithReplayURL:deterministic:replayDelegate:"
- "createAnonymousListenerDaemonWithReplayURL:replayEnableTelemetry:deterministic:replayDelegate:isDryRun:"
- "createDispatchChannelWithRequest:completion:"
- "createRTChannelWithRequest:completion:"
- "createService:"
- "currentLocation"
- "currentLocationWithReply:"
- "d"
- "daemonServiceInterface"
- "dataSource"
- "dataWithBytes:length:"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "decimalNumberByAdding:"
- "decimalNumberBySubtracting:"
- "defaultProfile"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didDiscoverControl:"
- "didDiscoverService:"
- "dispatchChannel"
- "dispatchChannelDataSize"
- "dryRun"
- "endpoint"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "firstObject"
- "fullDescriptionWithWaitEndOfTransition:"
- "getLocationFromWorldPosition:error:"
- "getLocationFromWorldPosition:reply:"
- "getStatusDictionaryWithReply:"
- "getStatusDictionaryWithWaitEndOfTransition:reply:"
- "getStatusWithVerboseOutput:reply:"
- "getStatusWithVerboseOutput:waitForEndOfTransaction:reply:"
- "hasLibraryDirectoryReadWriteAccess"
- "hash"
- "heading"
- "i"
- "i16@0:8"
- "indexesOfObjectsPassingTest:"
- "init"
- "initAsLocalService"
- "initWithAuditToken:"
- "initWithBundleIdentifier:"
- "initWithConfiguration:spawnTime:watchdogMonitor:"
- "initWithConfiguration:spawnTime:watchdogMonitor:graphScheduler:replayDelegate:"
- "initWithConnection:"
- "initWithConnection:exportedInterface:remoteObjectInterface:"
- "initWithDaemonConfiguration:spawnTime:sessionUUID:watchdogMonitor:executionManager:"
- "initWithDelegate:controlClass:isInProcess:"
- "initWithDelegate:watchdogMonitor:isInProcess:"
- "initWithDelegate:watchdogMonitor:isInProcess:ignoredServiceNames:"
- "initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:"
- "initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:"
- "initWithMachServiceName:"
- "initWithNSXPCConnection:"
- "initWithRemoteService:"
- "intValue"
- "integerForKey:"
- "interruptionHandler"
- "invalidate"
- "invalidateClient"
- "invalidationHandler"
- "isActive"
- "isActiveWithReply:"
- "isDryRun"
- "isEqual:"
- "isEqualToString:"
- "isInProcess"
- "isKeybagUnlocked"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isReplay"
- "isSecure"
- "isSupported"
- "lastDonTime"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "listenerEndPointForServiceNamed:"
- "listenerForServiceNamed:"
- "localizationResult"
- "location"
- "logStatusUpdateWithDictionary:forServerObject:andProcessName:"
- "lookupAltitudeAtCoordinate:completionHandler:"
- "mainBundle"
- "maximumConcurrentServicesPerClient"
- "memoryPressureMonitor:didUpdateProcessMemoryPressureCondition:"
- "memoryPressureMonitor:didUpdateSystemMemoryPressureCondition:"
- "minimumChannelQueueSize"
- "mutableCopy"
- "numberOfActiveConnectionsForService:"
- "numberOfActiveConnectionsWithReply:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "one"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "posteriorVisualLocalizationCallInterval"
- "posteriorVisualLocalizationCallIntervalWithReply:"
- "prepare:"
- "printInfo"
- "processData:"
- "processData:reply:"
- "processDeviceOrientationData:"
- "processIdentifier"
- "processInfo"
- "processLocationData:"
- "processName"
- "providedDataTypes"
- "providedDataTypesWithReply:"
- "q16@0:8"
- "q24@0:8@\"<ARServiceType>\"16"
- "q24@0:8@16"
- "r"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remoteService"
- "remoteServiceClass"
- "remoteServiceInterface"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "reportCoreAnalyticsDaemonEventWithServiceName:clientBundleIdentifier:isServiceRemoved:isDisconnectingClient:"
- "reportDaemonHeartbeatForSessionUUID:daemonUpTimeExcludingSleepMinutes:daemonUpTimeIncludingSleepMinutes:systemUpTimeMinutes:memoryFootprintInBytes:"
- "reportMemoryFootprintInBytes:"
- "reportServiceAddedWithName:clientBundleIdentifier:"
- "reportServiceRemovedWithName:clientBundleIdentifier:"
- "requestResultDataAtTimestamp:context:"
- "requiredSensorDataTypes"
- "requiredSensorDataTypesWithReply:"
- "requiredTimeInterval"
- "requiredTimeIntervalWithReply:"
- "requiresChannelSetup"
- "requiresDispatchChannelSetup"
- "respondsToSelector:"
- "resultDataClasses"
- "resultDataClassesWithReply:"
- "resume"
- "retain"
- "retainCount"
- "runningRemoteServices"
- "self"
- "sensor"
- "sensor:didFailWithError:"
- "sensor:didOutputSensorData:"
- "sensorDidFailWithError:"
- "sensorDidOutputSensorData:"
- "sensorDidPause"
- "sensorDidPause:"
- "sensorDidRestart"
- "sensorDidRestart:"
- "sensorDidStart"
- "sensorDidStart:"
- "server"
- "service:peerServiceOfType:"
- "serviceBeingRemoved"
- "serviceConfiguredWithError:"
- "serviceDidInterrupt:"
- "serviceDidInvalidate:"
- "serviceName"
- "serviceQueue"
- "serviceTypeRequiresAlgorithmObservationWhileSuspended"
- "serviceTypeRequiresDataAccessMonitoring"
- "servicesBeingAdded"
- "servicesIsEmpty"
- "setActive:"
- "setChannel:"
- "setClientProxy:"
- "setConnection:"
- "setCurrentMemoryFootprintAsPeak"
- "setDataSource:"
- "setDelegate:"
- "setDispatchChannel:"
- "setDryRun:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsKeybagUnlocked:"
- "setLastDonTime:"
- "setLocalAnonymousListenerDaemon:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPosteriorVisualLocalizationCallInterval:"
- "setRemoteObjectInterface:"
- "setRemoteService:"
- "setSensor:"
- "setServer:"
- "setServiceBeingRemoved:"
- "setServices:"
- "setServicesBeingAdded:"
- "setStatusLogger:"
- "setSupportEnablementOptions:"
- "setTechnique:"
- "setUserProfile:"
- "setValue:forKey:"
- "setVisualLocalizationCallInterval:"
- "setVisualLocalizationCallIntervalTimeThreshold:"
- "setVisualLocalizationUpdatesRequested:"
- "setupCompleteForRTChannel"
- "setupCompleteForRTDispatchChannel"
- "sharedDaemonMetrics"
- "shortenedServiceNameForLogging"
- "shutdown"
- "sortedArrayUsingSelector:"
- "start"
- "startService:"
- "startWithServices:"
- "startup"
- "state"
- "statusDictionaryWithWaitEndOfTransition:"
- "statusLogger"
- "statusStringWithWaitEndOfTransition:"
- "stop"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "superclass"
- "supportEnablementOptions"
- "supportEnablementOptionsWithReply:"
- "supportsWatchdog"
- "syncServiceWithTimeout:callback:"
- "technique"
- "technique:didFailWithError:"
- "technique:didOutputResultData:timestamp:context:"
- "techniqueDidFailWithError:"
- "techniqueDidOutputResultData:timestamp:context:"
- "timeSinceSnapshot:"
- "timestamp"
- "upTime"
- "upTimeIncludingSleep"
- "upTimeIncludingSleepAndDriftCorrection"
- "updateARSessionState:"
- "updateEstimationFromVIOPose:imageData:"
- "updateFromDeviceOrientationData:"
- "updateFromLocationData:"
- "updateFromVisualLocalizationResult:"
- "updateStatus:"
- "userProfile"
- "v16@0:8"
- "v16@?0@\"<ARDaemonServiceBaseProtocol>\"8"
- "v20@0:8B16"
- "v24@0:8@\"<ARDaemonServiceDataSource>\"16"
- "v24@0:8@\"<ARDaemonServiceDelegate>\"16"
- "v24@0:8@\"<ARSensor>\"16"
- "v24@0:8@\"<ARSensorData>\"16"
- "v24@0:8@\"<ARServiceType>\"16"
- "v24@0:8@\"ARDaemonControl\"16"
- "v24@0:8@\"ARDaemonService\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"ARLocationData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?d@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSDictionary\">20"
- "v28@0:8B16@?<v@?@\"NSString\">20"
- "v32@0:8@\"<ARData>\"16@?<v@?@\"<ARData>\"@\"NSError\">24"
- "v32@0:8@\"<ARSensor>\"16@\"<ARSensorData>\"24"
- "v32@0:8@\"<ARSensor>\"16@\"NSError\"24"
- "v32@0:8@\"ARMemoryPressureMonitor\"16q24"
- "v32@0:8@\"ARTechnique\"16@\"NSError\"24"
- "v32@0:8@\"ARWorldTrackingPoseData\"16@\"ARImageData\"24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v32@0:8B16B20@?24"
- "v32@0:8B16B20@?<v@?@\"NSString\">24"
- "v32@0:8d16@\"<ARResultDataContext>\"24"
- "v32@0:8d16@24"
- "v36@0:8@16i24@28"
- "v40@0:8@\"NSArray\"16d24@\"<ARResultDataContext>\"32"
- "v40@0:8@16@24B32B36"
- "v40@0:8@16d24@32"
- "v40@0:8{CLLocationCoordinate2D=dd}16@?32"
- "v40@0:8{CLLocationCoordinate2D=dd}16@?<v@?@\"_CLLocationGroundAltitude\">32"
- "v48@0:8@\"ARTechnique\"16@\"NSArray\"24d32@\"<ARResultDataContext>\"40"
- "v48@0:8@16@24d32@40"
- "v56@0:8@16Q24Q32Q40Q48"
- "visualLocalizationCallInterval"
- "visualLocalizationCallIntervalTimeThreshold"
- "visualLocalizationCallIntervalTimeThresholdWithReply:"
- "visualLocalizationCallIntervalWithReply:"
- "visualLocalizationUpdatesRequested"
- "visualLocalizationUpdatesRequestedWithReply:"
- "weakObjectsPointerArray"
- "wrapperWithDictionary:"
- "zero"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
