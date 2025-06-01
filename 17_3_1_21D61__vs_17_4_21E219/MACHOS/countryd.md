## countryd

> `/usr/libexec/countryd`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x9f0c
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x760
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0xb8
+45.0.6.0.1
+  __TEXT.__text: 0xa8a4
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x27c
+  __TEXT.__const: 0xc0
   __TEXT.__swift5_typeref: 0x1a2
-  __TEXT.__objc_methname: 0x904
-  __TEXT.__cstring: 0x3b5
+  __TEXT.__objc_methname: 0x97a
+  __TEXT.__cstring: 0x70c
   __TEXT.__constg_swiftt: 0xb0
   __TEXT.__swift5_reflstr: 0x2b
   __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0xaf7
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__oslogstring: 0xd3c
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methtype: 0x29a
-  __TEXT.__unwind_info: 0x30c
+  __TEXT.__objc_methtype: 0x2a5
+  __TEXT.__unwind_info: 0x334
   __TEXT.__eh_frame: 0x5b0
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x338
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xa68
-  __DATA.__objc_selrefs: 0x2a0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xa8
-  __DATA.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0xaa8
+  __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x3f0
+  __DATA.__data: 0x420
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D5696B0C-9EAB-3EDB-A12C-37A4CD9F19CA
-  Functions: 183
-  Symbols:   137
-  CStrings:  253
+  UUID: F9724F34-3D1E-390E-9AE9-58EFE51DE110
+  Functions: 187
+  Symbols:   146
+  CStrings:  287
 
Symbols:
+ __Unwind_Resume
+ ___gxx_personality_v0
+ __dispatch_main_q
+ __xpc_event_key_name
+ _geteuid
+ _objc_release_x27
+ _swift_initStaticObject
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "com.apple.countryd.lock"
+ "com.apple.notifyd.matching"
+ "com.apple.os-eligibility-domain.input-needed"
+ "invalid Collection: less than 'count' elements in collection"
+ "lock state can only be modified by root user"
+ "peer process is missing entitlement lock our cache"
+ "postResultsToEligibilityEngine"
+ "setBool:forKey:"
+ "setCacheLockState:"
+ "triggerUpdateToEligibilityEngine"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v20@0:8B16"
+ "{\"msg%{public}.0s\":\"Got Darwin notification\", \"notification\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"eligibility engine wants input\"}"
+ "{\"msg%{public}.0s\":\"lock state can only be modified by root user\"}"
+ "{\"msg%{public}.0s\":\"peer process is missing entitlement lock our cache\", \"entitlement\":%{public, location:escape_only}s, \"process\":%{public}d}"
+ "{\"msg%{public}.0s\":\"triggering update to eligibility engine\"}"
+ "{\"msg%{public}.0s\":\"updating lock state\", \"locked\":%{public}hhd}"

```
