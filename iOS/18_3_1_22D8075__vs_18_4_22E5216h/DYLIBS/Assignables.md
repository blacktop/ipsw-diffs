## Assignables

> `/System/Library/Frameworks/Assignables.framework/Assignables`

```diff

-1.3.0.0.0
-  __TEXT.__text: 0x1ad134
-  __TEXT.__auth_stubs: 0x2e70
-  __TEXT.__objc_methlist: 0x4d0
-  __TEXT.__cstring: 0x2c24
-  __TEXT.__const: 0xaef0
+1.4.1.0.0
+  __TEXT.__text: 0x1800fc
+  __TEXT.__auth_stubs: 0x2e40
+  __TEXT.__objc_methlist: 0x64c
+  __TEXT.__const: 0xae40
+  __TEXT.__cstring: 0x28a4
   __TEXT.__constg_swiftt: 0x3040
-  __TEXT.__swift5_typeref: 0x45e9
+  __TEXT.__swift5_typeref: 0x4559
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x2788
+  __TEXT.__swift5_reflstr: 0x2798
   __TEXT.__swift5_fieldmd: 0x2694
   __TEXT.__swift5_assocty: 0xf40
-  __TEXT.__swift5_proto: 0x964
+  __TEXT.__swift5_proto: 0x960
   __TEXT.__swift5_types: 0x290
   __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_capture: 0xb10
+  __TEXT.__swift_as_entry: 0x1a4
+  __TEXT.__swift_as_ret: 0x230
   __TEXT.__oslogstring: 0x1938
-  __TEXT.__unwind_info: 0x4a58
-  __TEXT.__eh_frame: 0x9cd4
+  __TEXT.__unwind_info: 0x45a8
+  __TEXT.__eh_frame: 0x99fc
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x1523
   __TEXT.__objc_methtype: 0x1bb
-  __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1738
-  __AUTH_CONST.__auth_ptr: 0x1448
-  __AUTH_CONST.__const: 0x5ab0
-  __AUTH_CONST.__objc_const: 0x2840
+  __AUTH_CONST.__auth_got: 0x1720
+  __AUTH_CONST.__auth_ptr: 0x1138
+  __AUTH_CONST.__const: 0x5e50
+  __AUTH_CONST.__objc_const: 0x2580
   __AUTH.__objc_data: 0xed8
   __AUTH.__data: 0x3238
-  __DATA.__data: 0x3d38
-  __DATA.__bss: 0x11b30
-  __DATA.__common: 0x618
+  __DATA.__data: 0x3c58
+  __DATA.__bss: 0x11ab0
+  __DATA.__common: 0x5e8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5611
-  Symbols:   280
-  CStrings:  697
+  Functions: 5193
+  Symbols:   287
+  CStrings:  678
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getFunctionTypeMetadata0
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x10
- _objc_release_x9
- _objc_retain_x10
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
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
