## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-767.4.1.0.0
-  __TEXT.__text: 0x56f28
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x68f8
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x1470
+778.5.1.0.0
+  __TEXT.__text: 0x62a18
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_methlist: 0x6970
+  __TEXT.__const: 0x160
+  __TEXT.__swift5_typeref: 0xef
+  __TEXT.__cstring: 0x30d9
+  __TEXT.__swift5_capture: 0xa4
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0x1550
   __TEXT.__oslogstring: 0x4186
-  __TEXT.__cstring: 0x2d97
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x1de0
-  __TEXT.__objc_classname: 0x1054
-  __TEXT.__objc_methname: 0xba7c
-  __TEXT.__objc_methtype: 0x259a
-  __TEXT.__objc_stubs: 0x85a0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x13b8
+  __TEXT.__unwind_info: 0x2e48
+  __TEXT.__eh_frame: 0xc70
+  __TEXT.__objc_classname: 0x1055
+  __TEXT.__objc_methname: 0xbb7a
+  __TEXT.__objc_methtype: 0x25aa
+  __TEXT.__objc_stubs: 0x8640
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x13f8
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xab48
-  __DATA_CONST.__objc_selrefs: 0x2c38
-  __AUTH_CONST.__const: 0xa78
-  __AUTH_CONST.__cfstring: 0x4bc0
+  __DATA_CONST.__objc_const: 0xabf8
+  __DATA_CONST.__objc_selrefs: 0x2c78
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x560
+  __DATA_CONST.__objc_superrefs: 0x378
+  __AUTH_CONST.__const: 0xb68
+  __AUTH_CONST.__auth_ptr: 0x28
+  __AUTH_CONST.__cfstring: 0x4be0
   __AUTH_CONST.__objc_const: 0x3f88
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__auth_got: 0xca0
   __AUTH.__objc_data: 0x1040
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x560
-  __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0x19c
-  __DATA.__data: 0x1fb0
+  __DATA.__data: 0x21a8
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x580
+  __DATA_DIRTY.__objc_ivar: 0x594
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x4d8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2445
-  Symbols:   8514
-  CStrings:  3829
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 2620
+  Symbols:   8639
+  CStrings:  3865
 
