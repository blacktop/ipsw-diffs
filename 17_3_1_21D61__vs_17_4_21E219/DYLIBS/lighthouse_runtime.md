## lighthouse_runtime

> `/System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime`

```diff

-3.0.7.0.0
-  __TEXT.__text: 0xc758
-  __TEXT.__auth_stubs: 0x860
+3.0.9.0.0
+  __TEXT.__text: 0x10a40
+  __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x792
-  __TEXT.__cstring: 0x23c
-  __TEXT.__swift5_typeref: 0x442
-  __TEXT.__swift5_reflstr: 0x1b1
-  __TEXT.__swift5_assocty: 0x50
-  __TEXT.__swift5_fieldmd: 0x298
-  __TEXT.__constg_swiftt: 0x52c
-  __TEXT.__swift5_capture: 0x114
-  __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x1088
-  __TEXT.__eh_frame: 0xaf8
-  __TEXT.__objc_methname: 0x20f
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x100
+  __TEXT.__const: 0x8f2
+  __TEXT.__cstring: 0x6bc
+  __TEXT.__swift5_typeref: 0x4b6
+  __TEXT.__swift5_reflstr: 0x211
+  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_fieldmd: 0x300
+  __TEXT.__constg_swiftt: 0x59c
+  __TEXT.__swift5_capture: 0x138
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__unwind_info: 0x1238
+  __TEXT.__eh_frame: 0xc00
+  __TEXT.__objc_methname: 0x24b
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b0
-  __DATA_CONST.__objc_selrefs: 0xd8
-  __AUTH_CONST.__const: 0xa88
-  __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH.__data: 0x98
+  __DATA_CONST.__objc_const: 0x2d0
+  __DATA_CONST.__objc_selrefs: 0xf0
+  __DATA_CONST.__objc_classrefs: 0x50
+  __AUTH_CONST.__const: 0xad8
+  __AUTH_CONST.__auth_ptr: 0x40
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__data: 0x148
   __AUTH.__objc_data: 0x150
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__data: 0x5f0
-  __DATA.__bss: 0x800
-  __DATA.__common: 0x18
+  __DATA.__data: 0x5d8
+  __DATA.__bss: 0xa00
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 416
-  Symbols:   233
-  CStrings:  59
+  Functions: 460
+  Symbols:   262
+  CStrings:  87
 
Symbols:
+ _OBJC_CLASS_$_OSLogPreferencesCategory
+ _OBJC_CLASS_$_OSLogPreferencesSubsystem
+ ___unnamed_13
+ __os_signpost_emit_with_name_impl
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_lighthouse_runtime
+ __swift_stdlib_malloc_size
+ _associated conformance 18lighthouse_runtime14LRSignpostNameOAA23StaticStringConvertibleAA8RawValueSY_Sy
+ _associated conformance 18lighthouse_runtime14LRSignpostNameOSHAASQ
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x23
+ _objc_retain_x26
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_initStructMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRetain
+ _symbolic $s18lighthouse_runtime23StaticStringConvertibleP
+ _symbolic $sSY
+ _symbolic 8RawValueSYQz
+ _symbolic SS
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 18lighthouse_runtime14LRSignpostNameO
+ _symbolic _____ 2os12OSSignposterV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s12StaticStringV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- ___swift_memcpy40_8
- ___unnamed_7
- _objc_retain_x21
- _objc_retain_x27
- _symbolic SS3key_yp5valuetSg
CStrings:
+ "DoWork"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "LoadData"
+ "Missing Data Records"
+ "Missing Worker Result"
+ "Report"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "TotalRuntime"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "[Error] Interval already ended"
+ "com.apple.lighthouse"
+ "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nenableTelemetry=YES"
+ "correlationID=%{public, signpost.telemetry:string1, name=correlationID,public}s\nerrorMessage=%{public, signpost.telemetry:string2, name=errorMessage,public}s\nenableTelemetry=YES"
+ "initWithName:"
+ "initWithName:subsystem:"
+ "invalid Collection: less than 'count' elements in collection"
+ "setSignpostPersisted:"
+ "telemetrySignposter"

```
