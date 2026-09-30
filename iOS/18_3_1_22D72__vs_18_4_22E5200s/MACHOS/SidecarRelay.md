## SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

-342.3.1.0.0
-  __TEXT.__text: 0x78764
-  __TEXT.__auth_stubs: 0x1b40
+342.4.3.0.0
+  __TEXT.__text: 0x71438
+  __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_stubs: 0x420
-  __TEXT.__objc_methlist: 0x6b4
-  __TEXT.__cstring: 0x31c7
+  __TEXT.__objc_methlist: 0xb24
+  __TEXT.__const: 0x43c6
+  __TEXT.__cstring: 0x2d17
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x3f7e
   __TEXT.__constg_swiftt: 0x1fbc
-  __TEXT.__swift5_typeref: 0x1be0
+  __TEXT.__swift5_typeref: 0x1bd8
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0xeea
   __TEXT.__swift5_fieldmd: 0x13c8

   __TEXT.__swift5_protos: 0x40
   __TEXT.__oslogstring: 0x2562
   __TEXT.__swift5_capture: 0x9dc
-  __TEXT.__unwind_info: 0x1e90
-  __TEXT.__eh_frame: 0x10f0
-  __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0x520
+  __TEXT.__unwind_info: 0x1d60
+  __TEXT.__eh_frame: 0x1178
+  __DATA_CONST.__auth_got: 0xd88
+  __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x6a8
-  __DATA_CONST.__const: 0x3fd0
+  __DATA_CONST.__const: 0x3fe8
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x3518
-  __DATA.__objc_selrefs: 0x768
+  __DATA.__objc_const: 0x2cd8
+  __DATA.__objc_selrefs: 0x808
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1638
-  __DATA.__data: 0x38c0
+  __DATA.__data: 0x38f0
   __DATA.__bss: 0x5698
   __DATA.__common: 0x118
   - /System/Library/Frameworks/Combine.framework/Combine

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
-  Functions: 3413
-  Symbols:   757
-  CStrings:  930
+  Functions: 3339
+  Symbols:   758
+  CStrings:  903
 
Symbols:
+ _$sSqMa
+ _objc_retain_x11
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_initStructMetadataWithLayoutString
- _$sBpWV
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x10
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "342.4.3"
- "342.3.1"
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
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
