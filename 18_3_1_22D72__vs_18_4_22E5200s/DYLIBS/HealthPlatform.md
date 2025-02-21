## HealthPlatform

> `/System/Library/PrivateFrameworks/HealthPlatform.framework/HealthPlatform`

```diff

-5200.3.6.1.1
-  __TEXT.__text: 0x177220
-  __TEXT.__auth_stubs: 0x3100
-  __TEXT.__objc_methlist: 0x57c
-  __TEXT.__const: 0xb122
-  __TEXT.__cstring: 0x7a5d
+5200.4.19.1.2
+  __TEXT.__text: 0x15708c
+  __TEXT.__auth_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x87c
+  __TEXT.__const: 0xc3c2
+  __TEXT.__cstring: 0x76ed
   __TEXT.__oslogstring: 0x5845
   __TEXT.__swift5_typeref: 0x41e6
   __TEXT.__swift5_capture: 0x2474
   __TEXT.__constg_swiftt: 0x4990
-  __TEXT.__swift5_reflstr: 0x30d4
-  __TEXT.__swift5_fieldmd: 0x3a54
+  __TEXT.__swift5_reflstr: 0x30f4
+  __TEXT.__swift5_fieldmd: 0x3a60
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x808
   __TEXT.__swift5_proto: 0x980
   __TEXT.__swift5_types: 0x4b8
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x54
-  __TEXT.__unwind_info: 0x5e48
-  __TEXT.__eh_frame: 0x514c
+  __TEXT.__swift_as_entry: 0x28
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__unwind_info: 0x5658
+  __TEXT.__eh_frame: 0x51ec
   __TEXT.__objc_classname: 0x123
-  __TEXT.__objc_methname: 0x2977
+  __TEXT.__objc_methname: 0x2996
   __TEXT.__objc_methtype: 0x3ce
-  __DATA_CONST.__got: 0xcb0
-  __DATA_CONST.__const: 0x908
+  __DATA_CONST.__got: 0xc98
+  __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xeb0
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x1880
+  __AUTH_CONST.__auth_got: 0x1840
   __AUTH_CONST.__auth_ptr: 0xd70
-  __AUTH_CONST.__const: 0xc710
-  __AUTH_CONST.__objc_const: 0x5270
-  __AUTH.__objc_data: 0x968
-  __AUTH.__data: 0xc60
-  __DATA.__data: 0x1b58
-  __DATA.__bss: 0xa238
+  __AUTH_CONST.__const: 0xc6f8
+  __AUTH_CONST.__objc_const: 0x4e78
+  __AUTH.__objc_data: 0x818
+  __AUTH.__data: 0xb68
+  __DATA.__data: 0x1b18
+  __DATA.__bss: 0x9f38
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xe18
-  __DATA_DIRTY.__data: 0x5be8
-  __DATA_DIRTY.__bss: 0x6b00
+  __DATA_DIRTY.__data: 0x5e18
+  __DATA_DIRTY.__bss: 0x6e00
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9005
-  Symbols:   704
-  CStrings:  1681
+  Functions: 8397
+  Symbols:   745
+  CStrings:  1663
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftWebKit
- _objc_release_x10
- _objc_retain_x10
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "accountSupportsSecureContainer"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
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
- "invalid Collection: less than 'count' elements in collection"

```
