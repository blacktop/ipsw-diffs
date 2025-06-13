## CoreNFC

> `/System/Library/Frameworks/CoreNFC.framework/CoreNFC`

```diff

-342.4.1.0.0
-  __TEXT.__text: 0x27f00
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x1484
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x720
-  __TEXT.__cstring: 0x1f2e
-  __TEXT.__oslogstring: 0x23bb
-  __TEXT.__unwind_info: 0x880
-  __TEXT.__objc_classname: 0x332
-  __TEXT.__objc_methname: 0x34ea
-  __TEXT.__objc_methtype: 0x13bf
-  __TEXT.__objc_stubs: 0x2360
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x890
-  __DATA_CONST.__objc_classlist: 0xd8
+344.25.0.0.0
+  __TEXT.__text: 0x4536c
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x16dc
+  __TEXT.__const: 0xb68
+  __TEXT.__gcc_except_tab: 0x89c
+  __TEXT.__cstring: 0x35dd
+  __TEXT.__oslogstring: 0x2501
+  __TEXT.__swift5_typeref: 0x66b
+  __TEXT.__swift5_fieldmd: 0x6c0
+  __TEXT.__constg_swiftt: 0x7f8
+  __TEXT.__swift5_reflstr: 0x744
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__swift5_capture: 0x3b4
+  __TEXT.__swift5_assocty: 0x38
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__unwind_info: 0x2178
+  __TEXT.__eh_frame: 0xea0
+  __TEXT.__objc_classname: 0x422
+  __TEXT.__objc_methname: 0x3a1a
+  __TEXT.__objc_methtype: 0x164a
+  __TEXT.__objc_stubs: 0x2600
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7590
-  __DATA_CONST.__objc_selrefs: 0xcd0
-  __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0xb38
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0x840
+  __DATA_CONST.__objc_const: 0xa428
+  __DATA_CONST.__objc_selrefs: 0xdf8
+  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_classrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__cfstring: 0xf00
+  __AUTH_CONST.__objc_const: 0xc10
+  __AUTH_CONST.__const: 0x1be0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x718
+  __AUTH.__objc_data: 0xe38
+  __AUTH.__data: 0x780
+  __DATA.__objc_ivar: 0x13c
+  __DATA.__data: 0xfe0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x9b0
+  __DATA.__common: 0x2e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0BA36C07-4EDF-3670-8ED9-F18578FAB4B8
-  Functions: 651
-  Symbols:   2446
-  CStrings:  1268
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 5B4E444B-F1BB-37D2-9F95-1EB57AE31D3A
+  Functions: 1631
+  Symbols:   3258
+  CStrings:  1512
 
Symbols:
+ +[NFCCardSessionCallbackInterface interface]
+ +[NFCCardSessionInterface interface]
+ +[NFCFieldDetectSessionCallbacksInterface interface]
+ +[NFCPresentmentSuppression assertionWithAssertion:delegate:]
+ -[NFCHardwareManager _cleanupPresentmentAssertion]
+ -[NFCHardwareManager _queueSession:]
+ -[NFCHardwareManager dequeueSession:]
+ -[NFCHardwareManager didExpire]
+ -[NFCHardwareManager didFinishCooldown]
+ -[NFCHardwareManager isCardSessionEligibleWithCompletionHandler:]
+ -[NFCHardwareManager queueCardFieldDetectSession:completionHandler:]
+ -[NFCHardwareManager queueCardSession:sessionConfig:completionHandler:]
+ -[NFCHardwareManager releasePresentmentSuppression:completion:]
+ -[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]
+ -[NFCPresentmentSuppression .cxx_destruct]
+ -[NFCPresentmentSuppression assertion]
+ -[NFCPresentmentSuppression delegate]
+ -[NFCPresentmentSuppression externalHandle]
+ -[NFCPresentmentSuppression initWithAssertion:delegate:]
+ -[NFCPresentmentSuppression invalidate]
+ -[NFCPresentmentSuppression setDelegate:]
+ -[NFCPresentmentSuppression startAssertion:]
+ -[NFCPresentmentSuppression startCooldown:]
+ -[NFCSession remoteObjectProxyWithErrorHandler:]
+ GCC_except_table15
+ GCC_except_table2
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table52
+ GCC_except_table8
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_NFCCardSessionCallbackInterface
+ _OBJC_CLASS_$_NFCCardSessionInterface
+ _OBJC_CLASS_$_NFCFieldDetectSessionCallbacksInterface
+ _OBJC_CLASS_$_NFCPresentmentSuppression
+ _OBJC_CLASS_$_NFCardSessionConfig
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtC7CoreNFC21AssertionNotification
+ _OBJC_CLASS_$__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_NFCHardwareManager._presentmentSuppression
+ _OBJC_IVAR_$_NFCHardwareManager._presentmentSuppressionDelegate
+ _OBJC_IVAR_$_NFCHardwareManager._presentmentSuppressionLock
+ _OBJC_IVAR_$_NFCHardwareManager._queuedCoreNFCSessions
+ _OBJC_IVAR_$_NFCPresentmentSuppression._assertion
+ _OBJC_IVAR_$_NFCPresentmentSuppression._assertionTimer
+ _OBJC_IVAR_$_NFCPresentmentSuppression._cooldownTimer
+ _OBJC_IVAR_$_NFCPresentmentSuppression._delegate
+ _OBJC_IVAR_$_NFCPresentmentSuppression._externalHandle
+ _OBJC_IVAR_$_NFCPresentmentSuppression._timerQueue
+ _OBJC_METACLASS_$_NFCCardSessionCallbackInterface
+ _OBJC_METACLASS_$_NFCCardSessionInterface
+ _OBJC_METACLASS_$_NFCFieldDetectSessionCallbacksInterface
+ _OBJC_METACLASS_$_NFCPresentmentSuppression
+ _OBJC_METACLASS_$__TtC7CoreNFC21AssertionNotification
+ _OBJC_METACLASS_$__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ _OBJC_METACLASS_$__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __DATA__TtC7CoreNFC11CardSession
+ __DATA__TtC7CoreNFC14NFCCardSession
+ __DATA__TtC7CoreNFC21AssertionNotification
+ __DATA__TtC7CoreNFC29NFCPresentmentIntentAssertion
+ __DATA__TtC7CoreNFC35NFCPresentmentSuppressionController
+ __DATA__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ __DATA__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ __DATA__TtCC7CoreNFC11CardSession11EventStream
+ __DATA__TtCC7CoreNFC11CardSession4APDU
+ __DATA__TtCCC7CoreNFC11CardSession11EventStream8Iterator
+ __IVARS__TtC7CoreNFC11CardSession
+ __IVARS__TtC7CoreNFC14NFCCardSession
+ __IVARS__TtC7CoreNFC21AssertionNotification
+ __IVARS__TtC7CoreNFC29NFCPresentmentIntentAssertion
+ __IVARS__TtC7CoreNFC35NFCPresentmentSuppressionController
+ __IVARS__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ __IVARS__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ __IVARS__TtCC7CoreNFC11CardSession11EventStream
+ __IVARS__TtCC7CoreNFC11CardSession4APDU
+ __IVARS__TtCCC7CoreNFC11CardSession11EventStream8Iterator
+ __METACLASS_DATA__TtC7CoreNFC11CardSession
+ __METACLASS_DATA__TtC7CoreNFC14NFCCardSession
+ __METACLASS_DATA__TtC7CoreNFC21AssertionNotification
+ __METACLASS_DATA__TtC7CoreNFC29NFCPresentmentIntentAssertion
+ __METACLASS_DATA__TtC7CoreNFC35NFCPresentmentSuppressionController
+ __METACLASS_DATA__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ __METACLASS_DATA__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ __METACLASS_DATA__TtCC7CoreNFC11CardSession11EventStream
+ __METACLASS_DATA__TtCC7CoreNFC11CardSession4APDU
+ __METACLASS_DATA__TtCCC7CoreNFC11CardSession11EventStream8Iterator
+ __OBJC_$_CLASS_METHODS_NFCFieldDetectSessionCallbacksInterface
+ __OBJC_$_CLASS_METHODS_NFCPresentmentSuppression
+ __OBJC_$_INSTANCE_METHODS_NFCPresentmentSuppression
+ __OBJC_$_INSTANCE_METHODS__TtC7CoreNFC21AssertionNotification
+ __OBJC_$_INSTANCE_METHODS__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ __OBJC_$_INSTANCE_METHODS__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ __OBJC_$_INSTANCE_VARIABLES_NFCPresentmentSuppression
+ __OBJC_$_PROP_LIST_NFCFeliCaTag.155
+ __OBJC_$_PROP_LIST_NFCISO15693Tag.203
+ __OBJC_$_PROP_LIST_NFCISO7816Tag.167
+ __OBJC_$_PROP_LIST_NFCMiFareTag.117
+ __OBJC_$_PROP_LIST_NFCNDEFTag.142
+ __OBJC_$_PROP_LIST_NFCPresentmentSuppression
+ __OBJC_$_PROP_LIST_NFCReaderSession.317
+ __OBJC_$_PROP_LIST_NFCTag.207
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFCCardSessionCallbackInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFCCardSessionInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFCFieldDetectSessionCallbacks
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFCPresentmentSuppressionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSXPCProxyCreating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCProxyCreating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFCCardSessionCallbackInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFCCardSessionInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFCFieldDetectSessionCallbacks
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFCPresentmentSuppressionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCProxyCreating
+ __OBJC_$_PROTOCOL_REFS_NFCCardSessionCallbackInterface
+ __OBJC_$_PROTOCOL_REFS_NFCCardSessionInterface
+ __OBJC_$_PROTOCOL_REFS_NFCFieldDetectSessionCallbacks
+ __OBJC_$_PROTOCOL_REFS_NFCFieldDetectSessionInterface
+ __OBJC_CLASS_RO_$_NFCCardSessionCallbackInterface
+ __OBJC_CLASS_RO_$_NFCCardSessionInterface
+ __OBJC_CLASS_RO_$_NFCFieldDetectSessionCallbacksInterface
+ __OBJC_CLASS_RO_$_NFCPresentmentSuppression
+ __OBJC_LABEL_PROTOCOL_$_NFCCardSessionCallbackInterface
+ __OBJC_LABEL_PROTOCOL_$_NFCCardSessionInterface
+ __OBJC_LABEL_PROTOCOL_$_NFCFieldDetectSessionCallbacks
+ __OBJC_LABEL_PROTOCOL_$_NFCFieldDetectSessionInterface
+ __OBJC_LABEL_PROTOCOL_$_NFCPresentmentSuppressionDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCProxyCreating
+ __OBJC_METACLASS_RO_$_NFCCardSessionCallbackInterface
+ __OBJC_METACLASS_RO_$_NFCCardSessionInterface
+ __OBJC_METACLASS_RO_$_NFCFieldDetectSessionCallbacksInterface
+ __OBJC_METACLASS_RO_$_NFCPresentmentSuppression
+ __OBJC_PROTOCOL_$_NFCCardSessionCallbackInterface
+ __OBJC_PROTOCOL_$_NFCCardSessionInterface
+ __OBJC_PROTOCOL_$_NFCFieldDetectSessionCallbacks
+ __OBJC_PROTOCOL_$_NFCFieldDetectSessionInterface
+ __OBJC_PROTOCOL_$_NFCPresentmentSuppressionDelegate
+ __OBJC_PROTOCOL_$_NSXPCProxyCreating
+ __OBJC_PROTOCOL_REFERENCE_$_NFCCardSessionCallbackInterface
+ __OBJC_PROTOCOL_REFERENCE_$_NFCCardSessionInterface
+ __OBJC_PROTOCOL_REFERENCE_$_NFCFieldDetectSessionCallbacks
+ __OBJC_PROTOCOL_REFERENCE_$_NFCFieldDetectSessionInterface
+ __PROTOCOLS__TtC7CoreNFC21AssertionNotification
+ __PROTOCOLS__TtC7CoreNFC21AssertionNotification.2
+ __PROTOCOLS__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper
+ __PROTOCOLS__TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper.2
+ __PROTOCOLS__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate
+ __PROTOCOLS__TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate.2
+ ___31-[NFCHardwareManager didExpire]_block_invoke
+ ___31-[NFCHardwareManager didExpire]_block_invoke.75
+ ___31-[NFCHardwareManager didExpire]_block_invoke_2
+ ___36-[NFCHardwareManager _queueSession:]_block_invoke
+ ___37-[NFCHardwareManager dequeueSession:]_block_invoke
+ ___39-[NFCHardwareManager didFinishCooldown]_block_invoke
+ ___43-[NFCPresentmentSuppression startCooldown:]_block_invoke
+ ___43-[NFCReaderSession beginSessionWithConfig:]_block_invoke.55
+ ___44-[NFCPresentmentSuppression startAssertion:]_block_invoke
+ ___50-[NFCHardwareManager _cleanupPresentmentAssertion]_block_invoke
+ ___50-[NFCHardwareManager _cleanupPresentmentAssertion]_block_invoke_2
+ ___50-[NFCHardwareManager _cleanupPresentmentAssertion]_block_invoke_3
+ ___55-[NFCNDEFReaderSession connectToTag:completionHandler:]_block_invoke.84
+ ___63-[NFCHardwareManager releasePresentmentSuppression:completion:]_block_invoke
+ ___63-[NFCHardwareManager releasePresentmentSuppression:completion:]_block_invoke.61
+ ___63-[NFCHardwareManager releasePresentmentSuppression:completion:]_block_invoke.62
+ ___63-[NFCHardwareManager releasePresentmentSuppression:completion:]_block_invoke_2
+ ___65-[NFCHardwareManager isCardSessionEligibleWithCompletionHandler:]_block_invoke
+ ___65-[NFCHardwareManager isCardSessionEligibleWithCompletionHandler:]_block_invoke_2
+ ___68-[NFCHardwareManager queueCardFieldDetectSession:completionHandler:]_block_invoke
+ ___68-[NFCHardwareManager queueCardFieldDetectSession:completionHandler:]_block_invoke_2
+ ___71-[NFCHardwareManager queueCardSession:sessionConfig:completionHandler:]_block_invoke
+ ___71-[NFCHardwareManager queueCardSession:sessionConfig:completionHandler:]_block_invoke_2
+ ___75-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]_block_invoke
+ ___75-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]_block_invoke.50
+ ___75-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]_block_invoke.52
+ ___75-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:]_block_invoke_2
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.158
+ ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.161
+ ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_64_e8_32s40s48bs_e41_v24?0"NFAssertionInternal"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e78_v28?0"NSObject<NFCCardSessionInterface><NSXPCProxyCreating>"8B16"NSError"20ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e82_v24?0"NSObject<NFCFieldDetectSessionInterface><NSXPCProxyCreating>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_8?0ls32l8s40l8r48l8
+ ___block_literal_global.73
+ ___block_literal_global.93
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_memcpy32_8
+ ___swift_memcpy40_8
+ ___swift_memcpy48_8
+ ___swift_memcpy56_8
+ ___swift_memcpy8_8
+ ___swift_memcpy9_8
+ ___swift_noop_void_return
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ ___unnamed_1
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftCoreNFC
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CoreNFC
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CoreNFC
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 7CoreNFC11CardSessionC11EventStreamCSciAA13AsyncIteratorSci_ScI
+ _associated conformance 7CoreNFC11CardSessionC17EmulationUIStatusOSHAASQ
+ _associated conformance 7CoreNFC11CardSessionC5ErrorOSHAASQ
+ _associated conformance 7CoreNFC14NFCCardSessionC5ErrorOSHAASQ
+ _associated conformance 7CoreNFC29NFCPresentmentIntentAssertionC5ErrorOSHAASQ
+ _associated conformance 7CoreNFC35NFCPresentmentSuppressionControllerC5EventOSHAASQ
+ _block_copy_helper
+ _block_copy_helper.113
+ _block_copy_helper.119
+ _block_copy_helper.128
+ _block_copy_helper.134
+ _block_copy_helper.14
+ _block_copy_helper.141
+ _block_copy_helper.148
+ _block_copy_helper.15
+ _block_copy_helper.159
+ _block_copy_helper.16
+ _block_copy_helper.20
+ _block_copy_helper.21
+ _block_copy_helper.26
+ _block_copy_helper.27
+ _block_copy_helper.32
+ _block_copy_helper.33
+ _block_copy_helper.38
+ _block_copy_helper.39
+ _block_copy_helper.4
+ _block_copy_helper.44
+ _block_copy_helper.45
+ _block_copy_helper.50
+ _block_copy_helper.51
+ _block_copy_helper.53
+ _block_copy_helper.57
+ _block_copy_helper.59
+ _block_copy_helper.63
+ _block_copy_helper.65
+ _block_copy_helper.70
+ _block_copy_helper.71
+ _block_copy_helper.76
+ _block_copy_helper.77
+ _block_copy_helper.8
+ _block_copy_helper.82
+ _block_copy_helper.89
+ _block_copy_helper.9
+ _block_copy_helper.92
+ _block_descriptor
+ _block_descriptor.10
+ _block_descriptor.11
+ _block_descriptor.115
+ _block_descriptor.121
+ _block_descriptor.130
+ _block_descriptor.136
+ _block_descriptor.143
+ _block_descriptor.150
+ _block_descriptor.16
+ _block_descriptor.161
+ _block_descriptor.17
+ _block_descriptor.18
+ _block_descriptor.22
+ _block_descriptor.23
+ _block_descriptor.28
+ _block_descriptor.29
+ _block_descriptor.34
+ _block_descriptor.35
+ _block_descriptor.40
+ _block_descriptor.41
+ _block_descriptor.46
+ _block_descriptor.47
+ _block_descriptor.52
+ _block_descriptor.53
+ _block_descriptor.55
+ _block_descriptor.59
+ _block_descriptor.6
+ _block_descriptor.61
+ _block_descriptor.65
+ _block_descriptor.67
+ _block_descriptor.72
+ _block_descriptor.73
+ _block_descriptor.78
+ _block_descriptor.79
+ _block_descriptor.84
+ _block_descriptor.91
+ _block_descriptor.94
+ _block_destroy_helper
+ _block_destroy_helper.10
+ _block_destroy_helper.114
+ _block_destroy_helper.120
+ _block_destroy_helper.129
+ _block_destroy_helper.135
+ _block_destroy_helper.142
+ _block_destroy_helper.149
+ _block_destroy_helper.15
+ _block_destroy_helper.16
+ _block_destroy_helper.160
+ _block_destroy_helper.17
+ _block_destroy_helper.21
+ _block_destroy_helper.22
+ _block_destroy_helper.27
+ _block_destroy_helper.28
+ _block_destroy_helper.33
+ _block_destroy_helper.34
+ _block_destroy_helper.39
+ _block_destroy_helper.40
+ _block_destroy_helper.45
+ _block_destroy_helper.46
+ _block_destroy_helper.5
+ _block_destroy_helper.51
+ _block_destroy_helper.52
+ _block_destroy_helper.54
+ _block_destroy_helper.58
+ _block_destroy_helper.60
+ _block_destroy_helper.64
+ _block_destroy_helper.66
+ _block_destroy_helper.71
+ _block_destroy_helper.72
+ _block_destroy_helper.77
+ _block_destroy_helper.78
+ _block_destroy_helper.83
+ _block_destroy_helper.9
+ _block_destroy_helper.90
+ _block_destroy_helper.93
+ _free
+ _interface.interface.90
+ _interface.onceToken.91
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_cleanupPresentmentAssertion
+ _objc_msgSend$_queueSession:
+ _objc_msgSend$assertion
+ _objc_msgSend$assertionWithAssertion:delegate:
+ _objc_msgSend$dequeueSession:
+ _objc_msgSend$didExpire
+ _objc_msgSend$didFinishCooldown
+ _objc_msgSend$externalHandle
+ _objc_msgSend$initWithAssertion:delegate:
+ _objc_msgSend$initialUIText
+ _objc_msgSend$isCardSessionEligibleWithCompletion:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$queueCardFieldDetectSession:completion:
+ _objc_msgSend$queueCardSession:sessionConfig:completion:
+ _objc_msgSend$releasePresentmentSuppression:completion:
+ _objc_msgSend$releaseSuppressPresentmentAssertion:completion:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$requestSuppressPresentmentWithCompletion:
+ _objc_msgSend$startAssertion:
+ _objc_msgSend$startCooldown:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_opt_self
+ _objc_release_x2
+ _objectdestroy.24Tm
+ _swift_allocError
+ _swift_allocObject
+ _swift_allocateGenericValueMetadata
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getGenericMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_stdlib_random
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _swift_willThrow
+ _symbolic $s7CoreNFC27NFCTagReaderSessionDelegateP
+ _symbolic $sScI
+ _symbolic $sSci
+ _symbolic BD
+ _symbolic SS
+ _symbolic SaySiG
+ _symbolic Say_____GSg 10Foundation4DataV
+ _symbolic Sb
+ _symbolic Sb5state_t
+ _symbolic ScPSg
+ _symbolic ScSy_____G 7CoreNFC11CardSessionC5EventO
+ _symbolic ScSy_____G 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic ScSy_____G 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic SccySb_____G s5NeverO
+ _symbolic SccySo8NSNumberC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic Sccyyt______pGSg s5ErrorP
+ _symbolic Sd
+ _symbolic Si
+ _symbolic So12NFCFeliCaTag_p
+ _symbolic So12NFCMiFareTag_p
+ _symbolic So13NFCISO7816Tag_p
+ _symbolic So14NFCISO15693Tag_p
+ _symbolic So18NSXPCProxyCreating_p
+ _symbolic So23NFCCardSessionInterface_p
+ _symbolic So30NFCFieldDetectSessionInterface_p
+ _symbolic So6NFCTag_p
+ _symbolic So7NFTimerCSg
+ _symbolic So8NSNumberCSg
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic Su
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 7CoreNFC10XPCSessionV
+ _symbolic _____ 7CoreNFC11CardSessionC
+ _symbolic _____ 7CoreNFC11CardSessionC11EventStreamC
+ _symbolic _____ 7CoreNFC11CardSessionC11EventStreamC8IteratorC
+ _symbolic _____ 7CoreNFC11CardSessionC17EmulationUIStatusO
+ _symbolic _____ 7CoreNFC11CardSessionC4APDUC
+ _symbolic _____ 7CoreNFC11CardSessionC5ErrorO
+ _symbolic _____ 7CoreNFC11CardSessionC5EventO
+ _symbolic _____ 7CoreNFC14NFCCardSessionC
+ _symbolic _____ 7CoreNFC14NFCCardSessionC5ErrorO
+ _symbolic _____ 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic _____ 7CoreNFC16NFCAtomicWrapperV
+ _symbolic _____ 7CoreNFC19NFCFeliCaStatusFlagV
+ _symbolic _____ 7CoreNFC21AssertionNotificationC
+ _symbolic _____ 7CoreNFC21NFCISO15693SystemInfoV
+ _symbolic _____ 7CoreNFC22NFCCardSessionDelegate33_EFB2E886CAEE49EE896FB2304411A556LLC
+ _symbolic _____ 7CoreNFC22NFCISO7816ResponseAPDUV
+ _symbolic _____ 7CoreNFC24NFCFeliCaPollingResponseV
+ _symbolic _____ 7CoreNFC29NFCPresentmentIntentAssertionC
+ _symbolic _____ 7CoreNFC29NFCPresentmentIntentAssertionC5ErrorO
+ _symbolic _____ 7CoreNFC33NFCFeliCaRequsetServiceV2ResponseV
+ _symbolic _____ 7CoreNFC35NFCPresentmentSuppressionControllerC
+ _symbolic _____ 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic _____ 7CoreNFC38NFCISO15693MultipleBlockSecurityStatusV
+ _symbolic _____ 7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapperC
+ _symbolic _____ 7CoreNFC44NFCFeliCaRequestSpecificationVersionResponseV
+ _symbolic _____ 7CoreNFC6NFCTagO
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ So21NFCFeliCaEncryptionIdV
+ _symbolic _____ So23NFCISO15693ResponseFlagV
+ _symbolic _____ s5UInt8V
+ _symbolic _____ s6UInt32V
+ _symbolic _____5error_t 7CoreNFC14NFCCardSessionC5ErrorO
+ _symbolic _____6reason_t 7CoreNFC11CardSessionC5ErrorO
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 10Foundation6LocaleV
+ _symbolic _____Sg 7CoreNFC11CardSessionC4APDUC
+ _symbolic _____Sg 7CoreNFC14NFCCardSessionC5ErrorO
+ _symbolic _____Sg 7CoreNFC22NFCCardSessionDelegate33_EFB2E886CAEE49EE896FB2304411A556LLC
+ _symbolic _____Sg5error_t 7CoreNFC14NFCCardSessionC5ErrorO
+ _symbolic _____SgXw 7CoreNFC14NFCCardSessionC
+ _symbolic _____SgXwz_Xx 7CoreNFC14NFCCardSessionC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic ______pSgXw 7CoreNFC27NFCTagReaderSessionDelegateP
+ _symbolic _____ySSG 7CoreNFC16NFCAtomicWrapperV
+ _symbolic _____ySS_____G s13ManagedBufferC So16os_unfair_lock_sV
+ _symbolic _____ySay_____G______pGIegg_ s6ResultO 10Foundation4DataV s5ErrorP
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferC So16os_unfair_lock_sV
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySi______pGIegg_ s6ResultO s5ErrorP
+ _symbolic _____ySo23NFCCardSessionInterface_pGSg 7CoreNFC10XPCSessionV
+ _symbolic _____ySo30NFCFieldDetectSessionInterface_pGSg 7CoreNFC10XPCSessionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7CoreNFC6NFCTagO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y______G ScS12ContinuationV 7CoreNFC11CardSessionC5EventO
+ _symbolic _____y______G ScS12ContinuationV 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic _____y______G ScS12ContinuationV 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic _____y______G ScS8IteratorV 7CoreNFC11CardSessionC5EventO
+ _symbolic _____y______G ScS8IteratorV 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic _____y______G ScS8IteratorV 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic _____y______Say_____Gt______pGIegn_ s6ResultO 7CoreNFC19NFCFeliCaStatusFlagV 10Foundation4DataV s5ErrorP
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 7CoreNFC11CardSessionC5EventO
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 7CoreNFC11CardSessionC5EventO
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 7CoreNFC14NFCCardSessionC5EventO
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO 7CoreNFC35NFCPresentmentSuppressionControllerC5EventO
+ _symbolic _____y___________Sgt______pGIegg_ s6ResultO So23NFCISO15693ResponseFlagV 10Foundation4DataV s5ErrorP
+ _symbolic _____y___________pGIegg_ s6ResultO 10Foundation4DataV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC19NFCFeliCaStatusFlagV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC21NFCISO15693SystemInfoV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC22NFCISO7816ResponseAPDUV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC24NFCFeliCaPollingResponseV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC33NFCFeliCaRequsetServiceV2ResponseV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC38NFCISO15693MultipleBlockSecurityStatusV s5ErrorP
+ _symbolic _____y___________pGIegn_ s6ResultO 7CoreNFC44NFCFeliCaRequestSpecificationVersionResponseV s5ErrorP
+ _symbolic _____y___________t______pGIegg_ s6ResultO So23NFCISO15693ResponseFlagV 10Foundation4DataV s5ErrorP
+ _symbolic _____yxG 2os21OSAllocatedUnfairLockV
+ _symbolic x
+ _symbolic ySuYbc
+ _symbolic y___________tYaYbKc 10Foundation4DataV 7CoreNFC11CardSessionC4APDUC
+ _symbolic ytIeghHr_
- -[NFCHardwareManager dequeueReaderSession:]
- GCC_except_table10
- GCC_except_table7
- _OBJC_IVAR_$_NFCHardwareManager._queuedReaderSessions
- __OBJC_$_PROP_LIST_NFCFeliCaTag.154
- __OBJC_$_PROP_LIST_NFCISO15693Tag.202
- __OBJC_$_PROP_LIST_NFCISO7816Tag.154
- __OBJC_$_PROP_LIST_NFCMiFareTag.116
- __OBJC_$_PROP_LIST_NFCNDEFTag.141
- __OBJC_$_PROP_LIST_NFCReaderSession.315
- __OBJC_$_PROP_LIST_NFCTag.206
- ___43-[NFCHardwareManager dequeueReaderSession:]_block_invoke
- ___43-[NFCReaderSession beginSessionWithConfig:]_block_invoke.54
- ___55-[NFCNDEFReaderSession connectToTag:completionHandler:]_block_invoke.83
- ___73-[NFCHardwareManager queueReaderSession:sessionConfig:completionHandler:]_block_invoke_3
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.155
- ___85-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:]_block_invoke.156
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_literal_global.36
- ___block_literal_global.66
- _interface.interface.63
- _interface.onceToken.64
- _objc_msgSend$dequeueReaderSession:
CStrings:
+ "\x04\x11"
+ "$defaultActor"
+ "%c[%{public}s %{public}s]:%i De-assert error=%@"
+ "%c[%{public}s %{public}s]:%i Drop XPC interrupt callback"
+ "%c[%{public}s %{public}s]:%i Invalid handle"
+ "%c[%{public}s %{public}s]:%i Resource unavailable"
+ "%c[%{public}s %{public}s]:%i XPC error=%@"
+ "%c[%{public}s %{public}s]:%i error=%{public}@"
+ "%c[%{public}s %{public}s]:%i expired"
+ "%c[%{public}s %{public}s]:%i handle=%lu"
+ "%s"
+ "%s: %ld: assertion expired"
+ "%s: %ld: cooldown completed"
+ "%s:%d"
+ "%s:%ld:"
+ "%s:%ld: %s"
+ "%s:%ld: Emulation has not started"
+ "%s:%ld: RF=%{bool}d, emuStarted=%{bool}d, currentFieldState=%{bool}d"
+ "%s:%ld: Session expired"
+ "%s:%ld: Session has been invalidated"
+ "%s:%ld: Stopping emulation"
+ "%s:%ld: Unexpected APDU)"
+ "%s:%ld: capdu=%s"
+ "%s:%ld: connected, currentFieldState=%{bool}d"
+ "%s:%ld: disconnected, currentFieldState=%{bool}d"
+ "%s:%ld: disconnected, emuStarted=%{bool}d"
+ "%s:%ld: error=%s"
+ "%s:%ld: fdSession=%{bool}d, cardSession=%{bool}d, reason=%s"
+ "%s:%ld: fieldChange=%{bool}d"
+ "%s:%ld: fieldPresent=%{bool}d"
+ "%s:%ld: handle=%llu"
+ "%s:%ld: invalidated, error=%s"
+ "%s:%ld: sent=%s"
+ "%s:%ld: started, error=%s"
+ "%s:%ld: xpcError=%@"
+ ", initialUIText=%@"
+ ": Received new APDU without responding"
+ ": Resource error"
+ "@\"NFAssertionInternal\""
+ "@\"NFCPresentmentSuppression\""
+ "@\"NSObject<NFCPresentmentSuppressionDelegate>\""
+ "@24@0:8@?<v@?@\"NSError\">16"
+ "@8@?0"
+ "Card session is not supported on this device"
+ "CardSession has previously started"
+ "CardSession is not supported on this device"
+ "CoreNFC.AssertionNotification"
+ "CoreNFC.NFCCardSessionDelegate"
+ "CoreNFC.NFCTagReaderSessionDelegateSwiftWrapper"
+ "CoreNFC/CardSession.swift"
+ "CoreNFC/NFCCardSession.swift"
+ "CoreNFC/NFCISO15693Tag.swift"
+ "CoreNFC/NFCPresentmentSuppression+Swift.swift"
+ "CoreNFC/NFCTag.swift"
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Emulation has been previously started"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Invalid Parameter"
+ "Line"
+ "Method"
+ "Missing assertion"
+ "NFCCardSessionCallbackInterface"
+ "NFCCardSessionInterface"
+ "NFCFieldDetectSessionCallbacks"
+ "NFCFieldDetectSessionCallbacksInterface"
+ "NFCFieldDetectSessionInterface"
+ "NFCPresentmentSuppression"
+ "NFCPresentmentSuppressionController is not supported on this device"
+ "NFCPresentmentSuppressionDelegate"
+ "NSArray element failed to match the Swift Array Element type\nExpected "
+ "NSXPCProxyCreating"
+ "Negative value is not representable"
+ "No resources"
+ "Not enough bits to represent the passed value"
+ "Response is empty"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NFAssertionInternal\",R,N,V_assertion"
+ "T@\"NSNumber\",R,N,V_externalHandle"
+ "T@\"NSObject<NFCPresentmentSuppressionDelegate>\",N,V_delegate"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Unsupported type"
+ "Vv24@0:8@?<v@?@\"NFAssertionInternal\"@\"NSError\">16"
+ "Vv24@0:8@?<v@?Q@\"NSError\">16"
+ "Vv32@0:8@\"NFAssertionInternal\"16@?<v@?@\"NSError\">24"
+ "Vv32@0:8@\"NSObject<NFCFieldDetectSessionCallbacks>\"16@?<v@?@\"NSObject<NFCFieldDetectSessionInterface>\"@\"NSError\">24"
+ "Vv40@0:8@\"NSObject<NFCCardSessionCallbackInterface>\"16@\"NFCardSessionConfig\"24@?<v@?@\"NSObject<NFCCardSessionInterface>\"B@\"NSError\">32"
+ "_TtC7CoreNFC11CardSession"
+ "_TtC7CoreNFC14NFCCardSession"
+ "_TtC7CoreNFC21AssertionNotification"
+ "_TtC7CoreNFC29NFCPresentmentIntentAssertion"
+ "_TtC7CoreNFC35NFCPresentmentSuppressionController"
+ "_TtC7CoreNFC39NFCTagReaderSessionDelegateSwiftWrapper"
+ "_TtC7CoreNFCP33_EFB2E886CAEE49EE896FB2304411A55622NFCCardSessionDelegate"
+ "_TtCC7CoreNFC11CardSession11EventStream"
+ "_TtCC7CoreNFC11CardSession4APDU"
+ "_TtCCC7CoreNFC11CardSession11EventStream8Iterator"
+ "_assertion"
+ "_assertionTimer"
+ "_cleanupPresentmentAssertion"
+ "_cooldownTimer"
+ "_externalHandle"
+ "_presentmentSuppression"
+ "_presentmentSuppressionDelegate"
+ "_presentmentSuppressionLock"
+ "_queueSession:"
+ "_queuedCoreNFCSessions"
+ "_timerQueue"
+ "_uiString"
+ "a"
+ "assertion"
+ "assertionController"
+ "assertionHandle"
+ "assertionWithAssertion:delegate:"
+ "asyncProxyExecute(_:)"
+ "cardSession"
+ "cardSessionDelegate"
+ "com.apple.corenfc.presentment.suppression.timer"
+ "configWithInitialUIText:"
+ "deinitHandler"
+ "delegateEventStream"
+ "delegateEventStreamContinuation"
+ "dequeueSession:"
+ "didConnectToReader"
+ "didConnectToReader()"
+ "didDetectField(_:)"
+ "didDetectField:"
+ "didDisconnectFromReader"
+ "didDisconnectFromReader()"
+ "didExpire"
+ "didFinishCooldown"
+ "didReceiveAPDU:"
+ "emulationExpirationTimer"
+ "emulationTimeLimit"
+ "eventStream"
+ "eventStreamContinuation"
+ "externalHandle"
+ "fieldChanged(_:)"
+ "fieldChanged:"
+ "fieldDetectDelegate"
+ "fieldDetectSession"
+ "handle(receivedAPDU:)"
+ "handle(receivedAPDU:):"
+ "handleApduDeinit(sequenceNumber:)"
+ "handleReaderDisconnect()"
+ "handleSendAPDU(apdu:requestor:)"
+ "handleSendAPDU(apdu:requestor:): Invalid APDU response send request received"
+ "hasResponded"
+ "i"
+ "init()"
+ "initWithAssertion:delegate:"
+ "initialUIText"
+ "integerValue"
+ "invalid Collection: less than 'count' elements in collection"
+ "invalidate(reason:)"
+ "isCardSessionEligibleWithCompletion:"
+ "isCardSessionEligibleWithCompletionHandler:"
+ "iterator"
+ "lastReceivedAPDU"
+ "lengthOfBytesUsingEncoding:"
+ "nfcCardSession"
+ "nfcEventStream"
+ "nfcEventStreamContinuation"
+ "notification"
+ "payloadHash"
+ "protectedValidState"
+ "queueCardFieldDetectSession:completion:"
+ "queueCardFieldDetectSession:completionHandler:"
+ "queueCardSession:sessionConfig:completion:"
+ "queueCardSession:sessionConfig:completionHandler:"
+ "releasePresentmentSuppression:completion:"
+ "releaseSuppressPresentmentAssertion:completion:"
+ "remoteObjectProxyWithErrorHandler:"
+ "requestPresentmentSuppressionWithDelegate:completion:"
+ "requestSuppressPresentmentWithCompletion:"
+ "sendAPDU:completion:"
+ "sendHandler"
+ "sequenceNumber"
+ "sessionStartContinuation"
+ "setDelegate:"
+ "startAssertion:"
+ "startCooldown:"
+ "startDelegateEventMonitor()"
+ "startEmulation()"
+ "startEmulation():"
+ "startEmulationTimer()"
+ "startEmulationWithCompletion:"
+ "stopEmulationWithStatus:completion:"
+ "stream"
+ "stringWithFormat:"
+ "swiftDelegate"
+ "unsignedIntegerValue"
+ "unsignedLongLongValue"
+ "updateUIString:completion:"
+ "v20@0:8B16"
+ "v24@0:8@\"NSData\"16"
+ "v24@?0@\"<NFCFieldDetectSessionInterface><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0@\"NFAssertionInternal\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSObject<NFCFieldDetectSessionInterface><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v24@?0Q8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\">20"
+ "v28@?0@\"NSObject<NFCCardSessionInterface><NSXPCProxyCreating>\"8B16@\"NSError\"20"
+ "v28@?0C8@\"NSData\"12@\"NSError\"20"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?>24"
+ "v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0@\"NSData\"8C16C20@\"NSError\"24"
+ "v32@?0q8q16@\"NSError\"24"
+ "v36@?0@\"<NFCCardSessionInterface><NSXPCProxyCreating>\"8B16@\"NSNumber\"20@\"NSError\"28"
+ "v40@?0q8q16@\"NSArray\"24@\"NSError\"32"
+ "v48@?0q8q16@\"NSData\"24@\"NSData\"32@\"NSError\"40"
+ "v56@?0q8q16q24@\"NSArray\"32@\"NSArray\"40@\"NSError\"48"
- "\x04"
- "%c[%{public}s %{public}s]:%i error=%@"
- "_queuedReaderSessions"
- "dequeueReaderSession:"

```
