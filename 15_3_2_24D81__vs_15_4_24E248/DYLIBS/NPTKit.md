## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/Versions/A/NPTKit`

```diff

-164.0.0.0.0
-  __TEXT.__text: 0x22e78
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x2098
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x27eb
-  __TEXT.__gcc_except_tab: 0x8bc
-  __TEXT.__oslogstring: 0x934
-  __TEXT.__unwind_info: 0x700
-  __TEXT.__objc_classname: 0x33a
-  __TEXT.__objc_methname: 0x5511
-  __TEXT.__objc_methtype: 0xf91
-  __TEXT.__objc_stubs: 0x5c40
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0xd8
+175.0.0.0.0
+  __TEXT.__text: 0x35718
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0x24d4
+  __TEXT.__const: 0x3c4
+  __TEXT.__cstring: 0x2ec0
+  __TEXT.__gcc_except_tab: 0x8c4
+  __TEXT.__oslogstring: 0xe74
+  __TEXT.__constg_swiftt: 0x124
+  __TEXT.__swift5_typeref: 0x681
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x25d
+  __TEXT.__swift5_fieldmd: 0x1c0
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_capture: 0x430
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__unwind_info: 0xc30
+  __TEXT.__eh_frame: 0x880
+  __TEXT.__objc_classname: 0x300
+  __TEXT.__objc_methname: 0x5797
+  __TEXT.__objc_methtype: 0xed3
+  __TEXT.__objc_stubs: 0x5ba0
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d0
+  __DATA_CONST.__objc_selrefs: 0x1a60
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x3f00
-  __AUTH_CONST.__objc_const: 0x8180
+  __AUTH_CONST.__auth_got: 0x738
+  __AUTH_CONST.__const: 0x12a8
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x7f08
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x364
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x10
+  __AUTH.__objc_data: 0x7d0
+  __AUTH.__data: 0x260
+  __DATA.__objc_ivar: 0x35c
+  __DATA.__data: 0x778
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x180
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi
+  - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /System/Library/PrivateFrameworks/WiFiVelocity.framework/Versions/A/WiFiVelocity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF95D55E-6121-3A57-A036-9F6804CAFCC6
-  Functions: 753
-  Symbols:   2481
-  CStrings:  2460
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  UUID: 1F6C64A2-CE97-359E-BE1B-4B34F7014792
+  Functions: 1237
+  Symbols:   2773
+  CStrings:  2569
 
Symbols:
+ +[NPTMetadataEvent supportsSecureCoding]
+ +[NPTPerformanceTestConfiguration supportsSecureCoding]
+ -[NPTMetadataEvent encodeWithCoder:]
+ -[NPTMetadataEvent initWithCoder:]
+ -[NPTPerformanceTestConfiguration encodeWithCoder:]
+ -[NPTPerformanceTestConfiguration initWithCoder:]
+ GCC_except_table54
+ _NSClassFromString
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_RPCompanionLinkClient
+ _OBJC_CLASS_$_RPCompanionLinkDevice
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _PROTOCOLS__TtC6NPTKit31NetworkPerformanceTesterDClient.25
+ __Block_copy
+ __Block_release
+ __DATA__TtC6NPTKit18NPTDRapportManager
+ __DATA__TtC6NPTKit31NetworkPerformanceTesterDClient
+ __DATA__TtC6NPTKit37NetworkPerformanceTesterDRemoteClient
+ __INSTANCE_METHODS__TtC6NPTKit31NetworkPerformanceTesterDClient
+ __IVARS__TtC6NPTKit18NPTDRapportManager
+ __IVARS__TtC6NPTKit31NetworkPerformanceTesterDClient
+ __IVARS__TtC6NPTKit37NetworkPerformanceTesterDRemoteClient
+ __METACLASS_DATA__TtC6NPTKit18NPTDRapportManager
+ __METACLASS_DATA__TtC6NPTKit31NetworkPerformanceTesterDClient
+ __METACLASS_DATA__TtC6NPTKit37NetworkPerformanceTesterDRemoteClient
+ __OBJC_$_CLASS_METHODS_NPTMetadataEvent
+ __OBJC_$_CLASS_PROP_LIST_NPTMetadataEvent
+ __OBJC_$_CLASS_PROP_LIST_NPTPerformanceTestConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_NPTMetadataEvent
+ __PROTOCOLS__TtC6NPTKit31NetworkPerformanceTesterDClient
+ __PROTOCOL_INSTANCE_METHODS__TtP6NPTKit12NPTDServices_
+ __PROTOCOL_METHOD_TYPES__TtP6NPTKit12NPTDServices_
+ __PROTOCOL__TtP6NPTKit12NPTDServices_
+ ___block_descriptor_56_e8_32s40bs48w_e35_v24?0"NPTPingResult"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs48w_e37_v24?0"NPTMetricResult"8"NSError"16l
+ ___chkstk_darwin
+ ___copy_helper_block_e8_32s40b48w
+ ___destroy_helper_block_e8_32s40s48w
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_errno_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_math_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_signal_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_stdio_$_NPTKit
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swift_time_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftsys_time_$_NPTKit
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_FORCE_LOAD_$_swiftunistd_$_NPTKit
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _associated conformance 6NPTKit15NPTDRequestTypeOSHAASQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _bzero
+ _flat unique 6NPTKit12NPTDServices_p
+ _malloc_size
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$classForCoder
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_opt_self
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
+ _symbolic $s6NPTKit12NPTDServicesP
+ _symbolic $sSY
+ _symbolic IeAgH_
+ _symbolic Ieg_
+ _symbolic IeghH_
+ _symbolic SDySSypG
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic SDy_____ypGABSgA2C______pSgIegggg_Iegggg_ s11AnyHashableV s5ErrorP
+ _symbolic SDy_____ypGABSgA2C______pSgytIegnnnr_ytIegnnnr_ s11AnyHashableV s5ErrorP
+ _symbolic SDy_____ypGABSgIeggg_ s11AnyHashableV
+ _symbolic SDy_____ypGABSgytIegnnr_ s11AnyHashableV
+ _symbolic SDy_____ypGSgAC______pSgIegggg_ s11AnyHashableV s5ErrorP
+ _symbolic SDy_____ypGSgAC______pSgytIegnnnr_ s11AnyHashableV s5ErrorP
+ _symbolic SDy_____ypGSg_Say______pGSgt s11AnyHashableV s5ErrorP
+ _symbolic SS
+ _symbolic SS_ypt
+ _symbolic SaySo21RPCompanionLinkDeviceCG
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic SayypG
+ _symbolic ScA_pSg
+ _symbolic ScCySDy_____ypGSg_Say______pGSgt_____G s11AnyHashableV s5ErrorP s5NeverO
+ _symbolic ScCySo10NPTResultsCSg_Say______pGSgt_____G s5ErrorP s5NeverO
+ _symbolic ScCyyt______pG s5ErrorP
+ _symbolic ScPSg
+ _symbolic SccySi_SSt_____G s5NeverO
+ _symbolic SccySo12NSFileHandleC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic ShySo21RPCompanionLinkClientCG
+ _symbolic Si
+ _symbolic SiSSIegyg_
+ _symbolic SiSo8NSStringCIeyByy_
+ _symbolic So10NPTResultsCSgSo7NSArrayCSgIeyByy_
+ _symbolic So10NPTResultsCSg_Say______pGSgt s5ErrorP
+ _symbolic So10NPTResultsCm
+ _symbolic So12NSDictionaryCSgACSo7NSErrorCSgIeyByyy_
+ _symbolic So12NSFileHandleCSgSo7NSErrorCSgIeyByy_
+ _symbolic So12NSFileHandleCSg______pSgIeggg_ s5ErrorP
+ _symbolic So15NSXPCConnectionC
+ _symbolic So21RPCompanionLinkClientC
+ _symbolic So21RPCompanionLinkDeviceC
+ _symbolic So21RPCompanionLinkDeviceCIegg_
+ _symbolic So21RPCompanionLinkDeviceCSg
+ _symbolic So21RPCompanionLinkDeviceCytIegnr_
+ _symbolic So7NSArrayC
+ _symbolic So7NSArrayCm
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So7NSErrorCm
+ _symbolic So8NSObjectCSg
+ _symbolic So8NSStringC
+ _symbolic _____ 6NPTKit15NPTDRequestTypeO
+ _symbolic _____ 6NPTKit18NPTDRapportManagerC
+ _symbolic _____ 6NPTKit19NPTDRemoteConstantsO
+ _symbolic _____ 6NPTKit31NetworkPerformanceTesterDClientC
+ _symbolic _____ 6NPTKit37NetworkPerformanceTesterDRemoteClientC
+ _symbolic _____ So12_NPTTestTypeV
+ _symbolic _____ s6UInt32V
+ _symbolic _____SgXw 6NPTKit18NPTDRapportManagerC
+ _symbolic _____SgXw 6NPTKit37NetworkPerformanceTesterDRemoteClientC
+ _symbolic _____SgXwz_Xx 6NPTKit18NPTDRapportManagerC
+ _symbolic ______p 6NPTKit12NPTDServicesP
+ _symbolic ______p s5ErrorP
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____ySSSiG s18_DictionaryStorageC
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySo21RPCompanionLinkClientCG s11_SetStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s5ErrorP
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic ySDy_____ypGSg_AC______pSgtcSg s11AnyHashableV s5ErrorP
+ _symbolic ySDy_____ypGSg_Say______pGSgtcSg s11AnyHashableV s5ErrorP
+ _symbolic ySDy_____ypG_ABSgtcSg s11AnyHashableV
+ _symbolic ySDy_____ypG_ABSgyAC_AC______pSgtctcSg s11AnyHashableV s5ErrorP
+ _symbolic ySo10NPTResultsCSg_Say______pGSgtcSg s5ErrorP
+ _symbolic ySo14NPTSpeedMetricCSg______tcSg So12_NPTTestTypeV
+ _symbolic ySo16NPTMetadataEventCSg_______pSgtcSg s5ErrorP
+ _symbolic ySo21RPCompanionLinkDeviceCcSg
+ _symbolic yp
+ _symbolic ypSg
+ _symbolic ytIeAgHr_
+ _symbolic ytIegr_
+ _symbolic yycSg
+ block_copy_helper.1
+ block_copy_helper.102
+ block_copy_helper.103
+ block_copy_helper.107
+ block_copy_helper.114
+ block_copy_helper.12
+ block_copy_helper.19
+ block_copy_helper.30
+ block_copy_helper.36
+ block_copy_helper.38
+ block_copy_helper.5
+ block_copy_helper.61
+ block_copy_helper.65
+ block_copy_helper.69
+ block_copy_helper.73
+ block_copy_helper.76
+ block_copy_helper.81
+ block_copy_helper.87
+ block_copy_helper.89
+ block_copy_helper.9
+ block_copy_helper.91
+ block_copy_helper.93
+ block_copy_helper.95
+ block_copy_helper.96
+ block_copy_helper.99
+ block_descriptor.101
+ block_descriptor.104
+ block_descriptor.105
+ block_descriptor.109
+ block_descriptor.11
+ block_descriptor.116
+ block_descriptor.14
+ block_descriptor.21
+ block_descriptor.3
+ block_descriptor.32
+ block_descriptor.38
+ block_descriptor.40
+ block_descriptor.63
+ block_descriptor.67
+ block_descriptor.7
+ block_descriptor.71
+ block_descriptor.75
+ block_descriptor.78
+ block_descriptor.83
+ block_descriptor.89
+ block_descriptor.91
+ block_descriptor.93
+ block_descriptor.95
+ block_descriptor.97
+ block_descriptor.98
+ block_destroy_helper.10
+ block_destroy_helper.100
+ block_destroy_helper.103
+ block_destroy_helper.104
+ block_destroy_helper.108
+ block_destroy_helper.115
+ block_destroy_helper.13
+ block_destroy_helper.2
+ block_destroy_helper.20
+ block_destroy_helper.31
+ block_destroy_helper.37
+ block_destroy_helper.39
+ block_destroy_helper.6
+ block_destroy_helper.62
+ block_destroy_helper.66
+ block_destroy_helper.70
+ block_destroy_helper.74
+ block_destroy_helper.77
+ block_destroy_helper.82
+ block_destroy_helper.88
+ block_destroy_helper.90
+ block_destroy_helper.92
+ block_destroy_helper.94
+ block_destroy_helper.96
+ block_destroy_helper.97
+ objectdestroy.33Tm
+ objectdestroy.3Tm
+ objectdestroy.44Tm
+ objectdestroy.60Tm
- +[NPTDLogger client]
- +[NPTDLogger daemon]
- +[NetworkPerformanceTesterDClient sharedInstance]
- -[NetworkPerformanceTesterDClient .cxx_destruct]
- -[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPacketCapture:]
- -[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPath:completionHandler:]
- -[NetworkPerformanceTesterDClient init]
- -[NetworkPerformanceTesterDClient testServiceWithArguments:completionHandler:]
- GCC_except_table55
- OBJC_IVAR_$_NetworkPerformanceTesterDClient.connection
- OBJC_IVAR_$_NetworkPerformanceTesterDClient.server
- _NSLog
- _OBJC_CLASS_$_NPTDLogger
- _OBJC_CLASS_$_NetworkPerformanceTesterDClient
- _OBJC_METACLASS_$_NPTDLogger
- _OBJC_METACLASS_$_NetworkPerformanceTesterDClient
- __OBJC_$_CLASS_METHODS_NPTDLogger
- __OBJC_$_CLASS_METHODS_NetworkPerformanceTesterDClient
- __OBJC_$_INSTANCE_METHODS_NetworkPerformanceTesterDClient
- __OBJC_$_INSTANCE_VARIABLES_NetworkPerformanceTesterDClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NPTDServices
- __OBJC_$_PROTOCOL_METHOD_TYPES_NPTDServices
- __OBJC_CLASS_PROTOCOLS_$_NetworkPerformanceTesterDClient
- __OBJC_CLASS_RO_$_NPTDLogger
- __OBJC_CLASS_RO_$_NetworkPerformanceTesterDClient
- __OBJC_LABEL_PROTOCOL_$_NPTDServices
- __OBJC_METACLASS_RO_$_NPTDLogger
- __OBJC_METACLASS_RO_$_NetworkPerformanceTesterDClient
- __OBJC_PROTOCOL_$_NPTDServices
- __OBJC_PROTOCOL_REFERENCE_$_NPTDServices
- ___39-[NetworkPerformanceTesterDClient init]_block_invoke
- ___39-[NetworkPerformanceTesterDClient init]_block_invoke_2
- ___39-[NetworkPerformanceTesterDClient init]_block_invoke_3
- ___49+[NetworkPerformanceTesterDClient sharedInstance]_block_invoke
- ___75-[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPacketCapture:]_block_invoke
- ___78-[NetworkPerformanceTesterDClient testServiceWithArguments:completionHandler:]_block_invoke
- ___84-[NetworkPerformanceTesterDClient getPrivilegedFileHandleForPath:completionHandler:]_block_invoke
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32bs_e21_v24?0q8"NSString"16l
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSFileHandle"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs56w_e35_v24?0"NPTPingResult"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs56w_e37_v24?0"NPTMetricResult"8"NSError"16l
- ___copy_helper_block_e8_32b
- ___copy_helper_block_e8_32s40s48b56w
- ___destroy_helper_block_e8_32s40s48s56w
- __block_literal_global.12
- __block_literal_global.17
- __block_literal_global.23
- _dispatch_once
- _objc_msgSend$getPrivilegedFileHandleForPacketCapture:
- _objc_msgSend$getPrivilegedFileHandleForPath:completionHandler:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$localizedFailureReason
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$setInterruptionHandler:
- _objc_msgSend$setInvalidationHandler:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$testServiceWithArguments:completionHandler:
- _sharedInstance
- sharedInstance.onceToken
CStrings:
+ "11BE"
+ "Activated send client to %@"
+ "Activated send client to %@ with error %@"
+ "Error on remote object proxy: %s %s"
+ "Event Response from %@ contains error %@"
+ "Event sent to %@"
+ "Identifier received does not match remote device identifier for this object"
+ "NPTDRemoteClient received a request %s - this is not currently supported"
+ "NetworkPerformanceTesterDRemoteClient activated with error: %@"
+ "NetworkPerformanceTesterDRemoteClient disconnected from remote"
+ "NetworkPerformanceTesterDRemoteClient found device %@"
+ "NetworkPerformanceTesterDRemoteClient lost device %@"
+ "Rapport client Found device %@"
+ "Rapport client Lost device %@"
+ "Rapport client activated"
+ "Rapport client activated with error: %@"
+ "Rapport received event %s"
+ "Rapport received request %@"
+ "Received response error: %@"
+ "Received response from %@"
+ "Received response from %s"
+ "Response from %@ contains error %@"
+ "Sending request %s to %@, device count %ld"
+ "Will send event to %@, device count %ld, event %@"
+ "Will send request to %@, device count %ld"
+ "_TtC6NPTKit18NPTDRapportManager"
+ "_TtC6NPTKit31NetworkPerformanceTesterDClient"
+ "_TtC6NPTKit37NetworkPerformanceTesterDRemoteClient"
+ "_TtP6NPTKit12NPTDServices_"
+ "activateWithCompletion:"
+ "activeDevices"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "classForCoder"
+ "com.apple.networkperformancetesterd.rapportWake"
+ "com.apple.nptkit"
+ "decodeInt32ForKey:"
+ "decodeInt64ForKey:"
+ "destinationDeviceDisconnected"
+ "destinationDeviceDiscoveredHandler"
+ "destinationDeviceLostHandler"
+ "deviceFoundHandler"
+ "deviceLostHandler"
+ "encodeInt32:forKey:"
+ "encodeInt64:forKey:"
+ "eventHandler"
+ "eventHandler dropping event %@"
+ "eventHandler dropping requestType %ld"
+ "eventHandler triggered in NPTDRemoteClient for event %@"
+ "eventHandler triggered in NPTDRemoteClient for sender event from %s"
+ "getPrivilegedFileHandleForPacketCaptureWithCompletionHandler:"
+ "idsDeviceIdentifier"
+ "initWithDictionary:"
+ "metadataCompletionHandler"
+ "metadataUpdateHandler"
+ "registerEventID:options:handler:"
+ "registerRequestID:options:handler:"
+ "remoteDevice"
+ "requestHandler"
+ "responseHandler"
+ "sendClients"
+ "sendEventID:event:options:completion:"
+ "sendRequestID:request:options:responseHandler:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setControlFlags:"
+ "setDestinationDevice:"
+ "setDeviceChangedHandler:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "setDisconnectHandler:"
+ "setServiceType:"
+ "startLocalPerformanceTestWith:completionHandler:"
+ "startMetadataCollection(updateHandler:)"
+ "startPerformanceTest(with:updateHandler:)"
+ "stopLocalPerformanceTest:"
+ "stopMetadataCollection()"
+ "stopPerformanceTest()"
+ "testCompletionHandler"
+ "testUpdateHandler"
+ "v16@?0@\"RPCompanionLinkDevice\"8"
+ "v20@?0@\"RPCompanionLinkDevice\"8I16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"NPTResults\"8@\"NSArray\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "v32@0:8@\"NPTPerformanceTestConfiguration\"16@?<v@?@\"NPTResults\"@\"NSArray\">24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">24"
- "%@: %@ %@\n"
- "@\"<NPTDServices>\""
- "@\"NSXPCConnection\""
- "Error on remote object proxy"
- "Interrupted"
- "Invalidated"
- "NPTDLogger"
- "NPTDServices"
- "NetworkPerformanceTesterDClient"
- "daemon"
- "getPrivilegedFileHandleForPacketCapture:"
- "sharedInstance"

```
