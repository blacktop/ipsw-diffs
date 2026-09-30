## HomePodSettings

> `/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`

```diff

-226.30.3.0.0
-  __TEXT.__text: 0xfe0fc
-  __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x1ca8
-  __TEXT.__const: 0xbcba
-  __TEXT.__cstring: 0x6276
+226.40.12.0.0
+  __TEXT.__text: 0xe2610
+  __TEXT.__auth_stubs: 0x25b0
+  __TEXT.__objc_methlist: 0x21ec
+  __TEXT.__const: 0xcdca
+  __TEXT.__cstring: 0x5ec6
   __TEXT.__oslogstring: 0x1129
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x204
   __TEXT.__constg_swiftt: 0x46c0
-  __TEXT.__swift5_typeref: 0x42b5
+  __TEXT.__swift5_typeref: 0x430d
   __TEXT.__swift5_reflstr: 0x1e23
   __TEXT.__swift5_fieldmd: 0x2d94
   __TEXT.__swift5_builtin: 0xf0

   __TEXT.__swift5_capture: 0x1164
   __TEXT.__swift5_assocty: 0x808
   __TEXT.__swift5_protos: 0x80
+  __TEXT.__swift_as_entry: 0x3bc
+  __TEXT.__swift_as_ret: 0x380
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__unwind_info: 0x58d8
-  __TEXT.__eh_frame: 0xa5d0
+  __TEXT.__unwind_info: 0x5410
+  __TEXT.__eh_frame: 0xa4d8
   __TEXT.__objc_classname: 0x495
-  __TEXT.__objc_methname: 0x2e93
+  __TEXT.__objc_methname: 0x2e73
   __TEXT.__objc_methtype: 0xb68
   __TEXT.__objc_stubs: 0x18a0
-  __DATA_CONST.__got: 0x728
-  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x1310
-  __AUTH_CONST.__auth_ptr: 0xba0
-  __AUTH_CONST.__const: 0x7fa0
+  __AUTH_CONST.__auth_got: 0x12e8
+  __AUTH_CONST.__auth_ptr: 0xbb8
+  __AUTH_CONST.__const: 0x8158
   __AUTH_CONST.__cfstring: 0x1160
-  __AUTH_CONST.__objc_const: 0x8230
+  __AUTH_CONST.__objc_const: 0x7ae0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2420
-  __AUTH.__data: 0x1dd8
+  __AUTH.__objc_data: 0x21f0
+  __AUTH.__data: 0x1de8
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x4d98
+  __DATA.__data: 0x4df8
   __DATA.__bss: 0x15770
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7897
-  Symbols:   2725
-  CStrings:  1418
+  Functions: 7650
+  Symbols:   2811
+  CStrings:  1398
 
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
+ _swift_getExistentialTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
- _COClusterHome
- _OBJC_CLASS_$_COFeatureStatus
- _objc_retain_x28
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
- _swift_weakCopyAssign
- _swift_weakCopyInit
- _swift_weakTakeAssign
- _swift_weakTakeInit
CStrings:
+ " expected "
+ "homeID homeKitIdentifiers "
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Range.swift"
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
- "isNoDaemonMessageChannelEnabled"

```
