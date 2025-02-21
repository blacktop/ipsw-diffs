## SPIHelper-iOS

> `/System/Library/PrivateFrameworks/CloudSharing.framework/XPCServices/SPIHelper-iOS.xpc/SPIHelper-iOS`

```diff

-188.1.3.2.0
-  __TEXT.__text: 0x9ec8c
-  __TEXT.__auth_stubs: 0x15a0
+188.4.1.0.0
+  __TEXT.__text: 0x92340
+  __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x178
-  __TEXT.__const: 0x3e80
-  __TEXT.__cstring: 0x40d3
-  __TEXT.__objc_methname: 0x1158
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x3e00
+  __TEXT.__cstring: 0x3f03
+  __TEXT.__objc_methname: 0x116d
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methtype: 0x11c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xc6c
-  __TEXT.__swift5_typeref: 0x2174
-  __TEXT.__swift5_fieldmd: 0xf90
+  __TEXT.__constg_swiftt: 0xc90
+  __TEXT.__swift5_typeref: 0x21d0
+  __TEXT.__swift5_fieldmd: 0xfc4
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x11ac
+  __TEXT.__swift5_reflstr: 0x11fc
   __TEXT.__swift5_assocty: 0x378
-  __TEXT.__swift5_proto: 0x194
-  __TEXT.__swift5_types: 0xcc
+  __TEXT.__oslogstring: 0x2742
+  __TEXT.__swift5_proto: 0x1a0
+  __TEXT.__swift5_types: 0xd0
   __TEXT.__swift5_capture: 0xecc
-  __TEXT.__oslogstring: 0x26a2
+  __TEXT.__swift_as_entry: 0x168
+  __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x23c8
-  __TEXT.__eh_frame: 0x64d0
-  __DATA_CONST.__auth_got: 0xad8
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__auth_ptr: 0x828
-  __DATA_CONST.__const: 0x2dd8
+  __TEXT.__unwind_info: 0x2210
+  __TEXT.__eh_frame: 0x6658
+  __DATA_CONST.__auth_got: 0xab0
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__auth_ptr: 0x848
+  __DATA_CONST.__const: 0x3028
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x1518
-  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_const: 0x1308
+  __DATA.__objc_selrefs: 0x520
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x598
-  __DATA.__data: 0x1f48
+  __DATA.__objc_data: 0x3f8
+  __DATA.__data: 0x1fc0
   __DATA.__common: 0xa0
-  __DATA.__bss: 0x36c0
+  __DATA.__bss: 0x3840
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CloudSharing.framework/CloudSharing
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2145
-  Symbols:   254
-  CStrings:  721
+  Functions: 2079
+  Symbols:   260
+  CStrings:  717
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x1
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "%s: SPI Entitlement Protection is disabled. Allowing connection regardless."
+ "CloudSharing SPI: Attempted connection without entitlement. Denied."
+ "CloudSharingUI"
+ "Gelato"
+ "SPIEntitlementProtection"
+ "ShareAccessRequests"
+ "com.apple.private.CloudSharing.SPI"
+ "listener(_:shouldAcceptNewConnection:)"
+ "valueForEntitlement:"
- "Insufficient space allocated to copy string contents"
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
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
