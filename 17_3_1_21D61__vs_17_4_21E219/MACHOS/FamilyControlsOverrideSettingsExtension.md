## FamilyControlsOverrideSettingsExtension

> `/System/Library/Frameworks/FamilyControls.framework/PlugIns/FamilyControlsOverrideSettingsExtension.appex/FamilyControlsOverrideSettingsExtension`

```diff

-1131.0.0.0.0
-  __TEXT.__text: 0x2074
-  __TEXT.__auth_stubs: 0x390
+1150.1.0.0.0
+  __TEXT.__text: 0x23c8
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__const: 0x102
   __TEXT.__swift5_typeref: 0x79
-  __TEXT.__cstring: 0x274
+  __TEXT.__cstring: 0x510
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methname: 0x1b
   __TEXT.__swift5_fieldmd: 0x2c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x1c8
+  __TEXT.__unwind_info: 0xbc
+  __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x70
   __DATA.__objc_selrefs: 0x10

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
-  UUID: 99F76551-6CA6-37B4-8474-67685BA88BFF
-  Functions: 38
-  Symbols:   64
-  CStrings:  12
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: DD892D2E-2B24-3B38-8D2E-569EF2DDFD04
+  Functions: 39
+  Symbols:   66
+  CStrings:  26
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_release_x20
- _objc_release_x22
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