Symbols:
+ -[HMFLocationAuthorization _mark]
+ -[HMFLocationAuthorization _requestAuthorization:completionHandler:]
+ -[HMFLocationAuthorization initWithScheduler:]
+ -[HMFNetworkDiagnostic runWithDelay:]
+ -[HMFNetworkDiagnosticPing delayFuture:]
+ -[HMFNetworkDiagnosticPing delayPromise]
+ -[HMFNetworkDiagnosticPing runWithDelay:]
+ -[HMFNetworkDiagnosticPing setDelayPromise:]
+ -[__HMFLocationAuthorizationRequest unregisterFromKVO]
+ -[__HMFLocationManagerOperation unregisterFromKVO]
+ _HMFProductInfoBorealisEOSVersion
+ _HMFProductInfoDawnEOSVersion
+ _HMFProductInfoLighthouseEOSVersion
+ _HMFProductInfoStarlightEOSVersion
+ _HMFProductInfoSunburstEOSVersion
+ __OBJC_$_CLASS_PROP_LIST_HMFWiFiManagerDataSource.108
+ __OBJC_$_PROP_LIST_HMFObject.57
+ __OBJC_$_PROP_LIST_HMFTimerManager.149
+ __OBJC_$_PROP_LIST_HMFTimerManagerTimerContext.68
+ __OBJC_$_PROP_LIST_HMFWiFiManagerDataSource.173
+ ___33-[HMFLocationAuthorization _mark]_block_invoke
+ ___40-[HMFNetworkDiagnosticPing delayFuture:]_block_invoke
+ ___41-[HMFNetworkDiagnosticPing runWithDelay:]_block_invoke
+ ___41-[HMFNetworkDiagnosticPing runWithDelay:]_block_invoke_2
+ ___41-[HMFNetworkDiagnosticPing runWithDelay:]_block_invoke_3
+ ___41-[HMFNetworkDiagnosticPing runWithDelay:]_block_invoke_4
+ ___45-[HMFLocationAuthorization registerObserver:]_block_invoke.54
+ ___54-[HMFLocationAuthorization locationOperationCompleted]_block_invoke
+ ___68-[HMFLocationAuthorization _requestAuthorization:completionHandler:]_block_invoke
+ ___68-[HMFLocationAuthorization _requestAuthorization:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e30_16?0"HMFNetworkDiagnostic"8lr32l8
+ ___block_descriptor_56_e8_32bs40w48w_e5_v8?0lw40l8s32l8w48l8
+ ___block_literal_global.130
+ ___block_literal_global.66
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_HMFoundation
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_HMFoundation
+ __swift_isClassOrObjCExistentialType
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memmove
+ _objc_msgSend$_mark
+ _objc_msgSend$_requestAuthorization:completionHandler:
+ _objc_msgSend$delayFuture:
+ _objc_msgSend$delayPromise
+ _objc_msgSend$runWithDelay:
+ _objc_msgSend$unregisterFromKVO
+ _objectdestroyTm
+ _qos_class_self
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_checkMetadataState
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumCaseMultiPayload
+ _swift_getObjectType
+ _swift_getTupleTypeMetadata2
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_taskGroup_destroy
+ _swift_taskGroup_initialize
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unexpectedError
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _symbolic 7ElementSTQz
+ _symbolic 7ElementSTQz______pIeghHnzo_ s5ErrorP
+ _symbolic 7ElementSTQzqd________pIeghHnrzo_ s5ErrorP
+ _symbolic B0
+ _symbolic B1
+ _symbolic ScPSg
+ _symbolic Scgyyt______pG s5ErrorP
+ _symbolic Si
+ _symbolic Siqd________pIeghHdrzo_ s5ErrorP
+ _symbolic _____ 12HMFoundation4FlowO
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySSG s9TaskLocalC
+ _symbolic _____ySSSgG s9TaskLocalC
+ _symbolic _____ySo7HMFFlowCSgG s9TaskLocalC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____G s9TaskLocalC 2os6LoggerV
+ _symbolic qd__
+ _symbolic x
+ _symbolic xIeghHr_
- __OBJC_$_CLASS_PROP_LIST_HMFWiFiManagerDataSource.107
- __OBJC_$_PROP_LIST_HMFObject.56
- __OBJC_$_PROP_LIST_HMFTimerManager.148
- __OBJC_$_PROP_LIST_HMFTimerManagerTimerContext.67
- __OBJC_$_PROP_LIST_HMFWiFiManagerDataSource.172
- ___31-[HMFNetworkDiagnosticPing run]_block_invoke
- ___31-[HMFNetworkDiagnosticPing run]_block_invoke_2
- ___31-[HMFNetworkDiagnosticPing run]_block_invoke_3
- ___45-[HMFLocationAuthorization registerObserver:]_block_invoke.51
- ___block_descriptor_32_e30_16?0"HMFNetworkDiagnostic"8l
- ___block_descriptor_56_e8_32bs40w48w_e5_v8?0ls32l8w40l8w48l8
- ___block_literal_global.129
- ___block_literal_global.64
- ___block_literal_global.9
- _objc_msgSend$run
CStrings:
+ "\x11'"
+ "@\"HMFScheduler\""
+ "Failed to unwrap optional at "
+ "Failed to unwrap optional at %s, %s, line %ld"
+ "Fatal error"
+ "HMFoundation/Flow.swift"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"HMFPromise\",&,N,V_delayPromise"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_Concurrency/TaskGroup.swift"
+ "_delayPromise"
+ "_mark"
+ "_registeredForKVO"
+ "_requestAuthorization:completionHandler:"
+ "_scheduler"
+ "delayFuture:"
+ "delayPromise"
+ "index value "
+ "initWithScheduler:"
+ "invalid Collection: less than 'count' elements in collection"
+ "offset element "
+ "runWithDelay:"
+ "scheduler"
+ "setDelayPromise:"
+ "unregisterFromKVO"
- "'"
- "R"

```
