## PreviewsFoundationOS

> `/System/Library/PrivateFrameworks/PreviewsFoundationOS.framework/PreviewsFoundationOS`

```diff

-22.20.7.0.0
-  __TEXT.__text: 0x18c088
-  __TEXT.__auth_stubs: 0x3250
-  __TEXT.__objc_methlist: 0x170
-  __TEXT.__const: 0xc374
+22.30.23.0.0
+  __TEXT.__text: 0x158e70
+  __TEXT.__auth_stubs: 0x3210
+  __TEXT.__objc_methlist: 0x274
+  __TEXT.__const: 0xdadc
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__cstring: 0x568b
-  __TEXT.__swift5_typeref: 0x560d
-  __TEXT.__constg_swiftt: 0x5554
-  __TEXT.__swift5_reflstr: 0x1fda
-  __TEXT.__swift5_fieldmd: 0x38d0
+  __TEXT.__cstring: 0x51fb
+  __TEXT.__swift5_typeref: 0x558f
+  __TEXT.__constg_swiftt: 0x559c
+  __TEXT.__swift5_reflstr: 0x1fea
+  __TEXT.__swift5_fieldmd: 0x392c
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x1220
   __TEXT.__swift5_protos: 0xc0
   __TEXT.__swift5_proto: 0x82c
-  __TEXT.__swift5_types: 0x550
+  __TEXT.__swift5_types: 0x558
   __TEXT.__swift5_capture: 0x29ec
+  __TEXT.__swift_as_entry: 0x164
+  __TEXT.__swift_as_ret: 0x148
   __TEXT.__oslogstring: 0x72c
   __TEXT.__swift5_mpenum: 0x80
-  __TEXT.__unwind_info: 0x63c8
-  __TEXT.__eh_frame: 0x7940
+  __TEXT.__unwind_info: 0x5890
+  __TEXT.__eh_frame: 0x7a18
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methname: 0x9e8
   __TEXT.__objc_methtype: 0x12f
   __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1938
-  __AUTH_CONST.__auth_ptr: 0x11c0
-  __AUTH_CONST.__const: 0xd668
+  __AUTH_CONST.__auth_got: 0x1918
+  __AUTH_CONST.__auth_ptr: 0x1318
+  __AUTH_CONST.__const: 0xd750
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x2928
+  __AUTH_CONST.__objc_const: 0x2738
   __AUTH.__objc_data: 0x1f8
-  __AUTH.__data: 0x24a0
+  __AUTH.__data: 0x24c0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x6d60
+  __DATA.__data: 0x6dd8
   __DATA.__bss: 0xcfc0
   __DATA.__common: 0x18
   __DATA_DIRTY.__data: 0x38

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8748
-  Symbols:   544
-  CStrings:  740
+  Functions: 7861
+  Symbols:   576
+  CStrings:  714
 
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
+ _swift_getExtendedExistentialTypeMetadata_unique
+ _swift_getFunctionTypeMetadata0
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
CStrings:
+ " observing cleanUpHandlers "
+ "UV_FORCE_MACOS_SRGB_COLOR_SPACE"
+ "select(file:line:)"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "select()"

```
