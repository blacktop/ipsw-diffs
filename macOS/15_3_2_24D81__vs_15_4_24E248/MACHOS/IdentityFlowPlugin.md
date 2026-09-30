## IdentityFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/IdentityFlowPlugin.bundle/Contents/MacOS/IdentityFlowPlugin`

```diff

 3402.6.1.0.0
-  __TEXT.__text: 0x1358
-  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__text: 0x110c
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__const: 0xb6
-  __TEXT.__cstring: 0x378
+  __TEXT.__cstring: 0x138
   __TEXT.__constg_swiftt: 0x68
   __TEXT.__swift5_typeref: 0x35
   __TEXT.__swift5_reflstr: 0x1b

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x78
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 191243C4-AB0D-35A3-B688-8A6DB16ED7A1
+  UUID: BDBAD29A-C675-332B-B8E4-F52C1924155B
   Functions: 32
-  Symbols:   61
-  CStrings:  22
+  Symbols:   60
+  CStrings:  10
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
Functions:
~ sub_255c -> sub_1604 : 988 -> 904
~ sub_2aac -> sub_1b00 : 212 -> 204
~ sub_2b80 -> sub_1bcc : 452 -> 268
~ sub_2d44 -> sub_1cd8 : 152 -> 156
~ sub_2ddc -> sub_1d74 : 388 -> 156
~ sub_2f60 -> sub_1e10 : 104 -> 108
~ sub_2fc8 -> sub_1e7c : 340 -> 236
~ sub_311c -> sub_1f68 : 572 -> 580
~ sub_345c -> sub_22b0 : 68 -> 76
CStrings:
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
