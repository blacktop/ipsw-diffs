## ARKitDaemon

> `/System/Library/PrivateFrameworks/ARKitDaemon.framework/ARKitDaemon`

```diff

-631.102.1.0.0
-  __TEXT.__text: 0xeb7c
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_methlist: 0x14dc
-  __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x1c16
-  __TEXT.__cstring: 0x9e2
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__unwind_info: 0x568
-  __TEXT.__objc_classname: 0x462
-  __TEXT.__objc_methname: 0x2f1e
-  __TEXT.__objc_methtype: 0xc85
-  __TEXT.__objc_stubs: 0x2080
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x420
-  __DATA_CONST.__objc_classlist: 0xd0
+735.0.1.0.0
+  __TEXT.__text: 0xe1a0
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x1294
+  __TEXT.__const: 0x90
+  __TEXT.__oslogstring: 0x2189
+  __TEXT.__cstring: 0x73f
+  __TEXT.__gcc_except_tab: 0x65c
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__objc_classname: 0x390
+  __TEXT.__objc_methname: 0x2af8
+  __TEXT.__objc_methtype: 0xc41
+  __TEXT.__objc_stubs: 0x1e80
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb60
+  __DATA_CONST.__objc_selrefs: 0xa78
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3d8
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x9c0
-  __AUTH_CONST.__objc_const: 0x5458
+  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x4450
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x170
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
   - /System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
   - /System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit

   - /System/Library/PrivateFrameworks/CoreLocationReplay.framework/CoreLocationReplay
   - /System/Library/PrivateFrameworks/CoreNavigation.framework/CoreNavigation
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
-  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libc++.1.dylib
+  - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E486C82-6E8D-3746-8D25-5FFC41615E00
-  Functions: 408
-  Symbols:   1900
-  CStrings:  995
+  UUID: C35CD3AB-B3EE-39C1-9F94-18EC6A4B0BD9
+  Functions: 358
+  Symbols:   1713
+  CStrings:  889
 
Symbols:
+ -[ARControlListener initWithDelegate:controlClass:isInProcess:]
+ -[ARDaemon isReplay]
+ -[ARDaemonControl setStatusLogger:]
+ -[ARDaemonControl statusLogger]
+ -[ARDaemonService beginDispatchChannelCreation]
+ -[ARDaemonService beginDispatchChannelCreation].cold.1
+ -[ARDaemonService beginRTChannelCreation]
+ -[ARDaemonService beginRTChannelCreation].cold.1
+ -[ARDaemonService channelDataSize]
+ -[ARDaemonService channel]
+ -[ARDaemonService dispatchChannelDataSize]
+ -[ARDaemonService dispatchChannel]
+ -[ARDaemonService invalidateClient]
+ -[ARDaemonService isDataAccessAllowed]
+ -[ARDaemonService isDryRun]
+ -[ARDaemonService isHidFocused]
+ -[ARDaemonService minimumChannelQueueSize]
+ -[ARDaemonService requiresChannelSetup]
+ -[ARDaemonService requiresDispatchChannelSetup]
+ -[ARDaemonService setChannel:]
+ -[ARDaemonService setDispatchChannel:]
+ -[ARDaemonService setDryRun:]
+ -[ARDaemonService setupCompleteForRTChannel]
+ -[ARDaemonService setupCompleteForRTDispatchChannel]
+ -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:]
+ -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:ignoredServiceNames:]
+ -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:]
+ -[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:]
+ -[ARServer _updateAlgorithmConfigurationWithServices:]
+ -[NSXPCConnection(ARAdditions) ar_remoteProcessIdentifier]
+ -[NSXPCConnection(ARAdditions) ar_valueForEntitlement:]
+ -[NSXPCConnection(ARAdditions) ar_valueForEntitlement:].cold.1
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table5
+ GCC_except_table8
+ _CFErrorCopyDescription
+ _CFRelease
+ _OBJC_CLASS_$_ARXPCDictionaryWrapper
+ _OBJC_IVAR_$_ARDaemon._isReplay
+ _OBJC_IVAR_$_ARDaemonControl._statusLogger
+ _OBJC_IVAR_$_ARDaemonService._channel
+ _OBJC_IVAR_$_ARDaemonService._dataAccessAllowed
+ _OBJC_IVAR_$_ARDaemonService._dispatchChannel
+ _OBJC_IVAR_$_ARDaemonService._dryRun
+ _OBJC_IVAR_$_ARDaemonService._hidFocused
+ _OBJC_IVAR_$_ARDaemonServiceListener._isInProcess
+ _OUTLINED_FUNCTION_0
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _SecTaskCreateWithAuditToken
+ __OBJC_$_PROP_LIST_ARLocalDaemon
+ __OBJC_$_PROTOCOL_CLASS_METHODS_ARLocalDaemon
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARLocalDaemon
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARServerStatusLogging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARLocalDaemon
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARServerStatusLogging
+ __OBJC_$_PROTOCOL_REFS_ARLocalDaemon
+ __OBJC_$_PROTOCOL_REFS_ARServerStatusLogging
+ __OBJC_LABEL_PROTOCOL_$_ARLocalDaemon
+ __OBJC_LABEL_PROTOCOL_$_ARServerStatusLogging
+ __OBJC_PROTOCOL_$_ARLocalDaemon
+ __OBJC_PROTOCOL_$_ARServerStatusLogging
+ ___113-[ARDaemonServiceListener initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:]_block_invoke
+ ___41-[ARDaemonService beginRTChannelCreation]_block_invoke
+ ___41-[ARDaemonService beginRTChannelCreation]_block_invoke.23
+ ___41-[ARDaemonService beginRTChannelCreation]_block_invoke.23.cold.1
+ ___41-[ARDaemonService beginRTChannelCreation]_block_invoke.23.cold.2
+ ___41-[ARDaemonService beginRTChannelCreation]_block_invoke.cold.1
+ ___42-[ARServer _configureServiceForExecution:]_block_invoke.103
+ ___42-[ARServer _configureServiceForExecution:]_block_invoke.104
+ ___47-[ARDaemonService beginDispatchChannelCreation]_block_invoke
+ ___47-[ARDaemonService beginDispatchChannelCreation]_block_invoke.26
+ ___47-[ARDaemonService beginDispatchChannelCreation]_block_invoke.26.cold.1
+ ___47-[ARDaemonService beginDispatchChannelCreation]_block_invoke.26.cold.2
+ ___47-[ARDaemonService beginDispatchChannelCreation]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e32_v16?0"ARXPCDictionaryWrapper"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.109
+ ___block_literal_global.140
+ ___block_literal_global.144
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.207
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.270
+ ___block_literal_global.86
+ _channel_create_asymmetric_endpoint_and_request
+ _channel_rt_close
+ _channel_rt_create_from_reply
+ _getpid
+ _kARDispatchChannelMessageSizeKey
+ _kCFAllocatorDefault
+ _objc_msgSend$_updateAlgorithmConfigurationWithServices:
+ _objc_msgSend$ar_remoteProcessIdentifier
+ _objc_msgSend$ar_valueForEntitlement:
+ _objc_msgSend$auditToken
+ _objc_msgSend$channel
+ _objc_msgSend$channelDataSize
+ _objc_msgSend$createDispatchChannelWithRequest:completion:
+ _objc_msgSend$createRTChannelWithRequest:completion:
+ _objc_msgSend$dictionary
+ _objc_msgSend$dispatchChannel
+ _objc_msgSend$dispatchChannelDataSize
+ _objc_msgSend$initWithDelegate:controlClass:isInProcess:
+ _objc_msgSend$initWithDelegate:watchdogMonitor:isInProcess:
+ _objc_msgSend$initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:
+ _objc_msgSend$minimumChannelQueueSize
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$setChannel:
+ _objc_msgSend$setDispatchChannel:
+ _objc_msgSend$setStatusLogger:
+ _objc_msgSend$setupCompleteForRTChannel
+ _objc_msgSend$setupCompleteForRTDispatchChannel
+ _objc_msgSend$statusLogger
+ _objc_msgSend$wrapperWithDictionary:
+ _os_transaction_create
+ _vm_page_size
+ _xpc_dictionary_create
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_set_uint64
- +[ARDaemon localAnonymousListenerDaemon]
- +[ARObjectTrackingDaemonControl serviceName]
- +[ARProcessMonitor processIsDaemon:error:]
- +[ARProcessMonitor processIsDaemon:error:].cold.1
- +[ARProcessMonitor processIsDaemon:error:].cold.2
- +[ARSystemTimeSnapshot timeSinceSnapshot:]
- +[ARUserProfile defaultProfile]
- +[ARUserProfile isGuestProfileEnabled]
- -[ARControlListener initWithDelegate:daemonConfiguration:]
- -[ARDaemonReplayBlockDelegate .cxx_destruct]
- -[ARDaemonReplayBlockDelegate replayDidFailWithError:]
- -[ARDaemonReplayBlockDelegate replayDidStartWithReplayTime:]
- -[ARDaemonReplayBlockDelegate replayDidStop]
- -[ARDaemonReplayBlockDelegate replayDidUpdateResourceWithKey:atTime:]
- -[ARDaemonReplayBlockDelegate replayFailedBlock]
- -[ARDaemonReplayBlockDelegate replayStartedBlock]
- -[ARDaemonReplayBlockDelegate replayStoppedBlock]
- -[ARDaemonReplayBlockDelegate replayUpdatedBlock]
- -[ARDaemonReplayBlockDelegate setReplayFailedBlock:]
- -[ARDaemonReplayBlockDelegate setReplayStartedBlock:]
- -[ARDaemonReplayBlockDelegate setReplayStoppedBlock:]
- -[ARDaemonReplayBlockDelegate setReplayUpdatedBlock:]
- -[ARDaemonService isImmersive]
- -[ARDaemonService resume]
- -[ARDaemonService setImmersive:]
- -[ARDaemonService suspend]
- -[ARDaemonServiceListener initWithDelegate:daemonConfiguration:watchdogMonitor:]
- -[ARJasperData dataBuffer]
- -[ARJasperData dealloc]
- -[ARJasperData initWithBuffer:timestamp:]
- -[ARJasperData setDataBuffer:]
- -[ARJasperData setTimestamp:]
- -[ARJasperData timestamp]
- -[ARObjectTrackingDaemonConfiguration controlClass]
- -[ARObjectTrackingDaemonConfiguration hasLibraryDirectoryReadWriteAccess]
- -[ARObjectTrackingDaemonConfiguration isInProcess]
- -[ARObjectTrackingDaemonConfiguration supportsWatchdog]
- -[ARProcessMonitor .cxx_destruct]
- -[ARProcessMonitor dealloc]
- -[ARProcessMonitor delegate]
- -[ARProcessMonitor handleStateUpdate:]
- -[ARProcessMonitor init]
- -[ARProcessMonitor setDelegate:]
- -[ARProcessMonitor startMonitoringImmersiveStatusForPID:withServices:]
- -[ARProcessMonitor startMonitoringPID:]
- -[ARProcessMonitor startMonitoringPID:].cold.1
- -[ARProcessMonitor stopMonitoringImmersiveStatusForPID:]
- -[ARProcessMonitor stopMonitoringPID:]
- -[ARProcessMonitor updateProcessMonitorConfig:withPredicates:]
- -[ARProcessMonitorStateUpdate .cxx_destruct]
- -[ARProcessMonitorStateUpdate debugState]
- -[ARProcessMonitorStateUpdate description]
- -[ARProcessMonitorStateUpdate initWithARProcessTaskState:]
- -[ARProcessMonitorStateUpdate initWithRBSProcessStateUpdate:]
- -[ARProcessMonitorStateUpdate isVisible]
- -[ARProcessMonitorStateUpdate name]
- -[ARProcessMonitorStateUpdate pid]
- -[ARProcessMonitorStateUpdate taskState]
- -[ARServer currentConfiguration]
- -[ARServer daemonServiceForServiceNamed:]
- -[ARServer resume]
- -[ARServer setCurrentConfiguration:]
- -[ARServer suspend]
- -[ARServer updateAlgorithmConfigurationWithService:]
- -[ARServer updateAlgorithmConfigurationWithServices:]
- -[ARSystemTimeSnapshot description]
- -[ARSystemTimeSnapshot initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:]
- -[ARSystemTimeSnapshot init]
- -[ARSystemTimeSnapshot timeSinceSnapshot:]
- -[ARSystemTimeSnapshot upTimeIncludingSleepAndDriftCorrection]
- -[ARSystemTimeSnapshot upTimeIncludingSleep]
- -[ARSystemTimeSnapshot upTime]
- -[ARUserProfile .cxx_destruct]
- -[ARUserProfile description]
- -[ARUserProfile identifier]
- -[ARUserProfile initWithIdentifier:type:]
- -[ARUserProfile isEqual:]
- -[ARUserProfile type]
- GCC_except_table10
- GCC_except_table13
- GCC_except_table20
- GCC_except_table24
- GCC_except_table27
- GCC_except_table3
- GCC_except_table40
- GCC_except_table42
- GCC_except_table43
- GCC_except_table6
- _ARGetSystemUpTime
- _ARGetSystemUpTimeIncludingSleep
- _ARGetSystemUpTimeIncludingSleepAndDriftCorrection
- _ARServiceNameObjectTrackingControl
- _CVBufferRelease
- _CVBufferRetain
- _NSStringFromARProcessDebugState
- _NSStringFromARProcessImmersivenessLevel
- _NSStringFromARProcessTaskState
- _OBJC_CLASS_$_ARDaemonReplayBlockDelegate
- _OBJC_CLASS_$_ARJasperData
- _OBJC_CLASS_$_ARObjectTrackingDaemonConfiguration
- _OBJC_CLASS_$_ARObjectTrackingDaemonControl
- _OBJC_CLASS_$_ARProcessMonitor
- _OBJC_CLASS_$_ARProcessMonitorStateUpdate
- _OBJC_CLASS_$_ARReplayGraphScheduler
- _OBJC_CLASS_$_RBSProcessHandle
- _OBJC_CLASS_$_RBSProcessIdentifier
- _OBJC_CLASS_$_RBSProcessMonitor
- _OBJC_CLASS_$_RBSProcessPredicate
- _OBJC_CLASS_$_RBSProcessStateDescriptor
- _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayFailedBlock
- _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayStartedBlock
- _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayStoppedBlock
- _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayUpdatedBlock
- _OBJC_IVAR_$_ARDaemonService._immersive
- _OBJC_IVAR_$_ARDaemonServiceListener._daemonConfiguration
- _OBJC_IVAR_$_ARJasperData._dataBuffer
- _OBJC_IVAR_$_ARJasperData._timestamp
- _OBJC_IVAR_$_ARProcessMonitor._delegate
- _OBJC_IVAR_$_ARProcessMonitor._pidsLock
- _OBJC_IVAR_$_ARProcessMonitor._pidsToObserve
- _OBJC_IVAR_$_ARProcessMonitor._processMonitor
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._debugState
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._isVisible
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._name
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._pid
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._taskState
- _OBJC_IVAR_$_ARProcessMonitorStateUpdate._update
- _OBJC_IVAR_$_ARServer._currentConfiguration
- _OBJC_IVAR_$_ARServer._latestTaskErrorMap
- _OBJC_IVAR_$_ARSystemTimeSnapshot._upTime
- _OBJC_IVAR_$_ARSystemTimeSnapshot._upTimeIncludingSleep
- _OBJC_IVAR_$_ARSystemTimeSnapshot._upTimeIncludingSleepAndDriftCorrection
- _OBJC_IVAR_$_ARUserProfile._identifier
- _OBJC_IVAR_$_ARUserProfile._type
- _OBJC_METACLASS_$_ARDaemonReplayBlockDelegate
- _OBJC_METACLASS_$_ARJasperData
- _OBJC_METACLASS_$_ARObjectTrackingDaemonConfiguration
- _OBJC_METACLASS_$_ARObjectTrackingDaemonControl
- _OBJC_METACLASS_$_ARProcessMonitor
- _OBJC_METACLASS_$_ARProcessMonitorStateUpdate
- _OBJC_METACLASS_$_ARReplayGraphScheduler
- _OBJC_METACLASS_$_ARSystemTimeSnapshot
- _OBJC_METACLASS_$_ARUserProfile
- __ARLogProcessMonitor
- __ARLogProcessMonitor.cold.1
- __ARLogProcessMonitor.logObj
- __ARLogProcessMonitor.onceToken
- __OBJC_$_CLASS_METHODS_ARObjectTrackingDaemonControl
- __OBJC_$_CLASS_METHODS_ARProcessMonitor
- __OBJC_$_CLASS_METHODS_ARSystemTimeSnapshot
- __OBJC_$_CLASS_METHODS_ARUserProfile
- __OBJC_$_CLASS_PROP_LIST_ARDaemon
- __OBJC_$_INSTANCE_METHODS_ARDaemonReplayBlockDelegate
- __OBJC_$_INSTANCE_METHODS_ARJasperData
- __OBJC_$_INSTANCE_METHODS_ARObjectTrackingDaemonConfiguration
- __OBJC_$_INSTANCE_METHODS_ARProcessMonitor
- __OBJC_$_INSTANCE_METHODS_ARProcessMonitorStateUpdate
- __OBJC_$_INSTANCE_METHODS_ARSystemTimeSnapshot
- __OBJC_$_INSTANCE_METHODS_ARUserProfile
- __OBJC_$_INSTANCE_VARIABLES_ARDaemonReplayBlockDelegate
- __OBJC_$_INSTANCE_VARIABLES_ARJasperData
- __OBJC_$_INSTANCE_VARIABLES_ARProcessMonitor
- __OBJC_$_INSTANCE_VARIABLES_ARProcessMonitorStateUpdate
- __OBJC_$_INSTANCE_VARIABLES_ARSystemTimeSnapshot
- __OBJC_$_INSTANCE_VARIABLES_ARUserProfile
- __OBJC_$_PROP_LIST_ARDaemonReplayBlockDelegate
- __OBJC_$_PROP_LIST_ARJasperData
- __OBJC_$_PROP_LIST_ARObjectTrackingDaemonConfiguration
- __OBJC_$_PROP_LIST_ARProcessMonitor
- __OBJC_$_PROP_LIST_ARProcessMonitorStateUpdate
- __OBJC_$_PROP_LIST_ARSystemTimeSnapshot
- __OBJC_$_PROP_LIST_ARUserProfile
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARDaemonReplayDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_ARDaemonReplayDelegate
- __OBJC_$_PROTOCOL_REFS_ARDaemonReplayDelegate
- __OBJC_$_PROTOCOL_REFS_ARData
- __OBJC_CLASS_PROTOCOLS_$_ARDaemonReplayBlockDelegate
- __OBJC_CLASS_PROTOCOLS_$_ARJasperData
- __OBJC_CLASS_PROTOCOLS_$_ARObjectTrackingDaemonConfiguration
- __OBJC_CLASS_RO_$_ARDaemonReplayBlockDelegate
- __OBJC_CLASS_RO_$_ARJasperData
- __OBJC_CLASS_RO_$_ARObjectTrackingDaemonConfiguration
- __OBJC_CLASS_RO_$_ARObjectTrackingDaemonControl
- __OBJC_CLASS_RO_$_ARProcessMonitor
- __OBJC_CLASS_RO_$_ARProcessMonitorStateUpdate
- __OBJC_CLASS_RO_$_ARReplayGraphScheduler
- __OBJC_CLASS_RO_$_ARSystemTimeSnapshot
- __OBJC_CLASS_RO_$_ARUserProfile
- __OBJC_LABEL_PROTOCOL_$_ARDaemonReplayDelegate
- __OBJC_LABEL_PROTOCOL_$_ARData
- __OBJC_METACLASS_RO_$_ARDaemonReplayBlockDelegate
- __OBJC_METACLASS_RO_$_ARJasperData
- __OBJC_METACLASS_RO_$_ARObjectTrackingDaemonConfiguration
- __OBJC_METACLASS_RO_$_ARObjectTrackingDaemonControl
- __OBJC_METACLASS_RO_$_ARProcessMonitor
- __OBJC_METACLASS_RO_$_ARProcessMonitorStateUpdate
- __OBJC_METACLASS_RO_$_ARReplayGraphScheduler
- __OBJC_METACLASS_RO_$_ARSystemTimeSnapshot
- __OBJC_METACLASS_RO_$_ARUserProfile
- __OBJC_PROTOCOL_$_ARDaemonReplayDelegate
- __OBJC_PROTOCOL_$_ARData
- ___18-[ARServer resume]_block_invoke
- ___19-[ARServer suspend]_block_invoke
- ___24-[ARProcessMonitor init]_block_invoke
- ___38-[ARProcessMonitor stopMonitoringPID:]_block_invoke
- ___39-[ARProcessMonitor startMonitoringPID:]_block_invoke
- ___42-[ARServer _configureServiceForExecution:]_block_invoke.107
- ___42-[ARServer _configureServiceForExecution:]_block_invoke.108
- ___62-[ARProcessMonitor updateProcessMonitorConfig:withPredicates:]_block_invoke
- ___80-[ARDaemonServiceListener initWithDelegate:daemonConfiguration:watchdogMonitor:]_block_invoke
- ____ARLogProcessMonitor_block_invoke
- ___block_descriptor_40_e8_32w_e40_v16?0"<RBSProcessMonitorConfiguring>"8lw32l8
- ___block_descriptor_40_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
- ___block_descriptor_48_e8_32s40w_e40_v16?0"<RBSProcessMonitorConfiguring>"8lw40l8s32l8
- ___block_literal_global.113
- ___block_literal_global.13
- ___block_literal_global.130
- ___block_literal_global.15
- ___block_literal_global.166
- ___block_literal_global.169
- ___block_literal_global.172
- ___block_literal_global.173
- ___block_literal_global.275
- ___block_literal_global.279
- ___block_literal_global.282
- _objc_msgSend$allValues
- _objc_msgSend$debugState
- _objc_msgSend$descriptor
- _objc_msgSend$endowmentNamespaces
- _objc_msgSend$handleForIdentifier:error:
- _objc_msgSend$handleStateUpdate:
- _objc_msgSend$identifierWithPid:
- _objc_msgSend$initWithDelegate:daemonConfiguration:
- _objc_msgSend$initWithDelegate:daemonConfiguration:watchdogMonitor:
- _objc_msgSend$initWithIdentifier:type:
- _objc_msgSend$initWithRBSProcessStateUpdate:
- _objc_msgSend$initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:
- _objc_msgSend$isDaemon
- _objc_msgSend$localAnonymousListenerDaemon
- _objc_msgSend$monitorWithConfiguration:
- _objc_msgSend$name
- _objc_msgSend$pid
- _objc_msgSend$predicateMatchingIdentifier:
- _objc_msgSend$process
- _objc_msgSend$processMonitor:didUpdateState:
- _objc_msgSend$replayFailedBlock
- _objc_msgSend$replayStartedBlock
- _objc_msgSend$replayStoppedBlock
- _objc_msgSend$replayUpdatedBlock
- _objc_msgSend$setDataBuffer:
- _objc_msgSend$setEndowmentNamespaces:
- _objc_msgSend$setPredicates:
- _objc_msgSend$setServiceClass:
- _objc_msgSend$setStateDescriptor:
- _objc_msgSend$setUpdateHandler:
- _objc_msgSend$setValues:
- _objc_msgSend$state
- _objc_msgSend$suspend
- _objc_msgSend$taskState
- _objc_msgSend$updateAlgorithmConfigurationWithService:
- _objc_msgSend$updateAlgorithmConfigurationWithServices:
- _objc_msgSend$updateConfiguration:
- _objc_msgSend$updateProcessMonitorConfig:withPredicates:
- _objc_msgSend$valueForEntitlement:
- _objc_setProperty_nonatomic_copy
CStrings:
+ "%@:%@"
+ "%{public}@ <%p>: Error retrieving entitlements for process %{public}@ (%{public}u): %@"
+ "%{public}@ <%p>: Failed to create RT channel using channel_rt_create_from_reply"
+ "%{public}@ <%p>: Failed to create dispatch channel using channel_rt_create_from_reply"
+ "%{public}@ <%p>: Failed to send request to remote service to create RT channel, aborting."
+ "%{public}@ <%p>: Failed to send request to remote service to create dispatch channel, aborting."
+ "%{public}@ <%p>: Force invalidating client"
+ "%{public}@ <%p>: Received a nil reply from createRTChannelWithRequest, aborting creating a RT channel"
+ "%{public}@ <%p>: Received a nil reply from createRTChannelWithRequest, aborting creating a dispatch channel"
+ "%{public}@ <%p>: Successfully setup RT channel"
+ "%{public}@ <%p>: Successfully setup dispatch channel"
+ "%{public}@ <%p>: Unable to create endpoint using channel_create_endpoint_and_request"
+ "%{public}@: Daemon service deallocated before RT channel creation completed, aborting error handler."
+ "%{public}@: Daemon service deallocated before RT channel creation completed, aborting request completion handler."
+ "%{public}@: Daemon service deallocated before dispatch channel creation completed, aborting error handler."
+ "%{public}@: Daemon service deallocated before dispatch channel creation completed, aborting request completion handler."
+ "@\"<ARServerStatusLogging>\""
+ "@\"NSDictionary\"20@0:8B16"
+ "@\"NSObject<OS_channel_rt>\""
+ "@\"NSString\"20@0:8B16"
+ "@\"NSXPCListenerEndpoint\"24@0:8@\"NSString\"16"
+ "@36@0:8@\"NSURL\"16B24@\"<ARDaemonReplayDelegate>\"28"
+ "@36@0:8@16#24B32"
+ "@36@0:8@16@24B32"
+ "@44@0:8@16@24B32@36"
+ "@52@0:8@16@24B32@36@44"
+ "ARLocalDaemon"
+ "ARServerStatusLogging"
+ "Error: %{public}@ <%p>: Error retrieving entitlements for process %{public}@ (%{public}u): %@"
+ "Error: %{public}@ <%p>: Failed to create RT channel using channel_rt_create_from_reply"
+ "Error: %{public}@ <%p>: Failed to create dispatch channel using channel_rt_create_from_reply"
+ "Error: %{public}@ <%p>: Failed to send request to remote service to create RT channel, aborting."
+ "Error: %{public}@ <%p>: Failed to send request to remote service to create dispatch channel, aborting."
+ "Error: %{public}@ <%p>: Received a nil reply from createRTChannelWithRequest, aborting creating a RT channel"
+ "Error: %{public}@ <%p>: Received a nil reply from createRTChannelWithRequest, aborting creating a dispatch channel"
+ "Error: %{public}@ <%p>: Unable to create endpoint using channel_create_endpoint_and_request"
+ "T@\"<ARServerStatusLogging>\",W,N,V_statusLogger"
+ "T@\"NSObject<OS_channel_rt>\",&,N,V_channel"
+ "T@\"NSObject<OS_channel_rt>\",&,N,V_dispatchChannel"
+ "TB,N,GisDryRun,V_dryRun"
+ "TB,R,N,V_isReplay"
+ "TQ,R,N"
+ "_channel"
+ "_dataAccessAllowed"
+ "_dispatchChannel"
+ "_dryRun"
+ "_hidFocused"
+ "_isInProcess"
+ "_isReplay"
+ "_updateAlgorithmConfigurationWithServices:"
+ "ar_remoteProcessIdentifier"
+ "ar_valueForEntitlement:"
+ "auditToken"
+ "beginDispatchChannelCreation"
+ "beginRTChannelCreation"
+ "channel"
+ "channelDataSize"
+ "createDispatchChannelWithRequest:completion:"
+ "createRTChannelWithRequest:completion:"
+ "dictionary"
+ "dispatchChannel"
+ "dispatchChannelDataSize"
+ "dryRun"
+ "initWithDelegate:controlClass:isInProcess:"
+ "initWithDelegate:watchdogMonitor:isInProcess:"
+ "initWithDelegate:watchdogMonitor:isInProcess:ignoredServiceNames:"
+ "initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:"
+ "initWithDelegate:watchdogMonitor:isInProcess:requiredServiceNames:ignoredServiceNames:"
+ "invalidateClient"
+ "isDryRun"
+ "isReplay"
+ "minimumChannelQueueSize"
+ "r"
+ "remoteObjectProxyWithErrorHandler:"
+ "requiresChannelSetup"
+ "requiresDispatchChannelSetup"
+ "serviceTypeRequiresDataAccessMonitoring"
+ "setChannel:"
+ "setDispatchChannel:"
+ "setDryRun:"
+ "setStatusLogger:"
+ "setupCompleteForRTChannel"
+ "setupCompleteForRTDispatchChannel"
+ "statusLogger"
+ "v16@?0@\"ARXPCDictionaryWrapper\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v24@0:8@\"NSArray\"16"
+ "wrapperWithDictionary:"
- "%{public}@ <%p>: Adding PID to monitor: %d"
- "%{public}@ <%p>: Could not create a process handle for pid %d"
- "%{public}@ <%p>: Could not find a process identifier for pid %d"
- "%{public}@ <%p>: Notifying delegate of update: %@"
- "%{public}@ <%p>: Removing PID to Monitor: %d"
- "%{public}@ <%p>: Resume: %{public}@"
- "%{public}@ <%p>: Resuming services"
- "%{public}@ <%p>: Suspend: %{public}@"
- "%{public}@ <%p>: Suspending services"
- "%{public}@ <%p>: Updating process monitor with new predicates"
- "%{public}@ <%p>: Warning: Removing PID to Monitor that's not being monitored: %d"
- "1"
- "<%@: %p upTime=%f upTimeIncludingSleep=%f upTimeIncludingSleepAndDriftCorrection=%f>"
- "<%@: %p | %@(%d) visible=%@ taskState=%@ debugState=%@"
- "<%@: %p: Identifier:%@, type:%@>"
- "@\"<ARProcessMonitorStateChangeDelegate>\""
- "@\"ARAlgorithmConfiguration\""
- "@\"RBSProcessMonitor\""
- "@\"RBSProcessStateUpdate\""
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@32@0:8@16q24"
- "@32@0:8^{__CVBuffer=}16d24"
- "@40@0:8d16d24d32"
- "@?"
- "@?16@0:8"
- "ARDaemonReplayBlockDelegate"
- "ARDaemonReplayDelegate"
- "ARData"
- "ARJasperData"
- "ARObjectTrackingDaemonConfiguration"
- "ARObjectTrackingDaemonControl"
- "ARProcessDebugStateDebuggingAsserted"
- "ARProcessDebugStateDebuggingPTraced"
- "ARProcessDebugStateNone"
- "ARProcessDebugStateUnknown"
- "ARProcessImmersivenessLevelDefocused"
- "ARProcessImmersivenessLevelFull"
- "ARProcessImmersivenessLevelNone"
- "ARProcessMonitor"
- "ARProcessMonitorStateUpdate"
- "ARProcessTaskStateBackgroundTaskSuspended"
- "ARProcessTaskStateRunningBackground"
- "ARProcessTaskStateRunningForeground"
- "ARProcessTaskStateTerminated"
- "ARProcessTaskStateUnknown"
- "ARReplayGraphScheduler"
- "ARSystemTimeSnapshot"
- "ARUserProfile"
- "B28@0:8i16o^@20"
- "Daemon service resume"
- "Default"
- "Enrolled"
- "Error: %{public}@ <%p>: Could not create a process handle for pid %d"
- "Error: %{public}@ <%p>: Could not find a process identifier for pid %d"
- "Guest"
- "PersistGuest"
- "ProcessMonitor"
- "T@\"<ARProcessMonitorStateChangeDelegate>\",W,N,V_delegate"
- "T@\"ARAlgorithmConfiguration\",&,V_currentConfiguration"
- "T@\"ARDaemon\",R,W,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_name"
- "T@?,C,N,V_replayFailedBlock"
- "T@?,C,N,V_replayStartedBlock"
- "T@?,C,N,V_replayStoppedBlock"
- "T@?,C,N,V_replayUpdatedBlock"
- "TB,R,N,V_isVisible"
- "T^{__CVBuffer=},N,V_dataBuffer"
- "Td,N,V_timestamp"
- "Td,R,N,V_upTime"
- "Td,R,N,V_upTimeIncludingSleep"
- "Td,R,N,V_upTimeIncludingSleepAndDriftCorrection"
- "Ti,R,N,V_pid"
- "Tq,R,N,V_debugState"
- "Tq,R,N,V_taskState"
- "Tq,R,N,V_type"
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "_currentConfiguration"
- "_dataBuffer"
- "_debugState"
- "_identifier"
- "_immersive"
- "_isVisible"
- "_latestTaskErrorMap"
- "_name"
- "_pid"
- "_pidsLock"
- "_pidsToObserve"
- "_processMonitor"
- "_replayFailedBlock"
- "_replayStartedBlock"
- "_replayStoppedBlock"
- "_replayUpdatedBlock"
- "_taskState"
- "_timestamp"
- "_type"
- "_upTime"
- "_upTimeIncludingSleep"
- "_upTimeIncludingSleepAndDriftCorrection"
- "_update"
- "allValues"
- "b"
- "com.apple.frontboard.visibility"
- "currentConfiguration"
- "d16@0:8"
- "daemonServiceForServiceNamed:"
- "dataBuffer"
- "debugState"
- "descriptor"
- "endowmentNamespaces"
- "handleForIdentifier:error:"
- "handleStateUpdate:"
- "identifier"
- "identifierWithPid:"
- "initWithARProcessTaskState:"
- "initWithBuffer:timestamp:"
- "initWithDelegate:daemonConfiguration:"
- "initWithDelegate:daemonConfiguration:watchdogMonitor:"
- "initWithIdentifier:type:"
- "initWithRBSProcessStateUpdate:"
- "initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:"
- "isDaemon"
- "isGuestProfileEnabled"
- "isVisible"
- "localAnonymousListenerDaemon"
- "monitorWithConfiguration:"
- "name"
- "predicateMatchingIdentifier:"
- "process"
- "processIsDaemon:error:"
- "processMonitor:didUpdateState:"
- "q"
- "replayDidFailWithError:"
- "replayDidStartWithReplayTime:"
- "replayDidStop"
- "replayDidUpdateResourceWithKey:atTime:"
- "replayFailedBlock"
- "replayStartedBlock"
- "replayStoppedBlock"
- "replayUpdatedBlock"
- "serviceTypeRequiresImmersiveMode"
- "setCurrentConfiguration:"
- "setDataBuffer:"
- "setEndowmentNamespaces:"
- "setPredicates:"
- "setReplayFailedBlock:"
- "setReplayStartedBlock:"
- "setReplayStoppedBlock:"
- "setReplayUpdatedBlock:"
- "setServiceClass:"
- "setStateDescriptor:"
- "setTimestamp:"
- "setUpdateHandler:"
- "setValues:"
- "startMonitoringImmersiveStatusForPID:withServices:"
- "startMonitoringPID:"
- "stopMonitoringImmersiveStatusForPID:"
- "stopMonitoringPID:"
- "suspend"
- "taskState"
- "type"
- "updateAlgorithmConfigurationWithService:"
- "updateAlgorithmConfigurationWithServices:"
- "updateConfiguration:"
- "updateProcessMonitorConfig:withPredicates:"
- "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
- "v20@0:8i16"
- "v24@0:8^{__CVBuffer=}16"
- "v28@0:8i16@20"
- "v32@0:8@\"NSString\"16d24"
- "v32@0:8@16d24"
- "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
- "valueForEntitlement:"

```
