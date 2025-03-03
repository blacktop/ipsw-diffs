## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-629.80.2.0.0
-  __TEXT.__text: 0xc7d90
-  __TEXT.__auth_stubs: 0x32c0
-  __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0x3c81
-  __TEXT.__cstring: 0x6986
-  __TEXT.__oslogstring: 0x5215
-  __TEXT.__gcc_except_tab: 0x10d0
-  __TEXT.__swift5_typeref: 0x137a
+649.100.4.0.0
+  __TEXT.__text: 0xba2c4
+  __TEXT.__auth_stubs: 0x3260
+  __TEXT.__objc_methlist: 0x360
+  __TEXT.__const: 0x4d78
+  __TEXT.__cstring: 0x6636
+  __TEXT.__oslogstring: 0x5235
+  __TEXT.__gcc_except_tab: 0x10e8
+  __TEXT.__swift5_typeref: 0x135a
   __TEXT.__swift5_reflstr: 0x28a1
   __TEXT.__swift5_assocty: 0x2a8
   __TEXT.__constg_swiftt: 0x1330

   __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_capture: 0x3b0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2d38
-  __TEXT.__eh_frame: 0x2858
+  __TEXT.__unwind_info: 0x2888
+  __TEXT.__eh_frame: 0x2748
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methname: 0xc46
   __TEXT.__objc_methtype: 0xfea
   __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__const: 0x1bf0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x1978
-  __AUTH_CONST.__auth_ptr: 0x4e8
+  __AUTH_CONST.__auth_got: 0x1948
+  __AUTH_CONST.__auth_ptr: 0x4e0
   __AUTH_CONST.__const: 0x4848
   __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0x12c0
+  __AUTH_CONST.__objc_const: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x1068
+  __AUTH.__data: 0x1078
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0xc48
+  __DATA.__data: 0xc58
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x6600
+  __DATA.__bss: 0x65f0
   __DATA.__common: 0x110
   __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x70

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3976
-  Symbols:   3512
-  CStrings:  1627
+  Functions: 3687
+  Symbols:   3558
+  CStrings:  1610
 
Symbols:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getExistentialTypeMetadata
+ _swift_getTupleTypeMetadata3
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x9
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "fileDescription from to "
+ "trace remove failed (%{errno}d)"
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
