## ManagedSettingsUI

> `/System/Library/Frameworks/ManagedSettingsUI.framework/ManagedSettingsUI`

```diff

-140.0.0.0.0
-  __TEXT.__text: 0x59d0
+150.0.0.0.0
+  __TEXT.__text: 0x5a20
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0xac
   __TEXT.__const: 0x22e
-  __TEXT.__cstring: 0x53c
+  __TEXT.__cstring: 0x7cc
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0x179
   __TEXT.__swift5_fieldmd: 0x10c

   __TEXT.__unwind_info: 0x148
   __TEXT.__objc_methname: 0x369
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x180
   __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x50
   __AUTH_CONST.__const: 0x2a8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__auth_got: 0x368
   __AUTH.__data: 0x50
   __AUTH.__objc_data: 0x1d0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x50
   __DATA.__objc_data: 0x68
   __DATA.__data: 0xb0
   __DATA.__common: 0x18

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 128
-  Symbols:   187
-  CStrings:  50
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 130
+  Symbols:   188
+  CStrings:  64
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_ManagedSettingsUI
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_ManagedSettingsUI
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
CStrings:
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "invalid Collection: less than 'count' elements in collection"

```
