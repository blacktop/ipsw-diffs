## AudioAnalytics

> `/System/Library/PrivateFrameworks/AudioAnalytics.framework/AudioAnalytics`

```diff

-197.4.1.0.0
-  __TEXT.__text: 0x0
-  __TEXT.__const: 0x40
+209.5.16.0.0
+  __TEXT.__text: 0x167e4
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x2f4
+  __TEXT.__const: 0x538
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__swift5_typeref: 0x338
+  __TEXT.__swift5_capture: 0x460
+  __TEXT.__cstring: 0x1515
+  __TEXT.__constg_swiftt: 0x4fc
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x14b
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_types: 0x40
+  __TEXT.__swift5_fieldmd: 0x238
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__eh_frame: 0x2b8
+  __TEXT.__objc_classname: 0x10
+  __TEXT.__objc_methname: 0x606
+  __TEXT.__objc_methtype: 0x80
+  __TEXT.__objc_stubs: 0xa0
+  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x8
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_const: 0x790
+  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__objc_const: 0x118
+  __AUTH_CONST.__const: 0x1118
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH.__objc_data: 0x4b0
+  __AUTH.__data: 0x510
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0xf8
+  __DATA.__data: 0x1f0
+  __DATA.__bss: 0x580
+  __DATA.__common: 0x48
+  - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: C91207A3-FB00-3B4F-83A1-8B9ECEB1D4C2
-  Functions: 0
-  Symbols:   2
-  CStrings:  0
+  - /usr/lib/libc++.1.dylib
+  - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libperfcheck.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 69AC3510-C2A6-3D3D-9885-461B479DBD78
+  Functions: 578
+  Symbols:   496
+  CStrings:  224
 
Symbols:
+ +[Trace post:arg1:arg2:arg3:arg4:]
+ +[Trace post:args:]
+ +[Trace postEnd:arg1:arg2:arg3:arg4:]
+ +[Trace postEnd:args:]
+ +[Trace postStart:arg1:arg2:arg3:arg4:]
+ +[Trace postStart:args:]
+ -[TraceArgs arg1]
+ -[TraceArgs arg2]
+ -[TraceArgs arg3]
+ -[TraceArgs arg4]
+ -[TraceArgs initWithArg1:]
+ -[TraceArgs initWithArg1:arg2:]
+ -[TraceArgs initWithArg1:arg2:arg3:]
+ -[TraceArgs initWithArg1:arg2:arg3:arg4:]
+ -[TraceArgs init]
+ -[TraceArgs setArg1:]
+ -[TraceArgs setArg2:]
+ -[TraceArgs setArg3:]
+ -[TraceArgs setArg4:]
+ <redacted>
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table18
+ _AnalyticsSendEventLazy
+ _AudioAnalyticsCopyConfiguration
+ _AudioAnalyticsCreateReporterID
+ _AudioAnalyticsCreateReporterIDFromSessionID
+ _AudioAnalyticsCreateSharedClient
+ _AudioAnalyticsDestroyReporterID
+ _AudioAnalyticsGetAudioServiceType
+ _AudioAnalyticsRequestMessage
+ _AudioAnalyticsSendMessage
+ _AudioAnalyticsSendSessionlessMessage
+ _AudioAnalyticsSetAudioServiceType
+ _AudioAnalyticsSetConfiguration
+ _AudioAnalyticsStartReporter
+ _AudioAnalyticsStopReporter
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_internalBuild
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_Trace
+ _OBJC_CLASS_$_TraceArgs
+ _OBJC_CLASS_$__TtC14AudioAnalytics12ServerClient
+ _OBJC_CLASS_$__TtC14AudioAnalytics22AudioAnalyticsReporter
+ _OBJC_CLASS_$__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_TraceArgs._arg1
+ _OBJC_IVAR_$_TraceArgs._arg2
+ _OBJC_IVAR_$_TraceArgs._arg3
+ _OBJC_IVAR_$_TraceArgs._arg4
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_Trace
+ _OBJC_METACLASS_$_TraceArgs
+ _OBJC_METACLASS_$__TtC14AudioAnalytics12ServerClient
+ _OBJC_METACLASS_$__TtC14AudioAnalytics22AudioAnalyticsReporter
+ _OBJC_METACLASS_$__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __CATEGORY__TtC14AudioAnalytics22AudioAnalyticsReporter_$_AudioAnalytics
+ __CLASS_PROPERTIES__TtC14AudioAnalytics12ServerClient
+ __DATA__TtC14AudioAnalytics12ReporterData
+ __DATA__TtC14AudioAnalytics12ServerClient
+ __DATA__TtC14AudioAnalytics22AudioAnalyticsReporter
+ __DATA__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ __DATA__TtC14AudioAnalytics9PerfCheck
+ __DATA__TtC14AudioAnalyticsP33_7E7FBD6C32D57130B72D361337A0A4D99PCSession
+ __DATA__TtC14AudioAnalyticsP33_913F00E80B7812A5727E88F596D417BB19ReporterIDGenerator
+ __IVARS__TtC14AudioAnalytics12ReporterData
+ __IVARS__TtC14AudioAnalytics12ServerClient
+ __IVARS__TtC14AudioAnalytics22AudioAnalyticsReporter
+ __IVARS__TtC14AudioAnalytics9PerfCheck
+ __IVARS__TtC14AudioAnalyticsP33_7E7FBD6C32D57130B72D361337A0A4D99PCSession
+ __IVARS__TtC14AudioAnalyticsP33_913F00E80B7812A5727E88F596D417BB19ReporterIDGenerator
+ __METACLASS_DATA__TtC14AudioAnalytics12ReporterData
+ __METACLASS_DATA__TtC14AudioAnalytics12ServerClient
+ __METACLASS_DATA__TtC14AudioAnalytics22AudioAnalyticsReporter
+ __METACLASS_DATA__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ __METACLASS_DATA__TtC14AudioAnalytics9PerfCheck
+ __METACLASS_DATA__TtC14AudioAnalyticsP33_7E7FBD6C32D57130B72D361337A0A4D99PCSession
+ __METACLASS_DATA__TtC14AudioAnalyticsP33_913F00E80B7812A5727E88F596D417BB19ReporterIDGenerator
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_Trace
+ __OBJC_$_CLASS_METHODS__TtC14AudioAnalytics12ServerClient
+ __OBJC_$_CLASS_METHODS__TtC14AudioAnalytics22AudioAnalyticsReporter(AudioAnalytics)
+ __OBJC_$_INSTANCE_METHODS_TraceArgs
+ __OBJC_$_INSTANCE_METHODS__TtC14AudioAnalytics12ServerClient
+ __OBJC_$_INSTANCE_METHODS__TtC14AudioAnalytics22AudioAnalyticsReporter
+ __OBJC_$_INSTANCE_METHODS__TtC14AudioAnalytics22AudioAnalyticsReporter(AudioAnalytics)
+ __OBJC_$_INSTANCE_METHODS__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ __OBJC_$_INSTANCE_VARIABLES_TraceArgs
+ __OBJC_$_PROP_LIST_TraceArgs
+ __OBJC_CLASS_RO_$_Trace
+ __OBJC_CLASS_RO_$_TraceArgs
+ __OBJC_METACLASS_RO_$_Trace
+ __OBJC_METACLASS_RO_$_TraceArgs
+ __PROPERTIES__TtC14AudioAnalytics22AudioAnalyticsReporter
+ __PROPERTIES__TtC14AudioAnalytics26AudioAnalyticsTestReporter
+ __PROTOCOL_INSTANCE_METHODS__TtP14AudioAnalytics14ServerProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP14AudioAnalytics14ServerProtocol_
+ __PROTOCOL__TtP14AudioAnalytics14ServerProtocol_
+ __Unwind_Resume
+ ___chkstk_darwin
+ ___gxx_personality_v0
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy0_1
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AudioAnalytics
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_AudioAnalytics
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 14AudioAnalytics9PCSession33_7E7FBD6C32D57130B72D361337A0A4D9LLC5StateOSHAASQ
+ _associated conformance 14AudioAnalytics9PerfCheckC5State33_7E7FBD6C32D57130B72D361337A0A4D9LLOSHAASQ
+ _associated conformance 14AudioAnalyticsAA33_B3297EBAA099207B14418022917BE6F0LLOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.105
+ _block_copy_helper.115
+ _block_copy_helper.12
+ _block_copy_helper.125
+ _block_copy_helper.13
+ _block_copy_helper.135
+ _block_copy_helper.24
+ _block_copy_helper.34
+ _block_copy_helper.37
+ _block_copy_helper.44
+ _block_copy_helper.46
+ _block_copy_helper.50
+ _block_copy_helper.54
+ _block_copy_helper.59
+ _block_copy_helper.64
+ _block_copy_helper.65
+ _block_copy_helper.67
+ _block_copy_helper.75
+ _block_copy_helper.85
+ _block_copy_helper.95
+ _block_descriptor
+ _block_descriptor.107
+ _block_descriptor.117
+ _block_descriptor.127
+ _block_descriptor.137
+ _block_descriptor.14
+ _block_descriptor.15
+ _block_descriptor.26
+ _block_descriptor.36
+ _block_descriptor.39
+ _block_descriptor.46
+ _block_descriptor.48
+ _block_descriptor.52
+ _block_descriptor.56
+ _block_descriptor.61
+ _block_descriptor.66
+ _block_descriptor.67
+ _block_descriptor.69
+ _block_descriptor.77
+ _block_descriptor.87
+ _block_descriptor.97
+ _block_destroy_helper
+ _block_destroy_helper.106
+ _block_destroy_helper.116
+ _block_destroy_helper.126
+ _block_destroy_helper.13
+ _block_destroy_helper.136
+ _block_destroy_helper.14
+ _block_destroy_helper.25
+ _block_destroy_helper.35
+ _block_destroy_helper.38
+ _block_destroy_helper.45
+ _block_destroy_helper.47
+ _block_destroy_helper.51
+ _block_destroy_helper.55
+ _block_destroy_helper.60
+ _block_destroy_helper.65
+ _block_destroy_helper.66
+ _block_destroy_helper.68
+ _block_destroy_helper.76
+ _block_destroy_helper.86
+ _block_destroy_helper.96
+ _bzero
+ _dispatch_sync
+ _free
+ _getpid
+ _kAAPCMetricDirtyMemPeakDeltaID
+ _kAAPCMetricDirtyMemRecentPeakID
+ _kdebug_trace
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_autoreleaseReturnValue
+ _objc_msgSend
+ _objc_msgSend$arg1
+ _objc_msgSend$arg2
+ _objc_msgSend$arg3
+ _objc_msgSend$arg4
+ _objc_msgSend$init
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objectdestroy.28Tm
+ _objectdestroy.6Tm
+ _objectdestroy.79Tm
+ _os_log_type_enabled
+ _os_variant_is_darwinos
+ _pc_session_add_metric
+ _pc_session_begin
+ _pc_session_create
+ _pc_session_destroy
+ _pc_session_end
+ _pc_session_get_procname
+ _pc_session_get_values
+ _pc_session_set_procpid
+ _strerror
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeLayout2
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initEnumMetadataMultiPayload
+ _swift_initStackObject
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _symbolic $s14AudioAnalytics14ServerProtocolP
+ _symbolic $sSY
+ _symbolic 14AudioAnalytics14ServerProtocol_p
+ _symbolic Ig_
+ _symbolic SDySSypG
+ _symbolic SDy__________G s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic SS3key_yp5valuet
+ _symbolic SS3key_yp5valuetSg
+ _symbolic SS4name______2idt s6UInt64V
+ _symbolic SSSg
+ _symbolic SS_ypt
+ _symbolic Say_____G 14AudioAnalytics9PCSession33_7E7FBD6C32D57130B72D361337A0A4D9LLC
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Say_____G s5Int32V
+ _symbolic So15NSXPCConnectionC
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So8NSObjectC
+ _symbolic _____ 14AudioAnalytics0aB12TestReporterC
+ _symbolic _____ 14AudioAnalytics0aB8ReporterC
+ _symbolic _____ 14AudioAnalytics12ReporterDataC
+ _symbolic _____ 14AudioAnalytics12ServerClientC
+ _symbolic _____ 14AudioAnalytics13ReporterStateO
+ _symbolic _____ 14AudioAnalytics19ReporterIDGenerator33_913F00E80B7812A5727E88F596D417BBLLC
+ _symbolic _____ 14AudioAnalytics22ConnectedReporterStateO
+ _symbolic _____ 14AudioAnalytics9PCSession33_7E7FBD6C32D57130B72D361337A0A4D9LLC
+ _symbolic _____ 14AudioAnalytics9PCSession33_7E7FBD6C32D57130B72D361337A0A4D9LLC5StateO
+ _symbolic _____ 14AudioAnalytics9PerfCheckC
+ _symbolic _____ 14AudioAnalytics9PerfCheckC5State33_7E7FBD6C32D57130B72D361337A0A4D9LLO
+ _symbolic _____ 14AudioAnalyticsAA33_B3297EBAA099207B14418022917BE6F0LLO
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ So14AudioEventTypeV
+ _symbolic _____ So16AudioServiceTypeV
+ _symbolic _____ So18AudioEventCategoryV
+ _symbolic _____ s13OpaquePointerV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5Int64V
+ _symbolic _____ s6UInt16V
+ _symbolic _____ s6UInt32V
+ _symbolic _____3key______5valuet s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic _____3key_yp5valuet s11AnyHashableV
+ _symbolic _____Sg 14AudioAnalytics13ReporterStateO
+ _symbolic _____Sg 14AudioAnalytics9PerfCheckC
+ _symbolic _____SgIegg_ So15CFDictionaryRefa
+ _symbolic _____SgIeyBy_ So15CFDictionaryRefa
+ _symbolic _____SgXw 14AudioAnalytics12ServerClientC
+ _symbolic ___________9startDatet 14AudioAnalytics12ReporterDataC 10Foundation4DateV
+ _symbolic ___________t s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____ySS4name______2idtG s23_ContiguousArrayStorageC s6UInt64V
+ _symbolic _____ySSSay_____3key______5valuetGG s18_DictionaryStorageC s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic _____ySSSdG s18_DictionaryStorageC
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_SdtG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____3key______5valuetG s23_ContiguousArrayStorageC s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int32V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5Int64V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________G s18_DictionaryStorageC s5Int64V 14AudioAnalytics13ReporterStateO
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic ypSg
CStrings:
+ ".cxx_destruct"
+ "@\"NSDictionary\"8@?0"
+ "@16@0:8"
+ "@24@0:8@16"
+ "@24@0:8I16S20"
+ "@24@0:8Q16"
+ "@24@0:8q16"
+ "@32@0:8Q16Q24"
+ "@40@0:8Q16Q24Q32"
+ "@48@0:8Q16Q24Q32Q40"
+ "AudioAnalytics.AudioAnalyticsReporter"
+ "AudioAnalytics.ServerClient"
+ "CAReporterID is invalid. Returning early. { function=%{private}s, reporterID=%lld }"
+ "CAReportingPerfProcesses"
+ "Configuration empty. Returning early. { reporterID=%lld }"
+ "Destroying reporter. { reporterID=%lld }"
+ "Dictionary is not a string-keyed dictionary. Returning early. { function=%{private}s, reporterID=%lld }"
+ "Disconnecting all other reporters. { reporterIDs=%{public}s }"
+ "Division by zero"
+ "Division results in an overflow"
+ "Error in requestMessage. { error=%{private}s, reporterID=%lld }"
+ "Fatal error"
+ "Gathered performance metrics. { perfMetrics=%{private}s, reporterID=%lld }"
+ "HostApplicationDisplayID"
+ "Insufficient space allocated to copy string contents"
+ "Interruption handler: Server exited or crashed."
+ "Invalidation handler: Connection cannot be formed."
+ "MXHostApplicationDisplayID"
+ "Negative value is not representable"
+ "Q"
+ "Q16@0:8"
+ "Reconnecting started reporters. { reporterIDs=%{public}s }"
+ "Reporter disconnected or already stopped. { reporterID=%lld }"
+ "Reporter disconnected. { reporterID=%lld }"
+ "Reporter not started. Returning early. { reporterID=%lld }"
+ "ReporterID not created by client. Returning early. { function=%{private}s, reporterID=%lld }"
+ "Requesting message. { reporterID=%lld }"
+ "Restarting session after reconfiguring serviceType. { reporterID=%lld }"
+ "S16@0:8"
+ "S24@0:8q16"
+ "Sending message. { reporterID=%lld, message=%{private}s } "
+ "Set serviceType. { serviceType=%{public}s, reporterID=%lld, }"
+ "Setting configuration. { reporterID=%lld, configuration=%{private}s }"
+ "Setting new serviceType. { reporterID=%lld }"
+ "SimulateCustomer"
+ "Starting reporter. { reporterID=%lld }"
+ "Stopping reporter. { reporterID=%lld }"
+ "Stopping session while reconfiguring serviceType. { reporterID=%lld }"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Synchronous remote object proxy encountered error. { error=%{private}s }"
+ "T@\"NSDictionary\",N,C"
+ "T@\"_TtC14AudioAnalytics12ServerClient\",N,R"
+ "TQ,N,V_arg1"
+ "TQ,N,V_arg2"
+ "TQ,N,V_arg3"
+ "TQ,N,V_arg4"
+ "TS,N,R"
+ "Tq,N,VreporterID"
+ "Trace"
+ "TraceArgs"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_TtC14AudioAnalytics12ReporterData"
+ "_TtC14AudioAnalytics12ServerClient"
+ "_TtC14AudioAnalytics22AudioAnalyticsReporter"
+ "_TtC14AudioAnalytics26AudioAnalyticsTestReporter"
+ "_TtC14AudioAnalytics9PerfCheck"
+ "_TtC14AudioAnalyticsP33_7E7FBD6C32D57130B72D361337A0A4D99PCSession"
+ "_TtC14AudioAnalyticsP33_913F00E80B7812A5727E88F596D417BB19ReporterIDGenerator"
+ "_TtP14AudioAnalytics14ServerProtocol_"
+ "_arg1"
+ "_arg2"
+ "_arg3"
+ "_arg4"
+ "_unboostingRemoteObjectProxy"
+ "appName"
+ "arg1"
+ "arg2"
+ "arg3"
+ "arg4"
+ "clientReporterStates"
+ "com.apple.audioanalyticsd"
+ "com.apple.coreaudio"
+ "com.apple.coreaudio.IO.Error"
+ "com.apple.coreaudio.careporting.client"
+ "configuration"
+ "createReportingSession"
+ "createReportingSessionFromSessionID:"
+ "createSessionWith:"
+ "dealloc"
+ "destroy(reporterID:)"
+ "destroyReporterID:"
+ "destroySessionFor:"
+ "getConfiguration(reporterID:)"
+ "getConfiguration. { reporterID=%lld }"
+ "getConfigurationForReporterID:"
+ "getServiceNameFor:completion:"
+ "getServiceType(reporterID:)"
+ "getServiceType. { reporterID=%lld }"
+ "getServiceTypeForReporterID:"
+ "idGenerator"
+ "init"
+ "init()"
+ "initWithArg1:"
+ "initWithArg1:arg2:"
+ "initWithArg1:arg2:arg3:"
+ "initWithArg1:arg2:arg3:arg4:"
+ "initWithEndpoint:"
+ "initWithListenerEndpoint:"
+ "initWithMachServiceName:options:"
+ "initWithNewReporterID"
+ "initWithReporterID:"
+ "initWithSessionID:serviceType:"
+ "interfaceWithProtocol:"
+ "invalid Collection: less than 'count' elements in collection"
+ "logger"
+ "pcSessions"
+ "pc_session_add_metric failed. { metric=%{private}s }"
+ "pc_session_begin failed. { ret=%{private}s }"
+ "pc_session_create failed. { ret=%{private}s }."
+ "pc_session_destroy failed, { ret=%{private}s }"
+ "pc_session_end failed. { ret=%{private}s }"
+ "pc_session_set_procpid failed. { ret=%{private}s }."
+ "perfCheck"
+ "pids"
+ "post:arg1:arg2:arg3:arg4:"
+ "post:args:"
+ "postEnd:arg1:arg2:arg3:arg4:"
+ "postEnd:args:"
+ "postStart:arg1:arg2:arg3:arg4:"
+ "postStart:args:"
+ "q16@0:8"
+ "q20@0:8I16"
+ "recovered_session"
+ "remoteObjectProxy"
+ "reporterID"
+ "reporterIDCount"
+ "requestMessage received message. Invoking callback. { category=%s, type=%s, reporterID=%lld }"
+ "requestMessage(for:type:callback:)"
+ "requestMessageFor:category:type:reply:"
+ "requestMessageForCategory:type:callback:"
+ "requestMessageForReporterID:category:type:callback:"
+ "resume"
+ "sendMessage(_:category:type:)"
+ "sendMessage:category:type:"
+ "sendMessageForReporterID:message:category:type:"
+ "sendSessionlessMessage(_:category:type:)"
+ "sendSessionlessMessage:category:type:"
+ "sendSingleMessage:category:type:"
+ "sendWithMessage:with:and:for:"
+ "serialQueue"
+ "serviceType"
+ "session"
+ "session_duration"
+ "set(serviceType:)"
+ "setArg1:"
+ "setArg2:"
+ "setArg3:"
+ "setArg4:"
+ "setConfiguration:"
+ "setConfiguration:reporterID:"
+ "setConfigurationOnQueue(_:reporterID:)"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setRemoteObjectInterface:"
+ "setReporterID:"
+ "setServiceType:reporterID:"
+ "setServiceTypeOnQueue(_:reporterID:)"
+ "setWithConfiguration:for:"
+ "setWithServiceType:"
+ "setWithServiceType:for:"
+ "shared"
+ "start"
+ "startOnQueue(reporterID:)"
+ "startSessionFor:"
+ "startWithReporterID:"
+ "state"
+ "stop"
+ "stopOnQueue(reporterID:)"
+ "stopSessionFor:"
+ "stopWithReporterID:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8S16"
+ "v24@0:8@16"
+ "v24@0:8Q16"
+ "v24@0:8q16"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v28@0:8I16@20"
+ "v28@0:8S16q20"
+ "v32@0:8@\"NSDictionary\"16q24"
+ "v32@0:8@16I24S28"
+ "v32@0:8@16q24"
+ "v32@0:8I16S20@?24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"NSError\"@\"NSDictionary\">24"
+ "v32@0:8q16@?<v@?@\"NSError\"S>24"
+ "v40@0:8@\"NSDictionary\"16I24S28@\"NSArray\"32"
+ "v40@0:8@16I24S28@32"
+ "v40@0:8q16@24I32S36"
+ "v40@0:8q16I24S28@?32"
+ "v40@0:8q16I24S28@?<v@?@\"NSError\"@\"NSDictionary\">32"
+ "v52@0:8I16Q20Q28Q36Q44"
+ "v64@?0i8r*12i20Q24r*32d40Q48^v56"
+ "v8@?0"
+ "validateFor:completion:"
+ "xpcConnection"

```
