## ProactiveDaemonSupport

> `/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport`

```diff

-137.12.0.0.0
-  __TEXT.__text: 0x1cdec
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x40
-  __TEXT.__cstring: 0x8f9
-  __TEXT.__swift5_typeref: 0xacc
-  __TEXT.__const: 0x1110
-  __TEXT.__constg_swiftt: 0xc14
-  __TEXT.__swift5_reflstr: 0x3cc
-  __TEXT.__swift5_fieldmd: 0x608
+193.0.5.0.0
+  __TEXT.__text: 0x1fa18
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__const: 0x16f0
+  __TEXT.__cstring: 0x727
+  __TEXT.__constg_swiftt: 0xe60
+  __TEXT.__swift5_typeref: 0xcfa
+  __TEXT.__swift5_reflstr: 0x444
+  __TEXT.__swift5_fieldmd: 0x750
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x98
-  __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_capture: 0x3e0
-  __TEXT.__swift5_protos: 0x34
+  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift5_proto: 0xa8
+  __TEXT.__swift5_capture: 0x414
+  __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__oslogstring: 0xa4d
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__oslogstring: 0xb7d
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x80
-  __TEXT.__unwind_info: 0x910
-  __TEXT.__eh_frame: 0xeb8
+  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__eh_frame: 0x1028
   __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0x41f
+  __TEXT.__objc_methname: 0x42d
   __TEXT.__objc_methtype: 0xe9
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x178
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
+  __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x8a0
-  __AUTH_CONST.__auth_ptr: 0x238
-  __AUTH_CONST.__const: 0x15f0
-  __AUTH_CONST.__objc_const: 0x7d0
-  __DATA.__data: 0x5f8
-  __DATA.__bss: 0xe00
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x8b0
-  __DATA_DIRTY.__bss: 0x500
+  __AUTH_CONST.__auth_got: 0x978
+  __AUTH_CONST.__auth_ptr: 0x278
+  __AUTH_CONST.__const: 0x1968
+  __AUTH_CONST.__objc_const: 0x730
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x128
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x1080
+  __DATA.__common: 0x20
+  __DATA_DIRTY.__data: 0x7f8
+  __DATA_DIRTY.__bss: 0x380
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 970
-  Symbols:   193
-  CStrings:  180
+  Functions: 1059
+  Symbols:   213
+  CStrings:  183
 
Symbols:
+ _WriteCrashReportWithStackshot
+ __swift_stdlib_reportUnimplementedInitializer
+ _dispatch_main
+ _getpid
+ _objc_retain_x25
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getFunctionTypeMetadata0
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_release_n
+ _swift_retain_n
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_updateClassMetadata2
- _objc_retain_x23
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "%{public}s: Connection to XPC Server interrupted."
+ "%{public}s: Connection to XPC Server invalidated."
+ "%{public}s: did not create connection."
+ "%{public}s: error during call: %{public}@."
+ "%{public}s: establishing connection."
+ ".cxx_destruct"
+ "Exiting with reason: %{public}s"
+ "Posting notification %{public}s"
+ "Posting notification %{public}s userInfo: %s"
+ "ProactiveDaemonSupport.BidirectionalDelegate"
+ "ProactiveDaemonSupport.Delegate"
+ "WATCHDOG EXPIRED: Stackshot acquired"
+ "WATCHDOG EXPIRED: The watchdog for %{public}s has expired. Capturing stackshot."
+ "WATCHDOG EXPIRED: The watchdog for %{public}s has expired. Unable to get stackshot."
+ "Watchdog expired"
+ "_TtC22ProactiveDaemonSupport8Watchdog"
+ "cacheSize"
+ "com.apple.proactivedaemonsupport.watchdog"
+ "context"
+ "deadline"
+ "init()"
+ "key value "
+ "logger"
+ "name"
+ "v16@0:8"
+ "value"
- "%s: Connection to XPC Server interrupted."
- "%s: Connection to XPC Server invalidated."
- "%s: did not create connection."
- "%s: error during call: %@."
- "%s: establishing connection."
- "Exiting with reason: %s"
- "Insufficient space allocated to copy string contents"
- "Posting notification %s"
- "Posting notification %s userInfo: %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
