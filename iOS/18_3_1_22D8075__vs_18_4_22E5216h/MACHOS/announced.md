## announced

> `/usr/libexec/announced`

```diff

-248.30.3.0.0
-  __TEXT.__text: 0x121c
-  __TEXT.__auth_stubs: 0x390
+248.40.28.0.0
+  __TEXT.__text: 0x101c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x52
-  __TEXT.__cstring: 0x290
+  __TEXT.__cstring: 0x39
   __TEXT.__objc_methname: 0x77
   __TEXT.__oslogstring: 0x154
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x10
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x38
   __DATA.__data: 0x18

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20
-  Symbols:   108
-  CStrings:  30
+  Functions: 21
+  Symbols:   99
+  CStrings:  17
 
Symbols:
+ _objc_retain_x8
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x28
- _swift_arrayDestroy
CStrings:
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
