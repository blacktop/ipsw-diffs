## ProactiveDaemonSupport

> `/System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/Versions/A/ProactiveDaemonSupport`

```diff

-137.12.0.0.0
-  __TEXT.__text: 0x1f1d8
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x40
-  __TEXT.__cstring: 0x9f9
-  __TEXT.__swift5_typeref: 0xb24
-  __TEXT.__const: 0x1130
-  __TEXT.__constg_swiftt: 0xc14
-  __TEXT.__swift5_reflstr: 0x3cc
-  __TEXT.__swift5_fieldmd: 0x608
+197.0.8.201.0
+  __TEXT.__text: 0x22e84
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x17c
+  __TEXT.__const: 0x13f8
+  __TEXT.__cstring: 0x827
+  __TEXT.__constg_swiftt: 0xe60
+  __TEXT.__swift5_typeref: 0xd52
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
-  __TEXT.__oslogstring: 0xb3d
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__oslogstring: 0xc6d
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x80
-  __TEXT.__unwind_info: 0x968
-  __TEXT.__eh_frame: 0xf38
+  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__eh_frame: 0x10a8
   __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0x41f
+  __TEXT.__objc_methname: 0x42d
   __TEXT.__objc_methtype: 0xe9
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
+  __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x15f0
-  __AUTH_CONST.__objc_const: 0x7d0
-  __AUTH.__data: 0x340
-  __DATA.__data: 0xb68
-  __DATA.__bss: 0x1300
-  __DATA.__common: 0x18
+  __AUTH_CONST.__auth_got: 0x910
+  __AUTH_CONST.__const: 0x1968
+  __AUTH_CONST.__objc_const: 0x730
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x3f0
+  __DATA.__data: 0xd48
+  __DATA.__bss: 0x1400
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/Versions/A/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C1FBBE79-BFB7-34A6-B044-D8A8740E4190
-  Functions: 1012
-  Symbols:   180
-  CStrings:  190
+  UUID: 769100D3-F481-3FCF-A717-134795DB527B
+  Functions: 1152
+  Symbols:   193
+  CStrings:  193
 
Symbols:
+ _WriteCrashReportWithStackshot
+ __swift_stdlib_reportUnimplementedInitializer
+ _dispatch_main
+ _getpid
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_initStructMetadata
+ _swift_release_n
+ _swift_retain_n
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_updateClassMetadata2
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
