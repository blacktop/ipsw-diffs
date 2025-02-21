## Coherence

> `/System/Library/PrivateFrameworks/Coherence.framework/Coherence`

```diff

-186.203.1.0.0
-  __TEXT.__text: 0x54563c
-  __TEXT.__auth_stubs: 0x33d0
-  __TEXT.__objc_methlist: 0x11c8
-  __TEXT.__const: 0x12a26
-  __TEXT.__gcc_except_tab: 0x266c
-  __TEXT.__cstring: 0x6a0b
+186.301.0.0.0
+  __TEXT.__text: 0x4aeff0
+  __TEXT.__auth_stubs: 0x3320
+  __TEXT.__objc_methlist: 0x157c
+  __TEXT.__const: 0x14248
+  __TEXT.__gcc_except_tab: 0x26f0
+  __TEXT.__cstring: 0x661b
   __TEXT.__oslogstring: 0x443
-  __TEXT.__swift5_typeref: 0x6626
-  __TEXT.__swift5_capture: 0x15dc
+  __TEXT.__swift5_typeref: 0x65e6
+  __TEXT.__swift5_capture: 0x1604
   __TEXT.__constg_swiftt: 0xb914
   __TEXT.__swift5_reflstr: 0x2f3d
   __TEXT.__swift5_fieldmd: 0x58d4

   __TEXT.__swift5_types: 0x6f4
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_protos: 0x130
-  __TEXT.__unwind_info: 0xaa20
-  __TEXT.__eh_frame: 0x132c8
+  __TEXT.__swift_as_entry: 0xdc
+  __TEXT.__swift_as_ret: 0xc0
+  __TEXT.__unwind_info: 0x96a0
+  __TEXT.__eh_frame: 0x13360
   __TEXT.__objc_classname: 0x16b
   __TEXT.__objc_methname: 0x2547
   __TEXT.__objc_methtype: 0xb67
   __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x850
+  __DATA_CONST.__got: 0x858
   __DATA_CONST.__const: 0xb48
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa38
+  __DATA_CONST.__objc_selrefs: 0xb28
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x19f8
-  __AUTH_CONST.__auth_ptr: 0x18f8
-  __AUTH_CONST.__const: 0xd158
+  __AUTH_CONST.__auth_got: 0x19a0
+  __AUTH_CONST.__auth_ptr: 0x17c0
+  __AUTH_CONST.__const: 0xd1a8
   __AUTH_CONST.__cfstring: 0x780
-  __AUTH_CONST.__objc_const: 0x7ad8
-  __AUTH.__objc_data: 0xec8
-  __AUTH.__data: 0x5ed8
+  __AUTH_CONST.__objc_const: 0x7418
+  __AUTH.__objc_data: 0xbb8
+  __AUTH.__data: 0x4c78
   __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0x6b50
-  __DATA.__bss: 0x170a0
-  __DATA.__common: 0x840
-  __DATA_DIRTY.__objc_data: 0x18f8
-  __DATA_DIRTY.__data: 0x7c58
-  __DATA_DIRTY.__bss: 0x3ba0
-  __DATA_DIRTY.__common: 0x1d8
+  __DATA.__data: 0x6780
+  __DATA.__bss: 0x17020
+  __DATA.__common: 0x820
+  __DATA_DIRTY.__objc_data: 0x1bc8
+  __DATA_DIRTY.__data: 0x9340
+  __DATA_DIRTY.__bss: 0x3c20
+  __DATA_DIRTY.__common: 0x1e0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14634
-  Symbols:   1040
-  CStrings:  1474
+  Functions: 12990
+  Symbols:   1066
+  CStrings:  1452
 
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
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
- _swift_weakCopyAssign
- _swift_weakCopyInit
- _swift_weakTakeAssign
- _swift_weakTakeInit
CStrings:
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
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
