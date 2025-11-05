## AppLaunchPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AppLaunchPlugin.bundle/Contents/MacOS/AppLaunchPlugin`

```diff

-3402.34.1.0.0
-  __TEXT.__text: 0x21b0
-  __TEXT.__auth_stubs: 0x400
+3404.15.1.0.0
+  __TEXT.__text: 0x1e2c
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__const: 0x9a
-  __TEXT.__cstring: 0x409
+  __TEXT.__cstring: 0x109
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x1b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__oslogstring: 0xad
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
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
-  UUID: 6072723F-6136-321B-BAAE-9F37AC50F993
-  Functions: 47
-  Symbols:   67
-  CStrings:  28
+  UUID: 521EA758-03F1-3FF9-925F-D80E1B6FCE47
+  Functions: 44
+  Symbols:   68
+  CStrings:  13
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_arrayDestroy
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
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
