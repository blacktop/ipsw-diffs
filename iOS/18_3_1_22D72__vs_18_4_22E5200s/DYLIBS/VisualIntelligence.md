## VisualIntelligence

> `/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence`

```diff

-4.3.66.0.0
-  __TEXT.__text: 0x35e6e8
-  __TEXT.__auth_stubs: 0x4b40
-  __TEXT.__objc_methlist: 0x3208
-  __TEXT.__const: 0x17808
-  __TEXT.__cstring: 0x14180
-  __TEXT.__oslogstring: 0x6a84
-  __TEXT.__gcc_except_tab: 0x3f30
+4.4.68.0.0
+  __TEXT.__text: 0x2e1080
+  __TEXT.__auth_stubs: 0x4bb0
+  __TEXT.__objc_methlist: 0x43dc
+  __TEXT.__const: 0x188d4
+  __TEXT.__cstring: 0x13d80
+  __TEXT.__oslogstring: 0x6b54
+  __TEXT.__gcc_except_tab: 0x3ed8
   __TEXT.__constg_swiftt: 0x71b4
-  __TEXT.__swift5_typeref: 0x5da5
+  __TEXT.__swift5_typeref: 0x5ce7
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_reflstr: 0x66d8
   __TEXT.__swift5_fieldmd: 0x75d0

   __TEXT.__swift5_proto: 0x1460
   __TEXT.__swift5_types: 0x7e8
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__swift5_capture: 0x1570
+  __TEXT.__swift5_capture: 0x15dc
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xa000
-  __TEXT.__eh_frame: 0xcfb4
+  __TEXT.__unwind_info: 0x8ea0
+  __TEXT.__eh_frame: 0xcddc
   __TEXT.__objc_classname: 0x84a
   __TEXT.__objc_methname: 0x9d8c
   __TEXT.__objc_methtype: 0x2367
   __TEXT.__objc_stubs: 0x4100
-  __DATA_CONST.__got: 0x1230
+  __DATA_CONST.__got: 0x1270
   __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x670
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a80
+  __DATA_CONST.__objc_selrefs: 0x1e58
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x25b8
-  __AUTH_CONST.__auth_ptr: 0x1730
-  __AUTH_CONST.__const: 0xf8a8
+  __AUTH_CONST.__auth_got: 0x25f0
+  __AUTH_CONST.__auth_ptr: 0x14b8
+  __AUTH_CONST.__const: 0xf938
   __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x12760
+  __AUTH_CONST.__objc_const: 0x10528
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x500
-  __AUTH.__data: 0x540
+  __AUTH.__objc_data: 0x460
+  __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x544
-  __DATA.__data: 0x37a0
-  __DATA.__bss: 0x19530
-  __DATA.__common: 0x778
-  __DATA_DIRTY.__objc_data: 0x2618
-  __DATA_DIRTY.__data: 0xdda8
-  __DATA_DIRTY.__bss: 0xbca0
-  __DATA_DIRTY.__common: 0x818
+  __DATA.__data: 0x3338
+  __DATA.__bss: 0x184b0
+  __DATA.__common: 0x708
+  __DATA_DIRTY.__objc_data: 0x26b8
+  __DATA_DIRTY.__data: 0xe898
+  __DATA_DIRTY.__bss: 0xcd20
+  __DATA_DIRTY.__common: 0x838
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12894
-  Symbols:   3689
-  CStrings:  4684
+  Functions: 11596
+  Symbols:   3735
+  CStrings:  4665
 
Symbols:
+ __ZNSt13exception_ptr31__from_native_exception_pointerEPv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___cxa_init_primary_exception
+ _memset_pattern16
+ _sqrt
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
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __ZNKSt9exception4whatEv
- _fmod
- _fmodf
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
CStrings:
+ "parseCameraFrame: No supported domain for lanuage: %s"
+ "parseCameraFrame: No supported domain when missing language identifier"
+ "parseCameraFrame: input domain count %ld, domains: %s for language: %s"
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
