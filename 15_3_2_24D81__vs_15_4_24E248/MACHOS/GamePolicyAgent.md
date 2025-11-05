## GamePolicyAgent

> `/usr/libexec/GamePolicyAgent`

```diff

-2.2.1.0.0
-  __TEXT.__text: 0xe9e0
-  __TEXT.__auth_stubs: 0xb80
+2.4.2.0.0
+  __TEXT.__text: 0xdf4c
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x27c
+  __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0x3e8
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__objc_classname: 0xc0
   __TEXT.__objc_methname: 0x9e2
   __TEXT.__objc_methtype: 0x1f0
-  __TEXT.__cstring: 0xc81
+  __TEXT.__cstring: 0x971
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x400
   __TEXT.__swift5_typeref: 0x2ab

   __TEXT.__swift5_protos: 0x4
   __TEXT.__unwind_info: 0x2c8
   __TEXT.__eh_frame: 0x1f8
-  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__const: 0x4c8
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xfb0
-  __DATA.__objc_selrefs: 0x298
+  __DATA.__objc_const: 0xd48
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0x6d8
+  __DATA.__objc_data: 0x650
   __DATA.__data: 0x5f8
   __DATA.__bss: 0x390
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AA95ECE1-06F5-3D02-8BFF-AF9405427B6D
+  UUID: 2C23B3F0-3441-37E6-9CB0-36BF59D7F035
   Functions: 221
-  Symbols:   302
-  CStrings:  299
+  Symbols:   298
+  CStrings:  283
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
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
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
