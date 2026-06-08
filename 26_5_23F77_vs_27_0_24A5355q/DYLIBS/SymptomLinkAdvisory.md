## SymptomLinkAdvisory

> `/System/Library/PrivateFrameworks/SymptomLinkAdvisory.framework/SymptomLinkAdvisory`

```diff

-2169.120.7.0.0
-  __TEXT.__text: 0xa68
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0x490
-  __TEXT.__cstring: 0x68
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__oslogstring: 0x176
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methname: 0xb7f
-  __TEXT.__objc_methtype: 0x859
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x18
+2357.0.0.0.2
+  __TEXT.__text: 0x190e0
+  __TEXT.__objc_methlist: 0x5ec
+  __TEXT.__cstring: 0x4a6
+  __TEXT.__const: 0xc90
+  __TEXT.__gcc_except_tab: 0x24
+  __TEXT.__oslogstring: 0xf53
+  __TEXT.__swift5_typeref: 0x3ac
+  __TEXT.__swift5_capture: 0x308
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__swift5_reflstr: 0x7be
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__constg_swiftt: 0x678
+  __TEXT.__swift5_fieldmd: 0x628
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_cont: 0x13c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__eh_frame: 0xdc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0xc20
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x58
+  __DATA_CONST.__objc_selrefs: 0x5e0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x240
+  __AUTH_CONST.__const: 0xee8
+  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__objc_const: 0x1a88
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH.__objc_data: 0x450
+  __AUTH.__data: 0x930
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x328
+  __DATA.__bss: 0xd50
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics
+  - /System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CA8A12C-3848-397E-9E72-7F02717A8E9E
-  Functions: 51
-  Symbols:   237
-  CStrings:  189
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 00BADC44-A0AA-3E03-9501-604C1F570135
+  Functions: 678
+  Symbols:   848
+  CStrings:  126
 
Symbols:
+ +[SLAPowerMonitorBridge sharedInstance]
+ +[SLAPowerMonitorBridge sharedInstance].cold.1
+ -[ALUManager(UltraLowPowerNetworking) isAluminiumSupported]
+ -[ALUManager(UltraLowPowerNetworking) startReceivingULPNRecommendationsForPeerWithUUID:completion:]
+ -[ALUManager(UltraLowPowerNetworking) stopReceivingULPNRecommendationsForPeerWithUUID:completion:]
+ -[SLAPowerMonitorBridge batteryPercentage]
+ -[SLAPowerMonitorBridge init]
+ -[SLAPowerMonitorBridge parseBatteryProperties:]
+ -[SLAPowerMonitorBridge parseBatteryProperties:].cold.1
+ -[SLAPowerMonitorBridge parseBatteryProperties:].cold.2
+ -[SLAPowerMonitorBridge pluggedIn]
+ -[SLAPowerMonitorBridge refreshBatteryState]
+ -[SLAPowerMonitorBridge refreshBatteryState].cold.1
+ -[SLAPowerMonitorBridge refreshBatteryState].cold.2
+ -[SLAPowerMonitorBridge setBatteryPercentage:]
+ -[SLAPowerMonitorBridge setPluggedIn:]
+ _AnalyticsSendEventLazy
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFRelease
+ _IOPSCopyPowerSourcesInfo
+ _IOPSCopyPowerSourcesList
+ _IOPSGetPowerSourceDescription
+ _NSLocalizedDescriptionKey
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NWStatsManager
+ _OBJC_CLASS_$_NWStatsProtocolSnapshot
+ _OBJC_CLASS_$_NWStatsQUICSnapshot
+ _OBJC_CLASS_$_NWStatsTCPSnapshot
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_SLAInterfaceStats
+ _OBJC_CLASS_$_SLAPowerMonitorBridge
+ _OBJC_CLASS_$_SLASnapshot
+ _OBJC_CLASS_$_SLATelemetrySnapshot
+ _OBJC_CLASS_$_SymptomLinkAdvisoryAOPShim
+ _OBJC_CLASS_$_SymptomLinkAdvisoryBridge
+ _OBJC_CLASS_$__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_SLAPowerMonitorBridge._batteryPercentage
+ _OBJC_IVAR_$_SLAPowerMonitorBridge._pluggedIn
+ _OBJC_METACLASS_$_SLAPowerMonitorBridge
+ _OBJC_METACLASS_$_SymptomLinkAdvisoryBridge
+ _OBJC_METACLASS_$__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_SymptomLinkAdvisoryBridge
+ __DATA_SymptomLinkAdvisoryBridge
+ __DATA__TtC19SymptomLinkAdvisory10SLAAOPShim
+ __DATA__TtC19SymptomLinkAdvisory14SLAFlowMonitor
+ __DATA__TtC19SymptomLinkAdvisory15SLAPowerMonitor
+ __DATA__TtC19SymptomLinkAdvisory17SLAThermalMonitor
+ __DATA__TtC19SymptomLinkAdvisory18SLAAdminController
+ __DATA__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ __DATA__TtC19SymptomLinkAdvisory22SLATelemetryController
+ __DATA__TtC19SymptomLinkAdvisory23SLALargeTransferMonitor
+ __INSTANCE_METHODS_SymptomLinkAdvisoryBridge
+ __INSTANCE_METHODS__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ __IVARS_SymptomLinkAdvisoryBridge
+ __IVARS__TtC19SymptomLinkAdvisory10SLAAOPShim
+ __IVARS__TtC19SymptomLinkAdvisory14SLAFlowMonitor
+ __IVARS__TtC19SymptomLinkAdvisory15SLAPowerMonitor
+ __IVARS__TtC19SymptomLinkAdvisory17SLAThermalMonitor
+ __IVARS__TtC19SymptomLinkAdvisory18SLAAdminController
+ __IVARS__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ __IVARS__TtC19SymptomLinkAdvisory22SLATelemetryController
+ __IVARS__TtC19SymptomLinkAdvisory23SLALargeTransferMonitor
+ __METACLASS_DATA_SymptomLinkAdvisoryBridge
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory10SLAAOPShim
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory14SLAFlowMonitor
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory15SLAPowerMonitor
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory17SLAThermalMonitor
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory18SLAAdminController
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory22SLATelemetryController
+ __METACLASS_DATA__TtC19SymptomLinkAdvisory23SLALargeTransferMonitor
+ __OBJC_$_CLASS_METHODS_SLAPowerMonitorBridge
+ __OBJC_$_INSTANCE_METHODS_ALUManager(UltraLowPowerNetworking)
+ __OBJC_$_INSTANCE_METHODS_SLAPowerMonitorBridge
+ __OBJC_$_INSTANCE_VARIABLES_SLAPowerMonitorBridge
+ __OBJC_$_PROP_LIST_SLAPowerMonitorBridge
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NWStatsManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NWStatsManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_NWStatsManagerDelegate
+ __OBJC_CLASS_RO_$_SLAPowerMonitorBridge
+ __OBJC_LABEL_PROTOCOL_$_NWStatsManagerDelegate
+ __OBJC_METACLASS_RO_$_SLAPowerMonitorBridge
+ __OBJC_PROTOCOL_$_NWStatsManagerDelegate
+ __PROTOCOLS__TtC19SymptomLinkAdvisory19FlowMonitorDelegate
+ __PROTOCOLS__TtC19SymptomLinkAdvisory19FlowMonitorDelegate.8
+ ___39+[SLAPowerMonitorBridge sharedInstance]_block_invoke
+ ___59-[SymptomLinkAdvisoryConnectionManager _setupXPCConnection]_block_invoke.138
+ ___block_literal_global.140
+ ___chkstk_darwin
+ ___swift__destructor
+ ___swift__destructor.10
+ ___swift__destructor.40
+ ___swift_allocate_value_buffer
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.36
+ ___swift_closure_destructor.37
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.43
+ ___swift_closure_destructor.43Tm
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.54
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.69
+ ___swift_closure_destructor.7
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.80
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_memcpy32_4
+ ___swift_memcpy43_8
+ ___swift_memcpy5_4
+ ___swift_memcpy78_8
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __os_log_debug_impl
+ __os_log_default
+ __os_log_error_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SymptomLinkAdvisory
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SymptomLinkAdvisory
+ __swift_dead_method_stub
+ __swift_implicitisolationactor_to_executor_cast
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 19SymptomLinkAdvisory15SLAAOPShimErrorOSHAASQ
+ _associated conformance 19SymptomLinkAdvisory16SLATransferEventOSHAASQ
+ _associated conformance 19SymptomLinkAdvisory18SLAAOPReportReasonOSHAASQ
+ _associated conformance 19SymptomLinkAdvisory8SLAErrorOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.2
+ _block_copy_helper.30
+ _block_copy_helper.33
+ _block_copy_helper.39
+ _block_copy_helper.71
+ _block_descriptor
+ _block_descriptor.32
+ _block_descriptor.35
+ _block_descriptor.4
+ _block_descriptor.41
+ _block_descriptor.73
+ _block_destroy_helper
+ _block_destroy_helper.3
+ _block_destroy_helper.31
+ _block_destroy_helper.34
+ _block_destroy_helper.40
+ _block_destroy_helper.72
+ _bzero
+ _clock_gettime_nsec_np
+ _kNWStatsParameterMappingCanonicalizeProcessNames
+ _kNWStatsParameterMappingUseNEHelper
+ _kNWStatsParameterTrafficDeltaAdjustmentFactor
+ _kNWStatsSelectHasTraffic
+ _kNWStatsSelectInterfaceCompanionLink
+ _kNWStatsSelectInterfaceCompanionLinkBluetooth
+ _kNWStatsSelectInterfaceWiFi
+ _kNWStatsSelectInterfaceWired
+ _malloc_size
+ _memcpy
+ _memmove
+ _notify_cancel
+ _notify_get_state
+ _notify_register_dispatch
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$QUICState
+ _objc_msgSend$TCPState
+ _objc_msgSend$attributedEntity
+ _objc_msgSend$batteryPercentage
+ _objc_msgSend$configure:
+ _objc_msgSend$connProbeFailed
+ _objc_msgSend$connectWithError:
+ _objc_msgSend$deltaAccountingRxCompanionLinkBluetoothBytes
+ _objc_msgSend$deltaAccountingRxWiFiBytes
+ _objc_msgSend$deltaAccountingRxWiredBytes
+ _objc_msgSend$deltaAccountingTxCompanionLinkBluetoothBytes
+ _objc_msgSend$deltaAccountingTxWiFiBytes
+ _objc_msgSend$deltaAccountingTxWiredBytes
+ _objc_msgSend$deltaRxDuplicateBytes
+ _objc_msgSend$deltaRxOutOfOrderBytes
+ _objc_msgSend$deltaTxRetransmittedBytes
+ _objc_msgSend$description
+ _objc_msgSend$disableAutoLinkUpgradeWithError:
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$enableAutoLinkUpgradeWithError:
+ _objc_msgSend$flowSnapshotTimestamp
+ _objc_msgSend$frictionEventsBT
+ _objc_msgSend$frictionEventsWiFi
+ _objc_msgSend$getTelemetryWithError:
+ _objc_msgSend$hasTraffic
+ _objc_msgSend$hasTrafficDelta
+ _objc_msgSend$init
+ _objc_msgSend$initWithAggregationWindowMs:reportReason:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithUnsignedChar:
+ _objc_msgSend$initWithUnsignedInt:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$interfaceCellular
+ _objc_msgSend$interfaceCompanionLink
+ _objc_msgSend$interfaceWiFi
+ _objc_msgSend$interfaceWired
+ _objc_msgSend$isAOPOffloaded
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$liveLinkAdvisories
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$parseBatteryProperties:
+ _objc_msgSend$periodDurationSec
+ _objc_msgSend$pluggedIn
+ _objc_msgSend$processName
+ _objc_msgSend$readProbeFailed
+ _objc_msgSend$recommendationChanges
+ _objc_msgSend$refreshBatteryState
+ _objc_msgSend$refreshUsingBlock:completionBlock:
+ _objc_msgSend$reportSnapshot:error:
+ _objc_msgSend$rttAverage
+ _objc_msgSend$rttMinimum
+ _objc_msgSend$rttVariation
+ _objc_msgSend$rxBytes
+ _objc_msgSend$rxPackets
+ _objc_msgSend$setActiveFlowCount:
+ _objc_msgSend$setActiveTransferEstimatedTotal:
+ _objc_msgSend$setActiveTransferRemainingBytes:
+ _objc_msgSend$setAvgRTTMs:
+ _objc_msgSend$setBatteryPercentage:
+ _objc_msgSend$setBluetoothStats:
+ _objc_msgSend$setConnProbeFailureCount:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDuplicateBytes:
+ _objc_msgSend$setIsPluggedIn:
+ _objc_msgSend$setMaxRTTVarianceMs:
+ _objc_msgSend$setMinRTTMs:
+ _objc_msgSend$setOutOfOrderBytes:
+ _objc_msgSend$setReadProbeFailureCount:
+ _objc_msgSend$setRetransmittedBytes:
+ _objc_msgSend$setRxBytes:
+ _objc_msgSend$setThermalPressure:
+ _objc_msgSend$setTransferActive:
+ _objc_msgSend$setTxBytes:
+ _objc_msgSend$setWifiStats:
+ _objc_msgSend$setWiredStats:
+ _objc_msgSend$setWriteProbeFailureCount:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$snapshotReason
+ _objc_msgSend$snapshotsProcessed
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$stallEventsBT
+ _objc_msgSend$stallEventsWiFi
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$teardown
+ _objc_msgSend$txBytes
+ _objc_msgSend$txPackets
+ _objc_msgSend$writeProbeFailed
+ _objc_opt_self
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
+ _sharedInstance.onceToken
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain
+ _swift_retain_n
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_retain_x8
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
+ _swift_willThrowTypedImpl
+ _symbolic $sSY
+ _symbolic BD
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SS_So8NSObjectCt
+ _symbolic SS_ypt
+ _symbolic SaySSG
+ _symbolic SaySo23NWStatsProtocolSnapshotCG
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic ScCy_____ySo14NWStatsManagerC_____G_____G s6ResultOsRi_zRi0_zrlE 19SymptomLinkAdvisory19SLAFlowMonitorErrorO s5NeverO
+ _symbolic ScCyyt_____G s5NeverO
+ _symbolic ScPSg
+ _symbolic ScTyyt_____GSg s5NeverO
+ _symbolic Sd
+ _symbolic Shy_____G s6UInt64V
+ _symbolic Si
+ _symbolic So14NWStatsManagerC
+ _symbolic So14NWStatsManagerCSg
+ _symbolic So15NWStatsSnapshotC
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So21SLAPowerMonitorBridgeC
+ _symbolic So26SymptomLinkAdvisoryAOPShimCSg
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 19SymptomLinkAdvisory10SLAAOPShimC
+ _symbolic _____ 19SymptomLinkAdvisory12SLATelemetryV
+ _symbolic _____ 19SymptomLinkAdvisory13SLAPowerStateV
+ _symbolic _____ 19SymptomLinkAdvisory14SLAFlowMonitorC
+ _symbolic _____ 19SymptomLinkAdvisory15SLAAOPShimErrorO
+ _symbolic _____ 19SymptomLinkAdvisory15SLAPowerMonitorC
+ _symbolic _____ 19SymptomLinkAdvisory16SLATransferEventO
+ _symbolic _____ 19SymptomLinkAdvisory17SLAThermalMonitorC
+ _symbolic _____ 19SymptomLinkAdvisory18SLAAOPReportReasonO
+ _symbolic _____ 19SymptomLinkAdvisory18SLAAdminControllerC
+ _symbolic _____ 19SymptomLinkAdvisory18SLATransferContextV
+ _symbolic _____ 19SymptomLinkAdvisory19FlowMonitorDelegateC
+ _symbolic _____ 19SymptomLinkAdvisory19SLAFlowMonitorErrorO
+ _symbolic _____ 19SymptomLinkAdvisory22SLAInterfaceAggregatorV
+ _symbolic _____ 19SymptomLinkAdvisory22SLATelemetryControllerC
+ _symbolic _____ 19SymptomLinkAdvisory23SLALargeTransferMonitorC
+ _symbolic _____ 19SymptomLinkAdvisory8SLAErrorO
+ _symbolic _____ 19SymptomLinkAdvisory9L4MetricsV
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ So22OSThermalPressureLevela
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt16V
+ _symbolic _____ s6UInt32V
+ _symbolic _____ s6UInt64V
+ _symbolic _____5errno_t s5Int32V
+ _symbolic _____Sg 19SymptomLinkAdvisory19FlowMonitorDelegateC
+ _symbolic _____Sg 19SymptomLinkAdvisory22SLAInterfaceAggregatorV
+ _symbolic _____SgXw 19SymptomLinkAdvisory14SLAFlowMonitorC
+ _symbolic _____SgXw 19SymptomLinkAdvisory17SLAThermalMonitorC
+ _symbolic _____SgXw 19SymptomLinkAdvisory23SLALargeTransferMonitorC
+ _symbolic _____SgXwz_Xx 19SymptomLinkAdvisory14SLAFlowMonitorC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySo14NWStatsManagerC_____G s6ResultOsRi_zRi0_zrlE 19SymptomLinkAdvisory19SLAFlowMonitorErrorO
+ _symbolic _____y_____G s11_SetStorageC s6UInt64V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____z_Xx s6UInt64V
+ _symbolic ySo15NWStatsSnapshotCYbc
+ _symbolic y_____YbcSg 19SymptomLinkAdvisory16SLATransferEventO
+ _symbolic ytIeAgHr_
+ _type_layout_string 19SymptomLinkAdvisory12SLATelemetryV
+ _type_layout_string 19SymptomLinkAdvisory13SLAPowerStateV
+ _type_layout_string 19SymptomLinkAdvisory18SLATransferContextV
+ _type_layout_string 19SymptomLinkAdvisory22SLAInterfaceAggregatorV
+ _type_layout_string 19SymptomLinkAdvisory9L4MetricsV
+ _type_layout_string So22OSThermalPressureLevela
- __OBJC_$_INSTANCE_METHODS_ALUManager
- ___59-[SymptomLinkAdvisoryConnectionManager _setupXPCConnection]_block_invoke.135
- ___block_literal_global.137
CStrings:
+ "  Delta: WiFi rx=%lluB tx=%lluB | Wired rx=%lluB tx=%lluB | BT rx=%lluB tx=%lluB"
+ "  QUIC probe failures: %s"
+ "  QUIC: rtt=%sms (min=%s var=%s) (retx=%uB dup=%uB ooo=%uB)%s"
+ "  TCP probe failures: %s"
+ "  TCP: rtt=%sms (min=%s var=%s) (retx=%uB dup=%uB ooo=%uB)%s"
+ "  Traffic: rx=%lluB/%llupkt tx=%lluB/%llupkt [%s]"
+ "AC Power"
+ "Already collecting telemetry, skipping"
+ "Battery properties: %{private}@"
+ "Cannot parse nil batteryProperties, returning"
+ "Cannot poll: monitoring not active"
+ "Cannot poll: stats manager not initialized"
+ "Current Capacity"
+ "Error connecting to coprocessor service: %@"
+ "Error fetching current thermal pressure level"
+ "Error fetching initial thermal pressure level"
+ "Error registering for thermal pressure notifications"
+ "Failed to configure NWStatsManager (errno: "
+ "Failed to configure NWStatsManager (errno: %d)"
+ "Failed to create NWStatsManager"
+ "Failed to disable Aluminium: %@"
+ "Failed to fetch telemetry, skipping submission: %@"
+ "Failed to get state for above_threshold"
+ "Failed to get state for below_threshold"
+ "Failed to register for above_threshold notification"
+ "Failed to register for below_threshold notification"
+ "Failed to report snapshot: %@"
+ "Failed to start ULPN monitoring: %@"
+ "Failed to stop ULPN monitoring"
+ "Flow monitor failed to start"
+ "Flow monitor failed to stop"
+ "Flow monitoring already active"
+ "Flow monitoring is already active"
+ "Flow monitoring not active"
+ "Found non-protocol snapshot, returning"
+ "Handling snapshot: %s [%s]"
+ "Handling transfer event %s, sending immediate report"
+ "IOPSCopyPowerSourcesInfo failed"
+ "IOPSCopyPowerSourcesList failed"
+ "InternalBattery"
+ "Large transfer monitoring started"
+ "Large transfer monitoring stopped"
+ "NWStatsManager configured successfully"
+ "No eventHandler registered"
+ "No recent snapshots to aggregate, skipping report"
+ "Poll failed (errno: %d)"
+ "Power Source State"
+ "Received below_threshold with no active transfers"
+ "Received thermal pressure notification for the same value: %s"
+ "Reported snapshot [%s window=%ums]"
+ "SLAAdminController"
+ "SLAAdminController not available"
+ "SLALargeTransferMonitor"
+ "SLAThermalMonitor"
+ "Skipping AOP-offloaded flow: %s[%s]"
+ "Skipping zero-traffic snapshot: %s[%s]"
+ "Started flow monitoring"
+ "Started periodic flow polling with interval: %fs"
+ "Started periodic snapshot reporting [interval %fs]"
+ "Starting Aluminium telemetry collection [interval %fs]"
+ "Starting Aluminium telemetry collection [override interval %fs]"
+ "Starting ULPN monitoring"
+ "Starting ULPN monitoring for peer %s"
+ "Stats manager configuration failed"
+ "Stats manager creation failed"
+ "Stopped flow monitoring"
+ "Stopped periodic polling"
+ "Stopped periodic reporting"
+ "Stopping Aluminium telemetry collection"
+ "Stopping ULPN monitoring"
+ "Stopping ULPN monitoring for peer %s"
+ "Submitting telemetry [period=%us snap=%u reco=%u wFric=%u bFric=%u wStall=%u bStall=%u ll=%u]"
+ "Successfully started ULPN monitoring"
+ "Successfully stopped ULPN monitoring"
+ "SymptomLinkAdvisory.FlowMonitorDelegate"
+ "SymptomLinkAdvisoryAOPShim not available"
+ "Thermal monitoring started, initial level: %s"
+ "Thermal monitoring stopped"
+ "Thermal pressure changed: %s -> %s"
+ "Transfer completed (remaining %llu <= %llu%% threshold %llu)"
+ "Transfer stalled (no progress for %fs)"
+ "Transfer started: estimated=%llu inbound=%{bool}d count=%ld total=%llu"
+ "Transfer state reset"
+ "Transfer threshold crossed: estimated=%llu inbound=%{bool}d count=%ld total=%llu"
+ "Type"
+ "[%s] Skipping immediate report"
+ "com.apple.libnetcore.workload_above_threshold"
+ "com.apple.libnetcore.workload_below_threshold"
+ "com.apple.symptoms.aluminium.periodic"
+ "com.apple.symptoms.aluminium.telemetryInterval"
+ "com.apple.symptoms.notify"
+ "com.apple.symptoms.slaflowmonitor"
+ "com.apple.symptomsframework.symptomlinkadvisory"
+ "com.apple.system.thermalpressurelevel"
+ "coprocessor W:%s B:%s w:%s pwr=%s th=%s xf=%s"
+ "frictionEventsBT"
+ "frictionEventsWiFi"
+ "init()"
+ "initializeStatsManager()"
+ "liveLinkAdvisories"
+ "periodDurationSec"
+ "recommendationChanges"
+ "snapshotsProcessed"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<ALUManagerDelegate>\""
- "@\"ALUManager\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@\"SymptomLinkAdvisoryNWActivityReporter\""
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "ALUManager"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SFServiceInterface"
- "SymptomLinkAdvisoryConnectionManager"
- "SymptomLinkAdvisoryNWActivityReporter"
- "SymptomLinkAdvisoryProtocol"
- "T#,R"
- "T@\"<ALUManagerDelegate>\",W,N,V_delegate"
- "T@\"ALUManager\",&,V_aluManager"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"SymptomLinkAdvisoryNWActivityReporter\",&,V_nwActivityReporter"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_aluManager"
- "_connection"
- "_delegate"
- "_handleALUMessageFromSymptomsd:"
- "_handleALUMessageTypeLinkAdviceWithPayload:"
- "_handleALUMessageTypeTransferStatsWithPayload:"
- "_handleNWActivityFragmentMessageFromSymptomsd"
- "_nwActivityReporter"
- "_setupXPCConnection"
- "aluManager"
- "autorelease"
- "class"
- "cleanupNDFDeviceRecordsWithReply:"
- "conformsToProtocol:"
- "createSnapshotFor:pred:actions:reply:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
- "fetchNDFDeviceRecordsWithReply:"
- "getOption:inScopes:reply:"
- "getPreferCellOverWiFiWithOptions:reply:"
- "hash"
- "identifierForUUID:reply:"
- "init"
- "initWithDelegate:queue:"
- "initWithMachServiceName:options:"
- "initWithQueue:fragmentRequesthandler:"
- "inquireNOIFor:orPredicate:requestedKeys:options:reply:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listNDFDeviceObjectsWithIdentifier:reply:"
- "ndfClientCheckInWithReply:"
- "ndfClientSubscriptionIsActive:reply:"
- "networkRestrictsMulticastTrafficWithReply:"
- "nwActivityReporter"
- "performActionWithOptions:inScopes:reply:"
- "performAppEndpointTrackingPeriodicTasksWithReply:"
- "performAppExperiencePeriodicTasksWithReply:"
- "performAppPeriodicTasksWithReply:"
- "performAppTrackingPeriodicTasksWithReply:"
- "performPersistentStoreHealthCheckWithReply:"
- "performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:"
- "performQueryOnEntity:pred:sort:actions:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pingEndpoints:reply:"
- "release"
- "reportALURecommendationHonoredStatus:forAdvice:adviceID:reason:peerUUID:"
- "reportALURecommendationUpgradeStatus:forAdviceID:peerUUID:"
- "reportLastReceivedALURecommendationWithAdvice:reason:peerUUID:"
- "reportPreferInfraWiFiRequestFromClient:peerUUID:"
- "resetDataFor:nameKind:inScopes:reply:"
- "resetUsageFor:nameKind:reply:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "retrieveActivityMetrics:reply:"
- "self"
- "sendALUMessageToSymptomsdWithPayload:"
- "sendMessage:toEndpoints:reply:"
- "sendNWActivityFragmentToSymptomsd:"
- "sendPayloadToDaemonWithReply:"
- "setAluManager:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setNwActivityReporter:"
- "setOption:inScopes:reply:"
- "setPreferCellOverWiFiWithOptions:reply:"
- "setRemoteObjectInterface:"
- "setUsageOption:reply:"
- "setWithObjects:"
- "sharedInstance"
- "startReceivingALURecommendationsForPeerWithUUID:"
- "startSendingNWActivityFragments"
- "stopReceivingALURecommendationsForPeerWithUUID:"
- "stopSendingNWActivityFragments"
- "subscribeToNOIsFor:orPredicate:options:"
- "superclass"
- "trainModelAndScore:lastScoreDate:reply:"
- "triggerSendPayloadToDaemonWithInterval:leeway:reply:"
- "unsubscribeToNOIs:"
- "updatedNDFDeviceRecords:reply:"
- "v16@0:8"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSString\"@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8B16@\"NSDate\"20@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8B16@20@?28"
- "v36@0:8B16Q20@28"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16Q24@32"
- "v40@0:8q16q24@?32"
- "v40@0:8q16q24@?<v@?B>32"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?B>40"
- "v48@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSDictionary\"32@?<v@?@\"NSUUID\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8B16Q20Q28Q36@44"
- "v56@0:8@\"NSString\"16@\"NSPredicate\"24@\"NSSortDescriptor\"32@\"NSDictionary\"40@?<v@?@\"NSArray\">48"
- "v56@0:8@\"NWNetworkOfInterest\"16@\"NSPredicate\"24@\"NSDictionary\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSString\"16@\"FetchRequestPropertiesDescriptor\"24@\"NSPredicate\"32@\"NSSortDescriptor\"40@\"NSDictionary\"48@?<v@?@\"NSArray\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
- "v72@0:8@16@24@32@40d48d56@?64"
- "zone"

```
