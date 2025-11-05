## SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

-342.3.1.0.0
-  __TEXT.__text: 0x7bd9c
-  __TEXT.__auth_stubs: 0x1aa0
+342.4.4.0.0
+  __TEXT.__text: 0x7bccc
+  __TEXT.__auth_stubs: 0x1a50
   __TEXT.__objc_stubs: 0x440
-  __TEXT.__objc_methlist: 0x674
-  __TEXT.__cstring: 0x2fe3
+  __TEXT.__objc_methlist: 0xa94
+  __TEXT.__const: 0x3e36
+  __TEXT.__cstring: 0x2b33
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x3ec6
   __TEXT.__constg_swiftt: 0x1fb0
-  __TEXT.__swift5_typeref: 0x1c36
+  __TEXT.__swift5_typeref: 0x1c2e
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_reflstr: 0xe2a
   __TEXT.__swift5_fieldmd: 0x1310

   __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_capture: 0xa68
   __TEXT.__oslogstring: 0x2b91
-  __TEXT.__unwind_info: 0x1ec8
-  __TEXT.__eh_frame: 0x11b4
-  __DATA_CONST.__auth_got: 0xd58
+  __TEXT.__unwind_info: 0x1e88
+  __TEXT.__eh_frame: 0x1224
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__auth_ptr: 0x638
-  __DATA_CONST.__const: 0x4098
+  __DATA_CONST.__auth_ptr: 0x6d0
+  __DATA_CONST.__const: 0x40c0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x3158
-  __DATA.__objc_selrefs: 0x738
+  __DATA.__objc_const: 0x29b0
+  __DATA.__objc_selrefs: 0x7b0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1420
-  __DATA.__data: 0x34c0
+  __DATA.__data: 0x34e0
   __DATA.__bss: 0x55a8
   __DATA.__common: 0x118
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftCoreMediaIO.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9A5EAA74-D446-3B4E-BD84-CF8F9429BB4F
-  Functions: 3458
-  Symbols:   743
-  CStrings:  923
+  UUID: ACC9F6E1-8B86-3F9B-96D5-7703C3A0F78F
+  Functions: 3470
+  Symbols:   739
+  CStrings:  896
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "342.4.4"
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
