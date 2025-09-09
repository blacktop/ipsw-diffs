## PednetInferenceProviderTarget

> `/System/Library/ExtensionKit/Extensions/PednetInferenceProviderTarget.appex/PednetInferenceProviderTarget`

```diff

 3056.0.25.0.8
-  __TEXT.__text: 0x0
-  __TEXT.__auth_stubs: 0x10
-  __TEXT.__const: 0x52
-  __DATA_CONST.__auth_got: 0x8
+  __TEXT.__text: 0xc5e8
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x94
+  __TEXT.__const: 0xb14
+  __TEXT.__objc_methname: 0x107
+  __TEXT.__cstring: 0x33a
+  __TEXT.__constg_swiftt: 0x310
+  __TEXT.__swift5_typeref: 0x268
+  __TEXT.__swift5_reflstr: 0x173
+  __TEXT.__swift5_fieldmd: 0x210
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x2c
+  __TEXT.__oslogstring: 0x1d6
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__unwind_info: 0x538
+  __TEXT.__eh_frame: 0x7a8
+  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_ptr: 0x338
+  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_const: 0x2f8
+  __DATA.__objc_selrefs: 0x70
+  __DATA.__objc_data: 0x240
+  __DATA.__data: 0x580
+  __DATA.__bss: 0xfa0
+  __DATA.__common: 0x68
+  - /System/Library/Frameworks/CoreML.framework/CoreML
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B08890E-9B35-35BE-904D-102C2B9E7C63
-  Functions: 0
-  Symbols:   5
-  CStrings:  0
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 7F1E22A1-63DE-36C0-B046-D1E18B861115
+  Functions: 402
+  Symbols:   120
+  CStrings:  63
 
Symbols:
+ _OBJC_CLASS_$_MLModel
+ _OBJC_CLASS_$_MLModelConfiguration
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$__TtC15PednetInterface15CMPednetRequest
+ _OBJC_CLASS_$__TtC15PednetInterface16CMPednetResponse
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__TtC15PednetInterface15CMPednetRequest
+ _OBJC_METACLASS_$__TtC15PednetInterface16CMPednetResponse
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_stdlib_bridgeErrorToNSError
+ _bzero
+ _free
+ _mach_continuous_time
+ _main
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend
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
+ _objc_release_x27
+ _objc_release_x8
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x23
+ _os_log_type_enabled
+ _strncpy
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_coroFrameAlloc
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorInMain
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initClassMetadata2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _swift_willThrowTypedImpl
CStrings:
+ "$defaultActor"
+ ".cxx_destruct"
+ "@16@0:8"
+ "CoreMotionPednet.Request"
+ "CoreMotionPednet.Response"
+ "FAILURE"
+ "Inference run. Output: %s"
+ "InferenceProvider requestOneShot called"
+ "Loading model from file: %s"
+ "Received request with timestamp %llu"
+ "SUCCESS"
+ "Serialize protobuf..."
+ "Serializing and returning output vector: %s"
+ "Tensor converted, about to run inference..."
+ "Transition to dynamic mode (aka loaded) for %s"
+ "Transition to loaded for %s"
+ "Transition to unloaded for %s"
+ "Unexpected error: %@"
+ "Unknown load state: %s"
+ "_TtC15PednetInterface15CMPednetRequest"
+ "_TtC15PednetInterface16CMPednetResponse"
+ "_TtC29PednetInferenceProviderTarget11CMb788Model"
+ "_TtC29PednetInferenceProviderTarget35CoreMotionPednetV1InferenceProvider"
+ "_TtC29PednetInferenceProviderTarget42CoreMotionPednetV1InferenceProviderService"
+ "_model"
+ "biometrics"
+ "biometrics: %s"
+ "com.apple.PednetInferenceProvider"
+ "dealloc"
+ "errorString::"
+ "errorStringLength:"
+ "error_message"
+ "getMachContinuousTimestamp:"
+ "getType:"
+ "init"
+ "loadedAssets"
+ "mach_continuous_timestamp"
+ "mainBundle"
+ "model"
+ "modelWithContentsOfURL:configuration:error:"
+ "pathForResource:ofType:"
+ "request"
+ "response"
+ "rotationRateX"
+ "rotationRateY"
+ "rotationRateZ"
+ "setArrays::::::::::::::"
+ "setComputeUnits:"
+ "setTimestamp:"
+ "type"
+ "userAccelX"
+ "userAccelY"
+ "userAccelZ"
+ "v128@0:8r^f16q24r^f32q40r^f48q56r^f64q72r^f80q88r^f96q104r^f112q120"
+ "v16@0:8"
+ "v24@0:8*16"
+ "v24@0:8Q16"
+ "v24@0:8^I16"
+ "v24@0:8^Q16"
+ "v28@0:8*16I24"
+ "v32@0:8^f16q24"
+ "values"
+ "writePredictionValuesToBuffer::"

```
