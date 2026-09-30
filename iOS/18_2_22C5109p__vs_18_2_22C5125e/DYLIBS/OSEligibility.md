## OSEligibility

> `/System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility`

```diff

-154.60.0.502.3
-  __TEXT.__text: 0x7000
-  __TEXT.__auth_stubs: 0x620
+160.60.1.0.0
+  __TEXT.__text: 0x87e8
+  __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x487
-  __TEXT.__const: 0xbc0
-  __TEXT.__swift5_typeref: 0xd0
-  __TEXT.__constg_swiftt: 0x118
+  __TEXT.__const: 0xc08
+  __TEXT.__cstring: 0x6f8
+  __TEXT.__oslogstring: 0x1be
+  __TEXT.__swift5_typeref: 0xee
+  __TEXT.__constg_swiftt: 0x148
+  __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_reflstr: 0x67e
   __TEXT.__swift5_fieldmd: 0x834
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x258
-  __TEXT.__eh_frame: 0x258
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__eh_frame: 0x250
   __TEXT.__objc_methname: 0x11a
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__auth_ptr: 0xc8
-  __AUTH_CONST.__const: 0x4a8
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__auth_ptr: 0xe0
+  __AUTH_CONST.__const: 0x4d8
   __AUTH_CONST.__objc_const: 0x118
   __AUTH.__objc_data: 0x70
   __AUTH.__data: 0x28
-  __DATA.__data: 0x90
-  __DATA.__bss: 0x890
+  __DATA.__data: 0xa8
+  __DATA.__bss: 0x898
+  __DATA.__common: 0x18
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_signal.dylib
   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 206
-  Symbols:   89
-  CStrings:  49
+  Functions: 223
+  Symbols:   110
+  CStrings:  70
 
Symbols:
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftos
+ _kCFAllocatorDefault
+ _memcpy
+ _objc_release_x19
+ _objc_release_x21
+ _objc_release_x26
+ _objc_retain
+ _os_log_type_enabled
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRetain_n
+ _swift_getObjectType
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
- _csops_audittoken
CStrings:
+ "Bypassing eligibility for %!s(MISSING):%!s(MISSING)"
+ "Could not create SecTask from audit token for pid %!d(MISSING)"
+ "Could not get signing identifier for pid %!d(MISSING): %!s(MISSING)"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "No app record found for %!s(MISSING) so not bypassing eligibility"
+ "Not bypassing eligibility for %!s(MISSING):%!s(MISSING) (isProfileValidated: %!{(MISSING)bool}d isUPPValidated:%!{(MISSING)bool}d isBeta:%!{(MISSING)bool}d"
+ "Persona %!s(MISSING) not applicable for %!s(MISSING) so not bypassing eligibility"
+ "Personal persona not found for %!s(MISSING) so not bypassing eligibility"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "com.apple.OSEligibility"
+ "invalid Collection: less than 'count' elements in collection"

```
