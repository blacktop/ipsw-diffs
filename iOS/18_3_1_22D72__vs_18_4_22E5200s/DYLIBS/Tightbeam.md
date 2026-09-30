## Tightbeam

> `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`

```diff

-326.60.70.0.0
-  __TEXT.__text: 0x29eac
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__const: 0x161a
-  __TEXT.__cstring: 0x2cbc
-  __TEXT.__constg_swiftt: 0x14a8
-  __TEXT.__swift5_typeref: 0xb0e
-  __TEXT.__swift5_fieldmd: 0x1030
+386.100.37.0.0
+  __TEXT.__text: 0x269c0
+  __TEXT.__auth_stubs: 0x10c0
+  __TEXT.__const: 0x1b9a
+  __TEXT.__cstring: 0x26ce
+  __TEXT.__constg_swiftt: 0x14cc
+  __TEXT.__swift5_typeref: 0xb3c
+  __TEXT.__swift5_fieldmd: 0x104c
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_reflstr: 0x849
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb8
-  __TEXT.__swift5_types: 0x15c
+  __TEXT.__swift5_types: 0x160
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__swift5_capture: 0xc4
+  __TEXT.__swift5_capture: 0x104
   __TEXT.__oslogstring: 0x16e
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0xbf8
-  __TEXT.__eh_frame: 0x860
+  __TEXT.__unwind_info: 0xb30
+  __TEXT.__eh_frame: 0x930
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1de
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__auth_ptr: 0x3b8
-  __AUTH_CONST.__const: 0x2100
+  __AUTH_CONST.__auth_got: 0x868
+  __AUTH_CONST.__auth_ptr: 0x3c8
+  __AUTH_CONST.__const: 0x24a0
   __AUTH_CONST.__objc_const: 0x1408
-  __DATA.__data: 0x358
+  __DATA.__data: 0x3b8
   __DATA.__bss: 0xf90
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x16e8
+  __DATA_DIRTY.__data: 0x15d0
   __DATA_DIRTY.__bss: 0x180
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1336
-  Symbols:   681
-  CStrings:  290
+  Functions: 1306
+  Symbols:   712
+  CStrings:  259
 
Symbols:
+ _objc_release_x24
+ _objc_release_x28
+ _objc_retain_x22
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getFunctionTypeMetadata0
+ _swift_getTupleTypeMetadata2
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_isEscapingClosureAtFileLocation
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _tb_message_decode_buffer
+ _tb_message_get_size
+ _tb_transport_client_activate
+ _tb_transport_construct_message_buffer
+ _tb_transport_destruct_message_buffer
+ _tb_transport_reset_message
+ _tb_transport_send_message
+ _tb_transport_service_activate
- _objc_release_x27
- _objc_retain_x21
- _objc_retain_x8
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
CStrings:
+ "I16@?0^v8"
+ "TB_ASSERT: tb_priv(transport)->static_vtable != NULL"
+ "TB_ASSERT: tp_priv->static_vtable != NULL"
+ "fetchNextCall responseCallback "
+ "identifier baseURL "
+ "withTransportBuffer called with nil buffer"
- "Can't construct Array with count < 0"
- "Can't drop a negative number of elements from a collection"
- "Can't take a prefix of negative length from a collection"
- "ClosedRange requires lowerBound <= upperBound"
- "Index out of bounds"
- "Index out of range"
- "Insufficient space allocated to copy string contents"
- "Invalid slice"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range out of bounds"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/ClosedRange.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeBufferPointer with negative count"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer has a nil start and nonzero count"
- "UnsafeMutableRawBufferPointer with negative count"
- "UnsafeMutableRawPointer.copyMemory with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeRawBufferPointer has a nil start and nonzero count"
- "UnsafeRawBufferPointer with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
